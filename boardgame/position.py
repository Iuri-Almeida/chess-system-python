class Position(object):

    def __init__(self, row: int, column: int) -> None:
        self.__row = row
        self.__column = column

    def __str__(self) -> str:
        return f'{self.row}, {self.column}'

    @property
    def row(self) -> int:
        return self.__row

    @row.setter
    def row(self, new_row: int) -> None:
        self.__row = new_row

    @property
    def column(self) -> int:
        return self.__column

    @column.setter
    def column(self, new_column: int) -> None:
        self.__column = new_column
