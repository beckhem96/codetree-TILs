n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
loc = [[-1, 0],[0, 1], [1, 0], [0, -1]]
result = 0
temp = 0

# 기준은 중심
def check_one(si, sj):
    ans = 0
    temp = [[0, 1], [1, 2], [2, 3], [3, 0]] # 중심 제외 위치값 
    for a, b in temp:
        max_value = 0
        ti1, tj1 = loc[a]
        ti2, tj2 = loc[b]
        si1, sj1 = si + ti1, sj + tj1
        si2, sj2 = si + ti2, sj + tj2
        if (check_line(si1, sj1) and check_line(si2, sj2)):
            max_value = array[si][sj] + array[si1][sj1] + array[si2][sj2]

        ans = max(ans, max_value)
    return ans

def check_two(si, sj):
    ans = 0
    temp = [[0, 2], [1, 3]] # 중심 제외 위치값 
    for a, b in temp:
        max_value = 0
        ti1, tj1 = loc[a]
        ti2, tj2 = loc[b]
        si1, sj1 = si + ti1, sj + tj1
        si2, sj2 = si + ti2, sj + tj2

        if (check_line(si1, sj1) and check_line(si2, sj2)):
            max_value = array[si][sj] + array[si1][sj1] + array[si2][sj2]

        ans = max(ans, max_value)
    return ans
        
def check_line(li, lj): 
    if (0<=li<n and 0<=lj<m):
        return True
    else: 
        return False

for i in range(n):
    for j in range(m):
        temp = max(check_one(i, j), check_two(i, j))
        result = max(result, temp)
        
print(result)