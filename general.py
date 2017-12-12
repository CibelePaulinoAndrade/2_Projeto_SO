def prox(lista, ind):
	menor = 0 if ind!=0 else 1
	for i in range(len(lista)):
		if ind!=i and abs(lista[ind] - lista[i]) < abs(lista[ind] - lista[menor]):
			menor = i
	return menor

def ler():
	f = open("ACESSOS_100.TXT", "r")
	entrada = []
	for line in f:
		entrada += line.split("-")
	entrada.pop(-1)
	for i in range(len(entrada)):
		entrada[i] = int(entrada[i])
	return entrada

def variancia(vetor, media, mult=1):
	sumVariancia = 0
	for i in vetor:
		sumVariancia += (int(i)*mult - media)**2
	return sumVariancia/(len(vetor) - 1) 
