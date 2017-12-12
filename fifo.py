import math
from general import *

inicial = int(input("inicio: "))
time = input("seek: ")
f = open("ACESSOS_100.TXT", "r")
entrada = []
for line in f:
	entrada += line.split("-")
entrada.pop(-1)

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


print("Deslocamentos: ", deslocamentosN)
print("Media Deslocamentos", mediaDesloc)
print("Variancia: ", va)
print("Desvio: ", math.sqrt(va))
print("Media Time: ", mediaTempoDesloc)
print("Variancia time: ", vat)
print("Desvio Time: ", math.sqrt(vat))

