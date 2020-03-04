class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo: {} do titular: {}".format(self.__saldo, self.__titular))

    def saca(self, valor):
        if self.__saldo < valor:
            print("Saldo insuficiente para esta operação")
        else:
            self.__saldo -= valor

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)