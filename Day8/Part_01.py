def solve(lines, si, sj, fi, fj):
    if (fi != si and fj != sj) and lines[si][sj][0] == lines[fi][fj][0] :
        tempi, tempj = si, sj
        temp1i, temp1j = fi, fj
        print()
        difi = si-fi
        difj = fj-si
        while (si - difi)>-1 and -1<( sj + difj)<len(lines[0]):
            lines[si-(difi)][sj+(difj)][1] = "#"
            si -= difi
            sj += difj
        si, sj, fi, fj = tempi, tempj, temp1i, temp1j
        difi = si - fi
        difj = fj - si
        while (si + difi)<len(lines) and -1<(sj - difj)<len(lines[0]) :
            lines[si + (difi)][sj-(difj)][1] = "#"
            si += difi
            sj -= difj



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
    print(lines)
    print(c)