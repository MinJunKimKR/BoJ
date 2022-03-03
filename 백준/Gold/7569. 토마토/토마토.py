from collections import deque
import sys
sys_input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = []
vector = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

day = -1

for _ in range(H):
    arr = []
    for _ in range(N):
        row = list(map(int, sys_input().strip().split()))
        arr.append(row)
    graph.append(arr)

q = deque([])

for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 1:
                q.append((z, x, y))

while q:
    z, x, y = q.popleft()
    for vec in vector:
        nz = z + vec[0]
        nx = x + vec[1]
        ny = y + vec[2]
        if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
            if graph[nz][nx][ny] != 0:
                continue
            graph[nz][nx][ny] = graph[z][x][y]+1
            q.append((nz, nx, ny))

result = -1
for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 0:
                print(-1)
                exit(0)
            result = max(result, graph[z][x][y])

print(result-1)
