import re

"""
Expresiones regulares
"""


def find_numbers(text: str) -> list:
    return re.findall(r"\d+", text)


print(find_numbers("Este es el ejercicio 16"))


"""
Extra
"""


def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))


print(validate_email("sinsinati@gmail.com"))


def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))


print(validate_phone("+593 983 397 026"))


def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))


print(validate_url("http://www.moure.dev"))