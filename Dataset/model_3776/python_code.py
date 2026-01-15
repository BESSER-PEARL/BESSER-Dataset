from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ValueType(Enum):
    FEATURE = "FEATURE"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    NONE = "NONE"
    STRING = "STRING"
class ConfigState(Enum):
    USER_SELECTED = "USER_SELECTED"
    USER_ELIMINATED = "USER_ELIMINATED"
    MACHINE_SELECTED = "MACHINE_SELECTED"
    MACHINE_ELIMINATED = "MACHINE_ELIMINATED"
    UNDECIDED = "UNDECIDED"


############################################
# Definition of Classes
############################################

class fmp_Project:

    pass
class Node:

    pass
class fmp_Clonable(Node):

    def __init__(self, state: str, Clonable34: "fmp_Clonable" = None, clones: "fmp_Clonable" = None, Clonable: "fmp_Clonable" = None, prototype: set["fmp_Clonable"] = None):
        self.state = state
        self.Clonable34 = Clonable34
        self.clones = clones
        self.Clonable = Clonable
        self.prototype = prototype if prototype is not None else set()
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def prototype(self):
        return self.__prototype

    @prototype.setter
    def prototype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Clonable__prototype", None)
        self.__prototype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Clonable"):
                    opp_val = getattr(item, "Clonable", None)
                    
                    if opp_val == self:
                        setattr(item, "Clonable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Clonable"):
                    opp_val = getattr(item, "Clonable", None)
                    
                    setattr(item, "Clonable", self)
                    

    @property
    def Clonable34(self):
        return self.__Clonable34

    @Clonable34.setter
    def Clonable34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Clonable__Clonable34", None)
        self.__Clonable34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clones"):
                opp_val = getattr(old_value, "clones", None)
                if opp_val == self:
                    setattr(old_value, "clones", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clones"):
                opp_val = getattr(value, "clones", None)
                setattr(value, "clones", self)

    @property
    def Clonable(self):
        return self.__Clonable

    @Clonable.setter
    def Clonable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Clonable__Clonable", None)
        self.__Clonable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prototype"):
                opp_val = getattr(old_value, "prototype", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prototype"):
                opp_val = getattr(value, "prototype", None)
                if opp_val is None:
                    setattr(value, "prototype", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def clones(self):
        return self.__clones

    @clones.setter
    def clones(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Clonable__clones", None)
        self.__clones = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Clonable34"):
                opp_val = getattr(old_value, "Clonable34", None)
                if opp_val == self:
                    setattr(old_value, "Clonable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Clonable34"):
                opp_val = getattr(value, "Clonable34", None)
                setattr(value, "Clonable34", self)

class fmp_FeatureGroup(Node):

    pass
class fmp_Constraint:

    def __init__(self, text: str, fmp_Constraint: "fmp_Feature" = None):
        self.text = text
        self.fmp_Constraint = fmp_Constraint
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def fmp_Constraint(self):
        return self.__fmp_Constraint

    @fmp_Constraint.setter
    def fmp_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Constraint__fmp_Constraint", None)
        self.__fmp_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_Feature7"):
                opp_val = getattr(old_value, "fmp_Feature7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_Feature7"):
                opp_val = getattr(value, "fmp_Feature7", None)
                if opp_val is None:
                    setattr(value, "fmp_Feature7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fmp_Node(ABC):

    def __init__(self, id: str, max: int, min: int, Node: "fmp_Feature" = None, Node10: "fmp_Node" = None, origin: set["fmp_Node"] = None, Node13: "fmp_Node" = None, confs: "fmp_Node" = None, fmp_Node: "fmp_Node" = None, fmp_Node14: set["fmp_Node"] = None, describedNode: "fmp_Feature" = None):
        self.id = id
        self.max = max
        self.min = min
        self.Node = Node
        self.Node10 = Node10
        self.origin = origin if origin is not None else set()
        self.Node13 = Node13
        self.confs = confs
        self.fmp_Node = fmp_Node
        self.fmp_Node14 = fmp_Node14 if fmp_Node14 is not None else set()
        self.describedNode = describedNode
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def Node13(self):
        return self.__Node13

    @Node13.setter
    def Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Node__Node13", None)
        self.__Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "confs"):
                opp_val = getattr(old_value, "confs", None)
                if opp_val == self:
                    setattr(old_value, "confs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "confs"):
                opp_val = getattr(value, "confs", None)
                setattr(value, "confs", self)

    @property
    def fmp_Node(self):
        return self.__fmp_Node

    @fmp_Node.setter
    def fmp_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Node__fmp_Node", None)
        self.__fmp_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_Node14"):
                opp_val = getattr(old_value, "fmp_Node14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_Node14"):
                opp_val = getattr(value, "fmp_Node14", None)
                if opp_val is None:
                    setattr(value, "fmp_Node14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node10(self):
        return self.__Node10

    @Node10.setter
    def Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Node__Node10", None)
        self.__Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "origin"):
                opp_val = getattr(old_value, "origin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "origin"):
                opp_val = getattr(value, "origin", None)
                if opp_val is None:
                    setattr(value, "origin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def describedNode(self):
        return self.__describedNode

    @describedNode.setter
    def describedNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Node__describedNode", None)
        self.__describedNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature"):
                opp_val = getattr(old_value, "Feature", None)
                if opp_val == self:
                    setattr(old_value, "Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature"):
                opp_val = getattr(value, "Feature", None)
                setattr(value, "Feature", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties"):
                opp_val = getattr(old_value, "properties", None)
                if opp_val == self:
                    setattr(old_value, "properties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties"):
                opp_val = getattr(value, "properties", None)
                setattr(value, "properties", self)

    @property
    def confs(self):
        return self.__confs

    @confs.setter
    def confs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Node__confs", None)
        self.__confs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node13"):
                opp_val = getattr(old_value, "Node13", None)
                if opp_val == self:
                    setattr(old_value, "Node13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node13"):
                opp_val = getattr(value, "Node13", None)
                setattr(value, "Node13", self)

    @property
    def fmp_Node14(self):
        return self.__fmp_Node14

    @fmp_Node14.setter
    def fmp_Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Node__fmp_Node14", None)
        self.__fmp_Node14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fmp_Node"):
                    opp_val = getattr(item, "fmp_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "fmp_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fmp_Node"):
                    opp_val = getattr(item, "fmp_Node", None)
                    
                    setattr(item, "fmp_Node", self)
                    

    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Node__origin", None)
        self.__origin = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node10"):
                    opp_val = getattr(item, "Node10", None)
                    
                    if opp_val == self:
                        setattr(item, "Node10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node10"):
                    opp_val = getattr(item, "Node10", None)
                    
                    setattr(item, "Node10", self)
                    

class Clonable:

    pass
class fmp_Feature(Clonable):

    def __init__(self, name: str, valueType: str, feature: set["fmp_Reference"] = None, fmp_Feature4: "fmp_TypedValue" = None, fmp_Feature: "fmp_Feature" = None, fmp_Feature0: set["fmp_Feature"] = None, properties: "fmp_Node" = None, fmp_Feature7: set["fmp_Constraint"] = None, Feature: "fmp_Node" = None, Feature18: "fmp_Reference" = None, fmp_Feature20: "fmp_Project" = None, fmp_Feature23: "fmp_Project" = None, fmp_Feature26: "fmp_Project" = None, fmp_Feature29: "fmp_TypedValue" = None):
        self.name = name
        self.valueType = valueType
        self.feature = feature if feature is not None else set()
        self.fmp_Feature4 = fmp_Feature4
        self.fmp_Feature = fmp_Feature
        self.fmp_Feature0 = fmp_Feature0 if fmp_Feature0 is not None else set()
        self.properties = properties
        self.fmp_Feature7 = fmp_Feature7 if fmp_Feature7 is not None else set()
        self.Feature = Feature
        self.Feature18 = Feature18
        self.fmp_Feature20 = fmp_Feature20
        self.fmp_Feature23 = fmp_Feature23
        self.fmp_Feature26 = fmp_Feature26
        self.fmp_Feature29 = fmp_Feature29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def valueType(self) -> str:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: str):
        self.__valueType = valueType

    @property
    def fmp_Feature20(self):
        return self.__fmp_Feature20

    @fmp_Feature20.setter
    def fmp_Feature20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__fmp_Feature20", None)
        self.__fmp_Feature20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_Project"):
                opp_val = getattr(old_value, "fmp_Project", None)
                if opp_val == self:
                    setattr(old_value, "fmp_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_Project"):
                opp_val = getattr(value, "fmp_Project", None)
                setattr(value, "fmp_Project", self)

    @property
    def Feature18(self):
        return self.__Feature18

    @Feature18.setter
    def Feature18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__Feature18", None)
        self.__Feature18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "references"):
                opp_val = getattr(old_value, "references", None)
                if opp_val == self:
                    setattr(old_value, "references", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "references"):
                opp_val = getattr(value, "references", None)
                setattr(value, "references", self)

    @property
    def fmp_Feature26(self):
        return self.__fmp_Feature26

    @fmp_Feature26.setter
    def fmp_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__fmp_Feature26", None)
        self.__fmp_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_Project25"):
                opp_val = getattr(old_value, "fmp_Project25", None)
                if opp_val == self:
                    setattr(old_value, "fmp_Project25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_Project25"):
                opp_val = getattr(value, "fmp_Project25", None)
                setattr(value, "fmp_Project25", self)

    @property
    def fmp_Feature7(self):
        return self.__fmp_Feature7

    @fmp_Feature7.setter
    def fmp_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__fmp_Feature7", None)
        self.__fmp_Feature7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fmp_Constraint"):
                    opp_val = getattr(item, "fmp_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "fmp_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fmp_Constraint"):
                    opp_val = getattr(item, "fmp_Constraint", None)
                    
                    setattr(item, "fmp_Constraint", self)
                    

    @property
    def fmp_Feature(self):
        return self.__fmp_Feature

    @fmp_Feature.setter
    def fmp_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__fmp_Feature", None)
        self.__fmp_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_Feature0"):
                opp_val = getattr(old_value, "fmp_Feature0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_Feature0"):
                opp_val = getattr(value, "fmp_Feature0", None)
                if opp_val is None:
                    setattr(value, "fmp_Feature0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__feature", None)
        self.__feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Reference"):
                    opp_val = getattr(item, "Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Reference"):
                    opp_val = getattr(item, "Reference", None)
                    
                    setattr(item, "Reference", self)
                    

    @property
    def fmp_Feature4(self):
        return self.__fmp_Feature4

    @fmp_Feature4.setter
    def fmp_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__fmp_Feature4", None)
        self.__fmp_Feature4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_TypedValue"):
                opp_val = getattr(old_value, "fmp_TypedValue", None)
                if opp_val == self:
                    setattr(old_value, "fmp_TypedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_TypedValue"):
                opp_val = getattr(value, "fmp_TypedValue", None)
                setattr(value, "fmp_TypedValue", self)

    @property
    def fmp_Feature29(self):
        return self.__fmp_Feature29

    @fmp_Feature29.setter
    def fmp_Feature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__fmp_Feature29", None)
        self.__fmp_Feature29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_TypedValue28"):
                opp_val = getattr(old_value, "fmp_TypedValue28", None)
                if opp_val == self:
                    setattr(old_value, "fmp_TypedValue28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_TypedValue28"):
                opp_val = getattr(value, "fmp_TypedValue28", None)
                setattr(value, "fmp_TypedValue28", self)

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__properties", None)
        self.__properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def fmp_Feature0(self):
        return self.__fmp_Feature0

    @fmp_Feature0.setter
    def fmp_Feature0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__fmp_Feature0", None)
        self.__fmp_Feature0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fmp_Feature"):
                    opp_val = getattr(item, "fmp_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "fmp_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fmp_Feature"):
                    opp_val = getattr(item, "fmp_Feature", None)
                    
                    setattr(item, "fmp_Feature", self)
                    

    @property
    def fmp_Feature23(self):
        return self.__fmp_Feature23

    @fmp_Feature23.setter
    def fmp_Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__fmp_Feature23", None)
        self.__fmp_Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_Project22"):
                opp_val = getattr(old_value, "fmp_Project22", None)
                if opp_val == self:
                    setattr(old_value, "fmp_Project22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_Project22"):
                opp_val = getattr(value, "fmp_Project22", None)
                setattr(value, "fmp_Project22", self)

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "describedNode"):
                opp_val = getattr(old_value, "describedNode", None)
                if opp_val == self:
                    setattr(old_value, "describedNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "describedNode"):
                opp_val = getattr(value, "describedNode", None)
                setattr(value, "describedNode", self)

class fmp_TypedValue:

    def __init__(self, integerValue: str, stringValue: str, floatValue: str, fmp_TypedValue: "fmp_Feature" = None, fmp_TypedValue28: "fmp_Feature" = None):
        self.integerValue = integerValue
        self.stringValue = stringValue
        self.floatValue = floatValue
        self.fmp_TypedValue = fmp_TypedValue
        self.fmp_TypedValue28 = fmp_TypedValue28
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

    @property
    def integerValue(self) -> str:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: str):
        self.__integerValue = integerValue

    @property
    def floatValue(self) -> str:
        return self.__floatValue

    @floatValue.setter
    def floatValue(self, floatValue: str):
        self.__floatValue = floatValue

    @property
    def fmp_TypedValue(self):
        return self.__fmp_TypedValue

    @fmp_TypedValue.setter
    def fmp_TypedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_TypedValue__fmp_TypedValue", None)
        self.__fmp_TypedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_Feature4"):
                opp_val = getattr(old_value, "fmp_Feature4", None)
                if opp_val == self:
                    setattr(old_value, "fmp_Feature4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_Feature4"):
                opp_val = getattr(value, "fmp_Feature4", None)
                setattr(value, "fmp_Feature4", self)

    @property
    def fmp_TypedValue28(self):
        return self.__fmp_TypedValue28

    @fmp_TypedValue28.setter
    def fmp_TypedValue28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fmp_TypedValue__fmp_TypedValue28", None)
        self.__fmp_TypedValue28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fmp_Feature29"):
                opp_val = getattr(old_value, "fmp_Feature29", None)
                if opp_val == self:
                    setattr(old_value, "fmp_Feature29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fmp_Feature29"):
                opp_val = getattr(value, "fmp_Feature29", None)
                setattr(value, "fmp_Feature29", self)

class fmp_Reference(Clonable):

    pass