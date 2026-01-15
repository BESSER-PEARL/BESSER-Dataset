from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
class kmLogo_ASM_Repeat(ControlStructure):

    pass
class kmLogo_ASM_While(ControlStructure):

    pass
class kmLogo_ASM_If(ControlStructure):

    pass
class kmLogo_ASM_LogoProgram:

    pass
class UnaryExpression:

    pass
class kmLogo_ASM_Sin(UnaryExpression):

    pass
class kmLogo_ASM_Tan(UnaryExpression):

    pass
class kmLogo_ASM_Cos(UnaryExpression):

    pass
class BinaryExp:

    pass
class kmLogo_ASM_Div(BinaryExp):

    pass
class kmLogo_ASM_Mult(BinaryExp):

    pass
class kmLogo_ASM_Equals(BinaryExp):

    pass
class kmLogo_ASM_Greater(BinaryExp):

    pass
class kmLogo_ASM_Lower(BinaryExp):

    pass
class kmLogo_ASM_Minus(BinaryExp):

    pass
class kmLogo_ASM_Plus(BinaryExp):

    pass
class ProcCall:

    pass
class Parameter:

    pass
class ProcDeclaration:

    pass
class Expression:

    pass
class kmLogo_ASM_BinaryExp(Expression):

    pass
class kmLogo_ASM_UnaryExpression(Expression):

    pass
class kmLogo_ASM_Constant(Expression):

    def __init__(self, value: float, Expression13: "kmLogo_ASM_UnaryExpression", Expression15: "kmLogo_ASM_ProcCall", Expression29: "kmLogo_ASM_ControlStructure", Expression2: "kmLogo_ASM_Forward", Expression4: "kmLogo_ASM_Left", Expression8: "kmLogo_ASM_BinaryExp", Expression6: "kmLogo_ASM_Right", Expression: "kmLogo_ASM_Back", Expression11: "kmLogo_ASM_BinaryExp"):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class kmLogo_ASM_ParameterCall(Expression):

    pass
class kmLogo_ASM_ProcCall(Expression):

    pass
class Primitive:

    pass
class kmLogo_ASM_Right(Primitive):

    pass
class kmLogo_ASM_Clear(Primitive):

    pass
class kmLogo_ASM_Forward(Primitive):

    pass
class kmLogo_ASM_Left(Primitive):

    pass
class kmLogo_ASM_PenDown(Primitive):

    pass
class kmLogo_ASM_PenUp(Primitive):

    pass
class kmLogo_ASM_Back(Primitive):

    pass
class Instruction:

    pass
class kmLogo_ASM_Expression(Instruction):

    pass
class kmLogo_ASM_ProcDeclaration(Instruction):

    def __init__(self, name: str, kmLogo_ASM_ProcDeclaration: set["Parameter"] = None, ProcCall: set["ProcCall"] = None, kmLogo_ASM_ProcDeclaration21: set["Instruction"] = None, Instruction23: "kmLogo_ASM_Block", Instruction: "kmLogo_ASM_ProcDeclaration", Instruction37: "kmLogo_ASM_LogoProgram"):
        self.name = name
        self.kmLogo_ASM_ProcDeclaration = kmLogo_ASM_ProcDeclaration if kmLogo_ASM_ProcDeclaration is not None else set()
        self.ProcCall = ProcCall if ProcCall is not None else set()
        self.kmLogo_ASM_ProcDeclaration21 = kmLogo_ASM_ProcDeclaration21 if kmLogo_ASM_ProcDeclaration21 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_ASM_ProcDeclaration21(self):
        return self.__kmLogo_ASM_ProcDeclaration21

    @kmLogo_ASM_ProcDeclaration21.setter
    def kmLogo_ASM_ProcDeclaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ASM_ProcDeclaration__kmLogo_ASM_ProcDeclaration21", None)
        self.__kmLogo_ASM_ProcDeclaration21 = value if value is not None else set()
        
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
                if hasattr(item, "ASM19"):
                    opp_val = getattr(item, "ASM19", None)
                    
                    if opp_val == self:
                        setattr(item, "ASM19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ASM19"):
                    opp_val = getattr(item, "ASM19", None)
                    
                    setattr(item, "ASM19", self)
                    

class kmLogo_ASM_Block(Instruction):

    pass
class kmLogo_ASM_ControlStructure(Instruction):

    pass
class kmLogo_ASM_Primitive(Instruction):

    pass
class kmLogo_ASM_Instruction(ABC):

    pass