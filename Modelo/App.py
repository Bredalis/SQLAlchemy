
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración del ORM para unirlo con Flask
app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/DesarrolloWeb/Backend/SQLAlchemy/Modelo/App.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo - Estructura para guardar los datos

class BandasDeKpop(db.Model):
	__tablename__ = "Bandas_De_Kpop" # Nombre de la tabla de bbdd

	# Columnas

	id = db.Column("ID", db.Integer, primary_key = True)
	nombre = db.Column("Nombre", db.String(30))
	integrantes = db.Column("Integrantes", db.Integer)

with app.app_context():
	db.create_all() # Crear la bbdd

if __name__ == "__main__":
	app.run(debug = True)