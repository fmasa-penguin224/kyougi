K, N = map(int, input().split())

A = list(map(int, input().split()))

#湖のスタートラインを超えない場合
ans = A[N-1] - A[0]

#湖のスタートラインを超える場合
for i in range(N):
#選択した家から湖のスタートラインまでの距離
    select_house_to_end = K - A[i]
#湖のスタートラインから選択された家の一つ前の家までの距離
    start_to_first_house = A[i-1]
    tmp = select_house_to_end + start_to_first_house

    if ans > tmp:
        ans = tmp

print(ans)