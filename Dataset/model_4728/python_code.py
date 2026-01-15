from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UnaryExpression:

    pass
class prolog_expressions_BitwiseNegation(UnaryExpression):

    pass
class prolog_expressions_PositiveNumber(UnaryExpression):

    pass
class prolog_expressions_NegativeNumber(UnaryExpression):

    pass
class prolog_expressions_NotProvable(UnaryExpression):

    pass
class BinaryExpression:

    pass
class prolog_expressions_ParticalUnification(BinaryExpression):

    pass
class prolog_expressions_Rem(BinaryExpression):

    pass
class prolog_expressions_EqualOrStandardOrderAfter(BinaryExpression):

    pass
class prolog_expressions_StandardOrderAfter(BinaryExpression):

    pass
class prolog_expressions_Multiplication(BinaryExpression):

    pass
class prolog_expressions_StandardOrderBefore(BinaryExpression):

    pass
class prolog_expressions_As(BinaryExpression):

    pass
class prolog_expressions_Div(BinaryExpression):

    pass
class prolog_expressions_NotUnifiable(BinaryExpression):

    pass
class prolog_expressions_Plus(BinaryExpression):

    pass
class prolog_expressions_Univ(BinaryExpression):

    pass
class prolog_expressions_BitwiseShiftLeft(BinaryExpression):

    pass
class prolog_expressions_LogicalAnd(BinaryExpression):

    pass
class prolog_expressions_GreaterOrEqual(BinaryExpression):

    pass
class prolog_expressions_IntegerDivision(BinaryExpression):

    pass
class prolog_expressions_Power(BinaryExpression):

    pass
class prolog_expressions_Mod(BinaryExpression):

    pass
class prolog_expressions_Division(BinaryExpression):

    pass
class prolog_expressions_Disequality(BinaryExpression):

    pass
class prolog_expressions_LessThan(BinaryExpression):

    pass
class prolog_expressions_Is(BinaryExpression):

    pass
class prolog_expressions_Unification(BinaryExpression):

    pass
class prolog_expressions_ModuleCall(BinaryExpression):

    pass
class prolog_expressions_StructuralEquivalence(BinaryExpression):

    pass
class prolog_expressions_EqualOrStandardOrderBefore(BinaryExpression):

    pass
class prolog_expressions_Rdiv(BinaryExpression):

    pass
class prolog_expressions_BinaryOr(BinaryExpression):

    pass
class prolog_expressions_SubDict(BinaryExpression):

    pass
class prolog_expressions_SoftCut(BinaryExpression):

    pass
class prolog_expressions_Minus(BinaryExpression):

    pass
class prolog_expressions_Condition(BinaryExpression):

    pass
class prolog_expressions_BinaryAnd(BinaryExpression):

    pass
class prolog_expressions_Xor(BinaryExpression):

    pass
class prolog_expressions_LogicalOr(BinaryExpression):

    pass
class prolog_expressions_Expression(ABC):

    pass
class prolog_expressions_GreaterThan(BinaryExpression):

    pass
class prolog_expressions_NonEqualNumber(BinaryExpression):

    pass
class prolog_expressions_Equivalence(BinaryExpression):

    pass
class prolog_expressions_LessOrEqual(BinaryExpression):

    pass
class prolog_expressions_NumberEqual(BinaryExpression):

    pass
class prolog_expressions_StructuralEquivalenceNotProvable(BinaryExpression):

    pass
class PredicateIndicator:

    pass
class ControlPredicate:

    pass
class prolog_False(ControlPredicate):

    pass
class prolog_Cut(ControlPredicate):

    pass
class prolog_Fail(ControlPredicate):

    pass
class prolog_True(ControlPredicate):

    pass
class Directive:

    pass
class prolog_directives_Public(Directive):

    pass
class prolog_directives_Volatile(Directive):

    pass
class prolog_directives_Multifile(Directive):

    pass
class prolog_directives_Discontiguous(Directive):

    pass
class prolog_directives_Dynamic(Directive):

    pass
class prolog_directives_PredicateIndicator:

    def __init__(self, name: str, arity: int):
        self.name = name
        self.arity = arity
        
    @property
    def arity(self) -> int:
        return self.__arity

    @arity.setter
    def arity(self, arity: int):
        self.__arity = arity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Clause:

    pass
class prolog_Rule(Clause):

    pass
class prolog_directives_Directive(Clause):

    def __init__(self, name: str, prolog_directives_Directive: set["PredicateIndicator"] = None):
        self.name = name
        self.prolog_directives_Directive = prolog_directives_Directive if prolog_directives_Directive is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def prolog_directives_Directive(self):
        return self.__prolog_directives_Directive

    @prolog_directives_Directive.setter
    def prolog_directives_Directive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_directives_Directive__prolog_directives_Directive", None)
        self.__prolog_directives_Directive = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PredicateIndicator"):
                    opp_val = getattr(item, "PredicateIndicator", None)
                    
                    if opp_val == self:
                        setattr(item, "PredicateIndicator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PredicateIndicator"):
                    opp_val = getattr(item, "PredicateIndicator", None)
                    
                    setattr(item, "PredicateIndicator", self)
                    

class prolog_directives_Table(Clause):

    pass
class prolog_Fact(Clause):

    pass
class prolog_Comment(Clause):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class prolog_Clause(ABC):

    pass
class prolog_Program:

    pass
class Term:

    pass
class prolog_AtomicQuotedString(Term):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class prolog_List(Term):

    pass
class prolog_AtomicNumber(Term):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class prolog_ControlPredicate(Term):

    pass
class prolog_CompoundTerm(Term, Clause):

    def __init__(self, value: str, prolog_CompoundTerm: set["Expression"] = None, prolog_CompoundTerm8: "prolog_Fact" = None, prolog_CompoundTerm10: "prolog_Rule" = None):
        self.value = value
        self.prolog_CompoundTerm = prolog_CompoundTerm if prolog_CompoundTerm is not None else set()
        self.prolog_CompoundTerm8 = prolog_CompoundTerm8
        self.prolog_CompoundTerm10 = prolog_CompoundTerm10
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def prolog_CompoundTerm8(self):
        return self.__prolog_CompoundTerm8

    @prolog_CompoundTerm8.setter
    def prolog_CompoundTerm8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_CompoundTerm__prolog_CompoundTerm8", None)
        self.__prolog_CompoundTerm8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Fact"):
                opp_val = getattr(old_value, "prolog_Fact", None)
                if opp_val == self:
                    setattr(old_value, "prolog_Fact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Fact"):
                opp_val = getattr(value, "prolog_Fact", None)
                setattr(value, "prolog_Fact", self)

    @property
    def prolog_CompoundTerm(self):
        return self.__prolog_CompoundTerm

    @prolog_CompoundTerm.setter
    def prolog_CompoundTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_CompoundTerm__prolog_CompoundTerm", None)
        self.__prolog_CompoundTerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression"):
                    opp_val = getattr(item, "Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression"):
                    opp_val = getattr(item, "Expression", None)
                    
                    setattr(item, "Expression", self)
                    

    @property
    def prolog_CompoundTerm10(self):
        return self.__prolog_CompoundTerm10

    @prolog_CompoundTerm10.setter
    def prolog_CompoundTerm10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_CompoundTerm__prolog_CompoundTerm10", None)
        self.__prolog_CompoundTerm10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Rule"):
                opp_val = getattr(old_value, "prolog_Rule", None)
                if opp_val == self:
                    setattr(old_value, "prolog_Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Rule"):
                opp_val = getattr(value, "prolog_Rule", None)
                setattr(value, "prolog_Rule", self)

class Expression:

    pass
class prolog_expressions_BinaryExpression(Expression):

    pass
class prolog_expressions_UnaryExpression(Expression):

    pass
class prolog_Term(Expression):

    pass