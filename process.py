from model import *

def process(plan):
    streets = plan.streets 
    intersections = []

    street_importance = {}
    for street in streets:
        count = 0
        
        for car in plan.cars:
            count += len([car_street for car_street in car.streets if car_street == street.name])
            #for car_street in car.streets:
            #    if car_street == street.name:
            #        count = count + 1
        street_importance[street.name] = count
        
    # time_path = {}
    

    for intersection_n in range(plan.nb_intersection):
        count = 0
        lights = []
        for street in streets:
            if street.end == intersection_n:
                count = count + 1
                lights.append(Light(street.name, street_importance[street.name] + 1))
        intersections.append(Intersection(intersection_n, count, lights))
    return Output(plan.nb_intersection, intersections)