class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None

    def __repr__(self):
        return str(self.info) + '-->' + str(self.prox)

class pilha:
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


def iguais(pilha1, pilha2):
    if pilha1.get_tamanho() != pilha2.get_tamanho():
        return f'as pilhas são diferentes'

    else:
        n1 = pilha1.topo
        n2 = pilha2.topo

        while n1 != None:
            if n1.info != n2.info:
                return f'as pilhas são diferentes'
            
            else:
                n1 = n1.prox
                n2 = n2.prox
        
        return f'as pilhas são iguais'
            
            
l = pilha()
l.empilhar(1)
print(l.consultar())
l.empilhar(3)
print(l.consultar())

p = pilha()
p.empilhar(1)
print(p.consultar())
p.empilhar(3)
print(p.consultar())

print(iguais(l, p))