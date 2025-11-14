#Se le da la bienvenida al usuario
print()
print("="*95)
print("Bienvenido al sistema de inventario, llena correctamente la información que vamos a solicitar")
print("="*95)
#Se solicita al usuario el nombre del objeto a ingresar en el sistema
nombre=input("Ingresa el nombre del objeto que se va a registrar en el sistema: ")
#Se solicita al usuario el precio del producto
#Si el usuario ingresa una información que no es congruente con lo solicitado, se le seguira solicitando
while True:
    precio=input("Ingresa el costo unitario del objeto antes mencionado: ")
    try:
        precio=float(precio)
        break
    except:
        print("El dato ingresado no corresponde con algun precio, intenta de nuevo.")
        continue
#Se solicita al usuario el precio del producto
#Si el usuario ingresa una información que no es congruente con lo solicitado, se le seguira solicitando
while True:
    cantidad=input("Ingresa la candtidad de unidades del objeto antes mencionado: ")
    try:
        cantidad=int(cantidad)
        break
    except:
        print("El dato ingresado no corresponde con la información solicitada, intenta de nuevo.")
        continue
#Se hace el calculo del costo total de todas las unidades del producto, posteriormente se imprime en pantalla toda la informacion solicitadad,
#Ademas, del calculo antes mencionado
costo_total=precio*cantidad
print(f"La información del elemento ingresado es:\nNombre: {nombre}\nPrecio Unitario: {precio}\nCantidad(unidades): {cantidad} \
    \nCosto total calculado: {costo_total:.0f}")
print()




#Este programa tiene la función de registrar un objeto en un sistema de inventario, solicitando al usuario el nombre del objeto,Su precio unitario 
#y la cantidad de unidades, Ademas, de imprimir toda la información ingresada junto con el costo total de todas las unidades del objeto.