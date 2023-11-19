def splitingPlainText(plain):
    result,count=[],0
    while(count<len(plain)):
        if(plain[count]!=plain[count+1]):
            result.append(plain[count]+plain[count+1])
            count+=2
        elif (plain[count]==plain[count+1]):
            result.append(plain[count]+'x')
            count+=1
        else:
            result.append(plain[count])
    if(len(result[-1])==1):
        temp=result[-1]+'x'
        result.pop()
        result.append(temp)
    print(*result)



splitingPlainText("kavv")