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

<img width="863" height="436" alt="image" src="https://github.com/user-attachments/assets/f948dffa-97ee-498c-86a6-24e058677528" />

<img width="887" height="417" alt="image" src="https://github.com/user-attachments/assets/9901f2b2-ba6a-44ab-be40-3cc993e63798" />

<img width="618" height="361" alt="image" src="https://github.com/user-attachments/assets/1699bbe8-2197-4f86-8403-eb13922dd4f0" />

<img width="632" height="376" alt="image" src="https://github.com/user-attachments/assets/3abf7fce-dfb1-4c1f-83b7-6dc078d8f0d6" />

## Respuestas conceptuales

### ¿Por qué hashear contraseñas?

Porque no deben almacenarse en texto plano. Si alguien obtiene la base de
datos, el hash evita que las contraseñas originales queden expuestas
directamente.

### ¿Ventajas de SQLite?

Es una base de datos liviana, basada en un archivo y no necesita un servidor
de base de datos independiente. Es sencilla y suficiente para un proyecto
pequeño como este.
