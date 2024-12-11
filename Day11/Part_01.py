with open("input.txt", "r") as f:
    line = f.readline()
    line = list(map(int, line.split()))
    for i in range(25):
        j = 0
        while j<len(line):
            if line[j]==0: line[j]=1
            elif len(str(line[j]))&1==0:
                first, second = int(str(line[j])[:len(str(line[j]))//2]), int(str(line[j])[len(str(line[j]))//2:])
                line[j] = first
                line.insert(j+1,second)
                j += 1
            else:
                line[j] *= 2024
            j += 1
        # print(line)
    print(len(line))