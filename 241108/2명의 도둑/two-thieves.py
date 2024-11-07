n, m, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
first_thief = []
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
    return sum_value

def add_nums(i, x1, x2):
    global selected_nums, nums, sum_value
    nums = []
    sum_value = 0
    selected_nums = []


    for j in range(x1, x2+1):
        nums.append(arr[i][j])

    return cal_nums(0)
 

# 겹치는 지 확인
def is_duplicate(i, x1, x2, x3, x4): # 시작점과 끝점
    return x1 <= x3 <= x2 or x1 <= x4 <= x2 

for i in range(n):
    for j in range(n-m+1):
        first_thief.append((i, j, j+m-1))
        max_nums[i][j] = add_nums(i, j, j+m-1)

for i, j, k in first_thief:
    for ni in range(n):
        for nj in range(n-m+1):
            if i == ni:
                if is_duplicate(i, j, k, j, j+m-1):
                    continue
            result = max(result, max_nums[i][j] + max_nums[ni][nj])
print(result)