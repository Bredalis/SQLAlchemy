
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

app = Flask(__name__)

# Configuración del ORM para unirlo con Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/DesarrolloWeb/Backend/SQLAlchemy/Migraciones/App.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelos

class Usuario(db.Model):
	__tablename__ = "Usuario"

	# Columnas
	
	id = db.Column("ID", db.Integer, primary_key = True)
	nombre = db.Column("Nombre", db.String(40))

class Post(db.Model):
	__tablename__ = "Post"

	# Columnas
	
	id = db.Column("ID", db.Integer, primary_key = True)
	post = db.Column("Post", db.String(40))

with app.app_context():
	db.create_all() # Crear bbdd

if __name__ == "__main__":
	app.run(debug = True)