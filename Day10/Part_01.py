def solve(lines, i, j, elmt, st):
    if elmt==9: st.add((i,j)); return 1
    first = solve(lines, i-1, j, elmt+1, st) if (i > 0 and lines[i-1][j]==elmt+1) else 0
    second = solve(lines, i+1, j, elmt+1, st) if (i < len(lines)-1 and lines[i+1][j]==elmt+1) else 0
    third = solve(lines, i, j-1, elmt+1, st) if (j > 0 and lines[i][j-1]==elmt+1) else 0
    fourth = solve(lines, i, j+1, elmt+1, st) if (j < len(lines[0])-1 and lines[i][j+1]==elmt+1) else 0
    return first + second + third + fourth


with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = list(map(int, list(lines[i].strip())))
    c = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]==0:
                new = set()
                solve(lines,i,j,0, new)
                c += len(new)
    print(c)