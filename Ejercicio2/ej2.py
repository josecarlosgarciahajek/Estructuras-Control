number1 = int(input("Introduce el número de inicio: "))
number2 = int(input("Introduce el número final: "))
suma = 0
for i in range(number1, number2+1):
    suma = i + suma
print("El resultado es: ", suma)