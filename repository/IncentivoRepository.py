
from models.role import Incentive
class IncentivoRepository:
    def __init__(self, db):  # Cambia __int__ a __init__
        self.db = db


    def create_incentive(self,title,descrption,idEmpleado,amount):
        incentivo = Incentive(title=title,descrption=descrption,idEmpleado=idEmpleado,amount=amount)
        self.db.session.add(incentivo)
        self.db.session.commit()
        return incentivo

    def get_incentive_by_id_empleado(self,id_empleado):
        incentives = Incentive.query.filter_by(idEmpleado=id_empleado).all()
        if incentives:
            return incentives
        return  None

    def get_all(self):
        employess=Incentive.query.all();
        return employess

