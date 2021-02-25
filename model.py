class Car:
    def __init__(self, nb_street, streets):
        self.nb_street = nb_street
        self.streets = streets

class Street:
    def __init__(self, start, end, name, duration):
        self.start = start
        self.end = end
        self.name = name
        self.duration = duration
    
class Plan:
    def __init__(self, duration, nb_intersection, nb_street, nb_cars, points, streets, cars):
        self.duration = duration
        self.nb_intersection = nb_intersection
        self.nb_street = nb_street
        self.nb_cars = nb_cars
        self.points = points    
        self.streets = streets
        self.cars = cars

class Light:
    def __init__(self, street_name, duration):
        self.street_name = street_name
        self.duration = duration
    

class Intersection:
    def __init__(self, id, nb_streets, lights):
        self.id = id
        self.nb_streets = nb_streets
        self.lights = lights

class Output:
    def __init__(self, nb_intersection, intersections):
        self.nb_intersection = nb_intersection
        self.intersections = intersections

    def print_obj(self):
        print("duration : {}".format(self.duration))
        print("nb_intersection : {}".format(self.nb_intersection))
        print("nb_street : {}".format(self.nb_street))
        print("nb_cars : {}".format(self.nb_cars))
        print("points : {}".format(self.points))

