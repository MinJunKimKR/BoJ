N, K = map(int, input().split())
items = list(map(int, input().split()))

tap = []
cnt_change = 0

for i in range(K):
    item = items[i]
    if item in tap:
        continue
    if len(tap) < N:
        tap.append(item)
        continue
    next_idx = []
    for j in range(N):
        try:
            idx = items[i:].index(tap[j])
        except:
            idx = 101
        next_idx.append(idx)
    out_idx = next_idx.index(max(next_idx))
    del tap[out_idx]
    tap.append(item)
    cnt_change += 1
print(cnt_change)