from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Collection:

    pass
class problog_PLTuple(Collection):

    pass
class problog_PLList(Collection):

    pass
class ProbabilityMeasure:

    pass
class problog_ProbabilityFraction(ProbabilityMeasure):

    def __init__(self, nominator: int, denominator: int):
        self.nominator = nominator
        self.denominator = denominator
        
    @property
    def nominator(self) -> int:
        return self.__nominator

    @nominator.setter
    def nominator(self, nominator: int):
        self.__nominator = nominator

    @property
    def denominator(self) -> int:
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator: int):
        self.__denominator = denominator

class problog_ProbabilityLiteral(ProbabilityMeasure):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class Annotatable:

    pass
class Referable:

    pass
class problog_TermInstance(Referable, Annotatable):

    pass
class problog_Collection(Referable):

    pass
class problog_Atom(Referable, Annotatable):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class problog_Referable(ABC):

    pass
class problog_Proposition(ABC):

    pass
class problog_ProbabilityMeasure(ABC):

    pass
class Proposition:

    pass
class problog_Annotatable(Proposition):

    pass
class problog_AnnotatedReferable(Proposition):

    pass
class problog_Variable(Referable):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Statement:

    pass
class problog_Cheat(Statement):

    def __init__(self, contents: str):
        self.contents = contents
        
    @property
    def contents(self) -> str:
        return self.__contents

    @contents.setter
    def contents(self, contents: str):
        self.__contents = contents

class problog_ImportLibrary(Statement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class problog_ProbLogStatement(Statement):

    pass
class problog_Comment(Statement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class problog_Rule(Statement):

    pass
class problog_Term:

    def __init__(self, name: str, arguments: int, problog_Term: "problog_ProbLogProgram" = None, problog_Term16: "problog_TermInstance" = None):
        self.name = name
        self.arguments = arguments
        self.problog_Term = problog_Term
        self.problog_Term16 = problog_Term16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arguments(self) -> int:
        return self.__arguments

    @arguments.setter
    def arguments(self, arguments: int):
        self.__arguments = arguments

    @property
    def problog_Term(self):
        return self.__problog_Term

    @problog_Term.setter
    def problog_Term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_problog_Term__problog_Term", None)
        self.__problog_Term = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "problog_ProbLogProgram2"):
                opp_val = getattr(old_value, "problog_ProbLogProgram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "problog_ProbLogProgram2"):
                opp_val = getattr(value, "problog_ProbLogProgram2", None)
                if opp_val is None:
                    setattr(value, "problog_ProbLogProgram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def problog_Term16(self):
        return self.__problog_Term16

    @problog_Term16.setter
    def problog_Term16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_problog_Term__problog_Term16", None)
        self.__problog_Term16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "problog_TermInstance"):
                opp_val = getattr(old_value, "problog_TermInstance", None)
                if opp_val == self:
                    setattr(old_value, "problog_TermInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "problog_TermInstance"):
                opp_val = getattr(value, "problog_TermInstance", None)
                setattr(value, "problog_TermInstance", self)

class problog_Statement(ABC):

    pass
class problog_ProbLogProgram:

    pass
class ProbLogStatement:

    pass
class problog_Query(ProbLogStatement):

    pass
class problog_Evidence(ProbLogStatement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class problog_RHS:

    pass
class problog_LHS:

    pass