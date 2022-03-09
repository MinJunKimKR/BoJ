from math import ceil
import sys
sys_input = sys.stdin.readline
T = int(input())

ans = []
for x in range(T):
    M = int(input())
    arr = []
    loop_cnt = ceil(M/10)
    for _ in range(loop_cnt):
        row = sys_input().strip().split()
        arr = arr+(list(map(int, row)))
    result = []
    for i in range(1, M+1, 2):
        this_arr = sorted(arr[:i])
        len_arr = len(this_arr)
        result.append(this_arr[len_arr//2])

    cnt = 0
    ans.append([len(result), result])

for i in range(T):
    print(ans[i][0], end=' ')
    for j in range(ans[i][0]):
        if j % 10 == 0:
            print()
        print(ans[i][1][j], end=' ')
    print()