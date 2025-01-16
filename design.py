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
        print(f"Дизайн {self.style} применен к комнате {room}.")

    def get_palette(self) -> List[str]:
        return self.colors
