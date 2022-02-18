N = int(input())
line = list(map(int, input().split()))

line = sorted(line)

total = 0
wait_time = 0

for i in line:
    total += wait_time + i
    wait_time += i
print(total)
