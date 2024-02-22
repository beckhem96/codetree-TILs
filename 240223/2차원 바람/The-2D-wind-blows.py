import copy
import math

n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp_arr = [[0] * m for _ in range(n)]
dis, djs = [1, -1, 0, 0], [0, 0, -1, 1]

def cal_average(i, j):
    tmp_sum = arr[i][j]
    cnt = 1
    for t in range(4):
        di, dj = dis[t], djs[t]
        si, sj = di + i, dj + j
        if (0<=si<n and 0<=sj<m):
            cnt += 1
            tmp_sum += arr[si][sj]
    return math.trunc(tmp_sum / cnt)

def move(r1, c1, r2, c2):
    global arr
    tmp1, tmp2, tmp3, tmp4 = arr[r1][c1], arr[r1][c2], arr[r2][c1], arr[r2][c2]

    for i in range(r1, r2):
        arr[i][c1] = arr[i + 1][c1]
    for i in range(r2, r1, -1):
        arr[i][c2] = arr[i - 1][c2]
    for i in range(c2, c1+1, -1):
        arr[r1][i] = arr[r1][i - 1]
    for i in range(c1, c2-1):
        arr[r2][i] = arr[r2][i + 1]
    arr[r1][c1+1], arr[r2][c2-1] = tmp1, tmp4

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            tmp_arr[i][j] = cal_average(i, j)
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            arr[i][j] = tmp_arr[i][j]
    
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    move(r1-1, c1-1, r2-1, c2-1)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()