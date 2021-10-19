S = input()

na = S.count("a")
nb = S.count("b")
nc = S.count("c")

nm = max(na, nb, nc)

if nm == na:
    print("a")
elif nm == nb:
    print("b")
elif nm == nc:
    print("c")