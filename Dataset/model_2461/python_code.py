from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class operators_OclExpression(ABC):

    pass
class OclExpression:

    pass
class operators_IfExp(OclExpression):

    pass
class operators_OclType(OclExpression):

    pass
class operators_OperationCallExp(OclExpression):

    def __init__(self, name: str, operators_OperationCallExp: "operators_OclExpression" = None, operators_OperationCallExp4: set["operators_OclExpression"] = None):
        self.name = name
        self.operators_OperationCallExp = operators_OperationCallExp
        self.operators_OperationCallExp4 = operators_OperationCallExp4 if operators_OperationCallExp4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operators_OperationCallExp4(self):
        return self.__operators_OperationCallExp4

    @operators_OperationCallExp4.setter
    def operators_OperationCallExp4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_OperationCallExp__operators_OperationCallExp4", None)
        self.__operators_OperationCallExp4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_OclExpression5"):
                    opp_val = getattr(item, "operators_OclExpression5", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_OclExpression5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_OclExpression5"):
                    opp_val = getattr(item, "operators_OclExpression5", None)
                    
                    setattr(item, "operators_OclExpression5", self)
                    

    @property
    def operators_OperationCallExp(self):
        return self.__operators_OperationCallExp

    @operators_OperationCallExp.setter
    def operators_OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_OperationCallExp__operators_OperationCallExp", None)
        self.__operators_OperationCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_OclExpression2"):
                opp_val = getattr(old_value, "operators_OclExpression2", None)
                if opp_val == self:
                    setattr(old_value, "operators_OclExpression2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_OclExpression2"):
                opp_val = getattr(value, "operators_OclExpression2", None)
                setattr(value, "operators_OclExpression2", self)

class operators_Type:

    def __init__(self, operators_Type: "operators_OclExpression" = None):
        self.operators_Type = operators_Type
        
    @property
    def operators_Type(self):
        return self.__operators_Type

    @operators_Type.setter
    def operators_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Type__operators_Type", None)
        self.__operators_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_OclExpression"):
                opp_val = getattr(old_value, "operators_OclExpression", None)
                if opp_val == self:
                    setattr(old_value, "operators_OclExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_OclExpression"):
                opp_val = getattr(value, "operators_OclExpression", None)
                setattr(value, "operators_OclExpression", self)

    def isSuperTypeOf(self, t: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def isSameType(self, t: str) -> bool:
        # TODO: Implement isSameType method
        pass
