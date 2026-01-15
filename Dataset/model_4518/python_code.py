from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Primitive:

    pass
class Primitives_Back(Primitive):

    pass
class Primitives_Right(Primitive):

    pass
class Primitives_Left(Primitive):

    pass
class Primitives_Forward(Primitive):

    pass
class Instruction:

    pass
class Primitives_Expression(Instruction):

    def __init__(self, Primitives_Expression: "Primitives_Forward" = None, Primitives_Expression3: "Primitives_Back" = None, Primitives_Expression5: "Primitives_Left" = None, Primitives_Expression7: "Primitives_Right" = None):
        self.Primitives_Expression = Primitives_Expression
        self.Primitives_Expression3 = Primitives_Expression3
        self.Primitives_Expression5 = Primitives_Expression5
        self.Primitives_Expression7 = Primitives_Expression7
        
    @property
    def Primitives_Expression3(self):
        return self.__Primitives_Expression3

    @Primitives_Expression3.setter
    def Primitives_Expression3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Primitives_Expression__Primitives_Expression3", None)
        self.__Primitives_Expression3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Primitives_Back"):
                opp_val = getattr(old_value, "Primitives_Back", None)
                if opp_val == self:
                    setattr(old_value, "Primitives_Back", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Primitives_Back"):
                opp_val = getattr(value, "Primitives_Back", None)
                setattr(value, "Primitives_Back", self)

    @property
    def Primitives_Expression7(self):
        return self.__Primitives_Expression7

    @Primitives_Expression7.setter
    def Primitives_Expression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Primitives_Expression__Primitives_Expression7", None)
        self.__Primitives_Expression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Primitives_Right"):
                opp_val = getattr(old_value, "Primitives_Right", None)
                if opp_val == self:
                    setattr(old_value, "Primitives_Right", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Primitives_Right"):
                opp_val = getattr(value, "Primitives_Right", None)
                setattr(value, "Primitives_Right", self)

    @property
    def Primitives_Expression(self):
        return self.__Primitives_Expression

    @Primitives_Expression.setter
    def Primitives_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Primitives_Expression__Primitives_Expression", None)
        self.__Primitives_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Primitives_Forward"):
                opp_val = getattr(old_value, "Primitives_Forward", None)
                if opp_val == self:
                    setattr(old_value, "Primitives_Forward", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Primitives_Forward"):
                opp_val = getattr(value, "Primitives_Forward", None)
                setattr(value, "Primitives_Forward", self)

    @property
    def Primitives_Expression5(self):
        return self.__Primitives_Expression5

    @Primitives_Expression5.setter
    def Primitives_Expression5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Primitives_Expression__Primitives_Expression5", None)
        self.__Primitives_Expression5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Primitives_Left"):
                opp_val = getattr(old_value, "Primitives_Left", None)
                if opp_val == self:
                    setattr(old_value, "Primitives_Left", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Primitives_Left"):
                opp_val = getattr(value, "Primitives_Left", None)
                setattr(value, "Primitives_Left", self)

    def eval(self, context: str) -> str:
        # TODO: Implement eval method
        pass

class Primitives_Primitive(Instruction):

    pass
class Primitives_Instruction(ABC):

    pass
class Primitives_LogoProgram:

    pass