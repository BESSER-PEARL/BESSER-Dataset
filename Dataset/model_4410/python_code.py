from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Library(Enum):
    none = "none"
    servo = "servo"
    music = "music"
class UnaryBooleanOperatorKind(Enum):
    not = "not"
class Time(Enum):
    MilliSecond = "MilliSecond"
    MicroSecond = "MicroSecond"
class BinaryBooleanOperatorKind(Enum):
    inf = "inf"
    sup = "sup"
    infOrEqual = "infOrEqual"
    supOrEqual = "supOrEqual"
    equal = "equal"
    and = "and"
    or = "or"
    Different = "Different"
class ModuleKind(Enum):
    digital = "digital"
    analog = "analog"
class UnaryIntegerOperatorKind(Enum):
    minus = "minus"
    squareRoot = "squareRoot"
class BinaryIntegerOperatorKind(Enum):
    minus = "minus"
    plus = "plus"
    mul = "mul"
    div = "div"
    min = "min"
    max = "max"
    pourcent = "pourcent"


############################################
# Definition of Classes
############################################

class InstantaneousInstruction:

    pass
class arduino_Synchro(InstantaneousInstruction):

    pass
class ModuleGet:

    pass
class Variable:

    pass
class UnaryExpression:

    pass
class IntegerExpression:

    pass
class arduino_UnaryIntegerExpression(UnaryExpression, IntegerExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class arduino_IntegerModuleGet(ModuleGet, IntegerExpression):

    pass
class arduino_IntegerVariable(Variable, IntegerExpression):

    def __init__(self, initialValue: int):
        self.initialValue = initialValue
        
    @property
    def initialValue(self) -> int:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: int):
        self.__initialValue = initialValue

class BinaryExpression:

    pass
class arduino_BinaryIntegerExpression(IntegerExpression, BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class arduino_Expression(ABC):

    pass
class Constant:

    pass
class arduino_IntegerConstant(Constant, IntegerExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class BooleanExpression:

    pass
class arduino_BooleanConstant(BooleanExpression, Constant):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class arduino_UnaryBooleanExpression(UnaryExpression, BooleanExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class arduino_BooleanModuleGet(ModuleGet, BooleanExpression):

    pass
class arduino_BinaryBooleanExpression(BooleanExpression, BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class arduino_BooleanVariable(Variable, BooleanExpression):

    def __init__(self, initialValue: bool):
        self.initialValue = initialValue
        
    @property
    def initialValue(self) -> bool:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: bool):
        self.__initialValue = initialValue

class Module:

    pass
class arduino_Sensor(Module):

    pass
class Utilities:

    pass
class arduino_Delay(Utilities):

    def __init__(self, unit: str, value: int):
        self.unit = unit
        self.value = value
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Assignment:

    pass
class ModuleInstruction:

    pass
class arduino_ModuleAssignment(ModuleInstruction, Assignment):

    pass
class Expression:

    pass
class arduino_BooleanExpression(Expression):

    pass
class arduino_UnaryExpression(Expression):

    pass
class arduino_IntegerExpression(Expression):

    pass
class arduino_VariableRef(Expression):

    pass
class arduino_BinaryExpression(Expression):

    pass
class arduino_Constant(Expression):

    pass
class arduino_ModuleGet(Expression):

    pass
class Control:

    pass
class arduino_While(Control):

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

class arduino_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class arduino_Actuator(Module):

    pass
class arduino_Pin(ABC):

    def __init__(self, id: int, level: int, arduino_Pin: "arduino_Connector" = None):
        self.id = id
        self.level = level
        self.arduino_Pin = arduino_Pin
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

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
            if hasattr(old_value, "arduino_Connector38"):
                opp_val = getattr(old_value, "arduino_Connector38", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Connector38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Connector38"):
                opp_val = getattr(value, "arduino_Connector38", None)
                setattr(value, "arduino_Connector38", self)

class Pin:

    pass
class arduino_AnalogPin(Pin):

    pass
class arduino_DigitalPin(Pin):

    pass
class arduino_Connector:

    pass
class arduino_Project:

    pass
class Instruction:

    pass
class arduino_VariableAssignment(Assignment, Instruction):

    pass
class arduino_Utilities(Instruction):

    pass
class arduino_InstantaneousInstruction(Instruction):

    pass
class arduino_ModuleInstruction(Instruction):

    pass
class arduino_Control(Instruction):

    def __init__(self, arduino_Control: set["arduino_Instruction"] = None):
        self.arduino_Control = arduino_Control if arduino_Control is not None else set()
        
    @property
    def arduino_Control(self):
        return self.__arduino_Control

    @arduino_Control.setter
    def arduino_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Control__arduino_Control", None)
        self.__arduino_Control = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Instruction36"):
                    opp_val = getattr(item, "arduino_Instruction36", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Instruction36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Instruction36"):
                    opp_val = getattr(item, "arduino_Instruction36", None)
                    
                    setattr(item, "arduino_Instruction36", self)
                    

    def evaluate(self) -> bool:
        # TODO: Implement evaluate method
        pass

class arduino_Assignment(Instruction):

    pass
class arduino_VariableDeclaration(Instruction):

    pass
class NamedElement:

    pass
class arduino_Sketch(NamedElement, Instruction):

    pass
class arduino_Module(NamedElement):

    def __init__(self, kind: str, image: str, level: bool, library: str, arduino_Module17: "arduino_Project" = None, arduino_Module: "arduino_Hardware" = None, arduino_Module41: "arduino_Connector" = None, arduino_Module43: "arduino_ModuleGet" = None, arduino_Module34: "arduino_ModuleInstruction" = None):
        self.kind = kind
        self.image = image
        self.level = level
        self.library = library
        self.arduino_Module17 = arduino_Module17
        self.arduino_Module = arduino_Module
        self.arduino_Module41 = arduino_Module41
        self.arduino_Module43 = arduino_Module43
        self.arduino_Module34 = arduino_Module34
        
    @property
    def library(self) -> str:
        return self.__library

    @library.setter
    def library(self, library: str):
        self.__library = library

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
    def arduino_Module43(self):
        return self.__arduino_Module43

    @arduino_Module43.setter
    def arduino_Module43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module43", None)
        self.__arduino_Module43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_ModuleGet"):
                opp_val = getattr(old_value, "arduino_ModuleGet", None)
                if opp_val == self:
                    setattr(old_value, "arduino_ModuleGet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_ModuleGet"):
                opp_val = getattr(value, "arduino_ModuleGet", None)
                setattr(value, "arduino_ModuleGet", self)

    @property
    def arduino_Module34(self):
        return self.__arduino_Module34

    @arduino_Module34.setter
    def arduino_Module34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module34", None)
        self.__arduino_Module34 = value
        
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
    def arduino_Module17(self):
        return self.__arduino_Module17

    @arduino_Module17.setter
    def arduino_Module17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module17", None)
        self.__arduino_Module17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Project16"):
                opp_val = getattr(old_value, "arduino_Project16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Project16"):
                opp_val = getattr(value, "arduino_Project16", None)
                if opp_val is None:
                    setattr(value, "arduino_Project16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    @property
    def arduino_Module41(self):
        return self.__arduino_Module41

    @arduino_Module41.setter
    def arduino_Module41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module41", None)
        self.__arduino_Module41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Connector40"):
                opp_val = getattr(old_value, "arduino_Connector40", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Connector40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Connector40"):
                opp_val = getattr(value, "arduino_Connector40", None)
                setattr(value, "arduino_Connector40", self)

class arduino_Platform(NamedElement):

    def __init__(self, image: str, arduino_Platform20: "arduino_Project" = None, arduino_Platform: "arduino_Hardware" = None, arduino_Platform6: set["arduino_DigitalPin"] = None, arduino_Platform8: set["arduino_AnalogPin"] = None):
        self.image = image
        self.arduino_Platform20 = arduino_Platform20
        self.arduino_Platform = arduino_Platform
        self.arduino_Platform6 = arduino_Platform6 if arduino_Platform6 is not None else set()
        self.arduino_Platform8 = arduino_Platform8 if arduino_Platform8 is not None else set()
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

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
    def arduino_Platform20(self):
        return self.__arduino_Platform20

    @arduino_Platform20.setter
    def arduino_Platform20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Platform__arduino_Platform20", None)
        self.__arduino_Platform20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Project19"):
                opp_val = getattr(old_value, "arduino_Project19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Project19"):
                opp_val = getattr(value, "arduino_Project19", None)
                if opp_val is None:
                    setattr(value, "arduino_Project19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class arduino_Variable(NamedElement, Expression):

    pass
class arduino_Instruction(NamedElement):

    def __init__(self, arduino_Instruction: "arduino_Sketch" = None, arduino_Instruction26: "arduino_Instruction" = None, arduino_Instruction24: "arduino_Instruction" = None, arduino_Instruction29: "arduino_Instruction" = None, arduino_Instruction27: "arduino_Instruction" = None, arduino_Instruction32: "arduino_Instruction" = None, arduino_Instruction30: "arduino_Instruction" = None, arduino_Instruction36: "arduino_Control" = None):
        self.arduino_Instruction = arduino_Instruction
        self.arduino_Instruction26 = arduino_Instruction26
        self.arduino_Instruction24 = arduino_Instruction24
        self.arduino_Instruction29 = arduino_Instruction29
        self.arduino_Instruction27 = arduino_Instruction27
        self.arduino_Instruction32 = arduino_Instruction32
        self.arduino_Instruction30 = arduino_Instruction30
        self.arduino_Instruction36 = arduino_Instruction36
        
    @property
    def arduino_Instruction(self):
        return self.__arduino_Instruction

    @arduino_Instruction.setter
    def arduino_Instruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction", None)
        self.__arduino_Instruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch12"):
                opp_val = getattr(old_value, "arduino_Sketch12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch12"):
                opp_val = getattr(value, "arduino_Sketch12", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Instruction32(self):
        return self.__arduino_Instruction32

    @arduino_Instruction32.setter
    def arduino_Instruction32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction32", None)
        self.__arduino_Instruction32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Instruction30"):
                opp_val = getattr(old_value, "arduino_Instruction30", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Instruction30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Instruction30"):
                opp_val = getattr(value, "arduino_Instruction30", None)
                setattr(value, "arduino_Instruction30", self)

    @property
    def arduino_Instruction24(self):
        return self.__arduino_Instruction24

    @arduino_Instruction24.setter
    def arduino_Instruction24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction24", None)
        self.__arduino_Instruction24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Instruction26"):
                opp_val = getattr(old_value, "arduino_Instruction26", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Instruction26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Instruction26"):
                opp_val = getattr(value, "arduino_Instruction26", None)
                setattr(value, "arduino_Instruction26", self)

    @property
    def arduino_Instruction26(self):
        return self.__arduino_Instruction26

    @arduino_Instruction26.setter
    def arduino_Instruction26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction26", None)
        self.__arduino_Instruction26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Instruction24"):
                opp_val = getattr(old_value, "arduino_Instruction24", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Instruction24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Instruction24"):
                opp_val = getattr(value, "arduino_Instruction24", None)
                setattr(value, "arduino_Instruction24", self)

    @property
    def arduino_Instruction29(self):
        return self.__arduino_Instruction29

    @arduino_Instruction29.setter
    def arduino_Instruction29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction29", None)
        self.__arduino_Instruction29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Instruction27"):
                opp_val = getattr(old_value, "arduino_Instruction27", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Instruction27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Instruction27"):
                opp_val = getattr(value, "arduino_Instruction27", None)
                setattr(value, "arduino_Instruction27", self)

    @property
    def arduino_Instruction27(self):
        return self.__arduino_Instruction27

    @arduino_Instruction27.setter
    def arduino_Instruction27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction27", None)
        self.__arduino_Instruction27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Instruction29"):
                opp_val = getattr(old_value, "arduino_Instruction29", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Instruction29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Instruction29"):
                opp_val = getattr(value, "arduino_Instruction29", None)
                setattr(value, "arduino_Instruction29", self)

    @property
    def arduino_Instruction30(self):
        return self.__arduino_Instruction30

    @arduino_Instruction30.setter
    def arduino_Instruction30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction30", None)
        self.__arduino_Instruction30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Instruction32"):
                opp_val = getattr(old_value, "arduino_Instruction32", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Instruction32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Instruction32"):
                opp_val = getattr(value, "arduino_Instruction32", None)
                setattr(value, "arduino_Instruction32", self)

    @property
    def arduino_Instruction36(self):
        return self.__arduino_Instruction36

    @arduino_Instruction36.setter
    def arduino_Instruction36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Instruction__arduino_Instruction36", None)
        self.__arduino_Instruction36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Control"):
                opp_val = getattr(old_value, "arduino_Control", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Control"):
                opp_val = getattr(value, "arduino_Control", None)
                if opp_val is None:
                    setattr(value, "arduino_Control", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def finalize(self):
        # TODO: Implement finalize method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Hardware(NamedElement):

    pass