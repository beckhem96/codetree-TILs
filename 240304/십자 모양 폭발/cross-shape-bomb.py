n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
dis, djs = [1, -1, 0, 0], [0, 0, 1, -1]
tmp = [[0] * n for _ in range(n)]

def bumb(i, j):
    bumb_range = arr[i][j]
    arr[i][j] = 0
    if (bumb_range == 1):
        return 
    else:
        for br in range(1, bumb_range):
            for si, sj in zip(dis, djs):
                di, dj = i + (si * br), j + (sj * br)

                if (0<=di<n and 0<=dj<n):
                    arr[di][dj] = 0
bumb(r-1, c-1)

for j in range(n):
    tmp_i = n-1
    for i in range(n-1, -1, -1):
        if (arr[i][j] != 0):
            tmp[tmp_i][j] = arr[i][j]
            tmp_i -= 1

for i in range(n):
    for j in range(n):
        print(tmp[i][j], end=" ")
    print()