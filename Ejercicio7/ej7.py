numeros = []
while True:
    num = str(input("Introduzca un numero: "))
    if num == "final":
        break
    else:
        numeros.append(num)

print ("El número más alto es: ", max(numeros))