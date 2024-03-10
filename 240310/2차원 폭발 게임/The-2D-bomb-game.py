BLANK = -1
WILL_EXPLODE = 0

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tmp = [0 for _ in range(n)] 

def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(tmp)):
        if tmp[end_idx] != curr_num:
            return end_idx - 1
    return len(tmp) - 1

def explode():
    while True:
        did_explode = False
        curr_idx = 0

        while curr_idx < len(tmp):
            end_idx = get_end_idx_of_explosion(curr_idx, tmp[curr_idx])

            if end_idx - curr_idx + 1 >= m:

                del tmp[curr_idx:end_idx + 1]
                did_explode = True
            else:
                curr_idx = end_idx + 1
        if not did_explode:
            break

def copy_column(col):
    global tmp
    tmp = [arr[row][col] for row in range(n) if arr[row][col] != BLANK]

def copy_result(col):
    for row in range(n - 1, -1, -1):
        ## 원소가 비어있지 
        arr[row][col] = tmp.pop() if tmp else BLANK

def simulate():
    for col in range(n):
        copy_column(col)
        explode()
        copy_result(col)

def rotate():
    global arr

    tmp_arr = [
        [BLANK for _ in range(n)]
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            tmp_arr[i][j] = arr[n - j - 1][i]
    arr = tmp_arr

simulate()
for _ in range(k):
    rotate()
    simulate()

answer = sum([arr[i][j] != BLANK for i in range(n) for j in range(n)])
print(answer)