S = input()

if S[0] == S[1]:
    if S[0] == S[2]:
        print(1)

    else:
        print(3)

elif S[0] == S[2]:
    if S[0] == S[1]:
        print(1)
    else:
        print(3)

elif S[1] == S[2]:
        print(3)

else:
    print(6)

################################################

#S = input()
#ans = 3
#if S[0]==S[1] and S[0]==S[2]:
#    ans=1
#elif S[0]!=S[1] and S[0]!=S[2]:
#    ans=6
#print(ans)

################################################