from flask import Flask,session,render_template,redirect,request
import database


app = Flask(__name__)
app.secret_key = "senha_muito_segura"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cadastro", methods = ["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template("cadastro.html")
    email = request.form["email"]
    senha = request.form["senha"]
    database.criar_conta(email, senha)
    return redirect("/login")
    
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    email = request.form["email"]
    senha = request.form["senha"]
    senha_banco = database.localizar_usuario(email)

    if database.localizar_usuario(email):
        senha_banco = database.localizar_usuario(email)
        if senha == senha_banco[0]:
            session['email'] = email
            return redirect("/menu")
    return "Parece que algo deu errado, tente novamente!"

@app.route("/menu")
def menu():
    return render_template("menu.html")
        
@app.route("/criar_pizza", methods = ["GET", "POST"])
def criar_pizza():
    if request.method == "GET":
        return render_template("criar_pizza.html")
    nome = request.form['nome']
    ingredientes = request.form['ingredientes']
    database.criar_pizza(nome,ingredientes)
    return redirect("/menu")

@app.route ("/editar_pizza")
def editar_pizza():
    pizzas=database.pegar_tipos_de_pizzas()
    return render_template("editar_pizza.html", pizzas = pizzas)

@app.route("/atualizar/<nome>", methods = ["GET", "POST"])
def atualizar_nome_da_pizza(nome):
    if request.method == "GET":
        pizza = database.pegar_uma_pizza(nome)
        return render_template("atualizar_pizza.html", pizza = pizza)
    nome_novo = request.form['nome']
    ingredientes = request.form['ingredientes']
    database.atualizar_pizza(nome_novo,ingredientes,nome)
    return redirect("/editar_pizza")

@app.route("/deletar/<nome>", methods = ["GET"])
def excluir_tipo_de_pizza(nome):
    database.deletar_pizza(nome)
    return redirect ("/editar_pizza")

@app.route("/criar_pedidos_de_pizza", methods = ["GET", "POST"])
def criar_pedidos_de_pizza():
    if request.method == "GET":
        pizzas = database.pegar_tipos_de_pizzas()
        return render_template("criar_pedido.html", pizzas = pizzas)
    
    pizza = request.form['pizza']
    tamanho = request.form['tamanho']
    refri = request.form['refri']
    entrega = request.form['entrega']
    nome = request.form['nome']
    endereco  = request.form['endereco']
    telefone  = request.form['telefone']

    precos_tamanho = {
        "pequena": 35,
        "media": 50,
        "grande": 65,
        "gigante": 80
    }

    refris = {
        "coca_2l": 13,
        "coca_1l": 8,
        "fantau_va_2l": 11,
        "fantau_va_1l": 5,
        "fanta_laranja_2l": 11,
        "fanta_laranja_1l": 5,
        "pepsi_2l": 12,
        "pepsi_1l": 7,
        "nada": 0
    }

    entregas = {
        "com": 15,
        "sem": 0,

    }

    refri_preco = refris.get(refri, 0)
    preco_tamanho = precos_tamanho.get(tamanho, 0)
    entrega_preco = entregas.get(entrega,0)
    preco_final = refri_preco + preco_tamanho + entrega_preco
    print(preco_final)


    database.criar_pedido(pizza,tamanho, preco_tamanho, refri_preco, entrega_preco, nome, endereco, telefone, "Não finalizado", preco_final)
    return redirect ("/criar_pedidos_de_pizza")

@app.route("/ver_pedidos")
def ver_pedidos():
    pedidos = database.pegar_pedidos()
    return render_template("ver_pedidos.html", pedidos= pedidos)

@app.route("/confirmar/<id>")
def confirmar_pedido(id):
    database.confirmar_entrega(id)
    return redirect("/ver_pedidos")


if __name__ == "__main__":
    app.run(debug=True)