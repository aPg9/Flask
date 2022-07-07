from flask import Flask, make_response, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))     #-----> Make response redirige al usuario al path hello, se guarda en una variable
    response.set_cookie("user_ip", user_ip)     #-----> Pone una cookie que es igual a la ip del usuario y se va a llamar user_ip

    return response


@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")     #-----> Obtenemos la ip del usuario desde las cookies del browser y no directamente de las request

    return f"Hello World!!! Tu ip es {user_ip}"