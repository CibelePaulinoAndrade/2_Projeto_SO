import math

def cscan(valorinicial, tempo_seek, clusters):

    totaldeslocamento = 0
    tempototaldeslocamento = 0
    varianciadeslocamentos = 0
    tempovarianciadeslocamentos = 0
    
    n = len(clusters)
    auxiliar = clusters[:]
    auxiliar2 = []

    auxiliar.sort()
    proximo = min(auxiliar, key=lambda x: abs(x - valorinicial))

    fim = len(auxiliar) - 1

    if proximo > valorinicial:
        anterior = auxiliar.index(proximo) - 1
        totaldeslocamento = abs(valorinicial - auxiliar[fim]) + abs(auxiliar[fim] - auxiliar[0]) + abs(auxiliar[0] - auxiliar[anterior])
        tempototaldeslocamento = abs(valorinicial - auxiliar[fim])*tempo_seek + abs(auxiliar[fim] - auxiliar[0])*tempo_seek + abs(auxiliar[0] - auxiliar[anterior])*tempo_seek
        anterior += 1

    elif proximo < valorinicial:
        anterior = auxiliar.index(proximo) + 1
        totaldeslocamento = abs(valorinicial - auxiliar[0]) + abs(auxiliar[0] - auxiliar[fim]) + abs(auxiliar[fim] - auxiliar[anterior])
        tempototaldeslocamento = abs(valorinicial - auxiliar[0])*tempo_seek + abs(auxiliar[0] - auxiliar[fim])*tempo_seek + abs(auxiliar[fim] - auxiliar[anterior])*tempo_seek
        anterior -= 1

    else:
        totaldeslocamento = abs(auxiliar[0] - auxiliar[fim])      

    mediadeslocamento = totaldeslocamento / n
    tempomediadeslocamento = tempototaldeslocamento / n

    if proximo > valorinicial:
        for i in range(anterior,fim+1):
            auxiliar2.append(auxiliar[i])
        for i in range(anterior):
            auxiliar2.append(auxiliar[i])

    elif proximo < valorinicial:
        for i in range(anterior,-1,-1):
            auxiliar2.append(auxiliar[i])
        for i in range(fim,anterior,-1):
            auxiliar2.append(auxiliar[i])
            
    elif valorinicial == auxiliar[0]:
        for i in range(fim):
            auxiliar2.append(auxiliar[i])
            
    else:
        for i in range(fim,-1,-1):
            auxiliar2.append(auxiliar[i])

    for i in range(len(auxiliar2)-1):
        varianciadeslocamentos += (abs(auxiliar2[i] - auxiliar2[i+1]) - mediadeslocamento)**2
        tempovarianciadeslocamentos += (abs(auxiliar2[i] - auxiliar2[i+1])*tempo_seek - tempomediadeslocamento)**2

    varianciadeslocamentos = varianciadeslocamentos / n
    tempovarianciadeslocamentos = tempovarianciadeslocamentos / n

    print(auxiliar)
    print(auxiliar2)

    texto = "CSCAN"+"\n"+"Deslocamentos: "+ str(totaldeslocamento)+"\n"+"Media Deslocamentos: "+ str(mediadeslocamento)+"\n"+"Variancia: "+ str(varianciadeslocamentos)+"\n" + "Desvio: "+ str(math.sqrt(varianciadeslocamentos))+"\n"+ "Media Time: "+ str(tempomediadeslocamento)+"\n"+ "Variancia Time: "+ str(tempovarianciadeslocamentos)+"\n" +"Desvio Time: "+ str(math.sqrt(tempovarianciadeslocamentos))
    
    f = open('Final.txt', 'w')
    f.write(texto+"\n\n\n"+str(auxiliar2))
    f.close()

valorinicial = int(input("inicio: "))
tempo_seek = int(input("tempo: "))

f = open('ACESSOS_100.txt', 'r')
linha = f.read()
f.close()

clusters = linha.split('-')
clusters.remove('')
clusters = [int(x) for x in clusters]


cscan(valorinicial,tempo_seek,clusters)


