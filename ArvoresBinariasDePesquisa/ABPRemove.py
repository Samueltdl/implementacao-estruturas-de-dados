class Nodo:
    def __init__(self, chave, valor, esq = None, dir = None, pai = None):
        self.chave = chave
        self.valor = valor
        self.filhoesq = esq
        self.filhodir = dir
        self.pai = pai
    
    def prefixesq(self):
        print(self.info)
        if self.filhoesq:
            self.filhoesq.prefixesq()
        if self.filhodir:
            self.filhodir.prefixesq()

    def prefixdir(self):
        print(self.info)
        if self.filhodir:
            self.filhodir.prefixdir()
        if self.filhoesq:
            self.filhoesq.prefixdir()

    def infixesq(self):
        if self.filhoesq:
            self.filhoesq.infixesq()
        print(self.info)
        if self.filhodir:
            self.filhodir.infixesq()

    def infixdir(self):
        if self.filhodir:
            self.filhodir.infixdir()
        print(self.info)
        if self.filhoesq:
            self.filhoesq.infixdir()

    def posfixesq(self):
        if self.filhoesq:
            self.filhoesq.posfixesq()
        if self.filhodir:
            self.filhodir.posfixesq()
        print(self.info)

    def posfixdir(self):
        if self.filhodir:
            self.filhodir.posfixdir()
        if self.filhoesq:
            self.filhoesq.posfixdir()
        print(self.info)
        
class abp:
    def __init__(self):
        self.raiz = None
        self.tam = 0

    def insere (self, chave, valor):
        if self.raiz:
            self.qualLado(chave, valor, self.raiz)

        else:
            self.raiz = Nodo(chave, valor)
        
        self.tam += 1

    def qualLado(self, chave, valor, nodoAtual):
        if chave < nodoAtual.chave:
            if nodoAtual.filhoesq:
                self.qualLado(chave, valor, nodoAtual.filhoesq)
            else:
                nodoAtual.filhoesq = Nodo(chave, valor, pai = nodoAtual)

        else:
            if nodoAtual.filhodir:
                self.qualLado(chave, valor, nodoAtual.filhodir)
            else:
                nodoAtual.filhodir = Nodo(chave, valor, pai = nodoAtual)

    def busca(self, chave):
        if self.raiz:
            response = self.verifica(chave, self.raiz)
            if response:
                return response.valor
            else:
                return None
        else:
            return None
        
    def verifica(self, chave, nodoAtual):
        if not nodoAtual:
            return None
        elif nodoAtual.chave == chave:
            return nodoAtual
        elif chave < nodoAtual.chave:
            return self.verifica(chave,nodoAtual.filhoesq)
        else:
            return self.verifica(chave,nodoAtual.filhodir)  

    def exclui(self, chave):
        if self.raiz:
            self.raiz = self._remove(chave, self.raiz)

    def _remove(self, chave, nodoAtual):
        if not nodoAtual:
            return nodoAtual

        if chave < nodoAtual.chave:
            nodoAtual.filhoesq = self._remove(chave, nodoAtual.filhoesq)
        elif chave > nodoAtual.chave:
            nodoAtual.filhodir = self._remove(chave, nodoAtual.filhodir)
        else:
            # Caso 1: Nó sem filhos ou com um filho
            if not nodoAtual.filhoesq:
                return nodoAtual.filhodir
            elif not nodoAtual.filhodir:
                return nodoAtual.filhoesq

            # Caso 2: Nó com dois filhos
            altura_esq = self._altura(nodoAtual.filhoesq)
            altura_dir = self._altura(nodoAtual.filhodir)
            
            # Verificando qual das subarvores tem maior altura
            if altura_esq > altura_dir:
                nodo_sucessor = self._encontraMaximo(nodoAtual.filhoesq)
                nodoAtual.chave, nodoAtual.valor = nodo_sucessor.chave, nodo_sucessor.valor
                nodoAtual.filhoesq = self._remove(nodo_sucessor.chave, nodoAtual.filhoesq)
            else:
                nodo_sucessor = self._encontraMinimo(nodoAtual.filhodir)
                nodoAtual.chave, nodoAtual.valor = nodo_sucessor.chave, nodo_sucessor.valor
                nodoAtual.filhodir = self._remove(nodo_sucessor.chave, nodoAtual.filhodir)
            self.tam -= 1
        return nodoAtual

    def _altura(self, nodoAtual):
        if not nodoAtual:
            return 0
        return max(self._altura(nodoAtual.filhoesq), self._altura(nodoAtual.filhodir)) + 1

    def _encontraMinimo(self, nodoAtual):
        while nodoAtual.filhoesq:
            nodoAtual = nodoAtual.filhoesq
        return nodoAtual

    def _encontraMaximo(self, nodoAtual):
        while nodoAtual.filhodir:
            nodoAtual = nodoAtual.filhodir
        return nodoAtual



arvore = abp()

arvore.insere(1, "a")
arvore.insere(2, "b")
arvore.insere(10, "c")
arvore.insere(30, "d")
arvore.insere(23, "e")
arvore.insere(20, "f")
arvore.insere(12, "g")
arvore.insere(32, "h")
arvore.insere(9, "i")
#arvore.insere(3, "j")
print(arvore.busca(3))
print(arvore.busca(1))
print(arvore.busca(10))
print(arvore.busca(1))
print(arvore.busca(9))
arvore.exclui(2)
arvore.exclui(1)
arvore.exclui(10)
arvore.exclui(30)
#print(arvore.busca(2))
print(arvore.tam)