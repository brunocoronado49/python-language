# import math as mate <= nombre alternativo
# from math import pow <= por ejemplo
import math

exponer = math.pow(9, 2)
print(exponer)

print(math.pi)

# Errores
#? los errores se manejan con un try:, except:
num1 = int(input('Ingresa un numero alv: '))
num2 = int(input('Echame otro numero alv: '))

try:
    resultado = num1 / num2
    print(f'{num1} / {num2} =', resultado)
except ZeroDivisionError as pendejo: # Solo manejamos un tipo de error
    print('tas bien wey alv ', pendejo)
else:
    print('fierro alv') # si no aplica ninguna excepcion
finally:
    print('a pistiiiaaarrr') # Siempre se ejecuta

