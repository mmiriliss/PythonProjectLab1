from abc import ABC, abstractmethod

class Furniture(ABC):
    def __init__(self, material: str, weight: float) -> None:
        if weight <= 0:
            raise ValueError("Вес мебели должен быть положительным числом.")
        self.material = material
        self.weight = weight

    @abstractmethod
    def move(self, new_location: str) -> None:
        """
        Перемещение мебели в новое место.

        :param new_location: Новое местоположение мебели.
        """
        ...

    @abstractmethod
    def get_description(self) -> str:
        """
        Получение описания мебели.

        :return: Описание в виде строки.
        """
        ...

class Chair(Furniture):
    def move(self, new_location: str) -> None:
        print(f"Мебель перемещена в {new_location}.")

    def get_description(self) -> str:
        return f"Мебель из материала {self.material} весом {self.weight} кг."
