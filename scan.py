import math
from general import *
arq = open('testealg.txt', 'w')


inicio = int(input("inicio: "))
time = int(input("time: "))
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

	texto = "SCAN"+"\n"+"Deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTime)+"\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))

	arq.write(texto)
	arq.close()


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

	
	texto = "SCAN"+"\n"+"Deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTime)+ "\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))

	arq.write(texto)
	arq.close()

	