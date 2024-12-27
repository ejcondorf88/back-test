# app.py
from flask import Flask
from models.role import db
from controller.RoleController import role_controller
from controller.EmpleadoController import empleado_controller
from  controller.PdfController import manual_controller
from controller.IncentiveController import incentive_controller
from Config import DevelopmentConfig
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # Permite solicitudes solo desde este origen

# Cargar configuración
app.config.from_object(DevelopmentConfig)

db.init_app(app)
app.register_blueprint(role_controller)
app.register_blueprint(empleado_controller)
app.register_blueprint(manual_controller)
app.register_blueprint(incentive_controller)
@app.before_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run()
