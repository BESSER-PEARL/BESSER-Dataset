from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComparisionOperator(Enum):
    GreaterThan = "GreaterThan"
    LessThan = "LessThan"
class BooleanOperator(Enum):
    And = "And"
    Or = "Or"


############################################
# Definition of Classes
############################################

class Predicate:

    pass
class expression_PredicateEqualityOperator(Predicate):

    pass
class expression_PredicateIsEmpty(Predicate):

    pass
class expression_PredicateComparisonOperator(Predicate):

    def __init__(self, operator: str, expression_PredicateComparisonOperator: "expression_Expression" = None, expression_PredicateComparisonOperator8: "expression_Expression" = None):
        self.operator = operator
        self.expression_PredicateComparisonOperator = expression_PredicateComparisonOperator
        self.expression_PredicateComparisonOperator8 = expression_PredicateComparisonOperator8
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def expression_PredicateComparisonOperator8(self):
        return self.__expression_PredicateComparisonOperator8

    @expression_PredicateComparisonOperator8.setter
    def expression_PredicateComparisonOperator8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_PredicateComparisonOperator__expression_PredicateComparisonOperator8", None)
        self.__expression_PredicateComparisonOperator8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression9"):
                opp_val = getattr(old_value, "expression_Expression9", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression9"):
                opp_val = getattr(value, "expression_Expression9", None)
                setattr(value, "expression_Expression9", self)

    @property
    def expression_PredicateComparisonOperator(self):
        return self.__expression_PredicateComparisonOperator

    @expression_PredicateComparisonOperator.setter
    def expression_PredicateComparisonOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_PredicateComparisonOperator__expression_PredicateComparisonOperator", None)
        self.__expression_PredicateComparisonOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression6"):
                opp_val = getattr(old_value, "expression_Expression6", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression6"):
                opp_val = getattr(value, "expression_Expression6", None)
                setattr(value, "expression_Expression6", self)

class expression_PredicateIsNull(Predicate):

    pass
class expression_PredicateLikeOperator(Predicate):

    pass
class expression_PredicateIsOperator(Predicate):

    pass
class expression_PredicateBooleanOperator(Predicate):

    def __init__(self, operator: str, expression_PredicateBooleanOperator: set["expression_Predicate"] = None):
        self.operator = operator
        self.expression_PredicateBooleanOperator = expression_PredicateBooleanOperator if expression_PredicateBooleanOperator is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def expression_PredicateBooleanOperator(self):
        return self.__expression_PredicateBooleanOperator

    @expression_PredicateBooleanOperator.setter
    def expression_PredicateBooleanOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_PredicateBooleanOperator__expression_PredicateBooleanOperator", None)
        self.__expression_PredicateBooleanOperator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "expression_Predicate"):
                    opp_val = getattr(item, "expression_Predicate", None)
                    
                    if opp_val == self:
                        setattr(item, "expression_Predicate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "expression_Predicate"):
                    opp_val = getattr(item, "expression_Predicate", None)
                    
                    setattr(item, "expression_Predicate", self)
                    

class Literal:

    pass
class expression_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expression_IntegerLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expression_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class expression_NullLiteral(Literal):

    pass
class Expression:

    pass
class expression_Function(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class expression_Variable(Expression):

    pass
class expression_Predicate(Expression):

    def __init__(self, negated: bool, expression_Predicate: "expression_PredicateBooleanOperator" = None):
        self.negated = negated
        self.expression_Predicate = expression_Predicate
        
    @property
    def negated(self) -> bool:
        return self.__negated

    @negated.setter
    def negated(self, negated: bool):
        self.__negated = negated

    @property
    def expression_Predicate(self):
        return self.__expression_Predicate

    @expression_Predicate.setter
    def expression_Predicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Predicate__expression_Predicate", None)
        self.__expression_Predicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateBooleanOperator"):
                opp_val = getattr(old_value, "expression_PredicateBooleanOperator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateBooleanOperator"):
                opp_val = getattr(value, "expression_PredicateBooleanOperator", None)
                if opp_val is None:
                    setattr(value, "expression_PredicateBooleanOperator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class expression_Literal(Expression):

    pass
class expression_TimeLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expression_Expression(ABC):

    pass