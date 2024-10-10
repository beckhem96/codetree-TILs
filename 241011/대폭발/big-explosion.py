import copy

n, m, r, c = map(int, input().split())
arr1 = [[0 for _ in range(n)] for _ in range(n)]
arr2 = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
arr1[r-1][c-1], arr2[r-1][c-1] = 1, 1
result = 0
def put_bomb(x, y, t):
    for dx, dy in zip(dxs, dys):
        nx, ny = dx*t + x, dy*t + y
        if  0 <= nx < n and 0 <= ny < n:
            arr2[nx][ny] = 1

for tm in range(1, m+1):
    t = 2**(tm-1)
    for x in range(n):
        for y in range(n):
            if(arr1[x][y] == 1):
                put_bomb(x, y, t)
    
    arr1 = copy.deepcopy(arr2)
for i in range(n):
    for j in range(n):
        if (arr2[i][j] == 1):
            result += 1

print(result)