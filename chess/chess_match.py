from typing import List, Union

from boardgame.board import Board
from chess.chess_piece import ChessPiece


class ChessMatch(object):

    def __init__(self) -> None:
        self.__board = Board(8, 8)

    def get_pieces(self) -> List[List[Union[ChessPiece, None]]]:

        rows = self.__board.rows
        columns = self.__board.columns

        pieces: List[List[Union[ChessPiece, None]]] = [[None] * columns] * rows

        for i in range(rows):
            for j in range(columns):
                pieces[i][j] = self.__board.piece_by_row_and_column(i, j)

        return pieces
