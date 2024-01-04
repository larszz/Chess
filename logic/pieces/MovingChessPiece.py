from abc import ABC

from logic.BoardNavigation import Coordinate, CoordinateDifference, Move
from logic.ChessError import ChessError
from logic.pieces.ChessPiece import ChessPiece


class MovingChessPiece(ChessPiece, ABC):

    def get_moved_over_fields(self, move: Move) -> list[Coordinate]:
        if self.is_valid_move_without_capture(move) or self.is_valid_move_with_capture(move):
            return move.get_fields_on_way()
        else:
            raise ChessError(f"{move} not possible, so no moved over fields available")
