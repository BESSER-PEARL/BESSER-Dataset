from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class kmlogo_asm_LogoProgram:

    pass
class BinaryExp:

    pass
class kmlogo_asm_Mult(BinaryExp):

    pass
class kmlogo_asm_Lower(BinaryExp):

    pass
class kmlogo_asm_Minus(BinaryExp):

    pass
class kmlogo_asm_Div(BinaryExp):

    pass
class kmlogo_asm_Greater(BinaryExp):

    pass
class kmlogo_asm_Equals(BinaryExp):

    pass
class kmlogo_asm_Plus(BinaryExp):

    pass
class kmlogo_asm_Parameter:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ProcCall:

    pass
class Parameter:

    pass
class ProcDeclaration:

    pass
class Block:

    pass
class ControlStructure:

    pass
class kmlogo_asm_While(ControlStructure):

    pass
class kmlogo_asm_Repeat(ControlStructure):

    pass
class kmlogo_asm_If(ControlStructure):

    pass
class Instruction:

    pass
class kmlogo_asm_ProcDeclaration(Instruction):

    def __init__(self, name: str, kmlogo_asm_ProcDeclaration21: set["Instruction"] = None, kmlogo_asm_ProcDeclaration: set["Parameter"] = None, 18: set["ProcCall"] = None, Instruction37: "kmlogo_asm_LogoProgram", Instruction: "kmlogo_asm_ProcDeclaration", Instruction23: "kmlogo_asm_Block"):
        self.name = name
        self.kmlogo_asm_ProcDeclaration21 = kmlogo_asm_ProcDeclaration21 if kmlogo_asm_ProcDeclaration21 is not None else set()
        self.kmlogo_asm_ProcDeclaration = kmlogo_asm_ProcDeclaration if kmlogo_asm_ProcDeclaration is not None else set()
        self.18 = 18 if 18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmlogo_asm_ProcDeclaration(self):
        return self.__kmlogo_asm_ProcDeclaration

    @kmlogo_asm_ProcDeclaration.setter
    def kmlogo_asm_ProcDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmlogo_asm_ProcDeclaration__kmlogo_asm_ProcDeclaration", None)
        self.__kmlogo_asm_ProcDeclaration = value if value is not None else set()
        
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
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmlogo_asm_ProcDeclaration__18", None)
        self.__18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "19"):
                    opp_val = getattr(item, "19", None)
                    
                    if opp_val == self:
                        setattr(item, "19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "19"):
                    opp_val = getattr(item, "19", None)
                    
                    setattr(item, "19", self)
                    

    @property
    def kmlogo_asm_ProcDeclaration21(self):
        return self.__kmlogo_asm_ProcDeclaration21

    @kmlogo_asm_ProcDeclaration21.setter
    def kmlogo_asm_ProcDeclaration21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmlogo_asm_ProcDeclaration__kmlogo_asm_ProcDeclaration21", None)
        self.__kmlogo_asm_ProcDeclaration21 = value if value is not None else set()
        
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
                    

class kmlogo_asm_Block(Instruction):

    pass
class kmlogo_asm_ControlStructure(Instruction):

    pass
class kmlogo_asm_Expression(Instruction):

    pass
class kmlogo_asm_Primitive(Instruction):

    pass
class kmlogo_asm_Instruction(ABC):

    pass
class Expression:

    pass
class kmlogo_asm_Constant(Expression):

    def __init__(self, integerValue: str, Expression8: "kmlogo_asm_BinaryExp", Expression4: "kmlogo_asm_Left", Expression6: "kmlogo_asm_Right", Expression11: "kmlogo_asm_BinaryExp", Expression: "kmlogo_asm_Back", Expression2: "kmlogo_asm_Forward", Expression13: "kmlogo_asm_ProcCall", Expression29: "kmlogo_asm_ControlStructure"):
        self.integerValue = integerValue
        
    @property
    def integerValue(self) -> str:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: str):
        self.__integerValue = integerValue

class kmlogo_asm_BinaryExp(Expression):

    pass
class kmlogo_asm_ProcCall(Expression):

    pass
class kmlogo_asm_ParameterCall(Expression):

    pass
class Primitive:

    pass
class kmlogo_asm_PenUp(Primitive):

    pass
class kmlogo_asm_Clear(Primitive):

    pass
class kmlogo_asm_PenDown(Primitive):

    pass
class kmlogo_asm_Left(Primitive):

    pass
class kmlogo_asm_Right(Primitive):

    pass
class kmlogo_asm_Forward(Primitive):

    pass
class kmlogo_asm_Back(Primitive):

    pass