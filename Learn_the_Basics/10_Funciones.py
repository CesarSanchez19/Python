### Funciones ###

"""
En Python, una función es un bloque de código reutilizable que realiza una tarea específica.
Se define usando la palabra clave def, seguida del nombre de la función y paréntesis (), que pueden contener parámetros opcionales.
Las funciones permiten mejorar la organización del código, reutilizar lógica y facilitar el mantenimiento.
"""

# Declarar una función que imprima un texto
def my_function():
    print("Esta es una función")  # Imprime un mensaje en la consola

# Llamar la función varias veces
my_function()
my_function()
my_function()

# Definir una función que reciba dos parámetros y los sume
def sum_two_values(first_value, second_value):
    print(first_value + second_value)  # Suma los dos parámetros y los muestra en pantalla

# Llamadas a la función con diferentes tipos de datos
sum_two_values(5, 7)  # Enteros: resultado 12
sum_two_values(54234432234, 23234233427)  # Enteros grandes
sum_two_values("5", "7")  # Strings: se concatenan, resultado "57"
sum_two_values(1.4, 5.2)  # Números decimales (float)

# Función que devuelve el resultado en lugar de imprimirlo
def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value  # Retorna la suma de los valores

# Almacenar el resultado de una función en una variable
my_result = sum_two_values_with_return(10, 5)
print(my_result)  # Imprime el resultado de la función (15)
print(sum_two_values_with_return(10, 5))  # También se puede imprimir directamente

# Otra forma de hacer lo mismo usando una variable interna
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value  # Almacena la suma en una variable
    return my_sum  # Retorna el valor de la variable

# Función con parámetros nombrados (keyword arguments)
def print_name(name, surname):
    print(f"{name} {surname}")  # Imprime el nombre y apellido

print_name(surname="Sanchez", name="Cesar")  # Se pueden pasar los parámetros en cualquier orden si se nombran

# Función con un parámetro por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")  # Si no se proporciona alias, usa "Sin alias"

print_name_with_default("Cesar", "Sanchez", "Mr.Cisco")  # Se proporciona alias
print_name_with_default("Cesar", "Sanchez")  # No se proporciona alias, usa el valor por defecto

# Función con un número variable de argumentos
def print_upper_texts(*texts):  # El asterisco permite recibir múltiples argumentos
    for text in texts:
        print(text.upper())  # Convierte cada texto a mayúsculas e imprime

print_upper_texts("Hola", "Python", "Cesar")  # Imprime cada palabra en mayúsculas
print_upper_texts("Hola")  # También funciona con un solo argumento

"""
Notas importantes sobre funciones en Python:
- Se pueden definir con `def nombre_funcion():`.
- Pueden recibir parámetros opcionales o requeridos.
- `return` permite devolver valores, lo que hace que sean reutilizables en cálculos.
- Se pueden usar parámetros nombrados para mayor claridad.
- Se pueden definir valores por defecto para evitar errores si no se pasan argumentos.
- `*args` permite recibir múltiples argumentos como una tupla.
- Usar funciones mejora la legibilidad y reutilización del código.
"""

### Ejemplos de uso de funciones en situaciones comunes ###

# 1. Función para verificar si un número es par o impar
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))  # True
print(es_par(7))  # False

# 2. Función recursivas para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

# 3. Función para contar las vocales en una cadena de texto
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vocales)

print(contar_vocales("Hola Mundo"))  # 4

# 4. Función para encontrar el número mayor en una lista
def encontrar_maximo(lista):
    return max(lista)

print(encontrar_maximo([3, 7, 2, 9, 5]))  # 9

# 5. Función para invertir una cadena
def invertir_cadena(texto):
    return texto[::-1]

print(invertir_cadena("Python"))  # nohtyP
