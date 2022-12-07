import requests
from flask import Blueprint, render_template, flash, redirect, url_for
from app.db import db


ram_router = Blueprint("ram_router", __name__)

@ram_router.route("/")
@ram_router.route("/personajes")
def lista():
    personajes = db.personaje.find()
    return render_template("lista.html", personajes = personajes)

@ram_router.route("/personaje/<int:id>")
def detalles(id):
    personaje = db.personaje.find_one({"id":id})
    return render_template("personaje.html", personaje = personaje)

@ram_router.route("/capitulos")
def capitulos():
    capitulos = db.capitulos.find()
    return render_template("capitulos.html", capitulos = capitulos)

@ram_router.route("/capitulo/<int:id>")
def capitulo_detalles(id):
    capitulo = db.capitulos.find_one({"id":id})
    personajes_cap = db.personaje.find({"episodes":str(id)},{"name":1,"image":1})
    # db.personaje.find({"episodes":{$all:[str(id)]}})
    # db.personaje.find( { "episodes": { $all: [ [ str(id) ] ] } },{"name":1,"image":1} )

    return render_template("capitulo.html", capitulo = capitulo, personajes_cap = personajes_cap)


@ram_router.route("/import_db", methods=['GET','POST'])
def import_db():
    for id in range(1,100):
        url = requests.get('https://rickandmortyapi.com/api/character/'+str(id))
        url_json = url.json()
        episodes=[]
        for item in url_json['episode']:
            flag = item.split('/')
            episodes.append(flag[-1])

        data = {
            'id': url_json['id'],
            'name': url_json['name'],
            'status': url_json['status'],
            'species': url_json['species'],
            'type': url_json['type'],
            'gender': url_json['gender'],
            'origin': url_json['origin'],
            'location': url_json['location'],
            'image': url_json['image'],
            'episodes':episodes
        }
        db.personaje.insert_one(data)

    return redirect('/personajes')

@ram_router.route("/import_caps", methods=['GET','POST'])
def import_caps():
    for id in range(1,20):
        url = requests.get('https://rickandmortyapi.com/api/episode/'+str(id))
        url_json = url.json()

        data = {
            'id': url_json['id'],
            'name': url_json['name'],
            'air_date': url_json['air_date'],
            'episode': url_json['episode'],
            'characters': url_json['characters']
        }
        db.capitulos.insert_one(data)

    return redirect('/capitulos')

