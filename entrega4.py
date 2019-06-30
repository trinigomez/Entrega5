from flask import Flask, render_template, request, abort, json
from pymongo import MongoClient
import pandas as pd
import os
import atexit
import subprocess

uri = "mongodb://grupo30:grupo30@146.155.13.149/grupo30?authSource=admin"
# La uri 'estándar' es "mongodb://user:password@ip/database?authSource=admin"
client = MongoClient(uri)
db = client.get_database()
mensajes = db.mensajes
informacion2 = db.usuario
app = Flask(__name__)

MESSAGE_KEYS = ['message', 'sender', 'receptant', 'lat', 'long','date']


@app.route("/")
def inicio():
    return "<h1>Entrega 4 Grupo 16</h1>"

@app.route("/mensaje_usuario/<int:mid>")
def informacion_mensaje(mid):
    mensaje = list(mensajes.find({"sender": mid}, {"_id": 0}))
    usuario = list(informacion2.find({"id": mid}, {"_id": 0}))
    final = mensaje+usuario
    hola = json.jsonify(final)
    return hola

@app.route("/informacion_mensaje/<int:mid>")
def informacion(mid):
    mensaje = list(mensajes.find({"id": mid}, {"_id": 0}))
    return json.jsonify(mensaje)



@app.route("/intercambio/<int:mid>/<int:mid2>")
def intercambio_mensajes(mid, mid2):
    primero = list(mensajes.find({"sender":mid, "receptant":mid2}, {"_id": 0}))
    segundo = list(mensajes.find({"sender":mid2, "receptant":mid}, {"_id": 0}))
    final = primero+segundo
    return json.jsonify(final)


@app.route('/mensaje2/<string:texto>')
def search_palabras_deseables(texto):
    #Este es con "or"
    mensajes.create_index([("message", "text")])
    m = list(mensajes.find({"$text": {"$search": texto}}, {"message": 1, "_id": 0}))
    return json.jsonify(m)


@app.route('/mensaje1/<string:texto>')
def search(texto):
    texto = "\"" + texto
    texto = texto.replace("&", "\"  \"")
    texto = texto + "\""

    mensajes.create_index([("message", "text")])

    m = list(mensajes.find({"$text": {"$search": texto}}, {"message": 1, "_id": 0}))


    # Retorno el texto plano de un json
    return json.jsonify(m)


@app.route('/mensaje3/<string:texto>')
def search_without(texto):
    texto = ' "' + texto
    texto = texto.replace(" ", '" -"')
    texto = texto + '"'

    mensajes.createIndex([("message", "text")])

    m = list(mensajes.find({"$text": {"$search": texto}}, {"message": 1}))


    return json.jsonify(m)

@app.route('/eliminar_msje/<int:id>', methods=['DELETE'])
def delete_user(id):

    mensajes.delete_one({"id": id})

    message = f'Mensaje con id={id} ha sido eliminado.'

    return json.jsonify({'result': 'success', 'message': message})


@app.route("/nuevo_msje", methods=['POST'])
def create_msge():

    data = {key: request.json[key] for key in MESSAGE_KEYS}

    # Se genera el id
    count = mensajes.count_documents({})
    data["id"] = count + 1

    result = mensajes.insert_one(data)

    # Creo el mensaje resultado
    if (result):
        message = "Mensaje creado correctamente"
        success = True
    else:
        message = "No se pudo crear el mensaje"
        success = False

    return json.jsonify({'success': success, 'message': message})

if os.name == 'nt':
    app.run()
