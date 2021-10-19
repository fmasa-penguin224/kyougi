N, M, C = map(int, input().split())
B = list(map(int, input().split()))

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

count = 0
for i in range(N):
    sum = 0
    for j in range(M):
        sum += A[i][j]*B[j]

    if sum+C > 0:
        count+=1

print(count)