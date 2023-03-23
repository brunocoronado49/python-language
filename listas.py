# listas
lista = [29, True, 3.353, "El numerop de avogadro"]

print(lista) # [29, True, 3.353, "El numerop de avogadro"]
print(lista[-1]) # "El numerop de avogadro"
print(lista[1:3]) # [True, 3.353]

lista[2] = "He cambiado el elemento"

lista[3] = [1,2,3,4]
print(lista)

print(len(lista))

lista_nueva = [1, 2, 3, 4, 5, 6]
lista_nueva.append(3)
print(lista_nueva) # inserta el numero al final

print(lista_nueva.count(3)) # retorna las veces que esta el elemento

print(lista_nueva.index(4)) # retorna el index del elemento

lista_nueva.remove(3) # elimina el primer elemento con el que coincida
print(lista_nueva)