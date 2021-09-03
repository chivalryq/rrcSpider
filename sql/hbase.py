from sql.util import get_cars

if __name__ == '__main__':
    cars = get_cars()
    print(cars[0].__dict__)
    print("\n".join(["{}:{}".format(i, cars[0].__dict__[i]) for i in cars[0].__dict__]))
