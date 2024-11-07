n, m, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
first_thief = []
max_nums = [[0 for _ in range(n)] for _ in range(n)]
result = 0
def cal_nums(i, x1, x2):
    tmp = []
    sum_value = 0
    cal_num = []

    for j in range(x1, x2+1):
        tmp.append(arr[i][j])

    tmp.sort(reverse=True)

    for value in tmp:
        sum_value += value
        if (sum_value <= c):
            cal_num.append(value * value)

    return sum(cal_num)

# 겹치는 지 확인
def is_duplicate(i, x1, x2, x3, x4): # 시작점과 끝점
    return x1 <= x3 <= x2 or x1 <= x4 <= x2 

for i in range(n):
    for j in range(n-m+1):
        first_thief.append((i, j, j+m-1))
        max_nums[i][j] = cal_nums(i, j, j+m-1)

for i, j, k in first_thief:
    for ni in range(n):
        for nj in range(n-m+1):
            if i == ni:
                if is_duplicate(i, j, k, j, j+m-1):
                    continue
            result = max(result, max_nums[i][j] + max_nums[ni][nj])
print(result)