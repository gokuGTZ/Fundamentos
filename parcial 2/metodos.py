def calcular_salario(salario_bruto):
    if(salario_bruto < 9500):
        return salario_bruto
    
    descuento = salario_bruto * 0.26
    return salario_bruto -descuento

def obtenerAguinaldo(salario_bruto): 
    salario_diario = salario_bruto / 30
    print("cuanto gano por dia :(",salario_diario)
    return salario_diario*15



salario = 9000
print("Empresa: GAMA CONSULTORES IA")
print(calcular_salario(salario))
print(obtenerAguinaldo(salario))
print("Desarollador full senior")
print(calcular_salario(36000.00))
print(obtenerAguinaldo(36000.00))