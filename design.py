from abc import ABC, abstractmethod
from typing import List

class Design(ABC):
    def __init__(self, style: str, colors: List[str]) -> None:
        self.style = style
        self.colors = colors

    @abstractmethod
    def apply_to_room(self, room: str) -> None:
        """
        Применение дизайна к комнате.

        :param room: Название комнаты.
        """
        ...

    @abstractmethod
    def get_palette(self) -> List[str]:
        """
        Получение палитры цветов дизайна.

        :return: Список цветов.
        """
        ...

class ModernDesign(Design):
    def apply_to_room(self, room: str) -> None:
        """
        >>> design = ModernDesign("Modern", ["white", "gray", "black"])
        >>> design.apply_to_room("Living Room")
        Applying Modern design to Living Room with colors ['white', 'gray', 'black'].
        """
        print(f"Applying {self.style} design to {room} with colors {self.colors}.")

    def get_palette(self) -> List[str]:
        """
        >>> design = ModernDesign("Modern", ["white", "gray", "black"])
        >>> design.get_palette()
        ['white', 'gray', 'black']
        """
        return self.colors

if __name__ == "__main__":
    import doctest
    doctest.testmod()