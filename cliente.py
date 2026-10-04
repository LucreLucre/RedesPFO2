import requests

URL = "http://127.0.0.1:5000"
sesion = requests.Session()

def registrar():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    r = sesion.post(f"{URL}/registro", json={"usuario": usuario, "contraseña": contraseña})
    print(r.status_code, r.json())

def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    r = sesion.post(f"{URL}/login", json={"usuario": usuario, "contraseña": contraseña})
    print(r.status_code, r.json())
    if r.ok:
        tareas()

def tareas():
    r = sesion.get(f"{URL}/tareas")
    print("\n--- /tareas ---")
    print(r.status_code)
    print(r.text)

def logout():
    r = sesion.get(f"{URL}/logout")
    print(r.status_code, r.json())

while True:
    print("""
=== GESTIÓN DE TAREAS ===
1. Registrar usuario
2. Iniciar sesión
3. Ver tareas
4. Cerrar sesión
5. Salir
""")
    opcion = input("Elegí una opción: ")
    if opcion == "1":
        registrar()
    elif opcion == "2":
        login()
    elif opcion == "3":
        tareas()
    elif opcion == "4":
        logout()
    elif opcion == "5":
        break
    else:
        print("Opción inválida.")
