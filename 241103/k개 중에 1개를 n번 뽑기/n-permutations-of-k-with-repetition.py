k, n = map(int, input().split())
answer = []
def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def c(num):
    if num == n + 1:
        print_answer()
        return
    
    for i in range(1, k + 1):
        answer.append(i)
        c(num + 1)
        answer.pop()

c(1)