# b1_3_conversor_datos.py
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura_cm = input("Ingrese su altura en centímetros: ")
altura_m = float(altura_cm) / 100
output = f"Hola, {nombre}, tienes {edad} años y mides {altura_m:.2f} metros."
print(output)

