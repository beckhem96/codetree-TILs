n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
tmp1, tmp2, tmp3 = 0, 0, 0
for _ in range(t):
    tmp1, tmp2, tmp3 = arr[0][n-1], arr[1][n-1], arr[2][n-1]
    for i in range(n-1, 0, -1):
        arr[0][i], arr[1][i], arr[2][i]  = arr[0][i - 1], arr[1][i - 1], arr[2][i - 1]

    arr[0][0], arr[1][0], arr[2][0] = tmp3, tmp1, tmp2

for i in range(3):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()