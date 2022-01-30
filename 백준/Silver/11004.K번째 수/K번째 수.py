import sys
sys_input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, sys_input().split()))
nums.sort()
print(nums[K-1])
