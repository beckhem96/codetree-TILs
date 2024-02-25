CCW = 0
CW = 1
import copy
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = [[0] * n for _ in range(n)]

def shift(x, y, k, l, move_dir):
    if move_dir == CCW:
        dis, djs = [-1, -1, 1, 1], [1, -1, -1, 1] 
        move_nums = [k, l, k, l]
    else: 
        dis, djs = [-1, -1, 1, 1], [-1, 1, 1, -1] 
        move_nums = [l, k, l, k]


    tmp = copy.deepcopy(arr)

    for dx, dy, move_num in zip(dis, djs, move_nums):
        for _ in range(move_num):
            nx, ny = x + dx, y + dy
            tmp[nx][ny] = arr[x][y]
            x, y = nx, ny
    for i in range(n):
        for j in range(n):
            arr[i][j] = tmp[i][j]

r, c, m1, m2, m3, m4, d = map(int, input().split())

shift(r-1, c-1, m1, m2, d)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()