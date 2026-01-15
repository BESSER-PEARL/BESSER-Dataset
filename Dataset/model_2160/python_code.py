from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Colors(Enum):
    clean = "clean"
    touched = "touched"
    performed = "performed"


############################################
# Definition of Classes
############################################

class egt_GraphModel:

    pass
class Edge:

    pass
class egt_SingleEdge(Edge):

    pass
class egt_DiEdge(Edge):

    pass
class egt_ColorRegistry:

    def __init__(self, images: str, egt_ColorRegistry: "egt_GraphModel" = None):
        self.images = images
        self.egt_ColorRegistry = egt_ColorRegistry
        
    @property
    def images(self) -> str:
        return self.__images

    @images.setter
    def images(self, images: str):
        self.__images = images

    @property
    def egt_ColorRegistry(self):
        return self.__egt_ColorRegistry

    @egt_ColorRegistry.setter
    def egt_ColorRegistry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egt_ColorRegistry__egt_ColorRegistry", None)
        self.__egt_ColorRegistry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "egt_GraphModel7"):
                opp_val = getattr(old_value, "egt_GraphModel7", None)
                if opp_val == self:
                    setattr(old_value, "egt_GraphModel7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "egt_GraphModel7"):
                opp_val = getattr(value, "egt_GraphModel7", None)
                setattr(value, "egt_GraphModel7", self)

    def dispose(self):
        # TODO: Implement dispose method
        pass

    def init(self):
        # TODO: Implement init method
        pass

class egt_Edge:

    def __init__(self, weight: float, color: str, egt_Edge: "egt_Vertex" = None, egt_Edge2: "egt_Vertex" = None):
        self.weight = weight
        self.color = color
        self.egt_Edge = egt_Edge
        self.egt_Edge2 = egt_Edge2
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def egt_Edge(self):
        return self.__egt_Edge

    @egt_Edge.setter
    def egt_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egt_Edge__egt_Edge", None)
        self.__egt_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "egt_Vertex"):
                opp_val = getattr(old_value, "egt_Vertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "egt_Vertex"):
                opp_val = getattr(value, "egt_Vertex", None)
                if opp_val is None:
                    setattr(value, "egt_Vertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def egt_Edge2(self):
        return self.__egt_Edge2

    @egt_Edge2.setter
    def egt_Edge2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egt_Edge__egt_Edge2", None)
        self.__egt_Edge2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "egt_Vertex3"):
                opp_val = getattr(old_value, "egt_Vertex3", None)
                if opp_val == self:
                    setattr(old_value, "egt_Vertex3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "egt_Vertex3"):
                opp_val = getattr(value, "egt_Vertex3", None)
                setattr(value, "egt_Vertex3", self)

class egt_Vertex:

    def __init__(self, index: int, name: str, color: str, egt_Vertex: set["egt_Edge"] = None, egt_Vertex3: "egt_Edge" = None, egt_Vertex5: "egt_GraphModel" = None):
        self.index = index
        self.name = name
        self.color = color
        self.egt_Vertex = egt_Vertex if egt_Vertex is not None else set()
        self.egt_Vertex3 = egt_Vertex3
        self.egt_Vertex5 = egt_Vertex5
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def egt_Vertex5(self):
        return self.__egt_Vertex5

    @egt_Vertex5.setter
    def egt_Vertex5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egt_Vertex__egt_Vertex5", None)
        self.__egt_Vertex5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "egt_GraphModel"):
                opp_val = getattr(old_value, "egt_GraphModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "egt_GraphModel"):
                opp_val = getattr(value, "egt_GraphModel", None)
                if opp_val is None:
                    setattr(value, "egt_GraphModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def egt_Vertex3(self):
        return self.__egt_Vertex3

    @egt_Vertex3.setter
    def egt_Vertex3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egt_Vertex__egt_Vertex3", None)
        self.__egt_Vertex3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "egt_Edge2"):
                opp_val = getattr(old_value, "egt_Edge2", None)
                if opp_val == self:
                    setattr(old_value, "egt_Edge2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "egt_Edge2"):
                opp_val = getattr(value, "egt_Edge2", None)
                setattr(value, "egt_Edge2", self)

    @property
    def egt_Vertex(self):
        return self.__egt_Vertex

    @egt_Vertex.setter
    def egt_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_egt_Vertex__egt_Vertex", None)
        self.__egt_Vertex = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "egt_Edge"):
                    opp_val = getattr(item, "egt_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "egt_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "egt_Edge"):
                    opp_val = getattr(item, "egt_Edge", None)
                    
                    setattr(item, "egt_Edge", self)
                    
