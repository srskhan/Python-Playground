n = int(input())

inp = input()

numbers = inp.split()
position = 1

lowest_number = int(numbers[0])

for i, num in enumerate(numbers):
    num = int(num)
    if(num<lowest_number):
        lowest_number = num
        position = i +1

print(lowest_number,position)


