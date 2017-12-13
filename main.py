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

	texto = "FIFO"+"\n"+"Quantidade de deslocamentos: "+ str(deslocamentosN)+"\n"
	arq.write(texto)
	texto = "Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia Deslocamentos: "+ str(va)+"\n" 
	arq.write(texto)
	texto = "Desvio Padrao Deslocamentos: "+ str(math.sqrt(va))+"\n"+ "Tempo medio de deslocamentos: "+ str(mediaTempoDesloc)+"\n"
	arq.write(texto)
	texto = "Variancia do Tempo de Deslocamento: "+ str(vat)+"\n" +"Desvio Padrao do Tempo de Deslocamento: "+ str(math.sqrt(vat))+"\n\n"
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

	texto = "SSF"+"\n"+"Quantidade de deslocamentos: "+ str(ndesloc)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"
	arq.write(texto)
	texto = "Variancia Deslocamentos: "+ str(va)+"\n" + "Desvio Padrao Deslocamentos: "+ str(math.sqrt(va))+"\n"
	arq.write(texto)
	texto = "Tempo medio de deslocamentos: "+ str(mediaTempoDesloc)+"\n"+ "Variancia do Tempo de Deslocamento: "+ str(vat)+"\n" 
	arq.write(texto)
	texto = "Desvio Padrao do Tempo de Deslocamento: "+ str(math.sqrt(vat))+"\n\n"
	arq.write(texto)

def SCAN(inicio, time):
	
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

		texto = "SCAN"+"\n"+"Quantidade de deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"
		arq.write(texto)
		texto = "Variancia Deslocamentos: "+ str(va)+"\n" + "Desvio Padrao Deslocamentos: "+ str(math.sqrt(va))+"\n"
		arq.write(texto)
		texto = "Tempo medio de deslocamentos: "+ str(mediaTime)+"\n"+ "Variancia do Tempo de Deslocamento: "+ str(vat)+"\n" 
		arq.write(texto)
		texto = "Desvio Padrao do Tempo de Deslocamento: "+ str(math.sqrt(vat))+"\n\n"
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
		
		texto = "SCAN"+"\n"+"Quantidade de deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"
		arq.write(texto)
		texto = "Variancia Deslocamentos: "+ str(va)+"\n" + "Desvio Padrao Deslocamentos: "+ str(math.sqrt(va))+"\n"
		arq.write(texto)
		texto = "Tempo medio de deslocamentos: "+ str(mediaTime)+ "\n"+ "Variancia do Tempo de Deslocamento: "+ str(vat)+"\n" 
		arq.write(texto)
		texto = "Desvio Padrao do Tempo de Deslocamento: "+ str(math.sqrt(vat))+"\n\n"
		arq.write(texto)

def SCANC(inicio, time):

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
		volta = goDirection(entrada, 0, maisproximo, 1, time)
		totalTime += ida[1] +  abs(entrada[len(entrada)-1] - entrada[0])*time + volta[1]
		total += ida[2] + abs(entrada[len(entrada)-1] - entrada[0])+ volta[2]
		
		mediaDesloc = total/len(entrada)
		mediaTime = totalTime/len(entrada)

		desloclist += ida[0] + [abs(entrada[len(entrada)-1] - entrada[0])] + volta[0]
		va = variancia(desloclist, mediaDesloc)

		timelist += ida[0] + [abs(entrada[len(entrada)-1] - entrada[0])*time] + volta[0]
		vat = variancia(timelist, mediaTime, time)

		texto = "SCAN-C"+"\n"+"Quantidade de deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"
		arq.write(texto)
		texto = "Variancia Deslocamentos: "+ str(va)+"\n" + "Desvio Padrao Deslocamentos: "+ str(math.sqrt(va))+"\n"
		arq.write(texto)
		texto = "Tempo medio de deslocamentos: "+ str(mediaTime)+"\n"+ "Variancia do Tempo de Deslocamento: "+ str(vat)+"\n" 
		arq.write(texto)
		texto = "Desvio Padrao do Tempo de Deslocamento: "+ str(math.sqrt(vat))+"\n\n"
		arq.write(texto)

	elif maisproximo < inicio:
		total = inicio - entrada[maisproximo]
		desloclist = [total]
		totalTime = total*time
		timelist = [totalTime]
		ida = goDirection(entrada, maisproximo, -1, -1, time)
		volta = goDirection(entrada, len(entrada)-1, maisproximo, -1, time)
		totalTime += ida[1] + abs(entrada[len(entrada)-1] - entrada[0])*time + volta[1]
		total += ida[2] + abs(entrada[len(entrada)-1] - entrada[0])+ volta[2]

		mediaDesloc = total/float(len(entrada))
		mediaTime = totalTime/float(len(entrada))

		desloclist += ida[0] + [abs(entrada[len(entrada)-1] - entrada[0])]+volta[0]
		va = variancia(desloclist, mediaDesloc)

		timelist += ida[0] + [abs(entrada[len(entrada)-1] - entrada[0])*time]+ volta[0]
		vat = variancia(timelist, mediaTime, time)

		
		texto = "SCAN-C"+"\n"+"Quantidade de deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"
		arq.write(texto)
		texto = "Variancia Deslocamentos: "+ str(va)+"\n" + "Desvio Padrao Deslocamentos: "+ str(math.sqrt(va))+"\n"
		arq.write(texto)
		texto = "Tempo medio de deslocamentos: "+ str(mediaTime)+"\n"+ "Variancia do Tempo de Deslocamento: "+ str(vat)+"\n" 
		arq.write(texto)
		texto = "Desvio Padrao do Tempo de Deslocamento: "+ str(math.sqrt(vat))+"\n\n"
		arq.write(texto)

inicio = int(input("inicio: "))
time = int(input("time: "))

FIFO(inicio, time)
SSF(inicio, time)
SCAN(inicio, time)
SCANC(inicio, time)

arq.close()
