import sqlite3
import os.path
import os

nome_banco = "Floricultura.db"

if os.path.exists(nome_banco):
    os.unlink(nome_banco)

conexao = sqlite3.connect(nome_banco)
cursor = conexao.cursor()

consulta = """CREATE TABLE Produtos(
   id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Nome TEXT,
    preco REAL
    )
    """
cursor.execute(consulta)


# conexao.commit()
conexao.close()