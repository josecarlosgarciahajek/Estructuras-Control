max_intentos = 3
for intento in range(1, max_intentos +1):
    usuario = str(input("Introduce el nombre del usuario: "))
    contraseña = str(input("Introduce la contraseña: "))
    intentos_restantes = max_intentos - intento
    if usuario == "root" and contraseña == "toor":
        print("Bienvenido")
        break
    else:
        if intentos_restantes >= 0:
            print("Datos incorrectos. Le quedan", intentos_restantes ,"intentos.")
            exit
            if intentos_restantes == 0:
                print("Has agotados todos tus intentos")