from typing import List

from chess.chess_piece import ChessPiece
from boardgame.board import Board
from chess.color import Color


class Rook(ChessPiece):

    def __init__(self, board: Board, color: Color) -> None:
        super().__init__(board, color)

    def __str__(self) -> str:
        return 'R'

    def possible_moves(self) -> List[List[bool]]:

        rows: int = self._board.rows
        columns: int = self._board.columns

        mat: List[List[bool]] = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(False)
            mat.append(row)

        return mat
