print("presiona 'k' para calcular un precio sin iva o presiona 'l' para calcular un precio con iva")
letra = input("introduce el tipo de conversor: ")

if letra == 'k' or letra == 'K':
    precio = float(input("introduce el precio sin iva: "))
    iva = int(input("introduce la cantidad del iva: "))
    formula = (precio * iva) / 100
    suma = precio + formula
    print("==========")
    print("RESULTADO")
    print("==========")
    print(f"precio sin iva {precio:.2f}")
    print(f"iva: {formula:.2f}")
    print(f"precio con iva: {suma:.2f}")
elif letra == 'l' or letra == 'L':
    precio = float(input("introduce el precio con iva: "))
    iva = int(input("introduce la cantidad de iva a analizar: "))
    complic = (iva / precio) + 1
    formula_dos = (precio / complic)
    print("==========")
    print("RESULTADO")
    print("==========")
    print(f"precio sin iva: {formula_dos:.2f}")
    print(f"precio con iva: {precio:.2f}")
else:
    print("no introduciste el valor indicado")