
def write_output(lp):
    file = open('out.csv', 'w')
    for p in lp:
        file.write(p.to_string())
    file.close()
