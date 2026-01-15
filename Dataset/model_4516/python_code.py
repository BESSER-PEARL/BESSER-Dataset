from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class logo_Parameter:

    def __init__(self, name: str, logo_Parameter38: "logo_ParameterCall" = None, logo_Parameter: "logo_ProcDeclaration" = None):
        self.name = name
        self.logo_Parameter38 = logo_Parameter38
        self.logo_Parameter = logo_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logo_Parameter(self):
        return self.__logo_Parameter

    @logo_Parameter.setter
    def logo_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_Parameter__logo_Parameter", None)
        self.__logo_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logo_ProcDeclaration13"):
                opp_val = getattr(old_value, "logo_ProcDeclaration13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logo_ProcDeclaration13"):
                opp_val = getattr(value, "logo_ProcDeclaration13", None)
                if opp_val is None:
                    setattr(value, "logo_ProcDeclaration13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def logo_Parameter38(self):
        return self.__logo_Parameter38

    @logo_Parameter38.setter
    def logo_Parameter38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_Parameter__logo_Parameter38", None)
        self.__logo_Parameter38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logo_ParameterCall"):
                opp_val = getattr(old_value, "logo_ParameterCall", None)
                if opp_val == self:
                    setattr(old_value, "logo_ParameterCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logo_ParameterCall"):
                opp_val = getattr(value, "logo_ParameterCall", None)
                setattr(value, "logo_ParameterCall", self)

class Expression:

    pass
class logo_Minus(Expression):

    pass
class logo_Greater(Expression):

    pass
class logo_Div(Expression):

    pass
class logo_Equals(Expression):

    pass
class logo_Mult(Expression):

    pass
class logo_Lower(Expression):

    pass
class logo_Plus(Expression):

    pass
class logo_Constant(Expression):

    def __init__(self, integerValue: int):
        self.integerValue = integerValue
        
    @property
    def integerValue(self) -> int:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: int):
        self.__integerValue = integerValue

class logo_Expression:

    pass
class Instruction:

    pass
class logo_Left(Instruction):

    pass
class logo_If(Instruction):

    pass
class logo_ProcDeclaration(Instruction):

    def __init__(self, name: str, logo_ProcDeclaration: "logo_ProcCall" = None, logo_ProcDeclaration13: set["logo_Parameter"] = None, logo_ProcDeclaration15: set["logo_Instruction"] = None):
        self.name = name
        self.logo_ProcDeclaration = logo_ProcDeclaration
        self.logo_ProcDeclaration13 = logo_ProcDeclaration13 if logo_ProcDeclaration13 is not None else set()
        self.logo_ProcDeclaration15 = logo_ProcDeclaration15 if logo_ProcDeclaration15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logo_ProcDeclaration13(self):
        return self.__logo_ProcDeclaration13

    @logo_ProcDeclaration13.setter
    def logo_ProcDeclaration13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_ProcDeclaration__logo_ProcDeclaration13", None)
        self.__logo_ProcDeclaration13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "logo_Parameter"):
                    opp_val = getattr(item, "logo_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "logo_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "logo_Parameter"):
                    opp_val = getattr(item, "logo_Parameter", None)
                    
                    setattr(item, "logo_Parameter", self)
                    

    @property
    def logo_ProcDeclaration15(self):
        return self.__logo_ProcDeclaration15

    @logo_ProcDeclaration15.setter
    def logo_ProcDeclaration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_ProcDeclaration__logo_ProcDeclaration15", None)
        self.__logo_ProcDeclaration15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "logo_Instruction16"):
                    opp_val = getattr(item, "logo_Instruction16", None)
                    
                    if opp_val == self:
                        setattr(item, "logo_Instruction16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "logo_Instruction16"):
                    opp_val = getattr(item, "logo_Instruction16", None)
                    
                    setattr(item, "logo_Instruction16", self)
                    

    @property
    def logo_ProcDeclaration(self):
        return self.__logo_ProcDeclaration

    @logo_ProcDeclaration.setter
    def logo_ProcDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_ProcDeclaration__logo_ProcDeclaration", None)
        self.__logo_ProcDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logo_ProcCall"):
                opp_val = getattr(old_value, "logo_ProcCall", None)
                if opp_val == self:
                    setattr(old_value, "logo_ProcCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logo_ProcCall"):
                opp_val = getattr(value, "logo_ProcCall", None)
                setattr(value, "logo_ProcCall", self)

class logo_While(Instruction):

    pass
class logo_Repeat(Instruction):

    pass
class logo_ParameterCall(Instruction, Expression):

    pass
class logo_Block(Instruction):

    pass
class logo_ProcCall(Instruction):

    pass
class logo_Forward(Instruction):

    pass
class logo_Backward(Instruction):

    pass
class logo_Instruction:

    pass
class logo_LogoProgram:

    pass
class logo_Clear(Instruction):

    pass
class logo_PenUp(Instruction):

    pass
class logo_PenDown(Instruction):

    pass
class logo_Right(Instruction):

    pass