
## Not Optimize

from math import inf

with open("input.txt", "r") as f:
    lines = f.readlines()
    queries = []
    querie = []
    for line in lines:
        if line != "\n":
            part1, part2 = line[line.index("X"):].split(",")
            x, y = int(part1[2:]), int(part2[3:])
            querie.append([x,y])
        else: queries.append(querie); querie = []
    score = 0
    for querie in queries:

        ans = []
        x1, y1, x2, y2 = querie[0][0], querie[0][1], querie[1][0], querie[1][1]
        i = 0
        for i in range(100000000):
            j = 0
            while x1*i+x2*j<=querie[2][0] and y1*i+y2*j<=querie[2][1]:
                if x1*i+x2*j==querie[2][0] and y1*i+y2*j==querie[2][1]:
                    ans.append((i,j))
                j += 1
        mn = inf
        for i,j in ans: mn = min(mn, j+3*i)
        if mn==inf: continue
        else:score += mn
    print(score)
