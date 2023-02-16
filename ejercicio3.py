## multiplicador de salario #3

# print("buen dia cuale estu nombre ")
# nombre = input("introduce tu nombre: ")
# print(f"que tal {nombre} introduce la cantidad de dinero que ganas al mes: ")
# num_uno = int(input("sueldo: "))
# formula = num_uno * 10
# print(f"{nombre} si aprendieras python ganarias esto ", formula)

## sumador de numeros ##
# print("introduce dos numeros para sumarlos")
# n_uno = int(input("introduce un numero: "))
# n_dos = int(input("introduce un segundo numero: "))
# formula = n_uno + n_dos
# print(f"la suma es {formula}")

## conversor de numeros reales (float) a enteros(int) ##

# print("que tal introduce tu nombre")
# name = input("introduce tu nombre: ")
# print(f"genial {name} introduce un numero decimal o real ejm: 3.123")
# uno = float(input("numero real o decimal: "))
# print (int(float(uno)))


## dividir gsstos de comidad ##

# print("quetal introduce el la cantidad de personas")
# pers = int(input("introduce la cantidad de personas: "))
# print("genial introduce el precio a pagar")
# precio = float(input("introduce el precio: "))
# division = precio / pers
# print(f"cada uno debe pagar {division}")

## otra forma ##
## convertir kilos a libras ##

# print("buen dias escribe la letra 'k' o 'l' si quieres convertir kilos a libras")
# compl = input("escribe la letra : ")
# if compl == "k" or compl == "K":
#     kilos = int(input("introduce el peso en kilos: "))
#     form = kilos * 2.205
#     print(f"el peso en libras seria {form}")
# elif compl == "l" or compl == "L":
#      libras = float(input("introduce el peso en libras: "))
#      form_dos = libras / 2.205
#      print(f"el peso en libras seria {form_dos}")
    
# else:
#     print("no has introducido el valor pedido")


## convertir iva ##



## ejercicio ## 
print("bienvenido a mi programa para calcular el iva del 21% 10% 4%")
print("sumar iva")
precio = float(input("precio sin iva: "))
porcentaje = int(input("porcentaje de iva: "))
suma = formula + precio

if porcentaje == 21:
     print("=============")
     print("resultado")
     print("=============")
     print(f"precio sin iva: {precio:.2f}")
     print(f"iva: {formula:.2f}")
     print(f"precio con iva: {suma:.2f}")
elif porcentaje == 10:
     print("=============")
     print("resultado")
     print("=============")
     print(f"precio sin iva: {precio:.2f}")
     print(f"iva: {formula:.2f}")
     print(f"precio con iva: {suma:.2f}")
elif porcentaje == 4:
     print("=============")
     print("resultado")
     print("=============")
     print(f"precio sin iva: {precio:.2f}")
     print(f"iva: {formula:.2f}")
     print(f"precio con iva: {suma:.2f}")

else:
     print("=======================================")
     print("no has introducido bien el porcentaje")
     print("fin de la aplicacion GRACIAS POR USARNOS")
     print("=======================================")
