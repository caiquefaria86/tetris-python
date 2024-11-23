class Peca:
    def __init__(self):
        self.formato = ""
        self.cor = ""
        self.posicaoX = ""
        self.posicaoY = ""

    def criaAtomo(self):
        print('Atomo criado')
        atomo = "Atomo criado"
        self.criaConjunto(atomo)

    def criaConjunto(self, atomo):
        print('Conjunto criado')
        desenharConjuntoTela(self)

    def desenharConjuntoTela(self):
        print('Conjunto desenhado na tela')