taquerias = {
    "Taqueria 1": {
        "nombre": "Tacos Emilio's",
        "empleados": 5,
        "combos": ["2 por 1", "otro combo"],
    },
    "Taqueria 2": {
        "nombre": "Tacos grillos",
        "empleados": 3,
        "combos": ["combo 1", "combo 2"],
    }
}

for clave, valor in taquerias.items():
    print("===============================")
    print(clave)
    print(valor["nombre"])
    for lista in valor["combos"]:
        print("Cada combo: ", lista)

