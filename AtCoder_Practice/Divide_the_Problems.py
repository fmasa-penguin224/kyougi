N = int(input())
N_cent = int(N/2)
d = list(map(int, input().split()))
d_sort = sorted(d)

ans = d_sort[N_cent] - d_sort[N_cent-1]

print(ans)