# print("hola quetal introduce tu nombre:")
# nombre = input("nombre: ")
# print(f"hola que tal {nombre} por favor introduce la cantidad que gans al mes")
# sueldo = int(input("introduce tu sueldo: "))
# formula = sueldo * 10
# print(f"hey {nombre} si feras experto en python ganarias esto {formula}")

## ejercicio 2 ##

# print("hola bienvenido a mi aplicacion de sumar por favor introduce dos numeros")
# num_uno = int(input("numero uno: "))
# num_dos = int(input("numero dos: "))
# formula = num_uno + num_dos
# print("la suma es", formula)

## ejercico 3 ##

# print("la accion de santander cambia convierte el valor de las siguientes acciones 3.1453 2.987 y 3.5 de mainframe")
# num_uno = float(input("introduce el primer numero: "))
# num_dos = float(input("introduce el segundo numero: "))
# num_tres = float(input("introduce el tercer numero: "))
# print(int(float(num_uno)))
# print(int(float(num_dos)))
# print(int(float(num_tres)))

## ejercicio 4 ##

# print("que tal cuantas personas son?")
# personas = int(input("introduce el numero de personas: "))
# print("cual es el precio a pagar?")
# precio = float(input("coso de la cena: "))
# formula = precio / personas
# print(f"el precio a pagar es : {formula}")

## ejercicio 5 ##

# print("presiona la letra 'k' para convertir a kilos a libras y la letra 'l' para convertir a libras a kilos")
# letra = input("introduce una letra")

# if letra == "k"
# or letra == "K":
#     kilos = int(input("introduce los kilos: "))
#     formula = kilos * 2.205
#     print(f"la con version da: {formula}")
# elif letra == "l" or letra == "L":
#     libras = float(input("introduce las libras: "))
#     formula_dos = libras / 2.205
#     print(f"la conversion da: {formula_dos}")

## ejercicio ## 



# string = "string"# declaamosla variable iterable qu nos va a permitir recorrer sus elementos uo a auno utilizando numeros que van desde 0 a lo que alcance

# for i in string:# niciamos el bucle le decimos que (i) tome el valor de la cadena 
#     print(i)# pedios que imprima cada uno de los elementos de la dadea por que i ya tomo su valor
# print("fin de la aplicacion")# al terminarsu ejecucio aprece el prent fi de la aplicaion

# range(10) #si solo declaramos un numero entero ese seria el stop, le dicimos a range que compare 0 +1 es igua a 10 y asi sucesivmente hasta llegar 9+ 1 es igual a 10? si ahi se detiene#
# range(5, 11)#start-stop (5-11) exactantelo mismo le dicemos que empiece desde el 5 y sumasmo uno hasta llegar a 11
# range(0, 11, 2)# declaramos el inicio (0)start- el final (11)stop- y las veces que se va a incrementar (2)step y se pregunta 2 es igual aa 11 y asi sumando el valor la secuencia que nos retorna rages igual del 0 al 10
# range(10, 0, -1)# de igual manera pero d emanera decreciente peroen esta ocacion no se imrimiria el 0 ya es el fin del range

# print("bienvenido al imprimidor de datos con for: ")
# start = int(input("inicio: "))
# stop = int(input("stop: "))
# step = int(input("step:"))

# for i in range(start, stop, step):
#      print(i)
# print("fin del bucle")

gente = int(input("cuantas personas acudiran al evento: "))
MAX_INVITADOS = 5
invitado = []

if gente > 5:
     print("solo pueden ser 5 invitados")
elif:
     for i in range(gente):#creamos un for para repetir las preguntas
          nombre = input("introducir un invitado")
          invitado.append(nombre)#utilizamos append pra  ñadir elementos a la lista

print(f"lista de invitados: ")
for i in invitado:
     print(i)
else:
     print("ERROR, Por favor reinicie el programa")


