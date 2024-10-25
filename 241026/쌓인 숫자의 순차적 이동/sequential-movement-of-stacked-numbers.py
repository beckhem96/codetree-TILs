n, m = map(int, input().split())
arr = [[list() for _ in range(n)] for _ in range(n)]

dis, djs = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    tmps = list(map(int, input().split()))
    for j in range(n):
        arr[i][j].append(tmps[j])

nums = list(map(int, input().split()))

def in_range(i, j):
    return 0<=i<n and 0<=j<n

def move(i, j, value):
    m_value, mi, mj = -1, -1, -1
    for k in range(8):
        ni, nj = dis[k] + i, djs[k] + j
        if in_range(ni, nj) and arr[ni][nj] != []:
            if (max(arr[ni][nj]) > m_value):
                m_value, mi, mj = max(arr[ni][nj]), ni, nj
                # if(value == 4):
                    # print(m_value, mi, mj)
    if m_value == -1:
        return
    tmp_list = []
    for _ in range(arr[i][j].index(value), len(arr[i][j])):
        tmp_list.append(arr[i][j].pop(-1))
    for _ in range(len(tmp_list)):
        arr[mi][mj].append(tmp_list.pop(-1))

for num in nums:
    flag = False
    for i in range(n):
        for j in range(n):
            if num in arr[i][j]:
                flag =True
                move(i, j, num)
                break
        if flag:
            break
                # for k in range(n):
                #     for l in range(n):
                #         if arr[k][l] == []:
                #             print(None)
                #         else:
                #             print(arr[k][l])
                # print()
for i in range(n):
    for j in range(n):
        if arr[i][j] == []:
            print(None)
        else:
            for k in range(len(arr[i][j])-1, -1, -1):
                if k == 0:
                    print(arr[i][j][k])
                else:
                    print(arr[i][j][k], end=' ')