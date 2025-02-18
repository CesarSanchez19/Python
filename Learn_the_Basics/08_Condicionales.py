### Condicionales en Python ###

'''
Los condicionales en Python son estructuras de control que permiten ejecutar 
diferentes bloques de código dependiendo de si una condición es verdadera o falsa. 
Se basan en la declaración if, junto con elif y else.
'''

# Definimos una variable booleana
my_condition = True  

# Un condicional simple con if
if my_condition:  # Equivalente a if my_condition == True
    print('Se ejecuta la condición del primer if')  # Se ejecuta si my_condition es True

print('La ejecución del programa continúa')  # Siempre se ejecuta, ya que está fuera del if

# Asignamos un valor a la variable
my_condition = 5 * 3  # my_condition ahora vale 15

# Condicional con comparación
if my_condition == 10:  # Usamos operadores de comparación
    print('Se ejecuta la condición del segundo if')  # No se ejecuta porque 15 no es igual a 10

print('La ejecución del programa continúa')

# Uso de if-else
if my_condition > 10:  # Comparamos si el valor es mayor que 10
    print('Es mayor que 10')
else:  # Se ejecuta si la condición anterior es falsa
    print('Es menor o igual a 10')

print('La ejecución del programa continúa')

# Uso de operadores lógicos (AND)
if my_condition > 10 and my_condition < 20:  
    # Ambas condiciones deben cumplirse (mayor que 10 y menor que 20)
    print('Es mayor que 10 y menor que 20')
else:  
    print('Es menor o igual a 10 o mayor o igual que 20')

print('La ejecución del programa continúa')

# Uso de if-elif-else (múltiples condiciones)
if my_condition > 10 and my_condition < 20:  
    print('Es mayor que 10 y menor que 20')
elif my_condition == 25:  
    # Se evalúa solo si la condición anterior es falsa
    print('Es igual a 25')
else:  
    # Se ejecuta si ninguna de las condiciones anteriores se cumple
    print('Es menor o igual a 10 o mayor o igual que 20')

print('La ejecución del programa continúa')

# Uso de la negación con "not"
my_string = " "  # Una cadena con un espacio no se considera vacía en Python

if not my_string:  # "not" invierte el valor de la condición
    print('Mi cadena de texto está vacía')  # No se ejecuta, porque la cadena tiene un espacio

if my_string == 'Mi cadena de texto':  
    # Comparamos el contenido de la cadena
    print('Estas cadenas de texto coinciden')  # No se ejecuta porque el contenido es diferente
