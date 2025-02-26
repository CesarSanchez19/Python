### Exception Handling ###

"""
El manejo de excepciones en Python permite capturar y manejar errores inesperados 
durante la ejecución de un programa, evitando que este se detenga abruptamente.
Se logra mediante los bloques try-except. Esto es útil para asegurar la estabilidad del programa y mejorar la experiencia del usuario.

Python proporciona excepciones predefinidas como:
- TypeError: Ocurre cuando se usa un tipo de dato incorrecto.
- ValueError: Se lanza cuando una función recibe un argumento con un valor incorrecto.
- FileNotFoundError: Se genera cuando se intenta abrir un archivo que no existe.
- ZeroDivisionError: Se produce cuando se intenta dividir por cero.
- KeyError: Ocurre cuando se intenta acceder a una clave inexistente en un diccionario.
"""

## Estructura de manejo de excepciones ##

# try: Intenta ejecutar este código y detecta posibles errores.
# except: Se ejecuta si ocurre una excepción y permite manejarla adecuadamente.
# else: (Opcional) Se ejecuta si NO ocurre ninguna excepción en el bloque try.
# finally: (Opcional) Se ejecuta siempre, haya o no una excepción, ideal para liberar recursos.

# Variables de ejemplo
numberOne = 5
numberTwo = 1
numberTwo = "1"  # Esto generará un error al intentar sumarlo con un entero.

# Ejemplo de verificación sin excepciones (método rudimentario, no recomendado para manejar errores)
"""
if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("No se cumplió la condición")
"""

# Manejo de excepciones con try-except para evitar fallos inesperados
try:
    print(numberOne + numberTwo)  # Esto generará un TypeError
    print("No se ha producido un error")  # No se ejecutará si hay error
except Exception as error:
    print("Se ha producido un error:", error)  # Captura cualquier error y lo muestra

# Manejo de excepciones con try-except-else para realizar acciones si no hay errores
try:
    print(numberOne + numberTwo)  # Intentamos realizar la operación
    print("No se ha producido un error")  
except Exception as error:
    print("Se ha producido un error:", error)  # Se ejecuta si ocurre un error
else:
    print("La ejecución continúa correctamente")  # Se ejecuta si no hay error

# Manejo de excepciones con try-except-else-finally para mayor control
try:
    print(numberOne + numberTwo)  # Intentamos realizar la operación
    print("No se ha producido un error")
except Exception as error:
    print("Se ha producido un error:", error)  # Se ejecuta si ocurre un error
else:
    print("La ejecución continúa correctamente")  # Se ejecuta si no hay error
finally:
    print("La ejecución continúa (finally siempre se ejecuta, útil para liberar recursos como archivos abiertos o conexiones de base de datos)")

# Sin manejo de errores, este código produciría un error
# print(numberOne + numberTwo)  # Descomentar para ver el error

### Excepciones por tipo ###

# Capturar excepciones específicas ayuda a manejar errores de manera más precisa
try:
    print(numberOne + numberTwo)  # Genera TypeError
    print("No se ha producido un error")
except ValueError:  # Captura errores de tipo ValueError
    print("Se ha producido un ValueError")
except TypeError:  # Captura errores de tipo TypeError
    print("Se ha producido un TypeError")

# Captura de la información de la excepción para debugging
try:
    print(numberOne + numberTwo)  # Genera TypeError
    print("No se ha producido un error")
except ValueError as error:
    print("Error capturado:", error)  # Imprime el error capturado
except Exception as error:
    print("Error capturado:", error)  # Captura cualquier otra excepción y la imprime

### Ejemplos adicionales de manejo de excepciones ###

# Captura múltiple de excepciones
try:
    numero = int(input("Ingresa un número: "))  # Puede generar ValueError si se ingresa texto
    resultado = 10 / numero  # Puede generar ZeroDivisionError si se ingresa 0
    print("El resultado es:", resultado)
except ValueError:
    print("Error: Debes ingresar un número entero.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")

# Uso de raise para lanzar excepciones personalizadas
try:
    edad = int(input("Ingresa tu edad: "))
    if edad < 18:
        raise ValueError("Debes ser mayor de edad.")
    print("Acceso permitido.")
except ValueError as e:
    print("Error:", e)

# Manejo de archivos con excepciones
try:
    with open("archivo.txt", "r") as file:
        contenido = file.read()
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")

### Buenas prácticas en el manejo de excepciones ###
# 1. Capturar excepciones específicas en lugar de usar 'except Exception' siempre que sea posible.
# 2. Incluir mensajes de error detallados para facilitar la depuración.
# 3. Usar 'finally' para limpiar recursos como archivos abiertos o conexiones de base de datos.
# 4. No abusar de excepciones para controlar el flujo del programa, mejor validar condiciones antes.
# 5. Personalizar excepciones con 'raise' para manejar errores específicos en nuestras funciones.
