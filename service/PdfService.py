# services/user_service.py
from repository.PdfRepository import PdfRepository


class PdfService:
    def __init__(self, pdf_repositoroy: PdfRepository):
        self.pdf_repositoroy = pdf_repositoroy

    def get_manual_by_id(self, id_manual):
        manual = self.pdf_repositoroy.get_manual(id_manual)
        if manual:
            return {"link":manual.link}
        return None

    def get_all(self):
        manuales=self.pdf_repositoroy.get_all()
        return manuales

    def create_manual(self, name, link):
        return self.pdf_repositoroy.create_manual(name,link)
