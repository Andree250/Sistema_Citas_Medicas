import customtkinter as ctk
from app.vistas.login_view import LoginView
from app.vistas.dashboard_view import DashboardView # Importamos la nueva vista
from database.db_config import inicializar_db

def abrir_dashboard(nombre):
    # 'nombre' vendrá del controlador después, por ahora usemos uno fijo
    DashboardView(root, nombre_usuario=nombre)

if __name__ == "__main__":
    inicializar_db() 
    
    root = ctk.CTk()
    root.title("Sistema Tech - EsSalud")
    root.geometry("450x750")
    
    # Pasamos una función que reciba el nombre para mostrarlo
    app = LoginView(root, on_success=lambda: abrir_dashboard("Usuario"))
    
    root.mainloop()
    