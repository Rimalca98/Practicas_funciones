def analizar_numero(numero):
    if numero > 0:
        return "El número es positivo."
    elif numero < 0:
        return "El número es negativo."
    else:
        return "El número es cero."
    
numero = int(input("Ingresa numero:"))


print(analizar_numero(numero))