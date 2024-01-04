import copy

from logic.Color import Color
from logic.BoardNavigation import Coordinate, CoordinateDifference, Move
from logic.pieces.ChessPiece import ChessPiece
from logic.pieces.MovingChessPiece import MovingChessPiece


class Rook(MovingChessPiece):


    def __init__(self, color: Color):
        self.color = color
        self.name = "ROOK"
        self.sign = "♖"


    def is_valid_move_independent_from_capture(self, move: Move) -> bool:
        return move.get_difference().is_straight_direction()







