N = int(input())

A = []
for _ in range(N-1):
    row = list(map(int, input().split()))
    A.append(row)

flag1=True
for i in range(1, N-1):
    if A[0][0] != A[i][0] and A[0][0] != A[i][1]:
        flag1 = False

flag2=True
for i in range(1, N-1):
    if A[0][1] != A[i][0] and A[0][1] != A[i][1]:
        flag2 = False

if flag1 or flag2:
    print("Yes")
else:
    print("No")
