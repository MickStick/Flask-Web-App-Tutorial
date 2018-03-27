
def getBrac(arr, text, oldAns):
    bracArr = []
    newText = ""
    newAns = ""
    aLen = len(arr)
    for x in range(0, aLen):
        try:
            if arr[x] == '(' or arr[x] == "(":
                print("found")
                #arr[x] = "_"
                y = x + 1
                while (y < len(arr)):
                    
                    print(x + 1, " - ", y)
                    print(arr)
                    print(arr[y])
                    if arr[y] == '(' or arr[y] == "(":
                        tempArr = arr
                        tempArr[x] = '_'
                        temp = getBrac(tempArr, text, oldAns)
                        arr = temp["array"]
                        text += temp["text"]
                        oldAns = temp["old"]
                        newText += temp["text"]
                        newAns = temp["old"]
                        print("Inner Brackets Done!")
                        y -= 2
                        print("Y: ", y, "\nX: ", x)
                        aLen = len(arr)
                    elif arr[y] != ')' or arr[y] != ")":
                        bracArr.append(arr[y])
                    else:
                        break
                    y += 1

                print(bracArr)
                aSize = len(bracArr)
                print("NewText (other): ", newText)
                print("NewAns (other): ", newAns)
                bracAns = getBrac(bracArr, newText, newAns)
                print("Within Brackets(Brac): ", bracArr)
                bracAns = getProd(bracAns["array"], bracAns["text"], bracAns["old"])
                print("Within Brackets(Prod): ", bracAns)
                bracAns = getQuot(bracAns["array"], bracAns["text"], bracAns["old"])
                print("Within Brackets(Quot): ", bracAns)
                bracAns = getSumOrDiff(bracAns["array"], bracAns["text"], bracAns["old"])
                print("Within Brackets(Sum): ", bracAns)
                #bracArr = getDiff(bracArr)
                #print("Within Brackets(Diff): ", bracArr)
                text += bracAns["text"]
                oldAns = bracAns["old"]
                newText += bracAns["text"]
                newAns = bracAns["old"]
                print("NewText: ", newText)
                print("NewAns: ", newAns)
                print("Text: ",text)
                print("OldAns: ",oldAns)
                arr[y] = "_"

                for y in range(x, len(arr)):
                    print("X in underscore replace: ", x)
                    if y - x != aSize:
                        arr[y] = "_"
                    else:
                        arr[y] = bracAns["array"][len(bracAns["array"]) - 1]
                        break

                print("After Brackets: ", bracAns["array"])
                print("After Brackets: ", arr)
                bracArr = []
                
        except:
            break
        

    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] == ")":
            arr[x] == "_"
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    print("NewAraay: ", newArr)
    print("NewText: ", newText)
    print("NewAns: ", newAns)
    ans = {
        'array': newArr,
        'text': newText,
        'old': newAns
    }
    return ans


def getProd(arr, text, oldAns):
    #print("OG: ",arr)
    
    for x in range(0, len(arr)):
        if arr[x] == '*' or arr[x] == "*":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                if oldAns != arr[x - 1]:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                else:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) * int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X * Y , θ -> "+a+" * "+b+"  <"+a+" * "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = {
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans

def getQuot(arr, text, oldAns):
    # text = ""
    #opCount  = 0
    for x in range(0, len(arr)):
        if arr[x] == '/' or arr[x] == "/":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                if oldAns != arr[x - 1]:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                else:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(int(arr[x - 1]) / int(arr[x + 1])))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X / Y , θ -> "+a+" / "+b+"  <"+a+" / "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = {
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans

def getSumOrDiff(arr, text, oldAns):
    #text = ""
    for x in range(0, len(arr)):
        if arr[x] == '+' or arr[x] == "+":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                if oldAns != arr[x - 1]:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                else:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) + int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X + Y , θ -> "+a+" + "+b+"  <"+a+" + "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
        elif arr[x] == '-' or arr[x] == "-":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                if oldAns != arr[x - 1]:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                else:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) - int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X - Y , θ -> "+a+" - "+b+"  <"+a+" - "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = {
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans

'''
def getDiff(arr, text, oldAns):
    #text = ""
    for x in range(0, len(arr)):
        if arr[x] == '-' or arr[x] == "-":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                if oldAns != arr[x - 1]:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                else:
                    text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) - int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X - Y , θ -> "+a+" - "+b+"  <"+a+" - "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = {
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans
'''

def getPost(text):
    arr = text.split()
    #arr = getBrac(arr)
    
    # ans = getProd(arr, "", 'null')
    # print("New Array(Prod): ", ans)
    ans = getBrac(arr, "", 'null')
    ans = getProd(ans["array"], ans["text"], ans["old"])
    print("New Array(Prod): ", ans)
    ans = getQuot(ans["array"], ans["text"], ans["old"])
    print("New Array(Quot): ", ans)
    ans = getSumOrDiff(ans["array"], ans["text"], ans["old"])
    print("New Array(Sum): ", ans)
    #ans = getDiff(ans["array"], ans["text"], ans["old"])
    #print("New Array(Diff): ", ans)
    

    return ans["text"]