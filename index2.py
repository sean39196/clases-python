###### repaso #####
#a = 10# declaracion de variable
#print(id(a))# bhuscamos donde esta ubicada la variable dentro de la memoria
#a = 11
#isinstance(a,int)# preguntamos el tipo de dato
#print(isinstance(a,int))#imprimimos el tipo de dato
#type(a)#PEDIMOS ELTIPO DE DATO QUE ES A
#b = ["adrian","alvaro"]
#b.append("genecis")
#a = 10
#if (a == 10 or a == 11):

#a = 11    
#if a in [10,11]:# asi se declara una lista
#print("es igual a 10") # si se cumple la condicion se imprime esto

#elif (a == 12):si no se cumple la primera condicion
    #print(12)
#else:
    #print("otros")# si no se cumple ninguna condicion este se va a imprimir

## ejemplo ##

#a = 10

#if a > 10:
    #print(f"la variable con valor {a} es igual a 10")
#else:
    #print(f"la variable con valor {a} es menor o igual")

# print("introduce un numero no mayor a 100")

# b = int(input("introduce un numero b: "))

# if b < 100:
#     print(f"la variable b con valor {b} es menor a 100")
# elif b > 100:
#     print(f"la variable b con valor {b} es mayor que 100")
# elif b >= 100:
#     print(f"la variable b con el valor {b} es mayor o igual a 100")
# else:
#     print("FIN. ES NEGATIVO")

#     ## for -range ##

#     var_uno = ["adrian", "alvaro"]
#     for i in var_uno: # i adquiere el valor de var_uno
#         print(i)

#     a = range(10)

#     for i in range(10):# imprime desde el un o al 9 el 10 es el fin no se muestra
#         print(i)

#     for i in range(10):#hace que repitamos 10 veces lo que queramos
#         print("hola")

nombres = ["adrian", "alvaro", "genecis"]
suma = "andrea"
nombres.append(suma)
for nombre in nombres:
    print(nombre)