arr = list(input())
n = len(arr)
result = 20
def shift():
    tmp = arr[-1] 
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
        arr[0] = tmp
    return get_len()

def get_len():
    cnt = 1
    for i in range(n-1):
        if (arr[i] != arr[i+1]):
            cnt += 1
    return cnt * 2

for _ in range(n):
    result = min(shift(), result)
print(result)