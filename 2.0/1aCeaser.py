alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Encryption(plain,key):
    result=''
    for i in range(len(plain)):
        if(plain[i]in alphabet):
            temp=alphabet.index(plain[i])
            temp=(temp+key)%26
            result+=alphabet[temp]
    return result
    

plainText=input("Enter the plain text")
key=int(input("Enter the Key :"))
print(Encryption(plainText,key))