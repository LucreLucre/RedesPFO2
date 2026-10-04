# PFO 2 - Sistema de Gestión de Tareas

Sistema de Gestión de Tareas con API y Base de Datos

## Ejecutar
pip install flask requests
python servidor.py


En otra terminal:

python cliente.py

## Endpoints

- `POST /registro`: registra usuario y guarda la contraseña hasheada.
- `POST /login`: verifica credenciales y crea una sesión.
- `GET /tareas`: muestra HTML de bienvenida.
- `GET /logout`: cierra la sesión.

## Pruebas

Registrar usuario -> iniciar sesión -> ver tareas-> cerrar sesión

## Respuestas conceptuales

### ¿Por qué hashear contraseñas?

Porque no deben almacenarse en texto plano. Si alguien obtiene la base de
datos, el hash evita que las contraseñas originales queden expuestas
directamente.

### ¿Ventajas de SQLite?

Es una base de datos liviana, basada en un archivo y no necesita un servidor
de base de datos independiente. Es sencilla y suficiente para un proyecto
pequeño como este.
