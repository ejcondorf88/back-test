# services/user_service.py
from repository.EmpleadoRepository import EmpleadoRepository


class EmpleadoService:
    def __init__(self, empleado_repository: EmpleadoRepository):
        self.empleado_repository = empleado_repository

    def get_role_by_email_password(self, email, password):
        empleado = self.empleado_repository.get_empleado(email, password)
        if empleado:
            return {"role": empleado.role_id}
        return None

    def create_role(self, name, email):
        return self.user_repository.create_role(name, email)


    def get_empleados(self):
        return  self.empleado_repository.get_all_empleados()
