from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Term:

    pass
class mprologTermReference_Parenthesis(Term):

    pass
class mprologTermReference_Variable(Term):

    def __init__(self, name: str, mprologTermReference_Variable: "mprologTermReference_VariableReference" = None):
        self.name = name
        self.mprologTermReference_Variable = mprologTermReference_Variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mprologTermReference_Variable(self):
        return self.__mprologTermReference_Variable

    @mprologTermReference_Variable.setter
    def mprologTermReference_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mprologTermReference_Variable__mprologTermReference_Variable", None)
        self.__mprologTermReference_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mprologTermReference_VariableReference"):
                opp_val = getattr(old_value, "mprologTermReference_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "mprologTermReference_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mprologTermReference_VariableReference"):
                opp_val = getattr(value, "mprologTermReference_VariableReference", None)
                setattr(value, "mprologTermReference_VariableReference", self)

class mprologTermReference_Term(ABC):

    pass
class mprologTermReference_Functor(Term):

    def __init__(self, text: str, mprologTermReference_Functor13: "mprologTermReference_Term" = None, mprologTermReference_Functor28: "mprologTermReference_FunctorReference" = None, mprologTermReference_Functor: "mprologTermReference_Head" = None):
        self.text = text
        self.mprologTermReference_Functor13 = mprologTermReference_Functor13
        self.mprologTermReference_Functor28 = mprologTermReference_Functor28
        self.mprologTermReference_Functor = mprologTermReference_Functor
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def mprologTermReference_Functor28(self):
        return self.__mprologTermReference_Functor28

    @mprologTermReference_Functor28.setter
    def mprologTermReference_Functor28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mprologTermReference_Functor__mprologTermReference_Functor28", None)
        self.__mprologTermReference_Functor28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mprologTermReference_FunctorReference"):
                opp_val = getattr(old_value, "mprologTermReference_FunctorReference", None)
                if opp_val == self:
                    setattr(old_value, "mprologTermReference_FunctorReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mprologTermReference_FunctorReference"):
                opp_val = getattr(value, "mprologTermReference_FunctorReference", None)
                setattr(value, "mprologTermReference_FunctorReference", self)

    @property
    def mprologTermReference_Functor(self):
        return self.__mprologTermReference_Functor

    @mprologTermReference_Functor.setter
    def mprologTermReference_Functor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mprologTermReference_Functor__mprologTermReference_Functor", None)
        self.__mprologTermReference_Functor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mprologTermReference_Head6"):
                opp_val = getattr(old_value, "mprologTermReference_Head6", None)
                if opp_val == self:
                    setattr(old_value, "mprologTermReference_Head6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mprologTermReference_Head6"):
                opp_val = getattr(value, "mprologTermReference_Head6", None)
                setattr(value, "mprologTermReference_Head6", self)

    @property
    def mprologTermReference_Functor13(self):
        return self.__mprologTermReference_Functor13

    @mprologTermReference_Functor13.setter
    def mprologTermReference_Functor13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mprologTermReference_Functor__mprologTermReference_Functor13", None)
        self.__mprologTermReference_Functor13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mprologTermReference_Term14"):
                opp_val = getattr(old_value, "mprologTermReference_Term14", None)
                if opp_val == self:
                    setattr(old_value, "mprologTermReference_Term14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mprologTermReference_Term14"):
                opp_val = getattr(value, "mprologTermReference_Term14", None)
                setattr(value, "mprologTermReference_Term14", self)

class mprologTermReference_Body:

    pass
class mprologTermReference_Head:

    pass
class mprologTermReference_Clause:

    pass
class TermReference:

    pass
class mprologTermReference_VariableReference(TermReference):

    pass
class mprologTermReference_FunctorReference(TermReference):

    pass
class mprologTermReference_TermReference(Term):

    pass
class mprologTermReference_Operator:

    def __init__(self, symbol: str, mprologTermReference_Operator: "mprologTermReference_InfixExpression" = None):
        self.symbol = symbol
        self.mprologTermReference_Operator = mprologTermReference_Operator
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def mprologTermReference_Operator(self):
        return self.__mprologTermReference_Operator

    @mprologTermReference_Operator.setter
    def mprologTermReference_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mprologTermReference_Operator__mprologTermReference_Operator", None)
        self.__mprologTermReference_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mprologTermReference_InfixExpression26"):
                opp_val = getattr(old_value, "mprologTermReference_InfixExpression26", None)
                if opp_val == self:
                    setattr(old_value, "mprologTermReference_InfixExpression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mprologTermReference_InfixExpression26"):
                opp_val = getattr(value, "mprologTermReference_InfixExpression26", None)
                setattr(value, "mprologTermReference_InfixExpression26", self)

class mprologTermReference_InfixExpression(Term):

    pass
class mprologTermReference_List(Term):

    pass
class mprologTermReference_QuotedAtom(Term):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class mprologTermReference_Model:

    def __init__(self, name: str, mprologTermReference_Model: set["mprologTermReference_Clause"] = None):
        self.name = name
        self.mprologTermReference_Model = mprologTermReference_Model if mprologTermReference_Model is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mprologTermReference_Model(self):
        return self.__mprologTermReference_Model

    @mprologTermReference_Model.setter
    def mprologTermReference_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mprologTermReference_Model__mprologTermReference_Model", None)
        self.__mprologTermReference_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mprologTermReference_Clause"):
                    opp_val = getattr(item, "mprologTermReference_Clause", None)
                    
                    if opp_val == self:
                        setattr(item, "mprologTermReference_Clause", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mprologTermReference_Clause"):
                    opp_val = getattr(item, "mprologTermReference_Clause", None)
                    
                    setattr(item, "mprologTermReference_Clause", self)
                    
