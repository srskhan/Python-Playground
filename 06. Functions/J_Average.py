from functools import reduce
n = int(input())

inp = input().split()

numbers = [float(num) for num in inp]

total = reduce(lambda x,y : x+y,numbers)

average = total/n

print(f"{average:.7f}")