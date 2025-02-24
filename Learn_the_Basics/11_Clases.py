### Clases ###

"""
En Python, una clase es una estructura que permite agrupar datos y funciones que operan sobre esos datos. Se utiliza para crear objetos, que son instancias de la clase. 
Las clases son un pilar fundamental de la programación orientada a objetos (POO), y permiten organizar el código de manera más efectiva y reutilizable.
"""

# Definición de una clase vacía llamada MyEmptyPerson
class MyEmptyPerson:
    pass  # 'pass' es una declaración que no hace nada; se usa aquí porque no hay contenido en la clase

# Imprime la clase MyEmptyPerson, mostrando su referencia en memoria
print(MyEmptyPerson)

# Crea una instancia de la clase MyEmptyPerson y la imprime
print(MyEmptyPerson())  # Esto muestra que hemos creado un objeto de MyEmptyPerson

# CLase con un objeto (Persona) 
class Person:
    # El constructor __init__ se ejecuta al crear una nueva instancia de la clase
    # 'self' se refiere a la instancia de la clase que estamos creando
    def __init__(self, name, surname):  # El constructor toma dos parámetros: name y surname
        self.name = name  # Asigna el parámetro 'name' a la propiedad 'name' de la instancia
        self.surname = surname  # Asigna el parámetro 'surname' a la propiedad 'surname' de la instancia

# Crea una instancia de la clase Person con el nombre "Cesar" y el apellido "Sanchez"
my_person = Person("Cesar", "Sanchez")

# Imprime el nombre completo de la persona creada
print(f"El nombre completo de la persona es {my_person.name} {my_person.surname}")


# También podemos definir las propiedades dentro de la clase sin parámetros en el constructor
class Person:
    def __init__(self):
        self.name = "Cesar"  # Asigna el valor "Cesar" a la propiedad 'name'
        self.surname = "Sanchez"  # Asigna el valor "Sanchez" a la propiedad 'surname'

# Crea una nueva instancia de la clase Person
my_person = Person()

# Imprime el nombre completo de la persona con valores predeterminados
print(f"El nombre completo de la persona es {my_person.name} {my_person.surname}")

# Otra forma de usarlo:
class Person:
    def __init__(self, name, surname):
        # Creamos una propiedad que almacena el nombre completo al instante de la creación
        self.fullname = f"El nombre completo de la persona es {name} {surname}"

    # Definimos un método llamado 'walk' que representa una acción que puede realizar el objeto
    def walk(self):  # 'self' se usa para acceder a las propiedades de la instancia
        print(f"{self.fullname} está caminando")  # Imprime un mensaje indicando que la persona está caminando

# Crea una instancia de la clase Person con nombre y apellido
my_person = Person("Cesar", "Sanchez")

# Imprime el nombre completo usando la propiedad 'fullname'
print(my_person.fullname)

# Llama al método 'walk' de la instancia para que imprima el mensaje
my_person.walk()

# Clase Person con un valor por defecto para el alias
class Person:
    def __init__(self, name, surname, alias="Sin alias"):  # 'alias' tiene un valor por defecto
        # Almacena el nombre completo con el alias (si se proporciona)
        self.fullname = f"El nombre completo de la persona es {name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada; no puede ser accedida directamente fuera de la clase
    
    # Método para obtener el valor de la propiedad privada 'name'
    def get_name(self):
        return self.__name  # Retorna el valor de 'name'
    
    def walk(self):  # Método para que la persona camine
        print(f"{self.fullname} está caminando")

# Crea una instancia de Person con nombre, apellido y alias
my_other_person = Person("Cesar", "Sanchez", "MrCisco")

# Imprime el nombre completo de la persona
print(my_other_person.fullname)

# Llama al método get_name para obtener el nombre privado
print(my_other_person.get_name())

# Llama al método 'walk' para que la persona camine
my_other_person.walk()

# Puedes reasignar el valor de la propiedad 'fullname' dentro del objeto
my_other_person.fullname = "David Trejo (Toreto)" 
print(my_other_person.fullname)  # Imprime el nuevo nombre completo

# Aquí se muestra que el tipado de Python permite modificar el tipo de dato de una propiedad
my_other_person.fullname = 666  # Se cambia 'fullname' a un número entero
print(my_other_person.fullname)  # Imprime el nuevo valor (un número)

### Conceptos Adicionales sobre Clases ###

# 1. Herencia:
# La herencia permite que una clase derive de otra, heredando atributos y métodos.

## Clase main o padre
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "El animal hace un sonido"

# Clase que hereda a la Class "Animal" o tambien conocida como hijo
class Dog(Animal):  # 'Dog' hereda de 'Animal'
    def speak(self):  # Sobrescribiendo el método 'speak'
        return f"{self.name} dice: ¡Guau!"

my_dog = Dog("Rex")
print(my_dog.speak())  # Salida: Rex dice: ¡Guau!

# 2. Polimorfismo:
# Permite que diferentes clases sean tratadas como instancias de la misma clase.
class Cat(Animal):
    def speak(self):
        return f"{self.name} dice: ¡Miau!"

def make_animal_speak(animal):
    print(animal.speak())  # Usa el método 'speak' de cada clase

my_cat = Cat("Miau")
make_animal_speak(my_dog)  # Salida: Rex dice: ¡Guau!
make_animal_speak(my_cat)  # Salida: Miau dice: ¡Miau!

# 3. Encapsulamiento:
# Utilizando propiedades privadas y métodos para obtener valores.
class Person:
    def __init__(self, name):
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name  # Método para acceder a la propiedad privada

person = Person("Cesar")
print(person.get_name())  # Salida: Cesar
