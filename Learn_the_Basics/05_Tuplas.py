### Tuplas ###

# Una tupla es una estructura de datos en Python que permite almacenar una colección ordenada e inmutable de elementos. 

my_tuple = tuple() # Este es un constructor de tuplas
my_other_tuple = ()

my_tuple = (35, 1.77, "Cesar", "Sanchez" , True, "Cesar") # Tupla con diferentes tipos de datos
my_other_tuple = (60,30,40,40) # Tupla con numeros enteros

print(my_tuple)
print(type(my_tuple)) # <class 'tuple'>

print(my_tuple[0]) # imprime el primer elemento de la tupla
print(my_tuple[-1]) # imprime el ultimo elemento de la tupla
# print(my_tuple[5]) # IndexError: tuple index out of range.
# print(my_tuple[6]) # IndexError: tuple index out of range.

## Operaciones con tuplas	

print(my_tuple.count("Cesar")) # Cuenta cuantas veces se repite un elemento en una tupla.

print(my_tuple.index("Cesar")) # Devuelve el indice (posicion que se encuentra elemento comenzando 0 hasta n cantidad) de un elemento en una tupla.

# my_tuple[1] = 1.80  TypeError: 'tuple' object does not support item assignment. Las tuplas son inmutables.

my_sum_tuple = my_tuple + my_other_tuple # Union de tuplas
print(my_sum_tuple)

print(my_sum_tuple[2 : 5]) # Imprime los elementos de la posicion 2 a la 4 de la tupla.

print(35 in my_sum_tuple) # Devuelve True si el elemento se encuentra en la tupla, de lo contrario False.

## Tupla mutable (se convertir  en lista )

my_tuple = list(my_tuple) # Convertir una tupla en una lista

print(type(my_tuple)) # <class 'list'>

my_tuple[4] = "Cesar" # Modificar un elemento de una lista

my_tuple.insert(1, "Green") # Agregar un elemento en una posicion especifica de una lista

print(my_tuple)

print(type(my_tuple)) # <class 'list'>

my_tuple = tuple(my_tuple) # Convertir una lista en una tupla

print(my_tuple)

print(type(my_tuple)) # <class 'tuple'>

"""
del my_tuple[4] # TypeError: 'tuple' object doesn't support item deletion. Las tuplas son inmutables.

del my_tuple # Eliminar una tupla
print(my_tuple) # NameError: name 'my_tuple' is not defined
"""

