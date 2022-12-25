import pathlib
import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import config

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    
    app = connex_app.app
    app.config.from_object(config["development"])
    config["development"].init_app(app)

    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()

    return app