letters='abcdefghijklmnopqrstuvwxyz'
        



def Index(x):
    return letters.index(x)


def main():
    plaintext=input("Enter the plain text :").replace(" ","").lower()
    key=input("Enter the key :").lower().replace(" ","")
    #print("plain letter || key  ||  index-p    || index-K  || final")
    result=''
    for i in range(len(plaintext)):
        letter1=plaintext[i]
        letter2=key[i%len(key)]
        a=Index(letter1)
        b=Index(letter2)
        temp=(a+b)%25
        result+=letters[temp]
        print(f'{letter1} ||  {letter2}||{a} || {b} || {temp}')
    print(result)
        
    


    



main()