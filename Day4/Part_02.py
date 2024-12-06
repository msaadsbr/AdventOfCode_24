def check(mat, i, j):
    cond = False

    try:
        cond |= (mat[i-1][j-1] == "M" and mat[i-1][j+1] == "M" and mat[i][j] == "A" and mat[i+1][j-1] == "S" and mat[i+1][j+1] == "S")
    except: pass

    try:
        cond |= (mat[i-1][j-1] == "M" and mat[i-1][j+1] == "S" and mat[i][j] == "A" and mat[i+1][j-1] == "M" and mat[i+1][j+1] == "S")
    except: pass

    try:
        cond |= (mat[i-1][j-1] == "S" and mat[i-1][j+1] == "S" and mat[i][j] == "A" and mat[i+1][j-1] == "M" and mat[i+1][j+1] == "M")
    except: pass

    try:
        cond |= (mat[i-1][j-1] == "S" and mat[i-1][j+1] == "M" and mat[i][j] == "A" and mat[i+1][j-1] == "S" and mat[i+1][j+1] == "M")
    except: pass
    return cond

c = 0

with open("input.txt", "r") as f:
    line = f.readlines()

    for i in range(1, len(line) - 1):
        for j in range(1, len(line[i].strip()) - 1):

            if check(line, i, j):
                c += 1

print(c)
