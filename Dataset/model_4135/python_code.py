from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class asso_NegFloatConstant(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class asso_Minus(Expression):

    pass
class asso_Mult(Expression):

    pass
class asso_Div(Expression):

    pass
class asso_VariableRef(Expression):

    pass
class asso_Plus(Expression):

    pass
class asso_FloatConstant(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class asso_Expression:

    pass
class asso_EvalExpression:

    pass
class asso_Variable:

    def __init__(self, name: str, asso_Variable: "asso_Model" = None, asso_Variable5: "asso_Variable" = None, asso_Variable3: set["asso_Variable"] = None, asso_Variable7: "asso_Expression" = None, asso_Variable12: "asso_VariableRef" = None):
        self.name = name
        self.asso_Variable = asso_Variable
        self.asso_Variable5 = asso_Variable5
        self.asso_Variable3 = asso_Variable3 if asso_Variable3 is not None else set()
        self.asso_Variable7 = asso_Variable7
        self.asso_Variable12 = asso_Variable12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def asso_Variable5(self):
        return self.__asso_Variable5

    @asso_Variable5.setter
    def asso_Variable5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asso_Variable__asso_Variable5", None)
        self.__asso_Variable5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asso_Variable3"):
                opp_val = getattr(old_value, "asso_Variable3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asso_Variable3"):
                opp_val = getattr(value, "asso_Variable3", None)
                if opp_val is None:
                    setattr(value, "asso_Variable3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def asso_Variable3(self):
        return self.__asso_Variable3

    @asso_Variable3.setter
    def asso_Variable3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asso_Variable__asso_Variable3", None)
        self.__asso_Variable3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "asso_Variable5"):
                    opp_val = getattr(item, "asso_Variable5", None)
                    
                    if opp_val == self:
                        setattr(item, "asso_Variable5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "asso_Variable5"):
                    opp_val = getattr(item, "asso_Variable5", None)
                    
                    setattr(item, "asso_Variable5", self)
                    

    @property
    def asso_Variable(self):
        return self.__asso_Variable

    @asso_Variable.setter
    def asso_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asso_Variable__asso_Variable", None)
        self.__asso_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asso_Model"):
                opp_val = getattr(old_value, "asso_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asso_Model"):
                opp_val = getattr(value, "asso_Model", None)
                if opp_val is None:
                    setattr(value, "asso_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def asso_Variable12(self):
        return self.__asso_Variable12

    @asso_Variable12.setter
    def asso_Variable12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asso_Variable__asso_Variable12", None)
        self.__asso_Variable12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asso_VariableRef"):
                opp_val = getattr(old_value, "asso_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "asso_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asso_VariableRef"):
                opp_val = getattr(value, "asso_VariableRef", None)
                setattr(value, "asso_VariableRef", self)

    @property
    def asso_Variable7(self):
        return self.__asso_Variable7

    @asso_Variable7.setter
    def asso_Variable7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_asso_Variable__asso_Variable7", None)
        self.__asso_Variable7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "asso_Expression"):
                opp_val = getattr(old_value, "asso_Expression", None)
                if opp_val == self:
                    setattr(old_value, "asso_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "asso_Expression"):
                opp_val = getattr(value, "asso_Expression", None)
                setattr(value, "asso_Expression", self)

class asso_Model:

    pass