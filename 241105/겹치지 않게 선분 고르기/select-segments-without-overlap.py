n = int(input())
lines = [
    tuple(map(int, input().split())) for _ in range(n)
]

ans = 0
selected_lines = []

def overlapped(line1, line2):
    (ax1, ax2), (bx1, bx2) = line1, line2

    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
            (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)
def possible():
    for i, line1 in enumerate(selected_lines):
        for j, line2 in enumerate(selected_lines):
            if i < j and overlapped(line1, line2):
                return False
    return True

def find_max_lines(cnt):
    global ans
    
    if cnt == n:
        if possible():
            ans = max(ans, len(selected_lines))
        return
    selected_lines.append(lines[cnt])
    find_max_lines(cnt + 1)
    selected_lines.pop()

    find_max_lines(cnt + 1)
    
find_max_lines(0)
print(ans)