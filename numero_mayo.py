numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 8, 5]
print(max(numeros))

pares = 0
impares = 0



for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"{pares} Son par")
print(f"{impares} Son impares")


invertida = numeros[::-1]



print(invertida)




sin_duplicados = (list(set(numeros)))
print(sin_duplicados)
