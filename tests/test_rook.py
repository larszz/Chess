import unittest

from logic.BoardNavigation import Coordinate, Move
from logic.pieces.Rook import Rook
from tests.BaseChessTest import BaseChessTest


# noinspection PyArgumentList
class TestRook(BaseChessTest):

    def setUp(self) -> None:
        self.tested_class = Rook

    def test_possible_moves(self):
        start = Coordinate(3, 3)
        piece = self.get_piece_for_testing()
        methods_to_test = [piece.is_valid_move_with_capture, piece.is_valid_move_without_capture]
        for method in methods_to_test:
            self.assertTrue(method(Move(start, Coordinate(3, 2))))
            self.assertTrue(method(Move(start, Coordinate(3, 0))))
            self.assertTrue(method(Move(start, Coordinate(3, 7))))
            self.assertTrue(method(Move(start, Coordinate(2, 3))))
            self.assertTrue(method(Move(start, Coordinate(0, 3))))
            self.assertTrue(method(Move(start, Coordinate(7, 3))))

            self.assertFalse(method(Move(start, Coordinate(2, 2))))
            self.assertFalse(method(Move(start, Coordinate(4, 4))))
            self.assertFalse(method(Move(start, Coordinate(4, 2))))
            self.assertFalse(method(Move(start, Coordinate(2, 4))))

            self.assertFalse(method(Move(start, Coordinate(0, 8))))

            self.assertFalse(method(Move.make_from_chess_coordinates('c2', 'e6')),
                             "Wild point without available direction")

            self.assertFalse(method(Move(start, start)))


    def test_moved_over_fields(self):
        piece = self.get_piece_for_testing()
        check_list: list = [Coordinate(0, i) for i in range(1, 5)]
        moved_over = piece.get_moved_over_fields(Move(Coordinate(0, 0), Coordinate(0, 5)))
        self.assertCountEqual(moved_over, check_list)


if __name__ == '__main__':
    unittest.main()
