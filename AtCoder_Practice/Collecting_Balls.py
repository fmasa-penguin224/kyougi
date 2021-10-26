N = int(input())
K = int(input())
x = list(map(int, input().split()))

sum_al = 0
for i in range(N):
    A = 2*x[i]
    B = 2*(K-x[i])
    if A <= B:
        sum_al += A
    else:
        sum_al += B

print(sum_al)