# conjuntos
print(set())

print(set([5, 2, 5, 1, 1.5]))
print(set((5, 2, 5, 1, 1.5)))
print(set("52511.5"))

conjunto = set([2, 3, 3, 4])
conjunto_2 = set([5, 3, 5, 6])
conjunto_3 = set([4, 2])

print(conjunto)
print(conjunto_2)
print(conjunto_3)

conjunto.add(1)
print(conjunto)

conjunto.remove(1)
print(conjunto)

print(conjunto.intersection(conjunto_2))
print(conjunto_2.issubset(conjunto))
print(conjunto_3.issubset(conjunto))