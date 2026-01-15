from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class realop_IsNegative(Expression):

    def __init__(self, featureName: str):
        self.featureName = featureName
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

class realop_AndExp(Expression):

    pass
class realop_IsRealised(Expression):

    def __init__(self, featureName: str):
        self.featureName = featureName
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

class realop_NotExp(Expression):

    pass
class realop_IsPositive(Expression):

    def __init__(self, featureName: str):
        self.featureName = featureName
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

class realop_XorExp(Expression):

    pass
class realop_OrExp(Expression):

    pass
class realop_Expression:

    pass
class realop_Operator:

    def __init__(self, name: str, realop_Operator: "realop_Realop" = None, realop_Operator2: "realop_Expression" = None, realop_Operator4: "realop_Expression" = None):
        self.name = name
        self.realop_Operator = realop_Operator
        self.realop_Operator2 = realop_Operator2
        self.realop_Operator4 = realop_Operator4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def realop_Operator(self):
        return self.__realop_Operator

    @realop_Operator.setter
    def realop_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_realop_Operator__realop_Operator", None)
        self.__realop_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "realop_Realop"):
                opp_val = getattr(old_value, "realop_Realop", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "realop_Realop"):
                opp_val = getattr(value, "realop_Realop", None)
                if opp_val is None:
                    setattr(value, "realop_Realop", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def realop_Operator4(self):
        return self.__realop_Operator4

    @realop_Operator4.setter
    def realop_Operator4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_realop_Operator__realop_Operator4", None)
        self.__realop_Operator4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "realop_Expression5"):
                opp_val = getattr(old_value, "realop_Expression5", None)
                if opp_val == self:
                    setattr(old_value, "realop_Expression5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "realop_Expression5"):
                opp_val = getattr(value, "realop_Expression5", None)
                setattr(value, "realop_Expression5", self)

    @property
    def realop_Operator2(self):
        return self.__realop_Operator2

    @realop_Operator2.setter
    def realop_Operator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_realop_Operator__realop_Operator2", None)
        self.__realop_Operator2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "realop_Expression"):
                opp_val = getattr(old_value, "realop_Expression", None)
                if opp_val == self:
                    setattr(old_value, "realop_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "realop_Expression"):
                opp_val = getattr(value, "realop_Expression", None)
                setattr(value, "realop_Expression", self)

class realop_Realop:

    pass