# repository/user_repository.p
from models.role import Manual


class PdfRepository:
    def __init__(self, db):
        self.db = db

    def get_manual(self, manual_id):
        return Manual.query.get(manual_id)




    def get_all(self):
        return Manual.query.all()

    def create_manual(self, name, link, empleado_id=1):
        # Crear un nuevo objeto Manual incluyendo el empleado_id
        new_manual = Manual(name=name, link=link, empleado_id=empleado_id)
        self.db.session.add(new_manual)
        self.db.session.commit()
        return new_manual