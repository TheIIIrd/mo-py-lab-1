"""
Точка входа программы, инициирует параметры и запускает симплекс-метод.
"""

from simplexsus.simplexsus import simplexsus

def main():
    """
    Точка входа программы - инициализация значений и вызов симплекс-метода.
    """
    minimize = False                            # Необходимость минимизации
    c = [3, 1, 4]                               # Коэффициенты целевой функции
    A = [[2, 1, 1], [1, 4, 0], [0, 0.5, 1]]     # Ограничения
    b = [6, 4, 1]                               # Правая часть ограничений
    f = 0

    # minimize = False
    # c = [1, -1]
    # A = [[1, -2], [-2, 1], [1, 1]]
    # b = [2, -2, 5]
    # f = 0

    print("[ + ] Ans:", simplexsus(minimize, c, A, b, f))

    return 0


if __name__ == "__main__":
    main()
