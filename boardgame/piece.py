from typing import Union

from boardgame.position import Position
# from boardgame.board import Board


class Piece(object):

    def __init__(self, board) -> None:
        self.__board = board
        self._position: Union[Position, None] = None

    @property
    def _board(self):
        return self.__board
