from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PrimitivesProv_Instruction(ABC):

    def __init__(self, PrimitivesProv_Instruction: "PrimitivesProv_LogoProgram" = None):
        self.PrimitivesProv_Instruction = PrimitivesProv_Instruction
        
    @property
    def PrimitivesProv_Instruction(self):
        return self.__PrimitivesProv_Instruction

    @PrimitivesProv_Instruction.setter
    def PrimitivesProv_Instruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrimitivesProv_Instruction__PrimitivesProv_Instruction", None)
        self.__PrimitivesProv_Instruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrimitivesProv_LogoProgram"):
                opp_val = getattr(old_value, "PrimitivesProv_LogoProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrimitivesProv_LogoProgram"):
                opp_val = getattr(value, "PrimitivesProv_LogoProgram", None)
                if opp_val is None:
                    setattr(value, "PrimitivesProv_LogoProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def evalInstruction(self, context: str):
        # TODO: Implement evalInstruction method
        pass

class PrimitivesProv_LogoProgram:

    pass
class Primitive:

    pass
class PrimitivesProv_Left(Primitive):

    pass
class PrimitivesProv_Right(Primitive):

    pass
class PrimitivesProv_Back(Primitive):

    pass
class PrimitivesProv_Forward(Primitive):

    pass
class Instruction:

    pass
class PrimitivesProv_Primitive(Instruction):

    pass