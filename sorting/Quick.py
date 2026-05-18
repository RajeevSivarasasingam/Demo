def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)


arr = [64, 34, 25, 12, 22, 11, 90]
arr = quickSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
