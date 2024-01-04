import unittest

from logic.ChessError import ChessError
from logic.BoardNavigation import Coordinate, ChessCoordinate, Move
from logic.pieces.Queen import Queen
from tests.BaseChessTest import BaseChessTest


# noinspection PyArgumentList
class TestQueen(BaseChessTest):
    
    def setUp(self) -> None:
        self.tested_class = Queen

    def test_possible_moves(self):
        start = self.DEFAULT_START_COORDINATE
        piece = self.get_piece_for_testing()
        methods_to_test = [piece.is_valid_move_with_capture,
                           piece.is_valid_move_without_capture]
        for method in methods_to_test:
            self.assertTrue(method(Move(start, Coordinate(3, 2))))
            self.assertTrue(method(Move(start, Coordinate(3, 4))))
            self.assertTrue(method(Move(start, Coordinate(2, 3))))
            self.assertTrue(method(Move(start, Coordinate(4, 3))))
            self.assertTrue(method(Move(start, Coordinate(2, 2))))
            self.assertTrue(method(Move(start, Coordinate(2, 4))))
            self.assertTrue(method(Move(start, Coordinate(4, 2))))
            self.assertTrue(method(Move(start, Coordinate(4, 4))))
    
            self.assertFalse(method(Move(start, start)))
    
            invalid_coordinates = self.DEFAULT_START_KNIGHT_MOVES
            for c in invalid_coordinates:
                self.assertFalse(method(Move(start, ChessCoordinate(c))))

            self.assertFalse(method(Move.make_from_chess_coordinates('c2', 'e6')),
                             "Wild point without available direction")


    def test_moved_over_fields(self):

        piece = self.get_piece_for_testing()
        check_list_straight: list = [Coordinate(0, i) for i in range(1, 5)]
        fields_straight = piece.get_moved_over_fields(Move(Coordinate(0, 0), Coordinate(0, 5)))
        self.assertCountEqual(fields_straight, check_list_straight)


        piece = self.get_piece_for_testing()
        check_list_diagonal: list = [Coordinate(i, i) for i in range(1, 5)]
        fields_diagonal = piece.get_moved_over_fields(Move(Coordinate(0, 0), Coordinate(5, 5)))
        self.assertCountEqual(fields_diagonal, check_list_diagonal)


if __name__ == '__main__':
    unittest.main()
