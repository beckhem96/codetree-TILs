n, m = map(int, input().split()) # m은 골드 값, 한 칸단 한 cost
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = [[-1, 0]. [0, 1], [1, 0], [0, -1]]
tmpa = [[-1, 0]. [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]] # z -1 곱하라 , 결국 n은 못 넘어감
result1 = 0
for i in range(n):
    for j in range(n):
        tmp2 = 0
        while(tmp2 <= n):

           result = max(calArea(n, i, j) - cost(tmp2), result1)

            tmp2 += 1

def cost(K):
    return K*K+(K+1)*(K+1)

def calArea(zn, zm, ti, tj):
    result2 = 0
    if (z==0):
        return arr[ti][sj]*zm 
    for a, b in tmp:
        si, sj = zn*a, zn*b
        if (arr[si][sj] == 1):
            result2 += m
              
    if (z >= 1):
        for a, b in tmpa:
            z - 1