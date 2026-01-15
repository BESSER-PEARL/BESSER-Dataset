from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Value:

    pass
class PrtInstruction:

    pass
class mil_ErrInstruction(PrtInstruction):

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

class mil_Value(ABC):

    pass
class Instruction:

    pass
class mil_NeqInstruction(Instruction):

    pass
class mil_EqInstruction(Instruction):

    pass
class mil_NegInstruction(Instruction):

    pass
class mil_SubInstruction(Instruction):

    pass
class mil_MulInstruction(Instruction):

    pass
class mil_StoreInstruction(Instruction):

    pass
class mil_LtInstruction(Instruction):

    pass
class mil_DivInstruction(Instruction):

    pass
class mil_AddInstruction(Instruction):

    pass
class mil_LoadInstruction(Instruction):

    pass
class mil_ConstantInteger(Value):

    def __init__(self, rawValue: int, mil_ConstantInteger: "mil_InpInstruction" = None, mil_ConstantInteger7: "mil_InpInstruction" = None):
        self.rawValue = rawValue
        self.mil_ConstantInteger = mil_ConstantInteger
        self.mil_ConstantInteger7 = mil_ConstantInteger7
        
    @property
    def rawValue(self) -> int:
        return self.__rawValue

    @rawValue.setter
    def rawValue(self, rawValue: int):
        self.__rawValue = rawValue

    @property
    def mil_ConstantInteger(self):
        return self.__mil_ConstantInteger

    @mil_ConstantInteger.setter
    def mil_ConstantInteger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mil_ConstantInteger__mil_ConstantInteger", None)
        self.__mil_ConstantInteger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mil_InpInstruction"):
                opp_val = getattr(old_value, "mil_InpInstruction", None)
                if opp_val == self:
                    setattr(old_value, "mil_InpInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mil_InpInstruction"):
                opp_val = getattr(value, "mil_InpInstruction", None)
                setattr(value, "mil_InpInstruction", self)

    @property
    def mil_ConstantInteger7(self):
        return self.__mil_ConstantInteger7

    @mil_ConstantInteger7.setter
    def mil_ConstantInteger7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mil_ConstantInteger__mil_ConstantInteger7", None)
        self.__mil_ConstantInteger7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mil_InpInstruction6"):
                opp_val = getattr(old_value, "mil_InpInstruction6", None)
                if opp_val == self:
                    setattr(old_value, "mil_InpInstruction6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mil_InpInstruction6"):
                opp_val = getattr(value, "mil_InpInstruction6", None)
                setattr(value, "mil_InpInstruction6", self)

class mil_InpInstruction(Instruction):

    pass
class mil_PrtInstruction(Instruction):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mil_YldInstruction(Instruction):

    pass
class mil_RetInstruction(Instruction):

    pass
class JumpInstruction:

    pass
class mil_JpcInstruction(JumpInstruction):

    pass
class mil_CalInstruction(JumpInstruction):

    pass
class mil_JmpInstruction(JumpInstruction):

    pass
class mil_LabelInstruction(Instruction):

    def __init__(self, name: str, mil_LabelInstruction: "mil_JumpInstruction" = None):
        self.name = name
        self.mil_LabelInstruction = mil_LabelInstruction
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class mil_JumpInstruction(Instruction):

    pass
class mil_GeqInstruction(Instruction):

    pass
class mil_GtInstruction(Instruction):

    pass
class mil_LeqInstruction(Instruction):

    pass
class mil_Instruction(ABC):

    pass
class mil_MILModel:

    pass