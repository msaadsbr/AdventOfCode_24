def get_initial_pos(grid):
    for i in range(len(grid)):
        if "@" in grid[i]: return (i,grid[i].index("@"))

def do_move(grid, curi, curj, inds):
    strt = (curi,curj)
    if grid[curi+inds[0]][curj+inds[1]]==".":
        grid[curi+inds[0]][curj+inds[1]] = "@"
        grid[curi][curj] = "."
        return curi+inds[0],curj+inds[1]
    if grid[curi+inds[0]][curj+inds[1]]=="#": return curi,curj

    while len(grid)-1>curi>0 and len(grid[0])-1>curj>0:
        if grid[curi][curj]=="." or grid[curi][curj]=="#": break
        curi += inds[0]
        curj += inds[1]
    if grid[curi][curj]==".":
        grid[strt[0]+inds[0]][strt[1]+inds[1]] = "@"
        grid[strt[0]][strt[1]] = "."
        grid[curi][curj]="O"
        return strt[0]+inds[0], strt[1]+inds[1]
    return strt

with open("input.txt", "r") as f:
    lines = f.readlines()

    moves = "".join(line for line in lines[lines.index("\n"):])
    grid = [list(line.strip()) for line in lines[:lines.index("\n")]]
    moves = moves.replace("\n", "")
    curi, curj = get_initial_pos(grid)
    directions = {">": (0,1), "<": (0,-1), "^": (-1,0), "v": (1,0)}

    for move in moves:
        curi, curj = do_move(grid, curi, curj, directions[move])

    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="O": score += i*100+j
    print(score)


