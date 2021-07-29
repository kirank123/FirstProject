from random import randint

def quick(array):
    if len(array) <2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array)-1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quick(low) + same + quick(high)



array = [19,2,31,45,6,11,121,27]
print(quick(array))



