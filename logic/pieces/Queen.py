import copy

from logic.ChessError import ChessError
from logic.Color import Color
from logic.BoardNavigation import Coordinate, CoordinateDifference, Move
from logic.pieces.MovingChessPiece import MovingChessPiece


class Queen(MovingChessPiece):


    def __init__(self, color: Color):
        self.color = color
        self.name = "QUEEN"
        self.sign = "♕"


    def is_possible_move(self, move: Move) -> bool:
        diff = move.get_difference()
        return diff.is_straight_direction() or diff.is_diagonal_direction()
