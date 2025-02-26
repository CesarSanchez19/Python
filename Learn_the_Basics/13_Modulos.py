### Módulos en Python ###

"""
Los módulos en Python son archivos que contienen definiciones y declaraciones de funciones, clases y variables 
que pueden ser reutilizados en otros programas. Esto permite organizar mejor el código y evitar la repetición.

Tipos de módulos:
1. **Módulos propios**: Archivos Python creados por nosotros mismos.
2. **Módulos del sistema**: Módulos que vienen preinstalados con Python, como `math`, `random`, `os`.
3. **Módulos de terceros**: Librerías externas que podemos instalar con `pip`, como `numpy`, `pandas`.
"""

# Importación de un módulo propio
import my_module  # Importa todas las funciones y variables definidas en el módulo my_module.py

# Reglas de nomenclatura: 
# - Un nombre de módulo no puede comenzar con un número (Ejemplo incorrecto: 12_module.py)
# - Se recomienda que los nombres de los módulos sean en minúsculas y con guiones bajos si es necesario una separacion

# Importación de funciones específicas de un módulo
from my_module import sumValue, printValue  # Importa solo sumValue y printValue desde my_module

# Uso de las funciones importadas desde my_module
my_module.sumValue(5, 3, 1)  # Llamada con prefijo del módulo
my_module.printValue("Hola Python!")

# También podemos llamar a las funciones sin prefijo si las importamos directamente
sumValue(5, 3, 1)
printValue("Hola Python")

# Importación de módulos del sistema
import math  # Módulo para operaciones matemáticas avanzadas
import random  # Módulo para generación de números aleatorios

# Uso de funciones del módulo math
print(math.pi)  # Imprime el valor de pi
print(math.pow(2, 8))  # Eleva 2 a la potencia de 8 (2^8 = 256)

# Asignación de alias a funciones o variables de un módulo para facilitar su uso
from math import pi as Pi_Value  # Importamos pi y le damos un alias

print(Pi_Value)  # Accedemos directamente a la constante pi sin usar math.pi

### Casos útiles para usar módulos en proyectos ###

# 1. Manejo de archivos y directorios
import os  # Permite interactuar con el sistema operativo
print(os.listdir("."))  # Lista los archivos en el directorio actual

# 2. Trabajo con fechas y tiempos
import datetime
fecha_actual = datetime.datetime.now()
print("Fecha y hora actual:", fecha_actual)

# 3. Peticiones HTTP y consumo de APIs
import requests
respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(respuesta.json())  # Imprime el contenido en formato JSON

# 4. Manejo de bases de datos con SQLite
import sqlite3
conexion = sqlite3.connect("mi_base_de_datos.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT)")
conexion.commit()
conexion.close()

# 5. Serialización y deserialización de datos con JSON
import json
datos = {"nombre": "Juan", "edad": 30}
datos_json = json.dumps(datos)  # Convierte un diccionario en una cadena JSON
print(datos_json)

### Buenas prácticas en el uso de módulos ###
# 1. Importar solo lo necesario para mejorar el rendimiento y la claridad del código.
# 2. Usar alias (`as`) cuando el nombre de un módulo o función es largo o poco claro.
# 3. Mantener los módulos organizados en archivos separados según su funcionalidad.
# 4. Evitar la importación de todo (`from module import *`), ya que puede generar conflictos de nombres.
# 5. Documentar correctamente los módulos para facilitar su comprensión y reutilización.
