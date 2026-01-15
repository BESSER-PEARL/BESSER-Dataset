from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class rankPL_FunctionCall(Expression):

    pass
class rankPL_Multi(Expression):

    pass
class rankPL_Minus(Expression):

    pass
class rankPL_NumberLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class rankPL_Div(Expression):

    pass
class rankPL_Plus(Expression):

    pass
class rankPL_Expression:

    pass
class AbstractDefinition:

    pass
class rankPL_DeclaredParameter(AbstractDefinition):

    pass
class rankPL_Definition(AbstractDefinition):

    pass
class rankPL_AbstractDefinition:

    def __init__(self, name: str, rankPL_AbstractDefinition: "rankPL_Model" = None, rankPL_AbstractDefinition23: "rankPL_FunctionCall" = None):
        self.name = name
        self.rankPL_AbstractDefinition = rankPL_AbstractDefinition
        self.rankPL_AbstractDefinition23 = rankPL_AbstractDefinition23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rankPL_AbstractDefinition(self):
        return self.__rankPL_AbstractDefinition

    @rankPL_AbstractDefinition.setter
    def rankPL_AbstractDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rankPL_AbstractDefinition__rankPL_AbstractDefinition", None)
        self.__rankPL_AbstractDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rankPL_Model"):
                opp_val = getattr(old_value, "rankPL_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankPL_Model"):
                opp_val = getattr(value, "rankPL_Model", None)
                if opp_val is None:
                    setattr(value, "rankPL_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rankPL_AbstractDefinition23(self):
        return self.__rankPL_AbstractDefinition23

    @rankPL_AbstractDefinition23.setter
    def rankPL_AbstractDefinition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rankPL_AbstractDefinition__rankPL_AbstractDefinition23", None)
        self.__rankPL_AbstractDefinition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rankPL_FunctionCall"):
                opp_val = getattr(old_value, "rankPL_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "rankPL_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankPL_FunctionCall"):
                opp_val = getattr(value, "rankPL_FunctionCall", None)
                setattr(value, "rankPL_FunctionCall", self)

class rankPL_Model:

    pass