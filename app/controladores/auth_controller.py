import sqlite3
import os
from tkinter import messagebox

class AuthController:
    def __init__(self):
        self.db_path = os.path.join("database", "sistema_tech.db")

    def registrar_usuario(self, dni, nombre, correo, password):
        # Validación de campos vacíos
        if not (dni and nombre and correo and password):
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
            return False
        
        # Validación de DNI (8 dígitos) [cite: 10]
        if not (dni.isdigit() and len(dni) == 8):
            messagebox.showerror("Error", "El DNI debe tener 8 números.")
            return False

        try:
            conexion = sqlite3.connect(self.db_path)
            cursor = conexion.cursor()
            # Insertamos los datos en la tabla usuarios [cite: 80]
            cursor.execute('''
                INSERT INTO usuarios (dni, nombre, correo, password)
                VALUES (?, ?, ?, ?)
            ''', (dni, nombre, correo, password))
            
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Este DNI ya está registrado.")
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Error en la base de datos: {e}")
            return False

    def validar_acceso(self, dni, password):
        try:
            conexion = sqlite3.connect(self.db_path)
            cursor = conexion.cursor()
            # Buscamos al usuario por DNI y Contraseña [cite: 64]
            cursor.execute('SELECT * FROM usuarios WHERE dni=? AND password=?', (dni, password))
            usuario = cursor.fetchone()
            conexion.close()
            
            if usuario:
                return True
            return False
        except Exception as e:
            print(f"Error al validar: {e}")
            return False
        