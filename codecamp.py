# Paso, indica como rebanar la cadena
palabra = 'python'
paso = palabra[1:6:2] #el ultimo numero es el paso
print(paso) # retorna yhn

# Metodos de cadenas
nombre = 'francisco rangel'
metodoCapitalize = nombre.capitalize()
print(metodoCapitalize)

#? Metodos importantes
# find, index, isalnum, isalpha, isdecimal, 
# lower, upper, isdigit, islower, isupper

# Recibiendo datos del usuario
name = input('Ingresa tu nombre: ')
print(name)

age = int(input('Ingresa tu edad: '))
print(age)

# Operadores
#? Aritmeticos: suma, resta, multiplicacion, division, division entera, exponente y modulo
print(1 + 1)
print(3 - 4)
print(10 * 2)
print(5 / 4)
print( 15 // 7 )
print(4 ** 3) # elebado a la 3
print(5 % 2) # saber si es par o impar
# Pemdas: Parentesis, Exponentes, Multiplicacion, division, suma y resta

# logicos: True, False, and, or y not(tiene mayor prioridad)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

# relacionales:
print(3 == 3)
print(4 == '4')
print(4 != 5)
print(4 < 5)
print(5 >= 6)

# asignacion: +=, -=, *=, /=, //=, **=, %=
edad = 25

edad += 3
print(edad)
edad -= 3
print(edad)
edad *= 3
print(edad)

# Semtencias Condicionales
autorizado = True
if autorizado:
    print('Puede ingresar')
else:
    print('No puede ingresar')


edad = 18
if edad >= 18:
    print('Ya eres mayor de edad')
else:
    print('No eres mayor de edad')

temp = 20
if temp > 30:
    print('Hace mucho calor')
elif temp <= 20:
    print('El clima esta rico')
else:
    print('No se que clima es')

entero = 100
if entero == 99:
    print('Es 99')
elif entero == 100:
    print('Es 100')
else:
    print('No es ninguno')

# Listas (mutables)
numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numeros1[5]) # accedemos por medio del indice

lista = ['a', 1, 'b', 2, True, False]
print(lista)

lista.append('20') # Agregando al final de la lista
lista.insert(1, 'hola') # insertamos por medio del indice
lista.remove(True) # Elmimnamos ppr medio del elemento
lista.index('hola') # conseguimos el indice por medio del elemento 

vocales = ['a', 'e', 'i', 'o', 'u']
print('a' in vocales) # mostramos si el elemento esta en la lista

vocales[2] = 'b' # Para asignarle un nuevo valor al indice
vocales.count('a') # cuantas veces se repite el elemento
vocales.extend(['c', 'd']) # extewndemos la lista
vocales.pop() # elimmina y retorna el elemento
vocales.reverse() # retorna la lista a la inversa
vocales.sort() # ordena la lista

# Tuplas (inmutables)
hola_tupla = (1, 2, 3, 4, 5)

print(hola_tupla[2])
print(3 in hola_tupla)

tupla = ('a', 'b', 'c', 'd')
tupla.index('b')
tupla.count('b')

# Diccionarios: coleccion pares-valor
persona = {
    'nombre': 'Francisco',
    'edad': 25,
    'soltero': False
}

jugador = {
    'Bruno': 10,
    'programador': True,
    'nivel': 100
}
print(jugador['programador']) # accedemos por medio de la llave al valor

edades = {
    'Bruce': 25,
    'Lupita': 26
}

edades['Franco'] = 30 # agrega una nuueva
edades['Bruce'] = 26 # Modifica 

del edades['Franco'] # para eliminar una clave del diccionario

'Bruce' in edades # vemos si existe en el dicc

# Ciclos
#? Ciclos For
for i in range(0, 10):
    print(i)

for char in 'bucle':
    print(char)

for num in [1, 2, 3, 4 ,5]:
    print(num)

letras = {'a': 1, 'b': 2, 'c': 3}
for clave in letras:
    print(clave)

for valor in letras.values():
    print(valor)

for clave, valor in letras.items():
    print(clave, valor)

#? Ciclos While
x = 20
while x < 35:
    print(x)
    x += 3

# Funciones
def mostrar_mensaje():
    print('Hola Mundo')

mostrar_mensaje()

def mostrar_doble(num): # parametros
    print(num * 2)

mostrar_doble(4) # argumentos

def sumar(x, y):
    print(x + y)

sumar(10, 54)

# Funcion con retorno
def otra_suma(x, y):
    return x + y

resultado = otra_suma(4, 5)
print(resultado)

# Recursion
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
fibonacci(5)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n)
# factorial(5) # retorna un error

# Archivos
#? Para abrir archivos se usa 'with'
#? Modos de apretura como segundo parametro:
#? r(read), w(write), a(append - añadir), Agregar un + incluye leer (w+ leer y escribir)
with open('hola.txt', 'r') as archivo:
    for linea in archivo:
        print('Holiiiiiiiii prriiineees')
        print(linea)

notas = {
    'nora': 78,
    'bruce': 32,
    'talia': 321
}

with open('burro.txt', 'w') as escribe:
    for nombre, nota in notas.items():
        escribe.write(nombre + ' - ' + str(nota) + '\n')

