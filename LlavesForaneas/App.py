
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# Configuración del ORM para unirlo con Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/DesarrolloWeb/Backend/SQLAlchemy/LlavesForaneas/App.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Tabla que representa la relción muchos a muchos
lenguajes_programador = db.Table("Lenguajes_Programador", 
	db.Column("ID_Lenguaje", db.Integer, db.ForeignKey("Lenguaje.ID"), primary_key = True),
	db.Column("ID_Programador", db.Integer, db.ForeignKey("Programador.ID"), primary_key = True)
)

# Modelos

class Empresa(db.Model):
	__tablename__ = "Empresa"

	# Columnas
	
	id = db.Column("ID", db.Integer, primary_key = True)
	nombre = db.Column("Nombre", db.String(40))
	fundacion = db.Column("Fundacion", db.Integer, nullable = True) 

	def __repr__(self):
		return f"Nombre: {self.nombre} | Fundacion: {self.fundacion}"

class Lenguaje(db.Model):
	__tablename__ = "Lenguaje"

	# Columnas
	
	id = db.Column("ID", db.Integer, primary_key = True)
	nombre = db.Column("Nombre", db.String(40))
	creador = db.Column("Creador", db.String(40))

	def __repr__(self):
		return f"Nombre: {self.nombre} | Creador: {self.creador}"

class Programador(db.Model):
	__tablename__ = "Programador"

	id = db.Column("ID", db.Integer, primary_key = True)
	nombre = db.Column("Nombre", db.String(40))
	edad = db.Column("Edad", db.Integer, nullable = True)

	# Agregar una llave foranea - relación uno a uno
	empresa_id = db.Column("ID_Empresa", db.Integer, db.ForeignKey("Empresa.ID"))
	empresa = db.relationship("Empresa", backref = db.backref("Programadores", lazy = True))

	# Relación muchos a muchos
	lenguaje = db.relationship("Lenguaje", secondary = lenguajes_programador, 
		backref = db.backref("Programadores", lazy = True))

	def __repr__(self):
		return f"Nombre: {self.nombre} | Edad: {self.edad} | Empresa: {self.empresa}"	

with app.app_context():

    # Insertar datos en la tabla Empresa
    empresa_1 = Empresa(nombre = "TechCorp", fundacion = 1999)
    empresa_2 = Empresa(nombre = "CodeFactory", fundacion = 2005)
    empresa_3 = Empresa(nombre = "DevSolutions", fundacion = 2010)
    empresa_4 = Empresa(nombre = "InnovateInc", fundacion = 2015)
    empresa_5 = Empresa(nombre = "FutureSoft", fundacion = 2020)
    
    db.session.add_all([empresa_1, empresa_2, empresa_3, empresa_4, empresa_5])
    
    # Insertar datos en la tabla Lenguaje
    lenguaje1 = Lenguaje(nombre = "Python", creador = "Guido van Rossum")
    lenguaje2 = Lenguaje(nombre = "JavaScript", creador = "Brendan Eich")
    lenguaje3 = Lenguaje(nombre = "Java", creador = "James Gosling")
    lenguaje4 = Lenguaje(nombre = "C#", creador = "Microsoft")
    lenguaje5 = Lenguaje(nombre = "Ruby", creador = "Yukihiro Matsumoto")
    
    db.session.add_all([lenguaje1, lenguaje2, lenguaje3, lenguaje4, lenguaje5])
    
    # Insertar datos en la tabla Programador
    programador1 = Programador(nombre = "Alice", edad = 30, empresa = empresa_1)
    programador2 = Programador(nombre = "Bob", edad = 28, empresa = empresa_2)
    programador3 = Programador(nombre = "Charlie", edad = 35, empresa = empresa_3)
    programador4 = Programador(nombre = "David", edad = 40, empresa = empresa_4)
    programador5 = Programador(nombre = "Eve", edad = 25, empresa = empresa_5)
    
    # Asociar programadores con lenguajes
    programador1.lenguaje.append(lenguaje1)
    programador2.lenguaje.append(lenguaje2)
    programador3.lenguaje.append(lenguaje3)
    programador4.lenguaje.append(lenguaje4)
    programador5.lenguaje.append(lenguaje5)

    db.session.add_all([programador1, programador2, programador3, programador4, programador5])

    # Guardar las instancias en la base de datos
    db.session.commit()

    print("Datos insertados correctamente \U0001F601")

if __name__ == "__main__":
	app.run()