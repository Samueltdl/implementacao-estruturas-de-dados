class pilha:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = [None] * tamanho
        self.lim = tamanho - 1
        self.base = 0
        self.topo = self.base - 1
        self.quantidade = 0

    def get_quantidade(self):
        return self.quantidade
    
    def get_base(self):
        return self.base
    
    def empilha(self, dado):
        if self.topo < self.lim:
            self.topo += 1
            self.vetor[self.topo] = dado
            self.quantidade += 1
        
        else:
            return f'A pilha está cheia.'

    def excluir(self):
        if self.topo >= self.base:
            self.topo -= 1
            self.quantidade -= 1
    
    def consulta(self):
        if self.topo >= self.base:
            return self.vetor[self.topo]
        
    def destruir(self):
        self.topo = self.base - 1
        self.quantidade = 0

def iguais(pilha1, pilha2):
    if pilha1.get_quantidade() != pilha2.get_quantidade():
        return f'As pilhas são diferentes.'
    
    for i in range (pilha1.get_quantidade()):
        if pilha1.consulta(i) != pilha2.consulta(i):
            return f'As pilhas são diferentes.'
        
    return f'As pilhas são iguais.'

x = pilha(3)
x.empilha(1)
x.empilha(10)
x.empilha(4)
print(x.consulta())
print('-' * 20)
x.excluir()
print(x.consulta())
print('-' * 20)
x.empilha(48764736)
print(x.consulta())
print('-' * 20)
x.destruir()
print(x.consulta())