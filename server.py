from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import collections, oSemantics, dSemantics
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



@app.route("/sem/opt", methods=["POST", "GET"])
def oSem():
        if request.method == 'POST':
            oldData =  request.form['data']
            Data = oSemantics.getPost(oldData)
            #Data = makeOpt(oldData)            
            print("\nData: \n%s", Data)
            return render_template(
                'o_sem_post.html', data=Data, old=oldData)
        
        return render_template(
        'o_sem_get.html',title="| Semantics : Operatonal")

@app.route("/sem/den", methods=["POST", "GET"])
def dSem():
        if request.method == 'POST':
            oldData =  request.form['data']
            Data = dSemantics.getPost(oldData)
            #Data = makeOpt(oldData)            
            print("\nData: \n%s", Data)
            return render_template(
                'd_sem_post.html', data=Data, old=oldData)
        
        return render_template(
        'd_sem_get.html',title="| Semantics : Denotational")





if __name__ == "__main__":
    app.run(host=host, port=port)
    print("Server has connected to %s on port: %s..." % (host, port))
    