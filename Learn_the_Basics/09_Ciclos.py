### Ciclos o Bucles ###

# While
"""
El bucle while en Python se utiliza para ejecutar un bloque de código repetidamente 
mientras una condición especificada sea verdadera. Se evalúa la condición antes de cada iteración.
"""

my_condition = 0  # Inicializamos la variable que se utilizará en la condición del bucle

# Comenzamos un bucle que continuará mientras my_condition sea menor que 10
while my_condition < 10:
    print(my_condition)  # Imprime el valor actual de my_condition
    my_condition += 2    # Incrementa my_condition de 2 en 2

# Este bloque else es opcional y se ejecuta si la condición del while se vuelve falsa
else:
    print("Mi condición es mayor o igual que 10")  # Indica que el bucle ha terminado al cumplir la condición

# Se terminó el bucle; el programa continúa
print('La ejecución del programa continúa')

# Otro ejemplo de bucle while
# Aquí se vuelve a utilizar my_condition, que ahora es 10, para otro bucle
while my_condition < 20:
    my_condition += 1  # Incrementa my_condition de 1 en 1
    if my_condition == 15:  # Si my_condition llega a 15, se ejecuta el siguiente bloque
        print("Se detiene la ejecución")  # Indica que el bucle se detendrá
        break  # Detiene el bucle cuando la condición se cumple
    print(my_condition)  # Imprime el valor actual de my_condition

# Se terminó el bucle; el programa continúa
print('La ejecución del programa continúa')


# For 
"""
El bucle for en Python se utiliza para iterar sobre una secuencia (como listas, tuplas, diccionarios, conjuntos o cadenas).
Permite ejecutar un bloque de código una vez por cada elemento de la secuencia.
"""

# Ejemplo de iteración sobre una lista
my_lists = [35, 24, 62, 52, 30, 30, 17]  # Definimos una lista de números

# Imprime todos los elementos que se encuentran en la lista
for element in my_lists:
    print(element)  # Imprime cada número de la lista

# Ejemplo de iteración sobre una tupla
my_tuple = (35, 1.77, "Cesar", "Sanchez", True, "Cesar")  # Tupla con diferentes tipos de datos

# Imprime todos los elementos que se encuentran en la tupla
for element in my_tuple:
    print(element)  # Imprime cada elemento de la tupla

# Ejemplo de iteración sobre un conjunto
my_set = {"Cesar", "Sanchez", 35}  # Definimos un conjunto con diferentes tipos de datos

# Imprime todos los elementos que se encuentran en el conjunto
for element in my_set:
    print(element)  # Imprime cada elemento del conjunto

# Ejemplo de iteración sobre un diccionario
my_dict = {
    "Nombre": "Cesar",
    "Apellido": "Sanchez",
    "Edad": 19,
    1: "Python"  # Se pueden usar enteros como claves
}

# Imprime todos los elementos que se encuentran en el diccionario
for element in my_dict:
    print(element)  # Imprime cada clave del diccionario
    if element == "Edad":  # Si se encuentra la clave "Edad"
        break  # Detiene el bucle
    print("Se ejecuta")  # Este mensaje se imprime si la clave no es "Edad"
else:
    print("El bucle for para diccionario ha finalizado")  # Se ejecuta si no se utiliza break

# Se terminó el bucle; el programa continúa
print('La ejecución del programa continúa')

# Otro ejemplo de iteración sobre un diccionario con continue
# Imprime todos los elementos que se encuentran en el diccionario
for element in my_dict:
    print(element)  # Imprime cada clave del diccionario
    if element == "Edad":  # Si se encuentra la clave "Edad"
        continue  # Salta el resto del código y continúa con la siguiente iteración
    print("Se ejecuta")  # Este mensaje se imprime si la clave no es "Edad"
else:
    print("El bucle for para diccionario ha finalizado")  # Se ejecuta si no se utiliza break

# Ejemplo adicional: Uso de range() con for
# El uso de range() permite crear una secuencia de números para iterar.

# 1. Iterar un número fijo de veces
print("Caso 1: Iterar un número fijo de veces")
for i in range(5):  # Se ejecuta exactamente 5 veces, con valores de 0 a 4
    print("Iteración:", i)  # Imprime el número de iteración actual

# 2. Definir un rango de inicio y fin
print("\nCaso 2: Definir un rango de inicio y fin")
for i in range(2, 6):  # Genera valores desde 2 hasta 5
    print(i)  # Imprime cada número del rango definido

# 3. Usar un paso personalizado
print("\nCaso 3: Usar un paso personalizado")
for i in range(1, 10, 2):  # Inicia en 1, incrementa de 2 en 2, hasta 9
    print(i)  # Imprime los valores impares del rango

# 4. Recorrer números en orden inverso
print("\nCaso 4: Recorrer números en orden inverso")
for i in range(10, 0, -2):  # Inicia en 10, decrementa de 2 en 2, hasta 2
    print(i)  # Imprime los valores pares en orden descendente

# 5. Iterar sobre índices de una lista
print("\nCaso 5: Iterar sobre índices de una lista")
frutas = ["Manzana", "Banana", "Cereza"]
for i in range(len(frutas)):  # Genera índices de 0 a len(frutas)-1
    print(i, frutas[i])  # Imprime el índice y el elemento correspondiente

# 6. Generar una lista de números con list()
print("\nCaso 6: Generar una lista de números con list()")
numeros = list(range(1, 6))  # Crea una lista con valores del 1 al 5
print(numeros)  # Imprime la lista generada

# 7. Iterar con enumerate()
print("\nCaso 7: Iterar con enumerate()")
for i, fruta in enumerate(frutas, start=1):  # Itera con índice desde 1
    print(i, fruta)  # Imprime el índice y el elemento correspondiente

# Simulación de un bucle do while
"""
Python no tiene un bucle do while nativo, pero podemos simularlo usando un bucle while con una condición al final.
El bloque de código se ejecutará al menos una vez antes de verificar la condición.
"""

my_condition = 0  # Inicializamos la variable

while True:  # Inicia un bucle infinito
    print("Esta es la ejecución del bucle do while. Current condition:", my_condition)
    my_condition += 1  # Incrementa my_condition
    if my_condition >= 5:  # Verifica la condición
        break  # Sale del bucle si la condición se cumple

# Se terminó el bucle; el programa continúa
print('La ejecución del programa continúa')


# Ejemplo de bucles anidados
"""
Los bucles anidados son bucles dentro de otros bucles. Se pueden usar para iterar sobre estructuras más complejas, como matrices.
"""

print("\nEjemplo de bucles anidados:")
for i in range(3):  # Bucle externo
    for j in range(2):  # Bucle interno
        print(f"Bucle externo {i}, Bucle interno {j}")  # Imprime los índices de ambos bucles

# Se terminó el bucle; el programa continúa
print('La ejecución del programa continúa')
