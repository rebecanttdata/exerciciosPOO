# 3. Herança com animais:
# Crie uma classe base Animal com atributos como nome e idade.
# Derive classes específicas como Cachorro e Gato.
# Adicione métodos que são específicos para cada tipo de animal.

class Animal(): 
    def __init__(self, nome, idade, espécie):
        self.nome = nome
        self.idade = idade

class Gato(Animal):
    def som(self):
        print("MIAU!!")
    def comidaPreferida(self):
        print("Tigela de leite")


class Cachorro(Animal):
    def som(self):
      """ Mostra o som do animal. """
      print("AU AU!!")
    
    def comidaPreferida(self):
        print("Bife suculento")

cachorro = Cachorro('Bidu', 7, 'Cachorro')
gato = Gato('Mingau', 5, 'Gato')
Cachorro.som(cachorro)
Gato.som(gato)