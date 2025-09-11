from typing import Callable
from inspect import isgenerator


def pow(x: int) -> int:
    return x ** 2

def some_gen(begin: int, end: int, func: Callable[[int], int]):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    value = begin
    for _ in range (max(0, end)):
        yield value
        value = func (value)

gen = some_gen(2, 4, pow)


assert isgenerator(gen) == True, "Test1"
assert list(gen) == [2, 4, 16, 256], "Test2"

print("OK")
