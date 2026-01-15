from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ADDITIVE_OPERATOR(Enum):
    plus = "plus"
    minus = "minus"
class MULTIPLICATIVE_OPERATOR(Enum):
    mult = "mult"
    div = "div"


############################################
# Definition of Classes
############################################

class Part:

    pass
class prolog_Tail(ABC):

    pass
class Tail:

    pass
class Term:

    pass
class prolog_Power(Term):

    pass
class prolog_Negation(Term):

    def __init__(self, operator: str, prolog_Negation: "prolog_Term" = None):
        self.operator = operator
        self.prolog_Negation = prolog_Negation
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def prolog_Negation(self):
        return self.__prolog_Negation

    @prolog_Negation.setter
    def prolog_Negation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Negation__prolog_Negation", None)
        self.__prolog_Negation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Term35"):
                opp_val = getattr(old_value, "prolog_Term35", None)
                if opp_val == self:
                    setattr(old_value, "prolog_Term35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Term35"):
                opp_val = getattr(value, "prolog_Term35", None)
                setattr(value, "prolog_Term35", self)

class prolog_Multiplicative(Term):

    def __init__(self, operator: str, prolog_Multiplicative: "prolog_Term" = None, prolog_Multiplicative27: "prolog_Term" = None):
        self.operator = operator
        self.prolog_Multiplicative = prolog_Multiplicative
        self.prolog_Multiplicative27 = prolog_Multiplicative27
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def prolog_Multiplicative(self):
        return self.__prolog_Multiplicative

    @prolog_Multiplicative.setter
    def prolog_Multiplicative(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Multiplicative__prolog_Multiplicative", None)
        self.__prolog_Multiplicative = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Term25"):
                opp_val = getattr(old_value, "prolog_Term25", None)
                if opp_val == self:
                    setattr(old_value, "prolog_Term25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Term25"):
                opp_val = getattr(value, "prolog_Term25", None)
                setattr(value, "prolog_Term25", self)

    @property
    def prolog_Multiplicative27(self):
        return self.__prolog_Multiplicative27

    @prolog_Multiplicative27.setter
    def prolog_Multiplicative27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Multiplicative__prolog_Multiplicative27", None)
        self.__prolog_Multiplicative27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Term28"):
                opp_val = getattr(old_value, "prolog_Term28", None)
                if opp_val == self:
                    setattr(old_value, "prolog_Term28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Term28"):
                opp_val = getattr(value, "prolog_Term28", None)
                setattr(value, "prolog_Term28", self)

class prolog_List(Tail, Term):

    pass
class prolog_BracketExpression(Term):

    pass
class prolog_Additive(Term):

    def __init__(self, operator: str, prolog_Additive: "prolog_Term" = None, prolog_Additive22: "prolog_Term" = None):
        self.operator = operator
        self.prolog_Additive = prolog_Additive
        self.prolog_Additive22 = prolog_Additive22
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def prolog_Additive22(self):
        return self.__prolog_Additive22

    @prolog_Additive22.setter
    def prolog_Additive22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Additive__prolog_Additive22", None)
        self.__prolog_Additive22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Term23"):
                opp_val = getattr(old_value, "prolog_Term23", None)
                if opp_val == self:
                    setattr(old_value, "prolog_Term23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Term23"):
                opp_val = getattr(value, "prolog_Term23", None)
                setattr(value, "prolog_Term23", self)

    @property
    def prolog_Additive(self):
        return self.__prolog_Additive

    @prolog_Additive.setter
    def prolog_Additive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Additive__prolog_Additive", None)
        self.__prolog_Additive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Term20"):
                opp_val = getattr(old_value, "prolog_Term20", None)
                if opp_val == self:
                    setattr(old_value, "prolog_Term20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Term20"):
                opp_val = getattr(value, "prolog_Term20", None)
                setattr(value, "prolog_Term20", self)

class prolog_String(Term):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class prolog_Variable(Tail, Term):

    def __init__(self, name: str, prolog_Variable: "prolog_VariableReference" = None):
        self.name = name
        self.prolog_Variable = prolog_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def prolog_Variable(self):
        return self.__prolog_Variable

    @prolog_Variable.setter
    def prolog_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Variable__prolog_Variable", None)
        self.__prolog_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_VariableReference"):
                opp_val = getattr(old_value, "prolog_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "prolog_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_VariableReference"):
                opp_val = getattr(value, "prolog_VariableReference", None)
                setattr(value, "prolog_VariableReference", self)

class prolog_Numeral(Term):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class prolog_Term(ABC):

    pass
class prolog_Conjunction:

    pass
class prolog_Part(ABC):

    pass
class prolog_Assignment(Part):

    pass
class prolog_AnonymousVariable(Term):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class prolog_VariableReference(Term):

    pass
class prolog_Predicate(Term, Part):

    def __init__(self, name: str, prolog_Predicate: "prolog_Clause" = None, prolog_Predicate9: set["prolog_Term"] = None):
        self.name = name
        self.prolog_Predicate = prolog_Predicate
        self.prolog_Predicate9 = prolog_Predicate9 if prolog_Predicate9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def prolog_Predicate9(self):
        return self.__prolog_Predicate9

    @prolog_Predicate9.setter
    def prolog_Predicate9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Predicate__prolog_Predicate9", None)
        self.__prolog_Predicate9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "prolog_Term10"):
                    opp_val = getattr(item, "prolog_Term10", None)
                    
                    if opp_val == self:
                        setattr(item, "prolog_Term10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "prolog_Term10"):
                    opp_val = getattr(item, "prolog_Term10", None)
                    
                    setattr(item, "prolog_Term10", self)
                    

    @property
    def prolog_Predicate(self):
        return self.__prolog_Predicate

    @prolog_Predicate.setter
    def prolog_Predicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prolog_Predicate__prolog_Predicate", None)
        self.__prolog_Predicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prolog_Clause2"):
                opp_val = getattr(old_value, "prolog_Clause2", None)
                if opp_val == self:
                    setattr(old_value, "prolog_Clause2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prolog_Clause2"):
                opp_val = getattr(value, "prolog_Clause2", None)
                setattr(value, "prolog_Clause2", self)

class prolog_Clause:

    pass
class prolog_PrologProgram:

    pass