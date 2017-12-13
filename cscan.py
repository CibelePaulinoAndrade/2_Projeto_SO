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


