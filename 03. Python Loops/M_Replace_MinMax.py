n = int(input())

arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

max_val = max(arr)
min_val = min(arr)

max_idx = arr.index(max_val)
min_idx = arr.index(min_val)

arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]

for x in arr:
    print(x, end=' ')