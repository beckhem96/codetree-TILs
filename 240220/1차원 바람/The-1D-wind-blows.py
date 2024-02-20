n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def check_spread_down(row):
    if (row < n):
        for j in range(m):
            if (arr[row][j] == arr[row - 1][j]):
                return True
    return False

def check_spread_up(row):
    if (row >= 0):
        for j in range(m):
            if (arr[row][j] == arr[row + 1][j]):
                return True
    return False

def wind_move(row, way, spread_way):
    if (way == 'R'):
        tmp = arr[row][0]
        for i in range(m-1):
            arr[row][i] = arr[row][i + 1]
        arr[row][m-1] = tmp
        if (spread_way == '' or spread_way== "up" and check_spread_up(row - 1)):
            wind_move(row - 1, 'L', 'up')
        if (spread_way == '' or spread_way== "down" and check_spread_down(row + 1)):
            wind_move(row + 1, 'L', 'down')
    else:
        tmp = arr[row][m-1]
        for i in range(m-1, 0, -1):
            arr[row][i] = arr[row][i - 1]
        arr[row][0] = tmp

        if (spread_way == '' or spread_way== "up" and check_spread_up(row - 1)):
            wind_move(row - 1, 'R', 'up')
        if (spread_way == '' or spread_way== "down" and check_spread_down(row + 1)):
            wind_move(row + 1, 'R', 'down')

for _ in range(q):
    row, way = input().split()
    row = int(row)
    wind_move(row - 1, way, '')

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()