from math import factorial

def sin_T(x,n):
	''' x es el numero a calcular y 
	n es el numero de factores del polinomio '''
	sumatoria=0
	for i in range(0,n):
		sumatoria+=((((-1)**i)*(pow(x,(2*i)+1)))/(factorial((2*i)+1)))
	return sumatoria

def cos_T(x,n):
	sumatoria=0
	for i in range(0,n):
		sumatoria+=((((-1)**n)*pow(x,2+n))/(factorial(2*n)))
	return sumatoria











