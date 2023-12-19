class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

class pilhaEncadeada:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def vazia(self):
        if self.topo == None:
            return True
        
        else:
            return False

    def get_tamanho(self):
        return self.tamanho

    def empilhar(self, dado):
        novo = Nodo(dado)
        
        if not self.vazia():
            novo.prox = self.topo
        self.topo = novo

        self.tamanho += 1

    def excluir(self):
        if not self.vazia():
            aux = self.topo
            self.topo = aux.prox
            del aux

    def consultar(self):
        if not self.vazia():
            return self.topo.info

    def destruir(self):
        while not self.vazia():
            self.excluir()


class filaEncadeada:
    def __init__(self):
        self.fim = None
        self.ini = None
        self.tam = 0

    def vazia(self):
        if self.ini == None:
            return True
        return False
    
    def consultar(self):
        if not self.vazia():
            return self.ini.info
        else:
            return f'A fila está vazia'
    
    def inserir(self, dado):
        novo = Nodo(dado)
        if self.vazia():
            self.ini = novo
        
        else:
            self.fim.prox = novo
        
        self.fim = novo
        self.tam += 1

    def excluir(self):
        if not self.vazia():
            aux = self.ini    
            self.ini = self.ini.prox
            self.tam -= 1
            del aux
            
        else:
            return f'A fila está vazia'
    
    def destruir(self):
        while not self.vazia():
            self.excluir()
        
        self.tam = 0

    def ordenar_fila(self):
        pord = pilhaEncadeada()
        paux = pilhaEncadeada()

        while not self.vazia():

            if pord.vazia() or pord.consultar() > self.consultar():
                pord.empilhar(self.consultar())
                self.excluir()
            
            else:
                while not pord.vazia() and self.consultar() > pord.consultar():
                    paux.empilhar(pord.consultar())
                    pord.excluir()
                
                pord.empilhar(self.consultar())
                self.excluir()

                while not paux.vazia():
                    pord.empilhar(paux.consultar())
                    paux.excluir()

        while not pord.vazia():
            self.inserir(pord.consultar())
            pord.excluir()