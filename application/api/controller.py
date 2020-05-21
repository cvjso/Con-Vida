import flask
from application import app # Aqui eu importo o app da aplicação

@app.route("/") # Rota que pode ser acessada
def hello():
    return "Hello World" # Retorno da minha rota
