class Nodo:
    def __init__(self, info):
        self.info = info
        self.prox = None
        self.ant = None

    def __repr__(self):
        return str(self.info) + '-->' + str(self.prox)
    
    
class ListaEnc:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tam = 0

    def vazia(self):
        if self.tam == 0:
            return True
        
        elif self.tam > 0:
            return False

    def insere(self, pos ,val):

        if pos < 1 or pos > self.tam + 1:
            return False

        if self.inicio == None:
            self.inicio = Nodo(val)
            self.fim = self.inicio
        
        elif pos == 1:
            aux = Nodo(val)
            self.inicio.ant = aux
            aux.prox = self.inicio
            self.inicio = aux

        else:
            aux = self.inicio

            if pos == self.tam + 1:
                while aux.prox != None:
                    aux = aux.prox
                aux.prox = Nodo(val)
                self.fim = aux.prox
                self.fim.ant = aux
            
            else:
                cont = 1
                while cont < pos - 1:
                    aux = aux.prox
                    cont += 1

                n = Nodo(val)
                n.prox = aux.prox
                aux.prox = n
                n.ant = aux
                n.prox.ant = n
        
        self.tam += 1

    def exclui(self, pos):
        if not self.vazia() and pos > 0:
            if pos == 1:
                self.inicio = self.inicio.prox
                if self.inicio:
                    self.inicio.ant = None
                else:
                    self.fim = None
            else:
                i = 1
                aux = self.inicio

                while i < pos and aux:
                    aux = aux.prox
                    i += 1

                if aux:
                    if aux.ant:
                        aux.ant.prox = aux.prox
                    if aux.prox:
                        aux.prox.ant = aux.ant
                    if aux == self.fim:
                        self.fim = aux.ant

    def buscar(self, valor):
        aux = self.inicio

        pos = 1
        while aux != None:
            if aux.info == valor:
                print (pos)
            
            aux = aux.prox
            pos += 1

    def imprimir(self):
        aux = self.inicio

        while aux != None:
            print(aux.info)

            aux = aux.prox

    def consulta (self, pos):
        aux = self.inicio
        cont = 1

        while aux != None and cont <= pos:
            if cont == pos:
                return aux.info
            
            aux = aux.prox
            cont += 1
        
        return False
    
    def destroi (self):
        while self.exclui(1):
            pass
    
    def numeroElementos(self):
        
        aux = self.inicio
        n = 0

        pos = 1
        while aux != None:
            if aux.info != None:
                n += 1
            
            aux = aux.prox
            pos += 1
        
        print(n)

    def imprimeInverso(self):
        aux = self.fim

        while aux != None:
            print(aux.info)
            aux = aux.ant
'''
    ########## não funciona ##########
    def imprimeImparesInverso(self):
        aux = self.fim

        while aux != None:
            if aux % 2 == 0:
                aux = aux.ant
            
            else:
                print(aux.info)
                aux = aux.ant
'''   

'''
    -------------Não consegui fazer funcionar em aula------------

    def buscarecursiva(self, valor, pos, aux):
        if aux != None:
        
            if aux.info == valor:
                return pos
            
            else:
                return self.buscarecursiva(valor, pos + 1, aux.prox)
        
        return False
        
L = ListaEnc()
L.insere(1, 10)
L.insere(2, 20)
L.buscarecursiva(20, 1, L.inicio)
'''

l = ListaEnc()
l.insere(1, 20)
l.insere(2, 2)
l.imprimir()
print(10 * '-')
l.buscar(20)
print(l.consulta(1))
print(10 * '-')
l.numeroElementos()
print(10 * '-')
l.insere(3, 15)
l.insere(4, 5)
l.imprimir()
print(10 * '-')
l.numeroElementos()
print(10 * '-')
#l.exclui(2)
l.imprimir()
print(10 * '-')
l.numeroElementos()
print(10 * '-')
l.exclui(1)
l.imprimir()
print(10 * '-')
l.imprimeInverso()
print(10 * '-')
#l.imprimeImparesInverso()