from chess.chess_piece import ChessPiece
from boardgame.board import Board
from chess.color import Color


class King(ChessPiece):

    def __init__(self, board: Board, color: Color) -> None:
        super().__init__(board, color)

    def __str__(self) -> str:
        return 'K'
