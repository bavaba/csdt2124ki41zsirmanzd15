# test_chess_logic.py in the 'tests' directory

import pytest
from chess_logic import ChessGame


def test_initial_board_setup():
    game = ChessGame()
    assert str(game.board) is not None


def test_invalid_move():
    game = ChessGame()
    assert not game.make_move("invalid move")


def test_valid_move():
    game = ChessGame()
    assert game.make_move("e4")
