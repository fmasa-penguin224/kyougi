A = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    A.append(row)

M = []
for _ in range(0, 3):
    row = []
    for _ in range(0,3):
        row.append(False)
    M.append(row)

N = int(input())

for _ in range(0, N):
    b = int(input())
    for i in range(0, 3):
        for j in range(0, 3):

            if A[i][j] == b:
                M[i][j] = True

flag = False
for i in range(0, 3):
    if M[i][0] and M[i][1] and M[i][2]:
        flag = True
        break

for i in range(0, 3):
    if M[0][i] and M[1][i] and M[2][i]:
        flag = True
        break

if M[0][0] and M[1][1] and M[2][2]:
    flag = True

if M[0][2] and M[1][1] and M[2][0]:
    flag = True

if flag:
    print("Yes")
else:
    print("No")


