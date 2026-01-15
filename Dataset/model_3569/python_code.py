from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

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

class expressions_BoolConstant(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_IntConstant(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expressions_VariableRef(Expression):

    pass
class expressions_Plus(Expression):

    pass
class AbstractElement:

    pass
class expressions_Expression(AbstractElement):

    pass
class expressions_Variable(AbstractElement):

    def __init__(self, name: str, expressions_Variable: "expressions_Expression" = None, expressions_Variable8: "expressions_VariableRef" = None):
        self.name = name
        self.expressions_Variable = expressions_Variable
        self.expressions_Variable8 = expressions_Variable8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressions_Variable8(self):
        return self.__expressions_Variable8

    @expressions_Variable8.setter
    def expressions_Variable8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Variable__expressions_Variable8", None)
        self.__expressions_Variable8 = value
        
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

class expressions_ExpressionsModel:

    pass
class expressions_AbstractElement:

    pass