from shapes import Shape


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