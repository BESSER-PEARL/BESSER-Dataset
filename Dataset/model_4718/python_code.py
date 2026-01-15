from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IntegerExpression:

    pass
class core_UnaryExpression(IntegerExpression):

    pass
class BinaryExpression:

    pass
class core_Minus(BinaryExpression):

    pass
class core_Equal(BinaryExpression):

    pass
class core_Div(BinaryExpression):

    pass
class core_Mod(BinaryExpression):

    pass
class core_Mult(BinaryExpression):

    pass
class core_Add(BinaryExpression):

    pass
class core_Filter(ABC):

    pass
class core_IntegerExpression(ABC):

    def __init__(self, core_IntegerExpression6: "core_Conditional" = None, core_IntegerExpression9: "core_Conditional" = None, core_IntegerExpression12: "core_Conditional" = None, core_IntegerExpression14: "core_BinaryExpression" = None, core_IntegerExpression: "core_Rule" = None, core_IntegerExpression4: "core_UnaryExpression" = None, core_IntegerExpression17: "core_BinaryExpression" = None):
        self.core_IntegerExpression6 = core_IntegerExpression6
        self.core_IntegerExpression9 = core_IntegerExpression9
        self.core_IntegerExpression12 = core_IntegerExpression12
        self.core_IntegerExpression14 = core_IntegerExpression14
        self.core_IntegerExpression = core_IntegerExpression
        self.core_IntegerExpression4 = core_IntegerExpression4
        self.core_IntegerExpression17 = core_IntegerExpression17
        
    @property
    def core_IntegerExpression12(self):
        return self.__core_IntegerExpression12

    @core_IntegerExpression12.setter
    def core_IntegerExpression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IntegerExpression__core_IntegerExpression12", None)
        self.__core_IntegerExpression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Conditional11"):
                opp_val = getattr(old_value, "core_Conditional11", None)
                if opp_val == self:
                    setattr(old_value, "core_Conditional11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Conditional11"):
                opp_val = getattr(value, "core_Conditional11", None)
                setattr(value, "core_Conditional11", self)

    @property
    def core_IntegerExpression4(self):
        return self.__core_IntegerExpression4

    @core_IntegerExpression4.setter
    def core_IntegerExpression4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IntegerExpression__core_IntegerExpression4", None)
        self.__core_IntegerExpression4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_UnaryExpression"):
                opp_val = getattr(old_value, "core_UnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "core_UnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_UnaryExpression"):
                opp_val = getattr(value, "core_UnaryExpression", None)
                setattr(value, "core_UnaryExpression", self)

    @property
    def core_IntegerExpression14(self):
        return self.__core_IntegerExpression14

    @core_IntegerExpression14.setter
    def core_IntegerExpression14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IntegerExpression__core_IntegerExpression14", None)
        self.__core_IntegerExpression14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_BinaryExpression"):
                opp_val = getattr(old_value, "core_BinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "core_BinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_BinaryExpression"):
                opp_val = getattr(value, "core_BinaryExpression", None)
                setattr(value, "core_BinaryExpression", self)

    @property
    def core_IntegerExpression9(self):
        return self.__core_IntegerExpression9

    @core_IntegerExpression9.setter
    def core_IntegerExpression9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IntegerExpression__core_IntegerExpression9", None)
        self.__core_IntegerExpression9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Conditional8"):
                opp_val = getattr(old_value, "core_Conditional8", None)
                if opp_val == self:
                    setattr(old_value, "core_Conditional8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Conditional8"):
                opp_val = getattr(value, "core_Conditional8", None)
                setattr(value, "core_Conditional8", self)

    @property
    def core_IntegerExpression17(self):
        return self.__core_IntegerExpression17

    @core_IntegerExpression17.setter
    def core_IntegerExpression17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IntegerExpression__core_IntegerExpression17", None)
        self.__core_IntegerExpression17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_BinaryExpression16"):
                opp_val = getattr(old_value, "core_BinaryExpression16", None)
                if opp_val == self:
                    setattr(old_value, "core_BinaryExpression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_BinaryExpression16"):
                opp_val = getattr(value, "core_BinaryExpression16", None)
                setattr(value, "core_BinaryExpression16", self)

    @property
    def core_IntegerExpression6(self):
        return self.__core_IntegerExpression6

    @core_IntegerExpression6.setter
    def core_IntegerExpression6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IntegerExpression__core_IntegerExpression6", None)
        self.__core_IntegerExpression6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Conditional"):
                opp_val = getattr(old_value, "core_Conditional", None)
                if opp_val == self:
                    setattr(old_value, "core_Conditional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Conditional"):
                opp_val = getattr(value, "core_Conditional", None)
                setattr(value, "core_Conditional", self)

    @property
    def core_IntegerExpression(self):
        return self.__core_IntegerExpression

    @core_IntegerExpression.setter
    def core_IntegerExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_core_IntegerExpression__core_IntegerExpression", None)
        self.__core_IntegerExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core_Rule"):
                opp_val = getattr(old_value, "core_Rule", None)
                if opp_val == self:
                    setattr(old_value, "core_Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core_Rule"):
                opp_val = getattr(value, "core_Rule", None)
                setattr(value, "core_Rule", self)

    def isBoolean(self) -> bool:
        # TODO: Implement isBoolean method
        pass

class core_Rule:

    pass
class core_BinaryExpression(IntegerExpression):

    pass
class core_Conditional(IntegerExpression):

    pass
class core_IntegerLiteral(IntegerExpression):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class core_Lower(BinaryExpression):

    pass
class core_Greater(BinaryExpression):

    pass
class UnaryExpression:

    pass
class core_UMinus(UnaryExpression):

    pass
class core_Not(UnaryExpression):

    pass
class core_Or(BinaryExpression):

    pass
class core_And(BinaryExpression):

    pass