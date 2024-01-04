import unittest

from logic.ChessError import ChessError
from logic.BoardNavigation import Coordinate, ChessCoordinate, Move
from logic.pieces.King import King
from tests.BaseChessTest import BaseChessTest


# noinspection PyArgumentList
class TestKing(BaseChessTest):
    
    def setUp(self) -> None:
        self.tested_class = King

    def test_possible_moves(self):
        row_and_col_value = 3
        start = Coordinate(row_and_col_value, row_and_col_value)
        piece = self.get_piece_for_testing()
        methods_to_test = [piece.is_valid_move_with_capture, piece.is_valid_move_without_capture]
        for method in methods_to_test:
            for row in range(row_and_col_value-1, row_and_col_value+1+1):
                for col in range(row_and_col_value-1, row_and_col_value+1+1):
                    if row != col:
                        move = Move(start, Coordinate(row, col))
                        self.assertTrue(method(Move(start, Coordinate(row, col))), f"{move}")

            invalid_coordinates = ['b7', 'c7', 'd7', 'e7', 'f7', 'b6', 'b5', 'b4', 'b3', 'c3', 'd3', 'e3', 'f3', 'f3', 'f6', 'f5', 'f4', ]
            for c in invalid_coordinates:
                self.assertFalse(method(Move(start, ChessCoordinate(c))))

            self.assertFalse(method(Move(start, start)))
            self.assertFalse(method(Move.make_from_chess_coordinates('c2', 'e6')),
                             "Wild point without available direction")


    def test_moved_over_fields(self):
        row_and_col_value = 3
        piece = self.get_piece_for_testing()
        start = Coordinate(row_and_col_value, row_and_col_value)
        for row in range(row_and_col_value - 1, row_and_col_value + 1 + 1):
            for col in range(row_and_col_value - 1, row_and_col_value + 1 + 1):
                if row != col:
                    destination = Coordinate(row, col)
                    move = Move(start, destination)
                    self.assertCountEqual(piece.get_moved_over_fields(move), [], f"{move}")

        with self.assertRaises(ChessError):
            piece.get_moved_over_fields(Move(start, start))


if __name__ == '__main__':
    unittest.main()
