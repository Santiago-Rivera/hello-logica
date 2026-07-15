"""
Operadores
"""

# Operadores aritméticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 *3 = {10* 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 **3 = {10** 3}")
print(f"Division entera: 10 // 3 = {10 // 3}")

# Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"AND: True and False es {True and False}")
print(f"OR: True or False es {True or False}")
print(f"NOT: not True es {not True}")

# Operadores de asignación
x = 10
print(f"Asignación: x = 10 es {x}")
x += 5
print(f"Asignación suma: x += 5 es {x}")
x -= 3
print(f"Asignación resta: x -= 3 es {x}")
x *= 2
print(f"Asignación multiplicación: x *= 2 es {x}")
x /= 4
print(f"Asignación división: x /= 4 es {x}")
x %= 3
print(f"Asignación módulo: x %= 3 es {x}")
x **= 2
print(f"Asignación exponente: x **= 2 es {x}")

# Operadores de identidad
a = [1, 2, 3]
b = a
print(f"Identidad: a is b es {a is b}")
c = [1, 2, 3]
print(f"Identidad: a is c es {a is c}")

# Operadores de pertenencia
print(f"Pertenencia: 2 in a es {2 in a}")
print(f"Pertenencia: 4 in a es {4 in a}")

# Operadores de bit
a = 10  # 1010 en binario
b = 4   # 0100 en binario
print(f"AND bit a & b = {10 & 4})")
print(f"OR bit a | b: = {10 | 4})")
print(f"XOR bit a ^ b: = {10 ^ 4})")
print(f"NOT bit ~a: = {~10})")
print(f"Desplazamiento a la izquierda a << 1: = {10 << 1})")
print(f"Desplazamiento a la derecha a >> 1: = {10 >> 1})")

"""
Estructuras de control
"""

# Condicionales

my_string = "Sinsinati"

if my_string == "Sinsinati":
    print(f"{my_string} es igual a 'Sinsinati'")
elif my_string == "SinsinatiDev":
    print(f"{my_string} es igual a 'SinsinatiDev'")
else:
    print(f"{my_string} no es igual a 'Sinsinati'")

# Iterativas

for i in range(11):
    print(f"Iteración {i}")

i = 0

while i < 11:
    print(i)
    i += 1

# Manejo de excepciones

try:
    print(10 / 1)
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
finally:
    print("Bloque finally ejecutado.")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
