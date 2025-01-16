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
        """
        >>> chair = Chair("Wood", 5.0)
        >>> chair.move("Living Room")
        Chair made of Wood weighing 5.0kg has been moved to Living Room.
        """
        print(f"Chair made of {self.material} weighing {self.weight}kg has been moved to {new_location}.")

    def get_description(self) -> str:
        """
        >>> chair = Chair("Wood", 5.0)
        >>> chair.get_description()
        'This is a chair made of Wood, weighing 5.0kg.'
        """
        return f"This is a chair made of {self.material}, weighing {self.weight}kg."

if __name__ == "__main__":
    import doctest
    doctest.testmod()