from collections import deque

N, K = list(map(int, input().split()))

left = deque([i for i in range(1, N+1)])
right = deque([])
result = []
while len(left)+len(right) > 0:
    for _ in range(1, K):
        if len(left) == 0:
            left, right = right, left
        right.append(left.popleft())

    if len(left) == 0:
        left, right = right, left
    result.append(left.popleft())

print('<', end='')
for i in range(len(result)):
    if i != len(result)-1:
        print(result[i], end=', ')
        continue
    print(result[i], end='')
print('>', end='')
