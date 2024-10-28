import copy
n, m, t, k = map(int, input().split())
arr = [[list() for _ in range(n)] for _ in range(n)]
next_arr = [[list() for _ in range(n)] for _ in range(n)]
dir_map = {'D': 0, 'R': 1, 'L': 2, 'U': 3}
reverse_dir_map = {0: 'D', 1:'R', 2:'L', 3:'U'}
dis, djs = [1, 0, 0, -1], [0, 1, -1, 0] # D, R, L, U
result = 0
for num in range(m):
    r, c, d, v = input().split()
    arr[int(r)-1][int(c)-1].append((d, int(v), num))

def in_range(i, j):
    return 0<=i<n and 0<=j<n

def move(i, j, t_dv):
    ni, nj = dis[dir_map[t_dv[0]]] + i, djs[dir_map[t_dv[0]]] + j
    if in_range(ni, nj):
        return ni,nj, t_dv, -1
    else:
        return i, j, (reverse_dir_map[(3-dir_map[t_dv[0]]) % 4], t_dv[1], t_dv[2]), 0

def check_crash():
    for i in range(n):
        for j in range(n):
            if len(next_arr[i][j]) > k:
                sorted(next_arr[i][j], key = lambda x:(-x[1], -x[2]))
                next_arr[i][j] = next_arr[i][j][:k]
    
for _ in range(t):
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) != 0:
                for _ in range(len(arr[i][j])):
                    tmp_dv = arr[i][j].pop(0)
                    ti, tj = i, j
                    time = tmp_dv[1] 
                    while(time != 0):
                        ti, tj, tmp_dv, tmp_time = move(ti, tj, tmp_dv) 
                        # if i == 0 and j == 1:
                            # print(ti, tj, tmp_dv, tmp_time)
                        time += tmp_time
                    next_arr[ti][tj].append(tmp_dv)
    check_crash()
    arr = copy.deepcopy(next_arr)

for i in range(n):
    for j in range(n):
        result += len(arr[i][j])

print(result)