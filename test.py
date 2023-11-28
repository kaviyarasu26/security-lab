#row and column 
def Encryption(text,key):
    Matrix=[['' for _ in range(len(text))] for _ in range(key)]
    print(Matrix)
    row=0
    column=0
    direction_down=0
    for i in range(len(text)):
            print(i)
            if(row==0) or (row==key-1):
                  direction_down=not direction_down
            Matrix[row][column]=text[i]
            column+=1
            if direction_down:
                  row+=1
            else:
                  row-=1
    result=''
    for i in Matrix:
          print(i)
          for j in i:
                if(j!=''):
                      result+=j
    print(result)

Encryption("iamthekingofmyworld",2)