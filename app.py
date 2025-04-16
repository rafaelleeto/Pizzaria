from flask import Flask,session,render_template,redirect,request
import database


app = Flask(__name__)
app.secret_key = "senha_muito_segura"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cadastro",methods = ["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template("cadastro.html")
    email = request.form["email"]
    senha = request.form["senha"]
    database.criar_conta(email, senha)
    return redirect("/login")
    
    
    
    


@app.route("/login",methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    



if __name__ == "__main__":
    app.run(debug=True)