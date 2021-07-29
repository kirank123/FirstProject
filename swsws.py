dup = []
new_list = []
def dup_check(word):
    for i in word:
        if not i in dup:
            dup.append(i)
        else:
            new_list.append(i)

    return dup

string = "abcdeab"
list1 =[]
list1[:0] =string
#print(list1)
print(dup_check(list1))
str(list1)

string = "abcdeab"

sss = ''.join(set(string))
print(sss)