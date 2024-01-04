import unittest

from logic.Color import Color


class TestColor(unittest.TestCase):

    def test_king_row(self):
        self.assertEqual(Color.BLACK.get_king_row(), 0)
        self.assertEqual(Color.WHITE.get_king_row(), 7)


    def test_pawn_row(self):
        self.assertEqual(Color.BLACK.get_pawn_row(), 1)
        self.assertEqual(Color.WHITE.get_pawn_row(), 6)


if __name__ == '__main__':
    unittest.main()
