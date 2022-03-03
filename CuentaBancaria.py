class CuentaBancaria:
    nombre_banco="Banco Dojo"
    lista_cuentas=[]
    
    def __init__(self, tasa_int, balance):
        self.tasa_int=tasa_int
        self.balance = balance
        CuentaBancaria.lista_cuentas.append(self)
    
    def deposito(self, amount):
        self.balance+=amount
        return self
    def retiro(self, amount):
        if(CuentaBancaria.puede_retirar(self.balance, amount)):
            self.balance-=amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            tarifa=5
            self.balance -= 5
        return self
    
    def transf_dinero(self, otra_cuenta, monto):
        if(CuentaBancaria.puede_retirar(self.balance,monto)):
            self.balance -= monto
            otra_cuenta.balance += monto
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            tarifa = 5
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print(f"nombreBanco:{self.nombre_banco} , tasa:{self.tasa_int}, balance:{self.balance}")
        return self
        
    def generar_interes(self):
        if(CuentaBancaria.balance_es_positivo(self.balance)):
            self.balance = self.balance + self.balance*self.tasa_int/100
        else:
            print(f"Balance negativo, no se puede generar interés")
        return self
        
    #los metodos classmethod funciona para la clase completa sin classmethod solo aplica al objeto
    @classmethod
    def cambio_banco(cls,nombre):
        cls.lista_cuentas=nombre
    
    @classmethod    
    def imprimir_cuentas(cls):
        for cuenta in cls.lista_cuentas:
            print(f"Nombre Banco: {cuenta.nombre_banco}, Tasa:{cuenta.tasa_int}, Balance:{cuenta.balance}")
    
    #aplica una funcionalidad no en base a clase completa ni algun objeto
    #usado para no repetir codigo, para no usar una funcion dentro de otra 
    #vale para pasarle this, class 
    @staticmethod
    def puede_retirar(balance,cantidad_retirar):
        if(balance>cantidad_retirar):
            return True
        else:
            return False
    
    @staticmethod
    def balance_es_positivo(balance):
        if(balance>0):
            return True
        else:
            return False