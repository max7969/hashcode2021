

def read_input(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    return lines
