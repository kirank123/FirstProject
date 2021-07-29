

dict1 = {'a': 23, 'g': 67, 'e': 12, 'd': 90}

for val in sorted(dict1, key=dict1.get):
    print(val, dict1[val])


values = [x for x in dict1.keys()]
#print(values)


def sort(arr):
    lent = len(values)
    for i in range(lent -1):
        for j in range(0, lent-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(sort(values))



str = "abbbeeecdeb "
num = {}
for i in str:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1

print(max(num, key=num.get))


a = [1, 2, 3, 4]
b = [4, 2, 5, 6, 3]
l1 = a + b
print(list(set(l1)))

