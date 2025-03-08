### Montículos, Heaps o Colas de Prioridad ###

# Un montículo (heap) es una estructura de datos que permite almacenar y recuperar datos siguiendo un orden específico.

import heapq

# ¿Qué es un Heap?
# Un heap es una estructura de árbol binario completo donde cada nodo cumple una propiedad:
# - En un Min-Heap: el valor de cada nodo es menor o igual que el de sus hijos. La raíz contiene el valor más pequeño.
# - En un Max-Heap: el valor de cada nodo es mayor o igual que el de sus hijos. La raíz contiene el valor más grande.

# Funciones principales de la librería heapq:

# heapq.heappush(heap, item) - Inserta un item en el heap, manteniendo el orden del heap.
# heapq.heappop(heap) - Extrae el valor más pequeño (para Min-Heap) del heap.
# heapq.heapify(x) - Convierte una lista en un heap en su lugar (en tiempo O(n)).
# heapq.heapreplace(heap, item) - Extrae el valor más pequeño y lo reemplaza por el nuevo item.
# heapq.heappushpop(heap, item) - Inserta el item y luego extrae el valor más pequeño del heap.
# heapq.nlargest(n, iterable, key=None) - Encuentra los n elementos más grandes de un iterable.
# heapq.nsmallest(n, iterable, key=None) - Encuentra los n elementos más pequeños de un iterable.
# heapq.merge(*iterables, key=None, reverse=False) - Fusiona varios iterables ya ordenados en uno solo.

# Crear un heap a partir de una lista
numeros = [5, 7, 9, 1, 3]  # Lista inicial de números
heapq.heapify(numeros)  # Convierte la lista en un heap (por defecto, un Min-Heap)
print("Heap después de heapify:", numeros)  # Muestra el heap resultante

# Insertar un nuevo elemento
heapq.heappush(numeros, 4)  # Inserta el valor 4 en el heap, manteniendo el orden del heap
print("Heap después de heappush(4):", numeros)  # Muestra el heap después de la inserción

# Extraer el elemento más pequeño
minimo = heapq.heappop(numeros)  # Extrae el elemento más pequeño del heap
print("Elemento mínimo extraído:", minimo)  # Muestra el valor extraído
print("Heap después de heappop:", numeros)  # Muestra el heap después de la extracción

# Usar heappushpop, agrega un elemento y luego extrae el más pequeño
resultado = heapq.heappushpop(numeros, 10)  # Inserta el valor 10 y extrae el más pequeño del heap
print("Resultado de heappushpop(10):", resultado)  # Muestra el valor extraído
print("Heap después de heappushpop:", numeros)  # Muestra el heap después de la operación

# Reemplazar el elemento más pequeño y extraerlo
reemplazo = heapq.heapreplace(numeros, 2)  # Extrae el elemento más pequeño y lo reemplaza con el valor 2
print("Resultado de heapreplace(2):", reemplazo)  # Muestra el valor extraído
print("Heap después de heapreplace:", numeros)  # Muestra el heap después de la operación

# Encontrar los 3 elementos más pequeños
elementos_pequenos = heapq.nsmallest(3, numeros)  # Devuelve los 3 elementos más pequeños del heap
print("Los 3 elementos más pequeños:", elementos_pequenos)  # Muestra los 3 elementos más pequeños

# Encontrar los 3 elementos más grandes
elementos_grandes = heapq.nlargest(3, numeros)  # Devuelve los 3 elementos más grandes del heap
print("Los 3 elementos más grandes:", elementos_grandes)  # Muestra los 3 elementos más grandes

# Fusionar varios iterables ordenados
iterable1 = [1, 3, 5]  # Primer iterable ordenado
iterable2 = [2, 4, 6]  # Segundo iterable ordenado
fusionados = list(heapq.merge(iterable1, iterable2))  # Fusiona los dos iterables en uno solo
print("Iterables fusionados:", fusionados)  # Muestra el iterable fusionado

# Crear un heap con claves personalizadas (por ejemplo, ordenando por longitud de las palabras)
palabras = ["banana", "apple", "cherry", "kiwi"]  # Lista de palabras
heapq.heapify(palabras)  # Convierte la lista de palabras en un heap
print("Heap de palabras:", palabras)  # Muestra el heap de palabras
palabras_ordenadas = heapq.nsmallest(2, palabras, key=len)  # Encuentra las dos palabras más cortas
print("Las 2 palabras más cortas:", palabras_ordenadas)  # Muestra las dos palabras más cortas

## Min-Heap

# Función para crear un Min-Heap (Heap por defecto en heapq)
def crear_min_heap(lista):
    heapq.heapify(lista)  # Convierte la lista en un Min-Heap
    return lista  # Retorna el Min-Heap creado

# Función para insertar un valor en el Min-Heap
def heappush_min(heap, item):
    heapq.heappush(heap, item)  # Inserta el valor en el Min-Heap manteniendo el orden

# Función para extraer el valor mínimo del Min-Heap
def heappop_min(heap):
    return heapq.heappop(heap)  # Extrae y retorna el valor más pequeño del Min-Heap


# Ejemplo de Min-Heap
numeros_min_heap = [5, 7, 9, 1, 3]  # Lista inicial para Min-Heap
min_heap = crear_min_heap(numeros_min_heap)  # Crea el Min-Heap
print("Min-Heap después de heapify:", min_heap)  # Muestra el Min-Heap después de crear

# Insertar un nuevo valor en el Min-Heap
heappush_min(min_heap, 2)  # Inserta el valor 2 en el Min-Heap
print("Min-Heap después de heappush(2):", min_heap)  # Muestra el Min-Heap después de insertar

# Extraer el valor mínimo del Min-Heap
minimo = heappop_min(min_heap)  # Extrae el valor más pequeño
print("Valor mínimo extraído del Min-Heap:", minimo)  # Muestra el valor extraído
print("Min-Heap después de heappop:", min_heap)  # Muestra el Min-Heap después de la extracción

## Max-Heap
# En Python, la librería heapq no proporciona una implementación directa de un Max-Heap.
# Sin embargo, se puede simular un Max-Heap utilizando valores negativos.

# Función para crear un Max-Heap simulando el comportamiento usando valores negativos
def crear_max_heap(lista):
    # Convertir la lista a un Min-Heap usando valores negativos para simular un Max-Heap
    max_heap = [-x for x in lista]  # Negamos todos los valores
    heapq.heapify(max_heap)  # Convierte la lista negada en un Min-Heap (lo que simula un Max-Heap)
    return max_heap  # Retorna el Max-Heap simulado

# Función para insertar un valor en el Max-Heap
def heappush_max(heap, item):
    heapq.heappush(heap, -item)  # Inserta el valor negativo para simular el Max-Heap

# Función para extraer el valor máximo del Max-Heap
def heappop_max(heap):
    return -heapq.heappop(heap)  # Extrae el valor negativo y lo convierte en positivo

# Ejemplo de Max-Heap
numeros_max_heap = [5, 7, 9, 1, 3]  # Lista inicial para Max-Heap
max_heap = crear_max_heap(numeros_max_heap)  # Crea el Max-Heap simulado
print("Max-Heap después de heapify:", [-x for x in max_heap])  # Muestra el Max-Heap simulado

# Insertar un nuevo valor en el Max-Heap
heappush_max(max_heap, 10)  # Inserta el valor 10 en el Max-Heap simulado
print("Max-Heap después de heappush(10):", [-x for x in max_heap])  # Muestra el Max-Heap después de insertar

# Extraer el valor máximo del Max-Heap
maximo = heappop_max(max_heap)  # Extrae el valor máximo
print("Valor máximo extraído del Max-Heap:", maximo)  # Muestra el valor extraído
print("Max-Heap después de heappop:", [-x for x in max_heap])  # Muestra el Max-Heap después de la extracción

# Encontrar los 3 elementos más grandes en un Max-Heap
elementos_grandes = heapq.nlargest(3, [-x for x in max_heap])  # Encuentra los 3 elementos más grandes
print("Los 3 elementos más grandes del Max-Heap:", elementos_grandes)  # Muestra los 3 elementos más grandes

# Encontrar los 3 elementos más pequeños en un Min-Heap
elementos_pequenos = heapq.nsmallest(3, min_heap)  # Encuentra los 3 elementos más pequeños
print("Los 3 elementos más pequeños del Min-Heap:", elementos_pequenos)  # Muestra los 3 elementos más pequeños
