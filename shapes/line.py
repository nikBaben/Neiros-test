from .shape import Shape


class Line(Shape):
    def __init__(self,x1: float, y1: float, x2: float, y2: float, shape_id: int | None = None) -> None:
        super().__init__(shape_id)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def info(self) -> str:
        return (
            f"Линия(ID: {self.shape_id}, координаты начала: ({self.x1}, {self.y1}), "
            f"координаты конца: ({self.x2}, {self.y2}))"
        )
    