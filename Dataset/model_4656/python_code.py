from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class di_Style(ABC):

    pass
class di_EObject:

    pass
class Shape:

    pass
class di_LabeledShape(Shape):

    pass
class Edge:

    pass
class di_LabeledEdge(Edge):

    pass
class di_Bounds:

    pass
class Node:

    pass
class di_Plane(Node):

    def __init__(self, di_Plane: set["di_DiagramElement"] = None):
        self.di_Plane = di_Plane if di_Plane is not None else set()
        
    @property
    def di_Plane(self):
        return self.__di_Plane

    @di_Plane.setter
    def di_Plane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Plane__di_Plane", None)
        self.__di_Plane = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_DiagramElement28"):
                    opp_val = getattr(item, "di_DiagramElement28", None)
                    
                    if opp_val == self:
                        setattr(item, "di_DiagramElement28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_DiagramElement28"):
                    opp_val = getattr(item, "di_DiagramElement28", None)
                    
                    setattr(item, "di_DiagramElement28", self)
                    

    def plane_element_type(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement plane_element_type method
        pass

class di_Label(Node):

    pass
class di_Shape(Node):

    pass
class di_Point:

    pass
class DiagramElement:

    pass
class di_Edge(DiagramElement):

    pass
class di_Node(DiagramElement):

    pass
class di_Diagram(ABC):

    def __init__(self, name: str, documentation: str, resolution: float, Diagram: "di_DiagramElement" = None, di_Diagram: set["di_Style"] = None, owningDiagram: "di_DiagramElement" = None):
        self.name = name
        self.documentation = documentation
        self.resolution = resolution
        self.Diagram = Diagram
        self.di_Diagram = di_Diagram if di_Diagram is not None else set()
        self.owningDiagram = owningDiagram
        
    @property
    def resolution(self) -> float:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: float):
        self.__resolution = resolution

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def di_Diagram(self):
        return self.__di_Diagram

    @di_Diagram.setter
    def di_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__di_Diagram", None)
        self.__di_Diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Style10"):
                    opp_val = getattr(item, "di_Style10", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Style10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Style10"):
                    opp_val = getattr(item, "di_Style10", None)
                    
                    setattr(item, "di_Style10", self)
                    

    @property
    def Diagram(self):
        return self.__Diagram

    @Diagram.setter
    def Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__Diagram", None)
        self.__Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rootElement"):
                opp_val = getattr(old_value, "rootElement", None)
                if opp_val == self:
                    setattr(old_value, "rootElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rootElement"):
                opp_val = getattr(value, "rootElement", None)
                setattr(value, "rootElement", self)

    @property
    def owningDiagram(self):
        return self.__owningDiagram

    @owningDiagram.setter
    def owningDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__owningDiagram", None)
        self.__owningDiagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramElement12"):
                opp_val = getattr(old_value, "DiagramElement12", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElement12"):
                opp_val = getattr(value, "DiagramElement12", None)
                setattr(value, "DiagramElement12", self)

class di_DiagramElement(ABC):

    pass