from multiprocessing.sharedctypes import Value
from CuentaBancaria import CuentaBancaria
class User():
    
    def __init__(self, nombre, email,cuentas):
        self.nombre = nombre
        self.email = email
        self.cuentas=cuentas
        #self.cuenta = cuenta #CuentaBancaria(2, 1000)
        

    def hacer_deposito(self, nombrecuenta, monto):
        self.cuentas[nombrecuenta].deposito(monto)
        return self

    def hacer_retiro(self, nombrecuenta, monto):
        self.cuentas[nombrecuenta].retiro(monto)
        return self

    def mostrar_cuentas_usuario(self):
        print("########################################\n")
        print(f"Nombre: {self.nombre}")
        i=1
        for key, Value in self.cuentas.items() :
            print("------------------------------------")
            print("|  Cuenta #"+str(i))
            print(f"|  {key}:\n|  Balance: {Value.balance}, Tasa interés: {Value.tasa_int}")
            print("------------------------------------")
            i+=1
        

    def transf_dinero(self, nombrecuenta, otro_usuario, nombre_cuenta_usuario, monto):
        self.cuentas[nombrecuenta].transf_dinero(
            otro_usuario.cuentas[nombre_cuenta_usuario], monto)
        return self
