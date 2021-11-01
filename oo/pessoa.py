class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    misael = Mutante(nome='Misael')
    filipe = Homem(misael, nome='Filipe')
    print(Pessoa.cumprimentar(filipe))
    print(id(filipe))
    print(filipe.cumprimentar())
    print(filipe.nome)
    print(filipe.idade)
    for filho in filipe.filhos:
        print(filho.nome)
    filipe.sobrenome = 'Cesario'
    del filipe.filhos
    filipe.olhos = 1
    del filipe.olhos
    print(filipe.__dict__)
    print(misael.__dict__)
    print(Pessoa.olhos)
    print(filipe.olhos)
    print(misael.olhos)
    print(id(Pessoa.olhos), id(filipe.olhos), id(misael.olhos))
    print(Pessoa.metodo_estatico(), filipe.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), filipe.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(misael, Pessoa))
    print(isinstance(misael, Homem))
    print(misael.olhos)
    print(filipe.cumprimentar())
    print(misael.cumprimentar())