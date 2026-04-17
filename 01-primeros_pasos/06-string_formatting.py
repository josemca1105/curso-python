# Concatenar strings
name = "Jose"
last_name = "Calderon"
age = 23

# full_name = name + " " + last_name # funcional pero no es buena practica

full_name = f"{name} {last_name}" # mejor practica, mas legible y facil de mantener
message = f"{full_name}, tienes {age} años" # tambien se pueden incluir variables dentro de la cadena

print(message) # Jose Calderon
