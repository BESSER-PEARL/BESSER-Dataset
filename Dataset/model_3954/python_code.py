from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class TypeOfContext(Enum):
    WIFI_STATUS = "WIFI_STATUS"
    BLUETOOTH_STATUS = "BLUETOOTH_STATUS"
    BATTERY_LEVEL = "BATTERY_LEVEL"
    CPU_LOAD = "CPU_LOAD"
    MEMORY_LOAD = "MEMORY_LOAD"
    AIRPLANE_MODE = "AIRPLANE_MODE"
    NETWORK_STATUS = "NETWORK_STATUS"
    GPS_STATUS = "GPS_STATUS"
class PseudostateKind(Enum):
    choice = "choice"
    deepHistory = "deepHistory"
    fork = "fork"
    initial = "initial"
    join = "join"
    junction = "junction"
    shallowHistory = "shallowHistory"
class TypeOfCondition(Enum):
    WHILE_EQUALS = "WHILE_EQUALS"
    WHILE_LOWER = "WHILE_LOWER"
    WHILE_HIGHER = "WHILE_HIGHER"
    WHEN_EQUALS = "WHEN_EQUALS"
    IS_OFF = "IS_OFF"
    IS_ON = "IS_ON"
    IS_EQUAL = "IS_EQUAL"
    WHEN_HIGHER = "WHEN_HIGHER"
    WHEN_LOWER = "WHEN_LOWER"
    IS_DIFFERENT = "IS_DIFFERENT"
class Operator(Enum):
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class Event:

    pass
class SecCon_AttackEvent(Event):

    pass
class SecCon_ThreatEvent(Event):

    pass
class SecCon_CountermeasureEvent(Event):

    pass
class SecCon_Action:

    def __init__(self, name: str, parameter: str, SecCon_Action: "SecCon_Rule" = None):
        self.name = name
        self.parameter = parameter
        self.SecCon_Action = SecCon_Action
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def SecCon_Action(self):
        return self.__SecCon_Action

    @SecCon_Action.setter
    def SecCon_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Action__SecCon_Action", None)
        self.__SecCon_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Rule99"):
                opp_val = getattr(old_value, "SecCon_Rule99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Rule99"):
                opp_val = getattr(value, "SecCon_Rule99", None)
                if opp_val is None:
                    setattr(value, "SecCon_Rule99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SecCon_Condition:

    def __init__(self, condition: str, value: str, logicValue: bool, SecCon_Condition: "SecCon_Rule" = None, SecCon_Condition101: "SecCon_ContextInformation" = None):
        self.condition = condition
        self.value = value
        self.logicValue = logicValue
        self.SecCon_Condition = SecCon_Condition
        self.SecCon_Condition101 = SecCon_Condition101
        
    @property
    def logicValue(self) -> bool:
        return self.__logicValue

    @logicValue.setter
    def logicValue(self, logicValue: bool):
        self.__logicValue = logicValue

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def SecCon_Condition(self):
        return self.__SecCon_Condition

    @SecCon_Condition.setter
    def SecCon_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Condition__SecCon_Condition", None)
        self.__SecCon_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Rule97"):
                opp_val = getattr(old_value, "SecCon_Rule97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Rule97"):
                opp_val = getattr(value, "SecCon_Rule97", None)
                if opp_val is None:
                    setattr(value, "SecCon_Rule97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SecCon_Condition101(self):
        return self.__SecCon_Condition101

    @SecCon_Condition101.setter
    def SecCon_Condition101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Condition__SecCon_Condition101", None)
        self.__SecCon_Condition101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_ContextInformation102"):
                opp_val = getattr(old_value, "SecCon_ContextInformation102", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_ContextInformation102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_ContextInformation102"):
                opp_val = getattr(value, "SecCon_ContextInformation102", None)
                setattr(value, "SecCon_ContextInformation102", self)

class SecCon_ContextInformation:

    def __init__(self, name: str, type: str, SecCon_ContextInformation: "SecCon_ContextScenario" = None, SecCon_ContextInformation102: "SecCon_Condition" = None):
        self.name = name
        self.type = type
        self.SecCon_ContextInformation = SecCon_ContextInformation
        self.SecCon_ContextInformation102 = SecCon_ContextInformation102
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SecCon_ContextInformation(self):
        return self.__SecCon_ContextInformation

    @SecCon_ContextInformation.setter
    def SecCon_ContextInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_ContextInformation__SecCon_ContextInformation", None)
        self.__SecCon_ContextInformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_ContextScenario95"):
                opp_val = getattr(old_value, "SecCon_ContextScenario95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_ContextScenario95"):
                opp_val = getattr(value, "SecCon_ContextScenario95", None)
                if opp_val is None:
                    setattr(value, "SecCon_ContextScenario95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SecCon_ContextInformation102(self):
        return self.__SecCon_ContextInformation102

    @SecCon_ContextInformation102.setter
    def SecCon_ContextInformation102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_ContextInformation__SecCon_ContextInformation102", None)
        self.__SecCon_ContextInformation102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Condition101"):
                opp_val = getattr(old_value, "SecCon_Condition101", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_Condition101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Condition101"):
                opp_val = getattr(value, "SecCon_Condition101", None)
                setattr(value, "SecCon_Condition101", self)

class SecCon_Rule:

    def __init__(self, name: str, operator: str, logicValue: bool, SecCon_Rule: "SecCon_ContextScenario" = None, SecCon_Rule97: set["SecCon_Condition"] = None, SecCon_Rule99: set["SecCon_Action"] = None):
        self.name = name
        self.operator = operator
        self.logicValue = logicValue
        self.SecCon_Rule = SecCon_Rule
        self.SecCon_Rule97 = SecCon_Rule97 if SecCon_Rule97 is not None else set()
        self.SecCon_Rule99 = SecCon_Rule99 if SecCon_Rule99 is not None else set()
        
    @property
    def logicValue(self) -> bool:
        return self.__logicValue

    @logicValue.setter
    def logicValue(self, logicValue: bool):
        self.__logicValue = logicValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def SecCon_Rule97(self):
        return self.__SecCon_Rule97

    @SecCon_Rule97.setter
    def SecCon_Rule97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Rule__SecCon_Rule97", None)
        self.__SecCon_Rule97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Condition"):
                    opp_val = getattr(item, "SecCon_Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Condition"):
                    opp_val = getattr(item, "SecCon_Condition", None)
                    
                    setattr(item, "SecCon_Condition", self)
                    

    @property
    def SecCon_Rule99(self):
        return self.__SecCon_Rule99

    @SecCon_Rule99.setter
    def SecCon_Rule99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Rule__SecCon_Rule99", None)
        self.__SecCon_Rule99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Action"):
                    opp_val = getattr(item, "SecCon_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Action"):
                    opp_val = getattr(item, "SecCon_Action", None)
                    
                    setattr(item, "SecCon_Action", self)
                    

    @property
    def SecCon_Rule(self):
        return self.__SecCon_Rule

    @SecCon_Rule.setter
    def SecCon_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Rule__SecCon_Rule", None)
        self.__SecCon_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_ContextScenario93"):
                opp_val = getattr(old_value, "SecCon_ContextScenario93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_ContextScenario93"):
                opp_val = getattr(value, "SecCon_ContextScenario93", None)
                if opp_val is None:
                    setattr(value, "SecCon_ContextScenario93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SecCon_ContextScenario:

    def __init__(self, name: str, SecCon_ContextScenario: "SecCon_Project" = None, SecCon_ContextScenario93: set["SecCon_Rule"] = None, SecCon_ContextScenario95: set["SecCon_ContextInformation"] = None):
        self.name = name
        self.SecCon_ContextScenario = SecCon_ContextScenario
        self.SecCon_ContextScenario93 = SecCon_ContextScenario93 if SecCon_ContextScenario93 is not None else set()
        self.SecCon_ContextScenario95 = SecCon_ContextScenario95 if SecCon_ContextScenario95 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SecCon_ContextScenario(self):
        return self.__SecCon_ContextScenario

    @SecCon_ContextScenario.setter
    def SecCon_ContextScenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_ContextScenario__SecCon_ContextScenario", None)
        self.__SecCon_ContextScenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Project91"):
                opp_val = getattr(old_value, "SecCon_Project91", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Project91"):
                opp_val = getattr(value, "SecCon_Project91", None)
                if opp_val is None:
                    setattr(value, "SecCon_Project91", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SecCon_ContextScenario93(self):
        return self.__SecCon_ContextScenario93

    @SecCon_ContextScenario93.setter
    def SecCon_ContextScenario93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_ContextScenario__SecCon_ContextScenario93", None)
        self.__SecCon_ContextScenario93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Rule"):
                    opp_val = getattr(item, "SecCon_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Rule"):
                    opp_val = getattr(item, "SecCon_Rule", None)
                    
                    setattr(item, "SecCon_Rule", self)
                    

    @property
    def SecCon_ContextScenario95(self):
        return self.__SecCon_ContextScenario95

    @SecCon_ContextScenario95.setter
    def SecCon_ContextScenario95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_ContextScenario__SecCon_ContextScenario95", None)
        self.__SecCon_ContextScenario95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_ContextInformation"):
                    opp_val = getattr(item, "SecCon_ContextInformation", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_ContextInformation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_ContextInformation"):
                    opp_val = getattr(item, "SecCon_ContextInformation", None)
                    
                    setattr(item, "SecCon_ContextInformation", self)
                    

class State:

    pass
class SecCon_ProtectedState(State):

    pass
class SecCon_AttackedState(State):

    pass
class SecCon_VulnerableState(State):

    pass
class SecCon_ThreatenedState(State):

    pass
class StateVertex:

    pass
class SecCon_InitialState(StateVertex):

    pass
class SecCon_FinalState(StateVertex):

    pass
class SecCon_State(StateVertex):

    pass
class UseCase:

    pass
class SecCon_VulnerabilityUseCase(UseCase):

    pass
class SecCon_AttackUseCase(UseCase):

    pass
class SecCon_ThreatUseCase(UseCase):

    pass
class SecCon_Extend:

    def __init__(self, name: str, condition: str, extend: "SecCon_UseCase" = None, extends: "SecCon_UseCase" = None, SecCon_Extend: "SecCon_UseCaseScenario" = None, SecCon_Extend57: "SecCon_UseCaseScenario" = None, Extend: "SecCon_UseCase" = None, Extend38: "SecCon_UseCase" = None):
        self.name = name
        self.condition = condition
        self.extend = extend
        self.extends = extends
        self.SecCon_Extend = SecCon_Extend
        self.SecCon_Extend57 = SecCon_Extend57
        self.Extend = Extend
        self.Extend38 = Extend38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def SecCon_Extend57(self):
        return self.__SecCon_Extend57

    @SecCon_Extend57.setter
    def SecCon_Extend57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Extend__SecCon_Extend57", None)
        self.__SecCon_Extend57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_UseCaseScenario56"):
                opp_val = getattr(old_value, "SecCon_UseCaseScenario56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_UseCaseScenario56"):
                opp_val = getattr(value, "SecCon_UseCaseScenario56", None)
                if opp_val is None:
                    setattr(value, "SecCon_UseCaseScenario56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SecCon_Extend(self):
        return self.__SecCon_Extend

    @SecCon_Extend.setter
    def SecCon_Extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Extend__SecCon_Extend", None)
        self.__SecCon_Extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_UseCaseScenario51"):
                opp_val = getattr(old_value, "SecCon_UseCaseScenario51", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_UseCaseScenario51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_UseCaseScenario51"):
                opp_val = getattr(value, "SecCon_UseCaseScenario51", None)
                setattr(value, "SecCon_UseCaseScenario51", self)

    @property
    def extend(self):
        return self.__extend

    @extend.setter
    def extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Extend__extend", None)
        self.__extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase47"):
                opp_val = getattr(old_value, "UseCase47", None)
                if opp_val == self:
                    setattr(old_value, "UseCase47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase47"):
                opp_val = getattr(value, "UseCase47", None)
                setattr(value, "UseCase47", self)

    @property
    def Extend(self):
        return self.__Extend

    @Extend.setter
    def Extend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Extend__Extend", None)
        self.__Extend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extension"):
                opp_val = getattr(old_value, "extension", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extension"):
                opp_val = getattr(value, "extension", None)
                if opp_val is None:
                    setattr(value, "extension", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extends(self):
        return self.__extends

    @extends.setter
    def extends(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Extend__extends", None)
        self.__extends = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase49"):
                opp_val = getattr(old_value, "UseCase49", None)
                if opp_val == self:
                    setattr(old_value, "UseCase49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase49"):
                opp_val = getattr(value, "UseCase49", None)
                setattr(value, "UseCase49", self)

    @property
    def Extend38(self):
        return self.__Extend38

    @Extend38.setter
    def Extend38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Extend__Extend38", None)
        self.__Extend38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base37"):
                opp_val = getattr(old_value, "base37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base37"):
                opp_val = getattr(value, "base37", None)
                if opp_val is None:
                    setattr(value, "base37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SecCon_DetectionUseCase(UseCase):

    pass
class SecCon_PrevenctionUseCase(UseCase):

    pass
class SecCon_RecoverUseCase(UseCase):

    pass
class SecCon_CountermeasureUseCase(UseCase):

    pass
class Type:

    pass
class SecCon_Class(Type):

    def __init__(self, isAbstract: bool, SecCon_Class: set["SecCon_Operation"] = None, SecCon_Class17: "SecCon_Class" = None, SecCon_Class15: set["SecCon_Class"] = None, SecCon_Class19: set["SecCon_Attribute"] = None):
        self.isAbstract = isAbstract
        self.SecCon_Class = SecCon_Class if SecCon_Class is not None else set()
        self.SecCon_Class17 = SecCon_Class17
        self.SecCon_Class15 = SecCon_Class15 if SecCon_Class15 is not None else set()
        self.SecCon_Class19 = SecCon_Class19 if SecCon_Class19 is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def SecCon_Class(self):
        return self.__SecCon_Class

    @SecCon_Class.setter
    def SecCon_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Class__SecCon_Class", None)
        self.__SecCon_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Operation14"):
                    opp_val = getattr(item, "SecCon_Operation14", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Operation14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Operation14"):
                    opp_val = getattr(item, "SecCon_Operation14", None)
                    
                    setattr(item, "SecCon_Operation14", self)
                    

    @property
    def SecCon_Class19(self):
        return self.__SecCon_Class19

    @SecCon_Class19.setter
    def SecCon_Class19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Class__SecCon_Class19", None)
        self.__SecCon_Class19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Attribute20"):
                    opp_val = getattr(item, "SecCon_Attribute20", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Attribute20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Attribute20"):
                    opp_val = getattr(item, "SecCon_Attribute20", None)
                    
                    setattr(item, "SecCon_Attribute20", self)
                    

    @property
    def SecCon_Class15(self):
        return self.__SecCon_Class15

    @SecCon_Class15.setter
    def SecCon_Class15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Class__SecCon_Class15", None)
        self.__SecCon_Class15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Class17"):
                    opp_val = getattr(item, "SecCon_Class17", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Class17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Class17"):
                    opp_val = getattr(item, "SecCon_Class17", None)
                    
                    setattr(item, "SecCon_Class17", self)
                    

    @property
    def SecCon_Class17(self):
        return self.__SecCon_Class17

    @SecCon_Class17.setter
    def SecCon_Class17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Class__SecCon_Class17", None)
        self.__SecCon_Class17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Class15"):
                opp_val = getattr(old_value, "SecCon_Class15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Class15"):
                opp_val = getattr(value, "SecCon_Class15", None)
                if opp_val is None:
                    setattr(value, "SecCon_Class15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SecCon_Include:

    def __init__(self, name: str, Include: "SecCon_UseCase" = None, Include34: "SecCon_UseCase" = None, includes: "SecCon_UseCase" = None, include: "SecCon_UseCase" = None, SecCon_Include: "SecCon_UseCaseScenario" = None, SecCon_Include60: "SecCon_UseCaseScenario" = None):
        self.name = name
        self.Include = Include
        self.Include34 = Include34
        self.includes = includes
        self.include = include
        self.SecCon_Include = SecCon_Include
        self.SecCon_Include60 = SecCon_Include60
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def includes(self):
        return self.__includes

    @includes.setter
    def includes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Include__includes", None)
        self.__includes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase"):
                opp_val = getattr(old_value, "UseCase", None)
                if opp_val == self:
                    setattr(old_value, "UseCase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase"):
                opp_val = getattr(value, "UseCase", None)
                setattr(value, "UseCase", self)

    @property
    def Include34(self):
        return self.__Include34

    @Include34.setter
    def Include34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Include__Include34", None)
        self.__Include34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "base"):
                opp_val = getattr(old_value, "base", None)
                if opp_val == self:
                    setattr(old_value, "base", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "base"):
                opp_val = getattr(value, "base", None)
                setattr(value, "base", self)

    @property
    def SecCon_Include60(self):
        return self.__SecCon_Include60

    @SecCon_Include60.setter
    def SecCon_Include60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Include__SecCon_Include60", None)
        self.__SecCon_Include60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_UseCaseScenario59"):
                opp_val = getattr(old_value, "SecCon_UseCaseScenario59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_UseCaseScenario59"):
                opp_val = getattr(value, "SecCon_UseCaseScenario59", None)
                if opp_val is None:
                    setattr(value, "SecCon_UseCaseScenario59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def include(self):
        return self.__include

    @include.setter
    def include(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Include__include", None)
        self.__include = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase43"):
                opp_val = getattr(old_value, "UseCase43", None)
                if opp_val == self:
                    setattr(old_value, "UseCase43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase43"):
                opp_val = getattr(value, "UseCase43", None)
                setattr(value, "UseCase43", self)

    @property
    def Include(self):
        return self.__Include

    @Include.setter
    def Include(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Include__Include", None)
        self.__Include = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "addition"):
                opp_val = getattr(old_value, "addition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "addition"):
                opp_val = getattr(value, "addition", None)
                if opp_val is None:
                    setattr(value, "addition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SecCon_Include(self):
        return self.__SecCon_Include

    @SecCon_Include.setter
    def SecCon_Include(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Include__SecCon_Include", None)
        self.__SecCon_Include = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_UseCaseScenario45"):
                opp_val = getattr(old_value, "SecCon_UseCaseScenario45", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_UseCaseScenario45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_UseCaseScenario45"):
                opp_val = getattr(value, "SecCon_UseCaseScenario45", None)
                setattr(value, "SecCon_UseCaseScenario45", self)

class DataType:

    pass
class SecCon_Enumeration(DataType):

    pass
class SecCon_PrimitiveType(DataType):

    pass
class SecCon_DataType(Type):

    pass
class NamedElement:

    pass
class SecCon_StateMachineScenario(NamedElement):

    def __init__(self, author: str, version: str, SecCon_StateMachineScenario68: set["SecCon_Transition"] = None, SecCon_StateMachineScenario: set["SecCon_StateVertex"] = None, SecCon_StateMachineScenario66: set["SecCon_Event"] = None, SecCon_StateMachineScenario89: "SecCon_Project" = None):
        self.author = author
        self.version = version
        self.SecCon_StateMachineScenario68 = SecCon_StateMachineScenario68 if SecCon_StateMachineScenario68 is not None else set()
        self.SecCon_StateMachineScenario = SecCon_StateMachineScenario if SecCon_StateMachineScenario is not None else set()
        self.SecCon_StateMachineScenario66 = SecCon_StateMachineScenario66 if SecCon_StateMachineScenario66 is not None else set()
        self.SecCon_StateMachineScenario89 = SecCon_StateMachineScenario89
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def SecCon_StateMachineScenario68(self):
        return self.__SecCon_StateMachineScenario68

    @SecCon_StateMachineScenario68.setter
    def SecCon_StateMachineScenario68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_StateMachineScenario__SecCon_StateMachineScenario68", None)
        self.__SecCon_StateMachineScenario68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Transition"):
                    opp_val = getattr(item, "SecCon_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Transition"):
                    opp_val = getattr(item, "SecCon_Transition", None)
                    
                    setattr(item, "SecCon_Transition", self)
                    

    @property
    def SecCon_StateMachineScenario89(self):
        return self.__SecCon_StateMachineScenario89

    @SecCon_StateMachineScenario89.setter
    def SecCon_StateMachineScenario89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_StateMachineScenario__SecCon_StateMachineScenario89", None)
        self.__SecCon_StateMachineScenario89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Project88"):
                opp_val = getattr(old_value, "SecCon_Project88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Project88"):
                opp_val = getattr(value, "SecCon_Project88", None)
                if opp_val is None:
                    setattr(value, "SecCon_Project88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SecCon_StateMachineScenario(self):
        return self.__SecCon_StateMachineScenario

    @SecCon_StateMachineScenario.setter
    def SecCon_StateMachineScenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_StateMachineScenario__SecCon_StateMachineScenario", None)
        self.__SecCon_StateMachineScenario = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_StateVertex"):
                    opp_val = getattr(item, "SecCon_StateVertex", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_StateVertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_StateVertex"):
                    opp_val = getattr(item, "SecCon_StateVertex", None)
                    
                    setattr(item, "SecCon_StateVertex", self)
                    

    @property
    def SecCon_StateMachineScenario66(self):
        return self.__SecCon_StateMachineScenario66

    @SecCon_StateMachineScenario66.setter
    def SecCon_StateMachineScenario66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_StateMachineScenario__SecCon_StateMachineScenario66", None)
        self.__SecCon_StateMachineScenario66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Event"):
                    opp_val = getattr(item, "SecCon_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Event"):
                    opp_val = getattr(item, "SecCon_Event", None)
                    
                    setattr(item, "SecCon_Event", self)
                    

class SecCon_Actor(NamedElement):

    pass
class SecCon_EnumerationLiteral(NamedElement):

    pass
class SecCon_Package(NamedElement):

    pass
class SecCon_Transition(NamedElement):

    pass
class SecCon_Project(NamedElement):

    pass
class SecCon_StateOperation(NamedElement):

    pass
class SecCon_Type(NamedElement):

    pass
class SecCon_StateVertex(NamedElement):

    pass
class SecCon_Event(NamedElement):

    pass
class SecCon_UseCase(NamedElement):

    def __init__(self, description: str, preCondition: str, SecCon_UseCase: set["SecCon_Actor"] = None, addition: set["SecCon_Include"] = None, base: "SecCon_Include" = None, UseCase: "SecCon_Include" = None, UseCase43: "SecCon_Include" = None, UseCase47: "SecCon_Extend" = None, UseCase49: "SecCon_Extend" = None, SecCon_UseCase54: "SecCon_UseCaseScenario" = None, extension: set["SecCon_Extend"] = None, base37: set["SecCon_Extend"] = None, SecCon_UseCase40: "SecCon_UseCaseScenario" = None):
        self.description = description
        self.preCondition = preCondition
        self.SecCon_UseCase = SecCon_UseCase if SecCon_UseCase is not None else set()
        self.addition = addition if addition is not None else set()
        self.base = base
        self.UseCase = UseCase
        self.UseCase43 = UseCase43
        self.UseCase47 = UseCase47
        self.UseCase49 = UseCase49
        self.SecCon_UseCase54 = SecCon_UseCase54
        self.extension = extension if extension is not None else set()
        self.base37 = base37 if base37 is not None else set()
        self.SecCon_UseCase40 = SecCon_UseCase40
        
    @property
    def preCondition(self) -> str:
        return self.__preCondition

    @preCondition.setter
    def preCondition(self, preCondition: str):
        self.__preCondition = preCondition

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def UseCase(self):
        return self.__UseCase

    @UseCase.setter
    def UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__UseCase", None)
        self.__UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "includes"):
                opp_val = getattr(old_value, "includes", None)
                if opp_val == self:
                    setattr(old_value, "includes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "includes"):
                opp_val = getattr(value, "includes", None)
                setattr(value, "includes", self)

    @property
    def UseCase43(self):
        return self.__UseCase43

    @UseCase43.setter
    def UseCase43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__UseCase43", None)
        self.__UseCase43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "include"):
                opp_val = getattr(old_value, "include", None)
                if opp_val == self:
                    setattr(old_value, "include", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "include"):
                opp_val = getattr(value, "include", None)
                setattr(value, "include", self)

    @property
    def SecCon_UseCase(self):
        return self.__SecCon_UseCase

    @SecCon_UseCase.setter
    def SecCon_UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__SecCon_UseCase", None)
        self.__SecCon_UseCase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Actor"):
                    opp_val = getattr(item, "SecCon_Actor", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Actor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Actor"):
                    opp_val = getattr(item, "SecCon_Actor", None)
                    
                    setattr(item, "SecCon_Actor", self)
                    

    @property
    def UseCase47(self):
        return self.__UseCase47

    @UseCase47.setter
    def UseCase47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__UseCase47", None)
        self.__UseCase47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extend"):
                opp_val = getattr(old_value, "extend", None)
                if opp_val == self:
                    setattr(old_value, "extend", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extend"):
                opp_val = getattr(value, "extend", None)
                setattr(value, "extend", self)

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__base", None)
        self.__base = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Include34"):
                opp_val = getattr(old_value, "Include34", None)
                if opp_val == self:
                    setattr(old_value, "Include34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Include34"):
                opp_val = getattr(value, "Include34", None)
                setattr(value, "Include34", self)

    @property
    def SecCon_UseCase54(self):
        return self.__SecCon_UseCase54

    @SecCon_UseCase54.setter
    def SecCon_UseCase54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__SecCon_UseCase54", None)
        self.__SecCon_UseCase54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_UseCaseScenario53"):
                opp_val = getattr(old_value, "SecCon_UseCaseScenario53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_UseCaseScenario53"):
                opp_val = getattr(value, "SecCon_UseCaseScenario53", None)
                if opp_val is None:
                    setattr(value, "SecCon_UseCaseScenario53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def addition(self):
        return self.__addition

    @addition.setter
    def addition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__addition", None)
        self.__addition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Include"):
                    opp_val = getattr(item, "Include", None)
                    
                    if opp_val == self:
                        setattr(item, "Include", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Include"):
                    opp_val = getattr(item, "Include", None)
                    
                    setattr(item, "Include", self)
                    

    @property
    def base37(self):
        return self.__base37

    @base37.setter
    def base37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__base37", None)
        self.__base37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Extend38"):
                    opp_val = getattr(item, "Extend38", None)
                    
                    if opp_val == self:
                        setattr(item, "Extend38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Extend38"):
                    opp_val = getattr(item, "Extend38", None)
                    
                    setattr(item, "Extend38", self)
                    

    @property
    def SecCon_UseCase40(self):
        return self.__SecCon_UseCase40

    @SecCon_UseCase40.setter
    def SecCon_UseCase40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__SecCon_UseCase40", None)
        self.__SecCon_UseCase40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_UseCaseScenario"):
                opp_val = getattr(old_value, "SecCon_UseCaseScenario", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_UseCaseScenario", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_UseCaseScenario"):
                opp_val = getattr(value, "SecCon_UseCaseScenario", None)
                setattr(value, "SecCon_UseCaseScenario", self)

    @property
    def UseCase49(self):
        return self.__UseCase49

    @UseCase49.setter
    def UseCase49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__UseCase49", None)
        self.__UseCase49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extends"):
                opp_val = getattr(old_value, "extends", None)
                if opp_val == self:
                    setattr(old_value, "extends", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extends"):
                opp_val = getattr(value, "extends", None)
                setattr(value, "extends", self)

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCase__extension", None)
        self.__extension = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Extend"):
                    opp_val = getattr(item, "Extend", None)
                    
                    if opp_val == self:
                        setattr(item, "Extend", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Extend"):
                    opp_val = getattr(item, "Extend", None)
                    
                    setattr(item, "Extend", self)
                    

class SecCon_UseCaseScenario(NamedElement):

    def __init__(self, author: str, version: str, SecCon_UseCaseScenario45: "SecCon_Include" = None, SecCon_UseCaseScenario51: "SecCon_Extend" = None, SecCon_UseCaseScenario53: set["SecCon_UseCase"] = None, SecCon_UseCaseScenario56: set["SecCon_Extend"] = None, SecCon_UseCaseScenario59: set["SecCon_Include"] = None, SecCon_UseCaseScenario: "SecCon_UseCase" = None, SecCon_UseCaseScenario62: set["SecCon_Actor"] = None, SecCon_UseCaseScenario86: "SecCon_Project" = None):
        self.author = author
        self.version = version
        self.SecCon_UseCaseScenario45 = SecCon_UseCaseScenario45
        self.SecCon_UseCaseScenario51 = SecCon_UseCaseScenario51
        self.SecCon_UseCaseScenario53 = SecCon_UseCaseScenario53 if SecCon_UseCaseScenario53 is not None else set()
        self.SecCon_UseCaseScenario56 = SecCon_UseCaseScenario56 if SecCon_UseCaseScenario56 is not None else set()
        self.SecCon_UseCaseScenario59 = SecCon_UseCaseScenario59 if SecCon_UseCaseScenario59 is not None else set()
        self.SecCon_UseCaseScenario = SecCon_UseCaseScenario
        self.SecCon_UseCaseScenario62 = SecCon_UseCaseScenario62 if SecCon_UseCaseScenario62 is not None else set()
        self.SecCon_UseCaseScenario86 = SecCon_UseCaseScenario86
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def SecCon_UseCaseScenario56(self):
        return self.__SecCon_UseCaseScenario56

    @SecCon_UseCaseScenario56.setter
    def SecCon_UseCaseScenario56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCaseScenario__SecCon_UseCaseScenario56", None)
        self.__SecCon_UseCaseScenario56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Extend57"):
                    opp_val = getattr(item, "SecCon_Extend57", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Extend57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Extend57"):
                    opp_val = getattr(item, "SecCon_Extend57", None)
                    
                    setattr(item, "SecCon_Extend57", self)
                    

    @property
    def SecCon_UseCaseScenario62(self):
        return self.__SecCon_UseCaseScenario62

    @SecCon_UseCaseScenario62.setter
    def SecCon_UseCaseScenario62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCaseScenario__SecCon_UseCaseScenario62", None)
        self.__SecCon_UseCaseScenario62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Actor63"):
                    opp_val = getattr(item, "SecCon_Actor63", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Actor63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Actor63"):
                    opp_val = getattr(item, "SecCon_Actor63", None)
                    
                    setattr(item, "SecCon_Actor63", self)
                    

    @property
    def SecCon_UseCaseScenario53(self):
        return self.__SecCon_UseCaseScenario53

    @SecCon_UseCaseScenario53.setter
    def SecCon_UseCaseScenario53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCaseScenario__SecCon_UseCaseScenario53", None)
        self.__SecCon_UseCaseScenario53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_UseCase54"):
                    opp_val = getattr(item, "SecCon_UseCase54", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_UseCase54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_UseCase54"):
                    opp_val = getattr(item, "SecCon_UseCase54", None)
                    
                    setattr(item, "SecCon_UseCase54", self)
                    

    @property
    def SecCon_UseCaseScenario51(self):
        return self.__SecCon_UseCaseScenario51

    @SecCon_UseCaseScenario51.setter
    def SecCon_UseCaseScenario51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCaseScenario__SecCon_UseCaseScenario51", None)
        self.__SecCon_UseCaseScenario51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Extend"):
                opp_val = getattr(old_value, "SecCon_Extend", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_Extend", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Extend"):
                opp_val = getattr(value, "SecCon_Extend", None)
                setattr(value, "SecCon_Extend", self)

    @property
    def SecCon_UseCaseScenario45(self):
        return self.__SecCon_UseCaseScenario45

    @SecCon_UseCaseScenario45.setter
    def SecCon_UseCaseScenario45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCaseScenario__SecCon_UseCaseScenario45", None)
        self.__SecCon_UseCaseScenario45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Include"):
                opp_val = getattr(old_value, "SecCon_Include", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_Include", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Include"):
                opp_val = getattr(value, "SecCon_Include", None)
                setattr(value, "SecCon_Include", self)

    @property
    def SecCon_UseCaseScenario59(self):
        return self.__SecCon_UseCaseScenario59

    @SecCon_UseCaseScenario59.setter
    def SecCon_UseCaseScenario59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCaseScenario__SecCon_UseCaseScenario59", None)
        self.__SecCon_UseCaseScenario59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Include60"):
                    opp_val = getattr(item, "SecCon_Include60", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Include60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Include60"):
                    opp_val = getattr(item, "SecCon_Include60", None)
                    
                    setattr(item, "SecCon_Include60", self)
                    

    @property
    def SecCon_UseCaseScenario(self):
        return self.__SecCon_UseCaseScenario

    @SecCon_UseCaseScenario.setter
    def SecCon_UseCaseScenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCaseScenario__SecCon_UseCaseScenario", None)
        self.__SecCon_UseCaseScenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_UseCase40"):
                opp_val = getattr(old_value, "SecCon_UseCase40", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_UseCase40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_UseCase40"):
                opp_val = getattr(value, "SecCon_UseCase40", None)
                setattr(value, "SecCon_UseCase40", self)

    @property
    def SecCon_UseCaseScenario86(self):
        return self.__SecCon_UseCaseScenario86

    @SecCon_UseCaseScenario86.setter
    def SecCon_UseCaseScenario86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_UseCaseScenario__SecCon_UseCaseScenario86", None)
        self.__SecCon_UseCaseScenario86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Project85"):
                opp_val = getattr(old_value, "SecCon_Project85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Project85"):
                opp_val = getattr(value, "SecCon_Project85", None)
                if opp_val is None:
                    setattr(value, "SecCon_Project85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SecCon_TypedElement(NamedElement):

    pass
class SecCon_Comment:

    def __init__(self, body: str, SecCon_Comment3: set["SecCon_Element"] = None, SecCon_Comment: "SecCon_Element" = None):
        self.body = body
        self.SecCon_Comment3 = SecCon_Comment3 if SecCon_Comment3 is not None else set()
        self.SecCon_Comment = SecCon_Comment
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def SecCon_Comment3(self):
        return self.__SecCon_Comment3

    @SecCon_Comment3.setter
    def SecCon_Comment3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Comment__SecCon_Comment3", None)
        self.__SecCon_Comment3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Element4"):
                    opp_val = getattr(item, "SecCon_Element4", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Element4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Element4"):
                    opp_val = getattr(item, "SecCon_Element4", None)
                    
                    setattr(item, "SecCon_Element4", self)
                    

    @property
    def SecCon_Comment(self):
        return self.__SecCon_Comment

    @SecCon_Comment.setter
    def SecCon_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Comment__SecCon_Comment", None)
        self.__SecCon_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Element"):
                opp_val = getattr(old_value, "SecCon_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Element"):
                opp_val = getattr(value, "SecCon_Element", None)
                if opp_val is None:
                    setattr(value, "SecCon_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SecCon_Element(ABC):

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class SecCon_Parameter(MultiplicityElement, TypedElement):

    def __init__(self, default: str, direction: str, SecCon_Parameter: "SecCon_Operation" = None):
        self.default = default
        self.direction = direction
        self.SecCon_Parameter = SecCon_Parameter
        
    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def SecCon_Parameter(self):
        return self.__SecCon_Parameter

    @SecCon_Parameter.setter
    def SecCon_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Parameter__SecCon_Parameter", None)
        self.__SecCon_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Operation10"):
                opp_val = getattr(old_value, "SecCon_Operation10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Operation10"):
                opp_val = getattr(value, "SecCon_Operation10", None)
                if opp_val is None:
                    setattr(value, "SecCon_Operation10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SecCon_Operation(MultiplicityElement, TypedElement):

    def __init__(self, body: str, SecCon_Operation: set["SecCon_Type"] = None, SecCon_Operation10: set["SecCon_Parameter"] = None, SecCon_Operation14: "SecCon_Class" = None):
        self.body = body
        self.SecCon_Operation = SecCon_Operation if SecCon_Operation is not None else set()
        self.SecCon_Operation10 = SecCon_Operation10 if SecCon_Operation10 is not None else set()
        self.SecCon_Operation14 = SecCon_Operation14
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def SecCon_Operation10(self):
        return self.__SecCon_Operation10

    @SecCon_Operation10.setter
    def SecCon_Operation10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Operation__SecCon_Operation10", None)
        self.__SecCon_Operation10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Parameter"):
                    opp_val = getattr(item, "SecCon_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Parameter"):
                    opp_val = getattr(item, "SecCon_Parameter", None)
                    
                    setattr(item, "SecCon_Parameter", self)
                    

    @property
    def SecCon_Operation14(self):
        return self.__SecCon_Operation14

    @SecCon_Operation14.setter
    def SecCon_Operation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Operation__SecCon_Operation14", None)
        self.__SecCon_Operation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Class"):
                opp_val = getattr(old_value, "SecCon_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Class"):
                opp_val = getattr(value, "SecCon_Class", None)
                if opp_val is None:
                    setattr(value, "SecCon_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SecCon_Operation(self):
        return self.__SecCon_Operation

    @SecCon_Operation.setter
    def SecCon_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Operation__SecCon_Operation", None)
        self.__SecCon_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecCon_Type8"):
                    opp_val = getattr(item, "SecCon_Type8", None)
                    
                    if opp_val == self:
                        setattr(item, "SecCon_Type8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecCon_Type8"):
                    opp_val = getattr(item, "SecCon_Type8", None)
                    
                    setattr(item, "SecCon_Type8", self)
                    

class SecCon_Attribute(MultiplicityElement, TypedElement):

    def __init__(self, isReadOnly: bool, default: str, isComposite: bool, isDerived: bool, isID: bool, SecCon_Attribute: "SecCon_Attribute" = None, SecCon_Attribute5: "SecCon_Attribute" = None, SecCon_Attribute20: "SecCon_Class" = None):
        self.isReadOnly = isReadOnly
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.SecCon_Attribute = SecCon_Attribute
        self.SecCon_Attribute5 = SecCon_Attribute5
        self.SecCon_Attribute20 = SecCon_Attribute20
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def isID(self) -> bool:
        return self.__isID

    @isID.setter
    def isID(self, isID: bool):
        self.__isID = isID

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def SecCon_Attribute5(self):
        return self.__SecCon_Attribute5

    @SecCon_Attribute5.setter
    def SecCon_Attribute5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Attribute__SecCon_Attribute5", None)
        self.__SecCon_Attribute5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Attribute"):
                opp_val = getattr(old_value, "SecCon_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Attribute"):
                opp_val = getattr(value, "SecCon_Attribute", None)
                setattr(value, "SecCon_Attribute", self)

    @property
    def SecCon_Attribute(self):
        return self.__SecCon_Attribute

    @SecCon_Attribute.setter
    def SecCon_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Attribute__SecCon_Attribute", None)
        self.__SecCon_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Attribute5"):
                opp_val = getattr(old_value, "SecCon_Attribute5", None)
                if opp_val == self:
                    setattr(old_value, "SecCon_Attribute5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Attribute5"):
                opp_val = getattr(value, "SecCon_Attribute5", None)
                setattr(value, "SecCon_Attribute5", self)

    @property
    def SecCon_Attribute20(self):
        return self.__SecCon_Attribute20

    @SecCon_Attribute20.setter
    def SecCon_Attribute20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SecCon_Attribute__SecCon_Attribute20", None)
        self.__SecCon_Attribute20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SecCon_Class19"):
                opp_val = getattr(old_value, "SecCon_Class19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SecCon_Class19"):
                opp_val = getattr(value, "SecCon_Class19", None)
                if opp_val is None:
                    setattr(value, "SecCon_Class19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class SecCon_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SecCon_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, lower: int, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower
