from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import collections
app = Flask(__name__)
host = '127.0.0.1'
port = 3000

# def serveFiles():
#     url_for('./public/style', filename='style.css')
#     url_for('./public/script', filename='script.js')
#     url_for('./public/static', filename='favicon.ico')

@app.route("/")
def index():
     # serveFiles()
    print("Index Page")
    return render_template(
        'index.html',title="")


def makeJSON(text):
    oldData = text.splitlines()
    newData = ""
    for x in range(0, len(oldData)):
        if x == 0 :
            newData += "{\n"
        
        data = "\tline_" + str(x + 1) + " : " + oldData[x] + "\n"
        newData += data

        if(x == len(oldData) - 1):
            newData += "}"

    return newData

def makeOpt(text):
    oldData = text.split()
    newData = ""
    for x in range(0, len(oldData)):
        if x == 0 :
            newData += "{\n"
        
        data = "\tline_" + str(x + 1) + " : " + oldData[x] + "\n"
        newData += data

        if(x == len(oldData) - 1):
            newData += "}"

    return newData

'''
def getBrac(arr):
    bracArr = []
    for x in range(0, len(arr)):
        if arr[x] == '(' or arr[x] == "(":
            print("found")
            #arr[x] = "_"
            for y in range(x + 1, len(arr)):
                print(x + 1, " - ", y)
                print(arr)
                print(arr[y])
                if arr[y] != ')' or arr[y] != ")":
                    bracArr.append(arr[y])
                else:
                    break
            print(bracArr)
            aSize = len(bracArr)
            bracArr = getBrac(bracArr)
            print("Within Brackets(Brac): ", bracArr)
            bracArr = getProd(bracArr)
            print("Within Brackets(Prod): ", bracArr)
            bracArr = getQuot(bracArr)
            print("Within Brackets(Quot): ", bracArr)
            bracArr = getSum(bracArr)
            print("Within Brackets(Sum): ", bracArr)
            bracArr = getDiff(bracArr)
            print("Within Brackets(Diff): ", bracArr)

            arr[y] = "_"

            for y in range(x, len(arr)):
                print("X in underscore replace: ", x)
                if y - x != aSize:
                    arr[y] = "_"
                else:
                    arr[y] = bracArr[len(bracArr) - 1]
                    break

            print("After Brackets: ", bracArr)
            print("After Brackets: ", arr)
            bracArr = []

    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    return newArr
'''

def getProd(arr, text, oldAns):
    #print("OG: ",arr)
    
    for x in range(0, len(arr)):
        if arr[x] == '*' or arr[x] == "*":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                text += "<X * Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                
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
                text += "<X / Y θ> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                
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

def getSum(arr, text, oldAns):
    #text = ""
    for x in range(0, len(arr)):
        if arr[x] == '+' or arr[x] == "+":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                text += "<X + Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                
            a = arr[x - 1]
            b = arr[x + 1] 
            oldAns = arr[x + 1] = str(int(arr[x - 1]) + int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
            text += "<X , θ> ->"+a+"  <Y , θ> ->"+b+"\n" 
            text += "<X + Y , θ -> "+a+" + "+b+"  <"+a+" + "+b+", θ> ↓↓ "+str(arr[x + 1])+"\n"
    
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

def getDiff(arr, text, oldAns):
    #text = ""
    for x in range(0, len(arr)):
        if arr[x] == '-' or arr[x] == "-":
            if x < 1 or x >= len(arr) - 1:
                return -1
            
            if oldAns != 'null':
                text += "<X - Y> ->"+oldAns+"  <Z , θ> ->"+arr[x - 1]+"\n" 
                
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


def getPost(text):
    arr = text.split()
    #arr = getBrac(arr)
    
    ans = getProd(arr, "", 'null')
    print("New Array(Prod): ", ans)
    ans = getQuot(ans["array"], ans["text"], ans["old"])
    print("New Array(Quot): ", ans)
    ans = getSum(ans["array"], ans["text"], ans["old"])
    print("New Array(Sum): ", ans)
    ans = getDiff(ans["array"], ans["text"], ans["old"])
    print("New Array(Diff): ", ans)
    

    return ans["text"]

# def getSem()
    
   



@app.route("/sem/opt", methods=["POST", "GET"])
def oSem():
        if request.method == 'POST':
            oldData =  request.form['data']
            Data = getPost(oldData)
            #Data = makeOpt(oldData)            
            print("\nData: \n%s", Data)
            return render_template(
                'o_sem_post.html', data=Data)
        
        return render_template(
        'o_sem_get.html',title="| Semantics : Operatonal")





if __name__ == "__main__":
    app.run(host=host, port=port)
    print("Server has connected to %s on port: %s..." % (host, port))
    