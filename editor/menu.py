import os

from shapes import (
    ShapeFactory,
    Point,
    Line,
    Square,
    Circle
)

from .editor import VectorEditor


class Menu:
    def __init__(self) -> None:
        self.editor = VectorEditor()
        self.factory = ShapeFactory()
        self.register_factory()
        
    @staticmethod
    def print_menu() -> None:
        print("\n===== Векторный редактор =====")
        print("1 - Создать точку")
        print("2 - Создать отрезок")
        print("3 - Создать круг")
        print("4 - Создать квадрат")
        print("5 - Список объектов")
        print("6 - Удалить объект по ID")
        print("7 - Удалить все объекты")
        print("0 - Выход")
        print("==============================\n")

    @staticmethod
    def clear_screen() -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("\033[H\033[J", end="")

    def register_factory(self) -> None:
        self.factory.register("point", Point)
        self.factory.register("line", Line) 
        self.factory.register("square", Square)
        self.factory.register("circle", Circle)

    def create_point(self) -> None:
        print("Добавление точки.")
        x = float(input("Введите координату X: "))
        y = float(input("Введите координату Y: "))
        point = self.factory.create("point", x, y)
        self.editor.add(point)
        print("Точка создана.")

    def create_line(self) -> None:
        print("Добавление линии.")
        x1 = float(input("Введите координату X1: "))
        y1 = float(input("Введите координату Y1: "))
        x2 = float(input("Введите координату X2: "))
        y2 = float(input("Введите координату Y2: "))
        line = self.factory.create("line", x1, y1, x2, y2)
        self.editor.add(line)
        print("Отрезок создан.")

    def create_circle(self) -> None:
        print("Добавление круга.")
        x = float(input("Введите координату X центра: "))
        y = float(input("Введите координату Y центра: "))
        radius = float(input("Введите радиус круга: "))
        circle = self.factory.create("circle", x, y, radius)
        self.editor.add(circle)
        print("Круг создан.")

    def create_square(self) -> None:
        print("Добавление квадрата.")
        x = float(input("Введите координату X левого верхнего угла квадрата: "))
        y = float(input("Введите координату Y левого верхнего угла квадрата: "))
        side_length = float(input("Введите длину стороны квадрата: "))
        square = self.factory.create("square", x, y, side_length)
        self.editor.add(square)
        print("Квадрат создан.")

    def list_shapes(self) -> None:
        self.editor.list()
        print("Список фигур отображён.")

    def delete_shape(self) -> None:
        shape_id = int(input("Введите ID фигуры для удаления: "))
        self.editor.delete(shape_id)
        print("Фигура удалена.")
    
    def delete_all_shapes(self) -> None:
        self.editor.delete_all()
        print("Все фигуры удалены.")