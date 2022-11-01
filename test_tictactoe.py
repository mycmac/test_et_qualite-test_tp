from TicTacToe_2016 import create_grid

import pytest

class test_tictactoe():
    def test_create_grid(self):
        b = create_grid()
        assert b == [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]