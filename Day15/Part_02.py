def update_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        inn = ""
        for j in range(len(grid[0])):
            if grid[i][j]=="#": inn += "##"
            elif grid[i][j]=="O": inn += "[]"
            elif grid[i][j]==".": inn += ".."
            else: inn += "@."
        new_grid.append(list(inn))
    return new_grid


def get_initial_pos(grid):
    for i in range(len(grid)):
        if "@" in grid[i]: return (i,grid[i].index("@"))


def do_x_move(grid, curi, curj, j):
    strt = (curi, curj)
    if grid[curi][curj +j] == ".":
        grid[curi][curj +j] = "@"
        grid[curi][curj] = "."
        return curi , curj +j
    if grid[curi][curj +j] == "#": return curi, curj

    while len(grid) - 2 > curi > 1 and len(grid[0]) - 2 > curj > 1 :
        if grid[curi][curj] == "." or grid[curi][curj] == "#": break
        curj += j
    chng = {"[":"]", "]":"["}
    st = "["
    if grid[curi][curj] == ".":
        for i in range(curj,strt[1],-j):
            print((curi,i), end=" ")
            grid[curi][i] = st
            st = chng[st]
        print()
        grid[strt[0]][strt[1]+j] = "@"
        grid[strt[0]][strt[1]] = "."
        return strt[0], strt[1] +j
    return strt





def do_y_move(grid, curi, curj, i):
    strt = (curi,curj)
    if grid[curi+i][curj]==".":
        grid[curi+i][curj] = "@"
        grid[curi][curj] = "."
        return curi+i,curj
    if grid[curi+i][curj]=="#": return curi,curj

    ## Code For This Part Left :(

with open("input.txt", "r") as f:
    lines = f.readlines()

    moves = "".join(line for line in lines[lines.index("\n"):])
    grid = [list(line.strip()) for line in lines[:lines.index("\n")]]
    grid = update_grid(grid)
    # print(grid)

    moves = moves.replace("\n", "")
    curi, curj = get_initial_pos(grid)

    directions = {">": (0,1), "<": (0,-1), "^": (-1,0), "v": (1,0)}

    for move in moves:
        if move in [">", "<"]:
            curi, curj = do_x_move(grid, curi, curj, directions[move][1])
        else:
            curi , curj = do_y_move(grid , curi , curj , directions[move][0])
        # print(grid)
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="O": score += i*100+j
    print(score)


