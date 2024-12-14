with open("input.txt", "r") as f:
    lines = f.readlines()

    pv = []
    for line in lines:
        pos, v = list(map(int, (line.split("="))[1][:-2].split(","))), list(map(int, line.split("=")[2].strip().split(",")))
        pv.append([pos,v])

    sec = 1
    while True:
        visited = set()
        for p,v in pv:
            p[0] = (p[0] + v[0]) % 101
            p[1] = (p[1] + v[1]) % 103
            visited.add((p[0], p[1]))
        if len(visited)==len(pv):
            break
        sec += 1

    print(sec)

