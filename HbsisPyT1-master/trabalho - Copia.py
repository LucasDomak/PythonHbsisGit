from flask import Flask, render_template,request, redirect
from models.invest import Invest

lista_investimentos = []

corpo = 'only the gods are here'

app=Flask(__name__)

corpo = 'Olá! Seja  bem vindo! Venha conhecer nosso site de investimento!'
@app.route('/')
def inc():
    return render_template('tbl.html',titulo='Home',nome=corpo)

@app.route('/listar')
def listar():
    return render_template('listar.html',titulo='Listar', lista = lista_investimentos)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html',titulo='Cadastrar')

@app.route('/pedido')
def pedido():
    return render_template('pedido.html',titulo='Pedido', lista = lista_investimentos)

@app.route('/salvar', methods=['POST'])
def salvar():
    
    nome = request.form['nome']
    tipo = request.form['tipo']
    valor = request.form['valor']
    rendimento_investimento = request.form['rendimento_investimento']

    novo_investimento = Invest(nome, tipo, valor,rendimento_investimento)
    lista_investimentos.append(novo_investimento)

    return redirect('/listar')
    
    
app.run()