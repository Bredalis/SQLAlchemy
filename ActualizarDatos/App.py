
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración del ORM para unirlo con Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/DesarrolloWeb/Backend/SQLAlchemy/ActualizarDatos/App.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo

class BandasDeKpop(db.Model):
	__tablename__ = "Bandas_De_Kpop"

	# Columnas
	id = db.Column("ID", db.Integer, primary_key = True)
	nombre = db.Column("Nombre", db.String(40))
	integrantes = db.Column("Integrantes", db.Integer)

	def __repr__(self):
		return f"<Bandas_De_Kpop Nombre: {self.nombre} Integrantes: {self.integrantes}>"

with app.app_context():

	# Mostar todos los datos
	bbdd = BandasDeKpop.query.all()

	for banda in bbdd:
		print(banda)

	# Obtener el dato a actualizar
	dato = BandasDeKpop.query.filter_by(nombre = "Aespa").first()
	
	# Actualizar datos
	if dato:
		dato.integrantes = 4
		db.session.commit() # Guardar los cambios

		print("Actualizacion exitosa! \U0001F603")

if __name__ == "__main__":
	app.run()