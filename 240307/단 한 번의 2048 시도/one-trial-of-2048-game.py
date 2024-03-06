NONE = -1

n = 4
arr = [list(map(int, input().split())) for _ in range(n)]
next_arr = [[0] * n for _ in range(n)]
direction = input()

def rotate():

    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = arr[n -j - 1][i]

    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

def drop():
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0

    for j in range(n):
        keep_num, next_row = NONE, n - 1
        for i in range(n - 1, -1, -1):
            if not arr[i][j]:
                continue

            if keep_num == NONE:
                keep_num = arr[i][j]
            elif keep_num == arr[i][j]:
                next_arr[next_row][j] = keep_num * 2
                keep_num = NONE

                next_row -= 1

            else:
                next_arr[next_row][j] = keep_num
                keep_num = arr[i][j]

                next_row -= 1
        if keep_num != NONE:
            next_arr[next_row][j] = keep_num
            next_row -= 1

    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

def tilt(move_dir):
    for _ in range(move_dir):
        rotate()

    drop()

    for _ in range(4 - move_dir):
        rotate()

dr_dict = {'D': 0, 'R':1, 'U':2, 'L':3}

tilt(dr_dict[direction])

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()