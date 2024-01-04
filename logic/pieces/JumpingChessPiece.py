from abc import ABC

from logic.BoardNavigation import Coordinate, Move
from logic.pieces.ChessPiece import ChessPiece


class JumpingChessPiece(ChessPiece, ABC):

    def get_moved_over_fields(self, move: Move) -> list[Coordinate]:
        return []
