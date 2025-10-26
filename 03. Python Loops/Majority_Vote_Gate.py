n = int(input())
yes_count = 0
no_count = 0

for _ in range(n):
    inp = input()
    if inp == "YES":
        yes_count+=1

    if inp == "NO":
        no_count += 1

if yes_count>= no_count:
    print("ACCEPT")
else:
    print("REJECT")