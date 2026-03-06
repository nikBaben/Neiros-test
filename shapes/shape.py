from abc import ABC, abstractmethod


class Shape(ABC):
    id = 0 
    
    def __init__(self) -> None:
        Shape.id += 1
        self.shape_id = Shape.id

    @abstractmethod
    def info(self)  -> str:
        pass
    

