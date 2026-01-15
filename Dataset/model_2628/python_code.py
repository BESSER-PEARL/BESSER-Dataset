from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ContainmentKind(Enum):
    FREE = "FREE"
    HORIZONTAL_ARRANGEMENT = "HORIZONTAL_ARRANGEMENT"
    VERTICAL_ARRANGEMENT = "VERTICAL_ARRANGEMENT"
    EXTERNAL_LINK = "EXTERNAL_LINK"
class ShapeKind(Enum):
    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"
    RECTANGLE = "RECTANGLE"
    ELLIPSE = "ELLIPSE"
    DIAMOND = "DIAMOND"
    TRIANGLE = "TRIANGLE"
class OutlineKind(Enum):
    SIMPLE = "SIMPLE"
    DOUBLE = "DOUBLE"
    NONE = "NONE"
class LineKind(Enum):
    SOLID = "SOLID"
    DASHED = "DASHED"
    DOTTED = "DOTTED"
class QueryLanguageKind(Enum):
    LINQ = "LINQ"
    JPQL = "JPQL"
    SQL = "SQL"
    AQL = "AQL"
    OCL = "OCL"
    XPATH_XQUERY = "XPATH_XQUERY"
class IntegrityRestrictionKind(Enum):
    CASCADE = "CASCADE"
    SET_NULL = "SET_NULL"
    NO_ACTION = "NO_ACTION"


############################################
# Definition of Classes
############################################

class SupportOperation:

    pass
class aredsl_ShowSystemMenu(SupportOperation):

    pass
class aredsl_ArrangeElements(SupportOperation):

    pass
class aredsl_Exit(SupportOperation):

    pass
class aredsl_MoveElement(SupportOperation):

    pass
class TrackerAction:

    pass
class aredsl_MarkerLessTrackerAction(TrackerAction):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class aredsl_MarkerBasedTrackerAction(TrackerAction):

    def __init__(self, markerId: int):
        self.markerId = markerId
        
    @property
    def markerId(self) -> int:
        return self.__markerId

    @markerId.setter
    def markerId(self, markerId: int):
        self.__markerId = markerId

class Action:

    pass
class aredsl_TactileAction(Action):

    pass
class aredsl_VoiceAction(Action):

    pass
class aredsl_MentalAction(Action):

    pass
class aredsl_GestureAction(Action):

    pass
class aredsl_SensorBasedAction(Action):

    pass
class DomainOperation:

    pass
class aredsl_UnsetOperation(DomainOperation):

    def __init__(self, feature: str, constraint: str):
        self.feature = feature
        self.constraint = constraint
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

class aredsl_ChangeContextOperation(DomainOperation):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class aredsl_CreateInstanceOperation(DomainOperation):

    def __init__(self, name: str, feature: str, type: str):
        self.name = name
        self.feature = feature
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class aredsl_Action(ABC):

    def __init__(self, description: str, aredsl_Action: "aredsl_Tool" = None):
        self.description = description
        self.aredsl_Action = aredsl_Action
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def aredsl_Action(self):
        return self.__aredsl_Action

    @aredsl_Action.setter
    def aredsl_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Action__aredsl_Action", None)
        self.__aredsl_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Tool37"):
                opp_val = getattr(old_value, "aredsl_Tool37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Tool37"):
                opp_val = getattr(value, "aredsl_Tool37", None)
                if opp_val is None:
                    setattr(value, "aredsl_Tool37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aredsl_Behaviour(ABC):

    def __init__(self, description: str, aredsl_Behaviour: "aredsl_Tool" = None):
        self.description = description
        self.aredsl_Behaviour = aredsl_Behaviour
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def aredsl_Behaviour(self):
        return self.__aredsl_Behaviour

    @aredsl_Behaviour.setter
    def aredsl_Behaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Behaviour__aredsl_Behaviour", None)
        self.__aredsl_Behaviour = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Tool"):
                opp_val = getattr(old_value, "aredsl_Tool", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Tool"):
                opp_val = getattr(value, "aredsl_Tool", None)
                if opp_val is None:
                    setattr(value, "aredsl_Tool", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aredsl_Tool:

    def __init__(self, id: str, description: str, precondition: str, targetPrecondition: str, aredsl_Tool: set["aredsl_Behaviour"] = None, aredsl_Tool37: set["aredsl_Action"] = None, aredsl_Tool40: "aredsl_ToolSet" = None):
        self.id = id
        self.description = description
        self.precondition = precondition
        self.targetPrecondition = targetPrecondition
        self.aredsl_Tool = aredsl_Tool if aredsl_Tool is not None else set()
        self.aredsl_Tool37 = aredsl_Tool37 if aredsl_Tool37 is not None else set()
        self.aredsl_Tool40 = aredsl_Tool40
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def targetPrecondition(self) -> str:
        return self.__targetPrecondition

    @targetPrecondition.setter
    def targetPrecondition(self, targetPrecondition: str):
        self.__targetPrecondition = targetPrecondition

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

    @property
    def aredsl_Tool(self):
        return self.__aredsl_Tool

    @aredsl_Tool.setter
    def aredsl_Tool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Tool__aredsl_Tool", None)
        self.__aredsl_Tool = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_Behaviour"):
                    opp_val = getattr(item, "aredsl_Behaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_Behaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_Behaviour"):
                    opp_val = getattr(item, "aredsl_Behaviour", None)
                    
                    setattr(item, "aredsl_Behaviour", self)
                    

    @property
    def aredsl_Tool40(self):
        return self.__aredsl_Tool40

    @aredsl_Tool40.setter
    def aredsl_Tool40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Tool__aredsl_Tool40", None)
        self.__aredsl_Tool40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_ToolSet39"):
                opp_val = getattr(old_value, "aredsl_ToolSet39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_ToolSet39"):
                opp_val = getattr(value, "aredsl_ToolSet39", None)
                if opp_val is None:
                    setattr(value, "aredsl_ToolSet39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aredsl_Tool37(self):
        return self.__aredsl_Tool37

    @aredsl_Tool37.setter
    def aredsl_Tool37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Tool__aredsl_Tool37", None)
        self.__aredsl_Tool37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_Action"):
                    opp_val = getattr(item, "aredsl_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_Action"):
                    opp_val = getattr(item, "aredsl_Action", None)
                    
                    setattr(item, "aredsl_Action", self)
                    

class aredsl_SetOperation(DomainOperation):

    def __init__(self, feature: str, value: str, constraint: str):
        self.feature = feature
        self.value = value
        self.constraint = constraint
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class aredsl_RemoveOperation(DomainOperation):

    def __init__(self, constraint: str):
        self.constraint = constraint
        
    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

class Behaviour:

    pass
class aredsl_SupportOperation(Behaviour):

    pass
class aredsl_DomainOperation(Behaviour):

    pass
class aredsl_EdgeStyle:

    def __init__(self, color: str, kind: str, width: int, semanticCondition: str, aredsl_EdgeStyle: "aredsl_Edge" = None):
        self.color = color
        self.kind = kind
        self.width = width
        self.semanticCondition = semanticCondition
        self.aredsl_EdgeStyle = aredsl_EdgeStyle
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def semanticCondition(self) -> str:
        return self.__semanticCondition

    @semanticCondition.setter
    def semanticCondition(self, semanticCondition: str):
        self.__semanticCondition = semanticCondition

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def aredsl_EdgeStyle(self):
        return self.__aredsl_EdgeStyle

    @aredsl_EdgeStyle.setter
    def aredsl_EdgeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_EdgeStyle__aredsl_EdgeStyle", None)
        self.__aredsl_EdgeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Edge19"):
                opp_val = getattr(old_value, "aredsl_Edge19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Edge19"):
                opp_val = getattr(value, "aredsl_Edge19", None)
                if opp_val is None:
                    setattr(value, "aredsl_Edge19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aredsl_LabelStyle:

    def __init__(self, color: str, height: int, semanticCondition: str, aredsl_LabelStyle: "aredsl_Label" = None):
        self.color = color
        self.height = height
        self.semanticCondition = semanticCondition
        self.aredsl_LabelStyle = aredsl_LabelStyle
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def semanticCondition(self) -> str:
        return self.__semanticCondition

    @semanticCondition.setter
    def semanticCondition(self, semanticCondition: str):
        self.__semanticCondition = semanticCondition

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def aredsl_LabelStyle(self):
        return self.__aredsl_LabelStyle

    @aredsl_LabelStyle.setter
    def aredsl_LabelStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_LabelStyle__aredsl_LabelStyle", None)
        self.__aredsl_LabelStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Label17"):
                opp_val = getattr(old_value, "aredsl_Label17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Label17"):
                opp_val = getattr(value, "aredsl_Label17", None)
                if opp_val is None:
                    setattr(value, "aredsl_Label17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NodeStyle:

    pass
class aredsl_Image2DNodeStyle(NodeStyle):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class aredsl_GeometricShapeNodeStyle(NodeStyle):

    def __init__(self, color: str, kind: str, outline: str):
        self.color = color
        self.kind = kind
        self.outline = outline
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def outline(self) -> str:
        return self.__outline

    @outline.setter
    def outline(self, outline: str):
        self.__outline = outline

class aredsl_Model3DNodeStyle(NodeStyle):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class aredsl_ToolSet:

    def __init__(self, id: str, description: str, aredsl_ToolSet: "aredsl_Editor" = None, aredsl_ToolSet39: set["aredsl_Tool"] = None):
        self.id = id
        self.description = description
        self.aredsl_ToolSet = aredsl_ToolSet
        self.aredsl_ToolSet39 = aredsl_ToolSet39 if aredsl_ToolSet39 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def aredsl_ToolSet(self):
        return self.__aredsl_ToolSet

    @aredsl_ToolSet.setter
    def aredsl_ToolSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_ToolSet__aredsl_ToolSet", None)
        self.__aredsl_ToolSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Editor2"):
                opp_val = getattr(old_value, "aredsl_Editor2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Editor2"):
                opp_val = getattr(value, "aredsl_Editor2", None)
                if opp_val is None:
                    setattr(value, "aredsl_Editor2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aredsl_ToolSet39(self):
        return self.__aredsl_ToolSet39

    @aredsl_ToolSet39.setter
    def aredsl_ToolSet39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_ToolSet__aredsl_ToolSet39", None)
        self.__aredsl_ToolSet39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_Tool40"):
                    opp_val = getattr(item, "aredsl_Tool40", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_Tool40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_Tool40"):
                    opp_val = getattr(item, "aredsl_Tool40", None)
                    
                    setattr(item, "aredsl_Tool40", self)
                    

class aredsl_Label:

    def __init__(self, id: str, description: str, semantics: str, aredsl_Label: "aredsl_Node" = None, aredsl_Label22: "aredsl_Edge" = None, aredsl_Label17: set["aredsl_LabelStyle"] = None, aredsl_Label31: "aredsl_Edge" = None, aredsl_Label34: "aredsl_Edge" = None):
        self.id = id
        self.description = description
        self.semantics = semantics
        self.aredsl_Label = aredsl_Label
        self.aredsl_Label22 = aredsl_Label22
        self.aredsl_Label17 = aredsl_Label17 if aredsl_Label17 is not None else set()
        self.aredsl_Label31 = aredsl_Label31
        self.aredsl_Label34 = aredsl_Label34
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def semantics(self) -> str:
        return self.__semantics

    @semantics.setter
    def semantics(self, semantics: str):
        self.__semantics = semantics

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def aredsl_Label31(self):
        return self.__aredsl_Label31

    @aredsl_Label31.setter
    def aredsl_Label31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Label__aredsl_Label31", None)
        self.__aredsl_Label31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Edge30"):
                opp_val = getattr(old_value, "aredsl_Edge30", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Edge30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Edge30"):
                opp_val = getattr(value, "aredsl_Edge30", None)
                setattr(value, "aredsl_Edge30", self)

    @property
    def aredsl_Label22(self):
        return self.__aredsl_Label22

    @aredsl_Label22.setter
    def aredsl_Label22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Label__aredsl_Label22", None)
        self.__aredsl_Label22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Edge21"):
                opp_val = getattr(old_value, "aredsl_Edge21", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Edge21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Edge21"):
                opp_val = getattr(value, "aredsl_Edge21", None)
                setattr(value, "aredsl_Edge21", self)

    @property
    def aredsl_Label17(self):
        return self.__aredsl_Label17

    @aredsl_Label17.setter
    def aredsl_Label17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Label__aredsl_Label17", None)
        self.__aredsl_Label17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_LabelStyle"):
                    opp_val = getattr(item, "aredsl_LabelStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_LabelStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_LabelStyle"):
                    opp_val = getattr(item, "aredsl_LabelStyle", None)
                    
                    setattr(item, "aredsl_LabelStyle", self)
                    

    @property
    def aredsl_Label34(self):
        return self.__aredsl_Label34

    @aredsl_Label34.setter
    def aredsl_Label34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Label__aredsl_Label34", None)
        self.__aredsl_Label34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Edge33"):
                opp_val = getattr(old_value, "aredsl_Edge33", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Edge33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Edge33"):
                opp_val = getattr(value, "aredsl_Edge33", None)
                setattr(value, "aredsl_Edge33", self)

    @property
    def aredsl_Label(self):
        return self.__aredsl_Label

    @aredsl_Label.setter
    def aredsl_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Label__aredsl_Label", None)
        self.__aredsl_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Node12"):
                opp_val = getattr(old_value, "aredsl_Node12", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Node12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Node12"):
                opp_val = getattr(value, "aredsl_Node12", None)
                setattr(value, "aredsl_Node12", self)

class aredsl_NodeStyle(ABC):

    def __init__(self, width: int, height: int, semanticCondition: str, aredsl_NodeStyle: "aredsl_Node" = None):
        self.width = width
        self.height = height
        self.semanticCondition = semanticCondition
        self.aredsl_NodeStyle = aredsl_NodeStyle
        
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
    def semanticCondition(self) -> str:
        return self.__semanticCondition

    @semanticCondition.setter
    def semanticCondition(self, semanticCondition: str):
        self.__semanticCondition = semanticCondition

    @property
    def aredsl_NodeStyle(self):
        return self.__aredsl_NodeStyle

    @aredsl_NodeStyle.setter
    def aredsl_NodeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_NodeStyle__aredsl_NodeStyle", None)
        self.__aredsl_NodeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Node10"):
                opp_val = getattr(old_value, "aredsl_Node10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Node10"):
                opp_val = getattr(value, "aredsl_Node10", None)
                if opp_val is None:
                    setattr(value, "aredsl_Node10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aredsl_TrackerAction(Action):

    pass
class aredsl_Edge:

    def __init__(self, id: str, originSemantics: str, destinationSemantics: str, description: str, aredsl_Edge: "aredsl_Layer" = None, aredsl_Edge19: set["aredsl_EdgeStyle"] = None, aredsl_Edge21: "aredsl_Label" = None, aredsl_Edge24: "aredsl_Node" = None, aredsl_Edge27: "aredsl_Node" = None, aredsl_Edge30: "aredsl_Label" = None, aredsl_Edge33: "aredsl_Label" = None):
        self.id = id
        self.originSemantics = originSemantics
        self.destinationSemantics = destinationSemantics
        self.description = description
        self.aredsl_Edge = aredsl_Edge
        self.aredsl_Edge19 = aredsl_Edge19 if aredsl_Edge19 is not None else set()
        self.aredsl_Edge21 = aredsl_Edge21
        self.aredsl_Edge24 = aredsl_Edge24
        self.aredsl_Edge27 = aredsl_Edge27
        self.aredsl_Edge30 = aredsl_Edge30
        self.aredsl_Edge33 = aredsl_Edge33
        
    @property
    def destinationSemantics(self) -> str:
        return self.__destinationSemantics

    @destinationSemantics.setter
    def destinationSemantics(self, destinationSemantics: str):
        self.__destinationSemantics = destinationSemantics

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def originSemantics(self) -> str:
        return self.__originSemantics

    @originSemantics.setter
    def originSemantics(self, originSemantics: str):
        self.__originSemantics = originSemantics

    @property
    def aredsl_Edge21(self):
        return self.__aredsl_Edge21

    @aredsl_Edge21.setter
    def aredsl_Edge21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Edge__aredsl_Edge21", None)
        self.__aredsl_Edge21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Label22"):
                opp_val = getattr(old_value, "aredsl_Label22", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Label22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Label22"):
                opp_val = getattr(value, "aredsl_Label22", None)
                setattr(value, "aredsl_Label22", self)

    @property
    def aredsl_Edge24(self):
        return self.__aredsl_Edge24

    @aredsl_Edge24.setter
    def aredsl_Edge24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Edge__aredsl_Edge24", None)
        self.__aredsl_Edge24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Node25"):
                opp_val = getattr(old_value, "aredsl_Node25", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Node25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Node25"):
                opp_val = getattr(value, "aredsl_Node25", None)
                setattr(value, "aredsl_Node25", self)

    @property
    def aredsl_Edge27(self):
        return self.__aredsl_Edge27

    @aredsl_Edge27.setter
    def aredsl_Edge27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Edge__aredsl_Edge27", None)
        self.__aredsl_Edge27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Node28"):
                opp_val = getattr(old_value, "aredsl_Node28", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Node28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Node28"):
                opp_val = getattr(value, "aredsl_Node28", None)
                setattr(value, "aredsl_Node28", self)

    @property
    def aredsl_Edge33(self):
        return self.__aredsl_Edge33

    @aredsl_Edge33.setter
    def aredsl_Edge33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Edge__aredsl_Edge33", None)
        self.__aredsl_Edge33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Label34"):
                opp_val = getattr(old_value, "aredsl_Label34", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Label34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Label34"):
                opp_val = getattr(value, "aredsl_Label34", None)
                setattr(value, "aredsl_Label34", self)

    @property
    def aredsl_Edge(self):
        return self.__aredsl_Edge

    @aredsl_Edge.setter
    def aredsl_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Edge__aredsl_Edge", None)
        self.__aredsl_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Layer6"):
                opp_val = getattr(old_value, "aredsl_Layer6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Layer6"):
                opp_val = getattr(value, "aredsl_Layer6", None)
                if opp_val is None:
                    setattr(value, "aredsl_Layer6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aredsl_Edge30(self):
        return self.__aredsl_Edge30

    @aredsl_Edge30.setter
    def aredsl_Edge30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Edge__aredsl_Edge30", None)
        self.__aredsl_Edge30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Label31"):
                opp_val = getattr(old_value, "aredsl_Label31", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Label31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Label31"):
                opp_val = getattr(value, "aredsl_Label31", None)
                setattr(value, "aredsl_Label31", self)

    @property
    def aredsl_Edge19(self):
        return self.__aredsl_Edge19

    @aredsl_Edge19.setter
    def aredsl_Edge19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Edge__aredsl_Edge19", None)
        self.__aredsl_Edge19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_EdgeStyle"):
                    opp_val = getattr(item, "aredsl_EdgeStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_EdgeStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_EdgeStyle"):
                    opp_val = getattr(item, "aredsl_EdgeStyle", None)
                    
                    setattr(item, "aredsl_EdgeStyle", self)
                    

class aredsl_Node:

    def __init__(self, id: str, semantics: str, contaimentKind: str, description: str, aredsl_Node: "aredsl_Layer" = None, aredsl_Node10: set["aredsl_NodeStyle"] = None, aredsl_Node12: "aredsl_Label" = None, aredsl_Node15: "aredsl_Node" = None, aredsl_Node13: set["aredsl_Node"] = None, aredsl_Node25: "aredsl_Edge" = None, aredsl_Node28: "aredsl_Edge" = None):
        self.id = id
        self.semantics = semantics
        self.contaimentKind = contaimentKind
        self.description = description
        self.aredsl_Node = aredsl_Node
        self.aredsl_Node10 = aredsl_Node10 if aredsl_Node10 is not None else set()
        self.aredsl_Node12 = aredsl_Node12
        self.aredsl_Node15 = aredsl_Node15
        self.aredsl_Node13 = aredsl_Node13 if aredsl_Node13 is not None else set()
        self.aredsl_Node25 = aredsl_Node25
        self.aredsl_Node28 = aredsl_Node28
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def semantics(self) -> str:
        return self.__semantics

    @semantics.setter
    def semantics(self, semantics: str):
        self.__semantics = semantics

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def contaimentKind(self) -> str:
        return self.__contaimentKind

    @contaimentKind.setter
    def contaimentKind(self, contaimentKind: str):
        self.__contaimentKind = contaimentKind

    @property
    def aredsl_Node13(self):
        return self.__aredsl_Node13

    @aredsl_Node13.setter
    def aredsl_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Node__aredsl_Node13", None)
        self.__aredsl_Node13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_Node15"):
                    opp_val = getattr(item, "aredsl_Node15", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_Node15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_Node15"):
                    opp_val = getattr(item, "aredsl_Node15", None)
                    
                    setattr(item, "aredsl_Node15", self)
                    

    @property
    def aredsl_Node25(self):
        return self.__aredsl_Node25

    @aredsl_Node25.setter
    def aredsl_Node25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Node__aredsl_Node25", None)
        self.__aredsl_Node25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Edge24"):
                opp_val = getattr(old_value, "aredsl_Edge24", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Edge24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Edge24"):
                opp_val = getattr(value, "aredsl_Edge24", None)
                setattr(value, "aredsl_Edge24", self)

    @property
    def aredsl_Node12(self):
        return self.__aredsl_Node12

    @aredsl_Node12.setter
    def aredsl_Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Node__aredsl_Node12", None)
        self.__aredsl_Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Label"):
                opp_val = getattr(old_value, "aredsl_Label", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Label"):
                opp_val = getattr(value, "aredsl_Label", None)
                setattr(value, "aredsl_Label", self)

    @property
    def aredsl_Node(self):
        return self.__aredsl_Node

    @aredsl_Node.setter
    def aredsl_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Node__aredsl_Node", None)
        self.__aredsl_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Layer4"):
                opp_val = getattr(old_value, "aredsl_Layer4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Layer4"):
                opp_val = getattr(value, "aredsl_Layer4", None)
                if opp_val is None:
                    setattr(value, "aredsl_Layer4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aredsl_Node15(self):
        return self.__aredsl_Node15

    @aredsl_Node15.setter
    def aredsl_Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Node__aredsl_Node15", None)
        self.__aredsl_Node15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Node13"):
                opp_val = getattr(old_value, "aredsl_Node13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Node13"):
                opp_val = getattr(value, "aredsl_Node13", None)
                if opp_val is None:
                    setattr(value, "aredsl_Node13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aredsl_Node28(self):
        return self.__aredsl_Node28

    @aredsl_Node28.setter
    def aredsl_Node28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Node__aredsl_Node28", None)
        self.__aredsl_Node28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Edge27"):
                opp_val = getattr(old_value, "aredsl_Edge27", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_Edge27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Edge27"):
                opp_val = getattr(value, "aredsl_Edge27", None)
                setattr(value, "aredsl_Edge27", self)

    @property
    def aredsl_Node10(self):
        return self.__aredsl_Node10

    @aredsl_Node10.setter
    def aredsl_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Node__aredsl_Node10", None)
        self.__aredsl_Node10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_NodeStyle"):
                    opp_val = getattr(item, "aredsl_NodeStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_NodeStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_NodeStyle"):
                    opp_val = getattr(item, "aredsl_NodeStyle", None)
                    
                    setattr(item, "aredsl_NodeStyle", self)
                    

class aredsl_Layer:

    def __init__(self, id: str, semantics: str, description: str, aredsl_Layer: "aredsl_Editor" = None, aredsl_Layer4: set["aredsl_Node"] = None, aredsl_Layer6: set["aredsl_Edge"] = None, aredsl_Layer8: "aredsl_TrackerAction" = None):
        self.id = id
        self.semantics = semantics
        self.description = description
        self.aredsl_Layer = aredsl_Layer
        self.aredsl_Layer4 = aredsl_Layer4 if aredsl_Layer4 is not None else set()
        self.aredsl_Layer6 = aredsl_Layer6 if aredsl_Layer6 is not None else set()
        self.aredsl_Layer8 = aredsl_Layer8
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def semantics(self) -> str:
        return self.__semantics

    @semantics.setter
    def semantics(self, semantics: str):
        self.__semantics = semantics

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aredsl_Layer4(self):
        return self.__aredsl_Layer4

    @aredsl_Layer4.setter
    def aredsl_Layer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Layer__aredsl_Layer4", None)
        self.__aredsl_Layer4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_Node"):
                    opp_val = getattr(item, "aredsl_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_Node"):
                    opp_val = getattr(item, "aredsl_Node", None)
                    
                    setattr(item, "aredsl_Node", self)
                    

    @property
    def aredsl_Layer6(self):
        return self.__aredsl_Layer6

    @aredsl_Layer6.setter
    def aredsl_Layer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Layer__aredsl_Layer6", None)
        self.__aredsl_Layer6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_Edge"):
                    opp_val = getattr(item, "aredsl_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_Edge"):
                    opp_val = getattr(item, "aredsl_Edge", None)
                    
                    setattr(item, "aredsl_Edge", self)
                    

    @property
    def aredsl_Layer8(self):
        return self.__aredsl_Layer8

    @aredsl_Layer8.setter
    def aredsl_Layer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Layer__aredsl_Layer8", None)
        self.__aredsl_Layer8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_TrackerAction"):
                opp_val = getattr(old_value, "aredsl_TrackerAction", None)
                if opp_val == self:
                    setattr(old_value, "aredsl_TrackerAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_TrackerAction"):
                opp_val = getattr(value, "aredsl_TrackerAction", None)
                setattr(value, "aredsl_TrackerAction", self)

    @property
    def aredsl_Layer(self):
        return self.__aredsl_Layer

    @aredsl_Layer.setter
    def aredsl_Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Layer__aredsl_Layer", None)
        self.__aredsl_Layer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aredsl_Editor"):
                opp_val = getattr(old_value, "aredsl_Editor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aredsl_Editor"):
                opp_val = getattr(value, "aredsl_Editor", None)
                if opp_val is None:
                    setattr(value, "aredsl_Editor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aredsl_Editor:

    def __init__(self, description: str, fileExtension: str, name: str, queryLanguageKind: str, aredsl_Editor: set["aredsl_Layer"] = None, aredsl_Editor2: set["aredsl_ToolSet"] = None):
        self.description = description
        self.fileExtension = fileExtension
        self.name = name
        self.queryLanguageKind = queryLanguageKind
        self.aredsl_Editor = aredsl_Editor if aredsl_Editor is not None else set()
        self.aredsl_Editor2 = aredsl_Editor2 if aredsl_Editor2 is not None else set()
        
    @property
    def fileExtension(self) -> str:
        return self.__fileExtension

    @fileExtension.setter
    def fileExtension(self, fileExtension: str):
        self.__fileExtension = fileExtension

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def queryLanguageKind(self) -> str:
        return self.__queryLanguageKind

    @queryLanguageKind.setter
    def queryLanguageKind(self, queryLanguageKind: str):
        self.__queryLanguageKind = queryLanguageKind

    @property
    def aredsl_Editor2(self):
        return self.__aredsl_Editor2

    @aredsl_Editor2.setter
    def aredsl_Editor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Editor__aredsl_Editor2", None)
        self.__aredsl_Editor2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_ToolSet"):
                    opp_val = getattr(item, "aredsl_ToolSet", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_ToolSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_ToolSet"):
                    opp_val = getattr(item, "aredsl_ToolSet", None)
                    
                    setattr(item, "aredsl_ToolSet", self)
                    

    @property
    def aredsl_Editor(self):
        return self.__aredsl_Editor

    @aredsl_Editor.setter
    def aredsl_Editor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aredsl_Editor__aredsl_Editor", None)
        self.__aredsl_Editor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aredsl_Layer"):
                    opp_val = getattr(item, "aredsl_Layer", None)
                    
                    if opp_val == self:
                        setattr(item, "aredsl_Layer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aredsl_Layer"):
                    opp_val = getattr(item, "aredsl_Layer", None)
                    
                    setattr(item, "aredsl_Layer", self)
                    
