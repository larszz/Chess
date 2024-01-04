import unittest

from logic.BoardNavigation import Coordinate, Move
from logic.pieces.Bishop import Bishop
from tests.BaseChessTest import BaseChessTest


# noinspection PyArgumentList
class TestBishop(BaseChessTest):

    def setUp(self) -> None:
        self.tested_class = Bishop

    def test_possible_moves(self):
        start = self.DEFAULT_START_COORDINATE
        piece = self.get_piece_for_testing()
        methods = [piece.is_valid_move_with_capture, piece.is_valid_move_without_capture]
        for m in methods:
            self.assertTrue(m(Move(start, Coordinate(2, 2))), f"Method {m} failed, should be True")
            self.assertTrue(m(Move(start, Coordinate(4, 4))), f"Method {m} failed, should be True")
            self.assertTrue(m(Move(start, Coordinate(2, 4))), f"Method {m} failed, should be True")
            self.assertTrue(m(Move(start, Coordinate(4, 2))), f"Method {m} failed, should be True")

            self.assertFalse(m(Move(start, Coordinate(3, 2))), f"Method {m} failed, should be False")
            self.assertFalse(m(Move(start, Coordinate(3, 4))), f"Method {m} failed, should be False")
            self.assertFalse(m(Move(start, Coordinate(2, 3))), f"Method {m} failed, should be False")
            self.assertFalse(m(Move(start, Coordinate(4, 3))), f"Method {m} failed, should be False")

            self.assertFalse(m(Move(start, Coordinate(1, 8))), f"Method {m} failed, should be False")

            # TODO test absolute random position without direction

            self.assertFalse(m(Move(start, start)), f"Method {m} failed, should be False")


if __name__ == '__main__':
    unittest.main()
