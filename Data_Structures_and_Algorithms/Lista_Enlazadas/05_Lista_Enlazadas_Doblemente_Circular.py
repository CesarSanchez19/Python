class NodoDobleCircular:
    def __init__(self):
        self.datos = None  # Almacena el dato
        self.next = None   # Apunta al siguiente nodo
        self.prev = None   # Apunta al nodo anterior

class ListaDobleCircular:
    def __init__(self):
        self.head = None  # Cabeza de la lista

    # Insertar al final de la lista doblemente circular
    def insFin(self, datos):
        nuevo = NodoDobleCircular()
        nuevo.datos = datos
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo
            nuevo.next = nuevo  # El nodo apunta a sí mismo
            nuevo.prev = nuevo  # El nodo apunta a sí mismo en la dirección contraria
        else:
            ultimo = self.head.prev
            ultimo.next = nuevo
            nuevo.prev = ultimo
            nuevo.next = self.head
            self.head.prev = nuevo

    # Imprimir todos los elementos de la lista doblemente circular
    def imprimir(self):
        if self.head is None:
            print("La lista está vacía")
            return
        actual = self.head
        while True:
            print(actual.datos, end=" <-> ")
            actual = actual.next
            if actual == self.head:  # Si volvemos al primer nodo, terminamos
                break
        print("... (doblemente circular)")

# Uso de la lista doblemente circular
lista_doble_circular = ListaDobleCircular()
lista_doble_circular.insFin(10)
lista_doble_circular.insFin(20)
lista_doble_circular.insFin(30)
lista_doble_circular.imprimir()  # Salida: 10 <-> 20 <-> 30 <-> ... (doblemente circular)
