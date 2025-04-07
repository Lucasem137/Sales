#importando a biblioteca do SQLite3 e o Flask
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

#iniciando o flask
app = Flask(__name__)

#funçao que cria a tabela e o arquivo 'vendas.db' caso nao tenha
def init_db():
    con = sqlite3.connect("vendas.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS vendas
                 (id INTEGER PRIMARY KEY, produto TEXT, 
                quantidade INTEGER, preco REAL, data TEXT)""")
    #salvando
    con.commit()
    con.close()

#definindo a rota do principal do app
@app.route('/')
#funçao que é chamada após a rota principal ser acessada
def index():
    #mostrando as vendas
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM vendas')
    #armazenando as vendas em uma lista
    vendas = cur.fetchall()
    con.close()
    #enviando a lista para o html
    return render_template('index.html', vendas=vendas)

#rota para adicionar vendas aceita apenas 'POST'
@app.route('/add', methods=['POST'])
def add():
    # o request.form é para introduzir as informações dadas pelo usuario
    produto = request.form['produto']
    quantidade = request.form['quantidade']
    preco = request.form['preco']
    data = request.form['data']
    #inserindo no sql
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()
    cur.execute("INSERT INTO vendas (produto, quantidade, preco, data) VALUES (?, ?, ?, ?)",
                 (produto, quantidade, preco, data))
    
    con.commit()
    con.close()
    #redireciona o usuário a página principal após registrar uma venda
    return redirect(url_for('index'))

#rota para remover vendas aceita apenas 'POST'
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()
    #removendo venda pelo id dela
    cur.execute('DELETE FROM vendas WHERE id = ?', (id,))
    con.commit()
    con.close()
    return redirect(url_for('index'))

#rota para editar alguma venda aceita 'GET' e 'POST'
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()
    #quando é usado o POST ele altera
    if request.method == 'POST':
        produto = request.form['produto']
        quantidade = request.form['quantidade']
        preco = request.form['preco']
        data = request.form['data']
        cur.execute('UPDATE vendas SET produto = ?, quantidade = ?, preco = ?, data = ? WHERE id = ?', (produto, quantidade, preco, data, id))
        con.commit()
        con.close()
        return redirect(url_for('index'))
    #Caso não use ele usa apenas o GET que busca os dados da venda
    else:
        cur.execute('SELECT * FROM vendas WHERE id = ?', (id,))
        venda = cur.fetchone()
        con.close()
        return render_template('edit.html', venda=venda)

#rota para filtrar as vendas usando 'GET' e 'POST'
@app.route('/filter', methods=['GET', 'POST'])
def filter():
    con = sqlite3.connect('vendas.db')
    cur = con.cursor()
    #consulta no SQL
    query = 'SELECT * FROM vendas WHERE 1=1'
    #parametros da consulta
    params = []
    if request.method == 'POST':
        produto = request.form.get('produto')
        data = request.form.get('data')
        #consulta por produto
        if produto:
            query += ' AND produto LIKE ?'
            params.append(f'%{produto}%')
        #consulta por data
        if data:
            query += ' AND data = ?'
            params.append(data)
            
    cur.execute(query, params)
    vendas = cur.fetchall()
    con.close()
    #volta apenas as filtradas
    return render_template('index.html', vendas=vendas)

#inicializando o app 
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

