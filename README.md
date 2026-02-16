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

### 6. Configurar la base de datos

```bash
python project/manage.py migrate
```


### 7. Ejecutar el servidor

```bash
python project/manage.py runserver
```

El servidor estará disponible en `http://localhost:8000`
