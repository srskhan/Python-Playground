n = int(input())
t = input().split()
lst = []
for i in t:
    x = int(i)
    lst.append(x)

tup = tuple(lst)

print(hash(tup))
