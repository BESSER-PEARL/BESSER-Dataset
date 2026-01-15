from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class editormodel_EStringToEObjectMapEntry:

    def __init__(self, key: str, editormodel_EStringToEObjectMapEntry: "editormodel_EObject" = None):
        self.key = key
        self.editormodel_EStringToEObjectMapEntry = editormodel_EStringToEObjectMapEntry
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def editormodel_EStringToEObjectMapEntry(self):
        return self.__editormodel_EStringToEObjectMapEntry

    @editormodel_EStringToEObjectMapEntry.setter
    def editormodel_EStringToEObjectMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_EStringToEObjectMapEntry__editormodel_EStringToEObjectMapEntry", None)
        self.__editormodel_EStringToEObjectMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_EObject60"):
                opp_val = getattr(old_value, "editormodel_EObject60", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_EObject60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_EObject60"):
                opp_val = getattr(value, "editormodel_EObject60", None)
                setattr(value, "editormodel_EObject60", self)

class editormodel_ConnectionBendpoint:

    def __init__(self, weight: float, editormodel_ConnectionBendpoint40: "editormodel_ConnectionVisualModel" = None, editormodel_ConnectionBendpoint: "editormodel_Dimension" = None, editormodel_ConnectionBendpoint37: "editormodel_Dimension" = None):
        self.weight = weight
        self.editormodel_ConnectionBendpoint40 = editormodel_ConnectionBendpoint40
        self.editormodel_ConnectionBendpoint = editormodel_ConnectionBendpoint
        self.editormodel_ConnectionBendpoint37 = editormodel_ConnectionBendpoint37
        
    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def editormodel_ConnectionBendpoint(self):
        return self.__editormodel_ConnectionBendpoint

    @editormodel_ConnectionBendpoint.setter
    def editormodel_ConnectionBendpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_ConnectionBendpoint__editormodel_ConnectionBendpoint", None)
        self.__editormodel_ConnectionBendpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Dimension35"):
                opp_val = getattr(old_value, "editormodel_Dimension35", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Dimension35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Dimension35"):
                opp_val = getattr(value, "editormodel_Dimension35", None)
                setattr(value, "editormodel_Dimension35", self)

    @property
    def editormodel_ConnectionBendpoint37(self):
        return self.__editormodel_ConnectionBendpoint37

    @editormodel_ConnectionBendpoint37.setter
    def editormodel_ConnectionBendpoint37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_ConnectionBendpoint__editormodel_ConnectionBendpoint37", None)
        self.__editormodel_ConnectionBendpoint37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Dimension38"):
                opp_val = getattr(old_value, "editormodel_Dimension38", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Dimension38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Dimension38"):
                opp_val = getattr(value, "editormodel_Dimension38", None)
                setattr(value, "editormodel_Dimension38", self)

    @property
    def editormodel_ConnectionBendpoint40(self):
        return self.__editormodel_ConnectionBendpoint40

    @editormodel_ConnectionBendpoint40.setter
    def editormodel_ConnectionBendpoint40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_ConnectionBendpoint__editormodel_ConnectionBendpoint40", None)
        self.__editormodel_ConnectionBendpoint40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_ConnectionVisualModel"):
                opp_val = getattr(old_value, "editormodel_ConnectionVisualModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_ConnectionVisualModel"):
                opp_val = getattr(value, "editormodel_ConnectionVisualModel", None)
                if opp_val is None:
                    setattr(value, "editormodel_ConnectionVisualModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class editormodel_Adapter(ABC):

    pass
class VisualModel:

    pass
class editormodel_NodeVisualModel(VisualModel):

    def __init__(self, rotation: str, NodeVisualModel: "editormodel_ConnectionVisualModel" = None, NodeVisualModel43: "editormodel_ConnectionVisualModel" = None, source: set["editormodel_ConnectionVisualModel"] = None, target: set["editormodel_ConnectionVisualModel"] = None, editormodel_NodeVisualModel: "editormodel_VisualDiagramJump" = None):
        self.rotation = rotation
        self.NodeVisualModel = NodeVisualModel
        self.NodeVisualModel43 = NodeVisualModel43
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.editormodel_NodeVisualModel = editormodel_NodeVisualModel
        
    @property
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_NodeVisualModel__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConnectionVisualModel"):
                    opp_val = getattr(item, "ConnectionVisualModel", None)
                    
                    if opp_val == self:
                        setattr(item, "ConnectionVisualModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConnectionVisualModel"):
                    opp_val = getattr(item, "ConnectionVisualModel", None)
                    
                    setattr(item, "ConnectionVisualModel", self)
                    

    @property
    def NodeVisualModel(self):
        return self.__NodeVisualModel

    @NodeVisualModel.setter
    def NodeVisualModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_NodeVisualModel__NodeVisualModel", None)
        self.__NodeVisualModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceConnections"):
                opp_val = getattr(old_value, "sourceConnections", None)
                if opp_val == self:
                    setattr(old_value, "sourceConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceConnections"):
                opp_val = getattr(value, "sourceConnections", None)
                setattr(value, "sourceConnections", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_NodeVisualModel__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConnectionVisualModel46"):
                    opp_val = getattr(item, "ConnectionVisualModel46", None)
                    
                    if opp_val == self:
                        setattr(item, "ConnectionVisualModel46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConnectionVisualModel46"):
                    opp_val = getattr(item, "ConnectionVisualModel46", None)
                    
                    setattr(item, "ConnectionVisualModel46", self)
                    

    @property
    def NodeVisualModel43(self):
        return self.__NodeVisualModel43

    @NodeVisualModel43.setter
    def NodeVisualModel43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_NodeVisualModel__NodeVisualModel43", None)
        self.__NodeVisualModel43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetConnections"):
                opp_val = getattr(old_value, "targetConnections", None)
                if opp_val == self:
                    setattr(old_value, "targetConnections", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetConnections"):
                opp_val = getattr(value, "targetConnections", None)
                setattr(value, "targetConnections", self)

    @property
    def editormodel_NodeVisualModel(self):
        return self.__editormodel_NodeVisualModel

    @editormodel_NodeVisualModel.setter
    def editormodel_NodeVisualModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_NodeVisualModel__editormodel_NodeVisualModel", None)
        self.__editormodel_NodeVisualModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_VisualDiagramJump67"):
                opp_val = getattr(old_value, "editormodel_VisualDiagramJump67", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_VisualDiagramJump67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_VisualDiagramJump67"):
                opp_val = getattr(value, "editormodel_VisualDiagramJump67", None)
                setattr(value, "editormodel_VisualDiagramJump67", self)

class NodeVisualModel:

    pass
class editormodel_VisualDiagramJump(NodeVisualModel):

    def __init__(self, to: str, editormodel_VisualDiagramJump64: "editormodel_Diagram" = None, editormodel_VisualDiagramJump67: "editormodel_NodeVisualModel" = None, editormodel_VisualDiagramJump: "editormodel_Diagram" = None):
        self.to = to
        self.editormodel_VisualDiagramJump64 = editormodel_VisualDiagramJump64
        self.editormodel_VisualDiagramJump67 = editormodel_VisualDiagramJump67
        self.editormodel_VisualDiagramJump = editormodel_VisualDiagramJump
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def editormodel_VisualDiagramJump64(self):
        return self.__editormodel_VisualDiagramJump64

    @editormodel_VisualDiagramJump64.setter
    def editormodel_VisualDiagramJump64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualDiagramJump__editormodel_VisualDiagramJump64", None)
        self.__editormodel_VisualDiagramJump64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Diagram65"):
                opp_val = getattr(old_value, "editormodel_Diagram65", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Diagram65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Diagram65"):
                opp_val = getattr(value, "editormodel_Diagram65", None)
                setattr(value, "editormodel_Diagram65", self)

    @property
    def editormodel_VisualDiagramJump(self):
        return self.__editormodel_VisualDiagramJump

    @editormodel_VisualDiagramJump.setter
    def editormodel_VisualDiagramJump(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualDiagramJump__editormodel_VisualDiagramJump", None)
        self.__editormodel_VisualDiagramJump = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Diagram62"):
                opp_val = getattr(old_value, "editormodel_Diagram62", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Diagram62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Diagram62"):
                opp_val = getattr(value, "editormodel_Diagram62", None)
                setattr(value, "editormodel_Diagram62", self)

    @property
    def editormodel_VisualDiagramJump67(self):
        return self.__editormodel_VisualDiagramJump67

    @editormodel_VisualDiagramJump67.setter
    def editormodel_VisualDiagramJump67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualDiagramJump__editormodel_VisualDiagramJump67", None)
        self.__editormodel_VisualDiagramJump67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_NodeVisualModel"):
                opp_val = getattr(old_value, "editormodel_NodeVisualModel", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_NodeVisualModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_NodeVisualModel"):
                opp_val = getattr(value, "editormodel_NodeVisualModel", None)
                setattr(value, "editormodel_NodeVisualModel", self)

class editormodel_ConnectionVisualModel(NodeVisualModel):

    def __init__(self, sourceTerminal: str, targetTerminal: str, editormodel_ConnectionVisualModel: set["editormodel_ConnectionBendpoint"] = None, sourceConnections: "editormodel_NodeVisualModel" = None, targetConnections: "editormodel_NodeVisualModel" = None, ConnectionVisualModel: "editormodel_NodeVisualModel" = None, ConnectionVisualModel46: "editormodel_NodeVisualModel" = None):
        self.sourceTerminal = sourceTerminal
        self.targetTerminal = targetTerminal
        self.editormodel_ConnectionVisualModel = editormodel_ConnectionVisualModel if editormodel_ConnectionVisualModel is not None else set()
        self.sourceConnections = sourceConnections
        self.targetConnections = targetConnections
        self.ConnectionVisualModel = ConnectionVisualModel
        self.ConnectionVisualModel46 = ConnectionVisualModel46
        
    @property
    def sourceTerminal(self) -> str:
        return self.__sourceTerminal

    @sourceTerminal.setter
    def sourceTerminal(self, sourceTerminal: str):
        self.__sourceTerminal = sourceTerminal

    @property
    def targetTerminal(self) -> str:
        return self.__targetTerminal

    @targetTerminal.setter
    def targetTerminal(self, targetTerminal: str):
        self.__targetTerminal = targetTerminal

    @property
    def ConnectionVisualModel(self):
        return self.__ConnectionVisualModel

    @ConnectionVisualModel.setter
    def ConnectionVisualModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_ConnectionVisualModel__ConnectionVisualModel", None)
        self.__ConnectionVisualModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def editormodel_ConnectionVisualModel(self):
        return self.__editormodel_ConnectionVisualModel

    @editormodel_ConnectionVisualModel.setter
    def editormodel_ConnectionVisualModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_ConnectionVisualModel__editormodel_ConnectionVisualModel", None)
        self.__editormodel_ConnectionVisualModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "editormodel_ConnectionBendpoint40"):
                    opp_val = getattr(item, "editormodel_ConnectionBendpoint40", None)
                    
                    if opp_val == self:
                        setattr(item, "editormodel_ConnectionBendpoint40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "editormodel_ConnectionBendpoint40"):
                    opp_val = getattr(item, "editormodel_ConnectionBendpoint40", None)
                    
                    setattr(item, "editormodel_ConnectionBendpoint40", self)
                    

    @property
    def targetConnections(self):
        return self.__targetConnections

    @targetConnections.setter
    def targetConnections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_ConnectionVisualModel__targetConnections", None)
        self.__targetConnections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeVisualModel43"):
                opp_val = getattr(old_value, "NodeVisualModel43", None)
                if opp_val == self:
                    setattr(old_value, "NodeVisualModel43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeVisualModel43"):
                opp_val = getattr(value, "NodeVisualModel43", None)
                setattr(value, "NodeVisualModel43", self)

    @property
    def sourceConnections(self):
        return self.__sourceConnections

    @sourceConnections.setter
    def sourceConnections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_ConnectionVisualModel__sourceConnections", None)
        self.__sourceConnections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeVisualModel"):
                opp_val = getattr(old_value, "NodeVisualModel", None)
                if opp_val == self:
                    setattr(old_value, "NodeVisualModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeVisualModel"):
                opp_val = getattr(value, "NodeVisualModel", None)
                setattr(value, "NodeVisualModel", self)

    @property
    def ConnectionVisualModel46(self):
        return self.__ConnectionVisualModel46

    @ConnectionVisualModel46.setter
    def ConnectionVisualModel46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_ConnectionVisualModel__ConnectionVisualModel46", None)
        self.__ConnectionVisualModel46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Adapter:

    pass
class editormodel_Color:

    def __init__(self, red: int, green: int, blue: int, editormodel_Color: "editormodel_VisualModel" = None, editormodel_Color33: "editormodel_VisualModel" = None):
        self.red = red
        self.green = green
        self.blue = blue
        self.editormodel_Color = editormodel_Color
        self.editormodel_Color33 = editormodel_Color33
        
    @property
    def red(self) -> int:
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red

    @property
    def blue(self) -> int:
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue

    @property
    def green(self) -> int:
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green

    @property
    def editormodel_Color(self):
        return self.__editormodel_Color

    @editormodel_Color.setter
    def editormodel_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Color__editormodel_Color", None)
        self.__editormodel_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_VisualModel30"):
                opp_val = getattr(old_value, "editormodel_VisualModel30", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_VisualModel30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_VisualModel30"):
                opp_val = getattr(value, "editormodel_VisualModel30", None)
                setattr(value, "editormodel_VisualModel30", self)

    @property
    def editormodel_Color33(self):
        return self.__editormodel_Color33

    @editormodel_Color33.setter
    def editormodel_Color33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Color__editormodel_Color33", None)
        self.__editormodel_Color33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_VisualModel32"):
                opp_val = getattr(old_value, "editormodel_VisualModel32", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_VisualModel32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_VisualModel32"):
                opp_val = getattr(value, "editormodel_VisualModel32", None)
                setattr(value, "editormodel_VisualModel32", self)

class editormodel_Dimension:

    def __init__(self, width: int, height: int, editormodel_Dimension: "editormodel_VisualModel" = None, editormodel_Dimension35: "editormodel_ConnectionBendpoint" = None, editormodel_Dimension38: "editormodel_ConnectionBendpoint" = None):
        self.width = width
        self.height = height
        self.editormodel_Dimension = editormodel_Dimension
        self.editormodel_Dimension35 = editormodel_Dimension35
        self.editormodel_Dimension38 = editormodel_Dimension38
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def editormodel_Dimension(self):
        return self.__editormodel_Dimension

    @editormodel_Dimension.setter
    def editormodel_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Dimension__editormodel_Dimension", None)
        self.__editormodel_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_VisualModel26"):
                opp_val = getattr(old_value, "editormodel_VisualModel26", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_VisualModel26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_VisualModel26"):
                opp_val = getattr(value, "editormodel_VisualModel26", None)
                setattr(value, "editormodel_VisualModel26", self)

    @property
    def editormodel_Dimension38(self):
        return self.__editormodel_Dimension38

    @editormodel_Dimension38.setter
    def editormodel_Dimension38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Dimension__editormodel_Dimension38", None)
        self.__editormodel_Dimension38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_ConnectionBendpoint37"):
                opp_val = getattr(old_value, "editormodel_ConnectionBendpoint37", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_ConnectionBendpoint37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_ConnectionBendpoint37"):
                opp_val = getattr(value, "editormodel_ConnectionBendpoint37", None)
                setattr(value, "editormodel_ConnectionBendpoint37", self)

    @property
    def editormodel_Dimension35(self):
        return self.__editormodel_Dimension35

    @editormodel_Dimension35.setter
    def editormodel_Dimension35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Dimension__editormodel_Dimension35", None)
        self.__editormodel_Dimension35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_ConnectionBendpoint"):
                opp_val = getattr(old_value, "editormodel_ConnectionBendpoint", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_ConnectionBendpoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_ConnectionBendpoint"):
                opp_val = getattr(value, "editormodel_ConnectionBendpoint", None)
                setattr(value, "editormodel_ConnectionBendpoint", self)

class editormodel_Point:

    def __init__(self, x: int, y: int, editormodel_Point: "editormodel_VisualModel" = None):
        self.x = x
        self.y = y
        self.editormodel_Point = editormodel_Point
        
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
    def editormodel_Point(self):
        return self.__editormodel_Point

    @editormodel_Point.setter
    def editormodel_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Point__editormodel_Point", None)
        self.__editormodel_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_VisualModel24"):
                opp_val = getattr(old_value, "editormodel_VisualModel24", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_VisualModel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_VisualModel24"):
                opp_val = getattr(value, "editormodel_VisualModel24", None)
                setattr(value, "editormodel_VisualModel24", self)

class editormodel_EObject:

    pass
class editormodel_Folder:

    def __init__(self, name: str, Folder: "editormodel_Diagram" = None, editormodel_Folder: "editormodel_FlabotFileModel" = None, folder: set["editormodel_Diagram"] = None, Folder55: "editormodel_Folder" = None, folders: "editormodel_Folder" = None, editormodel_Folder57: "editormodel_FlabotFileModel" = None, Folder50: "editormodel_Folder" = None, parent49: set["editormodel_Folder"] = None):
        self.name = name
        self.Folder = Folder
        self.editormodel_Folder = editormodel_Folder
        self.folder = folder if folder is not None else set()
        self.Folder55 = Folder55
        self.folders = folders
        self.editormodel_Folder57 = editormodel_Folder57
        self.Folder50 = Folder50
        self.parent49 = parent49 if parent49 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def editormodel_Folder57(self):
        return self.__editormodel_Folder57

    @editormodel_Folder57.setter
    def editormodel_Folder57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Folder__editormodel_Folder57", None)
        self.__editormodel_Folder57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_FlabotFileModel58"):
                opp_val = getattr(old_value, "editormodel_FlabotFileModel58", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_FlabotFileModel58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_FlabotFileModel58"):
                opp_val = getattr(value, "editormodel_FlabotFileModel58", None)
                setattr(value, "editormodel_FlabotFileModel58", self)

    @property
    def Folder(self):
        return self.__Folder

    @Folder.setter
    def Folder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Folder__Folder", None)
        self.__Folder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagrams"):
                opp_val = getattr(old_value, "diagrams", None)
                if opp_val == self:
                    setattr(old_value, "diagrams", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagrams"):
                opp_val = getattr(value, "diagrams", None)
                setattr(value, "diagrams", self)

    @property
    def parent49(self):
        return self.__parent49

    @parent49.setter
    def parent49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Folder__parent49", None)
        self.__parent49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Folder50"):
                    opp_val = getattr(item, "Folder50", None)
                    
                    if opp_val == self:
                        setattr(item, "Folder50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Folder50"):
                    opp_val = getattr(item, "Folder50", None)
                    
                    setattr(item, "Folder50", self)
                    

    @property
    def Folder55(self):
        return self.__Folder55

    @Folder55.setter
    def Folder55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Folder__Folder55", None)
        self.__Folder55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "folders"):
                opp_val = getattr(old_value, "folders", None)
                if opp_val == self:
                    setattr(old_value, "folders", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "folders"):
                opp_val = getattr(value, "folders", None)
                setattr(value, "folders", self)

    @property
    def folders(self):
        return self.__folders

    @folders.setter
    def folders(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Folder__folders", None)
        self.__folders = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Folder55"):
                opp_val = getattr(old_value, "Folder55", None)
                if opp_val == self:
                    setattr(old_value, "Folder55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Folder55"):
                opp_val = getattr(value, "Folder55", None)
                setattr(value, "Folder55", self)

    @property
    def folder(self):
        return self.__folder

    @folder.setter
    def folder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Folder__folder", None)
        self.__folder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Diagram52"):
                    opp_val = getattr(item, "Diagram52", None)
                    
                    if opp_val == self:
                        setattr(item, "Diagram52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Diagram52"):
                    opp_val = getattr(item, "Diagram52", None)
                    
                    setattr(item, "Diagram52", self)
                    

    @property
    def editormodel_Folder(self):
        return self.__editormodel_Folder

    @editormodel_Folder.setter
    def editormodel_Folder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Folder__editormodel_Folder", None)
        self.__editormodel_Folder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_FlabotFileModel12"):
                opp_val = getattr(old_value, "editormodel_FlabotFileModel12", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_FlabotFileModel12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_FlabotFileModel12"):
                opp_val = getattr(value, "editormodel_FlabotFileModel12", None)
                setattr(value, "editormodel_FlabotFileModel12", self)

    @property
    def Folder50(self):
        return self.__Folder50

    @Folder50.setter
    def Folder50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Folder__Folder50", None)
        self.__Folder50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent49"):
                opp_val = getattr(old_value, "parent49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent49"):
                opp_val = getattr(value, "parent49", None)
                if opp_val is None:
                    setattr(value, "parent49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class editormodel_VisualModel(Adapter):

    def __init__(self, lineStyle: int, lineWidth: int, detailLevel: int, VisualModel: "editormodel_Diagram" = None, VisualModel21: "editormodel_VisualModel" = None, children: "editormodel_VisualModel" = None, editormodel_VisualModel: "editormodel_EObject" = None, editormodel_VisualModel24: "editormodel_Point" = None, editormodel_VisualModel26: "editormodel_Dimension" = None, children28: "editormodel_Diagram" = None, editormodel_VisualModel30: "editormodel_Color" = None, VisualModel18: "editormodel_VisualModel" = None, parent: set["editormodel_VisualModel"] = None, editormodel_VisualModel32: "editormodel_Color" = None):
        self.lineStyle = lineStyle
        self.lineWidth = lineWidth
        self.detailLevel = detailLevel
        self.VisualModel = VisualModel
        self.VisualModel21 = VisualModel21
        self.children = children
        self.editormodel_VisualModel = editormodel_VisualModel
        self.editormodel_VisualModel24 = editormodel_VisualModel24
        self.editormodel_VisualModel26 = editormodel_VisualModel26
        self.children28 = children28
        self.editormodel_VisualModel30 = editormodel_VisualModel30
        self.VisualModel18 = VisualModel18
        self.parent = parent if parent is not None else set()
        self.editormodel_VisualModel32 = editormodel_VisualModel32
        
    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def detailLevel(self) -> int:
        return self.__detailLevel

    @detailLevel.setter
    def detailLevel(self, detailLevel: int):
        self.__detailLevel = detailLevel

    @property
    def lineStyle(self) -> int:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: int):
        self.__lineStyle = lineStyle

    @property
    def VisualModel(self):
        return self.__VisualModel

    @VisualModel.setter
    def VisualModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__VisualModel", None)
        self.__VisualModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram"):
                opp_val = getattr(old_value, "diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram"):
                opp_val = getattr(value, "diagram", None)
                if opp_val is None:
                    setattr(value, "diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def editormodel_VisualModel32(self):
        return self.__editormodel_VisualModel32

    @editormodel_VisualModel32.setter
    def editormodel_VisualModel32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__editormodel_VisualModel32", None)
        self.__editormodel_VisualModel32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Color33"):
                opp_val = getattr(old_value, "editormodel_Color33", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Color33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Color33"):
                opp_val = getattr(value, "editormodel_Color33", None)
                setattr(value, "editormodel_Color33", self)

    @property
    def VisualModel21(self):
        return self.__VisualModel21

    @VisualModel21.setter
    def VisualModel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__VisualModel21", None)
        self.__VisualModel21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def editormodel_VisualModel24(self):
        return self.__editormodel_VisualModel24

    @editormodel_VisualModel24.setter
    def editormodel_VisualModel24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__editormodel_VisualModel24", None)
        self.__editormodel_VisualModel24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Point"):
                opp_val = getattr(old_value, "editormodel_Point", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Point"):
                opp_val = getattr(value, "editormodel_Point", None)
                setattr(value, "editormodel_Point", self)

    @property
    def children28(self):
        return self.__children28

    @children28.setter
    def children28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__children28", None)
        self.__children28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Diagram"):
                opp_val = getattr(old_value, "Diagram", None)
                if opp_val == self:
                    setattr(old_value, "Diagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Diagram"):
                opp_val = getattr(value, "Diagram", None)
                setattr(value, "Diagram", self)

    @property
    def VisualModel18(self):
        return self.__VisualModel18

    @VisualModel18.setter
    def VisualModel18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__VisualModel18", None)
        self.__VisualModel18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualModel18"):
                    opp_val = getattr(item, "VisualModel18", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualModel18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualModel18"):
                    opp_val = getattr(item, "VisualModel18", None)
                    
                    setattr(item, "VisualModel18", self)
                    

    @property
    def editormodel_VisualModel(self):
        return self.__editormodel_VisualModel

    @editormodel_VisualModel.setter
    def editormodel_VisualModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__editormodel_VisualModel", None)
        self.__editormodel_VisualModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_EObject"):
                opp_val = getattr(old_value, "editormodel_EObject", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_EObject"):
                opp_val = getattr(value, "editormodel_EObject", None)
                setattr(value, "editormodel_EObject", self)

    @property
    def editormodel_VisualModel30(self):
        return self.__editormodel_VisualModel30

    @editormodel_VisualModel30.setter
    def editormodel_VisualModel30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__editormodel_VisualModel30", None)
        self.__editormodel_VisualModel30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Color"):
                opp_val = getattr(old_value, "editormodel_Color", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Color"):
                opp_val = getattr(value, "editormodel_Color", None)
                setattr(value, "editormodel_Color", self)

    @property
    def editormodel_VisualModel26(self):
        return self.__editormodel_VisualModel26

    @editormodel_VisualModel26.setter
    def editormodel_VisualModel26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__editormodel_VisualModel26", None)
        self.__editormodel_VisualModel26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Dimension"):
                opp_val = getattr(old_value, "editormodel_Dimension", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Dimension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Dimension"):
                opp_val = getattr(value, "editormodel_Dimension", None)
                setattr(value, "editormodel_Dimension", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_VisualModel__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualModel21"):
                opp_val = getattr(old_value, "VisualModel21", None)
                if opp_val == self:
                    setattr(old_value, "VisualModel21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualModel21"):
                opp_val = getattr(value, "VisualModel21", None)
                setattr(value, "VisualModel21", self)

class editormodel_Note:

    pass
class editormodel_CoreModel:

    pass
class NamedElementModel:

    pass
class ExtensibleElement:

    pass
class editormodel_FlabotFileModel(ExtensibleElement):

    def __init__(self, id: str, version: str, name: str, provider: str, file: "editormodel_CoreModel" = None, editormodel_FlabotFileModel: set["editormodel_Diagram"] = None, editormodel_FlabotFileModel10: "editormodel_FlabotFileModel" = None, editormodel_FlabotFileModel8: set["editormodel_FlabotFileModel"] = None, editormodel_FlabotFileModel12: "editormodel_Folder" = None, editormodel_FlabotFileModel14: set["editormodel_Diagram"] = None, editormodel_FlabotFileModel58: "editormodel_Folder" = None):
        self.id = id
        self.version = version
        self.name = name
        self.provider = provider
        self.file = file
        self.editormodel_FlabotFileModel = editormodel_FlabotFileModel if editormodel_FlabotFileModel is not None else set()
        self.editormodel_FlabotFileModel10 = editormodel_FlabotFileModel10
        self.editormodel_FlabotFileModel8 = editormodel_FlabotFileModel8 if editormodel_FlabotFileModel8 is not None else set()
        self.editormodel_FlabotFileModel12 = editormodel_FlabotFileModel12
        self.editormodel_FlabotFileModel14 = editormodel_FlabotFileModel14 if editormodel_FlabotFileModel14 is not None else set()
        self.editormodel_FlabotFileModel58 = editormodel_FlabotFileModel58
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def provider(self) -> str:
        return self.__provider

    @provider.setter
    def provider(self, provider: str):
        self.__provider = provider

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_FlabotFileModel__file", None)
        self.__file = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coremodel.ecoreCoreModel"):
                opp_val = getattr(old_value, "coremodel.ecoreCoreModel", None)
                if opp_val == self:
                    setattr(old_value, "coremodel.ecoreCoreModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coremodel.ecoreCoreModel"):
                opp_val = getattr(value, "coremodel.ecoreCoreModel", None)
                setattr(value, "coremodel.ecoreCoreModel", self)

    @property
    def editormodel_FlabotFileModel10(self):
        return self.__editormodel_FlabotFileModel10

    @editormodel_FlabotFileModel10.setter
    def editormodel_FlabotFileModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_FlabotFileModel__editormodel_FlabotFileModel10", None)
        self.__editormodel_FlabotFileModel10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_FlabotFileModel8"):
                opp_val = getattr(old_value, "editormodel_FlabotFileModel8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_FlabotFileModel8"):
                opp_val = getattr(value, "editormodel_FlabotFileModel8", None)
                if opp_val is None:
                    setattr(value, "editormodel_FlabotFileModel8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def editormodel_FlabotFileModel8(self):
        return self.__editormodel_FlabotFileModel8

    @editormodel_FlabotFileModel8.setter
    def editormodel_FlabotFileModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_FlabotFileModel__editormodel_FlabotFileModel8", None)
        self.__editormodel_FlabotFileModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "editormodel_FlabotFileModel10"):
                    opp_val = getattr(item, "editormodel_FlabotFileModel10", None)
                    
                    if opp_val == self:
                        setattr(item, "editormodel_FlabotFileModel10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "editormodel_FlabotFileModel10"):
                    opp_val = getattr(item, "editormodel_FlabotFileModel10", None)
                    
                    setattr(item, "editormodel_FlabotFileModel10", self)
                    

    @property
    def editormodel_FlabotFileModel14(self):
        return self.__editormodel_FlabotFileModel14

    @editormodel_FlabotFileModel14.setter
    def editormodel_FlabotFileModel14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_FlabotFileModel__editormodel_FlabotFileModel14", None)
        self.__editormodel_FlabotFileModel14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "editormodel_Diagram15"):
                    opp_val = getattr(item, "editormodel_Diagram15", None)
                    
                    if opp_val == self:
                        setattr(item, "editormodel_Diagram15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "editormodel_Diagram15"):
                    opp_val = getattr(item, "editormodel_Diagram15", None)
                    
                    setattr(item, "editormodel_Diagram15", self)
                    

    @property
    def editormodel_FlabotFileModel(self):
        return self.__editormodel_FlabotFileModel

    @editormodel_FlabotFileModel.setter
    def editormodel_FlabotFileModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_FlabotFileModel__editormodel_FlabotFileModel", None)
        self.__editormodel_FlabotFileModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "editormodel_Diagram7"):
                    opp_val = getattr(item, "editormodel_Diagram7", None)
                    
                    if opp_val == self:
                        setattr(item, "editormodel_Diagram7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "editormodel_Diagram7"):
                    opp_val = getattr(item, "editormodel_Diagram7", None)
                    
                    setattr(item, "editormodel_Diagram7", self)
                    

    @property
    def editormodel_FlabotFileModel58(self):
        return self.__editormodel_FlabotFileModel58

    @editormodel_FlabotFileModel58.setter
    def editormodel_FlabotFileModel58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_FlabotFileModel__editormodel_FlabotFileModel58", None)
        self.__editormodel_FlabotFileModel58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Folder57"):
                opp_val = getattr(old_value, "editormodel_Folder57", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Folder57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Folder57"):
                opp_val = getattr(value, "editormodel_Folder57", None)
                setattr(value, "editormodel_Folder57", self)

    @property
    def editormodel_FlabotFileModel12(self):
        return self.__editormodel_FlabotFileModel12

    @editormodel_FlabotFileModel12.setter
    def editormodel_FlabotFileModel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_FlabotFileModel__editormodel_FlabotFileModel12", None)
        self.__editormodel_FlabotFileModel12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_Folder"):
                opp_val = getattr(old_value, "editormodel_Folder", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_Folder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_Folder"):
                opp_val = getattr(value, "editormodel_Folder", None)
                setattr(value, "editormodel_Folder", self)

class editormodel_Diagram(NamedElementModel):

    def __init__(self, gridEnabled: str, snapToGeometryEnabled: str, editormodel_Diagram7: "editormodel_FlabotFileModel" = None, editormodel_Diagram: "editormodel_CoreModel" = None, editormodel_Diagram2: set["editormodel_Note"] = None, diagram: set["editormodel_VisualModel"] = None, diagrams: "editormodel_Folder" = None, Diagram: "editormodel_VisualModel" = None, editormodel_Diagram15: "editormodel_FlabotFileModel" = None, Diagram52: "editormodel_Folder" = None, editormodel_Diagram65: "editormodel_VisualDiagramJump" = None, editormodel_Diagram62: "editormodel_VisualDiagramJump" = None):
        self.gridEnabled = gridEnabled
        self.snapToGeometryEnabled = snapToGeometryEnabled
        self.editormodel_Diagram7 = editormodel_Diagram7
        self.editormodel_Diagram = editormodel_Diagram
        self.editormodel_Diagram2 = editormodel_Diagram2 if editormodel_Diagram2 is not None else set()
        self.diagram = diagram if diagram is not None else set()
        self.diagrams = diagrams
        self.Diagram = Diagram
        self.editormodel_Diagram15 = editormodel_Diagram15
        self.Diagram52 = Diagram52
        self.editormodel_Diagram65 = editormodel_Diagram65
        self.editormodel_Diagram62 = editormodel_Diagram62
        
    @property
    def gridEnabled(self) -> str:
        return self.__gridEnabled

    @gridEnabled.setter
    def gridEnabled(self, gridEnabled: str):
        self.__gridEnabled = gridEnabled

    @property
    def snapToGeometryEnabled(self) -> str:
        return self.__snapToGeometryEnabled

    @snapToGeometryEnabled.setter
    def snapToGeometryEnabled(self, snapToGeometryEnabled: str):
        self.__snapToGeometryEnabled = snapToGeometryEnabled

    @property
    def diagram(self):
        return self.__diagram

    @diagram.setter
    def diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__diagram", None)
        self.__diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualModel"):
                    opp_val = getattr(item, "VisualModel", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualModel"):
                    opp_val = getattr(item, "VisualModel", None)
                    
                    setattr(item, "VisualModel", self)
                    

    @property
    def editormodel_Diagram62(self):
        return self.__editormodel_Diagram62

    @editormodel_Diagram62.setter
    def editormodel_Diagram62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__editormodel_Diagram62", None)
        self.__editormodel_Diagram62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_VisualDiagramJump"):
                opp_val = getattr(old_value, "editormodel_VisualDiagramJump", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_VisualDiagramJump", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_VisualDiagramJump"):
                opp_val = getattr(value, "editormodel_VisualDiagramJump", None)
                setattr(value, "editormodel_VisualDiagramJump", self)

    @property
    def diagrams(self):
        return self.__diagrams

    @diagrams.setter
    def diagrams(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__diagrams", None)
        self.__diagrams = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Folder"):
                opp_val = getattr(old_value, "Folder", None)
                if opp_val == self:
                    setattr(old_value, "Folder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Folder"):
                opp_val = getattr(value, "Folder", None)
                setattr(value, "Folder", self)

    @property
    def editormodel_Diagram15(self):
        return self.__editormodel_Diagram15

    @editormodel_Diagram15.setter
    def editormodel_Diagram15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__editormodel_Diagram15", None)
        self.__editormodel_Diagram15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_FlabotFileModel14"):
                opp_val = getattr(old_value, "editormodel_FlabotFileModel14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_FlabotFileModel14"):
                opp_val = getattr(value, "editormodel_FlabotFileModel14", None)
                if opp_val is None:
                    setattr(value, "editormodel_FlabotFileModel14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def editormodel_Diagram2(self):
        return self.__editormodel_Diagram2

    @editormodel_Diagram2.setter
    def editormodel_Diagram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__editormodel_Diagram2", None)
        self.__editormodel_Diagram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "editormodel_Note"):
                    opp_val = getattr(item, "editormodel_Note", None)
                    
                    if opp_val == self:
                        setattr(item, "editormodel_Note", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "editormodel_Note"):
                    opp_val = getattr(item, "editormodel_Note", None)
                    
                    setattr(item, "editormodel_Note", self)
                    

    @property
    def editormodel_Diagram7(self):
        return self.__editormodel_Diagram7

    @editormodel_Diagram7.setter
    def editormodel_Diagram7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__editormodel_Diagram7", None)
        self.__editormodel_Diagram7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_FlabotFileModel"):
                opp_val = getattr(old_value, "editormodel_FlabotFileModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_FlabotFileModel"):
                opp_val = getattr(value, "editormodel_FlabotFileModel", None)
                if opp_val is None:
                    setattr(value, "editormodel_FlabotFileModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def editormodel_Diagram(self):
        return self.__editormodel_Diagram

    @editormodel_Diagram.setter
    def editormodel_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__editormodel_Diagram", None)
        self.__editormodel_Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_CoreModel"):
                opp_val = getattr(old_value, "editormodel_CoreModel", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_CoreModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_CoreModel"):
                opp_val = getattr(value, "editormodel_CoreModel", None)
                setattr(value, "editormodel_CoreModel", self)

    @property
    def Diagram(self):
        return self.__Diagram

    @Diagram.setter
    def Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__Diagram", None)
        self.__Diagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children28"):
                opp_val = getattr(old_value, "children28", None)
                if opp_val == self:
                    setattr(old_value, "children28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children28"):
                opp_val = getattr(value, "children28", None)
                setattr(value, "children28", self)

    @property
    def Diagram52(self):
        return self.__Diagram52

    @Diagram52.setter
    def Diagram52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__Diagram52", None)
        self.__Diagram52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "folder"):
                opp_val = getattr(old_value, "folder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "folder"):
                opp_val = getattr(value, "folder", None)
                if opp_val is None:
                    setattr(value, "folder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def editormodel_Diagram65(self):
        return self.__editormodel_Diagram65

    @editormodel_Diagram65.setter
    def editormodel_Diagram65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_editormodel_Diagram__editormodel_Diagram65", None)
        self.__editormodel_Diagram65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editormodel_VisualDiagramJump64"):
                opp_val = getattr(old_value, "editormodel_VisualDiagramJump64", None)
                if opp_val == self:
                    setattr(old_value, "editormodel_VisualDiagramJump64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editormodel_VisualDiagramJump64"):
                opp_val = getattr(value, "editormodel_VisualDiagramJump64", None)
                setattr(value, "editormodel_VisualDiagramJump64", self)
