import copy

n, m, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
first_theif = []
max_nums = [[0 for _ in range(n)] for _ in range(n)]
result = 0
    
def cal_nums(cnt):
    global sum_value

    if sum(selected_nums) <= c:
        tmp = 0
        for num in selected_nums:
            tmp += (num *num)
        sum_value = max(sum_value, tmp)
    else: return
    if cnt == m:
        return
    selected_nums.append(nums[cnt])
    cal_nums(cnt + 1)
    selected_nums.pop()
    cal_nums(cnt + 1)


def add_nums(i, x1, x2):
    global selected_nums, nums, sum_value
    nums = []
    sum_value = 0
    selected_nums = []

    for j in range(x1, x2+1):
        nums.append(arr[i][j])

    cal_nums(0)

    return sum_value
 

# 겹치는 지 확인
def is_duplicate(i, x1, x2, x3, x4): # 시작점과 끝점
    return x1 <= x3 <= x2 or x1 <= x4 <= x2 

for i in range(n):
    for j in range(n-m+1):
        first_theif.append((i, j, j+m-1))
        max_nums[i][j] = add_nums(i, j, j+m-1)

second_theif = copy.deepcopy(first_theif)

for i, j, k in first_theif:
    for ni, nj, nk in second_theif:
        if i == ni:
            if is_duplicate(i, j, k, nj, nk):
                continue
        result = max(result, max_nums[i][j] + max_nums[ni][nj])
print(result)