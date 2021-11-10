from typing import List, Union
from os import system

from chess.chess_piece import ChessPiece
from chess.chess_position import ChessPosition
from chess.chess_constants import ChessConstants
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
    def print_match(chess_match: ChessMatch, captured: List[ChessPiece]) -> None:

        game_status: str = ChessConstants.NO_CHECK

        UI.print_board(chess_match.get_pieces())

        print()
        UI.__print_captured_pieces(captured)

        print(f'\nTurn: {chess_match.turn}')

        if not chess_match.checkmate:
            print(f'Waiting player: {chess_match.current_player}')
            if chess_match.check:
                game_status = ChessConstants.CHECK
        else:
            game_status = ChessConstants.CHECKMATE

            player: Color = chess_match.current_player

            print(f'Winner: {ColorConstants.COLOR_YELLOW if player == Color.BLACK else ColorConstants.COLOR_WHITE}'
                  f'{player}{ColorConstants.RESET}')

        print(f'\nGame status: {ColorConstants.COLOR_RED}{game_status}{ColorConstants.RESET}')

    @staticmethod
    def print_board(pieces: List[List[Union[ChessPiece, None]]]) -> None:

        rows: int = len(pieces)
        columns: int = len(pieces[0])

        for i in range(rows):

            print(f'{ColorConstants.COLOR_GREEN}{rows - i} {ColorConstants.RESET}', end='')

            for j in range(columns):

                UI.__print_piece(pieces[i][j], False)

            print()

        print(f'{ColorConstants.COLOR_GREEN}  a b c d e f g h{ColorConstants.RESET}')

    @staticmethod
    def print_board_possible_moves(
            pieces: List[List[Union[ChessPiece, None]]], possible_moves: List[List[bool]]) -> None:

        rows: int = len(pieces)
        columns: int = len(pieces[0])

        for i in range(rows):

            print(f'{ColorConstants.COLOR_GREEN}{rows - i} {ColorConstants.RESET}', end='')

            for j in range(columns):

                UI.__print_piece(pieces[i][j], possible_moves[i][j])

            print()

        print(f'{ColorConstants.COLOR_GREEN}  a b c d e f g h{ColorConstants.RESET}')

    @staticmethod
    def __print_piece(piece: ChessPiece, background: bool) -> None:

        if background:
            print(ColorConstants.BACKGROUND_DARK_BLUE, end='')

        if piece is None:
            print(f'-{ColorConstants.RESET}', end='')
        else:
            if piece.color == Color.WHITE:
                print(f'{ColorConstants.COLOR_WHITE}{piece}{ColorConstants.RESET}', end='')
            else:
                print(f'{ColorConstants.COLOR_YELLOW}{piece}{ColorConstants.RESET}', end='')

        print(' ', end='')

    @staticmethod
    def __print_captured_pieces(captured: List[ChessPiece]) -> None:

        white: List[ChessPiece] = list(filter(lambda x: x.color == Color.WHITE, captured))
        black: List[ChessPiece] = list(filter(lambda x: x.color == Color.BLACK, captured))

        for i in range(len(white)):
            white[i] = str(white[i])

        for i in range(len(black)):
            black[i] = str(black[i])

        print('Captured pieces:')
        print(f'{ColorConstants.COLOR_WHITE}White: {", ".join(white)}{ColorConstants.RESET}')
        print(f'{ColorConstants.COLOR_YELLOW}Black: {", ".join(black)}{ColorConstants.RESET}')
