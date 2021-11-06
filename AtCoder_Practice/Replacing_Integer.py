N, K = map(int, input().split())

#Kが1の時とNの時は引いたらいずれ0になるので0
if K == 1 or N == K:
    print(0)

else:
#2^60がだいたい10^18以上になることを予想して60回操作する
    for _ in range(60):
        tmp = N
#任意の回数回引いたことと同じになるので剰余算を選択
        N = tmp%K
#N<Kの時例外が出るので調整(N=4,K=6の時とか)
    M = abs(N-K)
    if N > M:
        N = M

    print(N)

