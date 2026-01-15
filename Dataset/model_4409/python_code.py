from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    blue = "blue"
    red = "red"
    white = "white"
class UnaryIntegerOperatorKind(Enum):
    minus = "minus"
    squareRoot = "squareRoot"
class BinaryBooleanOperatorKind(Enum):
    inf = "inf"
    sup = "sup"
    infOrEqual = "infOrEqual"
    supOrEqual = "supOrEqual"
    equal = "equal"
    and = "and"
    or = "or"
    Different = "Different"
class Time(Enum):
    MilliSecond = "MilliSecond"
    MicroSecond = "MicroSecond"
class ChangeType(Enum):
    RISING = "RISING"
    FALLING = "FALLING"
    CHANGE = "CHANGE"
class UnaryBooleanOperatorKind(Enum):
    not = "not"
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

class ArduinoModule:

    pass
class Board:

    pass
class arduino_ArduinoBoard(Board):

    pass
class UnaryExpression:

    pass
class Module:

    pass
class arduino_ArduinoModule(Module):

    pass
class ArduinoAnalogModule:

    pass
class arduino_MusicPlayer(ArduinoAnalogModule):

    pass
class arduino_AmbientLightSensor(ArduinoAnalogModule):

    pass
class arduino_BluetoothTransceiver(ArduinoAnalogModule):

    pass
class arduino_SoundSensor(ArduinoAnalogModule):

    pass
class arduino_RotationSensor(ArduinoAnalogModule):

    pass
class ArduinoDigitalModule:

    pass
class arduino_InfraRedSensor(ArduinoDigitalModule):

    pass
class arduino_ArduinoCommunicationModule(ArduinoDigitalModule):

    pass
class arduino_MicroServo(ArduinoDigitalModule):

    pass
class arduino_Fan(ArduinoDigitalModule):

    pass
class arduino_PushButton(ArduinoDigitalModule):

    pass
class arduino_Buzzer(ArduinoDigitalModule):

    pass
class arduino_LED(ArduinoDigitalModule):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class VariableRef:

    pass
class BooleanExpression:

    pass
class arduino_BooleanVariableRef(VariableRef, BooleanExpression):

    pass
class arduino_UnaryBooleanExpression(UnaryExpression, BooleanExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class IntegerExpression:

    pass
class arduino_UnaryIntegerExpression(IntegerExpression, UnaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class arduino_IntegerVariableRef(VariableRef, IntegerExpression):

    pass
class BinaryExpression:

    pass
class arduino_BinaryBooleanExpression(BinaryExpression, BooleanExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class arduino_BinaryIntegerExpression(BinaryExpression, IntegerExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class ModuleGet:

    pass
class arduino_IntegerModuleGet(ModuleGet, IntegerExpression):

    pass
class arduino_BooleanModuleGet(ModuleGet, BooleanExpression):

    pass
class Variable:

    pass
class arduino_BooleanVariable(Variable):

    def __init__(self, initialValue: bool, arduino_BooleanVariable: "arduino_BooleanVariableRef" = None):
        self.initialValue = initialValue
        self.arduino_BooleanVariable = arduino_BooleanVariable
        
    @property
    def initialValue(self) -> bool:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: bool):
        self.__initialValue = initialValue

    @property
    def arduino_BooleanVariable(self):
        return self.__arduino_BooleanVariable

    @arduino_BooleanVariable.setter
    def arduino_BooleanVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_BooleanVariable__arduino_BooleanVariable", None)
        self.__arduino_BooleanVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BooleanVariableRef"):
                opp_val = getattr(old_value, "arduino_BooleanVariableRef", None)
                if opp_val == self:
                    setattr(old_value, "arduino_BooleanVariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BooleanVariableRef"):
                opp_val = getattr(value, "arduino_BooleanVariableRef", None)
                setattr(value, "arduino_BooleanVariableRef", self)

class arduino_IntegerVariable(Variable):

    def __init__(self, initialValue: int, arduino_IntegerVariable: "arduino_IntegerVariableRef" = None):
        self.initialValue = initialValue
        self.arduino_IntegerVariable = arduino_IntegerVariable
        
    @property
    def initialValue(self) -> int:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: int):
        self.__initialValue = initialValue

    @property
    def arduino_IntegerVariable(self):
        return self.__arduino_IntegerVariable

    @arduino_IntegerVariable.setter
    def arduino_IntegerVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_IntegerVariable__arduino_IntegerVariable", None)
        self.__arduino_IntegerVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_IntegerVariableRef"):
                opp_val = getattr(old_value, "arduino_IntegerVariableRef", None)
                if opp_val == self:
                    setattr(old_value, "arduino_IntegerVariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_IntegerVariableRef"):
                opp_val = getattr(value, "arduino_IntegerVariableRef", None)
                setattr(value, "arduino_IntegerVariableRef", self)

class Constant:

    pass
class arduino_BooleanConstant(Constant, BooleanExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class arduino_IntegerConstant(Constant, IntegerExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Utilities:

    pass
class arduino_WaitFor(Utilities):

    def __init__(self, mode: str, arduino_WaitFor: "arduino_Pin" = None):
        self.mode = mode
        self.arduino_WaitFor = arduino_WaitFor
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def arduino_WaitFor(self):
        return self.__arduino_WaitFor

    @arduino_WaitFor.setter
    def arduino_WaitFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_WaitFor__arduino_WaitFor", None)
        self.__arduino_WaitFor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Pin"):
                opp_val = getattr(old_value, "arduino_Pin", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Pin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Pin"):
                opp_val = getattr(value, "arduino_Pin", None)
                setattr(value, "arduino_Pin", self)

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

class Instruction:

    pass
class arduino_Utilities(Instruction):

    pass
class arduino_VariableDeclaration(Instruction):

    pass
class arduino_Assignment(Instruction):

    pass
class arduino_Control(Instruction):

    pass
class arduino_ModuleInstruction(Instruction):

    pass
class Assignment:

    pass
class arduino_VariableAssignment(Instruction, Assignment):

    pass
class ModuleInstruction:

    pass
class arduino_ModuleAssignment(ModuleInstruction, Assignment):

    pass
class arduino_Instruction(ABC):

    pass
class arduino_Expression(ABC):

    pass
class Expression:

    pass
class arduino_BinaryExpression(Expression):

    pass
class arduino_BooleanExpression(Expression):

    pass
class arduino_VariableRef(Expression):

    pass
class arduino_Constant(Expression):

    pass
class arduino_IntegerExpression(Expression):

    pass
class arduino_UnaryExpression(Expression):

    pass
class arduino_ModuleGet(Expression):

    pass
class Control:

    pass
class arduino_If(Control):

    pass
class arduino_While(Control):

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

class arduino_Block:

    pass
class arduino_ArduinoAnalogModule(ArduinoModule):

    pass
class arduino_ArduinoDigitalModule(ArduinoModule):

    pass
class Pin:

    pass
class arduino_AnalogPin(Pin):

    pass
class arduino_DigitalPin(Pin):

    pass
class arduino_Project:

    pass
class NamedElement:

    pass
class arduino_Board(NamedElement):

    pass
class arduino_Variable(NamedElement):

    pass
class arduino_Sketch(NamedElement):

    pass
class arduino_Pin(NamedElement):

    pass
class arduino_Module(NamedElement):

    pass