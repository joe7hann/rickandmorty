import requests
from flask import Blueprint, render_template, flash, redirect, url_for
from app.db import db


ram_router = Blueprint("ram_router", __name__)

@ram_router.route("/")
def index():
    return "index PAGINA PRINCIPAL"

@ram_router.route("/lista")
def lista():
    personajes = db.personaje.find()
    return render_template("lista.html", personajes = personajes)

@ram_router.route("/lista/<int:id>")
def detalles(id):
    personaje = db.personaje.find_one({"id":id})
    return render_template("personaje.html", personaje = personaje)

@ram_router.route("/import_db", methods=['GET','POST'])
def import_db():
    for id in range(1,20):
        url = requests.get('https://rickandmortyapi.com/api/character/'+str(id))
        url_json = url.json()

        data = {
            'id': url_json['id'],
            'name': url_json['name'],
            'status': url_json['status'],
            'species': url_json['species'],
            'type': url_json['type'],
            'gender': url_json['gender'],
            'origin': url_json['origin'],
            'location': url_json['location'],
            'image': url_json['image']
        }
        db.personaje.insert_one(data)

    return redirect('/lista')


