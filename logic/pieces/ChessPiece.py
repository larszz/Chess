from abc import ABC, abstractmethod

from logic.Color import Color
from logic.BoardNavigation import Coordinate, Move


class ChessPiece(ABC):
    name: str
    sign: str
    color: Color
    COLOR_OFFSET: int = 6


    @abstractmethod
    def __init__(self, color: Color):
        pass


    def get_name(self) -> str:
        return self.name


    def get_sign(self) -> str:
        offset: int = 0
        if self.color == Color.BLACK:
            offset = self.COLOR_OFFSET
        return chr(ord(self.sign) + offset)


    def get_color(self) -> Color:
        return self.color


    def move_piece(self, move: Move):
        pass


    @classmethod
    def create_black(cls):
        return cls(Color.BLACK)


    @classmethod
    def create_white(cls):
        return cls(Color.WHITE)


    def is_valid_move_independent_from_capture(self, move: Move) -> bool:
        raise NotImplementedError


    def is_valid_move_without_capture(self, move: Move) -> bool:
        return self.is_valid_move_independent_from_capture(move)


    def is_valid_move_with_capture(self, move: Move) -> bool:
        return self.is_valid_move_independent_from_capture(move)

    def is_valid_move(self, move: Move) -> bool:
        return self.is_valid_move_without_capture(move) or self.is_valid_move_with_capture(move)


    def is_invalid_move_without_capture(self, move: Move) -> bool:
        return not self.is_valid_move_without_capture(move)


    def is_invalid_move_with_capture(self, move: Move) -> bool:
        return not self.is_valid_move_with_capture(move)

    @abstractmethod
    def get_moved_over_fields(self, move: Move) -> list[Coordinate]:
        raise NotImplementedError
