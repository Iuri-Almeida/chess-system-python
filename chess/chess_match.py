from typing import List, Union

from boardgame.board import Board
from boardgame.piece import Piece
from boardgame.position import Position
from chess.chess_exception import ChessException
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

    def perform_chess_move(self, source_position: ChessPosition, target_position: ChessPosition) -> ChessPiece:

        source: Position = source_position.to_position()
        target: Position = target_position.to_position()

        self.validate_source_position(source)

        captured_piece = self.make_move(source, target)

        return captured_piece

    def make_move(self, source: Position, target: Position) -> Piece:

        piece: Piece = self.__board.remove_piece(source)
        captured_piece: Piece = self.__board.remove_piece(target)

        self.__board.place_piece(piece, target)

        return captured_piece

    def validate_source_position(self, position: Position) -> None:

        if not self.__board.there_is_a_piece(position):
            raise ChessException('There is no piece on source position.')

        if not self.__board.piece_by_position(position).is_there_any_possible_move():
            raise ChessException('There is no possible moves for the chosen piece.')

    def place_new_piece(self, column: str, row: int, piece: ChessPiece) -> None:
        self.__board.place_piece(piece, ChessPosition(column, row).to_position())

    def initial_setup(self) -> None:

        # white players
        self.place_new_piece('c', 1, Rook(self.__board, Color.WHITE))
        self.place_new_piece('c', 2, Rook(self.__board, Color.WHITE))
        self.place_new_piece('d', 2, Rook(self.__board, Color.WHITE))
        self.place_new_piece('e', 2, Rook(self.__board, Color.WHITE))
        self.place_new_piece('e', 1, Rook(self.__board, Color.WHITE))
        self.place_new_piece('d', 1, King(self.__board, Color.WHITE))

        # black players
        self.place_new_piece('c', 7, Rook(self.__board, Color.BLACK))
        self.place_new_piece('c', 8, Rook(self.__board, Color.BLACK))
        self.place_new_piece('d', 7, Rook(self.__board, Color.BLACK))
        self.place_new_piece('e', 7, Rook(self.__board, Color.BLACK))
        self.place_new_piece('e', 8, Rook(self.__board, Color.BLACK))
        self.place_new_piece('d', 8, King(self.__board, Color.BLACK))
