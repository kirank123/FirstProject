def bin_search(arr, low, high, x):
    if high > low:
        mid =(high + low)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] >x:
            return bin_search(arr, low, mid-1, x)
        else:
            return bin_search(arr, mid +1, high, x)

    else:
        print("Element not found")
        return -1


arr = ['a', 'b', 'c', 'd']
x = 'c'

res = bin_search(arr, 0, len(arr)-1, x)
if res != -1:
    print(f"element present at {str(res)}")
else:
    print("Element not found")

