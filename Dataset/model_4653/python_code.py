from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class di_EStringToStringMapEntry:

    pass
class di_Style(ABC):

    def __init__(self, id: str, di_Style: "di_DocumentRoot" = None):
        self.id = id
        self.di_Style = di_Style
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def di_Style(self):
        return self.__di_Style

    @di_Style.setter
    def di_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Style__di_Style", None)
        self.__di_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot35"):
                opp_val = getattr(old_value, "di_DocumentRoot35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot35"):
                opp_val = getattr(value, "di_DocumentRoot35", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    def __init__(self, diagramElementGroup: str, di_Plane: set["di_DiagramElement"] = None, di_Plane30: "di_DocumentRoot" = None):
        self.diagramElementGroup = diagramElementGroup
        self.di_Plane = di_Plane if di_Plane is not None else set()
        self.di_Plane30 = di_Plane30
        
    @property
    def diagramElementGroup(self) -> str:
        return self.__diagramElementGroup

    @diagramElementGroup.setter
    def diagramElementGroup(self, diagramElementGroup: str):
        self.__diagramElementGroup = diagramElementGroup

    @property
    def di_Plane30(self):
        return self.__di_Plane30

    @di_Plane30.setter
    def di_Plane30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Plane__di_Plane30", None)
        self.__di_Plane30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot29"):
                opp_val = getattr(old_value, "di_DocumentRoot29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot29"):
                opp_val = getattr(value, "di_DocumentRoot29", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "di_DiagramElement4"):
                    opp_val = getattr(item, "di_DiagramElement4", None)
                    
                    if opp_val == self:
                        setattr(item, "di_DiagramElement4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_DiagramElement4"):
                    opp_val = getattr(item, "di_DiagramElement4", None)
                    
                    setattr(item, "di_DiagramElement4", self)
                    

class di_Shape(Node):

    pass
class di_Label(Node):

    pass
class di_DocumentRoot:

    def __init__(self, mixed: str, di_DocumentRoot27: set["di_Node"] = None, di_DocumentRoot: set["di_EStringToStringMapEntry"] = None, di_DocumentRoot9: set["di_EStringToStringMapEntry"] = None, di_DocumentRoot12: set["di_DiagramElement"] = None, di_DocumentRoot15: set["di_Diagram"] = None, di_DocumentRoot17: set["di_Edge"] = None, di_DocumentRoot20: set["di_Label"] = None, di_DocumentRoot23: set["di_LabeledEdge"] = None, di_DocumentRoot25: set["di_LabeledShape"] = None, di_DocumentRoot29: set["di_Plane"] = None, di_DocumentRoot32: set["di_Shape"] = None, di_DocumentRoot35: set["di_Style"] = None):
        self.mixed = mixed
        self.di_DocumentRoot27 = di_DocumentRoot27 if di_DocumentRoot27 is not None else set()
        self.di_DocumentRoot = di_DocumentRoot if di_DocumentRoot is not None else set()
        self.di_DocumentRoot9 = di_DocumentRoot9 if di_DocumentRoot9 is not None else set()
        self.di_DocumentRoot12 = di_DocumentRoot12 if di_DocumentRoot12 is not None else set()
        self.di_DocumentRoot15 = di_DocumentRoot15 if di_DocumentRoot15 is not None else set()
        self.di_DocumentRoot17 = di_DocumentRoot17 if di_DocumentRoot17 is not None else set()
        self.di_DocumentRoot20 = di_DocumentRoot20 if di_DocumentRoot20 is not None else set()
        self.di_DocumentRoot23 = di_DocumentRoot23 if di_DocumentRoot23 is not None else set()
        self.di_DocumentRoot25 = di_DocumentRoot25 if di_DocumentRoot25 is not None else set()
        self.di_DocumentRoot29 = di_DocumentRoot29 if di_DocumentRoot29 is not None else set()
        self.di_DocumentRoot32 = di_DocumentRoot32 if di_DocumentRoot32 is not None else set()
        self.di_DocumentRoot35 = di_DocumentRoot35 if di_DocumentRoot35 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def di_DocumentRoot29(self):
        return self.__di_DocumentRoot29

    @di_DocumentRoot29.setter
    def di_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot29", None)
        self.__di_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Plane30"):
                    opp_val = getattr(item, "di_Plane30", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Plane30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Plane30"):
                    opp_val = getattr(item, "di_Plane30", None)
                    
                    setattr(item, "di_Plane30", self)
                    

    @property
    def di_DocumentRoot32(self):
        return self.__di_DocumentRoot32

    @di_DocumentRoot32.setter
    def di_DocumentRoot32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot32", None)
        self.__di_DocumentRoot32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Shape33"):
                    opp_val = getattr(item, "di_Shape33", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Shape33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Shape33"):
                    opp_val = getattr(item, "di_Shape33", None)
                    
                    setattr(item, "di_Shape33", self)
                    

    @property
    def di_DocumentRoot20(self):
        return self.__di_DocumentRoot20

    @di_DocumentRoot20.setter
    def di_DocumentRoot20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot20", None)
        self.__di_DocumentRoot20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Label21"):
                    opp_val = getattr(item, "di_Label21", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Label21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Label21"):
                    opp_val = getattr(item, "di_Label21", None)
                    
                    setattr(item, "di_Label21", self)
                    

    @property
    def di_DocumentRoot23(self):
        return self.__di_DocumentRoot23

    @di_DocumentRoot23.setter
    def di_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot23", None)
        self.__di_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_LabeledEdge"):
                    opp_val = getattr(item, "di_LabeledEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "di_LabeledEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_LabeledEdge"):
                    opp_val = getattr(item, "di_LabeledEdge", None)
                    
                    setattr(item, "di_LabeledEdge", self)
                    

    @property
    def di_DocumentRoot(self):
        return self.__di_DocumentRoot

    @di_DocumentRoot.setter
    def di_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot", None)
        self.__di_DocumentRoot = value if value is not None else set()
        
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
                    

    @property
    def di_DocumentRoot12(self):
        return self.__di_DocumentRoot12

    @di_DocumentRoot12.setter
    def di_DocumentRoot12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot12", None)
        self.__di_DocumentRoot12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_DiagramElement13"):
                    opp_val = getattr(item, "di_DiagramElement13", None)
                    
                    if opp_val == self:
                        setattr(item, "di_DiagramElement13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_DiagramElement13"):
                    opp_val = getattr(item, "di_DiagramElement13", None)
                    
                    setattr(item, "di_DiagramElement13", self)
                    

    @property
    def di_DocumentRoot15(self):
        return self.__di_DocumentRoot15

    @di_DocumentRoot15.setter
    def di_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot15", None)
        self.__di_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Diagram"):
                    opp_val = getattr(item, "di_Diagram", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Diagram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Diagram"):
                    opp_val = getattr(item, "di_Diagram", None)
                    
                    setattr(item, "di_Diagram", self)
                    

    @property
    def di_DocumentRoot9(self):
        return self.__di_DocumentRoot9

    @di_DocumentRoot9.setter
    def di_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot9", None)
        self.__di_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_EStringToStringMapEntry10"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry10", None)
                    
                    if opp_val == self:
                        setattr(item, "di_EStringToStringMapEntry10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_EStringToStringMapEntry10"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry10", None)
                    
                    setattr(item, "di_EStringToStringMapEntry10", self)
                    

    @property
    def di_DocumentRoot25(self):
        return self.__di_DocumentRoot25

    @di_DocumentRoot25.setter
    def di_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot25", None)
        self.__di_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_LabeledShape"):
                    opp_val = getattr(item, "di_LabeledShape", None)
                    
                    if opp_val == self:
                        setattr(item, "di_LabeledShape", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_LabeledShape"):
                    opp_val = getattr(item, "di_LabeledShape", None)
                    
                    setattr(item, "di_LabeledShape", self)
                    

    @property
    def di_DocumentRoot35(self):
        return self.__di_DocumentRoot35

    @di_DocumentRoot35.setter
    def di_DocumentRoot35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot35", None)
        self.__di_DocumentRoot35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Style"):
                    opp_val = getattr(item, "di_Style", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Style", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Style"):
                    opp_val = getattr(item, "di_Style", None)
                    
                    setattr(item, "di_Style", self)
                    

    @property
    def di_DocumentRoot27(self):
        return self.__di_DocumentRoot27

    @di_DocumentRoot27.setter
    def di_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot27", None)
        self.__di_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Node"):
                    opp_val = getattr(item, "di_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Node"):
                    opp_val = getattr(item, "di_Node", None)
                    
                    setattr(item, "di_Node", self)
                    

    @property
    def di_DocumentRoot17(self):
        return self.__di_DocumentRoot17

    @di_DocumentRoot17.setter
    def di_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot17", None)
        self.__di_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Edge18"):
                    opp_val = getattr(item, "di_Edge18", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Edge18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Edge18"):
                    opp_val = getattr(item, "di_Edge18", None)
                    
                    setattr(item, "di_Edge18", self)
                    

class di_Point:

    pass
class DiagramElement:

    pass
class di_Node(DiagramElement):

    pass
class di_Edge(DiagramElement):

    pass
class di_ExtensionType:

    def __init__(self, any: str, di_ExtensionType: "di_DiagramElement" = None):
        self.any = any
        self.di_ExtensionType = di_ExtensionType
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def di_ExtensionType(self):
        return self.__di_ExtensionType

    @di_ExtensionType.setter
    def di_ExtensionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_ExtensionType__di_ExtensionType", None)
        self.__di_ExtensionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DiagramElement"):
                opp_val = getattr(old_value, "di_DiagramElement", None)
                if opp_val == self:
                    setattr(old_value, "di_DiagramElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DiagramElement"):
                opp_val = getattr(value, "di_DiagramElement", None)
                setattr(value, "di_DiagramElement", self)

class di_DiagramElement(ABC):

    def __init__(self, id: str, anyAttribute: str, di_DiagramElement: "di_ExtensionType" = None, di_DiagramElement4: "di_Plane" = None, di_DiagramElement13: "di_DocumentRoot" = None):
        self.id = id
        self.anyAttribute = anyAttribute
        self.di_DiagramElement = di_DiagramElement
        self.di_DiagramElement4 = di_DiagramElement4
        self.di_DiagramElement13 = di_DiagramElement13
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def di_DiagramElement4(self):
        return self.__di_DiagramElement4

    @di_DiagramElement4.setter
    def di_DiagramElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__di_DiagramElement4", None)
        self.__di_DiagramElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Plane"):
                opp_val = getattr(old_value, "di_Plane", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Plane"):
                opp_val = getattr(value, "di_Plane", None)
                if opp_val is None:
                    setattr(value, "di_Plane", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_DiagramElement13(self):
        return self.__di_DiagramElement13

    @di_DiagramElement13.setter
    def di_DiagramElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__di_DiagramElement13", None)
        self.__di_DiagramElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot12"):
                opp_val = getattr(old_value, "di_DocumentRoot12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot12"):
                opp_val = getattr(value, "di_DocumentRoot12", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_DiagramElement(self):
        return self.__di_DiagramElement

    @di_DiagramElement.setter
    def di_DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DiagramElement__di_DiagramElement", None)
        self.__di_DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_ExtensionType"):
                opp_val = getattr(old_value, "di_ExtensionType", None)
                if opp_val == self:
                    setattr(old_value, "di_ExtensionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_ExtensionType"):
                opp_val = getattr(value, "di_ExtensionType", None)
                setattr(value, "di_ExtensionType", self)

class di_Diagram(ABC):

    def __init__(self, documentation: str, id: str, name: str, resolution: str, di_Diagram: "di_DocumentRoot" = None):
        self.documentation = documentation
        self.id = id
        self.name = name
        self.resolution = resolution
        self.di_Diagram = di_Diagram
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def resolution(self) -> str:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str):
        self.__resolution = resolution

    @property
    def di_Diagram(self):
        return self.__di_Diagram

    @di_Diagram.setter
    def di_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__di_Diagram", None)
        self.__di_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot15"):
                opp_val = getattr(old_value, "di_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot15"):
                opp_val = getattr(value, "di_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
