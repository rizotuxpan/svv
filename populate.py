from svv import db, InventoryItem, svv  # Importa la instancia 'svv' desde 'svv.py'

def populate_db():
    items = [
        {"nombre": "Cámara IP", "categoria": "Cámaras", "cantidad": 10, "ubicacion": "Almacén A"},
        {"nombre": "DVR 4 canales", "categoria": "Grabadores", "cantidad": 5, "ubicacion": "Almacén B"},
        {"nombre": "Cable coaxial", "categoria": "Accesorios", "cantidad": 100, "ubicacion": "Almacén A"},
        {"nombre": "Fuente de poder 12V", "categoria": "Accesorios", "cantidad": 50, "ubicacion": "Almacén C"},
    ]

    for item_data in items:
        item = InventoryItem(**item_data)
        db.session.add(item)

    db.session.commit()
    print("Datos de ejemplo agregados.")

if __name__ == '__main__':
    with svv.app_context():  # Usa 'svv' aquí
        db.create_all()    # Crea las tablas si no existen
        populate_db()      # Agregar datos de ejemplo

