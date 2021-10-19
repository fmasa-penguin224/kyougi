A, B = (float(x) for x in input().split())
i =(B-1)/(A-1)

for ans in range(100):
    if ans >= i:
        print(ans)
        break