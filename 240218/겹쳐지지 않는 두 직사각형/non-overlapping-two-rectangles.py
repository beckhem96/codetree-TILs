import sys

INT_MIN = -sys.maxsize

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * m for _ in range(n)]
ans = INT_MIN

def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

def chek_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False

def draw(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            board[i][j] += 1

def is_overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return chek_board()

def rect_sum(x1, y1, x2, y2):
    return sum([arr[i][j] for i in range(x1, x2+1) for j in range(y1, y2+1)])

def find_max_sum_wirh_rect(x1, y1, x2, y2):
    max_sum = INT_MIN
    for i in range(n):
        for j in range(m):
            for k in range(i, n): # row
                for l in range(j, m): # col
                    if not (is_overlapped(x1, y1, x2, y2, i, j, k, l)):
                        max_sum = max(max_sum, rect_sum(x1, y1, x2, y2) + rect_sum(i, j, k, l))
                        
    return max_sum
                    
def find_max_sum():
    max_sum = INT_MIN
    for i in range(n):
        for j in range(m):
            for k in range(i, n): # row
                for l in range(j, m): # col
                    max_sum = max(max_sum, find_max_sum_wirh_rect(i, j, k, l))
    return max_sum
ans = find_max_sum()
print(ans)