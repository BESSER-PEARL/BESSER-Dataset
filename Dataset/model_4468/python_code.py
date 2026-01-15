from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BinaryExp:

    pass
class logoASM_Mult(BinaryExp):

    pass
class logoASM_Minus(BinaryExp):

    pass
class logoASM_Plus(BinaryExp):

    pass
class logoASM_LogoProgram:

    pass
class logoASM_Lower(BinaryExp):

    pass
class logoASM_Greater(BinaryExp):

    pass
class logoASM_Equals(BinaryExp):

    pass
class logoASM_Div(BinaryExp):

    pass
class ControlStructure:

    pass
class logoASM_Repeat(ControlStructure):

    pass
class logoASM_While(ControlStructure):

    pass
class logoASM_If(ControlStructure):

    pass
class logoASM_Parameter:

    def __init__(self, name: str, logoASM_Parameter: "logoASM_ProcDeclaration" = None, logoASM_Parameter34: "logoASM_ParameterCall" = None):
        self.name = name
        self.logoASM_Parameter = logoASM_Parameter
        self.logoASM_Parameter34 = logoASM_Parameter34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logoASM_Parameter34(self):
        return self.__logoASM_Parameter34

    @logoASM_Parameter34.setter
    def logoASM_Parameter34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logoASM_Parameter__logoASM_Parameter34", None)
        self.__logoASM_Parameter34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logoASM_ParameterCall"):
                opp_val = getattr(old_value, "logoASM_ParameterCall", None)
                if opp_val == self:
                    setattr(old_value, "logoASM_ParameterCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logoASM_ParameterCall"):
                opp_val = getattr(value, "logoASM_ParameterCall", None)
                setattr(value, "logoASM_ParameterCall", self)

    @property
    def logoASM_Parameter(self):
        return self.__logoASM_Parameter

    @logoASM_Parameter.setter
    def logoASM_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logoASM_Parameter__logoASM_Parameter", None)
        self.__logoASM_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logoASM_ProcDeclaration17"):
                opp_val = getattr(old_value, "logoASM_ProcDeclaration17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logoASM_ProcDeclaration17"):
                opp_val = getattr(value, "logoASM_ProcDeclaration17", None)
                if opp_val is None:
                    setattr(value, "logoASM_ProcDeclaration17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Expression:

    pass
class logoASM_Constant(Expression):

    def __init__(self, integerValue: int):
        self.integerValue = integerValue
        
    @property
    def integerValue(self) -> int:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: int):
        self.__integerValue = integerValue

class logoASM_ParameterCall(Expression):

    pass
class logoASM_ProcCall(Expression):

    pass
class logoASM_BinaryExp(Expression):

    pass
class Primitive:

    pass
class logoASM_Left(Primitive):

    pass
class logoASM_Clear(Primitive):

    pass
class logoASM_PenDown(Primitive):

    pass
class logoASM_Forward(Primitive):

    pass
class logoASM_Right(Primitive):

    pass
class logoASM_PenUp(Primitive):

    pass
class logoASM_Back(Primitive):

    pass
class Instruction:

    pass
class logoASM_Expression(Instruction):

    pass
class logoASM_ProcDeclaration(Instruction):

    def __init__(self, name: str, logoASM_ProcDeclaration: "logoASM_ProcCall" = None, logoASM_ProcDeclaration17: set["logoASM_Parameter"] = None, logoASM_ProcDeclaration19: set["logoASM_Instruction"] = None):
        self.name = name
        self.logoASM_ProcDeclaration = logoASM_ProcDeclaration
        self.logoASM_ProcDeclaration17 = logoASM_ProcDeclaration17 if logoASM_ProcDeclaration17 is not None else set()
        self.logoASM_ProcDeclaration19 = logoASM_ProcDeclaration19 if logoASM_ProcDeclaration19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logoASM_ProcDeclaration(self):
        return self.__logoASM_ProcDeclaration

    @logoASM_ProcDeclaration.setter
    def logoASM_ProcDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logoASM_ProcDeclaration__logoASM_ProcDeclaration", None)
        self.__logoASM_ProcDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logoASM_ProcCall15"):
                opp_val = getattr(old_value, "logoASM_ProcCall15", None)
                if opp_val == self:
                    setattr(old_value, "logoASM_ProcCall15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logoASM_ProcCall15"):
                opp_val = getattr(value, "logoASM_ProcCall15", None)
                setattr(value, "logoASM_ProcCall15", self)

    @property
    def logoASM_ProcDeclaration17(self):
        return self.__logoASM_ProcDeclaration17

    @logoASM_ProcDeclaration17.setter
    def logoASM_ProcDeclaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logoASM_ProcDeclaration__logoASM_ProcDeclaration17", None)
        self.__logoASM_ProcDeclaration17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "logoASM_Parameter"):
                    opp_val = getattr(item, "logoASM_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "logoASM_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "logoASM_Parameter"):
                    opp_val = getattr(item, "logoASM_Parameter", None)
                    
                    setattr(item, "logoASM_Parameter", self)
                    

    @property
    def logoASM_ProcDeclaration19(self):
        return self.__logoASM_ProcDeclaration19

    @logoASM_ProcDeclaration19.setter
    def logoASM_ProcDeclaration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logoASM_ProcDeclaration__logoASM_ProcDeclaration19", None)
        self.__logoASM_ProcDeclaration19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "logoASM_Instruction"):
                    opp_val = getattr(item, "logoASM_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "logoASM_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "logoASM_Instruction"):
                    opp_val = getattr(item, "logoASM_Instruction", None)
                    
                    setattr(item, "logoASM_Instruction", self)
                    

class logoASM_Block(Instruction):

    pass
class logoASM_ControlStructure(Instruction):

    pass
class logoASM_Primitive(Instruction):

    pass
class logoASM_Instruction(ABC):

    pass