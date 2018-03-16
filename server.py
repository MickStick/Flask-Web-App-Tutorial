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

def getProd(arr):
    for x in range(0, len(arr)):
        if arr[x] == '*' or arr[x] == "*":
            if x < 1 or x >= len(arr) - 1:
                return -1
            arr[x + 1] = str(int(arr[x - 1]) * int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    return newArr

def getQuot(arr):
    for x in range(0, len(arr)):
        if arr[x] == '/' or arr[x] == "/":
            if x < 1 or x >= len(arr) - 1:
                return -1
            arr[x + 1] = str(int(int(arr[x - 1]) / int(arr[x + 1])))
            arr[x - 1] = "_"
            arr[x] = "_"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    return newArr

def getSum(arr):
    for x in range(0, len(arr)):
        if arr[x] == '+' or arr[x] == "+":
            if x < 1 or x >= len(arr) - 1:
                return -1
            arr[x + 1] = str(int(arr[x - 1]) + int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    return newArr

def getDiff(arr):
    for x in range(0, len(arr)):
        if arr[x] == '-' or arr[x] == "-":
            if x < 1 or x >= len(arr) - 1:
                return -1
            arr[x + 1] = str(int(arr[x - 1]) - int(arr[x + 1]))
            arr[x - 1] = "_"
            arr[x] = "_"
    
    newArr = []
    y = 0
    for x in range(0, len(arr)):
        if arr[x] != "_":
            newArr.append(arr[x])
            y += 1

    return newArr


def getAnswer(text):
    arr = text.split()
    arr = getProd(arr)
    print("New Array(Prod): ", arr)
    arr = getQuot(arr)
    print("New Array(Quot): ", arr)
    arr = getSum(arr)
    print("New Array(Sum): ", arr)
    arr = getDiff(arr)
    print("New Array(Diff): ", arr)

    return arr
    
   



@app.route("/sem/opt", methods=["POST", "GET"])
def oSem():
        if request.method == 'POST':
            oldData =  request.form['data']
            Data = getAnswer(oldData)
            #Data = makeOpt(oldData)            
            print("\nData: \n%s", Data)
            return render_template(
                'o_sem_post.html', data=Data)
        
        return render_template(
        'o_sem_get.html',title="| Semantics : Operatonal")





if __name__ == "__main__":
    app.run(host=host, port=port)
    print("Server has connected to %s on port: %s..." % (host, port))
    