#縦:H, 横:Wのマスを用意
H, W = map(int, input().split())

#角の置ける数
ans=0

#1*1のマスでは1つ置ける
if H==1 or W==1:
    ans = 1

#H*Wの1/2マス置ける,奇数になるときは切り上げ
else:
    ans = int((H*W)/2)
    if (H*W)%2==1:
        ans+=1

print(ans)