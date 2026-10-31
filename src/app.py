from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from database import mysql  # Importa la instancia centralizada
from blueprints.alumnos.routes import alumnos_bp
from blueprints.maestros.routes import maestros_bp
from config import config

app = Flask(__name__)

# 1. Cargamos la configuración de la base de datos primero
app.config.from_object(config['development'])

CORS(app)

# 2. Inicializamos la extensión con la app ya configurada
mysql.init_app(app)

# Registramos los blueprints
app.register_blueprint(alumnos_bp)
app.register_blueprint(maestros_bp)

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>", 404

if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000)