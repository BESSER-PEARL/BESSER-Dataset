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


############################################
# Definition of Classes
############################################

class CallMethodAction:

    pass
class soopl_CallMethodOfParameter(CallMethodAction):

    pass
class soopl_CallMethodOfProperty(CallMethodAction):

    pass
class IsInStateCondition:

    pass
class soopl_ParameterIsInState(IsInStateCondition):

    pass
class soopl_PropertyIsInState(IsInStateCondition):

    pass
class Guard:

    pass
class soopl_IsInStateCondition(Guard):

    pass
class soopl_ParameterBinding:

    pass
class Action:

    pass
class soopl_CallMethodAction(Action):

    pass
class Parameter:

    pass
class soopl_ComplexTypeParameter(Parameter):

    pass
class soopl_SimpleTypeParameter(Parameter):

    def __init__(self, dataType: str):
        self.dataType = dataType
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

class soopl_Guard(ABC):

    pass
class soopl_AssignProperty(Action):

    pass
class soopl_Transition:

    pass
class Method:

    pass
class soopl_TransitionMethod(Method):

    pass
class Property:

    pass
class soopl_ComplexTypeProperty(Property):

    pass
class soopl_SimpleTypeProperty(Property):

    def __init__(self, dataType: str):
        self.dataType = dataType
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

class Class:

    pass
class soopl_StateClass(Class):

    pass
class soopl_StateImplementationClass(Class):

    pass
class soopl_StatefulClass(Class):

    pass
class soopl_Action(ABC):

    pass
class NamedElement:

    pass
class soopl_Property(NamedElement):

    def __init__(self, upperBound: int, lowerBound: int, multiValued: bool, soopl_Property: "soopl_Class" = None, soopl_Property48: "soopl_ParameterBinding" = None):
        self.upperBound = upperBound
        self.lowerBound = lowerBound
        self.multiValued = multiValued
        self.soopl_Property = soopl_Property
        self.soopl_Property48 = soopl_Property48
        
    @property
    def multiValued(self) -> bool:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: bool):
        self.__multiValued = multiValued

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def soopl_Property48(self):
        return self.__soopl_Property48

    @soopl_Property48.setter
    def soopl_Property48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Property__soopl_Property48", None)
        self.__soopl_Property48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soopl_ParameterBinding47"):
                opp_val = getattr(old_value, "soopl_ParameterBinding47", None)
                if opp_val == self:
                    setattr(old_value, "soopl_ParameterBinding47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soopl_ParameterBinding47"):
                opp_val = getattr(value, "soopl_ParameterBinding47", None)
                setattr(value, "soopl_ParameterBinding47", self)

    @property
    def soopl_Property(self):
        return self.__soopl_Property

    @soopl_Property.setter
    def soopl_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Property__soopl_Property", None)
        self.__soopl_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soopl_Class9"):
                opp_val = getattr(old_value, "soopl_Class9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soopl_Class9"):
                opp_val = getattr(value, "soopl_Class9", None)
                if opp_val is None:
                    setattr(value, "soopl_Class9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class soopl_Method(NamedElement):

    pass
class soopl_Parameter(NamedElement):

    pass
class soopl_Package(NamedElement):

    pass
class soopl_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class soopl_Class(NamedElement):

    def __init__(self, isAbstract: bool, soopl_Class: "soopl_Package" = None, soopl_Class7: set["soopl_Method"] = None, soopl_Class9: set["soopl_Property"] = None, soopl_Class12: "soopl_Class" = None, soopl_Class10: "soopl_Class" = None, soopl_Class26: "soopl_ComplexTypeProperty" = None, soopl_Class41: "soopl_ComplexTypeParameter" = None):
        self.isAbstract = isAbstract
        self.soopl_Class = soopl_Class
        self.soopl_Class7 = soopl_Class7 if soopl_Class7 is not None else set()
        self.soopl_Class9 = soopl_Class9 if soopl_Class9 is not None else set()
        self.soopl_Class12 = soopl_Class12
        self.soopl_Class10 = soopl_Class10
        self.soopl_Class26 = soopl_Class26
        self.soopl_Class41 = soopl_Class41
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def soopl_Class(self):
        return self.__soopl_Class

    @soopl_Class.setter
    def soopl_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Class__soopl_Class", None)
        self.__soopl_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soopl_Package"):
                opp_val = getattr(old_value, "soopl_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soopl_Package"):
                opp_val = getattr(value, "soopl_Package", None)
                if opp_val is None:
                    setattr(value, "soopl_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def soopl_Class41(self):
        return self.__soopl_Class41

    @soopl_Class41.setter
    def soopl_Class41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Class__soopl_Class41", None)
        self.__soopl_Class41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soopl_ComplexTypeParameter"):
                opp_val = getattr(old_value, "soopl_ComplexTypeParameter", None)
                if opp_val == self:
                    setattr(old_value, "soopl_ComplexTypeParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soopl_ComplexTypeParameter"):
                opp_val = getattr(value, "soopl_ComplexTypeParameter", None)
                setattr(value, "soopl_ComplexTypeParameter", self)

    @property
    def soopl_Class7(self):
        return self.__soopl_Class7

    @soopl_Class7.setter
    def soopl_Class7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Class__soopl_Class7", None)
        self.__soopl_Class7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soopl_Method"):
                    opp_val = getattr(item, "soopl_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "soopl_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soopl_Method"):
                    opp_val = getattr(item, "soopl_Method", None)
                    
                    setattr(item, "soopl_Method", self)
                    

    @property
    def soopl_Class26(self):
        return self.__soopl_Class26

    @soopl_Class26.setter
    def soopl_Class26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Class__soopl_Class26", None)
        self.__soopl_Class26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soopl_ComplexTypeProperty"):
                opp_val = getattr(old_value, "soopl_ComplexTypeProperty", None)
                if opp_val == self:
                    setattr(old_value, "soopl_ComplexTypeProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soopl_ComplexTypeProperty"):
                opp_val = getattr(value, "soopl_ComplexTypeProperty", None)
                setattr(value, "soopl_ComplexTypeProperty", self)

    @property
    def soopl_Class9(self):
        return self.__soopl_Class9

    @soopl_Class9.setter
    def soopl_Class9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Class__soopl_Class9", None)
        self.__soopl_Class9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soopl_Property"):
                    opp_val = getattr(item, "soopl_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "soopl_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soopl_Property"):
                    opp_val = getattr(item, "soopl_Property", None)
                    
                    setattr(item, "soopl_Property", self)
                    

    @property
    def soopl_Class12(self):
        return self.__soopl_Class12

    @soopl_Class12.setter
    def soopl_Class12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Class__soopl_Class12", None)
        self.__soopl_Class12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soopl_Class10"):
                opp_val = getattr(old_value, "soopl_Class10", None)
                if opp_val == self:
                    setattr(old_value, "soopl_Class10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soopl_Class10"):
                opp_val = getattr(value, "soopl_Class10", None)
                setattr(value, "soopl_Class10", self)

    @property
    def soopl_Class10(self):
        return self.__soopl_Class10

    @soopl_Class10.setter
    def soopl_Class10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soopl_Class__soopl_Class10", None)
        self.__soopl_Class10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soopl_Class12"):
                opp_val = getattr(old_value, "soopl_Class12", None)
                if opp_val == self:
                    setattr(old_value, "soopl_Class12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soopl_Class12"):
                opp_val = getattr(value, "soopl_Class12", None)
                setattr(value, "soopl_Class12", self)
