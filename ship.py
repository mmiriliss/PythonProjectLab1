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

class Ship(ABC):
    """
    Абстрактный класс, описывающий корабль.
    """
    def __init__(self, name: str, tonnage: float) -> None:
        """
        Инициализация корабля.

        :param name: Название корабля.
        :type name: str
        :param tonnage: Грузоподъемность корабля в тоннах.
        :type tonnage: float
        :raises ValueError: Если грузоподъемность меньше или равна нулю.
        """
        if tonnage <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом.")
        self.name = name
        self.tonnage = tonnage

    @abstractmethod
    def sail(self, destination: str) -> None:
        """
        Отправляет корабль в пункт назначения.

        :param destination: Название пункта назначения.
        :type destination: str
        """
        pass

    @abstractmethod
    def dock(self) -> None:
        """
        Швартует корабль.
        """
        pass

    @abstractmethod
    def load_cargo(self, weight: float) -> None:
        """
        Загружает груз на корабль.

        :param weight: Вес груза в тоннах.
        :type weight: float
        :raises ValueError: Если вес превышает грузоподъемность корабля.
        """
        pass

class CargoShip(Ship):
    def sail(self, destination: str) -> None:
        """
        >>> ship = CargoShip("Hercules", 10000)
        >>> ship.sail("Port of Shanghai")
        Hercules is sailing to Port of Shanghai.
        """
        print(f"{self.name} is sailing to {destination}.")

    def dock(self) -> None:
        """
        >>> ship = CargoShip("Hercules", 10000)
        >>> ship.dock()
        Hercules has docked.
        """
        print(f"{self.name} has docked.")

    def load_cargo(self, weight: float) -> None:
        """
        >>> ship = CargoShip("Hercules", 10000)
        >>> ship.load_cargo(5000)
        5000 tons of cargo loaded onto Hercules.
        >>> ship.load_cargo(15000)
        Traceback (most recent call last):
        ValueError: Cargo weight exceeds the ship's capacity.
        """
        if weight > self.tonnage:
            raise ValueError("Cargo weight exceeds the ship's capacity.")
        print(f"{weight} tons of cargo loaded onto {self.name}.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()