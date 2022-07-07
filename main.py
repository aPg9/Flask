from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    user_ip = request.remote_addr     #----- > Regresa la ip que se obtiene desde la peticion del browser
    return f"Hello World Flask, tu ip es {user_ip}"