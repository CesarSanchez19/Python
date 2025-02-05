# Variables

my_string_variable = "My string variable"

print(my_string_variable)

my_int_variable = 19
print(my_int_variable) #Inicio con int

my_int_to_str_variable = str(my_int_variable) #Se convierte el valor a string
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) # Sera string

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print((my_string_variable, my_int_variable, my_bool_variable)) #se puede imprimir varias variables separados por coma
print("Este es el valor de: ", my_bool_variable)


# Algunas funciones del sistema
print(len(my_string_variable))  #Cuentas los caracteres de la variable

# Variables en una sola linea. !Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Cesar", "Sanchez", "Mrcisco", 20
print("Me llamo", name, surname,". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs !Solitar datos de entrada!
# name = input("¿Cual es tu nombre?: ")
# age = input("¿Cuantos años tienes?: ")
print(name, age)#

# Cambiamos su tipo
name = 20
age = "cesar"
print(name, age)

# ¿Forzamos el tipo?
address: str = "Mi direccion"
address = 32
address = True
address = 1.5
print(type(address))
print(address)