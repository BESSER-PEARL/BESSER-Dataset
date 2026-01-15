from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class expressions_Comparison(Expression):

    def __init__(self, op: str, expressions_Comparison: "expressions_Expression" = None, expressions_Comparison21: "expressions_Expression" = None):
        self.op = op
        self.expressions_Comparison = expressions_Comparison
        self.expressions_Comparison21 = expressions_Comparison21
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expressions_Comparison(self):
        return self.__expressions_Comparison

    @expressions_Comparison.setter
    def expressions_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Comparison__expressions_Comparison", None)
        self.__expressions_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression19"):
                opp_val = getattr(old_value, "expressions_Expression19", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression19"):
                opp_val = getattr(value, "expressions_Expression19", None)
                setattr(value, "expressions_Expression19", self)

    @property
    def expressions_Comparison21(self):
        return self.__expressions_Comparison21

    @expressions_Comparison21.setter
    def expressions_Comparison21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Comparison__expressions_Comparison21", None)
        self.__expressions_Comparison21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression22"):
                opp_val = getattr(old_value, "expressions_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression22"):
                opp_val = getattr(value, "expressions_Expression22", None)
                setattr(value, "expressions_Expression22", self)

class expressions_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_MulOrDiv(Expression):

    def __init__(self, op: str, expressions_MulOrDiv: "expressions_Expression" = None, expressions_MulOrDiv36: "expressions_Expression" = None):
        self.op = op
        self.expressions_MulOrDiv = expressions_MulOrDiv
        self.expressions_MulOrDiv36 = expressions_MulOrDiv36
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expressions_MulOrDiv36(self):
        return self.__expressions_MulOrDiv36

    @expressions_MulOrDiv36.setter
    def expressions_MulOrDiv36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_MulOrDiv__expressions_MulOrDiv36", None)
        self.__expressions_MulOrDiv36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression37"):
                opp_val = getattr(old_value, "expressions_Expression37", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression37"):
                opp_val = getattr(value, "expressions_Expression37", None)
                setattr(value, "expressions_Expression37", self)

    @property
    def expressions_MulOrDiv(self):
        return self.__expressions_MulOrDiv

    @expressions_MulOrDiv.setter
    def expressions_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_MulOrDiv__expressions_MulOrDiv", None)
        self.__expressions_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression34"):
                opp_val = getattr(old_value, "expressions_Expression34", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression34"):
                opp_val = getattr(value, "expressions_Expression34", None)
                setattr(value, "expressions_Expression34", self)

class expressions_VariableRef(Expression):

    pass
class expressions_Plus(Expression):

    pass
class expressions_Minus(Expression):

    pass
class expressions_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expressions_Not(Expression):

    pass
class expressions_Or(Expression):

    pass
class AbstractElement:

    pass
class expressions_EvalExpression(AbstractElement):

    pass
class expressions_Variable(AbstractElement):

    def __init__(self, name: str, expressions_Variable: "expressions_VariableRef" = None):
        self.name = name
        self.expressions_Variable = expressions_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressions_Variable(self):
        return self.__expressions_Variable

    @expressions_Variable.setter
    def expressions_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Variable__expressions_Variable", None)
        self.__expressions_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_VariableRef"):
                opp_val = getattr(old_value, "expressions_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "expressions_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_VariableRef"):
                opp_val = getattr(value, "expressions_VariableRef", None)
                setattr(value, "expressions_VariableRef", self)

class expressions_Expression:

    pass
class expressions_AbstractElement:

    pass
class expressions_Equality(Expression):

    def __init__(self, op: str, expressions_Equality: "expressions_Expression" = None, expressions_Equality16: "expressions_Expression" = None):
        self.op = op
        self.expressions_Equality = expressions_Equality
        self.expressions_Equality16 = expressions_Equality16
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expressions_Equality16(self):
        return self.__expressions_Equality16

    @expressions_Equality16.setter
    def expressions_Equality16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Equality__expressions_Equality16", None)
        self.__expressions_Equality16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression17"):
                opp_val = getattr(old_value, "expressions_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression17"):
                opp_val = getattr(value, "expressions_Expression17", None)
                setattr(value, "expressions_Expression17", self)

    @property
    def expressions_Equality(self):
        return self.__expressions_Equality

    @expressions_Equality.setter
    def expressions_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Equality__expressions_Equality", None)
        self.__expressions_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression14"):
                opp_val = getattr(old_value, "expressions_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression14"):
                opp_val = getattr(value, "expressions_Expression14", None)
                setattr(value, "expressions_Expression14", self)

class expressions_And(Expression):

    pass
class expressions_ExpressionsModel:

    pass