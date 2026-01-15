from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanOperator(Enum):
    And = "And"
    Or = "Or"
class ComparisionOperator(Enum):
    GreaterThan = "GreaterThan"
    LessThan = "LessThan"


############################################
# Definition of Classes
############################################

class Predicate:

    pass
class expression_PredicateIsNull(Predicate):

    pass
class expression_PredicateLikeOperator(Predicate):

    pass
class expression_PredicateEqualityOperator(Predicate):

    pass
class expression_PredicateIsEmpty(Predicate):

    pass
class expression_PredicateIsOperator(Predicate):

    pass
class expression_PredicateComparisonOperator(Predicate):

    def __init__(self, operator: str, expression_PredicateComparisonOperator: "expression_Expression" = None, expression_PredicateComparisonOperator10: "expression_Expression" = None):
        self.operator = operator
        self.expression_PredicateComparisonOperator = expression_PredicateComparisonOperator
        self.expression_PredicateComparisonOperator10 = expression_PredicateComparisonOperator10
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

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
            if hasattr(old_value, "expression_Expression8"):
                opp_val = getattr(old_value, "expression_Expression8", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression8"):
                opp_val = getattr(value, "expression_Expression8", None)
                setattr(value, "expression_Expression8", self)

    @property
    def expression_PredicateComparisonOperator10(self):
        return self.__expression_PredicateComparisonOperator10

    @expression_PredicateComparisonOperator10.setter
    def expression_PredicateComparisonOperator10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_PredicateComparisonOperator__expression_PredicateComparisonOperator10", None)
        self.__expression_PredicateComparisonOperator10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression11"):
                opp_val = getattr(old_value, "expression_Expression11", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression11"):
                opp_val = getattr(value, "expression_Expression11", None)
                setattr(value, "expression_Expression11", self)

class expression_PredicateInOperator(Predicate):

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

class expression_TimeLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
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
class Expression:

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

class expression_Variable(Expression):

    pass
class expression_Literal(Expression):

    pass
class expression_EObject:

    pass
class expression_Expression(ABC):

    def __init__(self, suffixes: str, expression_Expression: "expression_EObject" = None, expression_Expression3: "expression_PredicateEqualityOperator" = None, expression_Expression8: "expression_PredicateComparisonOperator" = None, expression_Expression11: "expression_PredicateComparisonOperator" = None, expression_Expression13: "expression_PredicateInOperator" = None, expression_Expression16: "expression_PredicateInOperator" = None, expression_Expression18: "expression_PredicateIsOperator" = None, expression_Expression21: "expression_PredicateIsOperator" = None, expression_Expression6: "expression_PredicateEqualityOperator" = None, expression_Expression23: "expression_PredicateLikeOperator" = None, expression_Expression26: "expression_PredicateLikeOperator" = None):
        self.suffixes = suffixes
        self.expression_Expression = expression_Expression
        self.expression_Expression3 = expression_Expression3
        self.expression_Expression8 = expression_Expression8
        self.expression_Expression11 = expression_Expression11
        self.expression_Expression13 = expression_Expression13
        self.expression_Expression16 = expression_Expression16
        self.expression_Expression18 = expression_Expression18
        self.expression_Expression21 = expression_Expression21
        self.expression_Expression6 = expression_Expression6
        self.expression_Expression23 = expression_Expression23
        self.expression_Expression26 = expression_Expression26
        
    @property
    def suffixes(self) -> str:
        return self.__suffixes

    @suffixes.setter
    def suffixes(self, suffixes: str):
        self.__suffixes = suffixes

    @property
    def expression_Expression26(self):
        return self.__expression_Expression26

    @expression_Expression26.setter
    def expression_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression26", None)
        self.__expression_Expression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateLikeOperator25"):
                opp_val = getattr(old_value, "expression_PredicateLikeOperator25", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateLikeOperator25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateLikeOperator25"):
                opp_val = getattr(value, "expression_PredicateLikeOperator25", None)
                setattr(value, "expression_PredicateLikeOperator25", self)

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
            if hasattr(old_value, "expression_PredicateComparisonOperator10"):
                opp_val = getattr(old_value, "expression_PredicateComparisonOperator10", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateComparisonOperator10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateComparisonOperator10"):
                opp_val = getattr(value, "expression_PredicateComparisonOperator10", None)
                setattr(value, "expression_PredicateComparisonOperator10", self)

    @property
    def expression_Expression18(self):
        return self.__expression_Expression18

    @expression_Expression18.setter
    def expression_Expression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression18", None)
        self.__expression_Expression18 = value
        
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
    def expression_Expression6(self):
        return self.__expression_Expression6

    @expression_Expression6.setter
    def expression_Expression6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression6", None)
        self.__expression_Expression6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_PredicateEqualityOperator5"):
                opp_val = getattr(old_value, "expression_PredicateEqualityOperator5", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateEqualityOperator5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateEqualityOperator5"):
                opp_val = getattr(value, "expression_PredicateEqualityOperator5", None)
                setattr(value, "expression_PredicateEqualityOperator5", self)

    @property
    def expression_Expression3(self):
        return self.__expression_Expression3

    @expression_Expression3.setter
    def expression_Expression3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression3", None)
        self.__expression_Expression3 = value
        
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
    def expression_Expression13(self):
        return self.__expression_Expression13

    @expression_Expression13.setter
    def expression_Expression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression13", None)
        self.__expression_Expression13 = value
        
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
            if hasattr(old_value, "expression_PredicateIsOperator20"):
                opp_val = getattr(old_value, "expression_PredicateIsOperator20", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateIsOperator20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateIsOperator20"):
                opp_val = getattr(value, "expression_PredicateIsOperator20", None)
                setattr(value, "expression_PredicateIsOperator20", self)

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
            if hasattr(old_value, "expression_PredicateInOperator15"):
                opp_val = getattr(old_value, "expression_PredicateInOperator15", None)
                if opp_val == self:
                    setattr(old_value, "expression_PredicateInOperator15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_PredicateInOperator15"):
                opp_val = getattr(value, "expression_PredicateInOperator15", None)
                setattr(value, "expression_PredicateInOperator15", self)

    @property
    def expression_Expression8(self):
        return self.__expression_Expression8

    @expression_Expression8.setter
    def expression_Expression8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression8", None)
        self.__expression_Expression8 = value
        
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
    def expression_Expression23(self):
        return self.__expression_Expression23

    @expression_Expression23.setter
    def expression_Expression23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression23", None)
        self.__expression_Expression23 = value
        
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
    def expression_Expression(self):
        return self.__expression_Expression

    @expression_Expression.setter
    def expression_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression", None)
        self.__expression_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_EObject"):
                opp_val = getattr(old_value, "expression_EObject", None)
                if opp_val == self:
                    setattr(old_value, "expression_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_EObject"):
                opp_val = getattr(value, "expression_EObject", None)
                setattr(value, "expression_EObject", self)
