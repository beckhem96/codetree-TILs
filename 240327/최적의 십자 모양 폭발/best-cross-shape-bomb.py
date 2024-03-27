import copy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = copy.deepcopy(arr)
dis, djs = [1, -1, 0, 0], [0, 0, -1, 1]
result = 0
def remove_nums(i, j):
    nums = tmp[i][j]
    tmp[i][j] = 0
    for num in range(nums): 
        for di, dj in zip(dis, djs):
            ni, nj = i + (di * num) , j + (dj * num)
            if check_range(ni, nj):
                tmp[ni][nj] = 0 

def move_nums():
    for j in range(n):
        for i in range(n-1, -1, -1):
            if (tmp[i][j] == 0 and check_range(i+1, j)):
                tmp[i][j] = tmp[i+1][j]
                tmp[i+1][j] = 0


def check_range(i, j):
    return 0 <= i < n and 0 <= j < n

def check_how_may():
    check_arr = [[0] * n for _ in range(n)]
    check_num = 0
    ret = 0
    for i in range(n):
        for j in range(n):
            check_num += 1
            for di, dj in zip(dis, djs):
                ni, nj = i + di, j + dj
                if check_range(ni, nj):
                    if (tmp[ni][nj] == tmp[i][j] and check_arr[ni][nj] != check_arr[i][j]):
                        check_arr[ni][nj] = check_num
                        check_arr[i][j] = check_num
                        ret += 1
    return ret



for i in range(n):
    for j in range(n):
        remove_nums(i, j)
        move_nums()
        result = max(result, check_how_may())
        tmp = copy.deepcopy(arr)
print(result)