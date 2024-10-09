OUT_OF_GRID = (-1, -1)
n, m, r, c = map(int, input().split())
r -= 1
c -= 1
direction = list(input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]
dir_mapper = {
    'R': 0,
    'L': 1,
    'U': 2,
    'D': 3
}
up, front, right = 1, 2, 3
def in_range(r, c):
    return 0<= r and r < n and 0<=c and c < n
def next_pos(r, c, move_dir):
    drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]
    nr, nc = r + drs[move_dir], c + dcs[move_dir]
    return (nr, nc) if in_range(nr, nc) else OUT_OF_GRID

def simulate(move_dir):
    global r, c
    global up, front, right

    nr, nc = next_pos(r, c, move_dir)

    if (nr, nc) == OUT_OF_GRID:
        return
    r, c = nr, nc

    if move_dir == 0:
        up, front, right = 7 - right, front, up
    elif move_dir == 1:
        up, front, right = right, front, 7 - up
    elif move_dir == 2:
        up, front, right = front, 7 - up, right
    else:
        up, front, right = 7 - front, up, right
    bottom = 7 - up
    arr[r][c] = bottom

arr[r][c] = 6
for char_dir in direction:
    simulate(dir_mapper[char_dir])
ans = sum([arr[i][j]
    for i in range(n)
    for j in range(n)
])

print(ans)