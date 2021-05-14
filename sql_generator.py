import datetime
import json
import logging
import re
from dataclasses import dataclass
from typing import Dict

datetime_format = '%Y-%m-%d %H:%M:%S'


def get_first_number(s: str) -> float:
    try:
        return float(re.findall(r"[-+]?\d*\.\d+|\d+", s)[0])
    except IndexError:
        logging.info(f"failed to find number: {s}")
        return 0.0


@dataclass
class Car(object):
    name: str = None
    regDate: str = datetime.datetime.now().strftime(datetime_format)
    model: str = None
    brand: str = None
    bodyType: str = None
    fuelType: str = None
    gearbox: str = None
    power: str = None
    mileage: float = 0.0
    notRepaired: int = None
    regionCode: int = None
    seller: str = None
    offerType: str = None
    createDate: int = None
    price: float = 0.0
    ownerId: int = None
    isReadable: bool = None
    description: str = None

    def __init__(self, data: Dict):
        super(Car, self).__init__()
        for key, val in data.items():
            if hasattr(self, key):
                if isinstance(getattr(self, key), float):
                    val = get_first_number(val)
                setattr(self, key, val)

        try:
            info_list = self.name.split('-', maxsplit=1)
            self.brand = info_list[0]
            self.model = info_list[1]
        except IndexError:
            pass

        try:
            reg_date = re.findall(r'\d+', data['car_buy_time'])
            year, month = int(reg_date[0]), int(reg_date[1])
            date_time = datetime.datetime(year=year, month=month, day=1)
            self.regDate = date_time.strftime(datetime_format)
        except IndexError:
            pass

    def gen_sql(self) -> str:
        key_val_map = {}
        for key, val in self.__dict__.items():
            if val is None:
                val = 'NULL'
            elif isinstance(val, int) or isinstance(val, float):
                val = str(val)
            elif isinstance(val, str):
                val = f"'{val}'"
            elif isinstance(val, bool):
                val = str(val).lower()
            key_val_map[f'"{key}"'] = val
        return f'''INSERT INTO car.car ({', '.join(key_val_map.keys())}) VALUES ({', '.join(key_val_map.values())});
        '''


if __name__ == '__main__':
    result_json = open('./result.json', 'r', encoding='utf-8')
    result_dict = json.loads(
        f'''{{
        "data": {''.join(result_json.readlines())}
        }}''')
    for item in result_dict['data']:
        car = Car(item)
        print(car.gen_sql())
