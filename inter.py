def rearrangeTheSentence(sentence):
    sentence = sentence[:-1]
    sentence = sentence.lower()
    words = sentence.split(" ")

    words.sort(key=len)
    newSentence = " ".join(words)

    newSentence = newSentence[0].upper() + newSentence[1:]

    newSentence = newSentence + "."

    return newSentence


def DFS(j, visited, zombies, row):
    for k in range(row):
        if zombies[j][k] == '1' and visited[j][k] == False and visited[k][j] == False:
            visited[j][k] = True
            visited[k][j] = True
            DFS(k,visited,zombies, row)

def  zombieCluster(zombies):
    row = len(zombies)
    col = len(zombies[0])
    count = 0
    if row == 0 or col == 0:
        return count
    print(row, col)
    visited = [[False for j in range(col)]for i in range(row)]
    for i in range(row):
        bol = False
        for j in range(row):
            if zombies[i][j] == '1' and visited[i][j] == False and visited[j][i] == False:
                visited[i][j] = True
                visited[j][i] = True
                DFS(j,visited,zombies, row)
                if bol == False:
                    count += 1
                    bol = True
    return count

zombies = ["10011" ,"00110", "11000", "01000", "10101"]
print(zombieCluster(zombies))


def solve(arr, k):
    if len(arr) == 1:
        return arr[0]
        opt = {}
    for i in range(1, k+1):
        opt[-i] = 0

    opt[0] = arr[0]

    for i in range(1, len(arr)):
        opt[i] = max([arr[i] + opt[i-x] for x in range(1, k+1)])

    return opt[len(arr)-1]


