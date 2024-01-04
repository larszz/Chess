import unittest

from logic.ChessError import ChessError
from logic.Color import Color
from logic.BoardNavigation import Coordinate, ChessCoordinate, Move
from logic.pieces.Pawn import Pawn
from logic.pieces.Rook import Rook
from tests.BaseChessTest import BaseChessTest


class ChessTestPawn(BaseChessTest):

    def reset_test_pawn(self):
        self.pawn = self.tested_class.create_white()


    def setUp(self) -> None:
        self.tested_class = Pawn
        self.reset_test_pawn()


    def test_move_moved(self):
        self.assertTrue(self.pawn.not_moved)
        self.pawn.move_piece(Move(ChessCoordinate('a2'), ChessCoordinate('a3')))
        self.assertFalse(self.pawn.not_moved)


    def test_move_double_step(self):
        self.reset_test_pawn()
        self.assertFalse(self.pawn.only_double_step)
        self.pawn.move_piece(Move(ChessCoordinate('a2'), ChessCoordinate('a3')))
        self.assertFalse(self.pawn.only_double_step)

        self.reset_test_pawn()
        self.assertFalse(self.pawn.only_double_step)
        self.pawn.move_piece(Move(ChessCoordinate('a2'), ChessCoordinate('a4')))
        self.assertTrue(self.pawn.only_double_step)


    def test_is_valid_move_without_capture(self):
        self.reset_test_pawn()
        self.assertTrue(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'c3')),
                        "Normal step")
        self.assertTrue(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'c4')),
                        "Double step")

        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'c2')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'b2')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'd2')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'b1')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'd1')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'c1')),
                         "Never possible")

        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'e6')),
                         "Wild point without available direction")

        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'b3')),
                         "Only possible when capture")
        self.assertFalse(self.pawn.is_valid_move_without_capture(Move.make_from_chess_coordinates('c2', 'd3')),
                         "Only possible when capture")


    def test_is_valid_move_with_capture(self):
        self.reset_test_pawn()

        self.assertTrue(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'b3')),
                        "Capture left")
        self.assertTrue(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'd3')),
                        "Capture right")

        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'c2')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'b2')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'd2')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'b1')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'd1')),
                         "Never possible")
        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'c1')),
                         "Never possible")

        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'e6')),
                         "Wild point without available direction")

        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'c3')),
                         "Normal step, only possible without capture")
        self.assertFalse(self.pawn.is_valid_move_with_capture(Move.make_from_chess_coordinates('c2', 'c4')),
                         "Double step, only possible without capture")


    def test_moved_over_fields(self):
        self.assertCountEqual(self.pawn.get_moved_over_fields(Move.make_from_chess_coordinates('c2', 'c3')), [],
                              "Normal step")
        self.assertCountEqual(self.pawn.get_moved_over_fields(Move.make_from_chess_coordinates('c2', 'c4')),
                              [ChessCoordinate('c3')], "Double step")
        self.assertCountEqual(self.pawn.get_moved_over_fields(Move.make_from_chess_coordinates('c2', 'b3')), [],
                              "Capture left")
        self.assertCountEqual(self.pawn.get_moved_over_fields(Move.make_from_chess_coordinates('c2', 'd3')), [],
                              "Capture right")

        with self.assertRaises(ChessError):
            self.pawn.get_moved_over_fields(Move.make_from_chess_coordinates('c2', 'c2'))
            self.pawn.get_moved_over_fields(Move.make_from_chess_coordinates('c2', 'c5'))
        pass


if __name__ == '__main__':
    unittest.main()
