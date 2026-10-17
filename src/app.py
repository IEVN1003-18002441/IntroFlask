from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #decorador o ruta
def index():
    titulo = "Pagina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template("index.html", titulo=titulo, listado=listado)


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