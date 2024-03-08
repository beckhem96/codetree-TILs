import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0] * n for _ in range(n)]
bumb_loc = [(int(input()) -1)  for _ in range(m)]
dis, djs = [1, -1, 0, 0], [0, 0, -1, 1]

def clean():
    global arr
    for j in range(n):
        for i in range(n-1, -1, -1):
            if (arr[i][j] != 0):
                tmp[i][j] = arr[i][j]
            elif (arr[i][j] == 0 and (i-1) >= 0 and arr[i-1][j] != 0):
                    tmp[i][j] = arr[i-1][j]
                    arr[i-1][j] = 0
            elif (arr[i][j] == 0 and (i-1) >= 0 and arr[i-1][j] == 0):
                tmp[i][j] = 0
            elif (arr[i][j] == 0 and (i-1) < 0):
                tmp[i][j] = 0
    arr = copy.deepcopy(tmp)

def bumb(i, j):
    bumb_range = arr[i][j]
    for r in range(bumb_range):
        for di, dj in zip(dis, djs):
            ni, nj = i + di * r, j + dj * r
            if(0<=ni<n and 0<=nj<n):
                arr[ni][nj] = 0
    clean()
    




for j in range(m):
    for i in range(n):
        if (arr[i][bumb_loc[j]] != 0):
            bumb(i, bumb_loc[j])
            break
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()