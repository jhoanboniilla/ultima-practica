class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)


class Cuenta:
    def __init__(self, numero_cuenta, saldo, limite_credito, tipo_cuenta):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.limite_credito = limite_credito
        self.tipo_cuenta = tipo_cuenta

    def depositar(self, monto):
        self.saldo += monto
        return f"Depósito exitoso. Nuevo saldo: {self.saldo}"

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return f"Retiro exitoso. Nuevo saldo: {self.saldo}"
        else:
            return "Fondos insuficientes para realizar el retiro."

    def transferir(self, otra_cuenta, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            otra_cuenta.saldo += monto
            return f"Transferencia exitosa. Nuevo saldo: {self.saldo}"
        else:
            return "Fondos insuficientes para realizar la transferencia."


class Cliente:
    def __init__(self, nombre, direccion, numero_cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_cuenta = numero_cuenta


class Cajero:
    def __init__(self, banco, nombre, codigo):
        self.banco = banco
        self.nombre = nombre
        self.codigo = codigo

    def mostrar_menu(self):
        print("1. Consultar Saldo")
        print("2. Realizar Depósito")
        print("3. Realizar Retiro")
        print("4. Transferir Fondos")
        print("5. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.consultar_saldo()
            elif opcion == "2":
                self.realizar_deposito()
            elif opcion == "3":
                self.realizar_retiro()
            elif opcion == "4":
                self.transferir_fondos()
            elif opcion == "5":
                print("Gracias por usar nuestro cajero Utesa Mao. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def consultar_saldo(self):
        numero_cuenta = input("Ingrese el número de cuenta: ")
        cliente = self.buscar_cliente_por_cuenta(numero_cuenta)

        if cliente:
            print(f"Saldo actual de {cliente.nombre}: ${cliente.numero_cuenta.saldo}")
        else:
            print("Cliente no encontrado.")

    def realizar_deposito(self):
        numero_cuenta = input("Ingrese el número de cuenta: ")
        cliente = self.buscar_cliente_por_cuenta(numero_cuenta)

        if cliente:
            monto = float(input("Ingrese el monto a depositar: "))
            print(cliente.numero_cuenta.depositar(monto))
        else:
            print("Cliente no encontrado.")

    def realizar_retiro(self):
        numero_cuenta = input("Ingrese el número de cuenta: ")
        cliente = self.buscar_cliente_por_cuenta(numero_cuenta)

        if cliente:
            monto = float(input("Ingrese el monto a retirar: "))
            print(cliente.numero_cuenta.retirar(monto))
        else:
            print("Cliente no encontrado.")

    def transferir_fondos(self):
        numero_cuenta_origen = input("Ingrese el número de cuenta de origen: ")
        cliente_origen = self.buscar_cliente_por_cuenta(numero_cuenta_origen)

        numero_cuenta_destino = input("Ingrese el número de cuenta de destino: ")
        cliente_destino = self.buscar_cliente_por_cuenta(numero_cuenta_destino)

        if cliente_origen and cliente_destino:
            monto = float(input("Ingrese el monto a transferir: "))
            print(cliente_origen.numero_cuenta.transferir(cliente_destino.numero_cuenta, monto))
        else:
            print("Cliente no encontrado.")

    def buscar_cliente_por_cuenta(self, numero_cuenta):
        for cliente in self.banco.clientes:
            if cliente.numero_cuenta.numero_cuenta == numero_cuenta:
                return cliente
        return None



mi_banco = Banco("Mi Banco")


cliente_JoseArmando = Cliente(nombre="JoseArmando", direccion="Calle durte mao", numero_cuenta=Cuenta(numero_cuenta="123456", saldo=1000, limite_credito=500, tipo_cuenta="Corriente"))
cliente_maria = Cliente(nombre="Maria", direccion="Avenida 456", numero_cuenta=Cuenta(numero_cuenta="789012", saldo=1500, limite_credito=1000, tipo_cuenta="Ahorro"))

mi_banco.agregar_cliente(cliente_JoseArmando)
mi_banco.agregar_cliente(cliente_maria)


cajero_automatico = Cajero(banco=mi_banco, nombre="Cajero1", codigo="1234")


cajero_automatico.ejecutar()
1

