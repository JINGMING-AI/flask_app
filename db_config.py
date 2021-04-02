from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123qweASD@182.92.179.151:3306/demo"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1822@127.0.0.1:3306/demo"

db_init = SQLAlchemy(app)