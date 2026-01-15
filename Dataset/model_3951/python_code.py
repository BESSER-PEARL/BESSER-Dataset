from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataType(Enum):
    String = "String"
    Integer = "Integer"
    Boolean = "Boolean"
    Complex = "Complex"


############################################
# Definition of Classes
############################################

class CallOperationAction:

    pass
class sooml_CallParameterOperationAction(CallOperationAction):

    pass
class sooml_CallReferenceOperationAction(CallOperationAction):

    pass
class IsInStateCondition:

    pass
class sooml_ParameterIsInStateCondition(IsInStateCondition):

    pass
class sooml_ReferenceIsInStateCondition(IsInStateCondition):

    pass
class Guard:

    pass
class sooml_IsInStateCondition(Guard):

    pass
class sooml_ParameterBinding:

    pass
class sooml_Event:

    pass
class sooml_Guard(ABC):

    pass
class sooml_Action(ABC):

    pass
class sooml_EntryOperation:

    pass
class sooml_Transition:

    pass
class Action:

    pass
class sooml_ReferenceAssignmentAction(Action):

    pass
class sooml_CallOperationAction(Action):

    pass
class StructuralFeature:

    pass
class sooml_Attribute(StructuralFeature):

    def __init__(self, dataType: str):
        self.dataType = dataType
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

class sooml_StateMachine:

    pass
class sooml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class sooml_Operation(NamedElement):

    pass
class sooml_Class(NamedElement):

    pass
class sooml_StructuralFeature(NamedElement):

    def __init__(self, upperBound: int, lowerBound: int, sooml_StructuralFeature: "sooml_Class" = None, sooml_StructuralFeature48: "sooml_ParameterBinding" = None):
        self.upperBound = upperBound
        self.lowerBound = lowerBound
        self.sooml_StructuralFeature = sooml_StructuralFeature
        self.sooml_StructuralFeature48 = sooml_StructuralFeature48
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def sooml_StructuralFeature48(self):
        return self.__sooml_StructuralFeature48

    @sooml_StructuralFeature48.setter
    def sooml_StructuralFeature48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sooml_StructuralFeature__sooml_StructuralFeature48", None)
        self.__sooml_StructuralFeature48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sooml_ParameterBinding47"):
                opp_val = getattr(old_value, "sooml_ParameterBinding47", None)
                if opp_val == self:
                    setattr(old_value, "sooml_ParameterBinding47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sooml_ParameterBinding47"):
                opp_val = getattr(value, "sooml_ParameterBinding47", None)
                setattr(value, "sooml_ParameterBinding47", self)

    @property
    def sooml_StructuralFeature(self):
        return self.__sooml_StructuralFeature

    @sooml_StructuralFeature.setter
    def sooml_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sooml_StructuralFeature__sooml_StructuralFeature", None)
        self.__sooml_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sooml_Class10"):
                opp_val = getattr(old_value, "sooml_Class10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sooml_Class10"):
                opp_val = getattr(value, "sooml_Class10", None)
                if opp_val is None:
                    setattr(value, "sooml_Class10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sooml_State(NamedElement):

    pass
class sooml_Package(NamedElement):

    pass
class sooml_Parameter(NamedElement):

    def __init__(self, dataType: str, sooml_Parameter: "sooml_Operation" = None, sooml_Parameter40: "sooml_Class" = None, sooml_Parameter51: "sooml_ParameterBinding" = None, sooml_Parameter60: "sooml_ParameterIsInStateCondition" = None, sooml_Parameter64: "sooml_CallParameterOperationAction" = None, sooml_Parameter66: "sooml_ReferenceAssignmentAction" = None):
        self.dataType = dataType
        self.sooml_Parameter = sooml_Parameter
        self.sooml_Parameter40 = sooml_Parameter40
        self.sooml_Parameter51 = sooml_Parameter51
        self.sooml_Parameter60 = sooml_Parameter60
        self.sooml_Parameter64 = sooml_Parameter64
        self.sooml_Parameter66 = sooml_Parameter66
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def sooml_Parameter40(self):
        return self.__sooml_Parameter40

    @sooml_Parameter40.setter
    def sooml_Parameter40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sooml_Parameter__sooml_Parameter40", None)
        self.__sooml_Parameter40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sooml_Class41"):
                opp_val = getattr(old_value, "sooml_Class41", None)
                if opp_val == self:
                    setattr(old_value, "sooml_Class41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sooml_Class41"):
                opp_val = getattr(value, "sooml_Class41", None)
                setattr(value, "sooml_Class41", self)

    @property
    def sooml_Parameter60(self):
        return self.__sooml_Parameter60

    @sooml_Parameter60.setter
    def sooml_Parameter60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sooml_Parameter__sooml_Parameter60", None)
        self.__sooml_Parameter60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sooml_ParameterIsInStateCondition"):
                opp_val = getattr(old_value, "sooml_ParameterIsInStateCondition", None)
                if opp_val == self:
                    setattr(old_value, "sooml_ParameterIsInStateCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sooml_ParameterIsInStateCondition"):
                opp_val = getattr(value, "sooml_ParameterIsInStateCondition", None)
                setattr(value, "sooml_ParameterIsInStateCondition", self)

    @property
    def sooml_Parameter64(self):
        return self.__sooml_Parameter64

    @sooml_Parameter64.setter
    def sooml_Parameter64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sooml_Parameter__sooml_Parameter64", None)
        self.__sooml_Parameter64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sooml_CallParameterOperationAction"):
                opp_val = getattr(old_value, "sooml_CallParameterOperationAction", None)
                if opp_val == self:
                    setattr(old_value, "sooml_CallParameterOperationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sooml_CallParameterOperationAction"):
                opp_val = getattr(value, "sooml_CallParameterOperationAction", None)
                setattr(value, "sooml_CallParameterOperationAction", self)

    @property
    def sooml_Parameter51(self):
        return self.__sooml_Parameter51

    @sooml_Parameter51.setter
    def sooml_Parameter51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sooml_Parameter__sooml_Parameter51", None)
        self.__sooml_Parameter51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sooml_ParameterBinding50"):
                opp_val = getattr(old_value, "sooml_ParameterBinding50", None)
                if opp_val == self:
                    setattr(old_value, "sooml_ParameterBinding50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sooml_ParameterBinding50"):
                opp_val = getattr(value, "sooml_ParameterBinding50", None)
                setattr(value, "sooml_ParameterBinding50", self)

    @property
    def sooml_Parameter66(self):
        return self.__sooml_Parameter66

    @sooml_Parameter66.setter
    def sooml_Parameter66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sooml_Parameter__sooml_Parameter66", None)
        self.__sooml_Parameter66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sooml_ReferenceAssignmentAction"):
                opp_val = getattr(old_value, "sooml_ReferenceAssignmentAction", None)
                if opp_val == self:
                    setattr(old_value, "sooml_ReferenceAssignmentAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sooml_ReferenceAssignmentAction"):
                opp_val = getattr(value, "sooml_ReferenceAssignmentAction", None)
                setattr(value, "sooml_ReferenceAssignmentAction", self)

    @property
    def sooml_Parameter(self):
        return self.__sooml_Parameter

    @sooml_Parameter.setter
    def sooml_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sooml_Parameter__sooml_Parameter", None)
        self.__sooml_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sooml_Operation17"):
                opp_val = getattr(old_value, "sooml_Operation17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sooml_Operation17"):
                opp_val = getattr(value, "sooml_Operation17", None)
                if opp_val is None:
                    setattr(value, "sooml_Operation17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sooml_Reference(StructuralFeature):

    pass