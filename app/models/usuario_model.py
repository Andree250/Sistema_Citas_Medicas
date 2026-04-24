class Usuario:
    def __init__(self, dni, nombre, correo, password):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def a_diccionario(self):
        """Convierte el objeto a un formato fácil de guardar"""
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "correo": self.correo,
            "password": self.password
        }
    