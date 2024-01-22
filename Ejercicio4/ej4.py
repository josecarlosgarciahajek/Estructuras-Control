usuario = str(input("Introduce el nombre del usuario: "))
contraseña = str(input("Introduce la contraseña: "))

if usuario == "root" and contraseña == "toor":
    print("Bienvenido")
else:
    print("Acceso fallido")