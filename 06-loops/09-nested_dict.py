nested_dict = {
    "Persona 1": {"Nombre": "Jose", "Edad": 24, "Ciudad": "Valencia"},
    "Persona 2": {"Nombre": "Carlos", "Edad": 25, "Ciudad": "Caracas"},
    "Persona 3": {"Nombre": "Antonio", "Edad": 26, "Ciudad": "Puerto"}
}

# print(nested_dict)

for key, value in nested_dict.items():
    print(f"{key}:")
    for subkey, subvalue in value.items():
        print(f"  {subkey}: {subvalue}")
