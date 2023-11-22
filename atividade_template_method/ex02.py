from abc import ABC, abstractmethod


class BuyCellPhone(ABC):
    def __init__(self):
        pass

    def selectPhone(self):
        print("* Celular selecionado com sucesso!")

    def packagePhone(self):
        print("* Celular embalado com sucesso!")

    def paymentPhone(self):
        print("* Pagamento realizado com sucesso!")

    def deliveryPhone(self):
        print("* Celular entregue com sucesso!")

    def wantselectPhone(self):
        return False

    def wantDeliveryPhone(self):
        print("* Deseja receber o celular em casa? (s/n)")
        option = str(input("\t> "))

        return True if option == "s" else False

    def buyPhone(self):
        print("* Comprando celular...")
        if self.wantselectPhone():
            self.selectPhone()
        self.packagePhone()
        self.paymentPhone()
        if self.wantDeliveryPhone():
            self.deliveryPhone()
        self.printReceipt()

    @abstractmethod
    def printReceipt(self):
        pass


class BuyOnline(BuyCellPhone):
    def printReceipt(self):
        print("* Compra realizada com sucesso! (Online)")

    def wantselectPhone(self):
        return True


class BuyOffline(BuyCellPhone):
    def printReceipt(self):
        print("* Compra realizada com sucesso! (Offline)")


def main():
    print("Escolha a forma de comprar o celular: ")
    print("\t1 - Online")
    print("\t2 - Offline")

    option = int(input("\t> "))
    while option < 1 or option > 2:
        print("* Escolha Inválida!")
        option = int(input("\t> "))

    if option == 1:
        BuyOnline().buyPhone()
    elif option == 2:
        BuyOffline().buyPhone()


if __name__ == "__main__":
    main()
