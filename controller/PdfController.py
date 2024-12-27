from flask import Blueprint, request, jsonify
from models.role import db, Manual
from repository.PdfRepository import PdfRepository
from service.PdfService import PdfService
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings
from flask_cors import cross_origin


manual_controller = Blueprint('manual_controller', __name__)
manual_repository = PdfRepository(db)
manual_service = PdfService(manual_repository)

# Configuración de Azure Blob Storage
CONTAINER_NAME = 'testjama'

blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)


@manual_controller.route('/manual', methods=['POST'])
@cross_origin(origins=["http://localhost:5173"])  # Permite solicitudes desde el frontend
def create_manual():
    data = request.form  # Para datos de texto
    file = request.files.get('file')  # Para el archivo PDF
    name = data.get('name')

    # Validación de campos requeridos
    if not name or not file:
        return jsonify({'error': 'El nombre y el archivo son obligatorios'}), 400

    if file.filename == '':
        return jsonify({"error": "No se ha seleccionado ningún archivo"}), 400

    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Solo se permiten archivos PDF"}), 400

    try:
        # Subir el archivo PDF a Azure Blob Storage
        blob_client = container_client.get_blob_client(file.filename)

        if blob_client.exists():
            return jsonify({"error": "El archivo ya existe en Azure"}), 400

        blob_client.upload_blob(file, blob_type="BlockBlob", content_settings=ContentSettings(content_type='application/pdf'))

        # Obtener la URL del archivo subido
        blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{CONTAINER_NAME}/{file.filename}"

        # Crear el manual en la base de datos con el link del archivo subido
        new_manual = manual_service.create_manual(name, link=blob_url)

        return jsonify({'message': 'Manual creado exitosamente', 'url': blob_url}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@manual_controller.route('/manuals', methods=['GET'])
def get_manuals():
    manuals = manual_service.get_all()
    manuals_dict = [manuals.to_dict() for manuals in manuals]

    return jsonify({"manuals":manuals_dict}) # Asegúrate de tener un método to_dict en tu modelo


