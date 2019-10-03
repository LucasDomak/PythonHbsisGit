from flask import Flask, render_template,request, redirect
from models.cerveja import Cerveja

lista_cervejas = []


app=Flask(__name__)

corpo = 'O Leo é lindo'

@app.route('/')
def inc():
    return render_template('tbl.html',titulo='Home',nome=corpo)

@app.route('/listar')
def listar():
    return render_template('listar.html',titulo='Listar', lista = lista_cervejas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html',titulo='Cadastrar')

@app.route('/pedido')
def pedido():
    return render_template('pedido.html',titulo='Pedido', lista = lista_cervejas)

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    tipo = request.form['tipo']
    preco = request.form['preco']
    validade = request.form['validade']

    nova_cerveja = Cerveja(nome, tipo, preco,validade)
    lista_cervejas.append(nova_cerveja)

    return redirect('/listar')
    
    
app.run()