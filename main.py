from read_input import read_input
from write_output import write_output
from process import process

plan_a = read_input("a.txt")
plan_b = read_input("b.txt")
plan_c = read_input("c.txt")
plan_d = read_input("d.txt")
plan_e = read_input("e.txt")
plan_f = read_input("f.txt")

out_a = process(plan_a)
out_b = process(plan_b)
out_c = process(plan_c)
out_d = process(plan_d)
out_e = process(plan_e)
out_f = process(plan_f)

write_output(out_a, "out_a")
write_output(out_b, "out_b")
write_output(out_c, "out_c")
write_output(out_d, "out_d")
write_output(out_e, "out_e")
write_output(out_f, "out_f")
