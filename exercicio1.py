# 1. Crie uma classe Carro:
# Adicione atributos como modelo, cor, ano, e preço.
# Implemente métodos para exibir informações do carro e calcular o preço com desconto.

class Carro:
    def __init__(self, modelo: str, cor: str, ano: int, preco: float):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco
    
    def exibirInformacoes(self):
      """ Exibe as informações do carro. """
      print(f"""Modelo: {self.modelo}
                Cor: {self.cor}
                Ano: {self.ano}
                Preço: {self.preco} """)

    def desconto(self):
        """ Mostra o valor do carro com desconto. """
        desconto = self.preco - (self.preco * 0.2)
        print(f'O valor do carro com desconto de 20% é R${desconto:.2f}')


carro1 = Carro('corsa', 'azul', 2008, 20.000)
Carro.exibirInformacoes(carro1)
Carro.desconto(carro1)