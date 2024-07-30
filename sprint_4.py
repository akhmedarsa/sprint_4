"""
ID 116498555
Модуль для расчёта минимального количества платформ для перевозки роботов.

Этот модуль включает функцию для вычисления минимального количества
транспортных платформ, необходимых для перевозки всех роботов,
описанных в списке весов. Каждый робот имеет разный вес, и платформа
может выдержать либо одного робота, либо двух, если их суммарный вес
не превышает грузоподъёмность.При решении использовался жадный алгоритм.

Функции:
- min_platforms(weights: list[int], limit: int) -> int:
  вычисляет минимальное количество платформ.

Пример использования:
weights = [3, 3, 2, 1]
limit = 3
print(min_platforms(weights, limit))  # Вывод: 3
"""


def min_platforms(weights: list[int], limit: int) -> int:
    """
    Вычисляет минимальное количество платформ, необходимых для
    перевозки всех роботов.

    Аргументы:
    weights (List[int]): Список весов роботов.
    limit (int): Грузоподъёмность одной платформы.

    Возвращает:
    int: Минимальное количество платформ.
    """
    # Создаем копию списка весов роботов и сортируем ее
    sorted_weights = sorted(weights)

    # Инициализируем указатели и счётчик платформ
    left_point, right_point = 0, len(sorted_weights) - 1
    platforms = 0

    # Используем два указателя для парного подхода
    while left_point <= right_point:
        # Если самый лёгкий и самый тяжёлый роботы могут быть перевезены вместе
        if sorted_weights[left_point] + sorted_weights[right_point] <= limit:
            left_point += 1
        # В любом случае, перевезём самого тяжёлого робота
        right_point -= 1
        # Увеличиваем счётчик платформ
        platforms += 1

    return platforms


if __name__ == '__main__':
    weights_input = input()
    limit = int(input())
    weights = [int(weight) for weight in weights_input.strip().split()]
    print(min_platforms(weights, limit))
