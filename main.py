from ensurepip import bootstrap
from os import abort
from flask import Flask, make_response, redirect, request, render_template, abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ["Comprar Cafe", "Enviar solicitud de comrpra", "Enviar video al productor"]


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route("/500")
def error500():
    abort(500)

 
@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))     #-----> Make response redirige al usuario al path hello, se guarda en una variable
    response.set_cookie("user_ip", user_ip)     #-----> Pone una cookie que es igual a la ip del usuario y se va a llamar user_ip

    return response


@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")     #-----> Obtenemos la ip del usuario desde las cookies del browser y no directamente de las request
    context = {
        "user_ip": user_ip,
        "todos": todos,
    }
    return render_template("hello.html", **context)     #-----> Renderea un template en un html 