class Human:
    """
    Клас Human описує людину та зберігає основну
    інформацію: ім'я, прізвище, вік, стать.
    """

    gender: str
    age: int
    first_name: str
    last_name: str

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}"

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


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
print(gr)


assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert isinstance(gr.find_student("Jobs"), Student) is True, "Метод поиска должен возвращать экземпляр"

gr.delete_student("Taylor")
print(gr)  # Only one student

gr.delete_student("Taylor")  # No error!

try:
    for i in range (1, 12):
        st = Student ("Male", 18+i, f"Name{i}", f"Surname{i}", f"RB{i}")
        gr.add_student(st)
except GroupLimitError as e:
    print("Помилка:", e)
print(gr)
print("Кількість у групі: ", len(gr))


assert len(gr.group) == 10
assert gr.find_student("Surname11") is None
