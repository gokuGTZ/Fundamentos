bases = [
    "PostgreSQL", "MongoDB", "InfluxDB", "MySQL",
    "Redis", "Prometheus", "SAP HANA",
    "Cassandra", "Oracle", "OpenTSDB"
]

clasificaciones = []

for base in bases:
    print("\nBase de datos:", base)
    print("1. Relacional")
    print("2. No relacional")
    print("3. Series temporales")

    opcion = input("Elige la clasificación: ")

    if opcion == "1":
        clasificaciones.append("Relacional")
    elif opcion == "2":
        clasificaciones.append("No relacional")
    elif opcion == "3":
        clasificaciones.append("Series temporales")
    else:
        clasificaciones.append("Opción no válida")

   
print("")
print("Clasificación de bases de datos:")
for i in range(len(bases)):
    print(bases[i] + ": " + clasificaciones[i])