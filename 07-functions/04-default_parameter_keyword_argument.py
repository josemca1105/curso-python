# Default parameters: son parametros que tienen un valor por defecto, en caso de que no se le pase un argumento al momento de hacer la llamada a la funcion
def hello(greet="Hola", name="estimado"):
    print(f"{greet}, {name}")

# Keyword arguments: son argumentos que se pasan a la funcion indicando el nombre del parametro al que se le esta asignando un valor, esto permite pasar los argumentos en cualquier orden
hello(name="Jose", greet="Hello")