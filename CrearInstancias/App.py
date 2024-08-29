
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración del ORM para unirlo con Flask
app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/DesarrolloWeb/Backend/SQLAlchemy/CrearInstancias/App.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo - estructura para guardar los datos

class BandasDeKpop(db.Model):
	__tablename__ = "Bandas_De_Kpop" # Nombre de la tabla de bbdd

	# Columnas

	id = db.Column("ID", db.Integer, primary_key = True)
	nombre = db.Column("Nombre", db.String(30))
	integrantes = db.Column("Integrantes", db.Integer)

with app.app_context():

	# Crear instancias
	
	banda_1 = BandasDeKpop(nombre = "NewJeans", integrantes = 5)
	banda_2 = BandasDeKpop(nombre = "Aespa", integrantes = 4)

	# Agregar instancias a la seccion
	db.session.add(banda_1)
	db.session.add(banda_2)

	# Guardar las instancias en la bbdd
	db.session.commit()

	print("Datos insertados correctarmente \U0001F601")
		
if __name__ == "__main__":
	app.run()