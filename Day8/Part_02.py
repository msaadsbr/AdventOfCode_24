






def solve(lines, si, sj, fi, fj):
    upperline = fi - abs(si - fi)
    lowerline = si + abs(si - fi)
    if sj<fj:
        upperind = fj + abs(sj - fj)
        lowerind = sj - abs(sj - fj)
        while upperline > -1 and -1 < upperind < len(lines[0]) :
            lines[upperline][upperind][1] = "#"
            upperline -= upperline
            upperind = upperind + abs(fj - upperind)
            fj = upperind
        while lowerline < len(lines) and -1 < lowerind < len(lines[0]) :
            lines[lowerline][lowerind][1] = "#"
            lowerline += lowerline
            lowerind = lowerind - abs(fj - lowerind)
            fj = lowerind
    else:
        upperind = fj - abs(sj - fj)
        lowerind = sj + abs(sj - fj)
        while upperline > -1 and -1 < upperind < len(lines[0]) :
            lines[upperline][upperind][1] = "#"
            upperline -= upperline
            upperind = upperind - abs(fj - upperind)
            fj = upperind
        while lowerline < len(lines) and -1 < lowerind < len(lines[0]) :
            lines[lowerline][lowerind][1] = "#"
            lowerline += lowerline
            lowerind = lowerind + abs(fj - lowerind)
            fj = lowerind



with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in range(len(lines)):
        lines[line] = [[i,""] for i in lines[line].strip()]

    for fi in range(len(lines)):
        for fj in range(len(lines[0])):
            if lines[fi][fj][0]!=".":
                for si in range(fi, len(lines)):
                    for sj in range(len(lines[0])):
                        if (fi != si and fj != sj) and lines[si][sj][0] == lines[fi][fj][0] :
                            solve(lines, si, sj, fi, fj)
    c = 0

    for line in lines:
        for part in line:
            if part[1]=="#": c += 1
    print(lines)
    print(c)