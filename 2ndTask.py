import timeit
from functools import partial


class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


class PersonTest:
    __slots__ = ("name", 'address', "email")

    def __init__(self, *args):
        self.name, self.address, self.email = args


def get_set_delete(person):
    a = person.__getattribute__("name")
    b = person.__getattribute__("address")
    c = person.__getattribute__("email")

    person.__delattr__("name")
    person.__delattr__("address")
    person.__delattr__("email")

    person.__setattr__("name", a)
    person.__setattr__("address", b)
    person.__setattr__("email", c)


def main():
    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    old = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    new = min(timeit.repeat(partial(get_set_delete, person_test), number=1000000))
    print(f"Текущая реализация: {old}")
    print(f"Тестовая реализация: {new}")
    print(f"Улучшение производительности: {(old - new) / old:.2%}")


if __name__ == "__main__":
    main()