from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class kmLogo_LogoProgram:

    pass
class BinaryExp:

    pass
class kmLogo_Lower(BinaryExp):

    pass
class kmLogo_Greater(BinaryExp):

    pass
class kmLogo_Div(BinaryExp):

    pass
class kmLogo_Mult(BinaryExp):

    pass
class kmLogo_Minus(BinaryExp):

    pass
class kmLogo_Equals(BinaryExp):

    pass
class kmLogo_Plus(BinaryExp):

    pass
class ControlStructure:

    pass
class kmLogo_Repeat(ControlStructure):

    pass
class kmLogo_While(ControlStructure):

    pass
class kmLogo_If(ControlStructure):

    pass
class kmLogo_Parameter:

    def __init__(self, name: str, kmLogo_Parameter: "kmLogo_ProcDeclaration" = None, kmLogo_Parameter33: "kmLogo_ParameterCall" = None):
        self.name = name
        self.kmLogo_Parameter = kmLogo_Parameter
        self.kmLogo_Parameter33 = kmLogo_Parameter33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def kmLogo_Parameter33(self):
        return self.__kmLogo_Parameter33

    @kmLogo_Parameter33.setter
    def kmLogo_Parameter33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Parameter__kmLogo_Parameter33", None)
        self.__kmLogo_Parameter33 = value
        
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

class Expression:

    pass
class kmLogo_ParameterCall(Expression):

    pass
class kmLogo_Constant(Expression):

    def __init__(self, integerValue: str):
        self.integerValue = integerValue
        
    @property
    def integerValue(self) -> str:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: str):
        self.__integerValue = integerValue

class kmLogo_ProcCall(Expression):

    pass
class kmLogo_BinaryExp(Expression):

    pass
class Primitive:

    pass
class kmLogo_Forward(Primitive):

    pass
class kmLogo_Left(Primitive):

    pass
class kmLogo_Right(Primitive):

    pass
class kmLogo_PenUp(Primitive):

    pass
class kmLogo_PenDown(Primitive):

    pass
class kmLogo_Clear(Primitive):

    pass
class kmLogo_Back(Primitive):

    pass
class Instruction:

    pass
class kmLogo_ProcDeclaration(Instruction):

    def __init__(self, name: str, ProcDeclaration: "kmLogo_ProcCall" = None, kmLogo_ProcDeclaration: set["kmLogo_Parameter"] = None, declaration: set["kmLogo_ProcCall"] = None, kmLogo_ProcDeclaration18: set["kmLogo_Instruction"] = None):
        self.name = name
        self.ProcDeclaration = ProcDeclaration
        self.kmLogo_ProcDeclaration = kmLogo_ProcDeclaration if kmLogo_ProcDeclaration is not None else set()
        self.declaration = declaration if declaration is not None else set()
        self.kmLogo_ProcDeclaration18 = kmLogo_ProcDeclaration18 if kmLogo_ProcDeclaration18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_ProcDeclaration18(self):
        return self.__kmLogo_ProcDeclaration18

    @kmLogo_ProcDeclaration18.setter
    def kmLogo_ProcDeclaration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__kmLogo_ProcDeclaration18", None)
        self.__kmLogo_ProcDeclaration18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_Instruction"):
                    opp_val = getattr(item, "kmLogo_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_Instruction"):
                    opp_val = getattr(item, "kmLogo_Instruction", None)
                    
                    setattr(item, "kmLogo_Instruction", self)
                    

    @property
    def ProcDeclaration(self):
        return self.__ProcDeclaration

    @ProcDeclaration.setter
    def ProcDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__ProcDeclaration", None)
        self.__ProcDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "procCall"):
                opp_val = getattr(old_value, "procCall", None)
                if opp_val == self:
                    setattr(old_value, "procCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "procCall"):
                opp_val = getattr(value, "procCall", None)
                setattr(value, "procCall", self)

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
                    

    @property
    def declaration(self):
        return self.__declaration

    @declaration.setter
    def declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ProcDeclaration__declaration", None)
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
                    

class kmLogo_Block(Instruction):

    pass
class kmLogo_ControlStructure(Instruction):

    pass
class kmLogo_Expression(Instruction):

    pass
class kmLogo_Primitive(Instruction):

    pass
class kmLogo_Instruction(ABC):

    pass