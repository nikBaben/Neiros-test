from .shape import Shape


class Oval(Shape):
    def __init__(
        self,
        x: float,
        y: float,
        radius_x: float,
        radius_y: float,
        shape_id: int | None = None,
    ) -> None:
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.radius_x = radius_x
        self.radius_y = radius_y

    def info(self) -> str:
        return (
            f"Овал(ID: {self.shape_id}, центр: ({self.x}, {self.y}), "
            f"радиус_x: {self.radius_x}, радиус_y: {self.radius_y})"
        )