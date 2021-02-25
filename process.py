from model import Light
from model import Intersection
from model import Output

def process(plan):
    streets = plan.streets 
    intersections = []
    
    for intersection_n in range(plan.nb_intersection):
        count = 0
        lights = []
        for street in streets:
            if street.end == intersection_n:
                count = count + 1
                lights.append(Light(street.name, 1))
        intersections.append(Intersection(intersection_n, count, lights))
    return Output(plan.nb_intersection, intersections)