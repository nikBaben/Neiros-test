from .shape import Shape

class Point(Shape):
    def __init__(
        self, 
        x: float,
        y: float,
        shape_id: int | None = None
    ) -> None:
        super().__init__(shape_id)
        self.x = x
        self.y = y

    def info(self) -> str:
        return f"Точка(ID: {self.shape_id}, x={self.x}, y={self.y})"
