from flask import Flask,render_template, request, redirect


teste = ('This is a text!')

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index2.html',name=teste)
    
app.run(port=80)