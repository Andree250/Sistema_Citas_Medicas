import sqlite3
import os

def inicializar_db():
    dir_actual = os.path.dirname(__file__)
    ruta_db = os.path.join(dir_actual, "sistema_tech.db")
    
    # Nos aseguramos de cerrar cualquier conexión previa
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    # Limpiamos tablas antiguas para evitar errores de estructura
    cursor.execute('DROP TABLE IF EXISTS citas')
    cursor.execute('DROP TABLE IF EXISTS usuarios')

    # Tabla de Usuarios
    cursor.execute('''
        CREATE TABLE usuarios (
            dni TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

# Tabla de Citas (CON COLUMNA HORA)
    cursor.execute('''
        CREATE TABLE citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dni_paciente TEXT NOT NULL,
            especialidad TEXT NOT NULL,
            doctor TEXT NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            FOREIGN KEY (dni_paciente) REFERENCES usuarios (dni)
        )
    ''')
    
    conexion.commit()
    conexion.close()
    print("Base de datos SQLite reseteada y lista (sin bloqueos).")

if __name__ == '__main__':
    inicializar_db()
    