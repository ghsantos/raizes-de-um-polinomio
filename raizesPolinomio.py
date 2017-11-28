
def divisores(n):
	d = []
	for i in range(abs(n)):
		if(n%(i+1) == 0):
			d.append(i+1)
	
	return d


def divideLists(l1, l2):
	d = []

	for i in l1:
		for j in l2:
			d.append(i/j)
	
	return d


def listInt(lista):
	n = lista.split()
	l = []
	
	for i in n:
		l.append(int(i))
	
	return l


def calcPolinomio(p, x):
	n = 0
	i = 0
	
	while(len(p)>0):
		n = n + p.pop() * (x ** i)
		
		i = i + 1 
	
	return n


def raizesPolinomio(polinomio, divisores):
	r = []
	
	for i in divisores:
		if(calcPolinomio(polinomio.copy(), i) == 0):
			r.append(i)
	
	return r


def briotRuffini(polinomio, raiz):
	r = []
	
	n = polinomio[0]
	r.append(n)
	
	for i in range(len(polinomio)-1):
		n = (n*raiz) + polinomio[i+1]
		r.append(n)
	
	return r


def bhaskara(p):
	x = []
	a, b, c = p[0:3]
	
	d = (((b ** 2) - (4 * a * c)) ** (1/2))
	
	x.append((-b + d) / (2 * a))
	x.append((-b - d) / (2 * a))
	
	return x



polinomio = input('entre com o polinomio (apenas coeficientes): ')

numPolinomio = listInt(polinomio)

print(numPolinomio)


a0 = numPolinomio[len(numPolinomio)-1]
an = numPolinomio[0]

divA0 = divisores(a0)
divAn = divisores(an)

print('\ndivisores de a0: ')
print(divA0)
print('\ndivisores de an: ')
print(divAn)


pSobreQ = divideLists(divA0, divAn)

print('\ndivisores de a0 / divisores de an: ')
print(pSobreQ)

r = raizesPolinomio(numPolinomio, pSobreQ)

print('\nRaizes: ')
print(r)

bRuffini = briotRuffini(numPolinomio, r[0])

print('\nBriot Ruffini: ')
print(bRuffini)

print('\nbhaskara: ')
print(bhaskara(bRuffini))

