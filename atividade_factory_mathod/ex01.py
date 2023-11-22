from abc import ABC, abstractmethod

class MotorVehicleFactory(ABC):
    @abstractmethod
    def createMotorVehicle(self):
        pass

class MotorVehicle(ABC):
    @abstractmethod
    def build(self):
        pass

class Motorcycle(MotorVehicle):
    def build(self):
        print("Construindo uma motocicleta")

class Car(MotorVehicle):
    def build(self):
        print("Construindo um carro")

class MotorcycleFactory(MotorVehicleFactory):
    def createMotorVehicle(self):
        return Motorcycle()

class CarFactory(MotorVehicleFactory):
    def createMotorVehicle(self):
        return Car()


motorcycle_factory = MotorcycleFactory()
car_factory = CarFactory()

motorcycle = motorcycle_factory.createMotorVehicle()
car = car_factory.createMotorVehicle()

motorcycle.build()
car.build()