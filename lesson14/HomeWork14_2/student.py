from __future__ import annotations
from human import Human


class Student(Human):
    """
    Клас Student успадковує властивості Human
    та додає інформацію про залікову книжку
    """

    record_book: str

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"{super().__str__()} [Record book: {self.record_book}]"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return str(self) == str(other)

    def __hash__(self) -> int:
        return hash(str(self))
