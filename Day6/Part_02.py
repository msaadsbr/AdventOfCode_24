import sys
sys.setrecursionlimit(10**6)

def start(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] not in ["#","."]: return (i,j)

def move(dir):
    if dir==">": return (0,1)
    if dir=="<": return (0,-1)
    if dir=="v": return (1,0)
    if dir=="^": return (-1,0)

def check(mat, i, j):
    if mat[i][j]=="#": return True
    return False

def inner_check(mat1, i, j, req_dir):
    p = move(req_dir)
    while True:
        if i == -1 or j == -1 or i == len(mat1) or j == len(mat1[0]) : return False
        if type(mat1[i][j])==list and mat1[i][j][1]==req_dir: return True
        i += p[0]; j += p[1]


def dic(arrow):
    return {">":"v", "v":"<", "<":"^", "^":">"}[arrow]

def solve(mat, i, j, direction):
    if i==-1 or j==-1 or i==len(mat) or j==len(mat[0]): return 0

    flag = False
    if check(mat, i, j):
        mc1 = move(direction)
        direction = dic(direction)
        mc2 = move(direction)
        return solve(mat, i-mc1[0]+mc2[0], j-mc1[1]+mc2[1], direction)


    mc = move(direction)
    if inner_check(mat, i, j, dic(direction)): flag = True; print(i,j)
    mat[i][j] = ["X",direction]
    return int(flag) + solve(mat, i+mc[0], j+mc[1], direction)



with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)): lines[i] = list(lines[i].strip())
    glb = lines.copy()
    st = start(lines)
    lines[st[0]][st[1]] = ["X", lines[st[0]][st[1]]]
    ans = solve(lines,st[0], st[1], lines[st[0]][st[1]][1])
    print(lines)
    print(ans)