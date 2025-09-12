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
