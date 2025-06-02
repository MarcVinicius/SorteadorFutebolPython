from random import choice

class Sorteador:
    def __init__(self):
        self.potes = []

    # Inserir pote na lista de potes da classe
    def inserir_pote(self, pote):
        self.potes.append(Pote(pote))

    # Verificar qual sorteador foi passado e executar o sorteio
    def sortear(self, tipo_sorteio):
        tamanho_potes = len(self.potes)

        # Verifica se a lista de potes da classe tem potes
        if self.potes:
            if tipo_sorteio == 'libertadores':
                if tamanho_potes == 2:
                    return self.sortear_libertadores()
                
                return 'Nenhum sorteio retornado!'
            
            return 'Nenhum sorteio retornado!'

        else:
            # Retorna uma mensagem de aviso que a lista de potes da classe não tem potes
            return 'Não tem potes para serem sorteados!'

    # Sorteio da libertadores
    def sortear_libertadores(self):
        confrontos = []
        
        # Criando cópia os potes para poder modifica-los
        pote1 = [time for time in self.potes[0].pote.keys()]
        pote2 = [time for time in self.potes[1].pote.keys()]

        #salvando comprimento dos potes
        tamanho_pote_1 = len(self.potes[0].pote)
        tamanho_pote_2 = len(self.potes[1].pote)

        if tamanho_pote_1 == 8 and tamanho_pote_2 == 8:
            for i in range(8):
                time1 = choice(pote1)
                time2 = choice(pote2)

                confrontos.append([time1+' X '+time2])

                pote1.remove(time1)
                pote2.remove(time2)

        return confrontos

class Pote:
    def __init__(self, kwargs):
        self.pote = kwargs

pote_1 = {
    'Palmeiras': 'Brasil',
    'São Paulo': 'Brasil',
    'Racing': 'Argentina',
    'River Plate': 'Argentina',
    'Estudiantes': 'Argentina',
    'Velez Sarsfield': 'Argentina',
    'Internacional': 'Brasil',
    'LDU': 'Equador',
}

pote_2 = {
    'Botafogo': 'Brasil',
    'Penarol': 'Uruguai',
    'Flamengo': 'Brasil',
    'Fortaleza': 'Brasil',
    'Atlético Nacional': 'Colombia',
    'Libertad': 'Paraguai',
    'Universitário': 'Peru',
    'Cerro Porteno': 'Paraguai',
}

sorteio = Sorteador()
sorteio.inserir_pote(pote_1)
sorteio.inserir_pote(pote_2)

sorteio_libertadores = sorteio.sortear('libertadores')

for confronto in sorteio_libertadores:
    print(confronto[0])