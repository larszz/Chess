import copy

from logic.ChessError import ChessError
from logic.Color import Color
from logic.BoardNavigation import Coordinate, CoordinateDifference, Move
from logic.pieces.MovingChessPiece import MovingChessPiece


class King(MovingChessPiece):


    def __init__(self, color: Color):
        self.color = color
        self.name = "KING"
        self.sign = "♔"


    def is_possible_move(self, move: Move) -> bool:
        try:
            difference = move.get_difference()
            direction = difference.get_direction()
        except ChessError:
            return False
        return (difference.create_as_absolute().get_max_difference() != 0) and (difference == direction)




