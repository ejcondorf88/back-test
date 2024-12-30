# Proyecto Back-Test

## Descripción
Sistema de back-testing desarrollado en Python para el análisis de estrategias de trading y datos financieros.

---

## Requisitos Previos

- Python 3.x  
- `pip` (Gestor de paquetes de Python)  

---

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/ejcondorf88/back-test.git
   cd back-test
## Instalación

2. **Crear un entorno virtual (recomendado):**

   ```bash
   python -m venv venv
 3. **Activar el entorno virtual:**

   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
## Estructura del Proyecto

```plaintext
back-test/
├── .idea/
├── __pycache__/
├── controller/
├── models/
├── repository/
├── service/
├── .gitignore
├── Config.py
├── __init__.py
├── app.py
└── requirements.txt
## Configuración

1. Abrir el archivo `Config.py` y ajustar las configuraciones necesarias para tu entorno.
2. Asegurarse de que todas las variables de entorno requeridas estén configuradas (si las hay).

---

## Ejecución de la Aplicación

1. Asegúrate de que tu entorno virtual esté activado.  
2. Ejecuta la aplicación:  

   ```bash
   python app.py
