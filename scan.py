import math
from general import *

def goDirection(entrada, inicio, limite, passo, time):
	deslocamento = 0
	tempo = 0
	deslocamentos = []
	for i in range(inicio, limite + passo*(-1), passo):
		deslocamentos.append(abs(entrada[i] - entrada[i + 1*passo]))
		deslocamento += deslocamentos[-1]
		tempo += deslocamentos[-1] * time 	
	return [deslocamentos, tempo, deslocamento]


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

	print("desloc:" , total)
	print("time desloc: ", totalTime)
	print("media desloc: ", mediaDesloc)
	print("media tempo: ", mediaTime)
	print("variancia: ", va)
	print("desvio: ", math.sqrt(va))
	print("variancia time: ", vat)
	print("desvio time: ", math.sqrt(vat))
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

	print "desloc:" , total 
	print "time desloc: ", totalTime
	print "media desloc: ", mediaDesloc
	print "media tempo: ", mediaTime
	print "variancia: ", va
	print "desvio: ", math.sqrt(va)
	print "variancia time: ", vat
	print "desvio time: ", math.sqrt(vat)
