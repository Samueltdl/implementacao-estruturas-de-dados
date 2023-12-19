class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

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
            return f'início: {self.ini.info}, fim: {self.fim.info}'
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

x  =filaEncadeada()
print(x.consultar())

x.inserir(1)
print(x.consultar())

x.inserir(1548546)
print(x.consultar())

x.inserir(15)
print(x.consultar())

x.excluir()
print(x.consultar())

x.destruir()
print(x.consultar())