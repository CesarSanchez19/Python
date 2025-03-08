### Hash Tables o hashing ###

"""
Una Hash Table es una estructura de datos que almacena pares clave-valor.
En Python, los diccionarios (`dict`) implementan Hash Tables de manera eficiente.

✅ Características:
- Inserción, eliminación y búsqueda en **O(1)** en promedio.
- Uso de una función hash para asignar índices únicos a cada clave.
- Puede manejar colisiones con técnicas como encadenamiento o direccionamiento abierto.
"""

# Implementación de una función hash simple
# Convierte una clave en un índice dentro de la tabla

def funcion_hash(clave, tamano_tabla):
    valor_hash = 0  # Inicializa el valor hash
    for c in clave:  # Itera sobre cada caracter de la clave
        valor_hash += ord(c) - ord('a') + 1  # Convierte el caracter en un número y lo suma
    return valor_hash % tamano_tabla  # Asegura que el índice esté dentro del tamaño de la tabla

# Inicializamos la tabla hash de tamaño 7
tabla_hash = [None] * 7

# Insertamos valores en la tabla hash
strings = ["ab", "cd", "efg"]
tamano_tabla = len(tabla_hash)

for string in strings:
    indice = funcion_hash(string, tamano_tabla)  # Calcula el índice de la clave
    tabla_hash[indice] = string  # Almacena el valor en la tabla

# Imprimimos la tabla hash
for i, valor in enumerate(tabla_hash):
    print(f'Índice {i}: {valor}')

### Manejo de colisiones en Hash Tables ###
print("-------------------------")
print("\nColisiones en Hash Tables:")
print("-------------------------")
print("Encadenamiento separado o Open Hashing:")

# Implementación de una tabla hash con encadenamiento separado
class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]  # Crea listas vacías para manejar colisiones

    def funcion_hash(self, clave):
        return sum(ord(c) for c in clave) % self.tamano  # Calcula el índice de la clave

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)  # Obtiene el índice de almacenamiento
        self.tabla[indice].append((clave, valor))  # Agrega el par clave-valor a la lista

    def obtener(self, clave):
        indice = self.funcion_hash(clave)  # Obtiene el índice de búsqueda
        for k, v in self.tabla[indice]:  # Busca la clave dentro de la lista enlazada
            if k == clave:
                return v  # Retorna el valor si se encuentra la clave
        return None  # Retorna None si la clave no existe

    def eliminar(self, clave):
        indice = self.funcion_hash(clave)  # Obtiene el índice
        for i, (k, v) in enumerate(self.tabla[indice]):  # Busca la clave dentro de la lista
            if k == clave:
                del self.tabla[indice][i]  # Elimina el par clave-valor si lo encuentra
                return

# Crear la tabla hash con encadenamiento separado
hash_table = TablaHash(5)

# Insertar valores con posibles colisiones
hash_table.insertar("gato", 10)
hash_table.insertar("perro", 20)
hash_table.insertar("tigre", 30)  # Puede colisionar con otra clave

# Imprimir la tabla hash con colisiones manejadas por listas enlazadas
for i, lista in enumerate(hash_table.tabla):
    print(f'Índice {i}: {lista}')

# Obtener valores por clave
print("Valor de 'gato':", hash_table.obtener("gato"))
print("Valor de 'tigre':", hash_table.obtener("tigre"))

# Eliminar un valor de la tabla
hash_table.eliminar("gato")

print("-------------------------")
print("\nOpen addressing o Closed Hashing:")

# Implementación de una tabla hash con direccionamiento abierto (doble hashing)
class TablaHashDoble:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [None] * tamanio  # Inicializa la tabla con valores None

    def funcion_hash_primaria(self, clave):
        return sum(ord(c) for c in clave) % self.tamanio  # Primera función hash

    def funcion_hash_secundaria(self, clave):
        return 1 + (sum(ord(c) for c in clave) % (self.tamanio - 1))  # Segunda función hash

    def insertar(self, clave, valor):
        indice = self.funcion_hash_primaria(clave)  # Calcula el primer índice
        desplazamiento = self.funcion_hash_secundaria(clave)  # Calcula el desplazamiento

        # Aplica doble hashing hasta encontrar un índice vacío
        while self.tabla[indice] is not None:
            indice = (indice + desplazamiento) % self.tamanio  # Calcula el siguiente índice

        self.tabla[indice] = (clave, valor)  # Almacena la clave y el valor en la tabla

    def obtener(self, clave):
        indice = self.funcion_hash_primaria(clave)  # Calcula el primer índice
        desplazamiento = self.funcion_hash_secundaria(clave)  # Calcula el desplazamiento

        # Busca la clave en la tabla usando doble hashing
        while self.tabla[indice] is not None:
            if self.tabla[indice][0] == clave:
                return self.tabla[indice][1]  # Retorna el valor si encuentra la clave
            indice = (indice + desplazamiento) % self.tamanio  # Calcula el siguiente índice

        return None  # Retorna None si no encuentra la clave

# Crear la tabla hash con doble hashing
hash_table_doble = TablaHashDoble(7)

# Insertar valores con colisiones posibles
hash_table_doble.insertar("gato", 10)
hash_table_doble.insertar("perro", 20)  # Puede colisionar con "gato"
hash_table_doble.insertar("tigre", 30)  # Puede colisionar con "gato" y "perro"

# Imprimir la tabla hash con direccionamiento abierto
for i, valor in enumerate(hash_table_doble.tabla):
    print(f'Índice {i}: {valor}')

# Obtener valores por clave
print("Valor de 'gato':", hash_table_doble.obtener("gato"))
print("Valor de 'tigre':", hash_table_doble.obtener("tigre"))
