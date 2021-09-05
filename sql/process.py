import csv

from sql.sql_generator import Car
from sql.util import get_cars


class PredictCar(object):
    def __init__(self, c: Car):
        self.price = c.price
        self.regDate = c.regDate
        self.original_price = c.original_price
        self.mileage = c.mileage
        self.name = c.name

    def __str__(self):
        return "\n".join(["{}:{}".format(i, self.__dict__[i]) for i in self.__dict__]) + "\n--------"


def get_process_data():
    cars = get_cars()
    p_cars = [PredictCar(c) for c in cars]
    return p_cars


def main():
    cars = get_process_data()
    keys = ['price', 'regDate', 'original_price', 'mileage', 'name']
    with open('predict_data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        for car in cars:
            d = {}
            for key in keys:
                d[key] = getattr(car, key, None)
            writer.writerow(d)
    # print("example data:")
    # print(cars[0])


if __name__ == '__main__':
    main()
