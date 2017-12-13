import math
from general import *

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

arq = open('testealg.txt', 'w')
texto = "FIFO"+"\n"+"Deslocamentos: "+ str(deslocamentosN)+"\n"+"Media Deslocamentos: "+ str(mediaDesloc)+"\n"+"Variancia: "+ str(va)+"\n" + "Desvio: "+ str(math.sqrt(va))+"\n"+ "Media Time: "+ str(mediaTempoDesloc)+"\n"+ "Variancia Time: "+ str(vat)+"\n" +"Desvio Time: "+ str(math.sqrt(vat))
arq.write(texto)
arq.close()


