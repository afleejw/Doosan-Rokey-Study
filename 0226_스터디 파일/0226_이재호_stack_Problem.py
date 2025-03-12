import sys
input = sys.stdin.readline

n = int(input())
numsOrdered = [] # 입력되는 수를 받는 역할
for _ in range(n):
    numsOrdered.append(int(input()))
numsSorted = [i for i in range(n,0,-1)] 
# 내림차순으로 정렬하는 역할 -> 나중에 pop할 때 오름차순으로 stack에 쌓기 위해서

# print(numsSorted)
stack = []
output = []
ans = True
for i in numsOrdered:
    if numsSorted and i >= numsSorted[-1]: # 올라가는 경우우
        while numsSorted and i >= numsSorted[-1]:
            stack.append(numsSorted.pop())
            output.append('+')

        if stack and i == stack[-1]:
            stack.pop()
            output.append('-')

    else: # 내려가는 경우
        if stack and i == stack[-1]:
            stack.pop()
            output.append('-')
        else:
            if stack:
                ans = False
                break
if ans:
    for i in output:
        print(i)
else:
    print('NO')
