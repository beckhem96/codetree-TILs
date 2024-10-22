import copy

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
loc_arr = [[0 for _ in range(n)] for _ in range(n)]

dis, djs = [0, 0, 1, -1], [1, -1, 0, 0]
result = 0
for _ in range(m):
    r, c = map(int, input().split())
    loc_arr[r-1][c-1] = 1

next_loc_arr = copy.deepcopy(loc_arr)

def in_range(i, j):
    return 0<=i<n and 0<=j<n
def move(i, j):
    m_value, mi, mj = -1, -1, -1
    for di, dj in zip(dis, djs):
        ni, nj = di + i, dj + j
        if in_range(ni, nj):
            if (arr[ni][nj] >= m_value):
                m_value, mi, mj = arr[ni][nj], ni, nj
    if (next_loc_arr[i][j] == 1):
        next_loc_arr[i][j] = 0
    elif (next_loc_arr[i][j] >= 2):
        next_loc_arr[i][j] -= 1
    next_loc_arr[mi][mj] += 1

for _ in range(t):
    for i in range(n):
        for j in range(n):
            if loc_arr[i][j] == 1:
                move(i, j)
    loc_arr = copy.deepcopy(next_loc_arr)
    for i in range(n):
        for j in range(n):
            if loc_arr[i][j] >= 2:
                loc_arr[i][j] = 0
    next_loc_arr = copy.deepcopy(loc_arr)
for i in range(n):
    for j in range(n):
        if loc_arr[i][j] == 1:
            result += 1
print(result)