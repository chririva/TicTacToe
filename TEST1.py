from unittest import TestCase
from TicTacToe import TicTacToe


class TestGame(TestCase):
    def test_right_name1(self):
        game = TicTacToe()
        name = 'Bob'
        game.set_name_player1(name)
        self.assertEqual(name, game.get_name_player1())

    def test_right_name2(self):
        game = TicTacToe()
        name = 'Bob'
        game.set_name_player2(name)
        self.assertEqual(name, game.get_name_player2())

    def test_is_free(self):
        game = TicTacToe()
        result = game.is_free(1);
        ex_result = True;
        self.assertEqual(result, ex_result)

    def test_is_free1(self):
        game = TicTacToe()
        game.put_choice(2, 4)
        result = game.is_free(4);
        ex_result = False;
        self.assertEqual(result, ex_result)

