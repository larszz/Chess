from logic.Color import Color
from logic.BoardNavigation import Coordinate, CoordinateDifference, Move
from logic.pieces.MovingChessPiece import MovingChessPiece


class Bishop(MovingChessPiece):


    def __init__(self, color: Color):
        self.color = color
        self.name = "BISHOP"
        self.sign = "♗"


    def is_possible_move(self, move: Move) -> bool:
        return move.get_difference().is_diagonal_direction()
