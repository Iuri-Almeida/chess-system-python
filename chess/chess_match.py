from typing import List, Union

from boardgame.board import Board
from chess.chess_piece import ChessPiece
from chess.color import Color
from boardgame.position import Position
from chess.pieces.rook import Rook
from chess.pieces.king import King


class ChessMatch(object):

    def __init__(self) -> None:
        self.__board = Board(8, 8)
        self.initial_setup()

    def get_pieces(self) -> List[List[Union[ChessPiece, None]]]:

        rows = self.__board.rows
        columns = self.__board.columns

        pieces: List[List[Union[ChessPiece, None]]] = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(None)
            pieces.append(row)

        for i in range(rows):
            for j in range(columns):
                pieces[i][j] = self.__board.piece_by_row_and_column(i, j)

        return pieces

    def initial_setup(self) -> None:
        self.__board.place_piece(Rook(self.__board, Color.WHITE), Position(2, 1))
        self.__board.place_piece(King(self.__board, Color.BLACK), Position(0, 4))
        self.__board.place_piece(King(self.__board, Color.WHITE), Position(7, 4))
