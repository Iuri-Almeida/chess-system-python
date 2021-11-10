"""
    Projeto: Jogo de Xadrez em Python

    Autor: Iuri Lopes Almeida

    GitHub: https://github.com/Iuri-Almeida

    Objetivo: Recriar o jogo de xadrez em Python rodando pelo terminal.

    Referência: https://github.com/Iuri-Almeida/chess-system-java
"""
from chess.chess_match import ChessMatch
from chess.chess_position import ChessPosition
from chess.chess_piece import ChessPiece
from application.ui import UI


def main() -> None:

    chess_match = ChessMatch()

    while True:

        UI.print_board(chess_match.get_pieces())

        source: ChessPosition = UI.read_chess_position('Source: ')
        target: ChessPosition = UI.read_chess_position('Target: ')

        captured_piece: ChessPiece = chess_match.perform_chess_move(source, target)

        print(captured_piece)


if __name__ == '__main__':
    main()
