from src import*
from cal import *


try:
	x=int(input('Ingrese un numero a calcular: '))
	n=int(input('Ingrese la cantidad de terminos: '))
	print(sin_T(x,n))
	print(cos_T(x,n))
	
except ValueError:
	print('Error de tipo')

finally:
	print(suma(2,2))
	print(mul(2,2)) 







