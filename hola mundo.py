############## CADENAS DE CARACTERES (STRINGS), asigna, concatena o suma, busca, extrae y compara ###########

mensaje = "hola"#asignamosun valor a la variable
mensaje +=" "#estamos agregando contenido a la misma variable (+= junto) sin borra el valor anterior
mensaje += "ernesto"#de igual manera agregamos contenido sin borrar el contenido anterior

mensaje = "hola"
espacio = " "
nombre = "ernesto"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 6 
resultado = numero_uno + numero_dos
resutado = str(resultado)#cambiamos el valor entero(int) de la variable resultado a un string con (str)
print("el resultado es: " +resultado)#hacerlo de esta manera daria error por que queremos suma una caena e caracteres(string) con una variable de tipo entero eso es incorrecto

## Buscar(.find)busca una posicion del 0 al .... cuentas los espacios  como numeros, en una cadena de caracteres y asume ese valor buscado ##

mensaje = "hola franc"
buscar_subcadena = mensaje.find("franc")
print(buscar_subcadena)#el valor de la variable q se est imprimiendo seria 5

## Extraccion [1:8] primer numero posicion inicial y segundo numero posicion final hasta que punto queremos extraer del string ##

nombre = "francisco moreno"
extraer = nombre[0:9]#empieza desde cero siempre osea el f y el 9 seria el espacio pero nose llega a tomar el valor final jamas por que se corta
print(extraer)#se imprimiria el valor que tomo extraer de nombre y es (francisco)
 

## comparacion(==) compara dos cadenas de caracteres strings ##

numero_uno = "que pedo"
numero_dos = "no hay pedo"
print(numero_uno == numero_dos)#con el (==) le pedimos que compare si es igual o no y nos entregara una respuesta booleana (true-false)

################################## PALABRAS RESERVADAS EN PYTHON ######################################

#and-del-for-is-raise-assert-if-else-elif-from-lambda-return-break-global-not-try-class-expert-or-while-continue-exec-import-yield-def-finally-in-print 

############################# OPERADORES ARITMETICOS #######################

## suma (+) ##

numero_uno = 5
numero_dos = 6
suma = numero_uno + numero_dos
print(f"el resultado da: {suma}")#resultado en pantalla 11
## resta (-) ##

numero_uno = 5
numero_dos = 6
resta = numero_uno - numero_dos
print(f"el resultado da: {resta}")#resultado -1

## división (/) ##
numero_uno = 4
numero_dos = 2
división = numero_uno / numero_dos
print(f"el resultado da: {división}")#python agrega un decimal .0 en las divisiones

## multiplicación (*) ##

numero_uno = 5
numero_dos = 6
multiplicación = numero_uno * numero_dos
print(f"el resultado da: {multiplicación}")

## exponente (**) potenciación dice cuatas veces un numero se debe multiplicar por si mismo ##

numero_potenciado = 2 ["ala 5"]
2 x 2 x 2 x 2 x 2
# 4   8   16  32 esta es la formula
numero_uno = 2
exponente = 5
formula = numero_uno ** exponente
print(f"el resultado del exponente es: {formula}")

## módulo (%) funciona e la siguiete manera quiero el resto de 30 debo buscar una multiplicacion que ese acerque a 30, 8 lo multiplico por 3 me da 24 y el resto seria 6 ##

numero_uno = 30
numero_dos = 8
modulo = numero_uno % numero_dos
print(f"el resto seria: {modulo}")# resultado seria 6

## división entera (//) divide dos (int) numeros enteros sin .0 ##

numero_uno = 4
numero_dos = 2
división = numero_uno // numero_dos
print(f"el resultado da: {división}")


#################################### TIPOS DE DATOS ##########################################

## Enteros(int) o largos(long) tanto para numeros positivos como negativos 5 -5 ##

numero = 15
print(numero, type(numero))#con una coma podemos agrgar varios elementos dentro de print,le pedimos q imprima el dato y pedimos el tipo de dato el cuales un entero (int)#

## Numeros flotantes o (float) reales son aquellos que tienen decimales, tanto positivos como negativos 1.5 -1,5 ##

numero = 15.5
print(numero, type(numero))# class float.

## numeros complejos(complex) son aquellos que tienen una parte real y una imaginaria, normalmente son utilizados por ingenieros y cintificos en general ##

numero = " 5 parte real + 6j parte imaginaria"
numero = 5 + 6j
print(numero, type(numero))#seria class complex


## las cadenas("strings", 'strings',"""strings""",'''strings''')es simplemente variable que almacena texto de codigo encerrado en una de los ejemplos de comillas ##

nombre = "franc"
print(nombre, type(nombre))# seria class str o string


## tipo de dato booleano(true, false) ##
verdadero_ono = 3 == 2# no se almace el dato sino que al compara se almacena el dato boleano false 
print(verdadero_ono, type(verdadero_ono))# da class bool.

## fin tipos des datos ##

######## ENTRADA DE DATOS DESDE EL TECLADO ######

nombre = input("introduce tu nombre")
num_int = int(input("introduce un numero entero"))#convierte a valor entero la entrada de los datos
num_float = float(input("introduce un numero flotante"))#convierte a valor decimal a la entrada de los datos
num_complex = complex(input("introduce un numero complex"))#convierte a valor complejo la entrada de los datos

print("string: ",nombre)#la coma se utilizz para ya no tner que transformar en string (str) l variable con los datos almacenados#
print("entero: ",num_int)
print("numero flotante",num_float)
print("numero complejo: ",num_complex)

## Datos aritmeticos ##

nombre = input("cual es tu nombre? ")
print(f" hola {nombre} vamos a realizar una suma")
num_uno = int(input("introduce un numero "))
num_dos = int(input("introduce un segundo numero "))
resultado = num_uno + num_dos
print(nombre + " el resultado de la suma es: ", resultado)


############### SENTENCIAS CONDICIONALES SIMPLES ################

## if ##

num_car = 5#declaramos la variable
if num_car == 5:#decimos si es verdadedor que la variable num_car es igual a 5 (==) ,estamos comparando
    print("el numero es 5")#se ejecuta esto
#si es false solo se muestra fin por que sale del flujo del programa
print("fin")  

## if y datos ##
print("hola que tal dime tu nombre")
nombre = input("introduc tu nombre: ")
print(f"genail como estas {nombre} analizaremos tus calificaciones")
mate = int(input("cual es tu calificacion en matematicas : "))
cta = int(input("cual es la calificacion en ciencias"))
comunicacion = int(input("cual es tu calificacion en lengua"))  
formula = (mate + cta + comunicacion) / 3

x = formula
if x >= 6:
    print(f"felicidades {nombre} aprobaste con: ", x)  


############## SENTENCIAS CONDICIONALES COMPUESTAS ##################

## else, si no se cumple ##

x = int(input("introduce numero no mayor a 10"))

if x <= 10:
    print("hola mundo")
else:
    print("muere mundo")
    
print("fin")

## else complejo ##

print("hola que tal cual es tu nombre? ")
nombre = input("nombre: ")
print(f"genial {nombre} vamos a analizar tus calificaciones")
matematica = int(input("matematicas: "))
lengua = int(input("lengua: "))
ciencias = int(input("ciencias: "))
formula = (matematica + lengua + ciencias) / 3

x = formula
if x >= 6:
    print(f"felicidades {nombre} aprobaste con un promedio de: ", round (x,2))
    
else:
    print(f"que lastima {nombre} desaprobaste basura humana con un promedio de: ", round (x,2))
    
    

##############  SENTENCIAS CONDICIONALES MULTIPLES  ############

## elif ##

print("introduce un numero paar convertir")
num_uno = int(input("introduce el numero: "))

if num_uno == 0:# siesta condicion no se cumle sigue la siguiente y asi susecivamente hasta llegar a else
    print("cero")
elif num_uno == 1:
    print("uno")
elif num_uno == 2:
    print("dos")
elif num_uno == 3:
    print("tres")
else:
    print("el numero es desconocido el programa solo llega hasta tres")
    
print("fin.")


############  SENTENCIAS CONDICIONALES ANIDADAS  ###########






#############  OPERADORES  LOGICOS  ###############

# conjuncion

print("conjuncion (and)")

num_uno = int(input("escribe un numero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("el numero ", num_uno, "cumple con la condicion.\n")
else:
    print("el numero ", num_uno, "no cumple con la condicion.\n")
    
#disyuncion (or)
print("disyuncion (or)")

palabra = input("para cumpir con la condicion escribe 'si' o 'yes'")

if palabra == "si" or palabra == "yes":
    print("la condicion se ha cumplido.\n")
    
else:
    print("la condicion no se ha cumplido.\n")

### IVA CON IVA ###
print("introduce el precio paar convertir el iva")
precio = float(input("introduce el precio: "))
iva = int(input("introduce el iva: "))
complex = (iva / precio) + 1
formula = (precio / complex)
print(f"el resultado es: {formula:.2f}")




############# FOR RANGE #################

print("bienvenido al imprimidor de datos con for: ")
start = int(input("inicio: "))
stop = int(input("stop: "))
step = int(input("step:"))

for i in range(start, stop, step):## RANGE START desde donde inicia, stop donde para no se imprime jamas el valor entero puesto, el orden posito o nagativo en
     print(i)
print("fin del bucle")

# se debe utilzar las mayusculas para las constantes su valor no cambiara MAX = 10



## loop ### imprime sin comillas
instrumentos = ["guitarra", "trombon", "bateria"]

for instrumento in instrumentos:
    print(instrumento)

## length ## 

print(len(instrumentos))

## count() cuidado - no es el numero de objetos, sino la cuenta de un elemento
print(instrumentos.count("piano"))


instrumentos = ["guitarra", "piano", "ukelele", "bateria"]
print(instrumentos)
for i in instrumentos:
  print("Instrumento es " + i)

print(len(instrumentos))
# cuidado - no es el numero de objetos, sino la cuenta de un valor
print(instrumentos.count("piano"))

#acceso
print(instrumentos[0])
print(instrumentos[1])
print(instrumentos[2])
print(instrumentos[-1])  # comenzar desde la final -2, -3 ...
print(instrumentos[2:3])  # rango - devuelve una lista
print(instrumentos[:3])  # coger todos desde prinipio hasta ...
print(instrumentos[2:])  # coger todos desde fin hasta ...
#print(instrumentos[3]) # error

if "piano" in instrumentos:
  print("Piano existe")

# modificar
instrumentos[1] = "PIANO"
print(instrumentos[1])

# añadir
instrumentos.append("bajo")
instrumentos.insert(2, "voz")

print(instrumentos)

# quitar
instrumentos.pop()
print(instrumentos)
instrumentos.remove("PIANO")
print(instrumentos)

# ordenar
instrumentos.sort()
print(instrumentos)
instrumentos.sort(reverse=True)
print(instrumentos)

# tuple - no cambia
dias = ("Lunes", "Martes", "Miercoles")
for d in dias:
  print(d)
print(dias[1])
# dias[1] = "MARTES" # error
#dias.append("Jueves") # error


## list comprehension

numeros = [5, 7 ,3 ,12 ,5 ,6 ,11 ,1]

lista_nueva = [n for n in numeros if n>5]
print(lista_nueva)

# [7, 12, 6, 11]