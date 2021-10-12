class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    misael = Pessoa(nome='Misael')
    filipe = Pessoa(misael, nome='Filipe')
    print(Pessoa.cumprimentar(filipe))
    print(id(filipe))
    print(filipe.cumprimentar())
    print(filipe.nome)
    print(filipe.idade)
    for filho in filipe.filhos:
        print(filho.nome)
    filipe.sobrenome = 'Cesario'
    del filipe.filhos
    print(filipe.__dict__)
    print(misael.__dict__)
