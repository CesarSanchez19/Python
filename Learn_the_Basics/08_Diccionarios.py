### Diccionarios en Python ###

"""
En Python, un diccionario es una estructura de datos que almacena pares de clave-valor.
Permite acceder a los valores a través de claves únicas en lugar de índices numéricos, 
como en las listas o tuplas.
"""

# Creación de diccionarios vacíos
my_dict = dict()  # Usando la función dict()
my_other_dict = {}  # Usando llaves {}

print(type(my_dict))       # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

# Creación de un diccionario con valores
my_other_dict = {
    "Nombre": "Cesar",
    "Apellido": "Sanchez",
    "Edad": 19,
    1: "Python"  # Se pueden usar enteros como claves
}

# Los diccionarios funcionan con relación (clave - valor)
# Son útiles para representar estructuras similares a objetos JSON.

# Diccionario con diferentes tipos de valores
my_dict = {
    "Nombre": "Cesar",
    "Apellido": "Sanchez",
    "Edad": 19,
    "Lenguajes": {"Python", "Java", "JavaScript"},  # Un conjunto como valor
    1: 1.78  # Un número entero como clave con un float como valor
}

print(my_other_dict)
print(my_dict)

# Obtener la cantidad de elementos (claves) en un diccionario
print(len(my_other_dict))  # 4
print(len(my_dict))        # 5

# Acceder a valores mediante sus claves
print(my_dict["Apellido"])  # Sanchez

# Modificar el valor de una clave existente
my_dict["Apellido"] = "Trejo"
print(my_dict["Apellido"])  # Trejo

# Acceder a un valor con una clave de tipo int
print(my_dict[1])  # 1.78

# Agregar una nueva clave con su valor al diccionario
my_dict["Direccion"] = "Calle Plumbago"
print(my_dict)

# Eliminar un elemento del diccionario usando 'del'
del my_dict["Direccion"]
print(my_dict)

# Comprobar si una clave existe en el diccionario
print("Nombre" in my_dict)  # True
print("Cesar" in my_dict)   # False (porque "Cesar" es un valor, no una clave)

# Obtener solo las claves del diccionario
print(my_dict.keys())

# Obtener los elementos del diccionario como pares clave-valor
print(my_dict.items())

# Obtener solo los valores del diccionario
print(my_dict.values())

# Copiar un diccionario
my_dict_copy = my_dict.copy()
print(my_dict_copy)

# Obtener un valor de forma segura con 'get()' (evita errores si la clave no existe)
print(my_dict.get("Edad"))  # 19
print(my_dict.get("Altura", "No especificado"))  # "No especificado"

# Eliminar un elemento y devolver su valor con 'pop()'
altura = my_dict.pop(1)  # Elimina la clave 1 y devuelve su valor
print(altura)  # 1.78
print(my_dict)

# Eliminar y devolver el último elemento insertado con 'popitem()'
ultima_clave, ultimo_valor = my_dict.popitem()
print(ultima_clave, ":", ultimo_valor)  # Muestra la última clave y su valor
print(my_dict)

# Crear un diccionario a partir de una lista de claves con valores None
my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)  # Todas las claves tendrán None como valor
print(my_new_dict)

# Crear un diccionario a partir de claves de otro diccionario con 'fromkeys()'
my_new_dict = dict.fromkeys(my_dict, "Valor Predeterminado")  # Todos los valores serán "Valor Predeterminado"
print(my_new_dict)

# Ver valores como un objeto 'dict_values' y convertirlos a diferentes estructuras
my_values = my_new_dict.values()
print(type(my_values))  # <class 'dict_values'>
print(list(my_values))  # Convertir a lista
print(tuple(my_values)) # Convertir a tupla
print(set(my_values))   # Convertir a conjunto

# Establecer un valor predeterminado si una clave no existe con 'setdefault()'
valor = my_dict.setdefault("Altura", 1.75)  # Si "Altura" no existe, la agrega con el valor 1.75
print(my_dict)

# Borra todo el diccionario
print(my_dict.clear())