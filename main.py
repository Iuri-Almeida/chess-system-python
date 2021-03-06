"""
    Projeto: Jogo de Xadrez em Python

    Autor: Iuri Lopes Almeida

    GitHub: https://github.com/Iuri-Almeida

    Objetivo: Recriar o jogo de xadrez em Python rodando pelo terminal.

    ReferĂȘncia: https://github.com/Iuri-Almeida/chess-system-java
"""
from typing import List

from application.ui import UI

from chess.chess_exception import ChessException
from chess.chess_match import ChessMatch
from chess.chess_piece import ChessPiece
from chess.chess_position import ChessPosition


def main() -> None:

    chess_match = ChessMatch()
    captured: List[ChessPiece] = []

    while not chess_match.checkmate:

        try:
            UI.clear_screen()

            UI.print_match(chess_match, captured)

            source: ChessPosition = UI.read_chess_position('Source: ', chess_match)

            possible_moves = chess_match.possible_moves(source)

            UI.clear_screen()
            UI.print_board_possible_moves(chess_match.get_pieces(), possible_moves)

            target: ChessPosition = UI.read_chess_position('Target: ', chess_match)

            captured_piece: ChessPiece = chess_match.perform_chess_move(source, target)

            if captured_piece is not None:
                captured.append(captured_piece)

            if chess_match.promoted is not None:

                promotion_type: str = input('Enter the piece for promotion (B/N/R/Q): ').upper()

                while not promotion_type == 'B' and not promotion_type == 'N' and\
                        not promotion_type == 'R' and not promotion_type == 'Q':
                    promotion_type = input('Invalid value! Enter the piece for promotion (B/N/R/Q): ').upper()

                chess_match.replace_promoted_piece(promotion_type)

        except (ChessException, ValueError) as e:
            print(e)
            input('\nClick ENTER to continue.')

    UI.clear_screen()
    UI.print_match(chess_match, captured)


if __name__ == '__main__':
    main()
