"""
    Projeto: Jogo de Xadrez em Python

    Autor: Iuri Lopes Almeida

    GitHub: https://github.com/Iuri-Almeida

    Objetivo: Recriar o jogo de xadrez em Python rodando pelo terminal.

    Referência: https://github.com/Iuri-Almeida/chess-system-java
"""
from chess.chess_match import ChessMatch
from application.ui import UI


def main() -> None:

    chess_match = ChessMatch()

    UI.print_board(chess_match.get_pieces())


if __name__ == '__main__':
    main()
