H, W = map(int, input().split())
field = []
vector = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(H):
    field.append(list(input()))

q = set([])
q.add((0, 0, ''))
ans = 1

while q:
    x, y, alpa = q.pop()
    if field[x][y] in alpa:
        continue
    alpa += field[x][y]
    ans = max(ans, len(alpa))
    for vec in vector:
        nx = x + vec[0]
        ny = y + vec[1]
        if 0 <= nx < H and 0 <= ny < W and field[nx][ny] not in alpa:
            q.add((nx, ny, alpa))
print(ans)