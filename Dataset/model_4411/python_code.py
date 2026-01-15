from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ModuleKind(Enum):
    digital = "digital"
    analog = "analog"
class OperatorKind(Enum):
    equal = "equal"
    minus = "minus"
    upper = "upper"
    lower = "lower"
    plus = "plus"
    diff = "diff"
    upperOrEqual = "upperOrEqual"
    lowerOrEqual = "lowerOrEqual"
    mul = "mul"
    div = "div"
    min = "min"
    max = "max"
    pourcent = "pourcent"
    and = "and"
    or = "or"
    not = "not"
class ParameterType(Enum):
    Delay = "Delay"
    Level = "Level"
    Status = "Status"
    Constant = "Constant"
    Sensor = "Sensor"
class Time(Enum):
    MilliSecond = "MilliSecond"
    MicroSecond = "MicroSecond"
class Library(Enum):
    none = "none"
    servo = "servo"
    music = "music"


############################################
# Definition of Classes
############################################

class arduino_Parameter(ABC):

    pass
class arduino_ParameterDefinition:

    def __init__(self, type: str, name: str, arduino_ParameterDefinition: "arduino_Function" = None, arduino_ParameterDefinition62: "arduino_Parameter" = None, arduino_ParameterDefinition69: "arduino_ParameterCall" = None):
        self.type = type
        self.name = name
        self.arduino_ParameterDefinition = arduino_ParameterDefinition
        self.arduino_ParameterDefinition62 = arduino_ParameterDefinition62
        self.arduino_ParameterDefinition69 = arduino_ParameterDefinition69
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def arduino_ParameterDefinition(self):
        return self.__arduino_ParameterDefinition

    @arduino_ParameterDefinition.setter
    def arduino_ParameterDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_ParameterDefinition__arduino_ParameterDefinition", None)
        self.__arduino_ParameterDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Function57"):
                opp_val = getattr(old_value, "arduino_Function57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Function57"):
                opp_val = getattr(value, "arduino_Function57", None)
                if opp_val is None:
                    setattr(value, "arduino_Function57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_ParameterDefinition69(self):
        return self.__arduino_ParameterDefinition69

    @arduino_ParameterDefinition69.setter
    def arduino_ParameterDefinition69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_ParameterDefinition__arduino_ParameterDefinition69", None)
        self.__arduino_ParameterDefinition69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_ParameterCall"):
                opp_val = getattr(old_value, "arduino_ParameterCall", None)
                if opp_val == self:
                    setattr(old_value, "arduino_ParameterCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_ParameterCall"):
                opp_val = getattr(value, "arduino_ParameterCall", None)
                setattr(value, "arduino_ParameterCall", self)

    @property
    def arduino_ParameterDefinition62(self):
        return self.__arduino_ParameterDefinition62

    @arduino_ParameterDefinition62.setter
    def arduino_ParameterDefinition62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_ParameterDefinition__arduino_ParameterDefinition62", None)
        self.__arduino_ParameterDefinition62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Parameter"):
                opp_val = getattr(old_value, "arduino_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Parameter"):
                opp_val = getattr(value, "arduino_Parameter", None)
                setattr(value, "arduino_Parameter", self)

class BooleanOperator:

    pass
class Control:

    pass
class arduino_If(Control):

    pass
class arduino_Repeat(Control):

    def __init__(self, iteration: int):
        self.iteration = iteration
        
    @property
    def iteration(self) -> int:
        return self.__iteration

    @iteration.setter
    def iteration(self, iteration: int):
        self.__iteration = iteration

class MathOperator:

    pass
class arduino_NumericalOperator(MathOperator):

    pass
class arduino_BooleanOperator(MathOperator):

    pass
class arduino_While(Control):

    pass
class arduino_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Module:

    pass
class arduino_OutputModule(Module):

    pass
class arduino_InputModule(Module):

    pass
class Utilities:

    pass
class arduino_Delay(Utilities):

    def __init__(self, unit: str, value: int):
        self.unit = unit
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

class Parameter:

    pass
class Value:

    pass
class arduino_Constant(Value):

    pass
class ModuleInstruction:

    pass
class arduino_Sensor(ModuleInstruction, BooleanOperator):

    pass
class arduino_Level(ModuleInstruction):

    pass
class arduino_Status(ModuleInstruction, Value):

    def __init__(self, status: bool, status: "arduino_Sensor" = None, Status: "arduino_Sensor" = None):
        self.status = status
        self.status = status
        self.Status = Status
        
    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, status: bool):
        self.__status = status

    @property
    def Status(self):
        return self.__Status

    @Status.setter
    def Status(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Status__Status", None)
        self.__Status = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensor"):
                opp_val = getattr(old_value, "sensor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensor"):
                opp_val = getattr(value, "sensor", None)
                if opp_val is None:
                    setattr(value, "sensor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Status__status", None)
        self.__status = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sensor"):
                opp_val = getattr(old_value, "Sensor", None)
                if opp_val == self:
                    setattr(old_value, "Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sensor"):
                opp_val = getattr(value, "Sensor", None)
                setattr(value, "Sensor", self)

class NamedElement:

    pass
class arduino_Module(NamedElement):

    def __init__(self, kind: str, image: str, level: bool, library: str, arduino_Module: "arduino_Hardware" = None, arduino_Module35: "arduino_ModuleInstruction" = None, arduino_Module22: "arduino_Project" = None, arduino_Module42: "arduino_Connector" = None):
        self.kind = kind
        self.image = image
        self.level = level
        self.library = library
        self.arduino_Module = arduino_Module
        self.arduino_Module35 = arduino_Module35
        self.arduino_Module22 = arduino_Module22
        self.arduino_Module42 = arduino_Module42
        
    @property
    def level(self) -> bool:
        return self.__level

    @level.setter
    def level(self, level: bool):
        self.__level = level

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def library(self) -> str:
        return self.__library

    @library.setter
    def library(self, library: str):
        self.__library = library

    @property
    def arduino_Module22(self):
        return self.__arduino_Module22

    @arduino_Module22.setter
    def arduino_Module22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module22", None)
        self.__arduino_Module22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Project21"):
                opp_val = getattr(old_value, "arduino_Project21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Project21"):
                opp_val = getattr(value, "arduino_Project21", None)
                if opp_val is None:
                    setattr(value, "arduino_Project21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Module42(self):
        return self.__arduino_Module42

    @arduino_Module42.setter
    def arduino_Module42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module42", None)
        self.__arduino_Module42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Connector41"):
                opp_val = getattr(old_value, "arduino_Connector41", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Connector41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Connector41"):
                opp_val = getattr(value, "arduino_Connector41", None)
                setattr(value, "arduino_Connector41", self)

    @property
    def arduino_Module35(self):
        return self.__arduino_Module35

    @arduino_Module35.setter
    def arduino_Module35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module35", None)
        self.__arduino_Module35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_ModuleInstruction"):
                opp_val = getattr(old_value, "arduino_ModuleInstruction", None)
                if opp_val == self:
                    setattr(old_value, "arduino_ModuleInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_ModuleInstruction"):
                opp_val = getattr(value, "arduino_ModuleInstruction", None)
                setattr(value, "arduino_ModuleInstruction", self)

    @property
    def arduino_Module(self):
        return self.__arduino_Module

    @arduino_Module.setter
    def arduino_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module", None)
        self.__arduino_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Hardware2"):
                opp_val = getattr(old_value, "arduino_Hardware2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Hardware2"):
                opp_val = getattr(value, "arduino_Hardware2", None)
                if opp_val is None:
                    setattr(value, "arduino_Hardware2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduino_Platform(NamedElement):

    def __init__(self, image: str, arduino_Platform6: set["arduino_DigitalPin"] = None, arduino_Platform8: set["arduino_AnalogPin"] = None, arduino_Platform: "arduino_Hardware" = None, arduino_Platform25: "arduino_Project" = None):
        self.image = image
        self.arduino_Platform6 = arduino_Platform6 if arduino_Platform6 is not None else set()
        self.arduino_Platform8 = arduino_Platform8 if arduino_Platform8 is not None else set()
        self.arduino_Platform = arduino_Platform
        self.arduino_Platform25 = arduino_Platform25
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def arduino_Platform6(self):
        return self.__arduino_Platform6

    @arduino_Platform6.setter
    def arduino_Platform6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Platform__arduino_Platform6", None)
        self.__arduino_Platform6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_DigitalPin"):
                    opp_val = getattr(item, "arduino_DigitalPin", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_DigitalPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_DigitalPin"):
                    opp_val = getattr(item, "arduino_DigitalPin", None)
                    
                    setattr(item, "arduino_DigitalPin", self)
                    

    @property
    def arduino_Platform8(self):
        return self.__arduino_Platform8

    @arduino_Platform8.setter
    def arduino_Platform8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Platform__arduino_Platform8", None)
        self.__arduino_Platform8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_AnalogPin"):
                    opp_val = getattr(item, "arduino_AnalogPin", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_AnalogPin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_AnalogPin"):
                    opp_val = getattr(item, "arduino_AnalogPin", None)
                    
                    setattr(item, "arduino_AnalogPin", self)
                    

    @property
    def arduino_Platform25(self):
        return self.__arduino_Platform25

    @arduino_Platform25.setter
    def arduino_Platform25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Platform__arduino_Platform25", None)
        self.__arduino_Platform25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Project24"):
                opp_val = getattr(old_value, "arduino_Project24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Project24"):
                opp_val = getattr(value, "arduino_Project24", None)
                if opp_val is None:
                    setattr(value, "arduino_Project24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Platform(self):
        return self.__arduino_Platform

    @arduino_Platform.setter
    def arduino_Platform(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Platform__arduino_Platform", None)
        self.__arduino_Platform = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Hardware"):
                opp_val = getattr(old_value, "arduino_Hardware", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Hardware"):
                opp_val = getattr(value, "arduino_Hardware", None)
                if opp_val is None:
                    setattr(value, "arduino_Hardware", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduino_Hardware(NamedElement):

    pass
class arduino_Project:

    pass
class arduino_Function:

    def __init__(self, name: str, arduino_Function: "arduino_Sketch" = None, arduino_Function57: set["arduino_ParameterDefinition"] = None, arduino_Function59: set["arduino_Instruction"] = None, arduino_Function64: "arduino_FunctionCall" = None):
        self.name = name
        self.arduino_Function = arduino_Function
        self.arduino_Function57 = arduino_Function57 if arduino_Function57 is not None else set()
        self.arduino_Function59 = arduino_Function59 if arduino_Function59 is not None else set()
        self.arduino_Function64 = arduino_Function64
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Function(self):
        return self.__arduino_Function

    @arduino_Function.setter
    def arduino_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Function__arduino_Function", None)
        self.__arduino_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch14"):
                opp_val = getattr(old_value, "arduino_Sketch14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch14"):
                opp_val = getattr(value, "arduino_Sketch14", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Function59(self):
        return self.__arduino_Function59

    @arduino_Function59.setter
    def arduino_Function59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Function__arduino_Function59", None)
        self.__arduino_Function59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Instruction60"):
                    opp_val = getattr(item, "arduino_Instruction60", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Instruction60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Instruction60"):
                    opp_val = getattr(item, "arduino_Instruction60", None)
                    
                    setattr(item, "arduino_Instruction60", self)
                    

    @property
    def arduino_Function64(self):
        return self.__arduino_Function64

    @arduino_Function64.setter
    def arduino_Function64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Function__arduino_Function64", None)
        self.__arduino_Function64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_FunctionCall"):
                opp_val = getattr(old_value, "arduino_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "arduino_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_FunctionCall"):
                opp_val = getattr(value, "arduino_FunctionCall", None)
                setattr(value, "arduino_FunctionCall", self)

    @property
    def arduino_Function57(self):
        return self.__arduino_Function57

    @arduino_Function57.setter
    def arduino_Function57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Function__arduino_Function57", None)
        self.__arduino_Function57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_ParameterDefinition"):
                    opp_val = getattr(item, "arduino_ParameterDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_ParameterDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_ParameterDefinition"):
                    opp_val = getattr(item, "arduino_ParameterDefinition", None)
                    
                    setattr(item, "arduino_ParameterDefinition", self)
                    

class arduino_Instruction(ABC):

    pass
class Instruction:

    pass
class arduino_ParameterCall(Instruction):

    pass
class arduino_FunctionCall(Instruction):

    pass
class arduino_Utilities(Instruction, Parameter):

    pass
class arduino_Value(Instruction, Parameter):

    def __init__(self, value: str, arduino_Value: "arduino_Level" = None, arduino_Value46: "arduino_MathOperator" = None, arduino_Value49: "arduino_MathOperator" = None, arduino_Value53: "arduino_Set" = None):
        self.value = value
        self.arduino_Value = arduino_Value
        self.arduino_Value46 = arduino_Value46
        self.arduino_Value49 = arduino_Value49
        self.arduino_Value53 = arduino_Value53
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def arduino_Value(self):
        return self.__arduino_Value

    @arduino_Value.setter
    def arduino_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Value__arduino_Value", None)
        self.__arduino_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Level"):
                opp_val = getattr(old_value, "arduino_Level", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Level", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Level"):
                opp_val = getattr(value, "arduino_Level", None)
                setattr(value, "arduino_Level", self)

    @property
    def arduino_Value46(self):
        return self.__arduino_Value46

    @arduino_Value46.setter
    def arduino_Value46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Value__arduino_Value46", None)
        self.__arduino_Value46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_MathOperator"):
                opp_val = getattr(old_value, "arduino_MathOperator", None)
                if opp_val == self:
                    setattr(old_value, "arduino_MathOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_MathOperator"):
                opp_val = getattr(value, "arduino_MathOperator", None)
                setattr(value, "arduino_MathOperator", self)

    @property
    def arduino_Value53(self):
        return self.__arduino_Value53

    @arduino_Value53.setter
    def arduino_Value53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Value__arduino_Value53", None)
        self.__arduino_Value53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Set52"):
                opp_val = getattr(old_value, "arduino_Set52", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Set52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Set52"):
                opp_val = getattr(value, "arduino_Set52", None)
                setattr(value, "arduino_Set52", self)

    @property
    def arduino_Value49(self):
        return self.__arduino_Value49

    @arduino_Value49.setter
    def arduino_Value49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Value__arduino_Value49", None)
        self.__arduino_Value49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_MathOperator48"):
                opp_val = getattr(old_value, "arduino_MathOperator48", None)
                if opp_val == self:
                    setattr(old_value, "arduino_MathOperator48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_MathOperator48"):
                opp_val = getattr(value, "arduino_MathOperator48", None)
                setattr(value, "arduino_MathOperator48", self)

class arduino_MathOperator(Instruction, Value):

    def __init__(self, operator: str, arduino_MathOperator: "arduino_Value" = None, arduino_MathOperator48: "arduino_Value" = None):
        self.operator = operator
        self.arduino_MathOperator = arduino_MathOperator
        self.arduino_MathOperator48 = arduino_MathOperator48
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def arduino_MathOperator(self):
        return self.__arduino_MathOperator

    @arduino_MathOperator.setter
    def arduino_MathOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_MathOperator__arduino_MathOperator", None)
        self.__arduino_MathOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Value46"):
                opp_val = getattr(old_value, "arduino_Value46", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Value46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Value46"):
                opp_val = getattr(value, "arduino_Value46", None)
                setattr(value, "arduino_Value46", self)

    @property
    def arduino_MathOperator48(self):
        return self.__arduino_MathOperator48

    @arduino_MathOperator48.setter
    def arduino_MathOperator48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_MathOperator__arduino_MathOperator48", None)
        self.__arduino_MathOperator48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Value49"):
                opp_val = getattr(old_value, "arduino_Value49", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Value49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Value49"):
                opp_val = getattr(value, "arduino_Value49", None)
                setattr(value, "arduino_Value49", self)

class arduino_IO(Instruction):

    pass
class arduino_Set(Instruction):

    pass
class arduino_ModuleInstruction(Instruction, Parameter):

    pass
class arduino_Control(Instruction):

    pass
class arduino_Variable(Instruction, Value):

    def __init__(self, name: str, arduino_Variable: "arduino_Set" = None):
        self.name = name
        self.arduino_Variable = arduino_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Variable(self):
        return self.__arduino_Variable

    @arduino_Variable.setter
    def arduino_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Variable__arduino_Variable", None)
        self.__arduino_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Set"):
                opp_val = getattr(old_value, "arduino_Set", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Set", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Set"):
                opp_val = getattr(value, "arduino_Set", None)
                setattr(value, "arduino_Set", self)

class arduino_Sketch(Instruction, NamedElement):

    pass
class arduino_Pin(ABC):

    def __init__(self, id: int, arduino_Pin: "arduino_Connector" = None):
        self.id = id
        self.arduino_Pin = arduino_Pin
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def arduino_Pin(self):
        return self.__arduino_Pin

    @arduino_Pin.setter
    def arduino_Pin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Pin__arduino_Pin", None)
        self.__arduino_Pin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Connector39"):
                opp_val = getattr(old_value, "arduino_Connector39", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Connector39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Connector39"):
                opp_val = getattr(value, "arduino_Connector39", None)
                setattr(value, "arduino_Connector39", self)

class Pin:

    pass
class arduino_AnalogPin(Pin):

    pass
class arduino_DigitalPin(Pin):

    pass
class arduino_Connector:

    pass