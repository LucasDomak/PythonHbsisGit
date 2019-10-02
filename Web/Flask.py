from flask import Flask,render_template, request, redirect
from alunos import Alunos

pagina_nome ='Lista Alunos'
aluno1 = Alunos('Lucas Alfredo',' da Silva', 47999705773)
aluno2 = Alunos('Tito',' o lindo', 47997534229)
aluno3 = Alunos('Gustavo',' Henrique', 47999705774)
lista_alunos = [aluno1,aluno2,aluno3]

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome=pagina_nome, lista=lista_alunos)


@app.route('/novo')   
def novo():
    return render_template('novo.html') 


@app.route('/salvar',methods=['POST'])   
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    novo_aluno = Alunos(nome,sobrenome,telefone)
    lista_alunos.append(novo_aluno)
    return redirect('/')

app.run()