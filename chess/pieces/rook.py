from chess.chess_piece import ChessPiece
from boardgame.board import Board
from chess.color import Color


class Rook(ChessPiece):

    def __init__(self, board: Board, color: Color) -> None:
        super().__init__(board, color)

    def __str__(self) -> str:
        return 'R'
