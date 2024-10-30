BLANK = -1

n, m, t = map(int, input().split())
arr = [[BLANK for _ in range(n)] for _ in range(n)]
marbles = []
next_marbles = []
mapper = {'D':0, 'R':1, 'L':2, 'U':3}
dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def move(marble):
    r, c, d, w, num = marble
    nx, ny = dxs[d] + r, dys[d] + c
    if (not in_range(nx, ny)): # 벗어나면 방향 바꿈
        d = (3-d) % 4
        return (r, c, d, w, num)
    else:
        return (nx, ny, d, w, num)

def check_crash(marble):
    r, c, d, w, num = marble
    return arr[r][c]
def crash(marble1, marble2):
    r, c, d1, w1, num1 = marble1
    r, c, d2, w2, num2 = marble2
    
    if num1 > num2:
        return (r, c, d1, w1+w2, num1)
    else:
        return (r, c, d2, w1+w2, num2)

def push_next_marbles(marble):
    index = check_crash(marble)
    r, c, d, w, num = marble
    if index == BLANK:
        next_marbles.append(marble)
        r, c, d, w, num = marble
        arr[r][c] = len(next_marbles) - 1
    else:
        next_marbles[index] = crash(next_marbles[index], marble)


for num in range(m):
    r, c, d, w = input().split()
    r, c, w = int(r)-1, int(c)-1, int(w)
    marbles.append((r, c, mapper[d], w, num))

for _ in range(t):
    for marble in marbles:
        next_marble = move(marble)
        push_next_marbles(next_marble)
    marbles = next_marbles[:]
    next_marbles = []
    arr = [[BLANK for _ in range(n)] for _ in range(n)]

result = 0
for i in range(len(marbles)):
    r, c, d, w, num = marbles[i]
    result = max(result, w)
print(len(marbles), result)