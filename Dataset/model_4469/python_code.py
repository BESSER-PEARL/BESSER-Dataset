from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BinaryExp:

    pass
class kmLogo_Minus(BinaryExp):

    pass
class kmLogo_Div(BinaryExp):

    pass
class kmLogo_Lower(BinaryExp):

    pass
class kmLogo_Greater(BinaryExp):

    pass
class kmLogo_Equals(BinaryExp):

    pass
class kmLogo_Mult(BinaryExp):

    pass
class kmLogo_Plus(BinaryExp):

    pass
class ControlStructure:

    pass
class kmLogo_While(ControlStructure):

    pass
class kmLogo_Repeat(ControlStructure):

    pass
class kmLogo_If(ControlStructure):

    pass
class kmLogo_Parameter:

    def __init__(self, name: str, kmLogo_Parameter: "kmLogo_ProcDeclaration" = None, kmLogo_Parameter38: "kmLogo_ParameterCall" = None):
        self.name = name
        self.kmLogo_Parameter = kmLogo_Parameter
        self.kmLogo_Parameter38 = kmLogo_Parameter38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_Parameter38(self):
        return self.__kmLogo_Parameter38

    @kmLogo_Parameter38.setter
    def kmLogo_Parameter38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Parameter__kmLogo_Parameter38", None)
        self.__kmLogo_Parameter38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_ParameterCall"):
                opp_val = getattr(old_value, "kmLogo_ParameterCall", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_ParameterCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_ParameterCall"):
                opp_val = getattr(value, "kmLogo_ParameterCall", None)
                setattr(value, "kmLogo_ParameterCall", self)

    @property
    def kmLogo_Parameter(self):
        return self.__kmLogo_Parameter

    @kmLogo_Parameter.setter
    def kmLogo_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Parameter__kmLogo_Parameter", None)
        self.__kmLogo_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_ProcDeclaration"):
                opp_val = getattr(old_value, "kmLogo_ProcDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_ProcDeclaration"):
                opp_val = getattr(value, "kmLogo_ProcDeclaration", None)
                if opp_val is None:
                    setattr(value, "kmLogo_ProcDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Expression:

    pass
class kmLogo_ProcCall(Expression):

    pass
class kmLogo_ParameterCall(Expression):

    pass
class kmLogo_Constant(Expression):

    def __init__(self, integerValue: int):
        self.integerValue = integerValue
        
    @property
    def integerValue(self) -> int:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: int):
        self.__integerValue = integerValue

class kmLogo_BinaryExp(Expression):

    pass
class Primitive:

    pass
class kmLogo_PenDown(Primitive):

    pass
class kmLogo_PenUp(Primitive):

    pass
class kmLogo_Right(Primitive):

    pass
class kmLogo_Clear(Primitive):

    pass
class kmLogo_Back(Primitive):

    pass
class Instruction:

    pass
class kmLogo_Expression(Instruction):

    pass
class kmLogo_ControlStructure(Instruction):

    pass
class kmLogo_Block(Instruction):

    pass
class kmLogo_ProcDeclaration(Instruction):

    def __init__(self, name: str, kmLogo_ProcDeclaration22: set["kmLogo_Instruction"] = None, 16: "kmLogo_ProcCall" = None, kmLogo_ProcDeclaration: set["kmLogo_Parameter"] = None, 19: set["kmLogo_ProcCall"] = None):
        self.name = name
        self.kmLogo_ProcDeclaration22 = kmLogo_ProcDeclaration22 if kmLogo_ProcDeclaration22 is not None else set()
        self.16 = 16
        self.kmLogo_ProcDeclaration = kmLogo_ProcDeclaration if kmLogo_ProcDeclaration is not None else set()
        self.19 = 19 if 19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__16", None)
        self.__16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def kmLogo_ProcDeclaration22(self):
        return self.__kmLogo_ProcDeclaration22

    @kmLogo_ProcDeclaration22.setter
    def kmLogo_ProcDeclaration22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__kmLogo_ProcDeclaration22", None)
        self.__kmLogo_ProcDeclaration22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_Instruction23"):
                    opp_val = getattr(item, "kmLogo_Instruction23", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_Instruction23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_Instruction23"):
                    opp_val = getattr(item, "kmLogo_Instruction23", None)
                    
                    setattr(item, "kmLogo_Instruction23", self)
                    

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__19", None)
        self.__19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    if opp_val == self:
                        setattr(item, "20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    setattr(item, "20", self)
                    

    @property
    def kmLogo_ProcDeclaration(self):
        return self.__kmLogo_ProcDeclaration

    @kmLogo_ProcDeclaration.setter
    def kmLogo_ProcDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__kmLogo_ProcDeclaration", None)
        self.__kmLogo_ProcDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_Parameter"):
                    opp_val = getattr(item, "kmLogo_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_Parameter"):
                    opp_val = getattr(item, "kmLogo_Parameter", None)
                    
                    setattr(item, "kmLogo_Parameter", self)
                    

class kmLogo_Primitive(Instruction):

    pass
class kmLogo_Instruction(ABC):

    pass
class kmLogo_LogoProgram:

    pass
class kmLogo_Left(Primitive):

    pass
class kmLogo_Forward(Primitive):

    pass