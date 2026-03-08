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
    
    @classmethod
    def create_from_dict(cls, data: dict) -> Shape:
        data = data.copy()
        shape_type = data.pop("type")
        if shape_type not in cls.registry:
            raise ValueError(f"Неизвестная фигура: {shape_type}")

        return cls.registry[shape_type](**data)