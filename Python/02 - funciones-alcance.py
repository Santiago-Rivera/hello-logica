"""
Funciones definidas por el usuario
"""

# Simple


def greet():
    print("Hola, Python!")


greet()  # Llamada a la función

# Con retorno


def return_greet():
    return "Hola, Python!"


print(return_greet())

# Con argumentos

def arg_greet(name):
    return f"Hola, {name}!"

print(arg_greet("Sinsinati"))  # Llamada a la función con argumento


def args_greet(greet, name):
    return f"{greet}, {name}!"

print(args_greet(greet="Hi", name="Sinsinati"))  # Llamada a la función con argumentos


# Con argumentos por defecto

def default_greet(name="Sinsinati"):
    return f"Hola, {name}!"

print(default_greet()) # Llamada a la función sin argumento
print(default_greet("Python")) # Llamada a la función con argumento


# Con argumentos y retorno

def arg_return_greet(greet, name):
    return f"{greet}, {name}!"

print(arg_return_greet("Hi", "Sinsinati"))  # Llamada a la función con argumentos y retorno


# Con retoro de varios valores

def multi_return_greet():
    return "Hola", "Python!"


greet, name = multi_return_greet()  # Llamada a la función con retorno de varios valores
print(greet)  # Imprime "Hola"
print(name)  # Imprime "Python!"

# Con un numero varoiable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Sinsinati", "Python", "JavaScript")  # Llamada a la función con un número variable de argumentos

# Con un número variable de argumentos con palabras clave


def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    first="Sinsinati",
    second="Python",
    third="JavaScript"
)  # Llamada a la función con un número variable de argumentos con palabras clave

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()  # Llamada a la función interna


outer_function()  # Llamada a la función externa

"""
Funciones del leguaje
"""

print(len("Sinsinati"))  # Llamada a la función len() del lenguaje
print(type(21))  # Llamada a la función type() del lenguaje
print("Sinsinati".upper())  # Llamada a la función upper() del lenguaje

"""
Variables globales y locales
"""

global_var = "Python!"  # Variable global

print(global_var)  # Imprime "Python!"

def hello_python():
    local_var = "Hola"  # Variable local
    print(f"{local_var}, {global_var}!")  # Imprime "Hola, Python!"


print(global_var)  # Imprime "Python!"
# print(local_var)  # Error: local_var no está definida en este ámbito

hello_python()  # Llamada a la función

"""
Extra
"""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{text_1} {text_2}")
        elif number % 3 == 0:
            print(f"{text_1}")
        elif number % 5 == 0:
            print(f"{text_2}")
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))  # Llamada a la función con argumentos