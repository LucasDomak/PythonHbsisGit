from flask import Flask,render_template
from alunos import Alunos

pagina_nome ='Lista Alunos'
aluno1 = Alunos('Lucas Alfredo', 47999705773)
aluno2 = Alunos('Tito', 47997534229)
aluno3 = Alunos('Gustavo', 47999705774)
lista_alunos = [aluno1,aluno2,aluno3]

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome=pagina_nome, lista=lista_alunos)
app.run()


