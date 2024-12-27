# controllers/user_controller.py
from flask import Blueprint, jsonify, request
from service.RoleService import RoleService
from repository.RoleRepository import RoleRepository
from models.role import db
from flask_cors import  cross_origin

role_controller = Blueprint('role_controller', __name__)
role_repository = RoleRepository(db)
role_service = RoleService(role_repository)

@role_controller.route("/role/<int:role_id>", methods=["GET"])
@cross_origin(origins=["http://localhost:5173"])  # Permite solicitudes desde el frontend
def get_role(role_id):

    role_info = role_service.get_role_id(role_id)
    print(role_info)
    if role_info:
        return jsonify(role_info)
    return jsonify({"error": "User not found"}), 404

@role_controller.route("/user", methods=["POST"])
def create_user():
    data = request.json
    new_user = role_service.create_user(data['name'], data['email'])
    return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email}), 201

@role_controller.route("/")
def index():
    return 'Hola Mindod'