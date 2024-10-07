n, m ,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dis, djs = [0, 1, 0], [-1, 0, 1]
flag = False
def check(i, j):
    for di, dj in zip(dis, djs):
        ni, nj = di + i, dj + j
        if (0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1):
            return True;
    return False   
for i in range(n):
    if (not flag):
        for j in range(k-1, k+m):
            if (i == n-1):
                arr[i][j] = 1
            else:
                if (check(i, j)):
                    flag = True
                    break
    else:
        for j in range(k-1, k+m):
            arr[i][j] = 1
        break 

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()