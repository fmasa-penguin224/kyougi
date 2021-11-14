N ,M, X = map(int, input().split())
A = list(map(int, input().split()))

count1 = 0
for i in range(1, X):
    for j in range(M):
        if i == A[j]:
            count1 += 1

count2 = 0
for i in range(X+1, N):
    for j in range(M):
        if i == A[j]:
            count2 += 1

print(min(count1, count2))

