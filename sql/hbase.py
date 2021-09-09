import happybase
import pandas as pd

import sql.process


def get_data_from_hbase():
    connection = happybase.Connection(host="81.70.249.193", port=9090)
    table = connection.table('car')
    data = table.scan(batch_size=1000)
    rows = []
    for row in data:
        binary_dict = row[1]
        d = {}
        for key, val in binary_dict.items():
            key_str = key.decode('utf-8').split(':')[1]
            val_str = val.decode('utf-8')
            if key_str in ['mileage', 'original_price', 'price']:
                val_str = float(val_str)
            d[key_str] = val_str
        valid = True
        for key in ['mileage', 'original_price', 'price', 'regDate']:
            if key not in d:
                valid = False
                break
        if valid:
            rows.append(d)
    df = pd.DataFrame.from_records(rows)
    print(df.head())
    return df


def write_to_hbase():
    connection = happybase.Connection(host="81.70.249.193", port=9090)
    table = connection.table('car')

    cars = sql.process.get_process_data()
    key = 0
    for car in cars:
        data = {}
        tmpl = 'info:{}'
        for k in car.__dict__:
            data[tmpl.format(k)] = str(car.__dict__[k])
        # print(data)
        table.put(str(key), data)
        key += 1
        if key % 1000 == 0:
            print("writing {} data".format(key))

    # row = table.row(b'row-key')
    # print(row[b'holy:qual1'])  # prints 'value1'
    # a = row[b'holy:qual1'].decode('utf-8')
    # print(a)
    #
    # for key, data in table.rows(['row-key-1', 'row-key-2']):
    #     print(key, data)  # prints row key and data for each row
    #
    # for key, data in table.scan(row_prefix=b'row'):
    #     print(key, data)  # prints 'value1' and 'value2'
    #
    # # row = table.delete(b'row-key')


if __name__ == '__main__':
    # write_to_hbase()
    get_data_from_hbase()
