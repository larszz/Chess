import copy

from logic.Color import Color
from logic.BoardNavigation import Coordinate, CoordinateDifference, Move
from logic.pieces.JumpingChessPiece import JumpingChessPiece
from logic.pieces.MovingChessPiece import MovingChessPiece


class Knight(JumpingChessPiece):


    def __init__(self, color: Color):
        self.color = color
        self.name = "KNIGHT"
        self.sign = "♘"


    def is_possible_move(self, move: Move) -> bool:
        difference: CoordinateDifference = move.get_difference()
        return ((difference.get_absolute_row_diff() == 2) and (difference.get_absolute_col_diff() == 1)) \
            or ((difference.get_absolute_row_diff() == 1) and (difference.get_absolute_col_diff() == 2))
