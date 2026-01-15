from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Comparison:

    pass
class mil_NotEqualsComparison(Comparison):

    pass
class mil_EqualsComparison(Comparison):

    pass
class Jumper:

    pass
class mil_Jumper(ABC):

    pass
class mil_GreaterEqualsComparison(Comparison):

    pass
class mil_GreaterThanComparison(Comparison):

    pass
class mil_LowerEqualsComparison(Comparison):

    pass
class mil_LowerThanComparison(Comparison):

    pass
class mil_Statement(ABC):

    pass
class mil_MILModel:

    pass
class Value:

    pass
class mil_ConstantInteger(Value):

    def __init__(self, rawValue: int):
        self.rawValue = rawValue
        
    @property
    def rawValue(self) -> int:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: int):
        self.__rawValue = rawValue

class BinaryOperation:

    pass
class mil_SubInstruction(BinaryOperation):

    pass
class mil_Comparison(BinaryOperation):

    pass
class mil_MultInstruction(BinaryOperation):

    pass
class mil_DivInstruction(BinaryOperation):

    pass
class mil_AddInstruction(BinaryOperation):

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

class UnaryOperation:

    pass
class mil_NegateInstruction(UnaryOperation):

    pass
class mil_ConditionalJumpInstruction(Jumper, UnaryOperation):

    pass
class mil_YieldInstruction(UnaryOperation):

    pass
class mil_StoreInstruction(UnaryOperation):

    pass
class mil_Value(ABC):

    pass
class Instruction:

    pass
class mil_JumpInstruction(Jumper, Instruction):

    pass
class mil_CallInstruction(Jumper, Instruction):

    pass
class mil_UnaryOperation(Instruction):

    pass
class mil_ReturnInstruction(Instruction):

    pass
class mil_PrintInstruction(Instruction):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class mil_BinaryOperation(Instruction):

    pass
class mil_LoadInstruction(Instruction):

    pass
class Statement:

    pass
class mil_JumpMarker(Statement):

    def __init__(self, name: str, mil_JumpMarker: "mil_Jumper" = None):
        self.name = name
        self.mil_JumpMarker = mil_JumpMarker
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mil_JumpMarker(self):
        return self.__mil_JumpMarker

    @mil_JumpMarker.setter
    def mil_JumpMarker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mil_JumpMarker__mil_JumpMarker", None)
        self.__mil_JumpMarker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mil_Jumper"):
                opp_val = getattr(old_value, "mil_Jumper", None)
                if opp_val == self:
                    setattr(old_value, "mil_Jumper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mil_Jumper"):
                opp_val = getattr(value, "mil_Jumper", None)
                setattr(value, "mil_Jumper", self)

class mil_Instruction(Statement):

    pass