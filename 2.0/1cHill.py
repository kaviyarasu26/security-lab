import numpy as np
letters = "abcdefghijklmnopqrstuvwxyz"

def createKeyMatrix(n):
    keyMatrix=[[0]*n for _ in range(n)]
    for i in range (n):
        for j in range(n):
            keyMatrix[i][j]=int(input(f"Enter the value {i+1},{j+1} :"))
    """for row in keyMatrix:
        print(row)"""
    return keyMatrix

def findTheIndex(x):
    return letters.index(x)

def en(plainMat, keyMat): 
    a = np.array(plainMat)
    b = np.array(keyMat)
    
    print(a)
    print(b)
    result = np.dot(b,a)
    result=np.mod(result,26)
    return result


def de(ChiperMat,keyMat):
    pass


def main():
    Mat=createKeyMatrix(int(input("Enter the value of n for n*n matrix :")))
    plainText=input("Enter the plain text (length of plain must be equal to {n}) :").lower()
    plainTextMat=[]
    for i in plainText:
        plainTextMat.append([findTheIndex(i)])
    print(plainTextMat)
    enMat=en(plainTextMat,Mat)
    print(enMat)
    encoding=''
    for i in range (len(enMat)):
        print(letters[enMat[i][0]])

    #print()
    #pass



if __name__=="__main__":
    main()