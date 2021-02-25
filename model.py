class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_obj(self):
        print("x: {} , y: {}".format(self.x,self.y))

    def to_string(self):
        return "x: {} , y: {}".format(self.x,self.y)
