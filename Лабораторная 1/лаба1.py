import doctest

class Tree:
    """
    Абстрактный класс, описывающий дерево.
    """
    def __init__(self, height: float, age: int):
        """
        Инициализация дерева.

        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах.

        :raises ValueError: Если высота или возраст имеют недопустимые значения.
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть числом.")
        if height <= 0:
            raise ValueError("Высота должна быть положительной.")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличивает высоту и возраст дерева.

        :param years: Количество лет, на которое дерево будет расти.

        :raises ValueError: Если количество лет отрицательно.
        >>> tree = Tree(10, 5)
        >>> tree.grow(2)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом.")
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным.")
        ...

    def shed_leaves(self) -> None:
        """
        Сбрасывает листья (для листопадных деревьев).
        >>> tree = Tree(10,5)
        >>> tree.shed_leaves()
        """
        ...


class Stack:
    """
    Абстрактный класс, описывающий стек (структура данных).
    """
    def __init__(self, max_size: int):
        """
        Инициализация стека.

        :param max_size: Максимальный размер стека.

        :raises ValueError: Если максимальный размер не положителен.
        """
        if not isinstance(max_size, int):
            raise TypeError("Максимальный размер должен быть целым числом.")
        if max_size <= 0:
            raise ValueError("Максимальный размер должен быть положительным.")
        self.max_size = max_size
        self.items = []

    def push(self, item: object) -> None:
        """
        Добавляет элемент на вершину стека.

        :param item: Элемент для добавления.

        :raises OverflowError: Если стек полон.
        >>> stack = Stack(2)
        >>> stack.push(1)
        """
        if len(self.items) >= self.max_size:
            raise OverflowError("Стек полон.")
        self.items.append(item)
        ...

    def pop(self) -> object:
        """
        Удаляет и возвращает элемент с вершины стека.

        :raises IndexError: Если стек пуст.
        :returns: Удаленный элемент.

        >>> stack = Stack(2)
        >>> stack.push(1)
        >>> stack.pop()
        1
        """
        if not self.items:
            raise IndexError("Стек пуст.")
        return self.items.pop()



class SocialNetwork:
    """
    Абстрактный класс, описывающий социальную сеть.
    """
    def __init__(self, name: str, num_users: int):
        """
        Инициализация социальной сети.

        :param name: Название социальной сети.
        :param num_users: Количество пользователей.

        :raises ValueError: Если количество пользователей отрицательно.
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой.")
        self.name = name

        if not isinstance(num_users, int):
            raise TypeError("Количество пользователей должно быть целым числом.")
        if num_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.num_users = num_users

    def add_user(self, username: str) -> None:
        """
        Добавляет нового пользователя.

        :param username: Имя пользователя.
        >>> network = SocialNetwork("TestNet", 0)
        >>> network.add_user("user1")
        """
        ...

    def remove_user(self, username: str) -> None:
        """
        Удаляет пользователя.

        :param username: Имя пользователя.
        >>> network = SocialNetwork("TestNet", 1)
        >>> network.add_user("user1")
        >>> network.remove_user("user1")
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
