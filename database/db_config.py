import sqlite3
import os

def inicializar_db():
    # Creamos la conexión (esto genera el archivo .db si no existe)
    ruta_db = os.path.join("database", "sistema_tech.db")
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    
    # Creamos la tabla de usuarios siguiendo tu diagrama
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            dni TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    conexion.commit()
    conexion.close()
    print("Base de datos inicializada correctamente.")
    