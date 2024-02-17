def cost(k):
    return k*k+(k+1)*(k+1)

def calCnt(k, ti, tj):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ((abs(i - ti) + abs(j - tj) <= k)):
                if (arr[i][j] == 1):
                    cnt += 1
    return cnt 


def checkLine(i, j):
    if (0<=i<n and 0<=j<n):
        return True
    else:
        return False
        
n, m = map(int, input().split()) # m은 골드 값, 한 칸단 한 cost
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        for k in range(2*(n-1)+1):
            costSum = cost(k)
            tmp = calCnt(k, i, j)
            if ((tmp * m - costSum) >= 0): # 손해가 아니면
                cnt = max(cnt, tmp)
print(cnt)