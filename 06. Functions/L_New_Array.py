def concatinate_array(a,b):
    return b+a

n = int(input())
a= input().split()
b= input().split()
arr1 = [int(num) for num in a]
arr2 = [int(num) for num in b]

arr3 = concatinate_array(arr1,arr2)

for num in arr3:
    print(num, end= " ")
