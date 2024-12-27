# repository/user_repository.p
from models.role import Role


class RoleRepository:
    def __init__(self, db):
        self.db = db

    def get_role(self, role_id):
        return Role.query.get(role_id)

    def create_role(self, name, email):
        new_user = Role(name=name, email=email)
        self.db.session.add(new_user)
        self.db.session.commit()
        return new_user
