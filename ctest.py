'''First repeating number'''

a = [2, 1, 3, 5, 3, 2]
num = []


def first_dup(a):
    for i in range(len(a)):
        if a[i] in num:
            return a[i]
        else:
            num.append(i)

    return "no dup"


print(first_dup(a))

'''First non repeating character from a string'''

s = "aebacabad"
dup = []


def non_rep(s):
    for i in s:
        if not s.count(i) >= 2:
            return i

    return "no rep"


print(non_rep(s))



a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


def rotateImage(a):
    import numpy as np
    N = len(a)
    print(N)
    x = []
    for j in range(N):
        for i in range(N - 1, -1, -1):
            x.append(a[i][j])

    x = np.array_split(x, N)
    for array in x:
        print(list(array))


print(rotateImage(a))

mat = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


def rotateImage(mat):
    N = len(mat)
    # Transpose the matrix
    for i in range(N):
        for j in range(i):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp

    # swap columns
    for i in range(N):
        for j in range(N // 2):
            temp = mat[i][j]
            mat[i][j] = mat[i][N - j - 1]
            mat[i][N - j - 1] = temp

    return mat


print(rotateImage(mat))