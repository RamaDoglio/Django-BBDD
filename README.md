# Django-BBDD

https://github.com/pindutn/fabrica_pastas/tree/main

## PASOS

### 1. Generar los proyectos

```sh
docker compose run --rm generate
sudo chown $USER:$USER -R .
docker compose up -d backend
```

### 2. Migrar la base de datos

```sh
docker compose run --rm manage makemigrations
docker compose run --rm manage migrate
```

### 3. Crear superusuario

```sh
docker compose run --rm manage createsuperuser
```

### 4. Cargar datos

```sh
docker compose run --rm manage loaddata initial_data
```

Ahora podes ir a localhost:8000/admin, loguearte con el usuario que creaste antes y crear o ver objetos!!

# Migrar todo a mongodb

### 1. Añadir el servicio de mongodb al docker compose

```docker
 mongo:
    image: mongo:latest
    container_name: mongo
    environment:
      - MONGO_INITDB_ROOT_USERNAME=mongo
      - MONGO_INITDB_ROOT_PASSWORD=mongo
      - MONGO_INITDB_DATABASE=mongo
    volumes:
      - mongo-data:/data/db
    ports:
      - "27017:27017"
    networks:
      - net

 volumes:
  mongo-data:
```

### 2. Cambiar la primera linea del models.py

```python
from djongo import models
```

### 3. Cambiar la conexion con la base de datos en settings.py

```python
DATABASES = {
"default": {
"ENGINE": "djongo",
"NAME": "mongo",
"CLIENT": {
"host": "mongo",
"port": 27017,
"username": "mongo",
"password": "mongo",
"authSource": "admin", # Importante para autenticación
},
}
}
```

### 4. Eliminar todos los archivos en la carpeta app/migrations/ hechos anteriormente menos el **init.py**

### 5. Buildear todo de nuevo

```bash
docker compose build
```

### 6. Levantar la base de datos mongodb

```bash
docker compose up -d
```

### 7. Migrar los modelos para mongodb

```bash
docker compose run manage makemigrations
docker compose run manage migrate
```

### 8. Crear superusuario

```sh
docker compose run --rm manage createsuperuser
```

### 9.
