from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    empleados = db.relationship('Empleado', backref='role', lazy=True)


class Empleado(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    manuales = db.relationship('Manual', backref='empleado', lazy=True)

    def __repr__(self):
        return f"<Empleado {self.nombre}>"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "role_id": self.role_id,
        }



class Manual(db.Model):
    __tablename__ = 'manuales'  # Cambiado a __tablename__

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)  # Corrección aquí

    def __repr__(self):
        return f"<Manual {self.name}>"

    def to_dict(self):
        return {
            "name":self.name,
            "link":self.link
        }

class Incentive(db.Model):
    __table__name__ = 'incentivo'
    title = db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    descrption = db.Column(db.String(100), nullable=False)
    idEmpleado= db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"<Manual {self.title}>"

    def to_dict(self):
        return {
           "title":self.title,
            "descrption":self.descrption,
            "idEmpleado": self.idEmpleado,
            "amount":self.amount
        }





