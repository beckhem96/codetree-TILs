n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0 # 양수 직사각형 중 가장 넓은 것

def cal_width(x1, y1, x2, y2):
    return (x2 + 1 - x1) * (y2 + 1 - y1)

def sum_rect(x1, y1, x2, y2):
    rect_sum = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if (arr[i][j] > 0):
                rect_sum += arr[i][j]
            else: 
                return -1
    return rect_sum



for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                tmp = sum_rect(i, j, k, l)
                if (tmp > 0):
                    ans = max(ans, cal_width(i, j, k, l))
print(ans)