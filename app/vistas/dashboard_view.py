import customtkinter as ctk

class DashboardView:
    def __init__(self, root, nombre_usuario):
        self.root = root
        
        # Contenedor principal
        self.frame = ctk.CTkFrame(master=root, fg_color="#F8FAFC")
        self.frame.pack(fill="both", expand=True)

        # Barra Superior de Bienvenida
        top_bar = ctk.CTkFrame(self.frame, fg_color="#006064", height=80, corner_radius=0)
        top_bar.pack(fill="x", side="top")

        ctk.CTkLabel(top_bar, text=f"Bienvenido, {nombre_usuario}", 
                     font=("Helvetica", 18, "bold"), text_color="white").pack(side="left", padx=30, pady=20)

        # --- CUERPO DEL DASHBOARD ---
        content = ctk.CTkFrame(self.frame, fg_color="transparent")
        content.pack(pady=40, padx=40, fill="both", expand=True)

        ctk.CTkLabel(content, text="¿Qué desea realizar hoy?", 
                     font=("Helvetica", 20, "bold"), text_color="#1E293B").pack(pady=(0, 30))

        # Botón Reservar Cita (Basado en tu flujo)
        self.btn_cita = ctk.CTkButton(content, text="RESERVAR NUEVA CITA", 
                                      fg_color="#007F8C", hover_color="#005F69",
                                      height=60, corner_radius=15, 
                                      font=("Helvetica", 16, "bold"),
                                      command=self.ir_a_reserva)
        self.btn_cita.pack(fill="x", pady=10)

        # Botón Ver Mis Pagos
        self.btn_pagos = ctk.CTkButton(content, text="MIS PAGOS Y RECIBOS", 
                                       fg_color="white", text_color="#007F8C",
                                       border_width=2, border_color="#007F8C",
                                       height=60, corner_radius=15, 
                                       font=("Helvetica", 16, "bold"))
        self.btn_pagos.pack(fill="x", pady=10)

        # Botón Cerrar Sesión
        ctk.CTkButton(self.frame, text="Cerrar Sesión", fg_color="transparent", 
                      text_color="#E11D48", font=("Helvetica", 13, "bold"),
                      command=self.cerrar_sesion).pack(pady=20)

    def ir_a_reserva(self):
        print("Cambiando al Módulo de Reserva de Citas...")
        # Aquí conectaremos con el formulario de citas después

    def cerrar_sesion(self):
        import sys
        sys.exit() # Por ahora cerramos, luego podemos volver al login
        