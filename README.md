# API-PAGOS

REST API de pagos utilizando arquitectura hexagonal

## Running

Para lanzar la aplicación se utiliza la herramienta de Docker, docker-compose, de manera sencilla con el comando

    docker-compose -f docker-compose.yml up -d

## Lógica de la API

- 
- El campo "valorPagado" deberá estar entre 1 y 1000000 (1 millón)
- El valor del arriendo total mensual para todo es 1 millón


## Cosas para mejorar

Se debe de implementar la posibidad de pagos nuevos (cambiando las keys)


    Column('documentoIdentificacionArrendatario', String, primary_key=True),
    Column('codigoInmueble', String, primary_key=True),
    Column('fechaPago', String, nullable=False),
    Column('valorPagado', String, nullable=False)


## Test

Para correr las pruebas del código se utiliza el comando

    docker-compose exec api python -m unittest discover

## File tree
   
    .
    ├── src
    │   ├── application
    │   │   ├── services
    │   │   │   ├── __init__.py
    │   │   │   ├── payment_methods.py
    │   │   │   └── validation_payment.py
    │   │   ├── __init__.py
    │   │   └── exceptions.py
    │   ├── controller
    │   │   ├── __init__.py
    │   │   ├── app.py
    │   │   └── exceptions.py
    │   ├── domain
    │   │   ├── models
    │   │   │   ├── __init__.py
    │   │   │   └── payment.py
    │   │   ├── repositories
    │   │   │   ├── __init__.py
    │   │   │   └── payment_interface.py
    │   │   └── __init__.py
    │   ├── infra
    │   │   ├── repositories
    │   │   │   ├── __init__.py
    │   │   │   ├── base_repository.py
    │   │   │   └── payment_repository.py
    │   │   ├── __init__.py
    │   │   └── database.py
    │   ├── test
    │   │   ├── infra
    │   │   │   ├── __init__.py
    │   │   │   └── test_repositories.py
    │   │   ├── __init__.py
    │   │   └── base_test.py
    │   ├── tmp
    │   ├── Dockerfile
    │   └── requirements.txt
    ├── commands.sh
    ├── docker-compose.yml
    └── README.md