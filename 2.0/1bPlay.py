matrix = [["0"] * 5 for _ in range(5)]

def splitPlainText(plain):
    plain = plain.lower().replace('j', 'i')
    result = []
    for i in range(0, len(plain)-1, 2):
        if plain[i] == plain[i+1]:
            plain = plain[:i+1] + 'x' + plain[i+1:]
    if len(plain) % 2 != 0:
        plain += 'x'
    for j in range(0, len(plain)-1, 2):
        result.append(plain[j] + plain[j+1])
    return result


def createMatrix(key):
    key = key.lower().replace('j', 'i')
    key = list(key)
    letters = "abcdefghiklmnopqrstuvwxyz"
    index = 0
    for i in range(5):
        for j in range(5):
            if index < len(key):
                matrix[i][j] = key[index]
                index += 1
            else:
                while True:
                    letter = letters[0]
                    letters = letters[1:]
                    if letter not in key:
                        matrix[i][j] = letter
                        break
    print(matrix)
    return matrix


def findIndex(mat, x):
    for i in range(5):
        if x in mat[i]:
            return i, mat[i].index(x)


def encrypt(plain, key):
    plainSplit = splitPlainText(plain)
    matrix = createMatrix(key)
    cipherText = ""
    for i in range(len(plainSplit)):
        a = findIndex(matrix, plainSplit[i][0])
        b = findIndex(matrix, plainSplit[i][1])
        if a[0] == b[0]:  # Same row
            cipherText += matrix[a[0]][(a[1] + 1) % 5] + matrix[b[0]][(b[1] + 1) % 5]
        elif a[1] == b[1]:  # Same column
            cipherText += matrix[(a[0] + 1) % 5][a[1]] + matrix[(b[0] + 1) % 5][b[1]]
        else:  # Different row and column
            cipherText += matrix[a[0]][b[1]] + matrix[b[0]][a[1]]
    return cipherText


def main():
    plainText = input("Enter the plain text: ").replace(" ","")
    key = input("Enter the value of Key: ").replace(" ","")
    cipherText = encrypt(plainText, key)
    print("Encrypted Text:", cipherText)


if __name__ == "__main__":
    main()
