import sys
sys_input = sys.stdin.readline
N = int(input())
nums = [int(sys_input()) for _ in range(N)]
nums.sort()
for num in nums:
    print(num)