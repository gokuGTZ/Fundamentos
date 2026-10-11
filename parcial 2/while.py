def faltan_archivos(respaldados):
    return respaldados < 10

respaldados = 0

while faltan_archivos(respaldados):
    print("RESPALDO DE ARCHIVOS")
    print("1. Respaldar un archivo")
    print("2. Respaldar varios archivos")
    print("3. Ver avance")
    print("4. Cancelar")
    print("5. Finalizar:")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        respaldados += 1
        print("Archivo respaldado, Total:", respaldados)

    elif opcion == "2":
        respaldados += 3
        print("Varios archivos respaldados, Total:", respaldados)

    elif opcion == "3":
        print("Archivos respaldados:", respaldados)
        continue

    elif opcion == "4":
        print("Respaldo cancelado.")
        break

    elif opcion == "5":
        print("Respaldo finalizado.")
        break

    else:
        print("Opción no válida.")

if respaldados == 10:
    print("Respaldo listo.")
