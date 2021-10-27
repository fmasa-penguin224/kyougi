N = int(input())
x = list(map(int, input().split()))

x.sort(reverse=True)

A=0
B=0

for i in range(N):
    if i%2==0:
        A += x[i]
    elif i%2==1:
        B += x[i]

if A <= B:
    print(B-A)
elif A > B:
    print(A-B)

