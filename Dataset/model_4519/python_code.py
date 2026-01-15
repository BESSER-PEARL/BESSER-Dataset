from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class logo_Parameter:

    def __init__(self, name: str, logo_Parameter: "logo_ProcDeclaration" = None):
        self.name = name
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
            if hasattr(old_value, "logo_ProcDeclaration"):
                opp_val = getattr(old_value, "logo_ProcDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logo_ProcDeclaration"):
                opp_val = getattr(value, "logo_ProcDeclaration", None)
                if opp_val is None:
                    setattr(value, "logo_ProcDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Instruction:

    pass
class logo_ProcCall(Instruction):

    def __init__(self, actualArgs: int, logo_ProcCall: "logo_ProcDeclaration" = None):
        self.actualArgs = actualArgs
        self.logo_ProcCall = logo_ProcCall
        
    @property
    def actualArgs(self) -> int:
        return self.__actualArgs

    @actualArgs.setter
    def actualArgs(self, actualArgs: int):
        self.__actualArgs = actualArgs

    @property
    def logo_ProcCall(self):
        return self.__logo_ProcCall

    @logo_ProcCall.setter
    def logo_ProcCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_ProcCall__logo_ProcCall", None)
        self.__logo_ProcCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logo_ProcDeclaration6"):
                opp_val = getattr(old_value, "logo_ProcDeclaration6", None)
                if opp_val == self:
                    setattr(old_value, "logo_ProcDeclaration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logo_ProcDeclaration6"):
                opp_val = getattr(value, "logo_ProcDeclaration6", None)
                setattr(value, "logo_ProcDeclaration6", self)

class logo_ProcDeclaration(Instruction):

    def __init__(self, name: str, logo_ProcDeclaration: set["logo_Parameter"] = None, logo_ProcDeclaration3: set["logo_Instruction"] = None, logo_ProcDeclaration6: "logo_ProcCall" = None):
        self.name = name
        self.logo_ProcDeclaration = logo_ProcDeclaration if logo_ProcDeclaration is not None else set()
        self.logo_ProcDeclaration3 = logo_ProcDeclaration3 if logo_ProcDeclaration3 is not None else set()
        self.logo_ProcDeclaration6 = logo_ProcDeclaration6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logo_ProcDeclaration(self):
        return self.__logo_ProcDeclaration

    @logo_ProcDeclaration.setter
    def logo_ProcDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_ProcDeclaration__logo_ProcDeclaration", None)
        self.__logo_ProcDeclaration = value if value is not None else set()
        
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
    def logo_ProcDeclaration6(self):
        return self.__logo_ProcDeclaration6

    @logo_ProcDeclaration6.setter
    def logo_ProcDeclaration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_ProcDeclaration__logo_ProcDeclaration6", None)
        self.__logo_ProcDeclaration6 = value
        
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

    @property
    def logo_ProcDeclaration3(self):
        return self.__logo_ProcDeclaration3

    @logo_ProcDeclaration3.setter
    def logo_ProcDeclaration3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_ProcDeclaration__logo_ProcDeclaration3", None)
        self.__logo_ProcDeclaration3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "logo_Instruction4"):
                    opp_val = getattr(item, "logo_Instruction4", None)
                    
                    if opp_val == self:
                        setattr(item, "logo_Instruction4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "logo_Instruction4"):
                    opp_val = getattr(item, "logo_Instruction4", None)
                    
                    setattr(item, "logo_Instruction4", self)
                    

class logo_Right(Instruction):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class logo_Left(Instruction):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class logo_Forward(Instruction):

    def __init__(self, steps: int):
        self.steps = steps
        
    @property
    def steps(self) -> int:
        return self.__steps

    @steps.setter
    def steps(self, steps: int):
        self.__steps = steps

class logo_Instruction:

    pass
class logo_LogoProgram:

    pass