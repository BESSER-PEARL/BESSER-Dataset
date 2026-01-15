from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Logo_Expression:

    def __init__(self, Logo_Expression: "Logo_Back" = None, Logo_Expression7: "Logo_Right" = None, Logo_Expression3: "Logo_Forward" = None, Logo_Expression5: "Logo_Left" = None):
        self.Logo_Expression = Logo_Expression
        self.Logo_Expression7 = Logo_Expression7
        self.Logo_Expression3 = Logo_Expression3
        self.Logo_Expression5 = Logo_Expression5
        
    @property
    def Logo_Expression7(self):
        return self.__Logo_Expression7

    @Logo_Expression7.setter
    def Logo_Expression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_Expression__Logo_Expression7", None)
        self.__Logo_Expression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_Right"):
                opp_val = getattr(old_value, "Logo_Right", None)
                if opp_val == self:
                    setattr(old_value, "Logo_Right", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_Right"):
                opp_val = getattr(value, "Logo_Right", None)
                setattr(value, "Logo_Right", self)

    @property
    def Logo_Expression(self):
        return self.__Logo_Expression

    @Logo_Expression.setter
    def Logo_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_Expression__Logo_Expression", None)
        self.__Logo_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_Back"):
                opp_val = getattr(old_value, "Logo_Back", None)
                if opp_val == self:
                    setattr(old_value, "Logo_Back", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_Back"):
                opp_val = getattr(value, "Logo_Back", None)
                setattr(value, "Logo_Back", self)

    @property
    def Logo_Expression5(self):
        return self.__Logo_Expression5

    @Logo_Expression5.setter
    def Logo_Expression5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_Expression__Logo_Expression5", None)
        self.__Logo_Expression5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_Left"):
                opp_val = getattr(old_value, "Logo_Left", None)
                if opp_val == self:
                    setattr(old_value, "Logo_Left", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_Left"):
                opp_val = getattr(value, "Logo_Left", None)
                setattr(value, "Logo_Left", self)

    @property
    def Logo_Expression3(self):
        return self.__Logo_Expression3

    @Logo_Expression3.setter
    def Logo_Expression3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_Expression__Logo_Expression3", None)
        self.__Logo_Expression3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_Forward"):
                opp_val = getattr(old_value, "Logo_Forward", None)
                if opp_val == self:
                    setattr(old_value, "Logo_Forward", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_Forward"):
                opp_val = getattr(value, "Logo_Forward", None)
                setattr(value, "Logo_Forward", self)

    def eval(self, context: str):
        # TODO: Implement eval method
        pass

class Primitive:

    pass
class Logo_PenUp(Primitive):

    pass
class Logo_Forward(Primitive):

    pass
class Logo_PenDown(Primitive):

    pass
class Logo_Clear(Primitive):

    pass
class Logo_Left(Primitive):

    pass
class Logo_Right(Primitive):

    pass
class Logo_Back(Primitive):

    pass
class Logo_Primitive(ABC):

    pass
class Logo_LogoProgram:

    pass