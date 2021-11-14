S = input()

ans = 0

for i in range(len(S)):
    for j in range(i, len(S)):
        if all('ACGT'.count(x) == 1 for x in S[i : j+1]):
            ans = max(ans, j-i+1)

print(ans)