from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
app = Flask(__name__)
host = '127.0.0.1'
port = 3000

def serveFiles():
    url_for('./public/style', filename='style.css')
    url_for('./public/script', filename='script.js')
    url_for('./public/static', filename='favicon.ico')

@app.route("/")
def index():
     # serveFiles()
    print("Index Page")
    return render_template(
        'index.html',title="")

@app.route("/login", methods=["POST", "GET"])
def login():
        if request.method == 'POST':
            return render_template(
                'dashboard.html', name=request.form["uname"])
        
        return render_template(
        'login.html',title="| Login")

@app.route("/register")
def register():
        #serveFiles()
        return render_template(
        'register.html',title="| Register")


@app.route("/sem/opt", methods=["POST", "GET"])
def oSem():
        if request.method == 'POST':
            oldData = request.form["data"].splitlines()
            newData = ""
            for x in range(0, len(oldData)):
                if x == 0 :
                    newData += "{\n"
                
                data = "\tline_" + str(x + 1) + " : " + oldData[x] + "\n"
                newData += data

                if(x == len(oldData) - 1):
                    newData += "}"
            
            
            print("\nData: \n%s", newData)
            return render_template(
                'o_sem_post.html', data=newData)
        
        return render_template(
        'o_sem_get.html',title="| Semantics : Operatonal")





if __name__ == "__main__":
    app.run(host=host, port=port)
    print("Server has connected to %s on port: %s..." % (host, port))
    