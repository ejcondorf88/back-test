# repository/user_repository.p
from models.role import Empleado


class EmpleadoRepository:
    def __init__(self, db):
        self.db = db

    def get_empleado(self, email,password):
        empleado = Empleado.query.filter_by(email=email, password=password).first()
        if empleado:
            return empleado

        return None

    def create_user(self, name, email):
        new_user = Empleado(name=name, email=email)
        self.db.session.add(new_user)
        self.db.session.commit()
        return new_user

    def get_all_empleados(self):
        return Empleado.query.all()

