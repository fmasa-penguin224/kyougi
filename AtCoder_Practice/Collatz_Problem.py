S = int(input())
flag = True

A = [S]

ans = 0

while flag:
    if S%2 == 0:
        S = S/2
    else:
        S = 3*S+1

    A.append(S)
    for i in range(len(A)-1):
        if A[i] == A[-1]:
            ans = len(A)
            flag = False
            break

print(ans)

