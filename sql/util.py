import json

from sql.sql_generator import Car


def keep(car: Car) -> bool:
    if car.price == 0.0:
        return False
    if car.original_price == -1:
        return False
    return True


def get_cars():
    result_json = open('../result.json', 'r', encoding='utf-8')
    result_dict = json.loads(
        f'''{{
        "data": {''.join(result_json.readlines())}
        }}''')
    primary_id = 1
    cars = []
    for item in result_dict['data']:
        car = Car(item, primary_id)
        primary_id += 1
        cars.append(car)
    # Warn: id won't be continues if filtered
    return [x for x in filter(keep, cars)]
