def disc(mp):
    new_map = []
    for i in range(len(mp)) :
        new_map.extend([str((i // 2))] * int(mp[i]) if i & 1 == 0 else ["."] * int(mp[i]))
    return new_map

def update_disc(new_map):
    i = len(new_map)-1
    while "." in new_map[:i+1]:
        if new_map[i]!=".":
            doti = new_map[:i+1].index(".")
            new_map[i], new_map[doti] = new_map[doti], new_map[i]
        i -= 1
    return new_map


with open("input.txt", "r") as f:
    mp = f.readline()
    if len(mp)&1==0: mp = mp[:-1]
    # print(mp)
    mp = disc(mp)
    print(mp)
    new_map = update_disc(mp)
    i, sm = 0, 0
    while new_map[i]!=".":
        sm += i*int(new_map[i])
        i += 1
    print(sm)
    # print(new_map)