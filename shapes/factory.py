from .shape import Shape


class ShapeFactory:

    registry: dict[str, type[Shape]] = {}

    @classmethod
    def register(cls, name: str, shape_class: type[Shape]) -> None:
        cls.registry[name] = shape_class

    @classmethod
    def create(cls, name: str, *args) -> Shape:
        if name not in cls.registry:
            raise ValueError(f"Неизвестная фигура: {name}")

        return cls.registry[name](*args)