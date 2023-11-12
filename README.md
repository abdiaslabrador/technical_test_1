# Prueba técnica
Esto es una prueba técnica para practicar habilidades en django rest framework.
El objetivo de la prueba técnica consistía en hacer peticiones a una api de chistes y a otra realacionada con matemáticas. Para el end-point de chistes se requería que:

# Metas
La prueba consiste en crear una API Rest de chistes y matemática con Django framework, utilizando los siguientes repositorios para el endpoint de chistes:
- https://api.chucknorris.io/
- https://icanhazdadjoke.com/api

**Endpoint de chistes**
- GET: devolverá un chiste aleatorio si no se pasa ningún path param. Si se envía el path param habrá que comprobar si tiene el valor “Chuck” o el valor “Dad”. Si tiene el valor “Chuck” se conseguirá el chiste de este API https://api.chucknorris.io, si tiene el valor “Dad” se conseguirá del API https://icanhazdadjoke.com/api, en caso de que el valor no sea ninguno de esos dos se devolverá el error correspondiente.

- POST:  guardará en una base de datos el chiste (texto pasado por parámetro).

- UPDATE: actualiza el chiste con el nuevo texto sustituyendo al chiste indicado en el parámetro “number”.

- DELETE: elimina el chiste indicado en el parametro number.

**Endpoint matemático**
- GET: Endpoint al que se le pasará un query param llamado “numbers” con una lista de números enteros. La respuesta de este endpoint debe ser el mínimo común múltiplo de ellos'.

- GET: Endpoint al que se le pasará un query param llamado “number” con un número entero. La respuesta será ese número + 1.

# Tecnología utilizada
- PostgreSQL 15.2
- Python 3.11.3 (última hasta el momento)
- Django 4.2.7
- Django REST Framework 3.14.0
- drf-yasg 1.21.7 (swagger)

# Instalación
1- Para correr la aplicación se debe contar con Python en la version 3.11.3 y postgreSQL 15.2 (Python: https://www.python.org/downloads/ PostgreSQL: https://www.postgresql.org/).

2- Se recomienda usar un entorno virtual para trabajar:

  Para crear el entorno virtual: ```python -m venv env```

  Para activar el entorno virtual: ```env\Scripts\activate.bat```

3- Al activar el entorno virtual ejecuta el siguiente comando para instalar las dependencias del proyecto:

```pip install -r requirements.txt```

4- Se debe crear el archivo .env en la raíz del proyecto y establecer los parámetros de acuerdo a tu configuración de conexión base de datos y tu SECRET_KEY, ejemplo:

```
DB_NAME=technical_test
DB_USER=root
DB_PASSWORD=123456
DB_HOST=localhost
DB_PORT=5432
```
5- Dentro del entorno virtual ejecutar las migraciones con el comando:

```python manage.py migrate```

6- Finalmente, ejecutar el proyecto con:

```python manage.py runserver```

Para  los end-points de chistes se tiene la url "api/", "api/Chuck", "api/Dad" y para el de matemáticas se tiene la url "api/math_endpoint/"
