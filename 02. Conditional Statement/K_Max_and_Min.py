val = input()
numbers = val.split()
 
num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])
 
mn = num1
mx = num1
#min
if(num2<mn):
    mn = num2
if(num3 < mn):
    mn = num3
 
#max 
if(num2>mx):
    mx = num2
if(num3>mx):
    mx = num3
print(f"{mn} {mx}")