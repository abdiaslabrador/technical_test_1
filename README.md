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

# Instalación (sin usar docker)
1- Para correr la aplicación se debe contar con Python en la version 3.11.3 y postgreSQL 15.2 (Python: https://www.python.org/downloads/ PostgreSQL: https://www.postgresql.org/).

2- Se recomienda usar un entorno virtual para trabajar:

  Para crear el entorno virtual: ```python -m venv env```

  Para activar el entorno virtual: ```env\Scripts\activate.bat```

3- Al activar el entorno virtual ejecuta el siguiente comando para instalar las dependencias del proyecto:

```pip install -r requirements.txt```

4- Previamente y antes de abrir el proyecto se debe crear la base de datos en postgreSQL.

5- Se debe crear el archivo .env en la raíz del proyecto y establecer los parámetros de acuerdo a tu configuración de conexión base de datos, ejemplo:

```
DB_NAME=technical_test
DB_USER=root
DB_PASSWORD=123456
DB_HOST=localhost
DB_PORT=5432
```
6- Dentro del entorno virtual ejecutar las migraciones con el comando:

```python manage.py migrate```

7- Finalmente, ejecutar el proyecto con:

```python manage.py runserver```

# Endpoints
El proyecto cuenta en total con tres endpoints, dos de ellos son correspondientes al de Chistes (jokes), y el otro al endpoint matemático (math).

![Captura de pantalla 2023-11-14 113922](https://github.com/abdiaslabrador/technical_test_1/assets/44957286/f5b356db-fa52-4a36-8703-fe4a93666c85)

**ENDPOINT /jokes/:**

- GET: Obtiene un chiste aleatorio.
- POST: Agrega un nuevo chiste por query param "text".
- PUT: Modificar chiste almacenado; tiene dos query params: "joke" como el texto con el nuevo chiste y "number" el ID del chiste a modificar.
- DELETE: Elimina chiste almacenado; tiene un query param "number", el cuál corresponde al ID del chiste a eliminar.

**ENDPOINT /jokes/{select}/**
- GET: Obtiene un chiste aleatorio por medio de consulta de api, tiene un path param el cuál debe ser "Chuck"o "Dad", en caso de no colocar ninguno lanza error.
 
**ENDPOINT /math/**
- GET: tiene dos query params, "number" obtiene el cálculo del número introducido por query param + 1 y "numbers" obtiene el mínimo común múltiplo del arreglo de enteros introducido por query param, ejemplo del arraglo: numbers=1,2,3,4.

# Test
Para probar los test escribe el comando ```python manage.py test api```. 

# Instalación y configuración usando docker
- Se debe crear el archivo .env en la raíz del proyecto y establecer los parámetros de acuerdo a tu configuración de conexión de base de datos y las variables de entorno de docker, ya que docker define sus propias variables de entorno para conectar con postgres.
- El valor de POSTGRES_HOST tiene que ser igual al nombre del servicio de la base de datos que se colocó en el archivo docker-compose, que para este caso le coloqué como nombre al servicio "db", ejemplo:

en el archivo .env
```
POSTGRES_DB=technical_test
POSTGRES_USER=abdias
POSTGRES_PASSWORD=123456
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
y en el docker-compose.yaml
```
db:
    image: postgres:16
    env_file: .env
```
- Vete a la raíz del proyecto y ejecuta este comando para instalar la imagen y cada dependencia necesaria en el proyecto:

```docker compose build```

Cuando finalice la instalación ejecuta el siguiente comando para correr el servidor:

```docker compose up```

Ya corriendo el servidor dirígete a http://localhost:8000/ y verás la aplicación corriendo
