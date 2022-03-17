# 6:02 -> 6:40

N, K = map(int, input().split())
coins = []
INF = int(1e9)
dp = [INF] * (K+1)
min_coin = INF
for _ in range(N):
    coin = int(input())
    min_coin = min(min_coin, coin)
    coins.append(coin)

dp[0] = 0

for i in range(min_coin, K+1):
    for coin in coins:
        if coin > i:
            continue
        dp[i] = min(dp[i], dp[i-coin]+1)
if dp[K] == INF:
    print(-1)
else:
    print(dp[K])
