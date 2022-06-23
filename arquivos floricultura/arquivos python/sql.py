import sqlite3
import os.path
import os

nome_banco = "Floricultura.db"

if os.path.exists(nome_banco): 
    os.unlink(nome_banco)

conexao = sqlite3.connect(nome_banco)
cursor = conexao.cursor()

consulta = """CREAT TABLE Floricultura (
   nome TEXT
    modelo TEXT,
     precos REAL
     )
     """

cursor.execute(consulta)

conexao.close()