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
class UnaryBooleanOperatorKind(Enum):
    not_ = "not_"
class Time(Enum):
    MilliSecond = "MilliSecond"
    MicroSecond = "MicroSecond"
class BinaryIntegerOperatorKind(Enum):
    plus = "plus"
    mul = "mul"
    div = "div"
    minus = "minus"
    min = "min"
    max = "max"
    pourcent = "pourcent"
class UnaryIntegerOperatorKind(Enum):
    minus = "minus"
    squareRoot = "squareRoot"
class BinaryBooleanOperatorKind(Enum):
    Different = "Different"
    inf = "inf"
    sup = "sup"
    infOrEqual = "infOrEqual"
    supOrEqual = "supOrEqual"
    equal = "equal"
    and_ = "and_"
    or_ = "or_"


############################################
# Definition of Classes
############################################

class ArduinoCommunicationModule:

    pass
class arduino_BluetoothTransceiver(ArduinoCommunicationModule):

    pass
class ArduinoModule:

    pass
class Board:

    pass
class arduino_ArduinoBoard(Board):

    pass
class Module:

    pass
class arduino_ArduinoModule(Module):

    pass
class ArduinoAnalogModule:

    pass
class arduino_ArduinoCommunicationModule(ArduinoAnalogModule):

    pass
class arduino_AmbientLightSensor(ArduinoAnalogModule):

    pass
class arduino_MusicPlayer(ArduinoAnalogModule):

    pass
class arduino_RotationSensor(ArduinoAnalogModule):

    pass
class ArduinoDigitalModule:

    pass
class arduino_MicroServo(ArduinoDigitalModule):

    pass
class arduino_InfraRedSensor(ArduinoDigitalModule):

    pass
class arduino_PushButton(ArduinoDigitalModule):

    pass
class arduino_Fan(ArduinoDigitalModule):

    pass
class arduino_Buzzer(ArduinoDigitalModule):

    pass
class arduino_LED(ArduinoDigitalModule):

    def __init__(self, color: str):
        self.color = color
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


class VariableRef:

    pass
class arduino_SoundSensor(ArduinoAnalogModule):

    pass
class UnaryExpression:

    pass
class ModuleGet:

    pass
class Variable:

    pass
class arduino_BooleanVariable(Variable):

    def __init__(self, initialValue: bool, arduino_BooleanVariable: "arduino_BooleanVariableRef" = None):
        self.initialValue = initialValue
        self.arduino_BooleanVariable = arduino_BooleanVariable
        
        pass
    @property
    def initialValue(self):
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

class Constant:

    pass
class arduino_IntegerVariable(Variable):

    def __init__(self, initialValue: int, arduino_IntegerVariable: "arduino_IntegerVariableRef" = None):
        self.initialValue = initialValue
        self.arduino_IntegerVariable = arduino_IntegerVariable
        
        pass
    @property
    def initialValue(self):
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

class BooleanExpression:

    pass
class arduino_UnaryBooleanExpression(BooleanExpression, UnaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class arduino_BooleanConstant(BooleanExpression, Constant):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class arduino_BooleanModuleGet(BooleanExpression, ModuleGet):

    pass
class arduino_BooleanVariableRef(BooleanExpression, VariableRef):

    pass
class IntegerExpression:

    pass
class arduino_UnaryIntegerExpression(IntegerExpression, UnaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class arduino_IntegerModuleGet(IntegerExpression, ModuleGet):

    pass
class arduino_IntegerConstant(IntegerExpression, Constant):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class arduino_IntegerVariableRef(IntegerExpression, VariableRef):

    pass
class BinaryExpression:

    pass
class arduino_BinaryBooleanExpression(BooleanExpression, BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class arduino_BinaryIntegerExpression(IntegerExpression, BinaryExpression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class arduino_Expression(ABC):

    pass
class Expression:

    pass
class arduino_VariableRef(Expression):

    pass
class arduino_BooleanExpression(Expression):

    pass
class arduino_UnaryExpression(Expression):

    pass
class arduino_BinaryExpression(Expression):

    pass
class arduino_IntegerExpression(Expression):

    pass
class arduino_Constant(Expression):

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
        
        pass
    @property
    def iteration(self):
        return self.__iteration

    @iteration.setter
    def iteration(self, iteration: int):
        self.__iteration = iteration


class arduino_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Utilities:

    pass
class arduino_Delay(Utilities):

    def __init__(self, unit: str, value: int):
        self.unit = unit
        self.value = value
        
        pass
    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class Instruction:

    pass
class arduino_Control(Instruction):

    pass
class arduino_VariableDeclaration(Instruction):

    pass
class arduino_Assignment(Instruction):

    pass
class arduino_Utilities(Instruction):

    pass
class arduino_ModuleInstruction(Instruction):

    pass
class arduino_Instruction(ABC):

    pass
class arduino_Block:

    pass
class Assignment:

    pass
class arduino_VariableAssignment(Assignment, Instruction):

    pass
class ModuleInstruction:

    pass
class arduino_ModuleGet(Expression, ModuleInstruction):

    pass
class arduino_ModuleAssignment(Assignment, ModuleInstruction):

    pass
class arduino_ArduinoDigitalModule(ArduinoModule):

    pass
class Pin:

    pass
class arduino_DigitalPin(Pin):

    pass
class arduino_Project:

    pass
class NamedElement:

    pass
class arduino_Pin(NamedElement):

    pass
class arduino_Module(NamedElement):

    pass
class arduino_Sketch(NamedElement):

    pass
class arduino_Variable(NamedElement):

    pass
class arduino_Board(NamedElement):

    pass
class arduino_ArduinoAnalogModule(ArduinoModule):

    pass
class arduino_AnalogPin(Pin):

    pass