### Hash Tables ###

"""

Una Hash Table es una estructura de datos que almacena pares clave-valor.
En Python, los diccionarios (`dict`) implementan Hash Tables de manera eficiente.

✅ Características:
- Inserción, eliminación y búsqueda en **O(1)** en promedio.
- Uso de una función hash para asignar índices únicos a cada clave.
- Puede manejar colisiones con técnicas como encadenamiento o direccionamiento abierto.
"""

## Primera parte o uso basico del hash table

def hash_key( key, m):
    return key % m

m = 7 # Definimos la longitud o la cantidad de slots que tendra la tabla

print(f'The hash value for 3 is {hash_key(3,m)}')

## Aqui hay una colision entre 2 y 9
print(f'The hash value for 2 is {hash_key(2,m)}')
print(f'The hash value for 9 is {hash_key(9,m)}')

print(f'The hash value for 11 is {hash_key(11,m)}')
print(f'The hash value for 7 is {hash_key(7,m)}')



# 📌 Ejemplo 1: Creación de una Hash Table en Python
hash_table = {"nombre": "Carlos", "edad": 25, "ciudad": "Madrid"}
print(hash_table)  # {'nombre': 'Carlos', 'edad': 25, 'ciudad': 'Madrid'}

# Imprime las claves (keys) que contenga el diccionario
print(hash_table.keys())

# Imprime los valores (values) que contenga el diccionario
print(hash_table.values())

# Imprime todos las clave-valor (items) que contenga el diccionario
print(hash_table.items())

# 📌 Ejemplo 2: Inserción de un nuevo par clave-valor
hash_table["profesion"] = "Ingeniero"
print(hash_table)  # {'nombre': 'Carlos', 'edad': 25, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# 📌 Ejemplo 3: Búsqueda de un valor por su clave
print(hash_table["ciudad"])  # Madrid

# 📌 Ejemplo 4: Eliminación de un elemento
del hash_table["edad"]
print(hash_table)  # {'nombre': 'Carlos', 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

"""
📌 Función hash en Python
La función `hash()` convierte un valor en un número hash único.
"""
clave = "Python"
print(hash(clave))  # Devuelve un número hash único

# 📌 Ejemplo 5: Uso de la función hash con múltiples valores
datos = ["perro", "gato", "elefante"]
hashes = {dato: hash(dato) for dato in datos}
print(hashes)  # Muestra el hash de cada palabra

"""
📌 Manejo de colisiones con Encadenamiento en una Clase
Si dos claves generan el mismo hash, almacenamos múltiples valores en una lista.
"""
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Actualizar valor si la clave ya existe
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Retorna None si la clave no se encuentra
    
    def delete(self, key):
        index = self._hash(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]

# Uso de la tabla hash
hash_map = HashTable(10)
hash_map.insert("nombre", "Carlos")
hash_map.insert("edad", 25)
hash_map.insert("ciudad", "Madrid")
print(hash_map.get("nombre"))  # Carlos
hash_map.delete("edad")
print(hash_map.get("edad"))  # None

"""
📌 Casos de Uso de Hash Tables en Python
"""
# Caso 1: Contar la frecuencia de elementos en una lista
palabras = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
print(frecuencia)  # {'manzana': 3, 'banana': 2, 'naranja': 1}

# Caso 2: Almacenar y buscar información de usuarios
usuarios = {
    "001": {"nombre": "Carlos", "edad": 25, "ciudad": "Madrid"},
    "002": {"nombre": "Ana", "edad": 30, "ciudad": "Barcelona"},
}
print(usuarios["002"])  # {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Barcelona'}

# Caso 3: Detectar duplicados en una lista grande
numeros = [10, 20, 30, 40, 10, 50, 60, 20]
vistos = {}
duplicados = [num for num in numeros if vistos.setdefault(num, 0) == 1]
print(duplicados)  # [10, 20]

# Caso 4: Implementar una caché para evitar cálculos repetidos
cache = {}
def factorial(n):
    if n in cache:
        return cache[n]
    resultado = 1 if n in (0, 1) else n * factorial(n - 1)
    cache[n] = resultado
    return resultado
print(factorial(5))  # 120
print(factorial(6))  # 720 (reutiliza factorial(5))

# Caso 5: Contar caracteres en un texto
texto = "programacion en python"
conteo = {}
for caracter in texto:
    conteo[caracter] = conteo.get(caracter, 0) + 1
print(conteo)

# Caso 6: Usar una Hash Table para registrar estudiantes y sus notas
notas_estudiantes = {
    "Carlos": [90, 85, 88],
    "Ana": [78, 80, 85],
    "Pedro": [92, 88, 95]
}
print(notas_estudiantes["Ana"])  # [78, 80, 85]

# Caso 7: Uso de un diccionario como un cache simple para mejorar rendimiento
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]
print(fibonacci(10))  # 55
