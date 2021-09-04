import happybase

import sql.process

if __name__ == '__main__':
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
