class NodoDoble:
    def __init__(self):
        self.datos = None  # Almacena el dato
        self.next = None   # Apunta al siguiente nodo
        self.prev = None   # Apunta al nodo anterior

class ListaDoble:
    def __init__(self):
        self.head = None  # Cabeza de la lista

    # Insertar al principio de la lista
    def insInicio(self, datos):
        nuevo = NodoDoble()
        nuevo.datos = datos
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo
        else:
            nuevo.next = self.head  # El nuevo nodo apunta al antiguo primer nodo
            self.head.prev = nuevo  # El antiguo primer nodo apunta al nuevo nodo
            self.head = nuevo       # Ahora el nuevo nodo es el primer nodo

    # Insertar al final de la lista
    def insFin(self, datos):
        nuevo = NodoDoble()
        nuevo.datos = datos
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo
        else:
            actual = self.head
            while actual.next is not None:  # Recorre hasta el último nodo
                actual = actual.next
            actual.next = nuevo   # El último nodo apunta al nuevo nodo
            nuevo.prev = actual   # El nuevo nodo apunta al nodo anterior

    # Eliminar el primer nodo
    def delInicio(self):
        if self.head is None:
            print("La lista está vacía")
        else:
            self.head = self.head.next  # El primer nodo ahora es el segundo nodo
            if self.head is not None:  # Si hay un segundo nodo
                self.head.prev = None  # El segundo nodo no tiene nodo anterior

    # Eliminar el último nodo
    def delFin(self):
        if self.head is None:
            print("La lista está vacía")
        else:
            actual = self.head
            if actual.next is None:  # Si solo hay un nodo
                self.head = None
            else:
                while actual.next is not None:  # Recorre hasta el último nodo
                    actual = actual.next
                actual.prev.next = None  # El penúltimo nodo ya no apunta al último

    # Imprimir todos los elementos de la lista
    def imprimir(self):
        actual = self.head
        while actual is not None:
            print(actual.datos, end=" <-> ")
            actual = actual.next
        print("None")

# Uso de la lista doblemente enlazada
lista_doble = ListaDoble()
lista_doble.insInicio(10)
lista_doble.insFin(20)
lista_doble.insFin(30)
lista_doble.imprimir()  # Salida: 10 <-> 20 <-> 30 <-> None
lista_doble.delInicio()
lista_doble.imprimir()  # Salida: 20 <-> 30 <-> None
lista_doble.delFin()
lista_doble.imprimir()  # Salida: 20 <-> None
