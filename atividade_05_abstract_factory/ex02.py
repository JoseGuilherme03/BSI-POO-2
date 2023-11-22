from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self):
        self.name = None

    @abstractmethod
    def initVehicle(self):
        pass

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return f"---- {self.name} ----\n"

class Corporation(ABC):
    @abstractmethod
    def create_vehicle(self, item):
        pass

    def order_vehicle(self, type):
        vehicle = self.create_vehicle(type)
        vehicle.initVehicle()
        return vehicle

class NextGenVehicleCorporation(Corporation):
    def create_vehicle(self, item):
        vehicle = None
        type_factory = NextGenVehicle()

        if item == "moto":
            vehicle = Moto(type_factory)
            vehicle.set_name("Veículo de Próxima Geração - moto")
        elif item == "carroeletrico":
            vehicle = CarroEletrico(type_factory)
            vehicle.set_name("Veículo de Próxima Geração - Carro Elétrico")

        return vehicle

class FutureVehicleCorporation(Corporation):
    def create_vehicle(self, item):
        vehicle = None
        type_factory = FutureVehicle()

        if item == "moto":
            vehicle = Moto(type_factory)
            vehicle.set_name("Veículo do Futuro - moto")
        elif item == "carroeletrico":
            vehicle = CarroEletrico(type_factory)
            vehicle.set_name("Veículo do Futuro - Carro Elétrico")

        return vehicle

class NextGenVehicle:
    def type_vehicle(self):
        return 'Próxima Geração'

class FutureVehicle:
    def type_vehicle(self):
        return 'Futuro'

class Moto(Vehicle):
    def __init__(self, factory):
        self.vehicle_type = factory.type_vehicle()
    
    def initVehicle(self):
        print(f"Inicializando a moto {self.vehicle_type}")

class CarroEletrico(Vehicle):
    def __init__(self, factory):
        self.vehicle_type = factory.type_vehicle()
    
    def initVehicle(self):
        print(f"Inicializando o Carro Elétrico {self.vehicle_type}")


if __name__ == "__main__":
    ng_corporation = NextGenVehicleCorporation()
    print(f'{"* NextGenVehicleCorporation"}\n')
    moto_futuro = ng_corporation.order_vehicle("moto")
    carro_futuro = ng_corporation.order_vehicle("carroeletrico")

    print(f'\n{10*"-----"}\n')

    future_corporation = FutureVehicleCorporation()
    print(f'{"* FutureVehicleCorporation"}\n')
    moto_eletrica = future_corporation.order_vehicle("moto")
    carro_eletrico = future_corporation.order_vehicle("carroeletrico")
