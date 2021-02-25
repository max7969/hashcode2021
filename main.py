from read_input import read_input
from write_output import write_output
from model import Point
from process import process

lines = read_input("in.csv")

out = []

for line in lines[1:]:
    x, y = line.split(';')
    p = Point(int(x), int(y))
    p.print_obj()
    p = process(p)
    out.append(p)

write_output(out)
