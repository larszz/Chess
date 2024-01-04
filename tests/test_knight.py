import unittest

from logic.ChessBoard import ChessBoard
from logic.BoardNavigation import Coordinate, CoordinateDifference, Move
from logic.pieces.Knight import Knight
from tests.BaseChessTest import BaseChessTest


# noinspection PyArgumentList
class TestKnight(BaseChessTest):

    def setUp(self) -> None:
        self.tested_class = Knight


    def test_possible_moves(self):
        start = Coordinate(3, 3)
        long_diff = [-2, 2]
        short_diff = [-1, 1]
        piece = self.get_piece_for_testing()
        methods_to_test = [piece.is_valid_move_with_capture,
                           piece.is_valid_move_without_capture]
        for method in methods_to_test:
            self.assertFalse(method(Move(start, start)), f"{method}")

            for ld in long_diff:
                for sd in short_diff:
                    self.assertTrue(
                        method(Move(start, start.get_with_added(CoordinateDifference(ld, sd)))))
                    self.assertTrue(
                        method(Move(start, start.get_with_added(CoordinateDifference(sd, ld)))))

            for diffs in [long_diff, short_diff]:
                for diff1 in diffs:
                    for diff2 in diffs:
                        self.assertFalse(
                            method(Move(start, start.get_with_added(CoordinateDifference(diff1, diff1)))))
                        self.assertFalse(
                            method(Move(start, start.get_with_added(CoordinateDifference(diff2, diff2)))))

            self.assertFalse(method(Move.make_from_chess_coordinates('c2', 'e6')),
                             "Wild point without available direction")


    def test_moved_over(self):
        piece = self.get_piece_for_testing()
        for from_row in range(ChessBoard.NUMBER_OF_FIELDS):
            for from_col in range(ChessBoard.NUMBER_OF_FIELDS):
                for to_row in range(ChessBoard.NUMBER_OF_FIELDS):
                    for to_col in range(ChessBoard.NUMBER_OF_FIELDS):
                        move = Move.make_from_tuples((from_row, from_col), (to_row, to_col))
                        self.assertCountEqual(piece.get_moved_over_fields(move), [], f"{move}")


if __name__ == '__main__':
    unittest.main()
