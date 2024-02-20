# 2. Desenvolva uma classe ContaBancaria:
# Inclua atributos como número da conta, titular e saldo.
# Forneça métodos para depositar, sacar e exibir o saldo.

class ContaBancaria: 
    def __init__(self, numeroConta: int, titular: str, saldo: float):
        self.numeroConta = numeroConta
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor, titular):
        """ Método para depositar valor na conta. """
        self.saldo += valor
        print(f"""Saldo atual da conta: R${self.saldo:.2f}
        Titular da conta: {self.titular}""")

    def sacar(self, valor):
        """ Método para sacar dinheiro na conta. """
        self.saldo -= valor
         print(f"""Saldo atual da conta: R${self.saldo:.2f}
        Titular da conta: {self.titular}""")

    def exibirSaldo(self): 
        """ Método que exibe o saldo atual da conta. """
        print(f"Saldo atual da conta: R${self.saldo:.2f}")