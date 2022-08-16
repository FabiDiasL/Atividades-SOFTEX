class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

raiz = NodoArvore(45)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.esquerda.direita = NodoArvore(30)
raiz.direita.direita = NodoArvore(81)
raiz.direita.direita.direita = NodoArvore(97)
raiz.direita.direita.direita.direita = NodoArvore(100)
raiz.esquerda.esquerda = NodoArvore(4)
raiz.esquerda.direta = NodoArvore(7)
raiz.esquerda.direta.direita = NodoArvore(8)
print("Árvore: ", raiz)

def em_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    em_ordem(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.chave),

    # Visita filho da direita.
    em_ordem(raiz.direita)
    