import math


class Rectangle:
    """
    Клас "Прямокутник", який описує об'єкт з шириною та висотою.
    Дозволяє працювати з площею, порівнювати, додавати та множити прямокутники.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Створює новий прямокутник.

        :param width: ширина прямокутника (int | float)
        :param height: висота прямокутника (int | float)
        """
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        """
        Обчислює площу прямокутника.

        :return: значення площі (width * height)
        """
        return self.width * self.height

    def __str__(self) -> str:
        """
        Представлення прямокутника у вигляді стрічки.

        :return: рядок у форматі "Rectangle(width, height), площа = area"
        """
        return f"Rectangle({self.width}, {self.height}) площа = {self.area}"

    def __eq__(self, other: "Rectangle") -> bool:
        """
        Перевіряє на рівність площі прямокутників.

        :param other: інший прямокутник
        :return: True, якщо площі рівні
        """
        return self.area == other.area

    def __lt__(self, other: "Rectangle") -> bool:
        """
        Перевіряє, чи менша площа даного прямокутника за площу іншого.

        :param other: інший прямокутник
        :return: True, якщо self.area < other.area
        """
        return self.area < other.area

    def __gt__(self, other: "Rectangle") -> bool:
        """
        Перевіряє, чи більша площа даного прямокутника за площу іншого.

        :param other: інший прямокутник
        :return: True, якщо self.area > other.area
        """
        return self.area > other.area

    def __add__(self, other: "Rectangle") -> "Rectangle":
        """
        Додає два прямокутники.

        Площа нового прямокутника = сумі площ обох.
        Одна сторона обирається близькою до квадратного
        кореня з площі => створюється новий екземпляр.

        :param other: інший прямокутник
        :return: новий об'єкт Rectangle
        """
        new_area = self.area + other.area
        side = math.isqrt(new_area)
        return Rectangle(side, new_area / side)

    def __mul__(self, n: float) -> "Rectangle":
        """
        Множить площу прямокутника на число.

        :param n: число (int | float), на яке множиться площа
        :return: новий об'єкт Rectangle з відповідною площею
        """
        new_area = self.area * n
        side = math.isqrt(new_area)
        return Rectangle(side, new_area / side)

    __rmul__ = __mul__


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.area == 8, "Test1"
assert r2.area == 18, "Test2"

r3 = r1 + r2
assert r3.area == 26, "Test3"

r4 = r1 * 4
assert r4.area == 32, "Test4"

assert Rectangle(3, 6) == Rectangle(2, 9), "Test5"
