# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
print(shopping_cart)

option = input("Elige una opción (1-6): ")

if option == "1":
    add_product = input("Indique el nombre del producto a agregar: ")
    if add_product not in shopping_cart:
        shopping_cart.append(add_product)
        print("Producto agregado")
        # print(shopping_cart)
    else:
        print(f"{add_product} ya se encuentra agregado al carrito")
        # print(shopping_cart)
elif option == "2":
    remove_product = input("Indique el nombre del producto a eliminar: ")
    if remove_product in shopping_cart:
        shopping_cart.remove(remove_product)
        print("Producto eliminado")
        # print(shopping_cart)
    else:
        print(f"No cuenta con {remove_product} agregado en su carrito")
        # print(shopping_cart)
elif option == "3":
    if len(shopping_cart) > 0:
        print("Carito: ")
        shopping_cart.sort()
        # print(shopping_cart)
    else:
        print("El carrito esta vacio")
elif option == "4":
    search = input("Indique el nombre del producto a buscar: ")
    if search in shopping_cart:
        print(f"El producto {search} se encuentra en la posicion {shopping_cart.index(search) + 1}")
    else:
        print(f"{search} no se encuentra agregado al carrito")
elif option == "5":
    print(f"El carrito cuenta con {len(shopping_cart)} productos agregados")
elif option == "6":
    empty_cart = shopping_cart.clear()
    print("El carrito ha sido vaciado")
    # print(shopping_cart)
else:
    print("Lo siento, no es una opcion valida")
    
print(shopping_cart)