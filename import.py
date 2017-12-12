
import matplotlib.pyplot as plt
from random import randint
from timeit import timeit
import threading
import time
import os

class Mpar(threading.Thread):
    def __init__(self, tam):
        threading.Thread.__init__(self)
        self.tam = tam
    def run(self):
        randomList(self.tam)

def grafico(x, y):
    plt.plot(x,y, label = "T / Thread")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure).get_frame().set_alpha(0.5)
    plt.xlabel("N Threads")
    plt.ylabel("Time")
    plt.title("Gerar Listas")
    plt.show()

def randomList(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        lista.append(n)
    return lista

def run(tam, num):
    fim = False
    threads = []
    for i in range(num):
        threads.append( Mpar( int(tam/num) ) )
    for i in range(num):
        threads[i].start()
    while(not fim):
        fim = True
        for i in range(num):
            if(threads[i].isAlive()):
                fim = False
                break
 
if __name__ == "__main__":
    numeroThreads = []
    tempo = []
    for i in range(1, 21):
        tempo.append(timeit("run({},{})".format(10000, i), setup="from __main__ import run", number=1))
    for i in range(1, 21):
        numeroThreads.append(i)
    grafico(numeroThreads, tempo)