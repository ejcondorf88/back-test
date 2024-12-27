
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Empleado(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password= db.Column(db.String(120), nullable=False)
    # Clave foránea que referencia al rol
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def __repr__(self):
        return f"<Empleado {self.nombre}, Role: {self.role.name}>"