def puede_votar(edad):
    if edad >= 18:
        return "Puede votar"
    else:
        return "No puede votar"
nombre = input("Tu nombre:")
edad = int(input("Tu edad:"))

print(nombre, puede_votar(edad))
