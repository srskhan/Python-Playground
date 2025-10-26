t = int(input())

good = True
for _ in range(t):
    st = input()
    good = False
    for i in range(len(st)-2):
        if st[i:i+3] == '010' or st[i:i+3] == '101':
            good = True

    if good:
        print("Good")
    else:
        print("Bad")