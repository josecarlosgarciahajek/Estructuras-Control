number1 = int(input("Introduce el número de inicio: "))
number2 = int(input("Introduce el número final: "))
num_par = 0
num_impar = 0
for i in range(number1, number2+1):
    if i % 2 == 0:
        num_par += i
    else:
        num_impar += i
print("Los pares suman" , num_par , "y los impares" , num_impar)