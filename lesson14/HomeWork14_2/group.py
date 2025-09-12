from __future__ import annotations
from student import Student


class GroupLimitError(Exception):
    pass

class Group:
    """
    Клас Group моделює групу студентів і
    реалізує методи для додавання, пошуку,
    видалення та відображення списку студентів
    """
    number: str
    group: set[Student]
    max_students = 10

    def __init__(self, number: str) -> None:
        self.number = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= self.max_students:
            raise GroupLimitError(f"У групі {self.number} не може бути більше ніж {self.max_students} студентів!")
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __len__(self) -> int:
        return len(self.group)

    def __str__(self) -> str:
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"
