numbers = input().split()

average_brightness = 0
total=0

for num in numbers:
    total+= int(num)

average_brightness = total/ len(numbers)

if average_brightness < 85:
    print("Dark Image")

if average_brightness>= 85 and average_brightness <=170:
    print("Normal Image")

if average_brightness>170:
    print("Bright Image")