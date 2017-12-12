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

print("Desloc: ", ndesloc)
print("Media Desloc", mediaDesloc)
print("Media time desloc", mediaTempoDesloc)
print("Variancia", va)
print("Desvio", math.sqrt(va))
print("VarianciaTIme ", vat)
print("Desvio Time", math.sqrt(vat))