from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AbstractDefinition:

    pass
class arithmetic_DeclaredParameter(AbstractDefinition):

    pass
class Statement:

    pass
class arithmetic_Definition(AbstractDefinition, Statement):

    pass
class arithmetic_Statement:

    pass
class arithmetic_Import:

    pass
class arithmetic_Module:

    def __init__(self, name: str, arithmetic_Module: set["arithmetic_Import"] = None, arithmetic_Module2: set["arithmetic_Statement"] = None, arithmetic_Module5: "arithmetic_Import" = None):
        self.name = name
        self.arithmetic_Module = arithmetic_Module if arithmetic_Module is not None else set()
        self.arithmetic_Module2 = arithmetic_Module2 if arithmetic_Module2 is not None else set()
        self.arithmetic_Module5 = arithmetic_Module5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arithmetic_Module(self):
        return self.__arithmetic_Module

    @arithmetic_Module.setter
    def arithmetic_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetic_Module__arithmetic_Module", None)
        self.__arithmetic_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arithmetic_Import"):
                    opp_val = getattr(item, "arithmetic_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "arithmetic_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arithmetic_Import"):
                    opp_val = getattr(item, "arithmetic_Import", None)
                    
                    setattr(item, "arithmetic_Import", self)
                    

    @property
    def arithmetic_Module2(self):
        return self.__arithmetic_Module2

    @arithmetic_Module2.setter
    def arithmetic_Module2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetic_Module__arithmetic_Module2", None)
        self.__arithmetic_Module2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arithmetic_Statement"):
                    opp_val = getattr(item, "arithmetic_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "arithmetic_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arithmetic_Statement"):
                    opp_val = getattr(item, "arithmetic_Statement", None)
                    
                    setattr(item, "arithmetic_Statement", self)
                    

    @property
    def arithmetic_Module5(self):
        return self.__arithmetic_Module5

    @arithmetic_Module5.setter
    def arithmetic_Module5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetic_Module__arithmetic_Module5", None)
        self.__arithmetic_Module5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arithmetic_Import4"):
                opp_val = getattr(old_value, "arithmetic_Import4", None)
                if opp_val == self:
                    setattr(old_value, "arithmetic_Import4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arithmetic_Import4"):
                opp_val = getattr(value, "arithmetic_Import4", None)
                setattr(value, "arithmetic_Import4", self)

class Expression:

    pass
class arithmetic_Plus(Expression):

    pass
class arithmetic_FunctionCall(Expression):

    pass
class arithmetic_Minus(Expression):

    pass
class arithmetic_Div(Expression):

    pass
class arithmetic_NumberLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class arithmetic_Multi(Expression):

    pass
class arithmetic_SumExpression(Expression):

    def __init__(self, lower: int, upper: int, arithmetic_SumExpression: "arithmetic_DeclaredParameter" = None, arithmetic_SumExpression14: "arithmetic_Expression" = None):
        self.lower = lower
        self.upper = upper
        self.arithmetic_SumExpression = arithmetic_SumExpression
        self.arithmetic_SumExpression14 = arithmetic_SumExpression14
        
    @property
    def upper(self) -> int:
        return self.__upper

    @upper.setter
    def upper(self, upper: int):
        self.__upper = upper

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def arithmetic_SumExpression(self):
        return self.__arithmetic_SumExpression

    @arithmetic_SumExpression.setter
    def arithmetic_SumExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetic_SumExpression__arithmetic_SumExpression", None)
        self.__arithmetic_SumExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arithmetic_DeclaredParameter12"):
                opp_val = getattr(old_value, "arithmetic_DeclaredParameter12", None)
                if opp_val == self:
                    setattr(old_value, "arithmetic_DeclaredParameter12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arithmetic_DeclaredParameter12"):
                opp_val = getattr(value, "arithmetic_DeclaredParameter12", None)
                setattr(value, "arithmetic_DeclaredParameter12", self)

    @property
    def arithmetic_SumExpression14(self):
        return self.__arithmetic_SumExpression14

    @arithmetic_SumExpression14.setter
    def arithmetic_SumExpression14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetic_SumExpression__arithmetic_SumExpression14", None)
        self.__arithmetic_SumExpression14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arithmetic_Expression15"):
                opp_val = getattr(old_value, "arithmetic_Expression15", None)
                if opp_val == self:
                    setattr(old_value, "arithmetic_Expression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arithmetic_Expression15"):
                opp_val = getattr(value, "arithmetic_Expression15", None)
                setattr(value, "arithmetic_Expression15", self)

class arithmetic_Evaluation(Statement):

    pass
class arithmetic_AbstractDefinition:

    def __init__(self, name: str, arithmetic_AbstractDefinition: "arithmetic_FunctionCall" = None):
        self.name = name
        self.arithmetic_AbstractDefinition = arithmetic_AbstractDefinition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arithmetic_AbstractDefinition(self):
        return self.__arithmetic_AbstractDefinition

    @arithmetic_AbstractDefinition.setter
    def arithmetic_AbstractDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arithmetic_AbstractDefinition__arithmetic_AbstractDefinition", None)
        self.__arithmetic_AbstractDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arithmetic_FunctionCall"):
                opp_val = getattr(old_value, "arithmetic_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "arithmetic_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arithmetic_FunctionCall"):
                opp_val = getattr(value, "arithmetic_FunctionCall", None)
                setattr(value, "arithmetic_FunctionCall", self)

class arithmetic_Expression:

    pass