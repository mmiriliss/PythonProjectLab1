from abc import ABC, abstractmethod

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

        Пример:
        >>> class CargoShip(Ship):
        ...     def sail(self, destination: str) -> None:
        ...         print(f"Корабль '{self.name}' отправляется в {destination}.")
        ...
        >>> ship = CargoShip(name="Титан", tonnage=5000)
        >>> ship.sail("Сингапур")
        Корабль 'Титан' отправляется в Сингапур.
        """
        pass

    @abstractmethod
    def dock(self) -> None:
        """
        Швартует корабль.

        Пример:
        >>> class CargoShip(Ship):
        ...     def dock(self) -> None:
        ...         print(f"Корабль '{self.name}' пришвартован.")
        ...
        >>> ship = CargoShip(name="Титан", tonnage=5000)
        >>> ship.dock()
        Корабль 'Титан' пришвартован.
        """
        pass

    @abstractmethod
    def load_cargo(self, weight: float) -> None:
        """
        Загружает груз на корабль.

        :param weight: Вес груза в тоннах.
        :type weight: float
        :raises ValueError: Если вес превышает грузоподъемность корабля.

        Пример:
        >>> class CargoShip(Ship):
        ...     def load_cargo(self, weight: float) -> None:
        ...         print(f"Загружено {weight} тонн.")
        ...
        >>> ship = CargoShip(name="Титан", tonnage=5000)
        >>> ship.load_cargo(3000)
        Загружено 3000 тонн.
        """
        pass
