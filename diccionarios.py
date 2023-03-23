# diccionarios
diccionario = {1: "Uno", 2: "Dos"}
diccionario[3] = "Tres"
print(diccionario)

dict_lista_tuplas = dict([(1, "Uno"), (2, "Dos"), (3, "Tres")])
print(dict_lista_tuplas)

dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)
print(dict_lista_string)

dict_tipos = {1: "integer", 
              2.2: "float", 
              "texto": "string", 
              (1, 2): "tupla"}

print(dict_tipos)

dict_repeticion = {1: "Primero", 1: "Último"}
print(dict_repeticion)

print(diccionario, 
      diccionario.keys(), 
      diccionario.values(), 
      diccionario.items())

claves = diccionario.values()
print(claves)
diccionario[1] = "One"
print(claves)
diccionario.pop(2)
print(diccionario)