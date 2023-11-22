from abc import ABC, abstractmethod

class FurnitureFactory(ABC):
    @abstractmethod
    def createArmchair(self):
        pass

    @abstractmethod
    def createCoffeeTable(self):
        pass

class Armchair(ABC):
    @abstractmethod
    def sitOn(self):
        pass

class CoffeeTable(ABC):
    @abstractmethod
    def putOn(self):
        pass

class ModernArmchair(Armchair):
    def sitOn(self):
        print("Sentado em uma poltrona moderna")

class ModernCoffeeTable(CoffeeTable):
    def putOn(self):
        print("Colocando algo em uma mesa de café moderna")

class RetroFurnitureFactory(FurnitureFactory):
    def createArmchair(self):
        return ModernArmchair()

    def createCoffeeTable(self):
        return ModernCoffeeTable()


factory = RetroFurnitureFactory()

armchair = factory.createArmchair()
coffee_table = factory.createCoffeeTable()

armchair.sitOn()
coffee_table.putOn()