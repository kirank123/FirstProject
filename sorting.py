from random import randint
from timeit import repeat


##Bubble sort -O(n^2)
def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for id in range(i):
            if list[id] > list[id+1]:
                list[id], list[id+1] = list[id+1], list[id]


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)
print(list[-2])
print("hahah")


##Insertion sort -O(n^2)
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array


array = [19,2,31,45,6,11,121,27]
insertion_sort(array)
print(array)


#Binary search -O(log n)
#Array need to be sorted already
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


arr = [2, 3, 4, 10, 40,45,6,11,121,27]
x = 10
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


#Quick sort - O(log2n)
def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


print("Quick Sort")
array = [19,2,31,45,6,11,121,27]
print(quicksort(array))


ARRAY_LENGTH=1000
if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

#    bubblesort(array)
#    print(array)
#    print(len(array))




# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = {**dict1, **dict2}
print(dict3)


contestants = { 'Randy Orton': 'Red', 'Dwayne Johnson' : 'Blue' }
contestants['Jhon Cena'] = 'Red'
contestants['Dave Bautista'] = 'Blue'
del contestants['Dwayne Johnson']

print(contestants)


