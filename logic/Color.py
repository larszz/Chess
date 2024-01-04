from enum import Enum

from logic.ChessError import ChessError


class Color(Enum):
    WHITE = 0
    BLACK = 1


    def get_king_row(self) -> int:
        match self:
            case Color.BLACK:
                return 0
            case _:
                return 7


    def get_pawn_row(self) -> int:
        match self:
            case Color.BLACK:
                return 1
            case _:
                return 6


    def get_pawn_moving_direction(self) -> int:
        match self:
            case Color.BLACK:
                return 1
            case Color.WHITE:
                return -1
            case _:
                raise ChessError(f"Color {self} is invalid")


    