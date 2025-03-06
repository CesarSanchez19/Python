# Nodo de una Lista Enlazada Simple
class Nodo:
    def __init__(self):
        self.datos = None  # Almacena el dato del nodo
        self.next = None   # Apunta al siguiente nodo

    def setDatos(self, datos):
        """Establece el valor de los datos del nodo."""
        self.datos = datos

    def getDatos(self):
        """Obtiene el valor almacenado en el nodo."""
        return self.datos

    def setNext(self, next):
        """Establece el siguiente nodo en la lista."""
        self.next = next

    def getNext(self):
        """Obtiene el siguiente nodo en la lista."""
        return self.next

class Lista:
    def __init__(self):
        self.head = None  # Apunta al primer nodo de la lista

    # Insertar en el principio de la lista
    def insInicio(self, datos):
        nuevo = Nodo()
        nuevo.setDatos(datos)
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo
        else:
            nuevo.setNext(self.head)  # El nuevo nodo apunta al antiguo primer nodo
            self.head = nuevo         # Ahora el nuevo nodo es el primer nodo

    # Insertar al final de la lista
    def insFin(self, datos):
        nuevo = Nodo()
        nuevo.setDatos(datos)
        if self.head is None:  # Si la lista está vacía
            self.head = nuevo
        else:
            actual = self.head
            while actual.getNext() is not None:  # Recorre la lista hasta el último nodo
                actual = actual.getNext()
            actual.setNext(nuevo)  # El último nodo apunta al nuevo nodo

    # Eliminar el primer nodo de la lista
    def delInicio(self):
        if self.head is None:
            print("La lista está vacía")
        else:
            self.head = self.head.getNext()  # El primer nodo ahora es el segundo nodo

    # Eliminar el último nodo de la lista
    def delFin(self):
        if self.head is None:
            print("La lista está vacía")
        else:
            actual = self.head
            if actual.getNext() is None:  # Si solo hay un nodo
                self.head = None
            else:
                while actual.getNext().getNext() is not None:  # Busca el penúltimo nodo
                    actual = actual.getNext()
                actual.setNext(None)  # El penúltimo nodo ya no apunta al último

    # Imprimir todos los elementos de la lista
    def imprimir(self):
        actual = self.head
        while actual is not None:
            print(actual.getDatos(), end=" -> ")
            actual = actual.getNext()
        print("None")

# Uso de la lista enlazada simple
lista = Lista()
lista.insInicio(10)
lista.insInicio(5)
lista.insFin(20)
lista.imprimir()  # Salida: 5 -> 10 -> 20 -> None
lista.delInicio()
lista.imprimir()  # Salida: 10 -> 20 -> None
lista.delFin()
lista.imprimir()  # Salida: 10 -> None
