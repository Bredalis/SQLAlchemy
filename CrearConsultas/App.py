
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración del ORM para unirlo con Flask
app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/DesarrolloWeb/Backend/SQLAlchemy/CrearConsultas/App.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo - Estructura para guardar los datos

class BandasDeKpop(db.Model):
	__tablename__ = "Bandas_De_Kpop" # Nombre de la tabla de bbdd

	# Columnas

	id = db.Column("ID", db.Integer, primary_key = True)
	nombre = db.Column("Nombre", db.String(30))
	integrantes = db.Column("Integrantes", db.Integer)

	# Forma de mostrar las consultas
	def __repr__(self):
		return f"<Bandas_De_Kpop Nombre: {self.nombre} | Integrantes: {self.integrantes}>"

with app.app_context():

	# Crear consulta para mostras datos
	bbdd = BandasDeKpop.query.all()

	for banda in bbdd:
		print(banda)

	# Consultas específicas
	bts = BandasDeKpop.query.filter(BandasDeKpop.nombre == "BTS").first()
	print("\n", bts.nombre)

	print("\nBandas con 7 y 4 integrantes:")
	bandas = BandasDeKpop.query.filter(BandasDeKpop.integrantes.in_([4, 7]))

	for r in bandas:
		print(r)

	print("\nBandas que no cumplen la condición:")
	bandas = BandasDeKpop.query.filter(~BandasDeKpop.integrantes.in_([4, 7]))
	
	for r in bandas:
		print(r)

if __name__ == "__main__":
	app.run()