inventory = {
    "chocolate": 10,
    "gomitas": 5,
    "paleta": 8,
    "chicle": 2,
    "mexicano": 8,
    "galleta": 12
}

cart = []

print("Bienvenido a la tienda de dulces, DevCandy!")
print("Inventario: ")

for candy, price in inventory.items():
    print(f"{candy.capitalize()} - ${price}")
    
while True:
    choice = input("Que dulces deseas comprar? (Escribe 'salir' para terminar): ").lower()
    
    if choice == "salir":
        break
    
    if choice in inventory:
        cart.append(choice)
        print(f"Agregaste {choice} al carrito.\n")
    
    else:
        print("Lo siento, este dulce no esta en el inventario. Intenta de nuevo por favor.")
        
total = 0
print("\nTu Carrito.")
for candy in cart:
    print(f"{candy.capitalize()} - ${inventory[candy]}")
    total += inventory[candy]
    
print(f"Total a pagar: ${total}")
print("Gracias por tu compra!")