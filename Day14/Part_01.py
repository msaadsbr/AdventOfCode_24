with open("input.txt", "r") as f:
    lines = f.readlines()
    q1, q2, q3, q4 = 0, 0, 0, 0
    for line in lines:

        pos, v = list(map(int, (line.split("="))[1][:-2].split(","))), list(map(int, line.split("=")[2].strip().split(",")))
        newx, newy = (pos[1]+100*(v[1]))%103, (pos[0]+100*(v[0]))%101

        if newx==103//2 or newy==101//2: continue
        if newx<103//2:
            if newy<101//2: q1 += 1
            else: q2 += 1
        else:
            if newy<101//2: q3 += 1
            else: q4 += 1

    print(q1*q2*q3*q4)
