from flask import Flask, render_template, request
import math
app = Flask(__name__)

@app.route("/") #decorador o ruta
def index():
    titulo = "Pagina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template("index.html", titulo=titulo, listado=listado)


@app.route("/operasbas", methods=["GET","POST"]) #decorador o ruta
def operasbas():
    n1=0
    n2=0
    res=0
    operacion=''
    simbolo = ''
    if request.method=='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')

        if request.form.get('operacion')=='sumar':
            res=float(n1)+float(n2)
            simbolo = '+'
            operacion ='suma'
        if request.form.get('operacion')=='restar':
            res=float(n1)-float(n2)
            simbolo = '-'
            operacion ='resta'
        if request.form.get('operacion')=='multiplicar':
            res=float(n1)*float(n2)
            simbolo = '*'
            operacion ='multiplicacion'
        if request.form.get('operacion')=='dividir':
            res=float(n1)*float(n2)
            simbolo = '/'
            operacion ='division'
    return render_template('operasbas.html', n1=n1,n2=n2, res=res, operacion=operacion, simbolo=simbolo )

@app.route("/distancia", methods=["GET","POST"]) #decorador o ruta
def distancia():
    n1=0
    n2=0
    n3=0
    n4=0
    res=0
    
    if request.method=='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        n3=request.form.get('n3')
        n4=request.form.get('n4')

        res = math.sqrt( ((float(n1) - float(n2)) ** 2) + ((float(n3) - float(n4)) ** 2))
    return render_template('distancia.html', n1=n1,n2=n2, n3=n3, n4=n4,res=res, )


@app.route("/hola")
def hola():
    return "<h1> hola PWA - IEVN1003 </h1> "

# Como pasar parametros por url

@app.route("/user/<string:nom>") 
def user(nom):
    return "<h1> Hola User:{} </h1>  ".format(nom)


@app.route("/numero/<int:n>") 
def numero(n):
    return "Numero: {}".format(n)


@app.route("/user/<int:id>/<string:username>")  # <- Corrección: Se agregó la barra '/' separadora
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)


@app.route("/suma/<float:n1>/<float:n2>") 
def func(n1, n2):
    return "la suma es : {}".format(n1 + n2)


 

if __name__ == "__main__":
    app.run(debug=True)