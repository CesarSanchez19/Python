### Lists ###

my_lists = list()
my_other_list = []

#La lista siempre comienza en la posicion "0" hasta "n" cantidad de numeros definidos

print(len(my_lists))

#Este es un verdadera lista
my_lists = [35, 24, 62, 52, 30, 30, 17]
print(my_lists)

#imprimir la longitud de nuestra lista.
print(len(my_lists))

#Puedes declara en una lista con varios tipos de datos
my_other_list = [35, 1.77, "Cesar", "Sanchez"]
print(my_other_list)
print(type(my_other_list))  #el tipo de datos es "list"
print(type(my_lists))

# Imprimir el primer elemento de una lista
print(my_other_list[0])

# Imprimir el segundo elemento de una lista
print(my_other_list[1])

# Imprimir el ultimo elemento de una lista
print(my_other_list[-1])

# Imprimir el ante penultimo elemento de una lista
print(my_other_list[-3])

# La funcion "count" se usa para saber cuantas veces se repite un elemento
print(my_lists.count(30))

# Dara un error  por que se sale el limite del rango de index definido de la lista
# print(my_other_list[-4]) IndexError

# Extraer un elemento definido en una lista dependiendo su posicion y cantidad elementos dentra en la lista
age, height, name, surname = my_other_list
print(name)

# Imprimir y definir la posicion de los elementos de una lista.
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list
print(age)

# Unir dos lista
print(my_lists + my_other_list)

# Function "append" añade un elemento al final de la lista
my_other_list.append("Galetics")
print(my_other_list)

# Funcion "insert" agrega un elemento en un lugar especifico definido por nosotros dentro de una lista.
my_other_list.insert(1, "Green")

print(my_other_list)

# Reasignamos o cambiamos el valor de un elemento de lista.
my_other_list[1] = "Rojo"
print(my_other_list)


# Funcion "Remove" elimina un elemento de la lista
my_lists.remove(30)
print(my_lists)

# Funcion "pop" elimina el ultimo elemento de la lista.
# Tambien puedes definir "indece de lista" el elemento se desea eliminar
print(my_lists.pop()) #Muestra el elemento eliminado
print(my_lists)

# Guardamos dentro de una variable elemento eliminado de la lista
my_pop_element = my_lists.pop(2)
print(my_pop_element)

# Otra forma de eliminar un elemento de una lista
del my_lists[2]
print(my_lists)

# Funcion "copy" copiamos una lista ya existente.
my_new_list = my_lists.copy()

# Funcion "Clear" limpia o borra todos los elementos de una lista.
my_lists.clear()
print(my_lists)

# Antes de borrar la lista que hemos limpiando
print(my_new_list)

# Function "Reverse" imprime arreves los elementos de una lista
my_new_list.reverse()
print(my_new_list)

# Funcion "sort" ordena los elementos conviertiendo en una lista ordenada (menor a mayor).
# Tambieen podemos definir criterios para ordenar los elementos de la lista.
my_new_list.sort()
print(my_new_list)

# Hacer una sublista (Definimos en donde comienza y cuando termina)
print(my_new_list[1:3])

# Python es un tipado dinamico, que llega cambiar los tipos de datos.
my_lists = "Hola python"
print(my_lists)
print(type(my_lists)) 