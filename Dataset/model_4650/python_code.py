from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ContainerShape:

    pass
class di_EStringToStringMapEntry:

    pass
class di_DiNode(ABC):

    def __init__(self, modelElement: str, di_DiNode: set["di_EStringToStringMapEntry"] = None):
        self.modelElement = modelElement
        self.di_DiNode = di_DiNode if di_DiNode is not None else set()
        
    @property
    def modelElement(self) -> str:
        return self.__modelElement

    @modelElement.setter
    def modelElement(self, modelElement: str):
        self.__modelElement = modelElement

    @property
    def di_DiNode(self):
        return self.__di_DiNode

    @di_DiNode.setter
    def di_DiNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiNode__di_DiNode", None)
        self.__di_DiNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_EStringToStringMapEntry"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "di_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_EStringToStringMapEntry"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry", None)
                    
                    setattr(item, "di_EStringToStringMapEntry", self)
                    

class di_Diagram(ContainerShape):

    pass
class di_Shape(ContainerShape):

    def __init__(self, x: int, y: int, width: int, height: int, di_Shape: "di_ContainerShape" = None, Shape: "di_Link" = None, Shape6: "di_Link" = None, target: set["di_Link"] = None, source: set["di_Link"] = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.di_Shape = di_Shape
        self.Shape = Shape
        self.Shape6 = Shape6
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Shape__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link3"):
                    opp_val = getattr(item, "Link3", None)
                    
                    if opp_val == self:
                        setattr(item, "Link3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link3"):
                    opp_val = getattr(item, "Link3", None)
                    
                    setattr(item, "Link3", self)
                    

    @property
    def Shape(self):
        return self.__Shape

    @Shape.setter
    def Shape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Shape__Shape", None)
        self.__Shape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetLinks"):
                opp_val = getattr(old_value, "targetLinks", None)
                if opp_val == self:
                    setattr(old_value, "targetLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetLinks"):
                opp_val = getattr(value, "targetLinks", None)
                setattr(value, "targetLinks", self)

    @property
    def di_Shape(self):
        return self.__di_Shape

    @di_Shape.setter
    def di_Shape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Shape__di_Shape", None)
        self.__di_Shape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_ContainerShape"):
                opp_val = getattr(old_value, "di_ContainerShape", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_ContainerShape"):
                opp_val = getattr(value, "di_ContainerShape", None)
                if opp_val is None:
                    setattr(value, "di_ContainerShape", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Shape6(self):
        return self.__Shape6

    @Shape6.setter
    def Shape6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Shape__Shape6", None)
        self.__Shape6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceLinks"):
                opp_val = getattr(old_value, "sourceLinks", None)
                if opp_val == self:
                    setattr(old_value, "sourceLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceLinks"):
                opp_val = getattr(value, "sourceLinks", None)
                setattr(value, "sourceLinks", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Shape__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    if opp_val == self:
                        setattr(item, "Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    setattr(item, "Link", self)
                    

class DiNode:

    pass
class di_Link(DiNode):

    pass
class di_ContainerShape(DiNode):

    pass