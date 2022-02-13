N = int(input())
facto = 1

for i in range(1, N+1):
    # if i == 1:
    #     facto += 1
    #     continue
    facto *= i
print(facto)