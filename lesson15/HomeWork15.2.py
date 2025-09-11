class Fraction:
    """
    Клас для роботи з дробами.

    Атрибути:
        a (int): чисельник
        b (int): знаменник
    """

    def __init__(self, a: int, b: int) -> None:
        """
        Ініціалізація дробу.

        Аргументи:
            a (int): чисельник
            b (int): знаменник
        """
        self.a = a
        self.b = b

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        Множення двох дробів.

        a/b * c/d = (a*c) / (b*d)

        Повертає:
            Fraction: новий дріб
        """
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        Додавання двох дробів.

        a/b + c/d = (a*d + b*c) / (b*d)

        Повертає:
            Fraction: новий дріб
        """
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        Віднімання двох дробів.

        a/b - c/d = (a*d - b*c) / (b*d)

        Повертає:
            Fraction: новий дріб
        """
        return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)

    def __eq__(self, other: "Fraction") -> bool:
        """
        Перевірка рівності дробів.

        a/b == c/d <=> a*d == b*c

        Повертає:
            bool: True, якщо дроби рівні
        """
        return self.a * other.b == self.b * other.a

    def __gt__(self, other: "Fraction") -> bool:
        """
        Перевірка чи більший дріб

        a/b > c/d <=> a*d > b*c

        Повертає:
            bool: True, якщо дріб більший
        """
        return self.a * other.b > self.b * other.a

    def __lt__(self, other: "Fraction") -> bool:
        """
        Перевірка чи меньший дріб

        a/b < c/d <=> a*d < b*c

        Повертає:
            bool: True, якщо дріб меньший
        """
        return self.a * other.b < self.b * other.a

    def __str__(self) -> str:
        """
        Перетворення дробу у формат стрічки

        Повертає:
            str:  у форматі "Fraction: a, b"
        """
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')
