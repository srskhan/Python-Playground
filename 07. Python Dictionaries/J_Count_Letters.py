characters = input()

dic = {}
for c in characters:
    dic[c] = dic.get(c,0) + 1

for key in sorted(dic.keys()):
    print(f"{key} : {dic[key]}")