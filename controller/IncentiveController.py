from flask import Blueprint, jsonify, request

from repository.IncentivoRepository import IncentivoRepository
from models.role import db
from service.IncentiveService import IncentiveService
from flask_cors import  cross_origin

incentive_controller=Blueprint('incentive_controller',__name__)
incentive_repository=IncentivoRepository(db)
incentive_service=IncentiveService(incentive_repository)


@incentive_controller.route('/incentive', methods=['POST'])
def create_incentive():
    data = request.json
    try:
        title = data['title']
        description = data['description']
        amount = float(data['amount'])  # Asegúrate de que es un número
        idEmpleado = int(data['idEmpleado'])  # Convertir a entero

        create = incentive_service.create(title, description, idEmpleado, amount)
        return jsonify({"create":True}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400

@incentive_controller.route("/incentive/<int:empleado_id>", methods=["GET"])
@cross_origin(origins=["http://localhost:5173"])  # Permite solicitudes desde el frontend
def get_incentive(empleado_id):
    try:
        # Imprime el ID de empleado recibido para depuración
        print(f"Empleado ID: {empleado_id}")

        # Obtener información de incentivos a partir del servicio
        incentive_info = incentive_service.get_by_id(int(empleado_id))

        # Convierte la información de incentivos a diccionario
        manuals_dict = [incentive.to_dict() for incentive in incentive_info]

        # Si se encontraron incentivos, devolverlos en formato JSON
        if manuals_dict:
            return jsonify({"incentives": manuals_dict})

        # Si no se encontraron incentivos, devolver un error 404
        return jsonify({"error": "Incentivos no encontrados para el empleado."}), 404

    except Exception as e:
        # Captura cualquier error y devuelve un mensaje de error con un código de estado 500
        return jsonify({"error": f"Ocurrió un error: {str(e)}"}), 500

@incentive_controller.route('/employees',methods=['GET'])
@cross_origin(origins=["http://localhost:5173"])  # Permite solicitudes desde el frontend
def getAll():
    info=incentive_service.get_all()
    empleados_dict=[empleados.to_dict()for empleados in info]
    print(empleados_dict)
    return empleados_dict