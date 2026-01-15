from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class simpleExpressions_NotExpression(Expression):

    pass
class simpleExpressions_OrExpression(Expression):

    pass
class simpleExpressions_AndExpression(Expression):

    pass
class simpleExpressions_Comparison(Expression):

    def __init__(self, operator: str, simpleExpressions_Comparison: "simpleExpressions_Expression" = None, simpleExpressions_Comparison14: "simpleExpressions_Expression" = None):
        self.operator = operator
        self.simpleExpressions_Comparison = simpleExpressions_Comparison
        self.simpleExpressions_Comparison14 = simpleExpressions_Comparison14
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def simpleExpressions_Comparison(self):
        return self.__simpleExpressions_Comparison

    @simpleExpressions_Comparison.setter
    def simpleExpressions_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleExpressions_Comparison__simpleExpressions_Comparison", None)
        self.__simpleExpressions_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleExpressions_Expression12"):
                opp_val = getattr(old_value, "simpleExpressions_Expression12", None)
                if opp_val == self:
                    setattr(old_value, "simpleExpressions_Expression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleExpressions_Expression12"):
                opp_val = getattr(value, "simpleExpressions_Expression12", None)
                setattr(value, "simpleExpressions_Expression12", self)

    @property
    def simpleExpressions_Comparison14(self):
        return self.__simpleExpressions_Comparison14

    @simpleExpressions_Comparison14.setter
    def simpleExpressions_Comparison14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleExpressions_Comparison__simpleExpressions_Comparison14", None)
        self.__simpleExpressions_Comparison14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleExpressions_Expression15"):
                opp_val = getattr(old_value, "simpleExpressions_Expression15", None)
                if opp_val == self:
                    setattr(old_value, "simpleExpressions_Expression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleExpressions_Expression15"):
                opp_val = getattr(value, "simpleExpressions_Expression15", None)
                setattr(value, "simpleExpressions_Expression15", self)

class simpleExpressions_MethodCall(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class simpleExpressions_NumberLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class simpleExpressions_Expression:

    pass
class simpleExpressions_IfCondition:

    def __init__(self, elseif: bool, simpleExpressions_IfCondition: "simpleExpressions_Expression" = None):
        self.elseif = elseif
        self.simpleExpressions_IfCondition = simpleExpressions_IfCondition
        
    @property
    def elseif(self) -> bool:
        return self.__elseif

    @elseif.setter
    def elseif(self, elseif: bool):
        self.__elseif = elseif

    @property
    def simpleExpressions_IfCondition(self):
        return self.__simpleExpressions_IfCondition

    @simpleExpressions_IfCondition.setter
    def simpleExpressions_IfCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleExpressions_IfCondition__simpleExpressions_IfCondition", None)
        self.__simpleExpressions_IfCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleExpressions_Expression"):
                opp_val = getattr(old_value, "simpleExpressions_Expression", None)
                if opp_val == self:
                    setattr(old_value, "simpleExpressions_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleExpressions_Expression"):
                opp_val = getattr(value, "simpleExpressions_Expression", None)
                setattr(value, "simpleExpressions_Expression", self)
