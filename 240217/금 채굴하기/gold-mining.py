def cost(K):
    return K*K+(K+1)*(K+1)

def calArea(K, ti, tj, n):
    cnt = 0

    if (K == 0 and arr[ti][tj] == 1):
        return 1
    if(K == 1):
        if (arr[ti][tj] == 1):
            cnt += 1
        for si, sj in cross1:
            if (checkLine(ti + si*K, tj + sj*K)):
                if(arr[ti + si*K][tj + sj*K] == 1):
                    # if(ti == 2 and tj == 4 and K == 1):
                    #     print(ti + si*K, tj + sj*K, "cross1")
                    cnt += 1
    elif (K == 2):
        # 정사각형 밖 4개
        for si, sj in cross1:
            if (checkLine(ti + si*K, tj + sj*K)):
                if(arr[ti + si*K][tj + sj*K] == 1):
                    # if(ti == 0 and tj == 0 and K == 4):
                    #     print(ti + si*K, tj + sj*K, "cross1")
                    cnt += 1
        # 정사각형
        tk = K - 1 
        for si in range(ti - tk, ti + K):
            for sj in range(tj - tk, tj + K):
                if (checkLine(si, sj)):
                    if(arr[si][sj] == 1):
                        # if(ti == 0 and tj == 0 and K == 4):
                        #     print(si, sj, ti - tk, ti + K, tj - tk, tj + K, "cross2")
                        cnt += 1
    elif (k >= 3):
        # 정사각형 밖 4개
        for si, sj in cross1:
            if (checkLine(ti + si*K, tj + sj*K)):
                if(arr[ti + si*K][tj + sj*K] == 1):
                    # if(ti == 0 and tj == 0 and K == 4):
                    #     print(ti + si*K, tj + sj*K, "cross1")
                    cnt += 1
        # 정사각형
        tk = K - 1 
        for si in range(ti - tk, ti + K):
            for sj in range(tj - tk, tj + K):
                if (checkLine(si, sj)):
                    if ((si != ti - tk and sj != tj - tk) and (si != ti - tk and sj != tj + tk) 
                    and (si != ti + tk and sj != tj - tk) and (si != ti + tk and sj != tj + tk)):
                        if(arr[si][sj] == 1):
                            # if(ti == 0 and tj == 0 and K == 4):
                            #     print(si, sj, ti - tk, ti + K, tj - tk, tj + K, "cross2")
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
        for k in range(2*(n-1)):
            costSum = cost(k)
            tmp = calArea(k, i, j, n)
            
            if ((tmp * m - costSum) >= 0): # 손해가 아니면
                cnt = max(cnt, tmp)
print(cnt)