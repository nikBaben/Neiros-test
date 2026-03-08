from .shape import Shape


class Square(Shape):
    def __init__(self, x: float, y: float, side: float, shape_id: int | None = None) -> None:
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.side = side
    
    def info(self) -> str:
        return f"Квадрат(ID: {self.shape_id}, длинна линии: {self.side})"
    