from model import Street
from model import Car
from model import Plan

def read_input(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()


    elements = lines[0].split(" ")

    duration = int(elements[0])
    n_intersections = int(elements[1])
    n_streets = int(elements[2])
    n_cars = int(elements[3])
    bonus = int(elements[4])

    streets = []
    cars = []

    for line in lines[1:1+n_streets]:
        line = line.replace('\n', '')
        split_street = line.split(" ")
        streets.append(Street(int(split_street[0]), int(split_street[1]), split_street[2], int(split_street[3])))

    for line in lines[1+n_streets+1:(1+n_streets+n_cars)]:
        line = line.replace('\n', '')
        split_car = line.split(" ")
        cars.append(Car(int(split_car[0]), split_car[1:]))

    return Plan(duration, n_intersections, n_streets, n_cars, bonus, streets, cars)
