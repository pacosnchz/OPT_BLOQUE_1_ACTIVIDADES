# b1_2_calculadora_simple.py
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
suma = float(num1) + float(num2)
resta = float(num1) - float(num2)
multiplicacion = float(num1) * float(num2)
if float(num2) != 0:
    division = float(num1) / float(num2)
else:
    division = "Indefinida (no se puede dividir por cero)"
output = f"""Resultados:
Suma: {suma}
Resta: {resta}
Multiplicación: {multiplicacion}
División: {division}"""
print(output)

