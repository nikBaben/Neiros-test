from .shape import Shape

class Circle(Shape):
    def __init__(
        self,
        x: float,
        y: float, 
        radius: float,
        shape_id: int | None = None
    ) -> None:
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.radius = radius

    def info(self) -> str:
        return (
            f"Круг(ID: {self.shape_id}, центр: ({self.x}, {self.y}), "
            f"радиус: {self.radius})"
        )