#何回交換されるか数える関数
def judge(A, B, C):
    count = 0
    #   A<B<Cだとすると最大値と最小値の差はC-Aで,1回目の操作後その差は(C-A)/2となる
    #   N回目の交換でその差は(C-A)/2**Nとなるため10**9程度の数値ではlog_2(10**9)=30~40回程度の交換でその差はiになる
    for i in range(40):
        # 奇数になったら終了
        if A%2==1:
            return i
        elif B%2==1:
            return i
        elif C%2==1:
            return i

        count += 1

        tmp_A = A
        tmp_B = B
        tmp_C = C

        A = (tmp_B + tmp_C)//2
        B = (tmp_A + tmp_C)//2
        C = (tmp_A + tmp_B)//2
    #40回交換しても奇数にならなければ全ての入力が同じ数である
    return -1

A, B ,C = map(int, input().split())

ans = judge(A, B, C)

print(ans)