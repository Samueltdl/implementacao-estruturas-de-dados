class lista:
    
    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1
        self.quantidade = 0

    def vazia(self):
        if self.ini == -1 or self.fim == -1:
            return True

        else:
            return False 

    def tamanho(self):
        if self.vazia():
            return 0
        else:
            return self.fim - self.ini + 1

    def inserir(self, posicao, dado):
        #verificar se existe espaço e se a posição é válida
        if (self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.tamanho() + 1:
            if self.vazia():
                self.ini = self.max // 2
                self.fim = self.max // 2

            elif self.fim != self.max - 1:
                for i in range(self.fim, self.ini + posicao - 2, -1):
                    self.vetor[i + 1] = self.vetor[i]
                    print('moveu')
                self.fim = self.fim + 1
            
            else: #deslocar para o início
                for i in range(self.ini, self.ini + posicao - 1):
                    self.vetor[i - 1] = self.vetor[i]
                    print('moveu')

                self.ini = self.ini - 1
            
            self.vetor[self.ini + posicao - 1] = dado
            return True
        
        else:
            return False

    def consultar(self, valor):
        if self.vazia():
            return f'Lista vazia'
        
        else:
            for i in range(self.ini, self.fim - 1):
                if self.vetor() == valor:
                    return i - self.ini + 1   

    def imprimir(self):
        if self.vazia():
            return f'Lista vazia'
        
        else:
            for i in range(self.ini, self.fim + 1):
                print(self.vetor[i])

    #essa merda n funciona
    def remove(self, posicao):
        if self.vazia():
            return f'Lista vazia'
        
        elif posicao > self.fim - 1:
            return False
        
        else:
            for i in range(1, 4, 1):
                if self.vetor[i] == posicao:
                    self.vetor = None

x = lista(5)
x.inserir(1, 1)
x.inserir(2, 5)
x.inserir(3, 10)
x.imprimir()
print('-' * 20)
x.remove(2)
x.imprimir()