# try:
#     resultado = 10/0
# except ZeroDivisionError:
#     print("Error: No se puede dividir entre cero.")

try:
    edad = int(input("Ingrese su edad: "))
    print(f"Edad registrada: {edad}")
except ValueError:
    print("Error: Por favor, ingrese un número entero")
    