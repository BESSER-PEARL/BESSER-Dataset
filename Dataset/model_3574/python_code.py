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

class Expression:

    pass
class Predicate:

    pass
class expression_PredicateLikeOperator(Predicate):

    pass
class expression_PredicateIsOperator(Predicate):

    pass
class expression_PredicateEqualityOperator(Predicate):

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

class expression_PredicateIsEmpty(Predicate):

    pass
class expression_PredicateInOperator(Predicate):

    pass
class expression_PredicateIsNull(Predicate):

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

class expression_Variable(Expression):

    pass
class Literal:

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

class expression_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
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

class expression_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expression_NullLiteral(Literal):

    pass
class expression_Literal(Expression):

    pass
class expression_Expression(ABC):

    def __init__(self, suffixes: str, expression_Expression: "expression_PredicateEqualityOperator" = None, expression_Expression4: "expression_PredicateEqualityOperator" = None, expression_Expression6: "expression_PredicateComparisonOperator" = None, expression_Expression9: "expression_PredicateComparisonOperator" = None, expression_Expression11: "expression_PredicateInOperator" = None, expression_Expression14: "expression_PredicateInOperator" = None, expression_Expression19: "expression_PredicateIsOperator" = None, expression_Expression21: "expression_PredicateLikeOperator" = None, expression_Expression24: "expression_PredicateLikeOperator" = None, expression_Expression16: "expression_PredicateIsOperator" = None):
        self.suffixes = suffixes
        self.expression_Expression = expression_Expression
        self.expression_Expression4 = expression_Expression4
        self.expression_Expression6 = expression_Expression6
        self.expression_Expression9 = expression_Expression9
        self.expression_Expression11 = expression_Expression11
        self.expression_Expression14 = expression_Expression14
        self.expression_Expression19 = expression_Expression19
        self.expression_Expression21 = expression_Expression21
        self.expression_Expression24 = expression_Expression24
        self.expression_Expression16 = expression_Expression16
        
    @property
    def suffixes(self) -> str:
        return self.__suffixes

    @suffixes.setter
    def suffixes(self, suffixes: str):
        self.__suffixes = suffixes

    @property
    def expression_Expression(self):
        return self.__expression_Expression

    @expression_Expression.setter
    def expression_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression", None)
        self.__expression_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateEqualityOperator"):
                opp_val = getattr(old_value, "expression_PredicateEqualityOperator", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateEqualityOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateEqualityOperator"):
                opp_val = getattr(value, "expression_PredicateEqualityOperator", None)
                setattr(value, "expression_PredicateEqualityOperator", self)

    @property
    def expression_Expression6(self):
        return self.__expression_Expression6

    @expression_Expression6.setter
    def expression_Expression6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression6", None)
        self.__expression_Expression6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateComparisonOperator"):
                opp_val = getattr(old_value, "expression_PredicateComparisonOperator", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateComparisonOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateComparisonOperator"):
                opp_val = getattr(value, "expression_PredicateComparisonOperator", None)
                setattr(value, "expression_PredicateComparisonOperator", self)

    @property
    def expression_Expression9(self):
        return self.__expression_Expression9

    @expression_Expression9.setter
    def expression_Expression9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression9", None)
        self.__expression_Expression9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateComparisonOperator8"):
                opp_val = getattr(old_value, "expression_PredicateComparisonOperator8", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateComparisonOperator8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateComparisonOperator8"):
                opp_val = getattr(value, "expression_PredicateComparisonOperator8", None)
                setattr(value, "expression_PredicateComparisonOperator8", self)

    @property
    def expression_Expression24(self):
        return self.__expression_Expression24

    @expression_Expression24.setter
    def expression_Expression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression24", None)
        self.__expression_Expression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateLikeOperator23"):
                opp_val = getattr(old_value, "expression_PredicateLikeOperator23", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateLikeOperator23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateLikeOperator23"):
                opp_val = getattr(value, "expression_PredicateLikeOperator23", None)
                setattr(value, "expression_PredicateLikeOperator23", self)

    @property
    def expression_Expression19(self):
        return self.__expression_Expression19

    @expression_Expression19.setter
    def expression_Expression19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression19", None)
        self.__expression_Expression19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateIsOperator18"):
                opp_val = getattr(old_value, "expression_PredicateIsOperator18", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateIsOperator18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateIsOperator18"):
                opp_val = getattr(value, "expression_PredicateIsOperator18", None)
                setattr(value, "expression_PredicateIsOperator18", self)

    @property
    def expression_Expression11(self):
        return self.__expression_Expression11

    @expression_Expression11.setter
    def expression_Expression11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression11", None)
        self.__expression_Expression11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateInOperator"):
                opp_val = getattr(old_value, "expression_PredicateInOperator", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateInOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateInOperator"):
                opp_val = getattr(value, "expression_PredicateInOperator", None)
                setattr(value, "expression_PredicateInOperator", self)

    @property
    def expression_Expression21(self):
        return self.__expression_Expression21

    @expression_Expression21.setter
    def expression_Expression21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression21", None)
        self.__expression_Expression21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateLikeOperator"):
                opp_val = getattr(old_value, "expression_PredicateLikeOperator", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateLikeOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateLikeOperator"):
                opp_val = getattr(value, "expression_PredicateLikeOperator", None)
                setattr(value, "expression_PredicateLikeOperator", self)

    @property
    def expression_Expression14(self):
        return self.__expression_Expression14

    @expression_Expression14.setter
    def expression_Expression14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression14", None)
        self.__expression_Expression14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateInOperator13"):
                opp_val = getattr(old_value, "expression_PredicateInOperator13", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateInOperator13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateInOperator13"):
                opp_val = getattr(value, "expression_PredicateInOperator13", None)
                setattr(value, "expression_PredicateInOperator13", self)

    @property
    def expression_Expression16(self):
        return self.__expression_Expression16

    @expression_Expression16.setter
    def expression_Expression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression16", None)
        self.__expression_Expression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateIsOperator"):
                opp_val = getattr(old_value, "expression_PredicateIsOperator", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateIsOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateIsOperator"):
                opp_val = getattr(value, "expression_PredicateIsOperator", None)
                setattr(value, "expression_PredicateIsOperator", self)

    @property
    def expression_Expression4(self):
        return self.__expression_Expression4

    @expression_Expression4.setter
    def expression_Expression4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression4", None)
        self.__expression_Expression4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateEqualityOperator3"):
                opp_val = getattr(old_value, "expression_PredicateEqualityOperator3", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateEqualityOperator3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateEqualityOperator3"):
                opp_val = getattr(value, "expression_PredicateEqualityOperator3", None)
                setattr(value, "expression_PredicateEqualityOperator3", self)
