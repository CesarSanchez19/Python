### Pila o Stacks ###

"""
Las operaciones se realizan siguiendo el principio LIFO (Last In, First Out),
lo que significa que el último elemento agregado será el primero en ser eliminado.
Una pila puede implementarse utilizando un arreglo (array) o una lista enlazada.
Si la pila se queda sin memoria, esto se conoce como desbordamiento de pila (stack overflow).
"""

# Implementación de una pila utilizando una lista o arreglo
print("Implementación de una pila utilizando una lista o arreglo:")

pila = []  # Inicializa una pila vacía

# Agregar elementos al final de la pila
pila.append(1)
print(f"agregando elemento a la pila: {pila}")  
pila.append(2)
print(f"agregando elemento a la pila: {pila}") 
pila.append(3)
print(f"agregando elemento a la pila: {pila}")  
pila.append(4)
print(f"agregando elemento a la pila: {pila}")  
pila.append(5)
print(f"agregando elemento a la pila: {pila}")

print(f"Pila actual: {pila}")  # [1, 2, 3 , 4, 5]

# Eliminar los ultimos elemento agregados a la pila
elemento = pila.pop()
print(f"Eliminando elemento de la pila: {elemento}")
print(f"Pila actual: {pila}")  # [1, 2, 3, 4]
print(f"Eliminando elemento de la pila: {elemento}")
print(f"Pila actual: {pila}")  # [1, 2, 3]

# Implementación de una pila utilizando una lista
print("Implementación de una pila utilizando una lista o arreglo:")

class Nodo:
    def __init__(self, objeto, siguiente=None):
        self.objeto = objeto
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None

    def esta_vacia(self):
        return self.cima is None

    def apilar(self, objeto):
        nuevo_nodo = Nodo(objeto, self.cima)
        self.cima = nuevo_nodo

    def desapilar(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        objeto = self.cima.objeto
        self.cima = self.cima.siguiente
        return objeto

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.cima.objeto

    def imprimir(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return
        actual = self.cima
        while actual:
            print(actual.objeto, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
pila = Pila()

# Apilamos elementos
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)

# Mostramos la pila
print("Pila después de apilar elementos:")
pila.imprimir()

# Ver el elemento en la cima
print(f"Elemento en la cima: {pila.ver_tope()}")

# Desapilamos un elemento
print(f"Elemento desapilado: {pila.desapilar()}")

# Mostramos la pila después de desapilar
print("Pila después de desapilar un elemento:")
pila.imprimir()

# Desbordamiento de pila (stack overflow)

"""
generalmente ocurre cuando una estructura de pila (o cualquier tipo de recursión)
intenta utilizar más memoria de la que el sistema puede asignar para las operaciones.
"""

# Función recursiva que causa un desbordamiento de pila

"""
def funcion_recursiva():
    return funcion_recursiva()  # Llamada recursiva infinita

funcion_recursiva()  # Esto causará un desbordamiento de pila

"""

# Lista enlazada que causa un desbordamiento de pila

class Nodo:
    def __init__(self, objeto, siguiente=None):
        self.objeto = objeto
        self.siguiente = siguiente  # Referencia al siguiente nodo

class Pila:
    def __init__(self, limite):
        self.cima = None  # La cima de la pila es inicialmente None (vacía)
        self.limite = limite  # Límite de elementos en la pila
        self.tamaño = 0  # Tamaño actual de la pila

    def esta_vacia(self):
        return self.cima is None  # Si la cima es None, la pila está vacía

    def apilar(self, objeto):
        if self.tamaño >= self.limite:
            print("Error: La pila ha alcanzado su límite (desbordamiento de pila).")
            return
        
        nuevo_nodo = Nodo(objeto, self.cima)  # Crear un nuevo nodo con el objeto
        self.cima = nuevo_nodo  # El tope ahora es el nuevo nodo
        self.tamaño += 1  # Incrementamos el tamaño

    def desapilar(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        objeto = self.cima.objeto  # Obtener el objeto de la cima
        self.cima = self.cima.siguiente  # La nueva cima es el siguiente nodo
        self.tamaño -= 1  # Decrementamos el tamaño
        return objeto

    def ver_tope(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        return self.cima.objeto  # Retorna el objeto del tope

    def imprimir(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return
        actual = self.cima
        while actual:
            print(actual.objeto, end=" -> ")
            actual = actual.siguiente
        print("None")  # Indicar el final de la pila

# Ejemplo de uso
pila = Pila(limite=3)

# Apilamos elementos
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)

# Intentamos apilar un elemento más allá del límite
pila.apilar(40)  # Salida: Error: La pila ha alcanzado su límite.

# Imprimimos la pila
pila.imprimir()  # Salida: 30 -> 20 -> 10 -> None



