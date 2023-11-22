from abc import ABC, abstractmethod


class IFurniture(ABC):
    @abstractmethod
    def furnitureFunction(self):
        pass

    @abstractmethod
    def showStyle(self):
        pass


class IFactory(ABC):
    @abstractmethod
    def create_furniture(self, furniture_type):
        pass


class ClassicCabinet(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Classic"


class ContemporaryCabinet(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Contemporary"


class ScandinavianCabinet(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Scandinavian"


class ClassicChair(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Classic"


class ContemporaryChair(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Contemporary"


class ScandinavianChair(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Scandinavian"


class ClassicTable(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Classic"


class ContemporaryTable(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Contemporary"


class ScandinavianTable(IFurniture):
    def furnitureFunction(self):
        return "furninure function"

    def showStyle(self):
        return "Scandinavian"


class FurnitureFactory(IFactory):
    def create_furniture(self, furniture_type):
        furniture_type = furniture_type.lower()
        if furniture_type == "classic cabinet":
            return ClassicCabinet()
        elif furniture_type == "contemporary cabinet":
            return ContemporaryCabinet()
        elif furniture_type == "scandinavian cabinet":
            return ScandinavianCabinet()
        elif furniture_type == "classic chair":
            return ClassicChair()
        elif furniture_type == "contemporary chair":
            return ContemporaryChair()
        elif furniture_type == "scandinavian chair":
            return ScandinavianChair()
        elif furniture_type == "classic table":
            return ClassicTable()
        elif furniture_type == "contemporary table":
            return ContemporaryTable()
        elif furniture_type == "scandinavian table":
            return ScandinavianTable()
        else:
            raise ValueError("Tipo de móvel inválido")


def main():
    factory = FurnitureFactory()

    try:
        furniture = factory.create_furniture("Scandinavian Cabinet")
        print(f"{furniture.__class__.__name__}: type {furniture.showStyle()}")

        furniture = factory.create_furniture("contemporary chair")
        print(f"{furniture.__class__.__name__}: type {furniture.showStyle()}")

        furniture = factory.create_furniture("classic table")
        print(f"{furniture.__class__.__name__}: type {furniture.showStyle()}")

        furniture = factory.create_furniture("classicWindow")
        print(f"{furniture.__class__.__name__}: type {furniture.showStyle()}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
