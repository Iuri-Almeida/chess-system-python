from typing import List, Union
from abc import ABC, abstractmethod

from boardgame.position import Position
# from boardgame.board import Board


class Piece(ABC):

    def __init__(self, board) -> None:
        self.__board = board
        self._position: Union[Position, None] = None

    @property
    def _board(self):
        return self.__board

    @abstractmethod
    def possible_moves(self) -> List[List[bool]]:
        pass

    def possible_move(self, position: Position) -> bool:
        return self.possible_moves()[position.row][position.column]

    def is_there_any_possible_move(self) -> bool:

        mat: List[List[bool]] = self.possible_moves()

        row: int = len(mat)
        column: int = len(mat[0])

        for i in range(row):
            for j in range(column):
                if mat[i][j]:
                    return True

        return False
