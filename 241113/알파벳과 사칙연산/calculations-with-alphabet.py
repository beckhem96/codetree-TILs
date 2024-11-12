import copy

inp = list(input())
nums = [1, 2, 3, 4]
ops = []
alphas = []
n = len(inp)
result = 0

for i in range(n):
    if (i % 2) != 0:
        ops.append(inp[i])

m = n - len(ops)

def cal(num1, op, num2):
    if op == '*':
        return num1 * num2
    elif op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2

def cal_all():
    tmp = copy.deepcopy(alphas)
    for operator in ops:
        num_count = 0

        tmp.insert(0, cal(tmp.pop(0), operator, tmp.pop(0)))
    
    return sum(tmp)

def find_max(cnt):
    global result

    if cnt == m:
        result = max(result, cal_all())
        return
    for i in range(4):
        alphas.append(nums[i])
        find_max(cnt + 1)
        alphas.pop()
    # find_max(cnt + 1)
    
find_max(0)
print(result)