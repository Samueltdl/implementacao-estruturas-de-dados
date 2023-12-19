class tabela:
    def __init__(self, tamanhoMax):
        self.chave = [None] * (tamanhoMax + 1)
        self.valor = [None] * (tamanhoMax + 1)
        self.li = 1
        self.ls = tamanhoMax
        self.ini = self.li - 1
        self.fim = self.ls + 1
        self.tamanho = 0

    def vazia(self):
        if self.tamanho == 0:
            return True

        return False

    def cheia(self):
        if self.tamanho == tamanhoMax:
            return True
        
        return False

    def buscar(self, chave):
        return self.buscaLinear(chave)

    def inserir (self, chave, valor):
        posicao = self.buscar(chave)

        if posicao > 0:
            self.valor[posicao] = valor

        elif not self.cheia():
            if self.vazia():
                self
        
        tamanho += 1

    def buscaBinaria(self, chave):
        if not self.vazia():
            ini = self.ini
            fim = self.fim
            while ini <= fim:
                meio = (ini + fim) // 2

                if self.chave[meio] == chave:
                    return meio

                elif self.chave[meio] > chave:
                    fim = meio - 1
                
                else:
                    ini = meio + 1
        
        return 0

    def buscaBinariaRecursiva (self, k, i, f):
        if i == f:
            if self.chave[i] == k:
                return i
            
            else:
                return 0

        m = (i = f) // 2
        if self.chave[m] == k:
            return m
        
        if self.chave[m] < k:
            return self.buscaBinariaRecursiva(k, m + 1, f):

        return self.buscaBinariaRecursiva(k, i, m - 1)