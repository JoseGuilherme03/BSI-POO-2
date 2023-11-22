from abc import ABC, abstractmethod


class TransformString(ABC):
    def __init__(self, string):
        self.string = string

    def read(self):
        pass

    @abstractmethod
    def transformString(self):
        pass

    def print(self):
        print(f"* Transformed String: {self.string}")

    def transform(self):
        self.read()
        self.transformString()
        self.print()


class TransformUpper(TransformString):
    def transformString(self):
        self.string = self.string.upper()


class TransformLower(TransformString):
    def transformString(self):
        self.string = self.string.lower()


class TransformReverse(TransformString):
    def transformString(self):
        self.string = self.string[::-1]


def main():
    string = input("* Digite o texto: ")

    print("* Escolha a Formatação: ")
    print("\t1 - Uppercase")
    print("\t2 - Lowercase")
    print("\t3 - Reverse")

    option = int(input("\t> "))
    while option < 1 or option > 3:
        print("* Escolha Inválida!")
        option = int(input("\t> "))

    if option == 1:
        TransformUpper(string).transform()
    elif option == 2:
        TransformLower(string).transform()
    elif option == 3:
        TransformReverse(string).transform()


if __name__ == "__main__":
    main()
