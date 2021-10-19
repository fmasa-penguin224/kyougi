sum_count, b_count = 0

N, A, B = (int(x) for x in input().split())
S = list(input())

for i in range(N):
    if S[i] == "a":
        if sum_count < A+B:
            sum_count += 1
            print("Yes")

        else:
            print("No")

    elif S[i] == "b":
        b_count += 1
        if sum_count < A+B and b_count <= B:
            sum_count += 1
            print("Yes")

        else:
            print("No")

    elif S[i] == "c":
        print("No")
