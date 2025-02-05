### Operador Aritmeticos ###

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicacion
print(3 / 4) # Division
print(10 % 3) #Residuo de una division
print(10 // 3) #Siempre el cuentra un numero entero aproximado
print(2 ** 3) # Exponente
print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hola" + "Python" + "¿Que tal") # Concatenar varias cadenas de texto
print("Hola" + str(5)) #Concatenar una cadena de texto y un numero
print("Hola " * 5) #Imprimir varias veces un string
print("Hola " * (2 ** 3)) #Se puede hacer una operacion tan simple que resultado sea un string

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operador Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(4 == 4)
print(3 != 4)
print(3 > 4 > 2)

print("Comparar cadenas de texto")

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "Abaa") # Ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa")) # Comparar la longitud de las cadenas
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operador logicos ###

print("Comparar operardores logicos")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or ("Hola" < "Python" and 4 == 4))
print(not(3 > 4))


### Tablas de verdad 

# Tabla de verdad para los operadores lógicos AND, OR y NOT:
# +---+---+---------+---------+-------+-------+
# | A | B | A AND B | A OR B  | NOT A | NOT B |
# +---+---+---------+---------+-------+-------+
# | T | T |    T    |    T    |   F   |   F   |
# +---+---+---------+---------+-------+-------+
# | T | F |    F    |    T    |   F   |   T   |
# +---+---+---------+---------+-------+-------+
# | F | T |    F    |    T    |   T   |   F   |
# +---+---+---------+---------+-------+-------+
# | F | F |    F    |    F    |   T   |   T   |
# +---+---+---------+---------+-------+-------+
#
# Donde:
# T = True, F = False
# A y B son variables booleanas.
# A AND B es True solo si ambas A y B son True.
# A OR B es True si al menos una de las variables A o B es True.
# NOT A invierte el valor de A, y NOT B invierte el valor de B.
