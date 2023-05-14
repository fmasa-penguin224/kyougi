import math

#値をstr型で受け取る
a, b = map(str, input().split())

#文字列を合体後int型へ
heiho = int(a+b)

#値の平方数の小数点以下が0(=True)か判定
flag = math.sqrt(heiho).is_integer()

if flag:
    print("Yes")
else:
    print("Noあああああ")