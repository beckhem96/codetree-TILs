import copy
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp_arr = [[0] *n for _ in range(n)] 
next_arr = [[0] * n for _ in range(n)]
result = 0

def bumb(i, j):
    cnt = 0
    tmp = []
    for di in range(i, n):
        if (arr[di][j] == arr[i][j]):
            cnt += 1
            tmp.append(di)
        elif(arr[di][j] != arr[i][j]):
            break
    if(cnt >= m):
        for di in tmp:
            arr[di][j] = 0 

def move():
   
    flag = False
    for j in range(n):
        b_num = -1
        for i in range(n-1, -1, -1):
            # if (arr[i][j] != 0 and flag != True):
            #     tmp_arr[i][j] = arr[i][j]
            # elif (arr[i][j] != 0 and flag == True):
            #     tmp_arr[b_num][j] = arr[i][j]
            #     # b_num += 1
            if (arr[i][j] == 0):
                for k in range(i, -1, -1):
                    if (arr[k][j] != 0):
                        arr[i][j] = arr[k][j]
                        arr[k][j] = 0
                        break 

def rotate():
    for i in range(n):
        for j in range(n):
            tmp_arr[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            tmp_arr[i][j] = arr[n - j - 1][i]

    for i in range(n):
        for j in range(n):
            arr[i][j] = tmp_arr[i][j]
            
for _ in range(k):      
    for i in range(n):
        for j in range(n):
            if (arr[i][j] != 0):
                bumb(i, j)
    move()
    rotate()
    move()

for i in range(n):
    for j in range(n):
        if(arr[i][j] != 0):
            result += 1
print(result)