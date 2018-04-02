## All prints are displayed in the console
###
# Function that traverses brackets and perform the operations inside
# def getBrac(arr, temp, text, oldAns):
#     bracArr = []
#     newText = ""
#     newAns = ""
#     aLen = len(arr)
#     for x in range(0, aLen):
#         try:
#             if arr[x] == '(' or arr[x] == "(": #If if finds a bracket/parentheses
#                 print("found")
#                 #arr[x] = "_"
#                 y = x + 1
#                 while (y < len(arr)): #Loop for creating a new array with contents of the brackets to run the operations on
                    
#                     print(x + 1, " - ", y) #Just checking that X and Y are in the right place
#                     print(arr)
#                     print(arr[y])
#                     if arr[y] == '(' or arr[y] == "(": #If another bracket is found then
#                         tempArr = arr #the original array is stored in a temp array
#                         tempArr[x] = '_' #and the position with the bracket replaced with "_"
#                         temp = getBrac(tempArr, temp, text, oldAns) #run the bracket function on the temp array
#                         arr = temp["array"] #gets the new array with the answers within the brackets
#                         text += temp["text"] #gets the denotinal text
#                         oldAns = temp["old"] #gets the last answer found
#                         newText += temp["text"] #this is for storing the temp denotinal text to be used in functions further down
#                         newAns = temp["old"] #this is the same as the formeer but for the last answwer found
#                         print("Inner Brackets Done!")
#                         y -= 2
#                         print("Y: ", y, "\nX: ", x)
#                         aLen = len(arr)
#                     elif arr[y] != ')' or arr[y] != ")":
#                         bracArr.append(arr[y]) #if a bracket is not found then the chracter in that position (Y fi dat) is added to the temp array "bracArr"
#                     else:
#                         break
#                     y += 1

#                 print(bracArr)
#                 aSize = len(bracArr) #to be used to add the contents of the temp array, after all functions have run, in the original array 
#                 print("NewText (other): ", newText)
#                 print("NewAns (other): ", newAns)
#                 bracAns = getBrac(bracArr, temp, newText, newAns) #runs the bracket function cuz uk... brackets might be in it <most likely redundant but uk... code>
#                 print("Within Brackets(Brac): ", bracArr)
#                 bracAns = getProd(bracArr, temp, bracAns["text"], bracAns["old"]) #runs the product function
#                 print("Within Brackets(Prod): ", bracAns)
#                 bracAns = getQuot(bracArr, temp, bracAns["text"], bracAns["old"]) #runs the quotient function
#                 print("Within Brackets(Quot): ", bracAns)
#                 bracAns = getSumOrDiff(bracArr, temp, bracAns["text"], bracAns["old"]) #runs the "addition or subtraction" function
#                 print("Within Brackets(Sum): ", bracAns)
#                 #bracArr = getDiff(bracArr)
#                 #print("Within Brackets(Diff): ", bracArr)
#                 text += bracAns["text"] #these are all to ensure that the correct text and last answer is sent to the funciton arguments
#                 oldAns = bracAns["old"]
#                 newText += bracAns["text"]
#                 newAns = bracAns["old"]
#                 print("NewText: ", newText)
#                 print("NewAns: ", newAns)
#                 print("Text: ",text)
#                 print("OldAns: ",oldAns)
#                 arr[y] = "_"

#                 for y in range(x, len(arr)): #for loop that replaces the places where the operations were with "_" until the last index which will be replaced with the answer for the operation
#                     print("X in underscore replace: ", x)
#                     #Y equals X (So if Y minus X is not = to the size of bracArr which will also be the index to store the answer.
#                     #breaks when the answer is added to the original array.
#                     if y - x != aSize:
#                         arr[y] = "_"
#                     else:
#                         arr[y] = bracAns["array"][len(bracAns["array"]) - 1]
#                         break

#                 print("After Brackets: ", bracAns["array"])
#                 print("After Brackets: ", arr)
#                 bracArr = []
                
#         except:
#             break
        

#     newArr = [] #the array to be returned in the list
#     y = 0
#     for x in range(0, len(arr)):
#         if arr[x] == ")": #just to ensure that the ending bracket is replaced
#             arr[x] == "_"
#         if arr[x] != "_":
#             newArr.append(arr[x])
#             y += 1

#     print("NewAraay: ", newArr)
#     print("NewText: ", newText)
#     print("NewAns: ", newAns)
#     ans = { #this is the list to be returned
#         'array': newArr,
#         'text': newText,
#         'old': newAns
#     }
#     return ans


###
# Function responsible for doing Multiplication operations
def getProd(arr, temp, text, oldAns): #pass the array, denotinal text and last answer
    #print("OG: ",arr)
    text += " ↓↓ n"
    for x in range(0, len(temp)): #Checks for multiplication sign
        if temp[x] == '*' or temp[x] == "*":
            if x < 1 or x >= len(temp) - 1: #if the first index is an multiplication sign then return false
                return -1
            
            # if oldAns != 'null': #if a previous operation exceuted, the value derived would added to the denotinal text
            #     if oldAns != arr[x - 1]:
            #         text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
            #     else:
            #         text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 

            textArr = text.split() 
            a = arr[x - 1] #the multiplier 
            b = arr[x + 1] #the multiplicant
            oldAns = arr[x + 1] = str(int(arr[x - 1]) * int(arr[x + 1])) #multiply them and store them as the new oldAns
            arr[x - 1] = "_" #Replace the first charactor with an "_"
            arr[x] = "_" #Replace the second character with an "_"
            #add the next step of operational semantics eto the denotational text
            #textArr[x - 1] = ">" + textArr[x - 1]
            text += "\n"
            for t in range(len(temp)):
                if t == (x - 1):
                     text += ">" + textArr[t] + " "
                else:
                     text += textArr[t] + " "              
            text += " ↓↓ " + textArr[x - 1]

            #same as the former
            text += "\n"
            for t in range(len(temp)):
                if t == (x + 1):
                     text += ">" + textArr[t] + " "
                else:
                     text += textArr[t] + " "
            
            text += " ↓↓ " + textArr[x - 1] + " " + textArr[x] + " " + textArr[x + 1]
    
    newArr = [] #array to be returned in list
    y = 0
    for x in range(0, len(arr)): # this for loop is used to clean up and generate a new array without the "_"
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    ans = { #list to be returned
        'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans

#All the get functions work the same way, they just do a different operaration!!!!!
def getQuot(arr, temp, text, oldAns):
    # text = ""
    #opCount  = 0
    for x in range(0, len(temp)):
        if temp[x] == '/' or [x] == "/":
            if x < 1 or x >= len(temp) - 1:
                return -1
            
            # if oldAns != 'null':
            #     if oldAns != arr[x - 1]:
            #         text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
            #     else:
            #         text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 

            textArr = text.split()    
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(int(arr[x - 1]) / int(arr[x + 1])))
            arr[x - 1] = "_"
            arr[x] = "_"

            text += "\n"
            for t in range(len(temp)):
                if t == (x - 1):
                     text += ">" + textArr[t] + " "
                else:
                     text += textArr[t] + " "              
            text += " ↓↓ " + textArr[x - 1]

            text += "\n"
            for t in range(len(temp)):
                if t == (x + 1):
                     text += ">" + textArr[t] + " "
                else:
                     text += textArr[t] + " "
            
            text += " ↓↓ " + textArr[x - 1] + " " + textArr[x] + " " + textArr[x + 1]
    
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

def getSumOrDiff(arr, temp, text, oldAns):
    #text = ""
    for x in range(0, len(temp)):
        if temp[x] == '+' or temp[x] == "+":
            if x < 1 or x >= len(temp) - 1:
                return -1
            
            # if oldAns != 'null':
            #     if oldAns != arr[x - 1]:
            #         text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
            #     else:
            #         text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 
            
            textArr = text.split()
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) + int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            
            text += "\n"
            for t in range(len(temp)):
                if t == (x - 1):
                     text += ">" + textArr[t] + " "
                else:
                     text += textArr[t] + " "              
            text += " ↓↓ " + textArr[x - 1]

            text += "\n"
            for t in range(len(temp)):
                if t == (x + 1):
                     text += ">" + textArr[t] + " "
                else:
                     text += textArr[t] + " "
            
            text += " ↓↓ " + textArr[x - 1] + " " + textArr[x] + " " + textArr[x + 1]

        elif temp[x] == '-' or temp[x] == "-":
            if x < 1 or x >= len(temp) - 1:
                return -1
            
            # if oldAns != 'null':
            #     if oldAns != arr[x - 1]:
            #         text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
            #     else:
            #         text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x + 1]+"\n" 

            textArr = text.split()   
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) - int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            
            text += "\n"
            for t in range(len(temp)):
                if t == (x - 1):
                     text += ">" + textArr[t] + " "
                else:
                     text += textArr[t] + " "              
            text += " ↓↓ " + textArr[x - 1]

            text += "\n"
            for t in range(len(temp)):
                if t == (x + 1):
                     text += ">" + textArr[t] + " "
                else:
                     text += textArr[t] + " "
            
            text += " ↓↓ " + textArr[x - 1] + " " + textArr[x] + " " + textArr[x + 1]

    # newArr = []
    # y = 0
    # for x in range(0, len(arr)):
    #     if arr[x] != "_":
    #         newArr.append(arr[x])
    #         y += 1

    ans = {
        #'array': newArr,
        'text': text,
        'old': oldAns
    }
    return ans


def makeDenotationalString(arr):
    text = ""
    count = 0
    for x in range(0, len(arr)):
        if arr[x] == '*' or arr[x] == '/' or arr[x] == '+' or arr[x] == '-' or arr[x] == '(' or arr[x] == ')':
            text += arr[x] + " "
        else:
            count += 1
            text += "e" + str(count) + " "
    
    return text


def getPost(text):
    arr = text.split()
    dText = makeDenotationalString(arr)
    temp = arr
    #arr = getBrac(arr)
    
    # ans = getProd(arr, temp, dText, 'null')
    # print("New Array(Prod): ", ans)
    #ans = getBrac(arr, temp, "", 'null')
    ans = getProd(arr, temp, dText, 'null')
    print("New Array(Prod): ", ans)
    ans = getQuot(arr, temp, ans["text"], ans["old"])
    print("New Array(Quot): ", ans)
    ans = getSumOrDiff(arr, temp, ans["text"], ans["old"])
    print("New Array(Sum): ", ans)
    ans["text"] += "\n" + dText + " ↓↓ " + ans["old"]
    # #ans = getDiff(ans["array"], ans["text"], ans["old"])
    # #print("New Array(Diff): ", ans)
    

    return ans["text"]