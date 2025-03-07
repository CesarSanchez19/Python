### Strings ###

# Un string es una secuencia de caracteres, puedes acceder a los elementos de un string por medio de indices

my_strigns = "Mi string"
my_other_strigns = 'Mi otro string'

# Longitud de un string
print(len(my_strigns))
print(len(my_other_strigns))

# Concatenar
print(my_strigns + " " + my_other_strigns)
print(my_strigns, my_other_strigns)

# Salto de linea
my_new_line_string = "Este es un string \n con salto de linea" 
print(my_new_line_string)

# Tabulacion
my_tab_string = "\t Este es un string con tabulacion"
print(my_tab_string)

# Tabulacion y salto de linea
my_scape_string = "\t Este es un string \n escapado"
print(my_scape_string)

my_scape_string = "\\ Este es un string \\ escapado" # Anular los saltos de linea y la tabulacion
print(my_scape_string)

# Formateo de datos 

name, surname, age = "Cesar", "Trejo", 20

print("Mi nombre es Cesar Sanchez {} {} y mi edad es {}".format(name, surname, age)) #Sustituyendo datos con valores definidas dentro de las variables
print("Mi nombre es Cesar Sanchez %s %s y mi edad es %d" %(name, surname, age)) #Sustitucion correcta dentro del tipo de datos definidos "Ser estrictos con el tipo de datos"

print("Mi nombres es " + name + " " + surname + " " + " y mi edad es " + str(age)) # Manera incorrecta de utilizar cadenas de texto

# Interpolacion de datos "Formateo y infiere los datos de una variable"
print(f"Mi nombre es Cesar Sanchez {name} {surname} y mi edad es {age}")

# Desempaquedo de caracteres
language = "python"
a, b , c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3]
print(language_slice)

# Imprime las letras desde el indice 1
language_slice = language[1:]
print(language_slice)

# Imprime la penultima letra de "O" de "Pyhton"
language_slice = language[-2]
print(language_slice)

# Imprime un rango "0 a hasta 6" de caracteres de cadena que cuente de dos a dos "2".
language_slice = language[0:6:2]
print(language_slice)

# Reverse

#Imprime la forma reversiva el caractere de una palabra
reversed_languaje = language[ ::-1]
print(reversed_languaje)

# Funciones

# Imprime la primer caracter en Mayuscula con el resto de caracteres que lo acompaña
print(language.capitalize())

#Imprime todos los caracteres en Mayuscula
print(language.upper())

#Imprime cuantas veces se encuentra el caracter dentro de una cadena de texto
print(language.count("t"))

# Imprime un valor booleano si la cadena de texto es numero
print(language.isnumeric())
print("1".isnumeric())

#Imprime toda la cadena de texto en minuscula 
print(language.lower())

#Puedes combinar dos funciones de las misma variable
print(language.upper().isupper())# Primero transforma en mayuscula y luego verifica si esta en mayuscula toda la cadena de texto

#Imprime si la cadena de texto comienza con cierta letra o palabra, regresara un valor booleano
print(language.startswith("py"))

#Tambien puedes imprimir un parrado de texto declarando tres comillas simples o dobles
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

# Los strings son arreglos de caracteres, por lo que podemos acceder a ellos por medio de indices
#Imprime el caracter de la posicion 1
a = "Hello, World!"
print(a[1]) # e

# Imprime el caractar separado uno por uno usando un ciclo "for" de manera vertical
for x in "banana":
  print(x)
  
# funcion "swapcase" intercambia los caracteres de mayusculas a minusculas y viceversa
s = "mI cAdEnA" 
print(s.swapcase()) #Mi CaDeNa

# funcion "isalnum" verifica si la cadena de texto es alfanumerica
s = "correo@dominio.com" # False
print(s.isalnum())

# funcion "isalpha" verifica si la cadena de texto es alfabetica
s = "abcdefg" # True
print(s.isalpha())

# Funcion "split" separa la cadena de texto en una lista

s = "Python,Java,C"
print(s.split(",")) #['Python', 'Java', 'C']  # Separa la cadena de texto por comas

# Funcion "strip" elimina los espacios en blanco al inicio y al final de la cadena de texto
s = "  abc  "
print(s.strip()) #abc # Elimina los espacios en blanco