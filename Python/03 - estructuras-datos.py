"""
Estructuras
"""

# Listas
from curses.ascii import isdigit


my_list = ["Brais", "Moure", "Python", "Ciencia de datos"]
print(my_list)
my_list.append("Castor") # inserción
my_list.append("Castor") # inserción
print(my_list)
my_list.remove("Python") # eliminación
print(my_list)
print(my_list[1]) # acceso
my_list[2] = "Data Science" # actualización
print(my_list)
my_list.sort() # ordenación
print(my_list)

# Tuplas
my_tuple = ("Santiago", "Rivera", "Sinsinati", "21")
print(my_tuple[1]) # acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_set = {"Santiago", "Rivera", "Sinsinati", "21"}
print(my_set)
my_set.add("sinsinati@gmail.com") # inserción
my_set.add("sinsinati@gmail.com")
my_set.remove("Rivera") # eliminación
my_set = set(sorted(my_set)) # ordenación
print(my_set)
print(type(my_set))

# Diccionarios
my_dict: dict = {
    "name": "Santiago",
    "surname": "Rivera",
    "alias": "Sinsinati",
    "age": 21
}
my_dict["email"] = "sinsinati@gmail.com" # inserción
print(my_dict)
del my_dict["surname"] # eliminación
print(my_dict)
print(my_dict["name"]) # acceso
my_dict["age"] = 22 # actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # ordenación
print(my_dict)
print(type(my_dict))

"""
Extra
"""

def my_agenda():

    agenda: dict = {}

    def insert_contact():
        phone = input("Nuevo teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
            print(f"\nContacto {name} actualizado con teléfono {phone}.")
        else:
            print("Debes ingresar un número de teléfono válido un máximo 11 dígitos.")

    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("\nNombre del contacto: ")
                if name in agenda:
                    print(f"\nEl teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"\nEl contacto {name} no existe en la agenda.")
            case "2":
                name = input("\nNombre del contacto: ")
                insert_contact()
            case "3":
                name = input("\nNombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"\nEl contacto {name} no existe en la agenda.")
            case "4":
                name = input("\nNombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f"\nContacto {name} eliminado de la agenda.")
                else:
                    print(f"\nEl contacto {name} no existe en la agenda.")
            case "5":
                print("\nSalir")
                break
            case _:
                print("\nOpción no válida. Elige una opción del 1 al 5.")

my_agenda()