from repository.IncentivoRepository import IncentivoRepository

class IncentiveService:
    def __init__(self,inicentive_repository:IncentivoRepository):
        self.incentive_repository=inicentive_repository

    def create(self,title,description,idEmpleado,amount):
        incentive=self.incentive_repository.create_incentive(title,description,idEmpleado,amount)
        return incentive

    def get_by_id(self,id):

        incentive= self.incentive_repository.get_incentive_by_id_empleado(id)
        if incentive is not None:
            return incentive
        return None
    def get_all(self):
        return  self.incentive_repository.get_all()

