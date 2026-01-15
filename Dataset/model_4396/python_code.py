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

class ModuleSet:

    pass
class arduino_SetLed(ModuleSet):

    def __init__(self, arduino_SetLed: "arduino_Led" = None):
        self.arduino_SetLed = arduino_SetLed
        
    @property
    def arduino_SetLed(self):
        return self.__arduino_SetLed

    @arduino_SetLed.setter
    def arduino_SetLed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_SetLed__arduino_SetLed", None)
        self.__arduino_SetLed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Led"):
                opp_val = getattr(old_value, "arduino_Led", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Led", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Led"):
                opp_val = getattr(value, "arduino_Led", None)
                setattr(value, "arduino_Led", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class Expression:

    pass
class arduino_UnaryExpression(Expression):

    def __init__(self, operator: str, arduino_UnaryExpression: "arduino_Expression" = None):
        self.operator = operator
        self.arduino_UnaryExpression = arduino_UnaryExpression
        
    @property
    def operator(self) -> str:
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

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class arduino_BinaryExpression(Expression):

    def __init__(self, operator: str, arduino_BinaryExpression: "arduino_Expression" = None, arduino_BinaryExpression29: "arduino_Expression" = None):
        self.operator = operator
        self.arduino_BinaryExpression = arduino_BinaryExpression
        self.arduino_BinaryExpression29 = arduino_BinaryExpression29
        
    @property
    def operator(self) -> str:
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

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class arduino_ModuleGet(Expression):

    def __init__(self, arduino_ModuleGet: "arduino_Module" = None):
        self.arduino_ModuleGet = arduino_ModuleGet
        
    @property
    def arduino_ModuleGet(self):
        return self.__arduino_ModuleGet

    @arduino_ModuleGet.setter
    def arduino_ModuleGet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_ModuleGet__arduino_ModuleGet", None)
        self.__arduino_ModuleGet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Module32"):
                opp_val = getattr(old_value, "arduino_Module32", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Module32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Module32"):
                opp_val = getattr(value, "arduino_Module32", None)
                setattr(value, "arduino_Module32", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class arduino_Constant(Expression):

    def __init__(self, value: str, arduino_Constant: "arduino_WaitFor" = None):
        self.value = value
        self.arduino_Constant = arduino_Constant
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
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

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class arduino_Expression(ABC):

    def __init__(self, arduino_Expression: "arduino_If" = None, arduino_Expression25: "arduino_UnaryExpression" = None, arduino_Expression27: "arduino_BinaryExpression" = None, arduino_Expression16: "arduino_While" = None, arduino_Expression30: "arduino_BinaryExpression" = None, arduino_Expression18: "arduino_ModuleSet" = None):
        self.arduino_Expression = arduino_Expression
        self.arduino_Expression25 = arduino_Expression25
        self.arduino_Expression27 = arduino_Expression27
        self.arduino_Expression16 = arduino_Expression16
        self.arduino_Expression30 = arduino_Expression30
        self.arduino_Expression18 = arduino_Expression18
        
    @property
    def arduino_Expression18(self):
        return self.__arduino_Expression18

    @arduino_Expression18.setter
    def arduino_Expression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression18", None)
        self.__arduino_Expression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_ModuleSet"):
                opp_val = getattr(old_value, "arduino_ModuleSet", None)
                if opp_val == self:
                    setattr(old_value, "arduino_ModuleSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_ModuleSet"):
                opp_val = getattr(value, "arduino_ModuleSet", None)
                setattr(value, "arduino_ModuleSet", self)

    @property
    def arduino_Expression27(self):
        return self.__arduino_Expression27

    @arduino_Expression27.setter
    def arduino_Expression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression27", None)
        self.__arduino_Expression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BinaryExpression"):
                opp_val = getattr(old_value, "arduino_BinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "arduino_BinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BinaryExpression"):
                opp_val = getattr(value, "arduino_BinaryExpression", None)
                setattr(value, "arduino_BinaryExpression", self)

    @property
    def arduino_Expression16(self):
        return self.__arduino_Expression16

    @arduino_Expression16.setter
    def arduino_Expression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression16", None)
        self.__arduino_Expression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_While"):
                opp_val = getattr(old_value, "arduino_While", None)
                if opp_val == self:
                    setattr(old_value, "arduino_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_While"):
                opp_val = getattr(value, "arduino_While", None)
                setattr(value, "arduino_While", self)

    @property
    def arduino_Expression30(self):
        return self.__arduino_Expression30

    @arduino_Expression30.setter
    def arduino_Expression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression30", None)
        self.__arduino_Expression30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_BinaryExpression29"):
                opp_val = getattr(old_value, "arduino_BinaryExpression29", None)
                if opp_val == self:
                    setattr(old_value, "arduino_BinaryExpression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_BinaryExpression29"):
                opp_val = getattr(value, "arduino_BinaryExpression29", None)
                setattr(value, "arduino_BinaryExpression29", self)

    @property
    def arduino_Expression25(self):
        return self.__arduino_Expression25

    @arduino_Expression25.setter
    def arduino_Expression25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression25", None)
        self.__arduino_Expression25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_UnaryExpression"):
                opp_val = getattr(old_value, "arduino_UnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "arduino_UnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_UnaryExpression"):
                opp_val = getattr(value, "arduino_UnaryExpression", None)
                setattr(value, "arduino_UnaryExpression", self)

    @property
    def arduino_Expression(self):
        return self.__arduino_Expression

    @arduino_Expression.setter
    def arduino_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Expression__arduino_Expression", None)
        self.__arduino_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_If"):
                opp_val = getattr(old_value, "arduino_If", None)
                if opp_val == self:
                    setattr(old_value, "arduino_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_If"):
                opp_val = getattr(value, "arduino_If", None)
                setattr(value, "arduino_If", self)

    def evaluate(self):
        # TODO: Implement evaluate method
        pass

class Control:

    pass
class arduino_While(Control):

    def __init__(self, arduino_While: "arduino_Expression" = None):
        self.arduino_While = arduino_While
        
    @property
    def arduino_While(self):
        return self.__arduino_While

    @arduino_While.setter
    def arduino_While(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_While__arduino_While", None)
        self.__arduino_While = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Expression16"):
                opp_val = getattr(old_value, "arduino_Expression16", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Expression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Expression16"):
                opp_val = getattr(value, "arduino_Expression16", None)
                setattr(value, "arduino_Expression16", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_If(Control):

    def __init__(self, arduino_If: "arduino_Expression" = None, arduino_If13: "arduino_Block" = None):
        self.arduino_If = arduino_If
        self.arduino_If13 = arduino_If13
        
    @property
    def arduino_If13(self):
        return self.__arduino_If13

    @arduino_If13.setter
    def arduino_If13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_If__arduino_If13", None)
        self.__arduino_If13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Block14"):
                opp_val = getattr(old_value, "arduino_Block14", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Block14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Block14"):
                opp_val = getattr(value, "arduino_Block14", None)
                setattr(value, "arduino_Block14", self)

    @property
    def arduino_If(self):
        return self.__arduino_If

    @arduino_If.setter
    def arduino_If(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_If__arduino_If", None)
        self.__arduino_If = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Expression"):
                opp_val = getattr(old_value, "arduino_Expression", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Expression"):
                opp_val = getattr(value, "arduino_Expression", None)
                setattr(value, "arduino_Expression", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class Instruction:

    pass
class arduino_ModuleSet(Instruction):

    def __init__(self, arduino_ModuleSet: "arduino_Expression" = None):
        self.arduino_ModuleSet = arduino_ModuleSet
        
    @property
    def arduino_ModuleSet(self):
        return self.__arduino_ModuleSet

    @arduino_ModuleSet.setter
    def arduino_ModuleSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_ModuleSet__arduino_ModuleSet", None)
        self.__arduino_ModuleSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Expression18"):
                opp_val = getattr(old_value, "arduino_Expression18", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Expression18"):
                opp_val = getattr(value, "arduino_Expression18", None)
                setattr(value, "arduino_Expression18", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Delay(Instruction):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_WaitFor(Instruction):

    def __init__(self, arduino_WaitFor: "arduino_Module" = None, arduino_WaitFor23: "arduino_Constant" = None):
        self.arduino_WaitFor = arduino_WaitFor
        self.arduino_WaitFor23 = arduino_WaitFor23
        
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
            if hasattr(old_value, "arduino_Module21"):
                opp_val = getattr(old_value, "arduino_Module21", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Module21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Module21"):
                opp_val = getattr(value, "arduino_Module21", None)
                setattr(value, "arduino_Module21", self)

    @property
    def arduino_WaitFor23(self):
        return self.__arduino_WaitFor23

    @arduino_WaitFor23.setter
    def arduino_WaitFor23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_WaitFor__arduino_WaitFor23", None)
        self.__arduino_WaitFor23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Constant"):
                opp_val = getattr(old_value, "arduino_Constant", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Constant"):
                opp_val = getattr(value, "arduino_Constant", None)
                setattr(value, "arduino_Constant", self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def setActivated(self):
        # TODO: Implement setActivated method
        pass

class arduino_Control(Instruction):

    def __init__(self, arduino_Control: "arduino_Block" = None):
        self.arduino_Control = arduino_Control
        
    @property
    def arduino_Control(self):
        return self.__arduino_Control

    @arduino_Control.setter
    def arduino_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Control__arduino_Control", None)
        self.__arduino_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Block10"):
                opp_val = getattr(old_value, "arduino_Block10", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Block10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Block10"):
                opp_val = getattr(value, "arduino_Block10", None)
                setattr(value, "arduino_Block10", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Instruction(ABC):

    def __init__(self, arduino_Instruction: "arduino_Block" = None):
        self.arduino_Instruction = arduino_Instruction
        
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
            if hasattr(old_value, "arduino_Block8"):
                opp_val = getattr(old_value, "arduino_Block8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Block8"):
                opp_val = getattr(value, "arduino_Block8", None)
                if opp_val is None:
                    setattr(value, "arduino_Block8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def finalize(self):
        # TODO: Implement finalize method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Block:

    def __init__(self, arduino_Block: "arduino_Sketch" = None, arduino_Block8: set["arduino_Instruction"] = None, arduino_Block10: "arduino_Control" = None, arduino_Block14: "arduino_If" = None):
        self.arduino_Block = arduino_Block
        self.arduino_Block8 = arduino_Block8 if arduino_Block8 is not None else set()
        self.arduino_Block10 = arduino_Block10
        self.arduino_Block14 = arduino_Block14
        
    @property
    def arduino_Block10(self):
        return self.__arduino_Block10

    @arduino_Block10.setter
    def arduino_Block10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Block__arduino_Block10", None)
        self.__arduino_Block10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Control"):
                opp_val = getattr(old_value, "arduino_Control", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Control", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Control"):
                opp_val = getattr(value, "arduino_Control", None)
                setattr(value, "arduino_Control", self)

    @property
    def arduino_Block(self):
        return self.__arduino_Block

    @arduino_Block.setter
    def arduino_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Block__arduino_Block", None)
        self.__arduino_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch6"):
                opp_val = getattr(old_value, "arduino_Sketch6", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sketch6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch6"):
                opp_val = getattr(value, "arduino_Sketch6", None)
                setattr(value, "arduino_Sketch6", self)

    @property
    def arduino_Block8(self):
        return self.__arduino_Block8

    @arduino_Block8.setter
    def arduino_Block8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Block__arduino_Block8", None)
        self.__arduino_Block8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Instruction"):
                    opp_val = getattr(item, "arduino_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Instruction"):
                    opp_val = getattr(item, "arduino_Instruction", None)
                    
                    setattr(item, "arduino_Instruction", self)
                    

    @property
    def arduino_Block14(self):
        return self.__arduino_Block14

    @arduino_Block14.setter
    def arduino_Block14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Block__arduino_Block14", None)
        self.__arduino_Block14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_If13"):
                opp_val = getattr(old_value, "arduino_If13", None)
                if opp_val == self:
                    setattr(old_value, "arduino_If13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_If13"):
                opp_val = getattr(value, "arduino_If13", None)
                setattr(value, "arduino_If13", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class InputModule:

    pass
class arduino_PushButton(InputModule):

    def __init__(self):
        
    def press(self):
        # TODO: Implement press method
        pass

    def release(self):
        # TODO: Implement release method
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
class NamedElement:

    pass
class arduino_Module(NamedElement):

    def __init__(self, level: str, arduino_Module: "arduino_Board" = None, arduino_Module21: "arduino_WaitFor" = None, arduino_Module32: "arduino_ModuleGet" = None):
        self.level = level
        self.arduino_Module = arduino_Module
        self.arduino_Module21 = arduino_Module21
        self.arduino_Module32 = arduino_Module32
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def arduino_Module21(self):
        return self.__arduino_Module21

    @arduino_Module21.setter
    def arduino_Module21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module21", None)
        self.__arduino_Module21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_WaitFor"):
                opp_val = getattr(old_value, "arduino_WaitFor", None)
                if opp_val == self:
                    setattr(old_value, "arduino_WaitFor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_WaitFor"):
                opp_val = getattr(value, "arduino_WaitFor", None)
                setattr(value, "arduino_WaitFor", self)

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
            if hasattr(old_value, "arduino_Board4"):
                opp_val = getattr(old_value, "arduino_Board4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Board4"):
                opp_val = getattr(value, "arduino_Board4", None)
                if opp_val is None:
                    setattr(value, "arduino_Board4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Module32(self):
        return self.__arduino_Module32

    @arduino_Module32.setter
    def arduino_Module32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Module__arduino_Module32", None)
        self.__arduino_Module32 = value
        
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

class arduino_Sketch(NamedElement):

    def __init__(self, arduino_Sketch: "arduino_Project" = None, arduino_Sketch6: "arduino_Block" = None):
        self.arduino_Sketch = arduino_Sketch
        self.arduino_Sketch6 = arduino_Sketch6
        
    @property
    def arduino_Sketch(self):
        return self.__arduino_Sketch

    @arduino_Sketch.setter
    def arduino_Sketch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch", None)
        self.__arduino_Sketch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Project2"):
                opp_val = getattr(old_value, "arduino_Project2", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Project2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Project2"):
                opp_val = getattr(value, "arduino_Project2", None)
                setattr(value, "arduino_Project2", self)

    @property
    def arduino_Sketch6(self):
        return self.__arduino_Sketch6

    @arduino_Sketch6.setter
    def arduino_Sketch6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch6", None)
        self.__arduino_Sketch6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Block"):
                opp_val = getattr(old_value, "arduino_Block", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Block"):
                opp_val = getattr(value, "arduino_Block", None)
                setattr(value, "arduino_Block", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class arduino_Board(NamedElement):

    pass
class arduino_Project(NamedElement):

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
