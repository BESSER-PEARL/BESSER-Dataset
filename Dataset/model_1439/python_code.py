from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class GraphicElement:

    pass
class RepresentationGraph_NodeElement(GraphicElement):

    def __init__(self, label: str, RepresentationGraph_NodeElement: "RepresentationGraph_EdgeElement" = None, RepresentationGraph_NodeElement4: "RepresentationGraph_EdgeElement" = None, RepresentationGraph_NodeElement7: "RepresentationGraph_NodeElement" = None, RepresentationGraph_NodeElement5: set["RepresentationGraph_NodeElement"] = None, RepresentationGraph_NodeElement9: "RepresentationGraph_ContainerElement" = None):
        self.label = label
        self.RepresentationGraph_NodeElement = RepresentationGraph_NodeElement
        self.RepresentationGraph_NodeElement4 = RepresentationGraph_NodeElement4
        self.RepresentationGraph_NodeElement7 = RepresentationGraph_NodeElement7
        self.RepresentationGraph_NodeElement5 = RepresentationGraph_NodeElement5 if RepresentationGraph_NodeElement5 is not None else set()
        self.RepresentationGraph_NodeElement9 = RepresentationGraph_NodeElement9
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def RepresentationGraph_NodeElement9(self):
        return self.__RepresentationGraph_NodeElement9

    @RepresentationGraph_NodeElement9.setter
    def RepresentationGraph_NodeElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RepresentationGraph_NodeElement__RepresentationGraph_NodeElement9", None)
        self.__RepresentationGraph_NodeElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentationGraph_ContainerElement"):
                opp_val = getattr(old_value, "RepresentationGraph_ContainerElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationGraph_ContainerElement"):
                opp_val = getattr(value, "RepresentationGraph_ContainerElement", None)
                if opp_val is None:
                    setattr(value, "RepresentationGraph_ContainerElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RepresentationGraph_NodeElement5(self):
        return self.__RepresentationGraph_NodeElement5

    @RepresentationGraph_NodeElement5.setter
    def RepresentationGraph_NodeElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RepresentationGraph_NodeElement__RepresentationGraph_NodeElement5", None)
        self.__RepresentationGraph_NodeElement5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepresentationGraph_NodeElement7"):
                    opp_val = getattr(item, "RepresentationGraph_NodeElement7", None)
                    
                    if opp_val == self:
                        setattr(item, "RepresentationGraph_NodeElement7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepresentationGraph_NodeElement7"):
                    opp_val = getattr(item, "RepresentationGraph_NodeElement7", None)
                    
                    setattr(item, "RepresentationGraph_NodeElement7", self)
                    

    @property
    def RepresentationGraph_NodeElement(self):
        return self.__RepresentationGraph_NodeElement

    @RepresentationGraph_NodeElement.setter
    def RepresentationGraph_NodeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RepresentationGraph_NodeElement__RepresentationGraph_NodeElement", None)
        self.__RepresentationGraph_NodeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentationGraph_EdgeElement"):
                opp_val = getattr(old_value, "RepresentationGraph_EdgeElement", None)
                if opp_val == self:
                    setattr(old_value, "RepresentationGraph_EdgeElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationGraph_EdgeElement"):
                opp_val = getattr(value, "RepresentationGraph_EdgeElement", None)
                setattr(value, "RepresentationGraph_EdgeElement", self)

    @property
    def RepresentationGraph_NodeElement7(self):
        return self.__RepresentationGraph_NodeElement7

    @RepresentationGraph_NodeElement7.setter
    def RepresentationGraph_NodeElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RepresentationGraph_NodeElement__RepresentationGraph_NodeElement7", None)
        self.__RepresentationGraph_NodeElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentationGraph_NodeElement5"):
                opp_val = getattr(old_value, "RepresentationGraph_NodeElement5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationGraph_NodeElement5"):
                opp_val = getattr(value, "RepresentationGraph_NodeElement5", None)
                if opp_val is None:
                    setattr(value, "RepresentationGraph_NodeElement5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RepresentationGraph_NodeElement4(self):
        return self.__RepresentationGraph_NodeElement4

    @RepresentationGraph_NodeElement4.setter
    def RepresentationGraph_NodeElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RepresentationGraph_NodeElement__RepresentationGraph_NodeElement4", None)
        self.__RepresentationGraph_NodeElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentationGraph_EdgeElement3"):
                opp_val = getattr(old_value, "RepresentationGraph_EdgeElement3", None)
                if opp_val == self:
                    setattr(old_value, "RepresentationGraph_EdgeElement3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationGraph_EdgeElement3"):
                opp_val = getattr(value, "RepresentationGraph_EdgeElement3", None)
                setattr(value, "RepresentationGraph_EdgeElement3", self)

class RepresentationGraph_EdgeElement(GraphicElement):

    pass
class RepresentationGraph_GraphicElement(ABC):

    def __init__(self, color: str, paletteName: str, paletteIconPath: str, RepresentationGraph_GraphicElement: "RepresentationGraph_Diagram" = None):
        self.color = color
        self.paletteName = paletteName
        self.paletteIconPath = paletteIconPath
        self.RepresentationGraph_GraphicElement = RepresentationGraph_GraphicElement
        
    @property
    def paletteName(self) -> str:
        return self.__paletteName

    @paletteName.setter
    def paletteName(self, paletteName: str):
        self.__paletteName = paletteName

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def paletteIconPath(self) -> str:
        return self.__paletteIconPath

    @paletteIconPath.setter
    def paletteIconPath(self, paletteIconPath: str):
        self.__paletteIconPath = paletteIconPath

    @property
    def RepresentationGraph_GraphicElement(self):
        return self.__RepresentationGraph_GraphicElement

    @RepresentationGraph_GraphicElement.setter
    def RepresentationGraph_GraphicElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RepresentationGraph_GraphicElement__RepresentationGraph_GraphicElement", None)
        self.__RepresentationGraph_GraphicElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentationGraph_Diagram"):
                opp_val = getattr(old_value, "RepresentationGraph_Diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationGraph_Diagram"):
                opp_val = getattr(value, "RepresentationGraph_Diagram", None)
                if opp_val is None:
                    setattr(value, "RepresentationGraph_Diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RepresentationGraph_Diagram:

    pass
class ContainerElement:

    pass
class RepresentationGraph_Rhombus(ContainerElement):

    def __init__(self, width: str, height: str):
        self.width = width
        self.height = height
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

class RepresentationGraph_Rectangle(ContainerElement):

    def __init__(self, width: str, height: str):
        self.width = width
        self.height = height
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

class RepresentationGraph_Circle(ContainerElement):

    def __init__(self, radius: str):
        self.radius = radius
        
    @property
    def radius(self) -> str:
        return self.__radius

    @radius.setter
    def radius(self, radius: str):
        self.__radius = radius

class NodeElement:

    pass
class RepresentationGraph_ContainerElement(NodeElement):

    pass
class RepresentationGraph_IconElement(NodeElement):

    def __init__(self, filepath: str):
        self.filepath = filepath
        
    @property
    def filepath(self) -> str:
        return self.__filepath

    @filepath.setter
    def filepath(self, filepath: str):
        self.__filepath = filepath
