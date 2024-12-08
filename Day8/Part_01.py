def solve(lines, si, sj, fi, fj):
    if (fi != si and fj != sj) and lines[si][sj][0] == lines[fi][fj][0] :
        upperline = fi - abs(si - fi)
        lowerline = si + abs(si - fi)
        upperind = fj + abs(sj - fj) if sj < fj else fj - abs(sj - fj)
        lowerind = sj - abs(sj - fj) if sj < fj else sj + abs(sj - fj)

        if upperline > -1 and upperind > -1 :
            try :
                lines[upperline][upperind][1] = "#"

            except :
                pass
        if lowerline > -1 and lowerind > -1 :
            try :
                lines[lowerline][lowerind][1] = "#"
            except :
                pass


with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in range(len(lines)):
        lines[line] = [[i,""] for i in lines[line].strip()]

    for fi in range(len(lines)):
        for fj in range(len(lines[0])):
            if lines[fi][fj][0]!=".":
                for si in range(fi, len(lines)):
                    for sj in range(len(lines[0])):
                        solve(lines, si, sj, fi, fj)
    c = 0

    for line in lines:
        for part in line:
            if part[1]=="#": c += 1
    # print(lines)
    print(c)
