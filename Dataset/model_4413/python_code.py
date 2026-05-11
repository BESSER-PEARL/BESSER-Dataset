from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryOperatorKind(Enum):
    sub = "sub"
    add = "add"
    mul = "mul"
    div = "div"
    min = "min"
    max = "max"
    mod = "mod"
    lt = "lt"
    le = "le"
    eq = "eq"
    ge = "ge"
    gt = "gt"
    neq = "neq"
class UnaryOperatorKind(Enum):
    minus = "minus"
    neg = "neg"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class arduino_BinaryExpression(Expression):

    def __init__(self, operator: str, arduino_BinaryExpression: "arduino_Expression" = None, arduino_BinaryExpression29: "arduino_Expression" = None):
        self.operator = operator
        self.arduino_BinaryExpression = arduino_BinaryExpression
        self.arduino_BinaryExpression29 = arduino_BinaryExpression29
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def arduino_BinaryExpression(self):
        return self.__arduino_BinaryExpression

    @arduino_BinaryExpression.setter
    def arduino_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_BinaryExpression__arduino_BinaryExpression", None)
        self.__arduino_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Expression27"):
                opp_val = getattr(old_value, "arduino_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Expression27"):
                opp_val = getattr(value, "arduino_Expression27", None)
                setattr(value, "arduino_Expression27", self)

    @property
    def arduino_BinaryExpression29(self):
        return self.__arduino_BinaryExpression29

    @arduino_BinaryExpression29.setter
    def arduino_BinaryExpression29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_BinaryExpression__arduino_BinaryExpression29", None)
        self.__arduino_BinaryExpression29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Expression30"):
                opp_val = getattr(old_value, "arduino_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Expression30"):
                opp_val = getattr(value, "arduino_Expression30", None)
                setattr(value, "arduino_Expression30", self)

class arduino_UnaryExpression(Expression):

    def __init__(self, operator: str, arduino_UnaryExpression: "arduino_Expression" = None):
        self.operator = operator
        self.arduino_UnaryExpression = arduino_UnaryExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def arduino_UnaryExpression(self):
        return self.__arduino_UnaryExpression

    @arduino_UnaryExpression.setter
    def arduino_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_UnaryExpression__arduino_UnaryExpression", None)
        self.__arduino_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Expression25"):
                opp_val = getattr(old_value, "arduino_Expression25", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Expression25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Expression25"):
                opp_val = getattr(value, "arduino_Expression25", None)
                setattr(value, "arduino_Expression25", self)

class arduino_Constant(Expression):

    def __init__(self, value: int, arduino_Constant: "arduino_WaitFor" = None):
        self.value = value
        self.arduino_Constant = arduino_Constant
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def arduino_Constant(self):
        return self.__arduino_Constant

    @arduino_Constant.setter
    def arduino_Constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Constant__arduino_Constant", None)
        self.__arduino_Constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_WaitFor23"):
                opp_val = getattr(old_value, "arduino_WaitFor23", None)
                if opp_val == self:
                    setattr(old_value, "arduino_WaitFor23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_WaitFor23"):
                opp_val = getattr(value, "arduino_WaitFor23", None)
                setattr(value, "arduino_WaitFor23", self)

class arduino_ModuleGet(Expression):

    pass
class arduino_Expression(ABC):

    pass
class Control:

    pass
class arduino_While(Control):

    pass
class arduino_If(Control):

    pass
class Instruction:

    pass
class arduino_Delay(Instruction):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class arduino_WaitFor(Instruction):

    pass
class arduino_Control(Instruction):

    pass
class ModuleSet:

    pass
class arduino_SetLed(ModuleSet):

    pass
class InputModule:

    pass
class arduino_ModuleSet(Instruction):

    pass
class arduino_PushButton(InputModule):

    pass
class OutputModule:

    pass
class arduino_Led(OutputModule):

    pass
class Module:

    pass
class arduino_InputModule(Module):

    pass
class arduino_OutputModule(Module):

    pass
class arduino_Instruction(ABC):

    pass
class arduino_Block:

    pass
class NamedElement:

    pass
class arduino_Sketch(NamedElement):

    pass
class arduino_Board(NamedElement):

    pass
class arduino_Module(NamedElement):

    pass
class arduino_Project(NamedElement):

    pass
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

