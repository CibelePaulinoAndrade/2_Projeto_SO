import math
from general import *

arq = open('testealg.txt', 'w')

def FIFO(inicio, time):

	entrada = ler()

	deslocamentos = [abs(inicio - int(entrada[0]))] 
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

def SSF(inicio, time):

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

def SCAN(inicio, time):
	def goDirection(entrada, inicio, limite, passo, time):
		deslocamento = 0
		tempo = 0
		deslocamentos = []
		for i in range(inicio, limite + passo*(-1), passo):
			deslocamentos.append(abs(entrada[i] - entrada[i + 1*passo]))
			deslocamento += deslocamentos[-1]
			tempo += deslocamentos[-1] * time 	
		return [deslocamentos, tempo, deslocamento]

	entrada = ler()

	entrada.sort()
	maisproximo = 0
	for i in range(len(entrada)):
		if abs(inicio - entrada[i]) < abs(inicio - entrada[maisproximo]):
			maisproximo = i

	if maisproximo > inicio:
		total = entrada[maisproximo] - inicio
		desloclist = [total]
		totalTime = total*time
		timelist = [totalTime]
		ida = goDirection(entrada, maisproximo, len(entrada), 1, time)
		volta = goDirection(entrada, maisproximo - 1, -1, -1, time)
		totalTime += ida[1] + abs(entrada[-1] - entrada[maisproximo - 1])*time + volta[1]
		total += ida[2] + abs(entrada[-1] - entrada[maisproximo - 1]) +volta[2]
		
		mediaDesloc = total/len(entrada)
		mediaTime = totalTime/len(entrada)

		desloclist += ida[0] + [abs(entrada[-1] - entrada[maisproximo - 1])] + volta[0]
		va = variancia(desloclist, mediaDesloc)

		timelist += ida[0] + [abs(entrada[-1] - entrada[maisproximo - 1])*time] + volta[0]
		vat = variancia(timelist, mediaTime, time)

		texto = "SCAN"+"\n"+"Deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTime)+"\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))+"\\n\n"
		arq.write(texto)

	elif maisproximo < inicio:
		total = inicio - entrada[maisproximo]
		desloclist = [total]
		totalTime = total*time
		timelist = [totalTime]
		ida = goDirection(entrada, maisproximo, -1, -1, time)
		volta = goDirection(entrada, maisproximo + 1, len(entrada), 1, time)
		totalTime += ida[1] + abs(entrada[0] - entrada[maisproximo + 1])*time  + volta[1]
		total += ida[2] + abs(entrada[0] - entrada[maisproximo + 1]) + volta[2]

		mediaDesloc = total/float(len(entrada))
		mediaTime = totalTime/float(len(entrada))

		desloclist += ida[0] + [abs(entrada[0] - entrada[maisproximo + 1])] + volta[0]
		va = variancia(desloclist, mediaDesloc)

		timelist += ida[0] + [abs(entrada[0] - entrada[maisproximo + 1])*time]+ volta[0]
		vat = variancia(timelist, mediaTime, time)
		
		texto = "SCAN"+"\n"+"Deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTime)+ "\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))+"\n\n"
		arq.write(texto)

inicio = int(input("inicio: "))
time = int(input("time: "))

FIFO(inicio, time)
SSF(inicio, time)
SCAN(inicio, time)

arq.close()
