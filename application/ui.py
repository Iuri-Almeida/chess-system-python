from typing import List, Union
from os import system

from chess.chess_piece import ChessPiece
from chess.chess_position import ChessPosition
from chess.chess_match import ChessMatch
from chess.color import Color
from application.color_constants import ColorConstants


class UI(object):

    @staticmethod
    def clear_screen() -> None:
        system('clear')

    @staticmethod
    def read_chess_position(txt: str) -> ChessPosition:

        try:
            s: str = input(txt)

            column: str = s[0]
            row: int = int(s[1:])

            return ChessPosition(column, row)
        except RuntimeError:
            raise ValueError('Error reading ChessPosition. Valida values are from a1 to h8.')

    @staticmethod
    def print_match(chess_match: ChessMatch) -> None:

        UI.print_board(chess_match.get_pieces())

        print(f'\nTurn: {chess_match.turn}')
        print(f'Waiting player: {chess_match.current_player}')

    @staticmethod
    def print_board(pieces: List[List[Union[ChessPiece, None]]]) -> None:

        rows: int = len(pieces)
        columns: int = len(pieces[0])

        for i in range(rows):

            print(f'{rows - i} ', end='')

            for j in range(columns):

                UI.print_piece(pieces[i][j], False)

            print()

        print('  a b c d e f g h')

    @staticmethod
    def print_board_possible_moves(
            pieces: List[List[Union[ChessPiece, None]]], possible_moves: List[List[bool]]) -> None:

        rows: int = len(pieces)
        columns: int = len(pieces[0])

        for i in range(rows):

            print(f'{rows - i} ', end='')

            for j in range(columns):

                UI.print_piece(pieces[i][j], possible_moves[i][j])

            print()

        print('  a b c d e f g h')

    @staticmethod
    def print_piece(piece: ChessPiece, background: bool) -> None:

        if background:
            print(ColorConstants.BACKGROUND_DARK_BLUE, end='')

        if piece is None:
            print(f'-{ColorConstants.RESET}', end='')
        else:
            if piece.color == Color.WHITE:
                print(f'{piece}{ColorConstants.RESET}', end='')
            else:
                print(f'{ColorConstants.COLOR_YELLOW}{piece}{ColorConstants.RESET}', end='')

        print(' ', end='')
