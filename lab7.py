#/* Disciplina: Programacao Concorrente */
#/* Prof.: Silvana Rossetto */
#/* Estudante: Mariana Fernandes Cabral */ 
#/* DRE: 121060838 */ 
#/* Laboratório 7: Atividade 5 */


from threading import Thread
from threading import Lock
from numpy import pi
import time

#classe variavel compartilhada
class Variavel():
    def __init__(self):
        self.piT = 0
        self.lock = Lock()
        self.j = 0
        self.erro

    def Leibniz(self):
        self.lock.acquire()
        self.piT += (pow(-1, self.j)*4.0) / (2 * self.j + 1)
        self.j+=1
        self.lock.release()

    def getPi(self):
        return self.piT

    def validarErroRelativo(self):
        valor_pi = pi
        self.erro = (abs(valor_pi - self.piT))/(valor_pi)
        if self.erro > (10) ** (-10)
            print("Erro relativo superior ao toleravel")
            print(self.erro)

#classe da thread
class LeibnizThread(Thread):
    def __init__(self, id, variavel, nthreads, n):
        super().__init__()
        self.threadid = id
        self.variavel = variavel
        self.nthreads = nthreads
        self.n = n

    def run(self):
        print("Thread {} executando", self.threadid)
        for _ in range (self.threadid, self.n, self.nthreads):
            self.variavel.Leibniz()

#fluxo principal
if __name__ == '__main__':
    #cria variavel compartilhada
    var = Variavel()
    #cria e dispara as threads
    print("Insira a quantidade de threads: ")
    qntdthreads = int(input())

    print("Insira o valor de n a ser usado na serie de Leibniz: ")
    nLeibniz = int(input())
    threads = [LeibnizThread(i, var, qntdthreads, nLeibniz) for i in range(qntdthreads)]
    start = time.time()
    for thread in threads:
        thread.start()
    #aguarda as threads terminarem
    for thread in threads:
        thread.join()
    #exibe o valor da variavel
    print("pi = ", var.getPi())    
    print("Resultado das {} threads obtido em {} segundos".format(len(threads), time.time() - start))    
