
#quiero crerar una lista de compras

lista_compras = [] #creo una lista vacia
while True: #ejecuto un bucle infinito para que se cumpla hasta que el usuario decida salir
    
    #pido al usuario que ingrese un producto
    producto = input("Ingrese un producto para añadir a su lista de compras, si desea salir, escriba 'salir': ")
    if producto.lower() == 'salir':
        break

    lista_compras.append(producto)#agrego el producto a la lista
print(" Lista de productos:") 

for cosas in lista_compras: #recorro la lista e imprimo cada elemento
    print(f"- {cosas}")
