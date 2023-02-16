compras = ["platanos", "manzanas", "leche"]
print("añade a la lista los elementos galletas, zumo")
lista = []
for i in range(2):
    item = input("introduce los elementos: ")
    compras.append(item)

if compras == ["platanos", "manzanas", "leche","galletas", "zumo"]:
    print(compras)
    print(compras [1])
    print(compras [2])
    compras[4] = "zumo de naranaja"
    print(compras)
    compras.remove(compras[4])
    print(compras)
    compras.insert(2,"limones")
    print(compras)
    compras.sort()
    print(compras)
else:
    print("no has introducido el dato pedido")

## if "piano" intrumentos:
# gente = int(input("cuantas personas acudiran al evento: "))
# MAX_INVITADOS = 5
# invitado = []

# if gente > 5:
#      print("solo pueden ser 5 invitados")
# elif:
#      for i in range(gente):#creamos un for para repetir las preguntas
#           nombre = input("introducir un invitado")
#           invitado.append(nombre)#utilizamos append pra  ñadir elementos a la lista

# print(f"lista de invitados: ")
# for i in invitado:
#      print(i)
# else:
#      print("ERROR, Por favor reinicie el programa")


