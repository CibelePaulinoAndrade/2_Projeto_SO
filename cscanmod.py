<<<<<<< HEAD
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
	volta = goDirection(entrada, 0, maisproximo, 1, time)
	totalTime += ida[1] +  abs(entrada[len(entrada)-1] - entrada[0])*time + volta[1]
	total += ida[2] + abs(entrada[len(entrada)-1] - entrada[0])+ volta[2]
	
	mediaDesloc = total/len(entrada)
	mediaTime = totalTime/len(entrada)

	desloclist += ida[0] + [abs(entrada[len(entrada)-1] - entrada[0])] + volta[0]
	va = variancia(desloclist, mediaDesloc)

	timelist += ida[0] + [abs(entrada[len(entrada)-1] - entrada[0])*time] + volta[0]
	vat = variancia(timelist, mediaTime, time)

	texto = "SCAN-C"+"\n"+"Deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTime)+"\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))

	arq.write(texto)
	arq.close()

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

	
	texto = "SCAN-C"+"\n"+"Deslocamentos: "+ str(total)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTime)+ "\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))

	arq.write(texto)
	arq.close()
=======
import math

def cscan(valorinicial, tempo_seek, clusters):

    totaldeslocamento = 0
    varianciadeslocamentos = 0
    n = len(clusters)
    auxiliar = clusters[:]
    auxiliar2 = []

    auxiliar.sort()
    proximo = min(auxiliar, key=lambda x: abs(x - valorinicial))

    fim = len(auxiliar) - 1

    if proximo > valorinicial:
        anterior = auxiliar.index(proximo) - 1
        totaldeslocamento = abs(valorinicial - auxiliar[fim]) + abs(auxiliar[fim] - auxiliar[0]) + abs(auxiliar[0] - auxiliar[anterior])
        anterior += 1

    if proximo < valorinicial:
        anterior = auxiliar.index(proximo) + 1
        totaldeslocamento = abs(valorinicial - auxiliar[0]) + abs(auxiliar[0] - auxiliar[fim]) + abs(auxiliar[fim] - auxiliar[anterior])
        anterior -= 1

    mediadeslocamento = totaldeslocamento / n

    if proximo > valorinicial:
        for i in range(anterior,fim+1):
            auxiliar2.append(auxiliar[i])
        for i in range(anterior):
            auxiliar2.append(auxiliar[i])

    if proximo < valorinicial:
        for i in range(anterior,-1,-1):
            auxiliar2.append(auxiliar[i])
        for i in range(fim,anterior,-1):
            auxiliar2.append(auxiliar[i])

    for i in range(len(auxiliar2)-1):
        varianciadeslocamentos += (abs(auxiliar2[i] - auxiliar[i+1]) - mediadeslocamento)**2
        

    varianciadeslocamentos = varianciadeslocamentos / n
    
    print(len(auxiliar2))
    print(auxiliar2)
    print(auxiliar)
	
    print('Total: ',totaldeslocamento)
    print('Media: ',mediadeslocamento)
    print('Variancia: ',varianciadeslocamentos)
    print('Desvio: ',math.sqrt(varianciadeslocamentos))
    
    f = open('Final.txt', 'w')
    f.write("Teste")
    f.close()


f = open('ACESSOS_100.txt', 'r')
linha = f.read()
f.close()

clusters = linha.split('-')
clusters.remove('')
clusters = [int(x) for x in clusters]


cscan(3000,1,clusters)


>>>>>>> c92251f7651ae226b38aded76ae05ab4e911ac6b
