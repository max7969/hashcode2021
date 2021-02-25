from model import *
import random as rd

def process(plan):
    streets = plan.streets 
    intersections = []

    street_importance = {}

    street_map = {}
    for street in plan.streets:
        street_map[street.name] = 0


    for car in plan.cars:
        for car_street in car.streets:
            street_map[car_street] += 1
            
    for intersection_n in range(plan.nb_intersection):
        count = 0
        lights = []
        for street in streets:
            if street.end == intersection_n:
                count = count + 1
                lights.append(Light(street.name, ((street_map[street.name] / 100) + 1) * rd.randint(1, 5)))
        intersections.append(Intersection(intersection_n, count, lights))
    return Output(plan.nb_intersection, intersections)