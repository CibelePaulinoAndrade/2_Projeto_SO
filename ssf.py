import math
from general import *

inicio = int(input("inicio: "))
time = int(input("time: "))
entrada = [inicio] + ler()

i = 0
ni = 0
deslocamentos = []
ndesloc = 0
tempodesloc = 0
tamentrada = len(entrada) - 1
ordem = []
while len(entrada) > 1:
	ni = prox(entrada, i)
	ordem.append(entrada[ni])
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

arq = open('testealg.txt', 'w')
texto = "SSF"+"\n"+"Deslocamentos: "+ str(ndesloc)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTempoDesloc)+"\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))

arq.write(texto)
texto = "Sequencia de Acesso: SSF"+"\n" + str(ordem)+"\n\n"
arq.write(texto)
arq.close()

##print "Desloc: ", ndesloc 
##print "Media Desloc", mediaDesloc 
##print "Media time desloc", mediaTempoDesloc
##print "Variancia", va
##print "Desvio", math.sqrt(va)
##print "VarianciaTIme ", vat
##print "Desvio Time", math.sqrt(vat)
