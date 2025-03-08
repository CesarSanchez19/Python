### Colas (Queues) ###

# Una cola es una estructura de datos que permite almacenar y recuperar datos siguiendo un orden FIFO (First In First Out).
print("\nImplementación de una cola utilizando una lista o arreglo:")
cola = []  # Inicializa una cola vacía

# Agregar elementos al final de la cola
cola.append(1)
print(f"\nAgregando elemento a la cola: {cola}")
cola.append(2)
print(f"\nAgregando elemento a la cola: {cola}")
cola.append(3)
print(f"\nAgregando elemento a la cola: {cola}")
cola.append(4)
print(f"\nAgregando elemento a la cola: {cola}")
cola.append(5)

print(f"\nCola actual: {cola}")  # [1, 2, 3, 4, 5]

# Eliminar los primeros elementos agregados a la cola
elemento = cola.pop(0)
print(f"Eliminando elemento de la cola: {elemento}")
print(f"\nCola actual: {cola}")  # [2, 3, 4, 5]
elemento = cola.pop(0)
print(f"Eliminando elemento de la cola: {elemento}")
print(f"\nCola actual: {cola}")  # [3, 4, 5]

# Implementación de una cola utilizando una libreria de Python llamada deque
print("\nImplementación de una cola utilizando una libreria de Python llamada deque:")
from collections import deque

cola = deque()  # Inicializa una cola vacía

# Agregar elementos al final de la cola
cola.append("cesar")
print(f"\nAgregando elemento a la cola: {cola}")
cola.append("jose")
print(f"\nAgregando elemento a la cola: {cola}")
cola.append("luis")
print(f"\nAgregando elemento a la cola: {cola}")
cola.append("juan")
print(f"\nAgregando elemento a la cola: {cola}")
cola.append("pedro")

print(f"\nCola actual: {cola}")  # ['cesar', 'jose', 'luis', 'juan', 'pedro']

# Eliminar los primeros elementos agregados a la cola
elemento = cola.popleft()
print(f"Eliminando elemento de la cola: {elemento}")
print(f"\nCola actual: {cola}")  # ['jose', 'luis', 'juan', 'pedro']
elemento = cola.popleft()
print(f"Eliminando elemento de la cola: {elemento}")
print(f"\nCola actual: {cola}")  # ['luis', 'juan', 'pedro']

# Implementación de una cola utilizando una lista enlazada
print("\nImplementación de una cola utilizando una lista enlazada:")
class Nodo:
    def __init__(self, objeto, siguiente=None):
        self.objeto = objeto
        self.siguiente = siguiente

class Cola:
    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None

    def encolar(self, objeto):
        nuevo_nodo = Nodo(objeto)

        if self.ultimo_nodo is None:
            self.primer_nodo = nuevo_nodo
        else:
            self.ultimo_nodo.siguiente = nuevo_nodo
        
        self.ultimo_nodo = nuevo_nodo

    def desencolar(self):
        if self.primer_nodo is None:
            return None  # Retorna None si la cola está vacía
        
        objeto = self.primer_nodo.objeto
        self.primer_nodo = self.primer_nodo.siguiente

        if self.primer_nodo is None:
            self.ultimo_nodo = None  # Si la cola queda vacía, actualizar `ultimo_nodo`

        return objeto


# Uso de la Cola
cola = Cola()

# Encolando elementos
cola.encolar("A")
cola.encolar("B")
cola.encolar("C")

# Desencolando elementos
print(cola.desencolar())  # Output: "A"
print(cola.desencolar())  # Output: "B"
print(cola.desencolar())  # Output: "C"
print(cola.desencolar())  # Output: None (cola vacía)
