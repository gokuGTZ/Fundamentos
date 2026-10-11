def leerPorcentaje(recurso):
    return int(input("Porcentaje de " + recurso + ": "))

def evaluarProcesador(porcentaje):
    if porcentaje <= 70:
        return "Estado normal"
    elif porcentaje <= 85:
        return "Requiere supervisión"
    else:
        return "Estado crítico"

def evaluarMemoria(porcentaje):
    if porcentaje <= 75:
        return "Estado normal"
    elif porcentaje <= 85:
        return "Requiere supervisión"
    else:
        return "Estado crítico"

def evaluarAlmacenamiento(porcentaje):
    if porcentaje <= 75:
        return "Estado normal"
    elif porcentaje <= 85:
        return "Requiere supervisión"
    else:
        return "Estado crítico"

def evaluarServidor(cpu, ram, disco):
    return (cpu == "Estado normal"
            and ram == "Estado normal"
            and disco == "Estado normal")

def mostrarResultados(cpu, ram, disco, estadoCPU,
                      estadoRAM, estadoDisco, correcto):
    print("\n--- REPORTE DEL SERVIDOR ---")
    print("Procesador:", cpu, "% -", estadoCPU)
    print("Memoria RAM:", ram, "% -", estadoRAM)
    print("Almacenamiento:", disco, "% -", estadoDisco)

    if correcto:
        print("Estado del servidor: Funciona correctamente")
    else:
        print("Estado del servidor: Requiere atención")

cpu = leerPorcentaje("procesador")
ram = leerPorcentaje("memoria RAM")
disco = leerPorcentaje("almacenamiento")

estadoCPU = evaluarProcesador(cpu)
estadoRAM = evaluarMemoria(ram)
estadoDisco = evaluarAlmacenamiento(disco)

correcto = evaluarServidor(estadoCPU, estadoRAM, estadoDisco)

mostrarResultados(cpu, ram, disco, estadoCPU,
                  estadoRAM, estadoDisco, correcto)
