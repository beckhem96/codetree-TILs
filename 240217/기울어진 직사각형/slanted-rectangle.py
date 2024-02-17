n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_score(x, y, k, l):
    sum_of_nums = 0
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l] # k, l이 같을 수 있는 이유는 바라보는 사각형의 변의 길이가 같아야하니까
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
            
            if not in_range(x, y):
                return 0

            sum_of_nums += arr[x][y]
    return sum_of_nums

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_score(i, j, k, l))
print(ans)