nombres = ["Ana", "Alejandro", "Juan", "Sofia", "Paco", "Angeles"]
for nombre in nombres:
    if nombre.startswith("A") or nombre.startswith("a"): #seleccionamos todos los nombre que empiezan por 'a' ó 'A'
        continue #saltamos los nombres seleccionadios y pasamos al siguiente paso
    print(nombre)

# Este código actúa sobre una lista de nombres y utiliza 'continue' para saltar aquellos que comienzan
# con la letra 'A' o 'a', imprimiendo solo los demás nombres.

