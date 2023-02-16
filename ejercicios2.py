print("conversor iva 21% 10% 4%")
precio = float(input("precio sin iva: "))
iva = int(input("cantidad de iva: "))
formula = (precio * iva) / 100
suma = formula + precio

if iva == 21:
     print("=============")
     print("resultado")
     print("=============")
     print(f"precio sin iva: {precio:.2f}")
     print(f"iva: {formula:.2f}")
     print(f"precio con iva: {suma:.2f}")

elif iva == 10:
     print("=============")
     print("resultado")
     print("=============")
     print(f"precio sin iva: {precio:.2f}")
     print(f"iva: {formula:.2f}")
     print(f"precio con iva: {suma:.2f}")

elif iva == 4:
     print("=============")
     print("resultado")
     print("=============")
     print(f"precio sin iva: {precio:.2f}")
     print(f"iva: {formula:.2f}")
     print(f"precio con iva: {suma:.2f}")

else:
     print("==============================")
     print("no cumple la condicion")
     print("GRACIAS POR USAR MI PROGRAMA")
     print("==============================")
 