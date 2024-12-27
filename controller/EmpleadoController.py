# controllers/user_controller.py
from flask import Blueprint, jsonify, request
from service.EmpleadoService import EmpleadoService
from repository.EmpleadoRepository import EmpleadoRepository
from models.employee import db
from flask_cors import  cross_origin

empleado_controller = Blueprint('empleado_controller', __name__)
empleado_repository = EmpleadoRepository(db)
empleado_service = EmpleadoService(empleado_repository)

@empleado_controller.route("/iniciar-sesion", methods=["POST"])
@cross_origin(origins=["http://localhost:5173"])  # Permite solicitudes desde el frontend
def iniciar_sesion():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email y contraseña son obligatorios"}), 400

    user = empleado_service.get_role_by_email_password(email,password)
    print(user)
    if user is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    # Verificar la contraseña (usando hash)
    # Si es correcto, retornar un mensaje de éxito

    return jsonify({"mensaje": f"Bienvenido, AL SISTEMA LA JAMA",
                    "login":True}), 200



@empleado_controller.route("/empleados", methods=["GET"])
@cross_origin(origins=["http://localhost:5173"])
def get_empleados():
    empleados=empleado_service.get_empleados()
    if empleados:
        empleados_dict = [empleado.to_dict() for empleado in empleados]
        return jsonify({"empleados": empleados_dict})
    return jsonify({"errro"})
@empleado_controller.route("/")
def index():
    return 'CARGANDO DATOS EN LA BD'