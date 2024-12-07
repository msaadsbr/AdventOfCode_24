def solve(arr, i, sm, target, sign):
    if i==0:
        return solve(arr, 1, sm, target, "+") or solve(arr, 1, sm, target, "*") or solve(arr, 1, sm, target, "|")

    if i==len(arr):
        return sm==target

    if sign=="|":
        return solve(arr, i+1, int(str(sm)+str(arr[i])), target, "+") or solve(arr, i+1, int(str(sm)+str(arr[i])), target, "*") or solve(arr, i+1, int(str(sm)+str(arr[i])), target, "|")

    if sign=="+":
        return solve(arr, i+1, sm+arr[i], target, "+") or solve(arr, i+1, sm+arr[i], target, "*") or solve(arr, i+1, sm+arr[i], target, "|")

    if sign=="*":
        return solve(arr, i+1, sm*arr[i], target, "+") or solve(arr, i+1, sm*arr[i], target, "*") or solve(arr, i+1, sm*arr[i], target, "|")

with open("input.txt", "r") as f:
    lines = f.readlines()
    sm = 0

    for line in lines:
        target, arr = line.split(":")
        target, arr = int(target), list(map(int, arr.strip().split()))
        if solve(arr, 0, arr[0], target, ""): sm += target

    print(sm)