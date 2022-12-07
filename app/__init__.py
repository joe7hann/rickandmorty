from flask import Flask
#from flask_bootstrap import Bootstrap

from .config import Config
from .routes.book import book_router
from .routes.personajes import ram_router

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    #Bootstrap(app)
    app.register_blueprint(ram_router)
    app.register_blueprint(book_router)
    return app