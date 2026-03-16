def calcular_salario(horas, valor_hora):
    if horas <= 40:
        salario = horas * valor_hora
        return (salario)
    else:
        extra = (horas - 40) * 2
        salario = (40+extra) * valor_hora
        return (salario)
    



nombre = input("Nombre empleado: ")
horas = int(input("Horas trabajadas: "))
valor_hora = int(input("Ingresa valor de hora: "))




print(f"Holiiiii {nombre} tu salario es de: {calcular_salario(horas,valor_hora)}")

