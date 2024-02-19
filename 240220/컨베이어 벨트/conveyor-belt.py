n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]
tmp1, tmp2 = 0, 0


def belt_move():
    tmp1, tmp2 = arr[0][n-1], arr[1][n-1]
    for i in range(n-1, 0, -1):
        arr[0][i] = arr[0][i - 1]
    for i in range(n-1, 0, -1):
        arr[1][i] = arr[1][i -1]
    arr[0][0] = tmp2
    arr[1][0] = tmp1
for time in range(t):
    belt_move()

for i in range(2):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()