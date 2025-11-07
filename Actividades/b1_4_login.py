ususario_correcto = "admin"
contrasena_correcta = "1234"
usuario = input("Ingrese su usuario: ")
contrasena = input("Ingrese su contraseña: ")
if usuario == ususario_correcto and contrasena == contrasena_correcta:
    print("¡Acceso concedido!")
else:
    print("¡Acceso denegado!")
