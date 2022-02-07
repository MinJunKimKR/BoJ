def gcd(A, B):
    while B > 0:
        A, B = B, A % B
    return A


A, B = map(int, input().split())

C = gcd(A, B)

print('1'*C)
