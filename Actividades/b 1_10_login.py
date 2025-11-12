# Sistema de registro e inicio de sesión
# --------------------------------------
# Este programa permite al usuario registrarse con un email y contraseña válidos,
# e iniciar sesión posteriormente con esas credenciales.

# Conceptos aplicados:
# - Variables y tipos de datos
# - Condicionales y bucles
# - Control de flujo
# - Validaciones con operadores lógicos
# - Buenas prácticas (PEP 8)

import re


def validar_email(email: str) -> bool:
    # Valida si el email cumple con los requisitos:
    # - Mínimo 3 caracteres
    # - Contiene '@'
    # - Contiene una extensión válida (.com, .es, .net)
    # - No contiene símbolos especiales no permitidos
    extensiones_validas = (".com", ".es", ".net")
    simbolos_invalidos = "!#$%&*? "

    if len(email) < 3:
        print("El email debe tener al menos 3 caracteres.")
        return False

    if "@" not in email:
        print("El email debe contener '@'.")
        return False

    if not any(email.endswith(ext) for ext in extensiones_validas):
        print("El email debe terminar en .com, .es o .net.")
        return False

    if any(s in email for s in simbolos_invalidos):
        print("El email contiene símbolos no permitidos.")
        return False

    return True


def validar_contrasena(password: str) -> bool:
    # Valida si la contraseña cumple con los requisitos:
    # - Mínimo 8 caracteres
    # - Contiene al menos una mayúscula
    # - Contiene al menos un número
    # - Contiene al menos un símbolo especial (!@#$%&*?)
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False

    if not re.search(r"[A-Z]", password):
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False

    if not re.search(r"\d", password):
        print("La contraseña debe contener al menos un número.")
        return False

    if not re.search(r"[!@#$%&*?]", password):
        print("La contraseña debe contener al menos un símbolo especial (!@#$%&*?).")
        return False

    return True


def registrar_usuario():
    # Permite al usuario registrarse si su email y contraseña son válidos.
    global usuario, contrasena

    print("\nREGISTRO DE NUEVO USUARIO")
    while True:
        email = input("Introduce tu email: ")
        if validar_email(email):
            break

    while True:
        password = input("Crea una contraseña: ")
        if validar_contrasena(password):
            break

    usuario = email
    contrasena = password
    print("Registro exitoso. Ya puedes iniciar sesión.")


def iniciar_sesion():
    # Permite al usuario iniciar sesión verificando sus credenciales.
    if not usuario:
        print("No hay usuarios registrados aún. Regístrate primero.")
        return

    print("\nINICIO DE SESIÓN")
    email = input("Email: ")

    if email != usuario:
        print("Usuario no encontrado.")
        return

    intentos = 3
    while intentos > 0:
        password = input("Contraseña: ")
        if password == contrasena:
            print("Acceso concedido.")
            return
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}")

    print("Demasiados intentos fallidos. Regresando al menú principal.")


def mostrar_menu():
    # Muestra el menú principal y gestiona la elección del usuario.
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("[1] Registrarse")
        print("[2] Iniciar sesión")
        print("[3] Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo del programa. Gracias.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Variables globales para guardar el usuario y contraseña
usuario = ""
contrasena = ""

# Punto de entrada del programa
if __name__ == "__main__":
    mostrar_menu()
