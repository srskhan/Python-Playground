inp = input().split()

A_count = 0
B_count = 0
for pre in inp:
    if pre == 'A':
        A_count+=1
    if pre == 'B':
        B_count += 1

percent_of_A = (A_count * 100)/ len(inp)

if percent_of_A>70 or percent_of_A <30:
    print("Biased Model")
else:
    print("Fair Model")