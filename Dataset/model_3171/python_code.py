from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

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

class expressions_MulOrDiv(Expression):

    def __init__(self, op: str, expressions_MulOrDiv: "expressions_Expression" = None, expressions_MulOrDiv35: "expressions_Expression" = None):
        self.op = op
        self.expressions_MulOrDiv = expressions_MulOrDiv
        self.expressions_MulOrDiv35 = expressions_MulOrDiv35
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

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
            if hasattr(old_value, "expressions_Expression33"):
                opp_val = getattr(old_value, "expressions_Expression33", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression33"):
                opp_val = getattr(value, "expressions_Expression33", None)
                setattr(value, "expressions_Expression33", self)

    @property
    def expressions_MulOrDiv35(self):
        return self.__expressions_MulOrDiv35

    @expressions_MulOrDiv35.setter
    def expressions_MulOrDiv35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_MulOrDiv__expressions_MulOrDiv35", None)
        self.__expressions_MulOrDiv35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression36"):
                opp_val = getattr(old_value, "expressions_Expression36", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression36"):
                opp_val = getattr(value, "expressions_Expression36", None)
                setattr(value, "expressions_Expression36", self)

class expressions_Plus(Expression):

    pass
class expressions_StringConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_Not(Expression):

    pass
class expressions_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_Equality(Expression):

    def __init__(self, op: str, expressions_Equality: "expressions_Expression" = None, expressions_Equality15: "expressions_Expression" = None):
        self.op = op
        self.expressions_Equality = expressions_Equality
        self.expressions_Equality15 = expressions_Equality15
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

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
            if hasattr(old_value, "expressions_Expression13"):
                opp_val = getattr(old_value, "expressions_Expression13", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression13"):
                opp_val = getattr(value, "expressions_Expression13", None)
                setattr(value, "expressions_Expression13", self)

    @property
    def expressions_Equality15(self):
        return self.__expressions_Equality15

    @expressions_Equality15.setter
    def expressions_Equality15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Equality__expressions_Equality15", None)
        self.__expressions_Equality15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression16"):
                opp_val = getattr(old_value, "expressions_Expression16", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression16"):
                opp_val = getattr(value, "expressions_Expression16", None)
                setattr(value, "expressions_Expression16", self)

class expressions_VariableRef(Expression):

    pass
class expressions_And(Expression):

    pass
class expressions_Comparison(Expression):

    def __init__(self, op: str, expressions_Comparison: "expressions_Expression" = None, expressions_Comparison20: "expressions_Expression" = None):
        self.op = op
        self.expressions_Comparison = expressions_Comparison
        self.expressions_Comparison20 = expressions_Comparison20
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def expressions_Comparison20(self):
        return self.__expressions_Comparison20

    @expressions_Comparison20.setter
    def expressions_Comparison20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Comparison__expressions_Comparison20", None)
        self.__expressions_Comparison20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression21"):
                opp_val = getattr(old_value, "expressions_Expression21", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression21"):
                opp_val = getattr(value, "expressions_Expression21", None)
                setattr(value, "expressions_Expression21", self)

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
            if hasattr(old_value, "expressions_Expression18"):
                opp_val = getattr(old_value, "expressions_Expression18", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression18"):
                opp_val = getattr(value, "expressions_Expression18", None)
                setattr(value, "expressions_Expression18", self)

class expressions_Or(Expression):

    pass
class AbstractElement:

    pass
class expressions_Expression(AbstractElement):

    pass
class expressions_Variable(AbstractElement):

    def __init__(self, name: str, expressions_Variable: "expressions_Expression" = None, expressions_Variable40: "expressions_VariableRef" = None):
        self.name = name
        self.expressions_Variable = expressions_Variable
        self.expressions_Variable40 = expressions_Variable40
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressions_Variable40(self):
        return self.__expressions_Variable40

    @expressions_Variable40.setter
    def expressions_Variable40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Variable__expressions_Variable40", None)
        self.__expressions_Variable40 = value
        
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
            if hasattr(old_value, "expressions_Expression"):
                opp_val = getattr(old_value, "expressions_Expression", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression"):
                opp_val = getattr(value, "expressions_Expression", None)
                setattr(value, "expressions_Expression", self)

class expressions_AbstractElement:

    pass
class expressions_ExpressionsModel:

    pass