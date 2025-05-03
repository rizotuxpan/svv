# svv.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_appbuilder import AppBuilder, SQLA
from flask_appbuilder.security.manager import BaseSecurityManager

# Crear la instancia de la aplicación Flask
svv = Flask(__name__)
CORS(svv)

# Configuración de la base de datos de PostgreSQL
svv.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:masterkey@localhost:5432/svv_db'
svv.config['SECRET_KEY'] = 'mysecretkey'  # Secreto para la sesión de Flask
svv.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear la instancia de SQLAlchemy
db = SQLA(svv)

# Configuración de Flask AppBuilder
appbuilder = AppBuilder(svv, db.session)

# Usar el manager de seguridad de Flask AppBuilder
class MySecurityManager(BaseSecurityManager):
    pass  # Aquí puedes personalizar la gestión de usuarios si lo necesitas

svv.appbuilder.security_manager = MySecurityManager

# Definir el modelo de datos (InventoryItem)
class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String)
    cantidad = db.Column(db.Integer)
    ubicacion = db.Column(db.String)

# Rutas de la API para manejar items
@svv.route('/items', methods=['POST'])
def add_item():
    data = request.json
    item = InventoryItem(**data)
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item agregado'}), 201

@svv.route('/items', methods=['GET'])
def get_items():
    items = InventoryItem.query.all()
    return jsonify([{
        'id': i.id,
        'nombre': i.nombre,
        'categoria': i.categoria,
        'cantidad': i.cantidad,
        'ubicacion': i.ubicacion
    } for i in items])

# Página de inicio o dashboard
@svv.route('/')
def home():
    return render_template('index.html')

# Iniciar la aplicación Flask
if __name__ == '__main__':
    svv.run(debug=True)

