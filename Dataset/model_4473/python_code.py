from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class kmlogo_asm_LogoProgram:

    pass
class ProcCall:

    pass
class Parameter:

    pass
class BinaryExp:

    pass
class kmlogo_asm_Lower(BinaryExp):

    pass
class kmlogo_asm_Greater(BinaryExp):

    pass
class kmlogo_asm_Minus(BinaryExp):

    pass
class kmlogo_asm_Mult(BinaryExp):

    pass
class kmlogo_asm_Div(BinaryExp):

    pass
class kmlogo_asm_Equals(BinaryExp):

    pass
class kmlogo_asm_Plus(BinaryExp):

    pass
class kmlogo_asm_Parameter:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
class ProcDeclaration:

    pass
class Expression:

    pass
class kmlogo_asm_Constant(Expression):

    def __init__(self, integerValue: str, Expression11: "kmlogo_asm_BinaryExp" = None, Expression4: "kmlogo_asm_Left" = None, Expression8: "kmlogo_asm_BinaryExp" = None, Expression6: "kmlogo_asm_Right" = None, Expression26: "kmlogo_asm_ControlStructure" = None, Expression: "kmlogo_asm_Back" = None, Expression2: "kmlogo_asm_Forward" = None, Expression13: "kmlogo_asm_ProcCall" = None):
        self.integerValue = integerValue
        
        pass
    @property
    def integerValue(self):
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: str):
        self.__integerValue = integerValue


class kmlogo_asm_BinaryExp(Expression):

    pass
class kmlogo_asm_ParameterCall(Expression):

    pass
class kmlogo_asm_ProcCall(Expression):

    pass
class Primitive:

    pass
class kmlogo_asm_Forward(Primitive):

    pass
class kmlogo_asm_Left(Primitive):

    pass
class kmlogo_asm_PenDown(Primitive):

    pass
class kmlogo_asm_Right(Primitive):

    pass
class kmlogo_asm_Clear(Primitive):

    pass
class kmlogo_asm_PenUp(Primitive):

    pass
class kmlogo_asm_Back(Primitive):

    pass
class Instruction:

    pass
class kmlogo_asm_Block(Instruction):

    pass
class kmlogo_asm_ControlStructure(Instruction):

    pass
class kmlogo_asm_ProcDeclaration(Instruction):

    def __init__(self, name: str, kmlogo_asm_ProcDeclaration: set["Parameter"] = None, declaration: set["ProcCall"] = None, kmlogo_asm_ProcDeclaration18: set["Instruction"] = None, Instruction: "kmlogo_asm_ProcDeclaration" = None, Instruction20: "kmlogo_asm_Block" = None, Instruction34: "kmlogo_asm_LogoProgram" = None):
        self.name = name
        self.kmlogo_asm_ProcDeclaration = kmlogo_asm_ProcDeclaration if kmlogo_asm_ProcDeclaration is not None else set()
        self.declaration = declaration if declaration is not None else set()
        self.kmlogo_asm_ProcDeclaration18 = kmlogo_asm_ProcDeclaration18 if kmlogo_asm_ProcDeclaration18 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def declaration(self):
        return self.__declaration

    @declaration.setter
    def declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmlogo_asm_ProcDeclaration__declaration", None)
        self.__declaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProcCall"):
                    opp_val = getattr(item, "ProcCall", None)
                    
                    if opp_val == self:
                        setattr(item, "ProcCall", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProcCall"):
                    opp_val = getattr(item, "ProcCall", None)
                    
                    setattr(item, "ProcCall", self)
                    

    @property
    def kmlogo_asm_ProcDeclaration18(self):
        return self.__kmlogo_asm_ProcDeclaration18

    @kmlogo_asm_ProcDeclaration18.setter
    def kmlogo_asm_ProcDeclaration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmlogo_asm_ProcDeclaration__kmlogo_asm_ProcDeclaration18", None)
        self.__kmlogo_asm_ProcDeclaration18 = value if value is not None else set()
        
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
                    

class kmlogo_asm_Expression(Instruction):

    pass
class kmlogo_asm_Primitive(Instruction):

    pass
class kmlogo_asm_Instruction(ABC):

    pass