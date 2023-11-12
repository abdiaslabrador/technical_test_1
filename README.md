# Prueba técnica
Esto es una prueba técnica para practicar habilidades en django rest framework.
El objetivo de la prueba técnica consistía en hacer peticiones a una api de chistes y a otra realacionada con matemáticas. Para el end-point de chistes se requería que:

# Metas
La prueba consiste en crear un API Rest en el framework Django utilizando los siguientes repositorios para realizar las solicitudes:
- https://api.chucknorris.io/
- https://icanhazdadjoke.com/api

**Endpoint de chistes**
- GET: devolverá un chiste aleatorio si no se pasa ningún path param. Si se envía el path param habrá que comprobar si tiene el valor “Chuck” o el valor “Dad”. Si tiene el valor “Chuck” se conseguirá el chiste de este API https://api.chucknorris.io, si tiene el valor “Dad” se conseguirá del API https://icanhazdadjoke.com/api, en caso de que el valor no sea ninguno de esos dos se devolverá el error correspondiente.

- POST:  guardará en una base de datos el chiste (texto pasado por parámetro)

- UPDATE: actualiza el chiste con el nuevo texto sustituyendo al chiste indicado en el parámetro “number”.

- DELETE: elimina el chiste indicado en el parametro number.

**Endpoint matemático**

- GET: Endpoint al que se le pasará un query param llamado “numbers” con una lista de números enteros. La respuesta de este endpoint debe ser el mínimo común múltiplo de ellos'.

- GET: Endpoint al que se le pasará un query param llamado “number” con un número entero. La respuesta será ese número + 1.

Para  los end-points de chistes se tiene la url "api/", "api/Chuck", "api/Dad" y para el de matemáticas se tiene la url "api/math_endpoint/"
