from .shape import Shape


class Rectangle(Shape):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        shape_id: int | None = None,
    ) -> None:
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def info(self) -> str:
        return (
            f"Прямоугольник(ID: {self.shape_id}, "
            f"левый верхний угол: ({self.x}, {self.y}), "
            f"width: {self.width}, height: {self.height})"
        )