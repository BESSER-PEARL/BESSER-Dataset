from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MultiplicativeKind(Enum):
    multiply = "multiply"
    divide = "divide"
    remainder = "remainder"
class EqualityKind(Enum):
    equal = "equal"
    notEqual = "notEqual"
class AccessKind(Enum):
    exist = "exist"
    read = "read"
    write = "write"
class ComparisonKind(Enum):
    lower = "lower"
    lowerOrEqual = "lowerOrEqual"
    greaterOrEqual = "greaterOrEqual"
    greater = "greater"
class AdditiveKind(Enum):
    add = "add"
    subtract = "subtract"


############################################
# Definition of Classes
############################################

class Atom:

    pass
class game_Cell(Atom):

    pass
class Collection:

    pass
class game_ImplicitSet(Collection):

    pass
class game_Join(Collection):

    pass
class game_Brackets(Collection):

    pass
class Index:

    pass
class game_Atom(Index):

    pass
class Primary:

    pass
class game_Index(Primary):

    pass
class game_Cardinal(Primary):

    pass
class game_Collection(Primary):

    pass
class Setable:

    pass
class game_Primary(Setable):

    pass
class game_SetExpression(Setable):

    pass
class game_LogicalNot(Primary):

    pass
class Equatable:

    pass
class game_Equality(Equatable):

    def __init__(self, kind: str, game_Equality: "game_Equatable" = None, game_Equality62: "game_Comparable" = None):
        self.kind = kind
        self.game_Equality = game_Equality
        self.game_Equality62 = game_Equality62
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def game_Equality62(self):
        return self.__game_Equality62

    @game_Equality62.setter
    def game_Equality62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Equality__game_Equality62", None)
        self.__game_Equality62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Comparable"):
                opp_val = getattr(old_value, "game_Comparable", None)
                if opp_val == self:
                    setattr(old_value, "game_Comparable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Comparable"):
                opp_val = getattr(value, "game_Comparable", None)
                setattr(value, "game_Comparable", self)

    @property
    def game_Equality(self):
        return self.__game_Equality

    @game_Equality.setter
    def game_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Equality__game_Equality", None)
        self.__game_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Equatable60"):
                opp_val = getattr(old_value, "game_Equatable60", None)
                if opp_val == self:
                    setattr(old_value, "game_Equatable60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Equatable60"):
                opp_val = getattr(value, "game_Equatable60", None)
                setattr(value, "game_Equatable60", self)

class game_Comparable(Equatable):

    pass
class Andable:

    pass
class game_And(Andable):

    pass
class game_Equatable(Andable):

    pass
class Orable:

    pass
class game_Andable(Orable):

    pass
class Expression:

    pass
class game_Orable(Expression):

    pass
class game_Call(Primary):

    def __init__(self, name: str, game_Call: "game_Subprocess" = None, game_Call80: set["game_Expression"] = None):
        self.name = name
        self.game_Call = game_Call
        self.game_Call80 = game_Call80 if game_Call80 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def game_Call(self):
        return self.__game_Call

    @game_Call.setter
    def game_Call(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Call__game_Call", None)
        self.__game_Call = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Subprocess"):
                opp_val = getattr(old_value, "game_Subprocess", None)
                if opp_val == self:
                    setattr(old_value, "game_Subprocess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Subprocess"):
                opp_val = getattr(value, "game_Subprocess", None)
                setattr(value, "game_Subprocess", self)

    @property
    def game_Call80(self):
        return self.__game_Call80

    @game_Call80.setter
    def game_Call80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Call__game_Call80", None)
        self.__game_Call80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Expression81"):
                    opp_val = getattr(item, "game_Expression81", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Expression81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Expression81"):
                    opp_val = getattr(item, "game_Expression81", None)
                    
                    setattr(item, "game_Expression81", self)
                    

class game_Or(Orable):

    pass
class Multipliable:

    pass
class game_Multiplication(Multipliable):

    def __init__(self, kind: str, game_Multiplication: "game_Multipliable" = None, game_Multiplication74: "game_Setable" = None):
        self.kind = kind
        self.game_Multiplication = game_Multiplication
        self.game_Multiplication74 = game_Multiplication74
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def game_Multiplication74(self):
        return self.__game_Multiplication74

    @game_Multiplication74.setter
    def game_Multiplication74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Multiplication__game_Multiplication74", None)
        self.__game_Multiplication74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Setable"):
                opp_val = getattr(old_value, "game_Setable", None)
                if opp_val == self:
                    setattr(old_value, "game_Setable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Setable"):
                opp_val = getattr(value, "game_Setable", None)
                setattr(value, "game_Setable", self)

    @property
    def game_Multiplication(self):
        return self.__game_Multiplication

    @game_Multiplication.setter
    def game_Multiplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Multiplication__game_Multiplication", None)
        self.__game_Multiplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Multipliable72"):
                opp_val = getattr(old_value, "game_Multipliable72", None)
                if opp_val == self:
                    setattr(old_value, "game_Multipliable72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Multipliable72"):
                opp_val = getattr(value, "game_Multipliable72", None)
                setattr(value, "game_Multipliable72", self)

class game_Setable(Multipliable):

    pass
class Addable:

    pass
class game_Addition(Addable):

    def __init__(self, kind: str, game_Addition: "game_Addable" = None, game_Addition70: "game_Multipliable" = None):
        self.kind = kind
        self.game_Addition = game_Addition
        self.game_Addition70 = game_Addition70
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def game_Addition70(self):
        return self.__game_Addition70

    @game_Addition70.setter
    def game_Addition70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Addition__game_Addition70", None)
        self.__game_Addition70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Multipliable"):
                opp_val = getattr(old_value, "game_Multipliable", None)
                if opp_val == self:
                    setattr(old_value, "game_Multipliable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Multipliable"):
                opp_val = getattr(value, "game_Multipliable", None)
                setattr(value, "game_Multipliable", self)

    @property
    def game_Addition(self):
        return self.__game_Addition

    @game_Addition.setter
    def game_Addition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Addition__game_Addition", None)
        self.__game_Addition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Addable68"):
                opp_val = getattr(old_value, "game_Addable68", None)
                if opp_val == self:
                    setattr(old_value, "game_Addable68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Addable68"):
                opp_val = getattr(value, "game_Addable68", None)
                setattr(value, "game_Addable68", self)

class game_Multipliable(Addable):

    pass
class Comparable:

    pass
class game_Comparison(Comparable):

    def __init__(self, kind: str, game_Comparison: "game_Comparable" = None, game_Comparison66: "game_Addable" = None):
        self.kind = kind
        self.game_Comparison = game_Comparison
        self.game_Comparison66 = game_Comparison66
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def game_Comparison66(self):
        return self.__game_Comparison66

    @game_Comparison66.setter
    def game_Comparison66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Comparison__game_Comparison66", None)
        self.__game_Comparison66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Addable"):
                opp_val = getattr(old_value, "game_Addable", None)
                if opp_val == self:
                    setattr(old_value, "game_Addable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Addable"):
                opp_val = getattr(value, "game_Addable", None)
                setattr(value, "game_Addable", self)

    @property
    def game_Comparison(self):
        return self.__game_Comparison

    @game_Comparison.setter
    def game_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Comparison__game_Comparison", None)
        self.__game_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Comparable64"):
                opp_val = getattr(old_value, "game_Comparable64", None)
                if opp_val == self:
                    setattr(old_value, "game_Comparable64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Comparable64"):
                opp_val = getattr(value, "game_Comparable64", None)
                setattr(value, "game_Comparable64", self)

class game_Addable(Comparable):

    pass
class game_Expression(ABC):

    pass
class Statement:

    pass
class game_Forall(Statement):

    pass
class game_Iteration(Statement):

    pass
class game_Subprocess(Statement):

    pass
class game_Selection(Statement):

    pass
class game_Assignment(Statement):

    pass
class game_Variable(Atom):

    def __init__(self, name: str, game_Variable: "game_Forall" = None, game_Variable94: "game_ImplicitSet" = None, game_Variable103: "game_Cell" = None, game_Variable106: "game_Cell" = None):
        self.name = name
        self.game_Variable = game_Variable
        self.game_Variable94 = game_Variable94
        self.game_Variable103 = game_Variable103
        self.game_Variable106 = game_Variable106
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def game_Variable(self):
        return self.__game_Variable

    @game_Variable.setter
    def game_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Variable__game_Variable", None)
        self.__game_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Forall42"):
                opp_val = getattr(old_value, "game_Forall42", None)
                if opp_val == self:
                    setattr(old_value, "game_Forall42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Forall42"):
                opp_val = getattr(value, "game_Forall42", None)
                setattr(value, "game_Forall42", self)

    @property
    def game_Variable103(self):
        return self.__game_Variable103

    @game_Variable103.setter
    def game_Variable103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Variable__game_Variable103", None)
        self.__game_Variable103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Cell"):
                opp_val = getattr(old_value, "game_Cell", None)
                if opp_val == self:
                    setattr(old_value, "game_Cell", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Cell"):
                opp_val = getattr(value, "game_Cell", None)
                setattr(value, "game_Cell", self)

    @property
    def game_Variable106(self):
        return self.__game_Variable106

    @game_Variable106.setter
    def game_Variable106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Variable__game_Variable106", None)
        self.__game_Variable106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Cell105"):
                opp_val = getattr(old_value, "game_Cell105", None)
                if opp_val == self:
                    setattr(old_value, "game_Cell105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Cell105"):
                opp_val = getattr(value, "game_Cell105", None)
                setattr(value, "game_Cell105", self)

    @property
    def game_Variable94(self):
        return self.__game_Variable94

    @game_Variable94.setter
    def game_Variable94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Variable__game_Variable94", None)
        self.__game_Variable94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_ImplicitSet93"):
                opp_val = getattr(old_value, "game_ImplicitSet93", None)
                if opp_val == self:
                    setattr(old_value, "game_ImplicitSet93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_ImplicitSet93"):
                opp_val = getattr(value, "game_ImplicitSet93", None)
                setattr(value, "game_ImplicitSet93", self)

class game_Query:

    def __init__(self, name: str, game_Query: "game_System" = None, game_Query23: set["game_Access"] = None):
        self.name = name
        self.game_Query = game_Query
        self.game_Query23 = game_Query23 if game_Query23 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def game_Query(self):
        return self.__game_Query

    @game_Query.setter
    def game_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Query__game_Query", None)
        self.__game_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_System21"):
                opp_val = getattr(old_value, "game_System21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_System21"):
                opp_val = getattr(value, "game_System21", None)
                if opp_val is None:
                    setattr(value, "game_System21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_Query23(self):
        return self.__game_Query23

    @game_Query23.setter
    def game_Query23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Query__game_Query23", None)
        self.__game_Query23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Access"):
                    opp_val = getattr(item, "game_Access", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Access", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Access"):
                    opp_val = getattr(item, "game_Access", None)
                    
                    setattr(item, "game_Access", self)
                    

class game_Statement(ABC):

    pass
class game_Function:

    def __init__(self, name: str, game_Function: "game_Game" = None, game_Function10: "game_Type" = None, game_Function13: set["game_Statement"] = None):
        self.name = name
        self.game_Function = game_Function
        self.game_Function10 = game_Function10
        self.game_Function13 = game_Function13 if game_Function13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def game_Function10(self):
        return self.__game_Function10

    @game_Function10.setter
    def game_Function10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Function__game_Function10", None)
        self.__game_Function10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Type11"):
                opp_val = getattr(old_value, "game_Type11", None)
                if opp_val == self:
                    setattr(old_value, "game_Type11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Type11"):
                opp_val = getattr(value, "game_Type11", None)
                setattr(value, "game_Type11", self)

    @property
    def game_Function13(self):
        return self.__game_Function13

    @game_Function13.setter
    def game_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Function__game_Function13", None)
        self.__game_Function13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Statement"):
                    opp_val = getattr(item, "game_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Statement"):
                    opp_val = getattr(item, "game_Statement", None)
                    
                    setattr(item, "game_Statement", self)
                    

    @property
    def game_Function(self):
        return self.__game_Function

    @game_Function.setter
    def game_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Function__game_Function", None)
        self.__game_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Game8"):
                opp_val = getattr(old_value, "game_Game8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Game8"):
                opp_val = getattr(value, "game_Game8", None)
                if opp_val is None:
                    setattr(value, "game_Game8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class game_Access:

    def __init__(self, name: str, kind: str, game_Access: "game_Query" = None):
        self.name = name
        self.kind = kind
        self.game_Access = game_Access
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def game_Access(self):
        return self.__game_Access

    @game_Access.setter
    def game_Access(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Access__game_Access", None)
        self.__game_Access = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Query23"):
                opp_val = getattr(old_value, "game_Query23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Query23"):
                opp_val = getattr(value, "game_Query23", None)
                if opp_val is None:
                    setattr(value, "game_Query23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class game_Type:

    def __init__(self, valueType: bool, namespace: str, name: str, game_Type: "game_Game" = None, game_Type11: "game_Function" = None, game_Type16: "game_ComponentData" = None, game_Type51: "game_Expression" = None, game_Type109: "game_Type" = None, game_Type107: set["game_Type"] = None):
        self.valueType = valueType
        self.namespace = namespace
        self.name = name
        self.game_Type = game_Type
        self.game_Type11 = game_Type11
        self.game_Type16 = game_Type16
        self.game_Type51 = game_Type51
        self.game_Type109 = game_Type109
        self.game_Type107 = game_Type107 if game_Type107 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def valueType(self) -> bool:
        return self.__valueType

    @valueType.setter
    def valueType(self, valueType: bool):
        self.__valueType = valueType

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def game_Type(self):
        return self.__game_Type

    @game_Type.setter
    def game_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Type__game_Type", None)
        self.__game_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Game"):
                opp_val = getattr(old_value, "game_Game", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Game"):
                opp_val = getattr(value, "game_Game", None)
                if opp_val is None:
                    setattr(value, "game_Game", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_Type16(self):
        return self.__game_Type16

    @game_Type16.setter
    def game_Type16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Type__game_Type16", None)
        self.__game_Type16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_ComponentData15"):
                opp_val = getattr(old_value, "game_ComponentData15", None)
                if opp_val == self:
                    setattr(old_value, "game_ComponentData15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_ComponentData15"):
                opp_val = getattr(value, "game_ComponentData15", None)
                setattr(value, "game_ComponentData15", self)

    @property
    def game_Type109(self):
        return self.__game_Type109

    @game_Type109.setter
    def game_Type109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Type__game_Type109", None)
        self.__game_Type109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Type107"):
                opp_val = getattr(old_value, "game_Type107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Type107"):
                opp_val = getattr(value, "game_Type107", None)
                if opp_val is None:
                    setattr(value, "game_Type107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game_Type107(self):
        return self.__game_Type107

    @game_Type107.setter
    def game_Type107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Type__game_Type107", None)
        self.__game_Type107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Type109"):
                    opp_val = getattr(item, "game_Type109", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Type109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Type109"):
                    opp_val = getattr(item, "game_Type109", None)
                    
                    setattr(item, "game_Type109", self)
                    

    @property
    def game_Type11(self):
        return self.__game_Type11

    @game_Type11.setter
    def game_Type11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Type__game_Type11", None)
        self.__game_Type11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Function10"):
                opp_val = getattr(old_value, "game_Function10", None)
                if opp_val == self:
                    setattr(old_value, "game_Function10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Function10"):
                opp_val = getattr(value, "game_Function10", None)
                setattr(value, "game_Function10", self)

    @property
    def game_Type51(self):
        return self.__game_Type51

    @game_Type51.setter
    def game_Type51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Type__game_Type51", None)
        self.__game_Type51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Expression50"):
                opp_val = getattr(old_value, "game_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "game_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Expression50"):
                opp_val = getattr(value, "game_Expression50", None)
                setattr(value, "game_Expression50", self)

class game_Game:

    def __init__(self, name: str, version: str, game_Game: set["game_Type"] = None, game_Game2: set["game_System"] = None, game_Game4: set["game_ComponentData"] = None, game_Game6: "game_End" = None, game_Game8: set["game_Function"] = None):
        self.name = name
        self.version = version
        self.game_Game = game_Game if game_Game is not None else set()
        self.game_Game2 = game_Game2 if game_Game2 is not None else set()
        self.game_Game4 = game_Game4 if game_Game4 is not None else set()
        self.game_Game6 = game_Game6
        self.game_Game8 = game_Game8 if game_Game8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def game_Game(self):
        return self.__game_Game

    @game_Game.setter
    def game_Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game", None)
        self.__game_Game = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Type"):
                    opp_val = getattr(item, "game_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Type"):
                    opp_val = getattr(item, "game_Type", None)
                    
                    setattr(item, "game_Type", self)
                    

    @property
    def game_Game4(self):
        return self.__game_Game4

    @game_Game4.setter
    def game_Game4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game4", None)
        self.__game_Game4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_ComponentData"):
                    opp_val = getattr(item, "game_ComponentData", None)
                    
                    if opp_val == self:
                        setattr(item, "game_ComponentData", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_ComponentData"):
                    opp_val = getattr(item, "game_ComponentData", None)
                    
                    setattr(item, "game_ComponentData", self)
                    

    @property
    def game_Game6(self):
        return self.__game_Game6

    @game_Game6.setter
    def game_Game6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game6", None)
        self.__game_Game6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_End"):
                opp_val = getattr(old_value, "game_End", None)
                if opp_val == self:
                    setattr(old_value, "game_End", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_End"):
                opp_val = getattr(value, "game_End", None)
                setattr(value, "game_End", self)

    @property
    def game_Game8(self):
        return self.__game_Game8

    @game_Game8.setter
    def game_Game8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game8", None)
        self.__game_Game8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Function"):
                    opp_val = getattr(item, "game_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Function"):
                    opp_val = getattr(item, "game_Function", None)
                    
                    setattr(item, "game_Function", self)
                    

    @property
    def game_Game2(self):
        return self.__game_Game2

    @game_Game2.setter
    def game_Game2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_Game__game_Game2", None)
        self.__game_Game2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_System"):
                    opp_val = getattr(item, "game_System", None)
                    
                    if opp_val == self:
                        setattr(item, "game_System", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_System"):
                    opp_val = getattr(item, "game_System", None)
                    
                    setattr(item, "game_System", self)
                    

class game_End:

    pass
class game_ComponentData:

    def __init__(self, name: str, game_ComponentData: "game_Game" = None, game_ComponentData15: "game_Type" = None):
        self.name = name
        self.game_ComponentData = game_ComponentData
        self.game_ComponentData15 = game_ComponentData15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def game_ComponentData15(self):
        return self.__game_ComponentData15

    @game_ComponentData15.setter
    def game_ComponentData15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_ComponentData__game_ComponentData15", None)
        self.__game_ComponentData15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Type16"):
                opp_val = getattr(old_value, "game_Type16", None)
                if opp_val == self:
                    setattr(old_value, "game_Type16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Type16"):
                opp_val = getattr(value, "game_Type16", None)
                setattr(value, "game_Type16", self)

    @property
    def game_ComponentData(self):
        return self.__game_ComponentData

    @game_ComponentData.setter
    def game_ComponentData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_ComponentData__game_ComponentData", None)
        self.__game_ComponentData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Game4"):
                opp_val = getattr(old_value, "game_Game4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Game4"):
                opp_val = getattr(value, "game_Game4", None)
                if opp_val is None:
                    setattr(value, "game_Game4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class game_System:

    def __init__(self, name: str, game_System: "game_Game" = None, game_System21: set["game_Query"] = None, game_System18: set["game_Statement"] = None):
        self.name = name
        self.game_System = game_System
        self.game_System21 = game_System21 if game_System21 is not None else set()
        self.game_System18 = game_System18 if game_System18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def game_System18(self):
        return self.__game_System18

    @game_System18.setter
    def game_System18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_System__game_System18", None)
        self.__game_System18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Statement19"):
                    opp_val = getattr(item, "game_Statement19", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Statement19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Statement19"):
                    opp_val = getattr(item, "game_Statement19", None)
                    
                    setattr(item, "game_Statement19", self)
                    

    @property
    def game_System21(self):
        return self.__game_System21

    @game_System21.setter
    def game_System21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_System__game_System21", None)
        self.__game_System21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game_Query"):
                    opp_val = getattr(item, "game_Query", None)
                    
                    if opp_val == self:
                        setattr(item, "game_Query", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game_Query"):
                    opp_val = getattr(item, "game_Query", None)
                    
                    setattr(item, "game_Query", self)
                    

    @property
    def game_System(self):
        return self.__game_System

    @game_System.setter
    def game_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_game_System__game_System", None)
        self.__game_System = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game_Game2"):
                opp_val = getattr(old_value, "game_Game2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game_Game2"):
                opp_val = getattr(value, "game_Game2", None)
                if opp_val is None:
                    setattr(value, "game_Game2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
