
def quick_sort(arr, low, high):
    i = low -1
    pt = arr[high]

    for j in range(low, high):
        if arr[j] <= pt:
            i =i +1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick(arr, low, high):
    if len(arr) == 1:
        return arr
    if low <high:
        qi = quick_sort(arr, low, high)
        quick(arr, low, qi-1)
        quick(arr, qi+1, high)


arr = [5, 12, 6, 9, 3, 45]
n = len(arr)
quick(arr, 0, n-1)

print("Sorted array is")
for i in range(n):
    print(arr[i])
