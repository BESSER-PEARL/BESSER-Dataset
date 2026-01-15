from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class kmLogo_ASM_LogoProgram:

    pass
class BinaryExp:

    pass
class kmLogo_ASM_Greater(BinaryExp):

    pass
class kmLogo_ASM_Equals(BinaryExp):

    pass
class kmLogo_ASM_Lower(BinaryExp):

    pass
class kmLogo_ASM_Mult(BinaryExp):

    pass
class kmLogo_ASM_Div(BinaryExp):

    pass
class kmLogo_ASM_Minus(BinaryExp):

    pass
class kmLogo_ASM_Plus(BinaryExp):

    pass
class kmLogo_ASM_Parameter:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Block:

    pass
class ControlStructure:

    pass
class kmLogo_ASM_While(ControlStructure):

    pass
class kmLogo_ASM_Repeat(ControlStructure):

    pass
class kmLogo_ASM_If(ControlStructure):

    pass
class ProcCall:

    pass
class Parameter:

    pass
class ProcDeclaration:

    pass
class Expression:

    pass
class kmLogo_ASM_Constant(Expression):

    def __init__(self, integerValue: str, Expression4: "kmLogo_ASM_Left", Expression27: "kmLogo_ASM_ControlStructure", Expression2: "kmLogo_ASM_Forward", Expression6: "kmLogo_ASM_Right", Expression8: "kmLogo_ASM_BinaryExp", Expression13: "kmLogo_ASM_ProcCall", Expression11: "kmLogo_ASM_BinaryExp", Expression: "kmLogo_ASM_Back"):
        self.integerValue = integerValue
        
    @property
    def integerValue(self) -> str:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: str):
        self.__integerValue = integerValue

class kmLogo_ASM_BinaryExp(Expression):

    pass
class kmLogo_ASM_ParameterCall(Expression):

    pass
class kmLogo_ASM_ProcCall(Expression):

    pass
class Primitive:

    pass
class kmLogo_ASM_Clear(Primitive):

    pass
class kmLogo_ASM_Forward(Primitive):

    pass
class kmLogo_ASM_Left(Primitive):

    pass
class kmLogo_ASM_Right(Primitive):

    pass
class kmLogo_ASM_PenDown(Primitive):

    pass
class kmLogo_ASM_Back(Primitive):

    pass
class Instruction:

    pass
class kmLogo_ASM_Expression(Instruction):

    pass
class kmLogo_ASM_ControlStructure(Instruction):

    pass
class kmLogo_ASM_Block(Instruction):

    pass
class kmLogo_ASM_ProcDeclaration(Instruction):

    def __init__(self, name: str, kmLogo_ASM_ProcDeclaration: set["Parameter"] = None, ProcCall: set["ProcCall"] = None, kmLogo_ASM_ProcDeclaration19: set["Instruction"] = None, Instruction35: "kmLogo_ASM_LogoProgram", Instruction: "kmLogo_ASM_ProcDeclaration", Instruction21: "kmLogo_ASM_Block"):
        self.name = name
        self.kmLogo_ASM_ProcDeclaration = kmLogo_ASM_ProcDeclaration if kmLogo_ASM_ProcDeclaration is not None else set()
        self.ProcCall = ProcCall if ProcCall is not None else set()
        self.kmLogo_ASM_ProcDeclaration19 = kmLogo_ASM_ProcDeclaration19 if kmLogo_ASM_ProcDeclaration19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_ASM_ProcDeclaration(self):
        return self.__kmLogo_ASM_ProcDeclaration

    @kmLogo_ASM_ProcDeclaration.setter
    def kmLogo_ASM_ProcDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ASM_ProcDeclaration__kmLogo_ASM_ProcDeclaration", None)
        self.__kmLogo_ASM_ProcDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def kmLogo_ASM_ProcDeclaration19(self):
        return self.__kmLogo_ASM_ProcDeclaration19

    @kmLogo_ASM_ProcDeclaration19.setter
    def kmLogo_ASM_ProcDeclaration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ASM_ProcDeclaration__kmLogo_ASM_ProcDeclaration19", None)
        self.__kmLogo_ASM_ProcDeclaration19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Instruction"):
                    opp_val = getattr(item, "Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Instruction"):
                    opp_val = getattr(item, "Instruction", None)
                    
                    setattr(item, "Instruction", self)
                    

    @property
    def ProcCall(self):
        return self.__ProcCall

    @ProcCall.setter
    def ProcCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ASM_ProcDeclaration__ProcCall", None)
        self.__ProcCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ASM17"):
                    opp_val = getattr(item, "ASM17", None)
                    
                    if opp_val == self:
                        setattr(item, "ASM17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ASM17"):
                    opp_val = getattr(item, "ASM17", None)
                    
                    setattr(item, "ASM17", self)
                    

class kmLogo_ASM_Primitive(Instruction):

    pass
class kmLogo_ASM_Instruction(ABC):

    pass
class kmLogo_ASM_PenUp(Primitive):

    pass