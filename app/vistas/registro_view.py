import customtkinter as ctk
from tkinter import messagebox

class RegistroView:
    def __init__(self, root, al_finalizar):
        self.root = root
        self.al_finalizar = al_finalizar
        
        # Contenedor principal con fondo suave
        self.frame = ctk.CTkFrame(master=root, fg_color="#F8FAFC")
        self.frame.pack(fill="both", expand=True)

        # Título principal resaltado
        ctk.CTkLabel(self.frame, text="REGISTRO DE USUARIO", 
                     font=("Helvetica", 24, "bold"), 
                     text_color="#006064").pack(pady=(40, 20))

        # --- TARJETA DE FORMULARIO ---
        form_card = ctk.CTkFrame(self.frame, fg_color="white", corner_radius=25, 
                                 border_width=2, border_color="#E2E8F0")
        form_card.pack(pady=10, padx=40, fill="x")

        # Creación de campos con etiquetas visibles y legibles
        self.ent_nombre = self.crear_campo(form_card, "Nombres Completos", "Ej: Andree Aquino")
        self.ent_dni = self.crear_campo(form_card, "DNI", "8 dígitos")
        self.ent_correo = self.crear_campo(form_card, "Correo Electrónico", "ejemplo@correo.com")
        self.ent_pass = self.crear_campo(form_card, "Nueva Contraseña", "••••••••", secreto=True)

        # Botón CREAR CUENTA (Estilo Teal)
        self.btn_registrar = ctk.CTkButton(form_card, text="CREAR CUENTA", 
                                           fg_color="#007F8C", hover_color="#005F69",
                                           height=50, corner_radius=12, 
                                           font=("Helvetica", 14, "bold"),
                                           command=self.ejecutar_registro)
        self.btn_registrar.pack(pady=(30, 40), padx=35, fill="x")
        
        # Enlace para volver
        self.btn_volver = ctk.CTkButton(self.frame, text="← Volver al Login", 
                                         fg_color="transparent", text_color="#64748B", 
                                         font=("Helvetica", 13), hover=False,
                                         command=self.volver)
        self.btn_volver.pack(pady=10)

    def crear_campo(self, parent, texto, placeholder, secreto=False):
        ctk.CTkLabel(parent, text=texto, font=("Helvetica", 13, "bold"), 
                     text_color="#1E293B").pack(anchor="w", padx=35, pady=(15, 0))
        
        entry = ctk.CTkEntry(parent, 
                             placeholder_text=placeholder, 
                             placeholder_text_color="#64748B", # Gris más oscuro y visible
                             text_color="#1E293B",             # Color de letra al escribir (Casi negro)
                             show="*" if secreto else "",
                             height=45, corner_radius=8,
                             border_color="#CBD5E1", fg_color="#FBFDFF")
        entry.pack(fill="x", padx=35, pady=(5, 5))
        return entry
    
    def ejecutar_registro(self):
        from app.controladores.auth_controller import AuthController
        control = AuthController()
        
        # Obtenemos los datos de los campos
        dni = self.ent_dni.get()
        nombre = self.ent_nombre.get()
        correo = self.ent_correo.get()
        password = self.ent_pass.get()

        # Intentamos guardar en la base de datos
        if control.registrar_usuario(dni, nombre, correo, password):
            messagebox.showinfo("Sistema Tech", "¡Cuenta creada con éxito!")
            self.volver()

    def volver(self):
        self.frame.pack_forget()
        self.al_finalizar()
