from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

base_path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_path, 'db.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some_super_secret_key'

db = SQLAlchemy(app)

from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)


# if not os.path.exists(os.path.join(base_path, 'db.sqlite')):
#     db.create_all()