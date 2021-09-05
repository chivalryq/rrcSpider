import csv


def main():
    with open('car.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            info_list = row['model'].split('_', maxsplit=2)
            if len(info_list) == 3:
                info_list[2] = info_list[2].replace('_', ' ')
            print(
                f'''update car.car set model = '{info_list[0]}', year = '{info_list[1]}', version = '{info_list[2]}' where id = {row['id']};''')


if __name__ == '__main__':
    main()
