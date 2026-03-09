import os

from shapes import (
    ShapeFactory,
    Point,
    Line,
    Square,
    Circle,
    Rectangle,
    Oval    
)

from .editor import VectorEditor


class Menu:
    def __init__(self) -> None:
        self.editor = VectorEditor()
        self.factory = ShapeFactory()
        self.register_factory()
        
    @staticmethod
    def main_menu() -> None:
        print("\n===== Векторный редактор =====")
        print("1 - Создать точку")
        print("2 - Создать отрезок")
        print("3 - Создать квадрат")
        print("4 - Создать прямоугольник")
        print("5 - Создать круг")
        print("6 - Создать овал")
        print("7 - Список объектов")
        print("8 - Удалить объект по ID")
        print("9 - Удалить все объекты")
        print("10 - файл")
        print("------------------------------\n")
        print("0 - Выход")
        print("==============================\n")

    @staticmethod
    def file() -> None:
        print("\n===== Введите название файла для работы =====")

    @staticmethod
    def file_menu() -> None:
        print("\n===== Файл =====")
        print("1 - Выбрать файл для сохранения/загрузки ")
        print("2 - сохранить в файл")
        print("3 - загрузить из файла")
        print("------------------------------\n")
        print("0 - выход")
        print("==============================\n")

    @staticmethod
    def clear_screen() -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("\033[H\033[J", end="")

    def register_file(self, filename: str) -> None:
        self.editor._init_storage(filename) 
        
    def register_factory(self) -> None:
        self.factory.register("Point", Point)
        self.factory.register("Line", Line) 
        self.factory.register("Square", Square)
        self.factory.register("Rectangle", Rectangle)
        self.factory.register("Oval", Oval) 
        self.factory.register("Circle", Circle)

    def create_point(self) -> None:
        print("Добавление точки.")
        x = float(input("Введите координату X: "))
        y = float(input("Введите координату Y: "))
        point = self.factory.create("Point", x, y)
        self.editor.add(point)
        print("Точка создана.")

    def create_line(self) -> None:
        print("Добавление линии.")
        x1 = float(input("Введите координату X1: "))
        y1 = float(input("Введите координату Y1: "))
        x2 = float(input("Введите координату X2: "))
        y2 = float(input("Введите координату Y2: "))
        line = self.factory.create("Line", x1, y1, x2, y2)
        self.editor.add(line)
        print("Отрезок создан.")

    def create_square(self) -> None:
        print("Добавление квадрата.")
        x = float(input("Введите координату X левого верхнего угла квадрата: "))
        y = float(input("Введите координату Y левого верхнего угла квадрата: "))
        side_length = float(input("Введите длину стороны квадрата: "))
        square = self.factory.create("Square", x, y, side_length)
        self.editor.add(square)
        print("Квадрат создан.")

    def create_rectangle(self) -> None: 
        print("Добавление прямоугольника.")
        x = float(input("Введите координату X левого верхнего угла прямоугольника: "))
        y = float(input("Введите координату Y левого верхнего угла прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        height = float(input("Введите высоту прямоугольника: "))
        rectangle = self.factory.create("Rectangle", x, y, width, height)
        self.editor.add(rectangle)
        print("Прямоугольник создан.")

    def create_circle(self) -> None:
        print("Добавление круга.")
        x = float(input("Введите координату X центра: "))
        y = float(input("Введите координату Y центра: "))
        radius = float(input("Введите радиус круга: "))
        circle = self.factory.create("Circle", x, y, radius)
        self.editor.add(circle)
        print("Круг создан.")
    
    def create_oval(self) -> None:
        print("Добавление овала.")
        x = float(input("Введите координату X центра: "))
        y = float(input("Введите координату Y центра: "))
        width = float(input("Введите ширину овала: "))
        height = float(input("Введите высоту овала: "))
        oval = self.factory.create("Oval", x, y, width, height)
        self.editor.add(oval)
        print("Овал создан.")

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

    def save_to_file(self) -> None:
        if self.editor.save():
            print("Фигуры сохранены в файл.")

    def load_from_file(self) -> None:
        if self.editor.load():
            print("Фигуры загружены из файла.")