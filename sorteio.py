import copy

class Sorteador:
    def __init__(self):
        self.potes = []

    def inserir_pote(self, pote):
        #if pote
        pass

    def sortear(self, potes, tipo_sorteio):
        ...

    def sortear_libertadores(self):
        tamanho_potes = len(self.potes)
        times_sorteados = []


        if tamanho_potes == 2:
            tamanho_pote_1 = len(self.potes[0])
            tamanho_pote_2 = len(self.potes[1])

            if tamanho_pote_1 == 8 and tamanho_pote_2 == 8:
                pass

class Pote:
    def __init__(self, pote):
        self.pote = pote

pote1 = {
    'Time A' : 'Brasil',
    'Time B' : 'Brasil',
    'Time C' : 'Brasil',
    'Time D' : 'Brasil',
}

pote2 = {
    'Time 1' : 'Argentina',
    'Time 1' : 'Argentina',
    'Time 1' : 'Argentina',
    'Time 1' : 'Argentina',
}