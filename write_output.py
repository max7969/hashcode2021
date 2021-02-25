
def write_output(lp, file_name):
    file = open('file_name', 'w')
    
    file.write(str(lp.nb_intersection) + "\n")
    
    for intersection in lp.intersections:
        file.write(str(intersection.id) + "\n")
        file.write(str(intersection.nb_streets) + "\n")
        for light in intersection.lights:
            file.write(light.street_name + " " + str(light.duration) + "\n")
    file.close()
