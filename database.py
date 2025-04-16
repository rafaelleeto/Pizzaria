import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("pedidos.db")
    return conexao

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario
                   (email TEXT PRIMARY KEY,
                   senha TEXT KEY)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                   id INTEGER PRIMARY KEY,
                   nome_pizza TEXT, 
                   tamanho_pizza TEXT,
                   preco_pizza REAL,
                   preco_refri REAL,
                   preco_entrega REAL,
                   preco_borda REAL,
                   endereco TEXT,
                   telefone TEXT,
                   nome_cliente TEXT
                   )   ''')
    
    
if __name__=="__main__":
    criar_tabelas()