N = int(input())

count_al = 0
for i in range(1, N+1):
    flag = True
    num = i
    count = 0

    while flag == True:
        if i%2==0:
            count += 1
            i = i/2

        else:
            flag = False

    count_tmp = count
    if count_tmp >= count_al:
        count_al = count_tmp
        ans = num

print(ans)