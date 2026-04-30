from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'sistema_tech_2026_key' 

# --- CONFIGURACIÓN DE RUTAS DE BASE DE DATOS ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'sistema_tech.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, timeout=20)
    conn.row_factory = sqlite3.Row
    return conn

# --- RUTAS DE NAVEGACIÓN ---

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario_nombre' not in session:
        return redirect(url_for('home'))
    return render_template('dashboard.html', nombre=session['usuario_nombre'])

# --- LÓGICA DE USUARIOS ---

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    dni = request.form['dni']
    nombre = request.form['nombre']
    correo = request.form['correo']
    password = request.form['password']
    
    try:
        with get_db_connection() as conn:
            conn.execute('''
                INSERT INTO usuarios (dni, nombre, correo, password) 
                VALUES (?, ?, ?, ?)
            ''', (dni, nombre, correo, password))
            conn.commit()
        return redirect(url_for('home'))
    except sqlite3.IntegrityError:
        return "<h1>Error: El DNI ya existe</h1><a href='/registro'>Regresar</a>"
    except Exception as e:
        return f"<h1>Error al registrar: {e}</h1><a href='/registro'>Regresar</a>"

@app.route('/login', methods=['POST'])
def login():
    dni = request.form['dni']
    password = request.form['password']
    
    with get_db_connection() as conn:
        user = conn.execute('SELECT * FROM usuarios WHERE dni = ? AND password = ?',
                            (dni, password)).fetchone()
    
    if user:
        session['usuario_nombre'] = user['nombre']
        session['usuario_dni'] = user['dni']
        return redirect(url_for('dashboard'))
    else:
        return "<h1>DNI o Contraseña incorrectos</h1><a href='/'>Intentar de nuevo</a>"

# --- LÓGICA DE CITAS MÉDICAS (ARREGLADA) ---

@app.route('/agendar/<especialidad>')
def agendar(especialidad):
    if 'usuario_nombre' not in session:
        return redirect(url_for('home'))
    return render_template('agendar.html', especialidad=especialidad)

@app.route('/confirmar_cita', methods=['POST'])
def confirmar_cita():
    # TEST RÁPIDO: Si el servidor recibe algo, lo primero que hará es imprimir esto
    print("--- RECIBIENDO DATOS DE CITA ---")
    
    try:
        # Extraemos los datos del formulario
        dni = request.form.get('dni')
        especialidad = request.form.get('especialidad')
        doctor = request.form.get('doctor')
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        
        # Guardamos en la base de datos[cite: 1, 3]
        with get_db_connection() as conn:
            conn.execute('''
                INSERT INTO citas (dni_paciente, especialidad, doctor, fecha, hora) 
                VALUES (?, ?, ?, ?, ?)
            ''', (dni, especialidad, doctor, fecha, hora))
            conn.commit()
        
        # RESPUESTA DIRECTA: No usamos render_template por ahora, 
        # enviamos el HTML directamente para asegurar que lo veas.
        return f"""
        <div style="text-align:center; margin-top:50px; font-family:sans-serif; color:#00796b;">
            <h1>✅ ¡CITA REGISTRADA CON ÉXITO!</h1>
            <hr style="width:50%;">
            <p><strong>Especialidad:</strong> {especialidad}</p>
            <p><strong>Doctor:</strong> {doctor}</p>
            <p><strong>Fecha:</strong> {fecha}</p>
            <p><strong>Hora:</strong> {hora}</p>
            <br>
            <a href="/dashboard" style="padding:10px 20px; background:#00796b; color:white; text-decoration:none; border-radius:5px;">Volver al Panel</a>
        </div>
        """
            
    except Exception as e:
        return f"<h1>Ocurrió un error:</h1><p>{str(e)}</p><a href='/dashboard'>Regresar</a>"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)
