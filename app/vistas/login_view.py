import customtkinter as ctk
from PIL import Image # Necesitas instalar: pip install Pillow

class LoginView:
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        
        # Fondo degradado suave (Simulado con color sólido muy claro)
        self.main_frame = ctk.CTkFrame(master=root, fg_color="#F8FAFC")
        self.main_frame.pack(fill="both", expand=True)

        # Encabezado (Teal EsSalud)
        ctk.CTkLabel(self.main_frame, text="EsSalud", font=("Helvetica", 42, "bold"), text_color="#006064").pack(pady=(60, 0))
        ctk.CTkLabel(self.main_frame, text="MiConsulta", font=("Helvetica", 22), text_color="#006064").pack(pady=(0, 40))

        # --- TARJETA PRINCIPAL (La que tiene bordes suaves) ---
        form_card = ctk.CTkFrame(self.main_frame, fg_color="white", corner_radius=25, 
                                 border_width=2, border_color="#E2E8F0")
        form_card.pack(pady=10, padx=40, fill="x")

        # DNI Label
        ctk.CTkLabel(form_card, text="Documento de Identidad (DNI)", font=("Helvetica", 13, "bold"), text_color="#1E293B").pack(anchor="w", padx=35, pady=(30, 0))
        
        # Input DNI con Icono (Simulado con un Frame)
        dni_container = ctk.CTkFrame(form_card, fg_color="white", border_width=1, border_color="#006064", corner_radius=8)
        dni_container.pack(fill="x", padx=35, pady=(5, 15))
        
        # Aquí cargarías el icono:
        # img_user = ctk.CTkImage(light_image=Image.open("app/static/user_icon.png"), size=(20, 20))
        # ctk.CTkLabel(dni_container, image=img_user, text="").pack(side="left", padx=10)
        
        self.ent_dni = ctk.CTkEntry(dni_container, 
                                    placeholder_text="Ingrese su DNI (8 dígitos)", 
                                    placeholder_text_color="#64748B", # Letra de ejemplo visible
                                    text_color="#1E293B",             # Letra que escribes
                                    border_width=0, fg_color="transparent", height=45)
        self.ent_dni.pack(side="left", fill="x", expand=True, padx=5)

        # Contraseña Label
        ctk.CTkLabel(form_card, text="Contraseña", font=("Helvetica", 13, "bold"), text_color="#1E293B").pack(anchor="w", padx=35, pady=(10, 0))
        
        # Input Pass con Icono
        pass_container = ctk.CTkFrame(form_card, fg_color="white", border_width=1, border_color="#CBD5E1", corner_radius=8)
        pass_container.pack(fill="x", padx=35, pady=(5, 5))
        
        self.ent_pass = ctk.CTkEntry(pass_container, 
                                     placeholder_text="Ingrese su contraseña (máx 20 caracteres)", 
                                     placeholder_text_color="#64748B", # Letra de ejemplo visible
                                     text_color="#1E293B",             # Letra que escribes
                                     show="*", border_width=0, fg_color="transparent", height=45)
        
        self.ent_pass.pack(side="left", fill="x", expand=True, padx=5)

        # Enlace Olvidó contraseña
        ctk.CTkButton(form_card, text="¿Olvidó su contraseña?", font=("Helvetica", 12), fg_color="transparent", 
                      text_color="#006064", hover=False, width=10).pack(anchor="e", padx=35, pady=(5, 20))

        # Botón INGRESAR (Teal degradado)
        self.btn_login = ctk.CTkButton(form_card, text="INGRESAR", fg_color="#4F9196", hover_color="#3D7074", 
                                       height=50, corner_radius=12, font=("Helvetica", 16, "bold"),
                                       command=self.intentar_login)
        self.btn_login.pack(fill="x", padx=35, pady=(20, 40))

        # --- SECCIÓN INFERIOR ---
        ctk.CTkLabel(self.main_frame, text="¿Aún no tienes una cuenta?", font=("Helvetica", 13), text_color="#1E293B").pack(pady=(40, 0))
        self.btn_signup = ctk.CTkButton(self.main_frame, text="Crear cuenta", fg_color="transparent", 
                                         text_color="#006064", font=("Helvetica", 13, "bold"), hover=False,
                                         command=self.ir_a_registro)
        self.btn_signup.pack()

    # (Las funciones intentar_login e ir_a_registro se mantienen igual que el código anterior)
    def intentar_login(self):
        from app.controladores.auth_controller import AuthController
        control = AuthController()
        if control.validar_acceso(self.ent_dni.get(), self.ent_pass.get()):
            self.main_frame.pack_forget()
            self.on_success()

    def ir_a_registro(self):
        from app.vistas.registro_view import RegistroView
        self.main_frame.pack_forget()
        RegistroView(self.root, al_finalizar=self.reabrir_login)

    def reabrir_login(self):
        self.main_frame.pack(fill="both", expand=True)
