import math
from general import *

arq = open('testealg.txt', 'w')

def FIFO():

	inicial = int(input("inicio: "))
	time = int(input("time: "))
	entrada = ler()

	deslocamentos = [abs(inicial - int(entrada[0]))] 
	deslocamentosN = deslocamentos[-1]
	tempoDesloc = deslocamentos[-1] * time

	for i in range(len(entrada) - 1):
		deslocamentos.append(abs(int(entrada[i]) - int(entrada[i + 1])))
		deslocamentosN += deslocamentos[-1]
		tempoDesloc += deslocamentos[-1] * time

	mediaDesloc = deslocamentosN/len(entrada)
	mediaTempoDesloc = tempoDesloc/len(entrada)

	va = variancia(deslocamentos, mediaDesloc)
	vat = variancia(deslocamentos, mediaTempoDesloc, time)

	texto = "FIFO"+"\n"+"Deslocamentos: "+ str(deslocamentosN)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTempoDesloc)+"\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))+"\n\n"
	arq.write(texto)

def SSF():

	inicio = int(input("inicio: "))
	time = int(input("time: "))
	entrada = [inicio] + ler()

	i = 0
	ni = 0
	deslocamentos = []
	ndesloc = 0
	tempodesloc = 0
	tamentrada = len(entrada) - 1
	while len(entrada) > 1:
		ni = prox(entrada, i)
		deslocamentos.append(abs(entrada[i] - entrada[ni]))
		ndesloc += deslocamentos[-1]
		tempodesloc += deslocamentos[-1] * time
		entrada.pop(i)
		if i < ni:
			ni -= 1
		i = ni

	mediaDesloc = ndesloc/float(tamentrada)
	mediaTempoDesloc = tempodesloc/float(tamentrada)

	va = variancia(deslocamentos, mediaDesloc)

	vat = variancia(deslocamentos, mediaTempoDesloc, time)

	texto = "SSF"+"\n"+"Deslocamentos: "+ str(ndesloc)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTempoDesloc)+"\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))+"\n\n"
	arq.write(texto)


FIFO()
SSF()
