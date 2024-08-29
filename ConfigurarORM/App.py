
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración del ORM para unirlo con Flask
app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/DesarrolloWeb/Backend/SQLAlchemy/CondigurarORM/App.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Ejecutar programa
if __name__ == "__main__":
	app.run(debug = True)