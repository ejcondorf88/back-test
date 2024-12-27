# services/user_service.py
from repository.RoleRepository import RoleRepository

class RoleService:
    def __init__(self, user_repository: RoleRepository):
        self.user_repository = user_repository

    def get_role_id(self, role_id):
        role = self.user_repository.get_role(role_id)
        if role:
            return {"id": role.id, "name": role.name, }
        return None

    def create_role(self, name, email):
        return self.user_repository.create_role(name, email)
