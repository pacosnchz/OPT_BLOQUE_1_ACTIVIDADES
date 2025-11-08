num1 = input("Insgrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
operacion = input("Ingrese la operación (+, -, *, /): ")
if operacion == "+":
    resultado = float(num1) + float(num2)
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "-":
    resultado = float(num1) - float(num2)
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "*":
    resultado = float(num1) * float(num2)
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "/":
    if float(num2) != 0:
        resultado = float(num1) / float(num2)
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no válida. Por favor, ingrese +, -, * o /.")