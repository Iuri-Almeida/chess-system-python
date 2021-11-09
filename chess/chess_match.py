from typing import List, Union

from boardgame.board import Board
from boardgame.position import Position
from chess.chess_piece import ChessPiece
from chess.chess_position import ChessPosition
from chess.color import Color
from chess.pieces.rook import Rook
from chess.pieces.king import King
from chess.chess_constants import ChessConstants


class ChessMatch(object):

    def __init__(self) -> None:
        self.__board = Board(ChessConstants.ROWS, ChessConstants.COLUMNS)
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

    def place_new_piece(self, column: str, row: int, piece: ChessPiece) -> None:
        self.__board.place_piece(piece, ChessPosition(column, row).to_position())

    def initial_setup(self) -> None:
        self.place_new_piece('b', 6, Rook(self.__board, Color.WHITE))
        self.place_new_piece('e', 8, King(self.__board, Color.BLACK))
        self.place_new_piece('e', 1, King(self.__board, Color.WHITE))
        self.place_new_piece('h', 1, Rook(self.__board, Color.BLACK))
