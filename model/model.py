from typing import List, Tuple

import lightgbm as lgb
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn import linear_model
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

from sql.hbase import get_data_from_hbase


def res_statistic(data):
    print('_min', np.min(data))
    print('_max:', np.max(data))
    print('_mean', np.mean(data))
    print('_ptp', np.ptp(data))
    print('_std', np.std(data))
    print('_var', np.var(data))


def build_model_lr(x_train, y_train):
    reg_model = linear_model.LinearRegression()
    reg_model.fit(x_train, y_train)
    return reg_model


def build_model_ridge(x_train, y_train):
    reg_model = linear_model.Ridge(alpha=0.8)  # alphas=range(1,100,5)
    reg_model.fit(x_train, y_train)
    return reg_model


def build_model_lasso(x_train, y_train):
    reg_model = linear_model.LassoCV()
    reg_model.fit(x_train, y_train)
    return reg_model


def build_model_gbdt(x_train, y_train):
    estimator = GradientBoostingRegressor(loss='ls', subsample=0.85, max_depth=5, n_estimators=100)
    param_grid = {
        'learning_rate': [0.05, 0.08, 0.1, 0.2],
    }
    gbdt = GridSearchCV(estimator, param_grid, cv=3)
    gbdt.fit(x_train, y_train)
    print(gbdt.best_params_)
    print(gbdt.best_estimator_)
    return gbdt


def build_model_xgb(x_train, y_train):
    model = xgb.XGBRegressor(n_estimators=120, learning_rate=0.08, gamma=0, subsample=0.8,
                             colsample_bytree=0.9, max_depth=5)  # , objective ='reg:squarederror'
    model.fit(x_train, y_train)
    return model


def build_model_lgb(x_train, y_train):
    estimator = lgb.LGBMRegressor(num_leaves=63, n_estimators=100)
    param_grid = {
        'learning_rate': [0.01, 0.05, 0.1],
    }
    gbm = GridSearchCV(estimator, param_grid)
    gbm.fit(x_train, y_train)
    return gbm


def parse_time_str(datetime_str: str) -> int:
    import datetime
    date = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    return (date.year - 1970) * 12 + date.month


def parse_timestamp(timestamp: int) -> int:
    return timestamp // 60 // 60 // 24 // 30


model_lgb, model_xgb, model_gbdt = lgb.LGBMRegressor(), xgb.XGBRegressor(), GradientBoostingRegressor()
model_lr = linear_model.LinearRegression()


def pre_train():
    global model_lgb, model_xgb, model_gbdt, model_lr

    csv_data = get_data_from_hbase()
    csv_data['regDate'] = csv_data['regDate'].apply(lambda x: parse_time_str(x))

    train_data = csv_data

    print('Train data shape:', train_data.shape)

    numerical_cols = train_data.select_dtypes(exclude='object').columns
    print(numerical_cols)
    categorical_cols = train_data.select_dtypes(include='object').columns
    print(categorical_cols)

    feature_cols = ['original_price', 'mileage', 'regDate']

    X_data = train_data[feature_cols]
    Y_data = train_data['price']
    X_data = X_data.fillna(-1)

    # Train and Predict
    model_gbdt = build_model_gbdt(X_data, Y_data)
    model_xgb = build_model_xgb(X_data, Y_data)
    model_lgb = build_model_lgb(X_data, Y_data)
    model_lr = build_model_lr(X_data, Y_data)


def weighted_method(val_weight_map: List[Tuple[float, float]]):
    sum_res = 0
    for val, weight in val_weight_map:
        sum_res += max(val * weight, 0.3)
    return sum_res


def predict(original_price: float, mileage: float, timestamp: int) -> float:
    data_dict = {
        'original_price': [original_price],
        'mileage': [mileage],
        'regDate': [parse_timestamp(timestamp)],
    }
    x_val = pd.DataFrame.from_dict(data_dict)
    val_gbdt = model_gbdt.predict(x_val)
    val_xgb = model_xgb.predict(x_val)
    val_lgb = model_lgb.predict(x_val)
    val_lr = model_lr.predict(x_val)
    weight_map = [
        (val_lr, 0.1),
        (val_gbdt[0], 0.3),
        (val_xgb[0], 0.3),
        (val_lgb[0], 0.3),
    ]
    val_predict = weighted_method(weight_map)
    return val_predict


def main():
    pre_train()
    res = predict(10, 5, 500)
    print(res)


if __name__ == '__main__':
    main()
