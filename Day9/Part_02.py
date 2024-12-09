
#               It's Not Complete Yet!!

def disc(mp):
    new_map = []
    for i in range(len(mp)) :
        new_map.extend([str((i // 2))] * int(mp[i]) if i & 1 == 0 else ["."] * int(mp[i]))
    return new_map

def update_disc(new_map):
    i = len(new_map)-1
    while i>=0:
        c = 1
        while i>=0 and new_map[i]==new_map[i-1]: i-=1; c+=1
        if new_map[i]=="." or new_map[i]=="#": i -= 1; continue
        j = 0
        while j+c<i:
            if len(set(new_map[j:j+c]))==1 and new_map[j]==".":
                for k in range(j,j+c): new_map[k] = new_map[i]
                for k in range(i,i+c): new_map[k] = "."
                break
            j += 1
        i -= 1
    return new_map


with open("input.txt", "r") as f:
    mp = f.readline().strip()
    if len(mp)&1==0: mp = mp[:-1]
    mp = disc(mp)
    new_map = update_disc(mp)
    # print(new_map)
    i, sm = 0, 0
    while i<len(new_map):
        if new_map[i]!="." and new_map[i]!="#":
            sm += i*int(new_map[i])
        i += 1
    print(sm)
    # print(new_map)
