# #print("hola")

# #help("keywords")
# #import keyword
# #print(keyword.kwlist)

# #a = keyword.kwlist

# #print(type(a)) #que tipo de dato es list

# #a = 4.345 #cambiamos el valor a un float
# #print(type(a)) #imprimimos el tipon de dato que es
# #print(isinstance(a, float)) #imprimimos utilizamos isinstance(a, float) para comprobar si es un float con una respuesta booleana


# #print(id(x))
# #x = 20
# #print(id(x))
# nombres = ["jon", "maria"]
# print(id(nombres))
# nombres.append("pedro")
# print(id(nombres))
# #que es del
# exist = true # tipo de dato booleano
# if exist == True:
#     print("TRUE")
#     print("true")
# print("fin")

# x = 3
# if (x > 1):
#     print("mas que uno")
# elif(x < 3) and (y < 3):
#     print("jkaja")
# else:
#     print("end")

# lista = [262, 444, "Maria"]
# for i in lista:
#     print(i)

#     x = range(10)
#     print(s)
#     print(type(s))

#     ######## repaso #######

print("introduce el precio paar convertir el iva")
precio = float(input("introduce el precio: "))
iva = int(input("introduce el iva: "))
complex = (iva / precio) + 1
formula = (precio / complex)
print(f"el resultado es: {formula:.2f}")