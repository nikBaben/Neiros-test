from typing import Callable
from functools import wraps

from shapes import Shape
from storage import JsonStorage
from shapes import ShapeFactory


class VectorEditor:
    def __init__(self) -> None:
        self.shapes: dict[int, Shape] = {}

    def add(self, shape: Shape) -> None:
        self.shapes[shape.shape_id] = shape

    def list(self) -> None:
        print(f"Общее количество фигур: {len(self.shapes)}")
        for shape in self.shapes.values():
            print(shape.info())

    def delete(self, shape_id: int) -> None:
        if shape_id in self.shapes:
            del self.shapes[shape_id]
        else:
            raise ValueError(f"Фигура с ID {shape_id} не найдена.")

    def delete_all(self) -> None:
        if not self.shapes:
            raise ValueError("Нет фигур для удаления.")
        self.shapes.clear()

    def _init_storage(self,filename: str) -> None:
        self.storage = JsonStorage(f"storage/data/{filename}.json")

    @staticmethod
    def hasattr_storage(func) -> Callable:
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except AttributeError:
                print("Хранилище не инициализировано.")
        return wrapper
        
    @hasattr_storage
    def save(self) -> bool:
        data = [shape.to_dict() for shape in self.shapes.values()]
        self.storage.save(data)

        return True

    @hasattr_storage
    def load(self) -> bool:
        data = self.storage.load()
        if data is None:
            print("Нет данных для загрузки.")
            return False
        try:
            self.delete_all() 
        except ValueError:
            pass

        for item in data:
            try:
                shape = ShapeFactory.create_from_dict(item)
                self.shapes[shape.shape_id] = shape
            except ValueError as e:
                print(f"Ошибка при загрузке фигуры: {e}")

        Shape.rebuild_id(self.shapes)
        
        return True

    