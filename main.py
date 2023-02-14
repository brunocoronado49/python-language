# Hola soy un comentario
print('Hola Mundo')

# Variables
name = 'El porogramador pragmático'
age = 24
salario = 20.000
soltero = False

# Listas
numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numeros1[5]) # accedemos por medio del indice

# Diccionarios
jugador = {
    'Bruno': 10,
    'programador': True,
    'nivel': 100
}
print(jugador['programador']) # accedemos por medio de la llave al valor

# Constantes
PI = 3.14 # se escriben con mayuculas

# Operadores
print(1 + 1)
print(3 - 4)
print(10 * 2)
print(5 / 4)

print(3 == 3)
print(4 == '4')
print(4 != 5)
print(4 < 5)
print(5 >= 6)
 
# Operadores logicos
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Condiciones
autorizado = True
if autorizado:
    print('Puede ingresar')
else:
    print('No puede ingresar')

entero = 100
if entero == 99:
    print('Es 99')
elif entero == 100:
    print('Es 100')
else:
    print('No es ninguno')

color = 'rojo'
match color:
    case 'verde':
        print('Exito!')
    case 'amarillo':
        print('Advertencia!')
    case _:
        print('Error!')

# Funciones
def sumar(primero, segundo):
    return primero + segundo

resultado = sumar(6, 8)
print(resultado)

#? Algoritmo de ordenamiento
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[0]
    izq = []
    der = []

    for i in range(1, len(lista)):
        izq.append(lista[i]) if lista[i] < pivote else der.append(lista[i])
    
    return quicksort(izq) + [pivote] + quicksort(der)

numeros2 = [43, 65, 834, 32, 12, 53, 87, 332, 10, 5, 8]
listaOrdenada = quicksort(numeros2)
print(listaOrdenada)

# Bucles
animales = ['perro', 'gato', 'pez']
for animal in animales:
    print(animal)

def multiplicar(primero, segundo):
    print(primero * segundo)

numeros3 = [43, 65, 834, 32, 12, 53, 87, 332, 10, 5, 8]
for numero in numeros3:
    multiplicar(numero, 2)

num1 = 100
emergencia = 200
while num1 < emergencia:
    print(num1)
    num1 += 1

javascript = {
    'nombre': 'javascript',
    'año': 1995
}

def desc():
    print('%s fue creado en %s' % (javascript['nombre'], javascript['año']))

desc()

# Clases
class Lenguaje:
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    
def descripcion(self):
    print('%s fue creado en %s' % (self.nombre, self.año))

js = Lenguaje('JavaScript', 1995)
js.descripcion()
