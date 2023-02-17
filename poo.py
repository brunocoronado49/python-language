# Programacion orientada a objetos (POO)

class CuentaBancaria:
    def __init__(self, num_cuenta, nom_titular, balance):
        self.num_cuenta = num_cuenta
        self.nom_titular = nom_titular
        self.balance = balance
    
    def generar_balance(self):
        print(self.balance)
    
    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(self.balance)

mi_cuenta = CuentaBancaria('105-356-643', 'Bruce Wayne', 5600)
mi_cuenta.generar_balance()
mi_cuenta.depositar(546)
