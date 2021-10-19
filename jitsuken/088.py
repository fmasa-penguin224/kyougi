N = int(input())

S = []
for _ in range(N):
    row = input()
    row = list(row)
    S.append(row)

for i in range(N-2, -1, -1):
    for j in range(2*N-2):
        if S[i][j]=="#":
            if S[i+1][j-1]=="X":
                S[i][j]="X"
            if S[i+1][j]=="X":
                S[i][j]="X"
            if S[i+1][j+1]=="X":
                S[i][j]="X"

for i in range(N):
    S[i] = "".join(S[i])
    print(S[i])