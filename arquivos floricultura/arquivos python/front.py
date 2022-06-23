import json
import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS

def pega_conexao():
    nome_banco = "Floricultura.db"
    con = sqlite3.connect(nome_banco) # Conecta no banco
    return con

    # Aplicação web com Flask
    app = Flask(__name__)
    CORS(app)

    @app.rooute("/")
    def raiz():
        return "Resposta do meu backend em Python!"
     
     @app.route("/todos")
     def todos():
        con = pega_conexao()
        cur = con.cursor()

        try:
         cur.execute("SELECT* FROM Floricultura")
        except:
        con.close()
        return jsonify("Erro ao consultar banco")

        dados = cur.fetchall()
        con.close()
        return jsonify(dados)

        @app.route("/lista/<int:id>") # http://127.0.0.1:500/lista/1
        def lista_um(id):
            con = pega_conexao()
            cur = con.cursor()

            try:
             cur.execute(f"SELECT * FROM Floricultura WHERE id= {id}")
            except:
                con.close()
                return jsonify("Erro ao consultar o banco")
            dados = cur.fetchone()
            com.close()
            if __name__""__main__":
                app.rum()