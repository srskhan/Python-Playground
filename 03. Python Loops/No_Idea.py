inp = input().split()
 
n = int(inp[0])
m = int(inp[1])

arr = input().split()
happiness = 0
a_set = set(input().split())
b_set = set(input().split())


for item in arr:
    if item in a_set:
        happiness += 1
    if item in b_set:
        happiness -= 1

print(happiness) 

