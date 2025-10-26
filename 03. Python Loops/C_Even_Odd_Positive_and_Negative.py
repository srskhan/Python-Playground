n = int(input())

inp = input()
numbers = inp.split()

even = 0
odd = 0
positive = 0
negateive = 0
for i in range(n):
    x = int(numbers[i])
    if(x%2 == 0):
        even+=1
    else:
        odd += 1

    if(x>0):
        positive+=1
    if(x<0):
        negateive+=1
    
print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:",negateive)
