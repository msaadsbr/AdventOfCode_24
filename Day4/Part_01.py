def possible_outcomes(line, i, j):
    cnt = 0
    
    try:
        hori = line[i][j:j + 4]
        cnt += 1 if hori == code or hori[::-1] == code else 0
    except: pass

    try:  
        vert = str(line[i][j] + line[i + 1][j + 1] + line[i + 2][j + 2] + line[i + 3][j + 3])
        cnt += 1 if vert == code or vert[::-1] == code else 0
    except: pass

    try: 
        if j >= 3:
            non_diag = str(line[i][j] + line[i + 1][j - 1] + line[i + 2][j - 2] + line[i + 3][j - 3])
            cnt += 1 if non_diag == code or non_diag[::-1] == code else 0
    except: pass

    try:
        diag = str(line[i][j] + line[i + 1][j] + line[i + 2][j] + line[i + 3][j])
        cnt += 1 if diag == code or diag[::-1] == code else 0
    except: pass

    return cnt  

c = 0

code = "XMAS"

with open("input.txt", "r") as f:
    lines = f.readlines()

    for i in range(len(lines)):
        for j in range(len(lines[i].strip())):  

            c += possible_outcomes(lines, i, j)

print(c)
