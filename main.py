from CuentaBancaria import CuentaBancaria
from User import User

cuenta1 = CuentaBancaria(8,8000)
cuenta2 = CuentaBancaria(5,7000)
cuenta3 = CuentaBancaria(2, 4000)
cuenta4 = CuentaBancaria(1, 2000)
# cuenta1.deposito(100).deposito(100).deposito(100).retiro(100).generar_interes().mostrar_info_cuenta()

# cuenta2.deposito(100).deposito(100).retiro(100).retiro(100).retiro(100).retiro(100).generar_interes().mostrar_info_cuenta()

# CuentaBancaria.imprimir_cuentas()

Kenny = User("kenny","kenny.luque.t@uni.pe",{"cuenta_bcp":cuenta1,"cuenta_interbank":cuenta2})
Paul = User("paul", "paul.luque.t@uni.pe",
            {"cuenta_bcp": cuenta3, "cuenta_interbank": cuenta4})


Kenny.mostrar_cuentas_usuario()
Paul.mostrar_cuentas_usuario()

print("**************************\n")

Kenny.transf_dinero("cuenta_bcp",Paul,1005)
Kenny.mostrar_cuentas_usuario()
Paul.mostrar_cuentas_usuario()

# CuentaBancaria.imprimir_cuentas()
# print("=====================")
# for i in range(len(Kenny.cuenta.lista_cuentas)):
#     print(Kenny.cuenta.lista_cuentas[i])