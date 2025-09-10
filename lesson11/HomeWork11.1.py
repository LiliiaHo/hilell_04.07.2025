def prime_generator(end):
    """
    Генератор простих чисел до межі end (включно).

    Аргументи:
        end (int): верхня межа діапазону пошуку простих чисел.

    Повертає:
        generator: послідовність простих чисел від 2 до end.
    """
    def is_prime(n):
        """
        Перевіряє, чи є число n простим.

        Аргументи:
            n (int): число для перевірки.

        Повертає:
            bool: True, якщо n є простим числом, інакше False.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, end + 1):
        if is_prime(num):
            yield num

from inspect import isgenerator

gen = prime_generator(1)


assert isgenerator(gen) == True, "Test0"
assert list(prime_generator(10)) == [2, 3, 5, 7], "Test1"
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], "Test2"
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test3"

print("Ok")
