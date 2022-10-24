from app import app
from flask import render_template
#from flask import request
"""from pymongo import MongoClient

client = MongoClient("mongodb+srv://adminuser:adminuser@mygame.t19zp9a.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("clientslandpage") #Trocar caso mude a database
client = db.clients_landpage #Mudar caso mude a tabela"""

@app.route('/')
@app.route('/index')
def index():
    return "Hello World"#render_template('login.html')

"""@app.route('/salvar', methods=['GET'])
def salvar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    data = {"nome":usuario,"senha:":senha}
    client.insert_one(data)
    return """