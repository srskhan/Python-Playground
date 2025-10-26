
n = int(input())

target = float(input())
average_loss = 0
total_loss = 0
for _ in range(n):
    loss = float(input())
    total_loss += loss

average_loss = total_loss/n

if average_loss <= target:
    print("PASS")
else:
    print("RETRY")