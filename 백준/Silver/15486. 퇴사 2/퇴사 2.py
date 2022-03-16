import sys
sys_input = sys.stdin.readline

N = int(input())
booking = []
dp = [0] * (N+1)

for _ in range(N):
    time, pay = map(int, sys_input().strip().split())
    booking.append((time, pay))
max_pay = 0
for now in range(0, N):
    max_pay = max(max_pay, dp[now])
    time = booking[now][0]
    pay = booking[now][1]
    if now+time > N:
        continue
    dp[now] = max_pay
    dp[now+time] = max(dp[now]+pay, dp[now+time])
# print(dp[N])
print(max(dp))