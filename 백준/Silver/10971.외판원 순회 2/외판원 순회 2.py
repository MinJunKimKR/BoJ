import sys
sys_input = sys.stdin.readline
N = int(input())
graph = []
city = [x for x in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys_input().strip().split())))

INF = 100000001*N
min_cost = INF


def dfs(start, next, cost, visited):
    global min_cost
    if len(visited) == N and graph[next][start] != 0:
        min_cost = min(min_cost, cost+graph[next][start])
        return

    for i in range(N):
        this_cost = cost+graph[next][i]
        if i not in visited and this_cost < min_cost and graph[next][i] != 0:
            visited.append(i)
            dfs(start, i, this_cost, visited)
            visited.pop()


for i in range(N):
    dfs(i, i, 0, [i])

print(min_cost)