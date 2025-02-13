### Sets en Python ###

"""
En Python, un set (conjunto) es una colección **desordenada** de elementos **únicos**.
Se utiliza para almacenar múltiples valores sin duplicados y permite realizar operaciones 
como unión, intersección y diferencia.
"""

# Creación de un set vacío
my_set = set()  # Se usa el constructor set() para definir un conjunto vacío
my_other_set = {}  # Esto NO es un set, sino un diccionario vacío

# Imprimir el tipo de dato
print(type(my_set))  # <class 'set'>
print(type(my_other_set))  # <class 'dict'> (porque {} crea un diccionario)

# Definir un set con elementos iniciales
my_other_set = {"Cesar", "Sanchez", 35}  # Un set puede contener diferentes tipos de datos
print(type(my_other_set))  # Ahora es un <class 'set'>

print(len(my_other_set))  # Imprime la cantidad de elementos en el set (3 en este caso)

## Operaciones con sets ##

# Agregar un elemento al set
my_other_set.add("Galetics")  # Se añade un nuevo elemento
print(my_other_set)  # El orden puede variar, ya que los sets son desordenados

# Intentar agregar un elemento duplicado
my_other_set.add("Galetics")  # No se permite duplicados, el set sigue igual
print(my_other_set)  # {'Cesar', 'Sanchez', 35, 'Galetics'}

# Verificar si un elemento está en el set
print("Cesar" in my_other_set)  # True, el elemento está en el set
print("Cesarin" in my_other_set)  # False, no está presente

# Eliminar un elemento del set
my_other_set.remove("Sanchez")  # Elimina el elemento si existe
print(my_other_set)  # Imprime el set sin "Sanchez"

# Vaciar un set (elimina todos sus elementos)
my_other_set.clear()
print(my_other_set)  # set() (un conjunto vacío)
print(len(my_other_set))  # 0 elementos

# Eliminar el set por completo (borrar la variable del sistema)
del my_other_set
# print(my_other_set)  # Esto generaría un NameError porque la variable ya no existe

# Convertir un set en una lista
my_set = {"Cesar", "Sanchez", 35}  # Definir un set
my_list = list(my_set)  # Convertir el set en una lista
print(my_list)  # Imprime la lista con los mismos elementos del set
print(my_list[0])  # Ahora sí podemos acceder por índice

# Creación de otro set
my_other_set = {"Java", "Python", "JavaScript"}

# Unión de dos sets
my_new_set = my_set.union(my_other_set)  # Combina ambos conjuntos sin duplicados
print(my_new_set)

# Intentar unir el set consigo mismo (el resultado será el mismo)
print(my_new_set.union(my_new_set).union(my_set))

# Unir y agregar nuevos elementos temporalmente
print(my_new_set.union({"Arduino", "HTML"}))
# Nota: No se almacenan los nuevos elementos, solo se imprimen

# Diferencia entre dos conjuntos (elementos en `my_new_set` que no están en `my_set`)
print(my_new_set.difference(my_set))  # Muestra los elementos exclusivos de `my_other_set`


### Teoría de Conjuntos en Python ###

# Definición de dos conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {5, 2, 6, 7, 8}

# Unión de conjuntos (combina ambos sin duplicar elementos)
union_conjuntos = conjunto_a.union(conjunto_b)
print(union_conjuntos)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(conjunto_a | conjunto_b) # Otra forma de union de dos conjuntos

# Intersección de conjuntos (elementos en común)
interseccion_conjuntos = conjunto_a.intersection(conjunto_b)
print(interseccion_conjuntos)  # {2}
print(conjunto_a & conjunto_b) # Otra forma de intersecciondos de dos conjuntos

# Diferencia de conjuntos (elementos en A que no están en B)
diferencia_conjuntos = conjunto_a.difference(conjunto_b)
print(diferencia_conjuntos)  # {1, 3, 4}
print(conjunto_a - conjunto_b) # Otra forma de diferencia de dos conjuntos

# Diferencia simétrica (elementos que están en A o en B, pero no en ambos)
diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferencia_simetrica)  # {1, 3, 4, 5, 6, 7, 8}
print(conjunto_a ^ conjunto_b) # Otra forma de Diferencia simétrica de dos conjuntos

## Otros métodos de conjuntos ##

# Verifica si conjunto_a es un superconjunto de conjunto_b (si contiene todos sus elementos)
es_superconjunto = conjunto_a.issuperset(conjunto_b)
print(es_superconjunto)  # False

# Verifica si los conjuntos son disjuntos (sin elementos en común)
es_disjunto = conjunto_a.isdisjoint(conjunto_b)
print(es_disjunto)  # False, porque el 2 está en ambos

# Descartar un elemento del conjunto (si existe, lo elimina; si no, no genera error)
conjunto_b.discard(2)
print(conjunto_b)  # {5, 6, 7, 8}

# Verifica si conjunto_a es un subconjunto de conjunto_b (si todos sus elementos están en B)
es_subconjunto = conjunto_a.issubset(conjunto_b)
print(es_subconjunto)  # False, conjunto_a no está completamente contenido en conjunto_b

# Agrega un nuevo elemento al conjunto
conjunto_a.add(9)
print(conjunto_a)  # {1, 2, 3, 4, 9}

# Copia el conjunto en una nueva variable
copia_conjunto_a = conjunto_a.copy()
print(copia_conjunto_a)  # {1, 2, 3, 4, 9}

# Actualiza conjunto_a con la intersección (modifica el conjunto original)
conjunto_a.intersection_update(conjunto_b)
print(conjunto_a)  # set() (porque no hay elementos en común después de `discard(2)`)

# Actualiza conjunto_a con la diferencia simétrica de conjunto_b
conjunto_a.symmetric_difference_update(conjunto_b)
print(conjunto_a)  # {8, 5, 6, 7}

# Extrae y elimina un elemento aleatorio del conjunto
elemento_eliminado = conjunto_a.pop()  # `pop()` elimina un elemento aleatorio
print(elemento_eliminado)  # Puede ser cualquier elemento del conjunto
print(conjunto_a)  # El conjunto sin el elemento eliminado

# Elimina un elemento específico (si no existe, genera un error)
conjunto_b.remove(5)
print(conjunto_b)  # {6, 7, 8}
