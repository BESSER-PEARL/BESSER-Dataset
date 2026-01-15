from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BinaryExp:

    pass
class kmLogo_Equals(BinaryExp):

    pass
class kmLogo_Mult(BinaryExp):

    pass
class kmLogo_Div(BinaryExp):

    pass
class kmLogo_Minus(BinaryExp):

    pass
class kmLogo_Plus(BinaryExp):

    pass
class kmLogo_Parameter:

    def __init__(self, name: str, kmLogo_Parameter31: "kmLogo_MethodeDeclaration" = None, kmLogo_Parameter: "kmLogo_ParameterCall" = None):
        self.name = name
        self.kmLogo_Parameter31 = kmLogo_Parameter31
        self.kmLogo_Parameter = kmLogo_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_Parameter31(self):
        return self.__kmLogo_Parameter31

    @kmLogo_Parameter31.setter
    def kmLogo_Parameter31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_Parameter__kmLogo_Parameter31", None)
        self.__kmLogo_Parameter31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_MethodeDeclaration30"):
                opp_val = getattr(old_value, "kmLogo_MethodeDeclaration30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_MethodeDeclaration30"):
                opp_val = getattr(value, "kmLogo_MethodeDeclaration30", None)
                if opp_val is None:
                    setattr(value, "kmLogo_MethodeDeclaration30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "kmLogo_ParameterCall"):
                opp_val = getattr(old_value, "kmLogo_ParameterCall", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_ParameterCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_ParameterCall"):
                opp_val = getattr(value, "kmLogo_ParameterCall", None)
                setattr(value, "kmLogo_ParameterCall", self)

class kmLogo_Main:

    pass
class kmLogo_JavaProgram:

    def __init__(self, name: str, kmLogo_JavaProgram: "kmLogo_Main" = None, kmLogo_JavaProgram22: set["kmLogo_MethodeDeclaration"] = None):
        self.name = name
        self.kmLogo_JavaProgram = kmLogo_JavaProgram
        self.kmLogo_JavaProgram22 = kmLogo_JavaProgram22 if kmLogo_JavaProgram22 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_JavaProgram22(self):
        return self.__kmLogo_JavaProgram22

    @kmLogo_JavaProgram22.setter
    def kmLogo_JavaProgram22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_JavaProgram__kmLogo_JavaProgram22", None)
        self.__kmLogo_JavaProgram22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_MethodeDeclaration"):
                    opp_val = getattr(item, "kmLogo_MethodeDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_MethodeDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_MethodeDeclaration"):
                    opp_val = getattr(item, "kmLogo_MethodeDeclaration", None)
                    
                    setattr(item, "kmLogo_MethodeDeclaration", self)
                    

    @property
    def kmLogo_JavaProgram(self):
        return self.__kmLogo_JavaProgram

    @kmLogo_JavaProgram.setter
    def kmLogo_JavaProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_JavaProgram__kmLogo_JavaProgram", None)
        self.__kmLogo_JavaProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Main"):
                opp_val = getattr(old_value, "kmLogo_Main", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Main", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Main"):
                opp_val = getattr(value, "kmLogo_Main", None)
                setattr(value, "kmLogo_Main", self)

class kmLogo_Lower(BinaryExp):

    pass
class kmLogo_Greater(BinaryExp):

    pass
class Instruction:

    pass
class kmLogo_Expression(Instruction):

    pass
class kmLogo_MethodeDeclaration(Instruction):

    def __init__(self, name: str, MethodeDeclaration: "kmLogo_MethodeCall" = None, kmLogo_MethodeDeclaration: "kmLogo_JavaProgram" = None, kmLogo_MethodeDeclaration27: set["kmLogo_Instruction"] = None, kmLogo_MethodeDeclaration30: set["kmLogo_Parameter"] = None, methodedeclaration: set["kmLogo_MethodeCall"] = None):
        self.name = name
        self.MethodeDeclaration = MethodeDeclaration
        self.kmLogo_MethodeDeclaration = kmLogo_MethodeDeclaration
        self.kmLogo_MethodeDeclaration27 = kmLogo_MethodeDeclaration27 if kmLogo_MethodeDeclaration27 is not None else set()
        self.kmLogo_MethodeDeclaration30 = kmLogo_MethodeDeclaration30 if kmLogo_MethodeDeclaration30 is not None else set()
        self.methodedeclaration = methodedeclaration if methodedeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kmLogo_MethodeDeclaration30(self):
        return self.__kmLogo_MethodeDeclaration30

    @kmLogo_MethodeDeclaration30.setter
    def kmLogo_MethodeDeclaration30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_MethodeDeclaration__kmLogo_MethodeDeclaration30", None)
        self.__kmLogo_MethodeDeclaration30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_Parameter31"):
                    opp_val = getattr(item, "kmLogo_Parameter31", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_Parameter31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_Parameter31"):
                    opp_val = getattr(item, "kmLogo_Parameter31", None)
                    
                    setattr(item, "kmLogo_Parameter31", self)
                    

    @property
    def kmLogo_MethodeDeclaration27(self):
        return self.__kmLogo_MethodeDeclaration27

    @kmLogo_MethodeDeclaration27.setter
    def kmLogo_MethodeDeclaration27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_MethodeDeclaration__kmLogo_MethodeDeclaration27", None)
        self.__kmLogo_MethodeDeclaration27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kmLogo_Instruction28"):
                    opp_val = getattr(item, "kmLogo_Instruction28", None)
                    
                    if opp_val == self:
                        setattr(item, "kmLogo_Instruction28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kmLogo_Instruction28"):
                    opp_val = getattr(item, "kmLogo_Instruction28", None)
                    
                    setattr(item, "kmLogo_Instruction28", self)
                    

    @property
    def MethodeDeclaration(self):
        return self.__MethodeDeclaration

    @MethodeDeclaration.setter
    def MethodeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_MethodeDeclaration__MethodeDeclaration", None)
        self.__MethodeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methodecall"):
                opp_val = getattr(old_value, "methodecall", None)
                if opp_val == self:
                    setattr(old_value, "methodecall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methodecall"):
                opp_val = getattr(value, "methodecall", None)
                setattr(value, "methodecall", self)

    @property
    def kmLogo_MethodeDeclaration(self):
        return self.__kmLogo_MethodeDeclaration

    @kmLogo_MethodeDeclaration.setter
    def kmLogo_MethodeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_MethodeDeclaration__kmLogo_MethodeDeclaration", None)
        self.__kmLogo_MethodeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_JavaProgram22"):
                opp_val = getattr(old_value, "kmLogo_JavaProgram22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_JavaProgram22"):
                opp_val = getattr(value, "kmLogo_JavaProgram22", None)
                if opp_val is None:
                    setattr(value, "kmLogo_JavaProgram22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def methodedeclaration(self):
        return self.__methodedeclaration

    @methodedeclaration.setter
    def methodedeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_MethodeDeclaration__methodedeclaration", None)
        self.__methodedeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodeCall"):
                    opp_val = getattr(item, "MethodeCall", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodeCall", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodeCall"):
                    opp_val = getattr(item, "MethodeCall", None)
                    
                    setattr(item, "MethodeCall", self)
                    

class Expression:

    pass
class kmLogo_ParameterCall(Expression):

    pass
class kmLogo_MethodeCall(Expression):

    pass
class kmLogo_Instruction(ABC):

    pass
class kmLogo_ControlStructure(Instruction):

    pass
class ControlStructure:

    pass
class kmLogo_While(ControlStructure):

    pass
class kmLogo_For(ControlStructure):

    pass
class kmLogo_If(ControlStructure):

    pass
class kmLogo_Block(Instruction):

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

class kmLogo_BinaryExp(Expression):

    pass