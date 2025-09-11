class Item:
    """Descriptions of one product."""

    def __init__(self, name: str, price: float,description: str, dimensions: str):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"


class User:
    """Buyer details."""

    def __init__(self, name: str, surname: str, numberphone: str):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return f"{self.name}  {self.surname}"


class Purchase:
    """The order contains a buyer and a list of goods(goods + quantity)"""

    def __init__(self, user: User) -> None:
        self.products: dict[Item, int] = {}
        self.user = user
        self.total = 0

    def add_item(self, item: Item, cnt: int) -> None:
        """Add the product to order."""
        self.products[item] = cnt

    def __str__(self) -> str:
        lines = [f"User: {self.user}", "Items:"]
        for item, cnt in self.products.items():
            lines.append(f"{item.name}: {cnt} pcs.")
        return "\n".join(lines)

    def get_total(self) -> float:
        """Total order amount."""
        return sum(item.price * cnt for item, cnt in self.products.items())


lemon = Item("lemon", 5, "yellow", "small", )
apple = Item("apple", 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)

"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""


assert isinstance(cart.user, User) is True, "Екземпляр класу User"
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, "Повинно залишатися 60!"

cart.add_item(apple, 10)
print(cart)

"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40