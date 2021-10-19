N = int(input())

x = N//9+1
y = N%9

ans = ""

for _ in range(x):
    ans += str(y)

print(ans)