BLANK = -1
COLLIDE = -2

t = int(input())
n, m = 0, 0
curr_dir = list()
next_dir = list()

mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

def in_range(i, j):
    return 0<=i<n and 0<=j<n

def update_next_dir(i, j, move_dir):
    if next_dir[i][j] == BLANK:
        next_dir[i][j] = move_dir
    else:
        next_dir[i][j] = COLLIDE

def move(i, j, move_dir):
    dis, djs = [-1, 1, 0, 0], [0, 0, 1, -1]
    ni, nj = i + dis[move_dir], j + djs[move_dir]
    if in_range(ni, nj):
        update_next_dir(ni, nj, move_dir)
    else:
        update_next_dir(i, j, (5-move_dir)%4)
def move_all():
    global next_dir

    next_dir = [[BLANK for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if curr_dir[i][j] != BLANK:
                move(i, j, curr_dir[i][j])
    for i in range(n):
        for j in range(n):
            curr_dir[i][j] = next_dir[i][j]

def remove_duplicate_marbles():
    for i in range(n):
        for j in range(n):
            if curr_dir[i][j] == COLLIDE:
                curr_dir[i][j] = BLANK
def simulate():
    move_all()
    remove_duplicate_marbles()

for _ in range(t):
    n, m = map(int, input().split())

    curr_dir = [[BLANK for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        x, y, d = input().split()
        x, y = int(x), int(y)
        curr_dir[x-1][y-1] = mapper[d]

    for _ in range(2*n):
        simulate()

    marble_cnt = sum([
        curr_dir[i][j] != BLANK
        for i in range(n)
        for j in range(n)
    ])

    print(marble_cnt)