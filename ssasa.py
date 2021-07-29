def mul(n):
    if n == 1:
        return 1
    else:
        m = n * mul(n-1)
        return m

for i  in range(1, 11):
    print(mul(i))


###################### Re arranging words in a sentence ########################


def rearrangeTheSentence(sentence):
    sentence = sentence[:-1]
    sentence = sentence.lower()
    words = sentence.split(" ")
    words.sort(key=len)
    newSentence = " ".join(words)
    newSentence = newSentence[0].upper() + newSentence[1:]
    newSentence = newSentence + "."

    return newSentence


sentence = "It is the hottest sun in the beach."
wx = sentence[:-1].lower().split(" ")
wx.sort(key=len, reverse=True)
ns = " ".join(wx)
ns = ns[0].upper() + ns[1:] + "."
print(ns)
print(rearrangeTheSentence(sentence))


##################### Sum of first 100 numbers of a fibinocci ##################

def fibonacci_sum(N):
    if N == 0:
        return 0
    Sum = 0
    a, b = 1, 1
    Sum += a
    while b <= N:
        Sum += b
        a, b = b, a + b
    return Sum

N=100
print(fibonacci_sum(N))


##################### Number of charectors, digits, space in a string #################

import re
s = 'Some String @12344#'
ss = "%#%^$%$^#"

numbers = sum(c.isdigit() for c in s)
letters = sum(c.isalpha() for c in s)
spaces = sum(c.isspace() for c in s)
others = len(s) - numbers - letters - spaces

print(numbers)
print(letters)
print(spaces)
print(others)

print(re.sub("[^0-9]", "", s))
print(re.sub("[^a-zA-Z]", "", s))
print(len(re.sub("[^A-Z]", "", s)))

if re.match(r'^[_\W]+$', ss):
    print("Yes")