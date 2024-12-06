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
    # print(i,j)
    if mat[i][j]=="#": return True
    return False

def dic(arrow):
    return {">":"v", "v":"<", "<":"^", "^":">"}[arrow]

def solve(mat, i, j, direction):
    if i==-1 or j==-1 or i==len(mat) or j==len(mat[0]): return 1

    flag = False
    if check(mat, i, j):
        mc1 = move(direction)
        direction = dic(direction)
        mc2 = move(direction)
        if mat[i][j]==".": flag = True
        return int(flag) + solve(mat, i-mc1[0]+mc2[0], j-mc1[1]+mc2[1], direction)


    mc = move(direction)
    if mat[i][j]==".": flag = True; mat[i][j] = "X"
    return int(flag) + solve(mat, i+mc[0], j+mc[1], direction)



with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)): lines[i] = list(lines[i].strip())
    st = start(lines)
    # lines[st[0]][st[1]] = "X"
    ans = solve(lines,st[0], st[1], lines[st[0]][st[1]])
    print(ans)
    print(lines)