from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class kmLogo_ASM_LogoProgram:

    pass
class UnaryExpression:

    pass
class kmLogo_ASM_Tan(UnaryExpression):

    pass
class kmLogo_ASM_Sin(UnaryExpression):

    pass
class kmLogo_ASM_Cos(UnaryExpression):

    pass
class ControlStructure:

    pass
class kmLogo_ASM_If(ControlStructure):

    pass
class ProcCall:

    pass
class Parameter:

    pass
class BinaryExp:

    pass
class kmLogo_ASM_Greater(BinaryExp):

    pass
class kmLogo_ASM_Equals(BinaryExp):

    pass
class kmLogo_ASM_Div(BinaryExp):

    pass
class kmLogo_ASM_Lower(BinaryExp):

    pass
class kmLogo_ASM_Minus(BinaryExp):

    pass
class kmLogo_ASM_Mult(BinaryExp):

    pass
class kmLogo_ASM_Plus(BinaryExp):

    pass
class kmLogo_ASM_Parameter:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class kmLogo_ASM_While(ControlStructure):

    pass
class kmLogo_ASM_Repeat(ControlStructure):

    pass
class Block:

    pass
class ProcDeclaration:

    pass
class Expression:

    pass
class kmLogo_ASM_BinaryExp(Expression):

    pass
class kmLogo_ASM_ParameterCall(Expression):

    pass
class kmLogo_ASM_Constant(Expression):

    def __init__(self, value: float, Expression8: "kmLogo_ASM_BinaryExp" = None, Expression6: "kmLogo_ASM_Right" = None, Expression28: "kmLogo_ASM_ControlStructure" = None, Expression13: "kmLogo_ASM_UnaryExpression" = None, Expression15: "kmLogo_ASM_ProcCall" = None, Expression2: "kmLogo_ASM_Forward" = None, Expression: "kmLogo_ASM_Back" = None, Expression11: "kmLogo_ASM_BinaryExp" = None, Expression4: "kmLogo_ASM_Left" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class kmLogo_ASM_UnaryExpression(Expression):

    pass
class kmLogo_ASM_ProcCall(Expression):

    pass
class Primitive:

    pass
class kmLogo_ASM_Forward(Primitive):

    pass
class kmLogo_ASM_PenDown(Primitive):

    pass
class kmLogo_ASM_Right(Primitive):

    pass
class kmLogo_ASM_PenUp(Primitive):

    pass
class kmLogo_ASM_Left(Primitive):

    pass
class kmLogo_ASM_Clear(Primitive):

    pass
class kmLogo_ASM_Back(Primitive):

    pass
class Instruction:

    pass
class kmLogo_ASM_ControlStructure(Instruction):

    pass
class kmLogo_ASM_ProcDeclaration(Instruction):

    def __init__(self, name: str, kmLogo_ASM_ProcDeclaration: set["Parameter"] = None, declaration: set["ProcCall"] = None, kmLogo_ASM_ProcDeclaration20: set["Instruction"] = None, Instruction36: "kmLogo_ASM_LogoProgram" = None, Instruction22: "kmLogo_ASM_Block" = None, Instruction: "kmLogo_ASM_ProcDeclaration" = None):
        self.name = name
        self.kmLogo_ASM_ProcDeclaration = kmLogo_ASM_ProcDeclaration if kmLogo_ASM_ProcDeclaration is not None else set()
        self.declaration = declaration if declaration is not None else set()
        self.kmLogo_ASM_ProcDeclaration20 = kmLogo_ASM_ProcDeclaration20 if kmLogo_ASM_ProcDeclaration20 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kmLogo_ASM_ProcDeclaration20(self):
        return self.__kmLogo_ASM_ProcDeclaration20

    @kmLogo_ASM_ProcDeclaration20.setter
    def kmLogo_ASM_ProcDeclaration20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ASM_ProcDeclaration__kmLogo_ASM_ProcDeclaration20", None)
        self.__kmLogo_ASM_ProcDeclaration20 = value if value is not None else set()
        
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
    def declaration(self):
        return self.__declaration

    @declaration.setter
    def declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ASM_ProcDeclaration__declaration", None)
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
                    

class kmLogo_ASM_Expression(Instruction):

    pass
class kmLogo_ASM_Block(Instruction):

    pass
class kmLogo_ASM_Primitive(Instruction):

    pass
class kmLogo_ASM_Instruction(ABC):

    pass