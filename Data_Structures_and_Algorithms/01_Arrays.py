### Arreglos en Python ###

# En Python, los arreglos se representan comúnmente usando listas.
# Son estructuras de datos dinámicas y pueden contener elementos de diferentes tipos.

# Definir una lista (array unidimensional)
numeros = [10, 20, 30, 40, 50]
print("Lista original:", numeros)

# Acceder a elementos individuales de la lista
print("Primer elemento:", numeros[0])  # Accede al primer elemento
print("Último elemento:", numeros[-1])  # Accede al último elemento usando índice negativo

# Modificar elementos de la lista
numeros[2] = 99  # Cambia el tercer elemento (índice 2)
print("Lista después de modificar el tercer elemento:", numeros)

# Agregar elementos a la lista
numeros.append(60)  # Agrega 60 al final de la lista
numeros.insert(2, 25)  # Inserta 25 en la posición 2
print("Lista después de agregar elementos:", numeros)

# Eliminar elementos de la lista
numeros.remove(40)  # Elimina el número 40 si existe
eliminado = numeros.pop(1)  # Elimina el segundo elemento y lo devuelve
print(f"Elemento eliminado: {eliminado}")
print("Lista después de eliminar elementos:", numeros)

# Recorrer la lista con un bucle for
print("Elementos de la lista:")
for num in numeros:
    print(num)

# Obtener la longitud de la lista
print("Tamaño de la lista:", len(numeros))

### Matrices (Listas Bidimensionales) ###

# Definir una matriz (lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz completa:", matriz)

# Acceder a elementos específicos de la matriz
print("Primer elemento de la matriz:", matriz[0][0])  # Elemento en la primera fila y columna
print("Último elemento de la matriz:", matriz[-1][-1])  # Último elemento de la última fila

# Recorrer la matriz con bucles anidados
print("Elementos de la matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

# Generar una matriz con los cuadrados de sus elementos
cuadrados = [[x**2 for x in fila] for fila in matriz]
print("Matriz de cuadrados:", cuadrados)

### Modificar Matrices ###

# Modificar un elemento específico de la matriz
matriz[0][0] = 10  # Cambiar el primer elemento de la primera fila
print("Matriz modificada:", matriz)

# Insertar una fila en una posición específica
matriz.insert(1, [10, 11, 12])  # Insertar en la segunda posición
print("Matriz después de insertar fila:", matriz)

# Agregar una columna a cada fila de la matriz
for i in range(len(matriz)):
    matriz[i].append(i + 100)  # Agrega un valor basado en el índice
print("Matriz después de agregar columna:", matriz)

# Eliminar una fila completa de la matriz
print("Matriz antes de eliminar fila:", matriz)
del matriz[1]  # Elimina la segunda fila
print("Matriz después de eliminar fila:", matriz)

### Operaciones con Listas ###

# Copiar una lista
lista_copia = numeros.copy()
print("Copia de la lista:", lista_copia)

# Contar ocurrencias de un elemento en una lista
print("Número de veces que aparece 10 en la lista:", numeros.count(10))

# Extender una lista con otra
nueva_lista = [70, 80, 90]
numeros.extend(nueva_lista)
print("Lista después de extenderla:", numeros)

# Encontrar el índice de un elemento
if 30 in numeros:
    print("Índice del número 30 en la lista:", numeros.index(30))
else:
    print("El número 30 no está en la lista")

# Eliminar un elemento por índice
if len(numeros) > 2:
    numeros.pop(2)  # Elimina el tercer elemento
print("Lista después de eliminar por índice:", numeros)

### Uso de NumPy para Operaciones Avanzadas ###

# Importar la biblioteca NumPy para trabajar con arreglos multidimensionales
import numpy as np

# Crear una matriz con NumPy
matriz_np = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Matriz con NumPy:", matriz_np)

# Calcular la inversa de la matriz si es cuadrada
if matriz_np.shape[0] == matriz_np.shape[1]:
    inversa = np.linalg.inv(matriz_np)
    print("Matriz inversa:", inversa)
else:
    print("La matriz no es cuadrada, no se puede calcular la inversa")

# Calcular la transpuesta de la matriz
transpuesta = np.transpose(matriz_np)
print("Matriz transpuesta:", transpuesta)

# Calcular la suma de los elementos de la matriz
suma_total = np.sum(matriz_np)
print("Suma total de los elementos de la matriz:", suma_total)

# Más sobre NumPy en: https://numpy.org/doc/
