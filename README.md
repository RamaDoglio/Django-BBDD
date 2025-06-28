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
