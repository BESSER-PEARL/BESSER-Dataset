from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ArithmeticInstruction:

    pass
class mil_SubInstruction(ArithmeticInstruction):

    pass
class mil_DivInstruction(ArithmeticInstruction):

    pass
class mil_MulInstruction(ArithmeticInstruction):

    pass
class mil_AddInstruction(ArithmeticInstruction):

    pass
class OutputInstruction:

    pass
class mil_PrintInstruction(OutputInstruction):

    def __init__(self, output: str):
        self.output = output
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

class mil_YieldInstruciton(OutputInstruction):

    pass
class CompareInstruction:

    pass
class mil_GreaterThanEqualInstruction(CompareInstruction):

    pass
class mil_LessThanEqualInstruction(CompareInstruction):

    pass
class mil_LessThanInstruction(CompareInstruction):

    pass
class mil_NotEqualInstruction(CompareInstruction):

    pass
class mil_GreaterThanInstruction(CompareInstruction):

    pass
class mil_EqualInstruction(CompareInstruction):

    pass
class JumpInstruction:

    pass
class mil_ConditionalJumpInstruction(JumpInstruction):

    pass
class mil_UnconditionalJumpInstruction(JumpInstruction):

    pass
class Value:

    pass
class mil_RegisterReference(Value):

    def __init__(self, address: str, mil_RegisterReference: "mil_StoreInstruction" = None):
        self.address = address
        self.mil_RegisterReference = mil_RegisterReference
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def mil_RegisterReference(self):
        return self.__mil_RegisterReference

    @mil_RegisterReference.setter
    def mil_RegisterReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mil_RegisterReference__mil_RegisterReference", None)
        self.__mil_RegisterReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mil_StoreInstruction"):
                opp_val = getattr(old_value, "mil_StoreInstruction", None)
                if opp_val == self:
                    setattr(old_value, "mil_StoreInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mil_StoreInstruction"):
                opp_val = getattr(value, "mil_StoreInstruction", None)
                setattr(value, "mil_StoreInstruction", self)

class mil_ConstantInteger(Value):

    def __init__(self, rawValue: int):
        self.rawValue = rawValue
        
    @property
    def rawValue(self) -> int:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: int):
        self.__rawValue = rawValue

class mil_Instruction(ABC):

    pass
class mil_MILModel:

    pass
class mil_Value(ABC):

    pass
class Instruction:

    pass
class mil_StoreInstruction(Instruction):

    pass
class mil_ArithmeticInstruction(Instruction):

    pass
class mil_CallInstruction(Instruction):

    pass
class mil_NegateInstruction(Instruction):

    pass
class mil_JumpInstruction(Instruction):

    pass
class mil_ReturnInstruction(Instruction):

    pass
class mil_LoadInstruction(Instruction):

    pass
class mil_CompareInstruction(Instruction):

    pass
class mil_OutputInstruction(Instruction):

    pass
class mil_LabelInstruction(Instruction):

    def __init__(self, name: str, mil_LabelInstruction: "mil_JumpInstruction" = None, mil_LabelInstruction5: "mil_CallInstruction" = None):
        self.name = name
        self.mil_LabelInstruction = mil_LabelInstruction
        self.mil_LabelInstruction5 = mil_LabelInstruction5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mil_LabelInstruction5(self):
        return self.__mil_LabelInstruction5

    @mil_LabelInstruction5.setter
    def mil_LabelInstruction5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mil_LabelInstruction__mil_LabelInstruction5", None)
        self.__mil_LabelInstruction5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mil_CallInstruction"):
                opp_val = getattr(old_value, "mil_CallInstruction", None)
                if opp_val == self:
                    setattr(old_value, "mil_CallInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mil_CallInstruction"):
                opp_val = getattr(value, "mil_CallInstruction", None)
                setattr(value, "mil_CallInstruction", self)

    @property
    def mil_LabelInstruction(self):
        return self.__mil_LabelInstruction

    @mil_LabelInstruction.setter
    def mil_LabelInstruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mil_LabelInstruction__mil_LabelInstruction", None)
        self.__mil_LabelInstruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mil_JumpInstruction"):
                opp_val = getattr(old_value, "mil_JumpInstruction", None)
                if opp_val == self:
                    setattr(old_value, "mil_JumpInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mil_JumpInstruction"):
                opp_val = getattr(value, "mil_JumpInstruction", None)
                setattr(value, "mil_JumpInstruction", self)
