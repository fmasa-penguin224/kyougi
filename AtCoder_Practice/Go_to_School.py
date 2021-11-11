N = int(input())
A = list(map(int, input().split()))

ANS = [0] * N

for i in range(N):
    j = A[i] - 1
    ANS[j] = i+1

ANS = [str(x) for x in ANS]
ANS = ' '.join(ANS)
print(ANS)