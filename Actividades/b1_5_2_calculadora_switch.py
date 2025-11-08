num1 = input("ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
operacion = input("Ingrese la operación (+, -, *, /): ")
match operacion:
    case "+":
        resultado = float(num1) + float(num2)
        print(f"El resultado de la suma es: {resultado}")
    case "-":
        resultado = float(num1) - float(num2)
        print(f"El resultado de la resta es: {resultado}")
    case "*":
        resultado = float(num1) * float(num2)
        print(f"El resultado de la multiplicación es: {resultado}")
    case "/":
        if float(num2) != 0:
            resultado = float(num1) / float(num2)
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    case _:
        print("Operación no válida. Por favor, ingrese +, -, * o /.")