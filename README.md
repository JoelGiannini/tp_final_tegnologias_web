# 🚀 Aplicación de Comandos Web (comandos_app)

Este proyecto es una aplicación web sencilla construida con **Flask** que te permite gestionar una base de datos de comandos de línea. Puedes buscar, agregar, editar y eliminar comandos de forma rápida y eficiente.

## 📁 Estructura del Proyecto

El proyecto sigue una arquitectura modular para mantener el código limpio y escalable.
```bash
├── app/
│   ├── forms.py            # Definición de formularios con Flask-WTF
│   ├── init.py         # Inicialización de la app y del Blueprint
│   ├── models.py           # Modelos de la base de datos (SQLAlchemy)
│   ├── routes.py           # Lógica de las rutas (CRUD)
│   ├── static/             # Archivos estáticos (CSS, JS)
│   │   └── style.css       # Hoja de estilos principal
│   └── templates/          # Plantillas HTML (Jinja2)
│       ├── add.html        # Formulario para agregar un nuevo comando
│       ├── base.html       # Plantilla base
│       ├── edit.html       # Formulario para editar un comando
│       ├── form.html       # Componente de formulario reutilizable
│       └── index.html      # Página principal y de búsqueda
├── Dockerfile              # Instrucciones para construir la imagen de Docker
├── requirements.txt        # Dependencias de Python
├── run.py                  # Punto de entrada de la aplicación
└── README.md

```

## 🛠️ Tecnologías Utilizadas

* **Python**: Lenguaje de programación.
* **Flask**: Framework web para construir la aplicación.
* **Flask-SQLAlchemy**: ORM para interactuar con la base de datos **SQLite**.
* **Flask-WTF**: Extensión para la gestión de formularios web.
* **Html**: Es el lenguaje principal que se usa para crear páginas web.
* **Css**: Es un lenguaje que se usa para dar estilo y diseño a las páginas web.
* **Jinja2**: Motor de plantillas HTML.
* **Docker**: Para la contenerización del proyecto.

## ✨ Características Principales

* **Búsqueda Dinámica**: La lista de comandos solo se muestra al realizar una búsqueda por nombre, descripción o sistema operativo.
* **Gestión de Comandos (CRUD)**: La aplicación permite crear, leer, actualizar y eliminar comandos fácilmente.
* **Interfaz de Usuario Sencilla**: El diseño es minimalista y enfocado en la funcionalidad.
* **Contenerización con Docker**: El proyecto está listo para ser empaquetado y desplegado usando Docker, simplificando la gestión de dependencias y la configuración del entorno.

---

## 🚀 Cómo Empezar

### Con Docker (Método recomendado)

Este método es el más sencillo, ya que el `Dockerfile` **se encarga automáticamente de instalar todas las dependencias y configurar la base de datos** al construir la imagen. No necesitas realizar pasos de configuración manual.

1.  Clona el repositorio:
    ```bash
    git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
    cd tu-repositorio
    ```
2.  Construye la imagen de Docker:
    ```bash
    docker build -t comandos-app .
    ```
3.  Ejecuta el contenedor:
    ```bash
    docker run -p 5000:5000 comandos-app
    ```

La aplicación estará disponible en `http://localhost:5000`.

### Sin Docker (Método manual)

1.  Clona el repositorio:
    ```bash
    git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
    cd tu-repositorio
    ```
2.  Crea un entorno virtual e instala las dependencias:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Configura la base de datos (paso manual):**
    ```bash
    python3 -c "from app import db; db.create_all()"
    ```
4.  Ejecuta la aplicación:
    ```bash
    python3 run.py
    ```

La aplicación estará disponible en `http://127.0.0.1:5000`.

---
## 🎥 Video demostrativo de deploy de app y funcionamiento:

[![Video demostrativo de la app en funcionamiento](https://img.youtube.com/vi/rD0_iyl7WI8/0.jpg)](https://youtu.be/rD0_iyl7WI8)


## 🤝 Contribuciones

Las contribuciones son bienvenidas. Sentite libre de abrir un "pull request" y mejorar el codigo.

## 📝 Licencia

Este proyecto está bajo la licencia **MIT**, que es una de las licencias más permisivas. Te permite usar, modificar y distribuir el código libremente, incluso en proyectos comerciales, siempre y cuando incluyas una copia del texto original de la licencia y el aviso de copyright.
