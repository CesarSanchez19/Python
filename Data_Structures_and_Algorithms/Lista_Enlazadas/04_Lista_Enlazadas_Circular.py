class NodoCircular:
    def __init__(self):
        self.datos = None  # Almacena el dato
        self.next = None   # Apunta al siguiente nodo

class ListaCircular:
    def __init__(self):
        self.head = None  # Cabeza de la lista

    # Insertar al final de la lista circular
    def insFin(self, datos):
        nuevo = NodoCircular()
        nuevo.datos = datos
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo
            nuevo.next = self.head  # El nuevo nodo apunta a sí mismo
        else:
            actual = self.head
            while actual.next != self.head:  # Recorre hasta llegar al último nodo
                actual = actual.next
            actual.next = nuevo   # El último nodo apunta al nuevo nodo
            nuevo.next = self.head  # El nuevo nodo apunta al primer nodo

    # Imprimir todos los elementos de la lista circular
    def imprimir(self):
        if self.head is None:
            print("La lista está vacía")
            return
        actual = self.head
        while True:
            print(actual.datos, end=" -> ")
            actual = actual.next
            if actual == self.head:  # Si volvemos al primer nodo, terminamos
                break
        print("... (circular)")

# Uso de la lista circular
lista_circular = ListaCircular()
lista_circular.insFin(10)
lista_circular.insFin(20)
lista_circular.insFin(30)
lista_circular.imprimir()  # Salida: 10 -> 20 -> 30 -> ... (circular)
