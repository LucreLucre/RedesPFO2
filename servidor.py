from flask import Flask, request, jsonify, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "clave-secreta-desarrollo"
DB = "tareas.db"

def conectar_db():
    conexion = sqlite3.connect(DB)
    conexion.row_factory = sqlite3.Row
    return conexion

def inicializar_db():
    conexion = conectar_db()
    conexion.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        contraseña TEXT NOT NULL
    )""")
    conexion.commit()
    conexion.close()

@app.route("/registro", methods=["POST"])
def registro():
    datos = request.get_json()
    if not datos or "usuario" not in datos or "contraseña" not in datos:
        return jsonify({"error": "Faltan usuario o contraseña"}), 400
    if not datos["usuario"] or not datos["contraseña"]:
        return jsonify({"error": "Usuario y contraseña no pueden estar vacíos"}), 400

    conexion = conectar_db()
    try:
        conexion.execute(
            "INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
            (datos["usuario"], generate_password_hash(datos["contraseña"]))
        )
        conexion.commit()
    except sqlite3.IntegrityError:
        conexion.close()
        return jsonify({"error": "El usuario ya existe"}), 409
    conexion.close()
    return jsonify({"mensaje": "Usuario registrado correctamente"}), 201

@app.route("/login", methods=["POST"])
def login():
    datos = request.get_json()
    if not datos or "usuario" not in datos or "contraseña" not in datos:
        return jsonify({"error": "Faltan usuario o contraseña"}), 400

    conexion = conectar_db()
    usuario = conexion.execute(
        "SELECT * FROM usuarios WHERE usuario = ?", (datos["usuario"],)
    ).fetchone()
    conexion.close()

    if usuario is None or not check_password_hash(usuario["contraseña"], datos["contraseña"]):
        return jsonify({"error": "Credenciales incorrectas"}), 401

    session["usuario"] = usuario["usuario"]
    return jsonify({"mensaje": "Inicio de sesión exitoso", "usuario": usuario["usuario"]})

@app.route("/tareas", methods=["GET"])
def tareas():
    if "usuario" not in session:
        return """<html><body><h1>Acceso denegado</h1>
        <p>Debés iniciar sesión para acceder a las tareas.</p></body></html>""", 401

    return f"""<html><head><meta charset="UTF-8">
    <title>Gestión de Tareas</title></head><body>
    <h1>Bienvenido/a, {session["usuario"]}</h1>
    <p>Has iniciado sesión correctamente.</p>
    <p>Esta es la sección de gestión de tareas.</p>
    </body></html>"""

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return jsonify({"mensaje": "Sesión cerrada"})

if __name__ == "__main__":
    inicializar_db()
    app.run(host="127.0.0.1", port=5000, debug=True)
