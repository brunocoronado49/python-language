# Hola soy un comentario
print('Hola Mundo')

# Variables
name = 'El porogramador pragmático'
age = 24
grados = -5
salario = 20.000
soltero = False

print(name[3])

# Diccionarios
jugador = {
    'Bruno': 10,
    'programador': True,
    'nivel': 100
}
print(jugador['programador']) # accedemos por medio de la llave al valor

# Constantes
PI = 3.14 # se escriben con mayuculas

# Para saber el tipo de valor de una variable se usa type
tipo = type(name)
print(tipo) # retorna <class 'str'>

# Para saber el numero de caracteres de una cadena
cantidad = len(name)
print(cantidad)

# Rebanado, tomar parte de una cadena
pastel = 'python'
pedazo = pastel[2:4]
print(pedazo)

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
