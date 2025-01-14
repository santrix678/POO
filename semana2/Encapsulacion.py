class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        return f"Saldo de {self.__titular}: {self.__saldo}"

cuenta = CuentaBancaria("Santiago", 1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(cuenta.mostrar_saldo())
