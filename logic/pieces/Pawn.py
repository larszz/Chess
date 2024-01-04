import copy

from logic.ChessError import ChessError
from logic.Color import Color
from logic.BoardNavigation import Coordinate, CoordinateDifference, Move
from logic.pieces.MovingChessPiece import MovingChessPiece


# noinspection PyAbstractClass
class Pawn(MovingChessPiece):

    LENGTH_OF_SINGLE_STEP: int = 1
    LENGTH_OF_DIAGONAL_STEP: int = 1
    LENGTH_OF_DOUBLE_STEP: int = 2
    MAX_LENGTH_OF_STEP = max(LENGTH_OF_SINGLE_STEP, LENGTH_OF_DOUBLE_STEP)

    not_moved: bool
    only_double_step: bool

    def __init__(self, color: Color):
        self.color = color
        self.name = "PAWN"
        self.sign = "♙"
        self.not_moved = True
        self.only_double_step = False


    def _get_possible_direction(self):
        row_direction = self.color.get_pawn_moving_direction()
        return CoordinateDifference(row_direction, 0).get_direction()



    def move_piece(self, move: Move):
        if self.is_invalid_move_with_capture(move) and self.is_invalid_move_without_capture(move):
            raise ChessError(f"Move {move} invalid")
        if self.not_moved and move.get_number_of_fields_to_move() == self.LENGTH_OF_DOUBLE_STEP:
            self.only_double_step = True
        else:
            self.only_double_step = False
        self.not_moved = False




    def is_valid_move_without_capture(self, move: Move) -> bool:
        difference = move.get_difference()
        try:
            if difference.get_direction().row_diff != self.color.get_pawn_moving_direction():
                return False
            if difference.create_as_absolute().get_max_difference() > self.MAX_LENGTH_OF_STEP:
                return False
            if (difference.get_max_difference() == self.LENGTH_OF_DOUBLE_STEP) and not self.only_double_step:
                return False
            if difference.col_diff != 0:
                return False
            return True
        except ChessError:
            return False



    def is_valid_move_with_capture(self, move: Move) -> bool:
        difference = move.get_difference()
        try:
            if difference.get_direction().row_diff != self.color.get_pawn_moving_direction():
                return False
            return (difference.create_as_absolute().get_max_difference() == self.LENGTH_OF_DIAGONAL_STEP) and (difference.is_diagonal_direction())
        except ChessError:
            return False
