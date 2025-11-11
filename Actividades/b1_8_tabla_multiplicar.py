numero = input("Ingrese un número para ver su tabla de multiplicar: ") # Solicitar al usuario un número
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):  # creamos la variable 'i' que va del 1 al 10
    resultado = int(numero) * i # multiplicamos el numero ingresado por 'i'
    print(f"{numero} x {i} = {resultado}") #imprimimos todos los resultados en orden