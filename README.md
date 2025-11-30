# gestor de tareas
proyecto sencillo con CRUD para usuarios autenticados e incluye demo de video en inspiración de piano roll hecho con pygames.
Gestor de Tareas - Taller de Música en Colores

Este proyecto es una pequeña aplicación web para gestionar tareas. Permite a los usuarios autenticarse, crear, ver y eliminar tareas, y ver la lista de sus tareas asignadas.

La interfaz está diseñada con Bootstrap para que sea responsiva y amigable, y el proyecto sigue buenas prácticas de Django en cuanto a autenticación y estructura de vistas.

## Estructura del proyecto
```bash
.
│── gestor_tareas/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tareas/
│   ├── templates/tareas/
│   │   ├──tareas
│   │   │   ├── base.html
│   │   │   ├── lista.html
│   │   │   ├── detalle.html
│   │   │   ├── agregar.html
│   │   │   └── eliminar.html
│   │   └── registration
│   │           ├── login.html
│   │           ├── register.html
│   │           └── logged_out.html
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
└── manage.py

```

## Funcionalidades implementadas

- Registro, login y logout de usuarios

- Lista de tareas asociadas a cada usuario

- Detalle de cada tarea

- Agregar nuevas tareas

- Eliminar tareas

- Interfaz responsiva con Bootstrap 5

## Instalación
1. Clonar el repositorio
```bash
git clone https://github.com/npuntorodriguez/gestor_tareas_modulo_6
cd gestor_tareas
```

2. Crear un entorno virtual
```bash
python -m venv venv
```

3. Activar el entorno virtual:
```bash
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. Instalar dependencias
```bash
pip install -r requirements.txt
```

5. Migrar la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Crear superusuario (opcional)  
```bash
python manage.py createsuperuser
``` 

7. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

8. Acceder a la aplicación en: http://127.0.0.1:8000/


