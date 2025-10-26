n = int(input())
inp = input().split()
arr = [int(num) for num in inp]

mn = lambda x: min(x)
mx = lambda x: max(x)

print(mn(arr),mx(arr))