"""
    Projeto: Jogo de Xadrez em Python

    Autor: Iuri Lopes Almeida

    GitHub: https://github.com/Iuri-Almeida

    Objetivo: Recriar o jogo de xadrez em Python rodando pelo terminal.

    Referência: https://github.com/Iuri-Almeida/chess-system-java
"""
from boardgame.position import Position


def main() -> None:

    pos = Position(3, 4)
    print(pos)


if __name__ == '__main__':
    main()
