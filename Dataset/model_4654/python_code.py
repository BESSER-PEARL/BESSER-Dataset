from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class mtm_di_EStringToStringMapEntry:

    pass
class mtm_di_DocumentRoot:

    def __init__(self, mixed: str, mtm_di_DocumentRoot9: set["mtm_di_EStringToStringMapEntry"] = None, mtm_di_DocumentRoot12: set["mtm_di_DiagramElement"] = None, mtm_di_DocumentRoot15: set["mtm_di_Diagram"] = None, mtm_di_DocumentRoot17: set["mtm_di_Edge"] = None, mtm_di_DocumentRoot20: set["mtm_di_Label"] = None, mtm_di_DocumentRoot23: set["mtm_di_LabeledEdge"] = None, mtm_di_DocumentRoot25: set["mtm_di_LabeledShape"] = None, mtm_di_DocumentRoot27: set["mtm_di_Node"] = None, mtm_di_DocumentRoot: set["mtm_di_EStringToStringMapEntry"] = None, mtm_di_DocumentRoot35: set["mtm_di_Style"] = None, mtm_di_DocumentRoot29: set["mtm_di_Plane"] = None, mtm_di_DocumentRoot32: set["mtm_di_Shape"] = None):
        self.mixed = mixed
        self.mtm_di_DocumentRoot9 = mtm_di_DocumentRoot9 if mtm_di_DocumentRoot9 is not None else set()
        self.mtm_di_DocumentRoot12 = mtm_di_DocumentRoot12 if mtm_di_DocumentRoot12 is not None else set()
        self.mtm_di_DocumentRoot15 = mtm_di_DocumentRoot15 if mtm_di_DocumentRoot15 is not None else set()
        self.mtm_di_DocumentRoot17 = mtm_di_DocumentRoot17 if mtm_di_DocumentRoot17 is not None else set()
        self.mtm_di_DocumentRoot20 = mtm_di_DocumentRoot20 if mtm_di_DocumentRoot20 is not None else set()
        self.mtm_di_DocumentRoot23 = mtm_di_DocumentRoot23 if mtm_di_DocumentRoot23 is not None else set()
        self.mtm_di_DocumentRoot25 = mtm_di_DocumentRoot25 if mtm_di_DocumentRoot25 is not None else set()
        self.mtm_di_DocumentRoot27 = mtm_di_DocumentRoot27 if mtm_di_DocumentRoot27 is not None else set()
        self.mtm_di_DocumentRoot = mtm_di_DocumentRoot if mtm_di_DocumentRoot is not None else set()
        self.mtm_di_DocumentRoot35 = mtm_di_DocumentRoot35 if mtm_di_DocumentRoot35 is not None else set()
        self.mtm_di_DocumentRoot29 = mtm_di_DocumentRoot29 if mtm_di_DocumentRoot29 is not None else set()
        self.mtm_di_DocumentRoot32 = mtm_di_DocumentRoot32 if mtm_di_DocumentRoot32 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def mtm_di_DocumentRoot20(self):
        return self.__mtm_di_DocumentRoot20

    @mtm_di_DocumentRoot20.setter
    def mtm_di_DocumentRoot20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot20", None)
        self.__mtm_di_DocumentRoot20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_Label21"):
                    opp_val = getattr(item, "mtm_di_Label21", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_Label21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_Label21"):
                    opp_val = getattr(item, "mtm_di_Label21", None)
                    
                    setattr(item, "mtm_di_Label21", self)
                    

    @property
    def mtm_di_DocumentRoot35(self):
        return self.__mtm_di_DocumentRoot35

    @mtm_di_DocumentRoot35.setter
    def mtm_di_DocumentRoot35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot35", None)
        self.__mtm_di_DocumentRoot35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_Style"):
                    opp_val = getattr(item, "mtm_di_Style", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_Style", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_Style"):
                    opp_val = getattr(item, "mtm_di_Style", None)
                    
                    setattr(item, "mtm_di_Style", self)
                    

    @property
    def mtm_di_DocumentRoot(self):
        return self.__mtm_di_DocumentRoot

    @mtm_di_DocumentRoot.setter
    def mtm_di_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot", None)
        self.__mtm_di_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_EStringToStringMapEntry"):
                    opp_val = getattr(item, "mtm_di_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_EStringToStringMapEntry"):
                    opp_val = getattr(item, "mtm_di_EStringToStringMapEntry", None)
                    
                    setattr(item, "mtm_di_EStringToStringMapEntry", self)
                    

    @property
    def mtm_di_DocumentRoot32(self):
        return self.__mtm_di_DocumentRoot32

    @mtm_di_DocumentRoot32.setter
    def mtm_di_DocumentRoot32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot32", None)
        self.__mtm_di_DocumentRoot32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_Shape33"):
                    opp_val = getattr(item, "mtm_di_Shape33", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_Shape33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_Shape33"):
                    opp_val = getattr(item, "mtm_di_Shape33", None)
                    
                    setattr(item, "mtm_di_Shape33", self)
                    

    @property
    def mtm_di_DocumentRoot17(self):
        return self.__mtm_di_DocumentRoot17

    @mtm_di_DocumentRoot17.setter
    def mtm_di_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot17", None)
        self.__mtm_di_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_Edge18"):
                    opp_val = getattr(item, "mtm_di_Edge18", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_Edge18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_Edge18"):
                    opp_val = getattr(item, "mtm_di_Edge18", None)
                    
                    setattr(item, "mtm_di_Edge18", self)
                    

    @property
    def mtm_di_DocumentRoot23(self):
        return self.__mtm_di_DocumentRoot23

    @mtm_di_DocumentRoot23.setter
    def mtm_di_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot23", None)
        self.__mtm_di_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_LabeledEdge"):
                    opp_val = getattr(item, "mtm_di_LabeledEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_LabeledEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_LabeledEdge"):
                    opp_val = getattr(item, "mtm_di_LabeledEdge", None)
                    
                    setattr(item, "mtm_di_LabeledEdge", self)
                    

    @property
    def mtm_di_DocumentRoot25(self):
        return self.__mtm_di_DocumentRoot25

    @mtm_di_DocumentRoot25.setter
    def mtm_di_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot25", None)
        self.__mtm_di_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_LabeledShape"):
                    opp_val = getattr(item, "mtm_di_LabeledShape", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_LabeledShape", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_LabeledShape"):
                    opp_val = getattr(item, "mtm_di_LabeledShape", None)
                    
                    setattr(item, "mtm_di_LabeledShape", self)
                    

    @property
    def mtm_di_DocumentRoot29(self):
        return self.__mtm_di_DocumentRoot29

    @mtm_di_DocumentRoot29.setter
    def mtm_di_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot29", None)
        self.__mtm_di_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_Plane30"):
                    opp_val = getattr(item, "mtm_di_Plane30", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_Plane30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_Plane30"):
                    opp_val = getattr(item, "mtm_di_Plane30", None)
                    
                    setattr(item, "mtm_di_Plane30", self)
                    

    @property
    def mtm_di_DocumentRoot12(self):
        return self.__mtm_di_DocumentRoot12

    @mtm_di_DocumentRoot12.setter
    def mtm_di_DocumentRoot12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot12", None)
        self.__mtm_di_DocumentRoot12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_DiagramElement13"):
                    opp_val = getattr(item, "mtm_di_DiagramElement13", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_DiagramElement13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_DiagramElement13"):
                    opp_val = getattr(item, "mtm_di_DiagramElement13", None)
                    
                    setattr(item, "mtm_di_DiagramElement13", self)
                    

    @property
    def mtm_di_DocumentRoot27(self):
        return self.__mtm_di_DocumentRoot27

    @mtm_di_DocumentRoot27.setter
    def mtm_di_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot27", None)
        self.__mtm_di_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_Node"):
                    opp_val = getattr(item, "mtm_di_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_Node"):
                    opp_val = getattr(item, "mtm_di_Node", None)
                    
                    setattr(item, "mtm_di_Node", self)
                    

    @property
    def mtm_di_DocumentRoot15(self):
        return self.__mtm_di_DocumentRoot15

    @mtm_di_DocumentRoot15.setter
    def mtm_di_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot15", None)
        self.__mtm_di_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_Diagram"):
                    opp_val = getattr(item, "mtm_di_Diagram", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_Diagram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_Diagram"):
                    opp_val = getattr(item, "mtm_di_Diagram", None)
                    
                    setattr(item, "mtm_di_Diagram", self)
                    

    @property
    def mtm_di_DocumentRoot9(self):
        return self.__mtm_di_DocumentRoot9

    @mtm_di_DocumentRoot9.setter
    def mtm_di_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DocumentRoot__mtm_di_DocumentRoot9", None)
        self.__mtm_di_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_EStringToStringMapEntry10"):
                    opp_val = getattr(item, "mtm_di_EStringToStringMapEntry10", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_EStringToStringMapEntry10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_EStringToStringMapEntry10"):
                    opp_val = getattr(item, "mtm_di_EStringToStringMapEntry10", None)
                    
                    setattr(item, "mtm_di_EStringToStringMapEntry10", self)
                    

class mtm_di_Bounds:

    pass
class Node:

    pass
class mtm_di_Label(Node):

    pass
class mtm_di_Style(ABC):

    def __init__(self, id: str, mtm_di_Style: "mtm_di_DocumentRoot" = None):
        self.id = id
        self.mtm_di_Style = mtm_di_Style
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def mtm_di_Style(self):
        return self.__mtm_di_Style

    @mtm_di_Style.setter
    def mtm_di_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_Style__mtm_di_Style", None)
        self.__mtm_di_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtm_di_DocumentRoot35"):
                opp_val = getattr(old_value, "mtm_di_DocumentRoot35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtm_di_DocumentRoot35"):
                opp_val = getattr(value, "mtm_di_DocumentRoot35", None)
                if opp_val is None:
                    setattr(value, "mtm_di_DocumentRoot35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mtm_di_Shape(Node):

    pass
class mtm_di_Plane(Node):

    def __init__(self, diagramElementGroup: str, mtm_di_Plane: set["mtm_di_DiagramElement"] = None, mtm_di_Plane30: "mtm_di_DocumentRoot" = None):
        self.diagramElementGroup = diagramElementGroup
        self.mtm_di_Plane = mtm_di_Plane if mtm_di_Plane is not None else set()
        self.mtm_di_Plane30 = mtm_di_Plane30
        
    @property
    def diagramElementGroup(self) -> str:
        return self.__diagramElementGroup

    @diagramElementGroup.setter
    def diagramElementGroup(self, diagramElementGroup: str):
        self.__diagramElementGroup = diagramElementGroup

    @property
    def mtm_di_Plane(self):
        return self.__mtm_di_Plane

    @mtm_di_Plane.setter
    def mtm_di_Plane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_Plane__mtm_di_Plane", None)
        self.__mtm_di_Plane = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtm_di_DiagramElement4"):
                    opp_val = getattr(item, "mtm_di_DiagramElement4", None)
                    
                    if opp_val == self:
                        setattr(item, "mtm_di_DiagramElement4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtm_di_DiagramElement4"):
                    opp_val = getattr(item, "mtm_di_DiagramElement4", None)
                    
                    setattr(item, "mtm_di_DiagramElement4", self)
                    

    @property
    def mtm_di_Plane30(self):
        return self.__mtm_di_Plane30

    @mtm_di_Plane30.setter
    def mtm_di_Plane30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_Plane__mtm_di_Plane30", None)
        self.__mtm_di_Plane30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtm_di_DocumentRoot29"):
                opp_val = getattr(old_value, "mtm_di_DocumentRoot29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtm_di_DocumentRoot29"):
                opp_val = getattr(value, "mtm_di_DocumentRoot29", None)
                if opp_val is None:
                    setattr(value, "mtm_di_DocumentRoot29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Shape:

    pass
class mtm_di_LabeledShape(Shape):

    pass
class Edge:

    pass
class mtm_di_LabeledEdge(Edge):

    pass
class mtm_di_Diagram(ABC):

    def __init__(self, name: str, resolution: str, documentation: str, id: str, mtm_di_Diagram: "mtm_di_DocumentRoot" = None):
        self.name = name
        self.resolution = resolution
        self.documentation = documentation
        self.id = id
        self.mtm_di_Diagram = mtm_di_Diagram
        
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
    def mtm_di_Diagram(self):
        return self.__mtm_di_Diagram

    @mtm_di_Diagram.setter
    def mtm_di_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_Diagram__mtm_di_Diagram", None)
        self.__mtm_di_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtm_di_DocumentRoot15"):
                opp_val = getattr(old_value, "mtm_di_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtm_di_DocumentRoot15"):
                opp_val = getattr(value, "mtm_di_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "mtm_di_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mtm_di_Point:

    pass
class DiagramElement:

    pass
class mtm_di_Node(DiagramElement):

    pass
class mtm_di_Edge(DiagramElement):

    pass
class mtm_di_ExtensionType:

    def __init__(self, any: str, mtm_di_ExtensionType: "mtm_di_DiagramElement" = None):
        self.any = any
        self.mtm_di_ExtensionType = mtm_di_ExtensionType
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def mtm_di_ExtensionType(self):
        return self.__mtm_di_ExtensionType

    @mtm_di_ExtensionType.setter
    def mtm_di_ExtensionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_ExtensionType__mtm_di_ExtensionType", None)
        self.__mtm_di_ExtensionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtm_di_DiagramElement"):
                opp_val = getattr(old_value, "mtm_di_DiagramElement", None)
                if opp_val == self:
                    setattr(old_value, "mtm_di_DiagramElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtm_di_DiagramElement"):
                opp_val = getattr(value, "mtm_di_DiagramElement", None)
                setattr(value, "mtm_di_DiagramElement", self)

class mtm_di_DiagramElement(ABC):

    def __init__(self, id: str, anyAttribute: str, mtm_di_DiagramElement: "mtm_di_ExtensionType" = None, mtm_di_DiagramElement4: "mtm_di_Plane" = None, mtm_di_DiagramElement13: "mtm_di_DocumentRoot" = None):
        self.id = id
        self.anyAttribute = anyAttribute
        self.mtm_di_DiagramElement = mtm_di_DiagramElement
        self.mtm_di_DiagramElement4 = mtm_di_DiagramElement4
        self.mtm_di_DiagramElement13 = mtm_di_DiagramElement13
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def mtm_di_DiagramElement(self):
        return self.__mtm_di_DiagramElement

    @mtm_di_DiagramElement.setter
    def mtm_di_DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DiagramElement__mtm_di_DiagramElement", None)
        self.__mtm_di_DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtm_di_ExtensionType"):
                opp_val = getattr(old_value, "mtm_di_ExtensionType", None)
                if opp_val == self:
                    setattr(old_value, "mtm_di_ExtensionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtm_di_ExtensionType"):
                opp_val = getattr(value, "mtm_di_ExtensionType", None)
                setattr(value, "mtm_di_ExtensionType", self)

    @property
    def mtm_di_DiagramElement4(self):
        return self.__mtm_di_DiagramElement4

    @mtm_di_DiagramElement4.setter
    def mtm_di_DiagramElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DiagramElement__mtm_di_DiagramElement4", None)
        self.__mtm_di_DiagramElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtm_di_Plane"):
                opp_val = getattr(old_value, "mtm_di_Plane", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtm_di_Plane"):
                opp_val = getattr(value, "mtm_di_Plane", None)
                if opp_val is None:
                    setattr(value, "mtm_di_Plane", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mtm_di_DiagramElement13(self):
        return self.__mtm_di_DiagramElement13

    @mtm_di_DiagramElement13.setter
    def mtm_di_DiagramElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtm_di_DiagramElement__mtm_di_DiagramElement13", None)
        self.__mtm_di_DiagramElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtm_di_DocumentRoot12"):
                opp_val = getattr(old_value, "mtm_di_DocumentRoot12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtm_di_DocumentRoot12"):
                opp_val = getattr(value, "mtm_di_DocumentRoot12", None)
                if opp_val is None:
                    setattr(value, "mtm_di_DocumentRoot12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
