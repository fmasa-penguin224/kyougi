K, N = map(int, input().split())

A = list(map(int, input().split()))

ans = A[N-1] - A[0]

for i in range(N):
    select_house_to_end = K - A[i]
    start_to_first_house = A[i-1]
    tmp = select_house_to_end + start_to_first_house

    if ans > tmp:
        ans = tmp

print(ans)