from abc import ABC, abstractmethod


class ServiçoDeExecoes(ABC):
    @staticmethod
    @abstractmethod
    def adicionar(descricao):
        pass


class Classe1(ServiçoDeExecoes):
    def __init__(self):
        self.fila = FilaExecoes()

    def adicionar(self, descricao):
        self.fila.adicionar(descricao)


class Classe2(ServiçoDeExecoes):
    def __init__(self):
        self.fila = FilaExecoes()

    def adicionar(self, descricao):
        self.fila.adicionar(descricao)


class Classe3(ServiçoDeExecoes):
    def __init__(self):
        self.fila = FilaExecoes()

    def adicionar(self, descricao):
        self.fila.adicionar(descricao)


class FilaExecoes:
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def printTotal(cls):
        print(f"Total de exceções do dia: {len(cls._table)}\n\n{ 50 * '-'}\n")

    @classmethod
    def print(cls):
        print("-- Fila de Exeções do Dia --\n")
        for key, value in sorted(cls._table.items()):
            print(f"| {key} | {value}")
            print()

    @classmethod
    def adicionar(cls, descricao):
        x = len(cls._table) + 1
        cls._table[x] = descricao


CLASSE1 = Classe1()
CLASSE1.adicionar("EXCEPTION - ...")
CLASSE1.fila.print()
FilaExecoes.printTotal()

CLASSE2 = Classe2()
CLASSE2.adicionar("EXCEPTION - ...")
CLASSE2.fila.print()
FilaExecoes.printTotal()

CLASSE3 = Classe3()
CLASSE3.adicionar("EXCEPTION - ...")
CLASSE3.fila.print()
FilaExecoes.printTotal()
