from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class expressions_Model:

    pass
class UnaryOperator:

    pass
class expressions_Neg(UnaryOperator):

    pass
class BinaryOperator:

    pass
class expressions_Div(BinaryOperator):

    pass
class expressions_Mul(BinaryOperator):

    pass
class expressions_Minus(BinaryOperator):

    pass
class expressions_Plus(BinaryOperator):

    pass
class Expression:

    pass
class expressions_BinaryOperator(Expression):

    pass
class expressions_UnaryOperator(Expression):

    pass
class expressions_FunctionCall(Expression):

    pass
class expressions_ParameterAccess(Expression):

    pass
class expressions_Number(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expressions_Expression(ABC):

    pass
class expressions_Parameter:

    def __init__(self, name: str, expressions_Parameter: "expressions_Function" = None, expressions_Parameter4: "expressions_ParameterAccess" = None):
        self.name = name
        self.expressions_Parameter = expressions_Parameter
        self.expressions_Parameter4 = expressions_Parameter4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressions_Parameter4(self):
        return self.__expressions_Parameter4

    @expressions_Parameter4.setter
    def expressions_Parameter4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Parameter__expressions_Parameter4", None)
        self.__expressions_Parameter4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_ParameterAccess"):
                opp_val = getattr(old_value, "expressions_ParameterAccess", None)
                if opp_val == self:
                    setattr(old_value, "expressions_ParameterAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_ParameterAccess"):
                opp_val = getattr(value, "expressions_ParameterAccess", None)
                setattr(value, "expressions_ParameterAccess", self)

    @property
    def expressions_Parameter(self):
        return self.__expressions_Parameter

    @expressions_Parameter.setter
    def expressions_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Parameter__expressions_Parameter", None)
        self.__expressions_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Function"):
                opp_val = getattr(old_value, "expressions_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Function"):
                opp_val = getattr(value, "expressions_Function", None)
                if opp_val is None:
                    setattr(value, "expressions_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class expressions_Function:

    def __init__(self, name: str, expressions_Function: set["expressions_Parameter"] = None, expressions_Function2: "expressions_Expression" = None, expressions_Function13: "expressions_FunctionCall" = None, expressions_Function18: "expressions_Model" = None):
        self.name = name
        self.expressions_Function = expressions_Function if expressions_Function is not None else set()
        self.expressions_Function2 = expressions_Function2
        self.expressions_Function13 = expressions_Function13
        self.expressions_Function18 = expressions_Function18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressions_Function13(self):
        return self.__expressions_Function13

    @expressions_Function13.setter
    def expressions_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Function__expressions_Function13", None)
        self.__expressions_Function13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_FunctionCall"):
                opp_val = getattr(old_value, "expressions_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "expressions_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_FunctionCall"):
                opp_val = getattr(value, "expressions_FunctionCall", None)
                setattr(value, "expressions_FunctionCall", self)

    @property
    def expressions_Function(self):
        return self.__expressions_Function

    @expressions_Function.setter
    def expressions_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Function__expressions_Function", None)
        self.__expressions_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expressions_Parameter"):
                    opp_val = getattr(item, "expressions_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "expressions_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expressions_Parameter"):
                    opp_val = getattr(item, "expressions_Parameter", None)
                    
                    setattr(item, "expressions_Parameter", self)
                    

    @property
    def expressions_Function2(self):
        return self.__expressions_Function2

    @expressions_Function2.setter
    def expressions_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Function__expressions_Function2", None)
        self.__expressions_Function2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression"):
                opp_val = getattr(old_value, "expressions_Expression", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression"):
                opp_val = getattr(value, "expressions_Expression", None)
                setattr(value, "expressions_Expression", self)

    @property
    def expressions_Function18(self):
        return self.__expressions_Function18

    @expressions_Function18.setter
    def expressions_Function18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Function__expressions_Function18", None)
        self.__expressions_Function18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Model"):
                opp_val = getattr(old_value, "expressions_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Model"):
                opp_val = getattr(value, "expressions_Model", None)
                if opp_val is None:
                    setattr(value, "expressions_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
