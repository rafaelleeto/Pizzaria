import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("pedidos.db")
    return conexao

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                   (email TEXT PRIMARY KEY,
                   senha TEXT KEY)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                   id INTEGER PRIMARY KEY,
                   nome_pizza TEXT, 
                   tamanho_pizza TEXT,
                   preco_pizza REAL,
                   preco_refri REAL,
                   preco_entrega REAL,
                   endereco TEXT,
                   telefone TEXT,
                   nome_cliente TEXT,
                   status TEXT,
                   preco_final REAL
                   )   ''')
    

    cursor.execute('''CREATE TABLE IF NOT EXISTS tipos (
                   nome TEXT primary key,
                   ingredientes TEXT
                   )   ''')

def criar_conta(email, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    # Sistema interno não precisa de criptograficação das senhas
    cursor.execute("""INSERT INTO usuarios VALUES (?,?)""",(email, senha))
    conexao.commit()
    cursor.close()

def localizar_usuario(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT senha FROM usuarios WHERE email=?""",(email,))
    return cursor.fetchone()

def criar_pizza(nome, ingredientes):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO tipos VALUES (?,?)""",(nome, ingredientes))
    conexao.commit()
    cursor.close()

def pegar_tipos_de_pizzas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM tipos""")
    return cursor.fetchall()

def pegar_uma_pizza(nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM tipos where nome=?""",(nome,))
    return cursor.fetchone()

def atualizar_pizza(nome_novo, ingredientes, nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""UPDATE tipos set nome=?, ingredientes=? where nome=?""",(nome_novo, ingredientes, nome))
    conexao.commit()
    cursor.close()

def deletar_pizza(nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""DELETE FROM tipos WHERE nome=? """,(nome,))
    conexao.commit()
    cursor.close()

def criar_pedido(pizza,tamanho,preco,refri,entrega,nome,endereco,telefone,status,preco_final):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO pedidos (nome_pizza, tamanho_pizza, preco_pizza, preco_refri, preco_entrega, nome_cliente, endereco, telefone, status, preco_final)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (pizza, tamanho, preco, refri, entrega, nome, endereco, telefone, status,preco_final))    
    conexao.commit()
    cursor.close()

def pegar_pedidos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM pedidos """)
    return cursor.fetchall()

def confirmar_entrega(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT status FROM pedidos WHERE id=?""",(id,))
    variavel = cursor.fetchone()
    if variavel[0] == "Entregue":
        cursor.execute("""UPDATE pedidos SET status=? WHERE id=?""",("Não finalizado",id))
    else:
        cursor.execute("""UPDATE pedidos SET status=? WHERE id=?""",("Entregue",id))
    conexao.commit()
    cursor.close()

def pegar_um_tipo(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM pedidos WHERE id=?""",(id,))
    return cursor.fetchone()

def atualizar_pedido(nome,tamanho,preco,preco_refri,preco_entrega,nome_cliente,endereco,telefone,status,preco_final,id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""UPDATE pedidos set nome_pizza=?, tamanho_pizza=?, preco_pizza=?, preco_refri=?, preco_entrega=?, nome_cliente=?, endereco=?,
                    telefone=?, status=?, preco_final=? WHERE id=?""",(nome,tamanho,preco,preco_refri,preco_entrega,nome_cliente,endereco,telefone,status,preco_final, id,))
    conexao.commit()
    cursor.close()

def lucro_total():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(preco_final) FROM pedidos WHERE status = ?", ("Entregue",))
    return cursor.fetchone()[0]
        

if __name__=="__main__":
    criar_tabelas()