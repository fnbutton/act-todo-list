## Pasos de instalación

### 1. Clonar o descargar el proyecto

```bash
git clone <repository-url>
cd django-todo-list
```

O descargar el archivo ZIP desde el repositorio.

### 2. Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Navegar a la carpeta del proyecto

```bash
cd project
```

### 6. Configurar la base de datos

```bash
python manage.py project/migrate
```


### 7. Ejecutar el servidor

```bash
python manage.py project/runserver
```

El servidor estará disponible en `http://localhost:8000`
