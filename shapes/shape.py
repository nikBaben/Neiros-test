from abc import ABC, abstractmethod


class Shape(ABC):
    id = 0 

    def __init__(self, shape_id: int | None = None ) -> None:
        if shape_id is None:
            Shape.id += 1
            self.shape_id = Shape.id
        else:
            self.shape_id = shape_id
            if shape_id > Shape.id:     
                Shape.id = shape_id

    @abstractmethod
    def info(self)  -> str:
        pass

    def to_dict(self) -> dict:
        return {
            "type": self.__class__.__name__,
            **self.__dict__
        }
    
    @classmethod
    def rebuild_id(cls, shapes: dict[int, "Shape"]) -> None:
        cls.id = max(shapes.keys(), default=0)