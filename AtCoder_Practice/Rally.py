N = int(input())
X = list(map(int, input().split()))

ans = 100000000
X_min = X[0]
X_max = X[0]
for i in range(N):
    if X_min > X[i]:
        X_min = X[i]

    if X_max < X[i]:
        X_max = X[i]

for i in range(X_min, X_max+1):
    sum = 0
    for j in range(N):
        sum += (X[j]-i)*(X[j]-i)

    if sum < ans:
        ans = sum

print(ans)