
## Approach Change From First Part Solution

from collections import defaultdict
with open("input.txt", "r") as f:
    line = f.readline()
    line = list(map(int, line.split()))
    cnt = defaultdict(int)
    for num in line: cnt[num]+=1
    for _ in range(75):
        new_cnt = defaultdict(int)
        for num in cnt:
            if num == 0:
                new_cnt[1] += cnt[num]
            elif len(str(num)) % 2 == 0:
                first, second = int(str(num)[:len(str(num)) // 2]), int(str(num)[len(str(num)) // 2:])
                new_cnt[first] += cnt[num]
                new_cnt[second] += cnt[num]
            else:
                new_cnt[num*2024] += cnt[num]
        cnt = new_cnt
    # print(cnt)
    c = 0
    for num in cnt: c += cnt[num]
    print(c)
