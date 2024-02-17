def cost(K):
    return K*K+(K+1)*(K+1)

def calArea(K, ti, tj, n):
    cnt = 0

    if (arr[ti][tj] == 1):
            cnt += 1
    if(K == 1):
        for si, sj in cross1:
            if (checkLine(ti + si*K, tj + sj*K)):
                if(arr[ti + si*K][tj + sj*K] == 1):
                    cnt += 1
    elif (K >= 2):
        # 십자
        for si, sj in cross1:
            if (checkLine(ti + si*K, tj + sj*K)):
                if(arr[ti + si*K][tj + sj*K] == 1):
                    cnt += 1
        # 꺾인 십자
        for z in range(1, K):
            for si in range(ti -z, ti + z):
                for sj in range(tj -z, tj + z):
                    if (checkLine(ti + si*K, tj + sj*K)):
                        if(arr[si][sj] == 1):
                            cnt += 1
    return cnt

def checkLine(i, j):
    if (0<=i<n and 0<=j<n):
        return True
    else:
        return False

n, m = map(int, input().split()) # m은 골드 값, 한 칸단 한 cost
arr = [list(map(int, input().split())) for _ in range(n)]
cross1 = [[-1, 0], [0, 1], [1, 0], [0, -1]] # n -1까지
cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            costSum = cost(k)
            tmp = calArea(k, i, j, n)
            if ((tmp * m - costSum) >= 0): # 손해가 아니면
                if (cnt < tmp):
                    cnt = tmp
print(cnt)