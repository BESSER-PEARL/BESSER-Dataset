from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Constraint:

    pass
class tExp_Size(Constraint):

    def __init__(self, minSize: int, maxSize: int):
        self.minSize = minSize
        self.maxSize = maxSize
        
    @property
    def minSize(self) -> int:
        return self.__minSize

    @minSize.setter
    def minSize(self, minSize: int):
        self.__minSize = minSize

    @property
    def maxSize(self) -> int:
        return self.__maxSize

    @maxSize.setter
    def maxSize(self, maxSize: int):
        self.__maxSize = maxSize

class tExp_Singletons(Constraint):

    def __init__(self, minSingletons: int, maxSingletons: int):
        self.minSingletons = minSingletons
        self.maxSingletons = maxSingletons
        
    @property
    def maxSingletons(self) -> int:
        return self.__maxSingletons

    @maxSingletons.setter
    def maxSingletons(self, maxSingletons: int):
        self.__maxSingletons = maxSingletons

    @property
    def minSingletons(self) -> int:
        return self.__minSingletons

    @minSingletons.setter
    def minSingletons(self, minSingletons: int):
        self.__minSingletons = minSingletons

class tExp_Cardinality(Constraint):

    def __init__(self, minCardinality: int, maxCardinality: int):
        self.minCardinality = minCardinality
        self.maxCardinality = maxCardinality
        
    @property
    def maxCardinality(self) -> int:
        return self.__maxCardinality

    @maxCardinality.setter
    def maxCardinality(self, maxCardinality: int):
        self.__maxCardinality = maxCardinality

    @property
    def minCardinality(self) -> int:
        return self.__minCardinality

    @minCardinality.setter
    def minCardinality(self, minCardinality: int):
        self.__minCardinality = minCardinality

class Expression:

    pass
class tExp_FilterExpr(Expression):

    pass
class tExp_SeqExpr(Expression):

    pass
class tExp_TerminalExpr(Expression):

    pass
class tExp_VarExpr(Expression):

    pass
class tExp_CatExpr(Expression):

    pass
class tExp_ShuffleExpr(Expression):

    pass
class PrologExpression:

    pass
class tExp_NumberExpression(PrologExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class tExp_StringExpression(PrologExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class tExp_ListExpression(PrologExpression):

    pass
class tExp_VariableExpression(PrologExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tExp_AtomExpression(PrologExpression):

    def __init__(self, atom: str, tExp_AtomExpression: "tExp_PrologExpression" = None):
        self.atom = atom
        self.tExp_AtomExpression = tExp_AtomExpression
        
    @property
    def atom(self) -> str:
        return self.__atom

    @atom.setter
    def atom(self, atom: str):
        self.__atom = atom

    @property
    def tExp_AtomExpression(self):
        return self.__tExp_AtomExpression

    @tExp_AtomExpression.setter
    def tExp_AtomExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_AtomExpression__tExp_AtomExpression", None)
        self.__tExp_AtomExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression88"):
                opp_val = getattr(old_value, "tExp_PrologExpression88", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression88"):
                opp_val = getattr(value, "tExp_PrologExpression88", None)
                setattr(value, "tExp_PrologExpression88", self)

class tExp_AndExpr(Expression):

    pass
class tExp_UnionExpr(Expression):

    pass
class tExp_Msg:

    def __init__(self, performative: str, tExp_Msg: "tExp_EventType" = None, tExp_Msg59: "tExp_Role" = None, tExp_Msg62: "tExp_Role" = None, tExp_Msg65: "tExp_Role" = None, tExp_Msg68: "tExp_Role" = None, tExp_Msg71: "tExp_PrologExpression" = None, tExp_Msg74: "tExp_PrologExpression" = None):
        self.performative = performative
        self.tExp_Msg = tExp_Msg
        self.tExp_Msg59 = tExp_Msg59
        self.tExp_Msg62 = tExp_Msg62
        self.tExp_Msg65 = tExp_Msg65
        self.tExp_Msg68 = tExp_Msg68
        self.tExp_Msg71 = tExp_Msg71
        self.tExp_Msg74 = tExp_Msg74
        
    @property
    def performative(self) -> str:
        return self.__performative

    @performative.setter
    def performative(self, performative: str):
        self.__performative = performative

    @property
    def tExp_Msg71(self):
        return self.__tExp_Msg71

    @tExp_Msg71.setter
    def tExp_Msg71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Msg__tExp_Msg71", None)
        self.__tExp_Msg71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression72"):
                opp_val = getattr(old_value, "tExp_PrologExpression72", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression72"):
                opp_val = getattr(value, "tExp_PrologExpression72", None)
                setattr(value, "tExp_PrologExpression72", self)

    @property
    def tExp_Msg(self):
        return self.__tExp_Msg

    @tExp_Msg.setter
    def tExp_Msg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Msg__tExp_Msg", None)
        self.__tExp_Msg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_EventType54"):
                opp_val = getattr(old_value, "tExp_EventType54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_EventType54"):
                opp_val = getattr(value, "tExp_EventType54", None)
                if opp_val is None:
                    setattr(value, "tExp_EventType54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_Msg74(self):
        return self.__tExp_Msg74

    @tExp_Msg74.setter
    def tExp_Msg74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Msg__tExp_Msg74", None)
        self.__tExp_Msg74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression75"):
                opp_val = getattr(old_value, "tExp_PrologExpression75", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression75"):
                opp_val = getattr(value, "tExp_PrologExpression75", None)
                setattr(value, "tExp_PrologExpression75", self)

    @property
    def tExp_Msg65(self):
        return self.__tExp_Msg65

    @tExp_Msg65.setter
    def tExp_Msg65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Msg__tExp_Msg65", None)
        self.__tExp_Msg65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Role66"):
                opp_val = getattr(old_value, "tExp_Role66", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Role66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Role66"):
                opp_val = getattr(value, "tExp_Role66", None)
                setattr(value, "tExp_Role66", self)

    @property
    def tExp_Msg59(self):
        return self.__tExp_Msg59

    @tExp_Msg59.setter
    def tExp_Msg59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Msg__tExp_Msg59", None)
        self.__tExp_Msg59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Role60"):
                opp_val = getattr(old_value, "tExp_Role60", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Role60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Role60"):
                opp_val = getattr(value, "tExp_Role60", None)
                setattr(value, "tExp_Role60", self)

    @property
    def tExp_Msg62(self):
        return self.__tExp_Msg62

    @tExp_Msg62.setter
    def tExp_Msg62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Msg__tExp_Msg62", None)
        self.__tExp_Msg62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Role63"):
                opp_val = getattr(old_value, "tExp_Role63", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Role63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Role63"):
                opp_val = getattr(value, "tExp_Role63", None)
                setattr(value, "tExp_Role63", self)

    @property
    def tExp_Msg68(self):
        return self.__tExp_Msg68

    @tExp_Msg68.setter
    def tExp_Msg68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Msg__tExp_Msg68", None)
        self.__tExp_Msg68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Role69"):
                opp_val = getattr(old_value, "tExp_Role69", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Role69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Role69"):
                opp_val = getattr(value, "tExp_Role69", None)
                setattr(value, "tExp_Role69", self)

class tExp_Together:

    pass
class tExp_Expression:

    def __init__(self, operator: str, variable: str, eps: str, tExp_Expression22: "tExp_Expression" = None, tExp_Expression20: "tExp_Expression" = None, tExp_Expression24: "tExp_EventType" = None, tExp_Expression27: "tExp_PrologExpression" = None, tExp_Expression30: set["tExp_PrologExpression"] = None, tExp_Expression34: "tExp_Expression" = None, tExp_Expression32: "tExp_Expression" = None, tExp_Expression: "tExp_Term" = None, tExp_Expression36: "tExp_EventType" = None, tExp_Expression40: "tExp_Expression" = None, tExp_Expression38: "tExp_Expression" = None, tExp_Expression42: "tExp_Term" = None, tExp_Expression46: "tExp_Expression" = None, tExp_Expression44: "tExp_Expression" = None, tExp_Expression98: "tExp_ShuffleExpr" = None, tExp_Expression100: "tExp_UnionExpr" = None, tExp_Expression103: "tExp_UnionExpr" = None, tExp_Expression105: "tExp_AndExpr" = None, tExp_Expression95: "tExp_ShuffleExpr" = None, tExp_Expression108: "tExp_AndExpr" = None, tExp_Expression110: "tExp_CatExpr" = None, tExp_Expression113: "tExp_CatExpr" = None, tExp_Expression115: "tExp_SeqExpr" = None, tExp_Expression117: "tExp_FilterExpr" = None, tExp_Expression119: "tExp_VarExpr" = None, tExp_Expression121: "tExp_TerminalExpr" = None):
        self.operator = operator
        self.variable = variable
        self.eps = eps
        self.tExp_Expression22 = tExp_Expression22
        self.tExp_Expression20 = tExp_Expression20
        self.tExp_Expression24 = tExp_Expression24
        self.tExp_Expression27 = tExp_Expression27
        self.tExp_Expression30 = tExp_Expression30 if tExp_Expression30 is not None else set()
        self.tExp_Expression34 = tExp_Expression34
        self.tExp_Expression32 = tExp_Expression32
        self.tExp_Expression = tExp_Expression
        self.tExp_Expression36 = tExp_Expression36
        self.tExp_Expression40 = tExp_Expression40
        self.tExp_Expression38 = tExp_Expression38
        self.tExp_Expression42 = tExp_Expression42
        self.tExp_Expression46 = tExp_Expression46
        self.tExp_Expression44 = tExp_Expression44
        self.tExp_Expression98 = tExp_Expression98
        self.tExp_Expression100 = tExp_Expression100
        self.tExp_Expression103 = tExp_Expression103
        self.tExp_Expression105 = tExp_Expression105
        self.tExp_Expression95 = tExp_Expression95
        self.tExp_Expression108 = tExp_Expression108
        self.tExp_Expression110 = tExp_Expression110
        self.tExp_Expression113 = tExp_Expression113
        self.tExp_Expression115 = tExp_Expression115
        self.tExp_Expression117 = tExp_Expression117
        self.tExp_Expression119 = tExp_Expression119
        self.tExp_Expression121 = tExp_Expression121
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def eps(self) -> str:
        return self.__eps

    @eps.setter
    def eps(self, eps: str):
        self.__eps = eps

    @property
    def tExp_Expression24(self):
        return self.__tExp_Expression24

    @tExp_Expression24.setter
    def tExp_Expression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression24", None)
        self.__tExp_Expression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_EventType25"):
                opp_val = getattr(old_value, "tExp_EventType25", None)
                if opp_val == self:
                    setattr(old_value, "tExp_EventType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_EventType25"):
                opp_val = getattr(value, "tExp_EventType25", None)
                setattr(value, "tExp_EventType25", self)

    @property
    def tExp_Expression95(self):
        return self.__tExp_Expression95

    @tExp_Expression95.setter
    def tExp_Expression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression95", None)
        self.__tExp_Expression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_ShuffleExpr"):
                opp_val = getattr(old_value, "tExp_ShuffleExpr", None)
                if opp_val == self:
                    setattr(old_value, "tExp_ShuffleExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_ShuffleExpr"):
                opp_val = getattr(value, "tExp_ShuffleExpr", None)
                setattr(value, "tExp_ShuffleExpr", self)

    @property
    def tExp_Expression46(self):
        return self.__tExp_Expression46

    @tExp_Expression46.setter
    def tExp_Expression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression46", None)
        self.__tExp_Expression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression44"):
                opp_val = getattr(old_value, "tExp_Expression44", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression44"):
                opp_val = getattr(value, "tExp_Expression44", None)
                setattr(value, "tExp_Expression44", self)

    @property
    def tExp_Expression36(self):
        return self.__tExp_Expression36

    @tExp_Expression36.setter
    def tExp_Expression36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression36", None)
        self.__tExp_Expression36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_EventType37"):
                opp_val = getattr(old_value, "tExp_EventType37", None)
                if opp_val == self:
                    setattr(old_value, "tExp_EventType37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_EventType37"):
                opp_val = getattr(value, "tExp_EventType37", None)
                setattr(value, "tExp_EventType37", self)

    @property
    def tExp_Expression40(self):
        return self.__tExp_Expression40

    @tExp_Expression40.setter
    def tExp_Expression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression40", None)
        self.__tExp_Expression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression38"):
                opp_val = getattr(old_value, "tExp_Expression38", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression38"):
                opp_val = getattr(value, "tExp_Expression38", None)
                setattr(value, "tExp_Expression38", self)

    @property
    def tExp_Expression42(self):
        return self.__tExp_Expression42

    @tExp_Expression42.setter
    def tExp_Expression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression42", None)
        self.__tExp_Expression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Term43"):
                opp_val = getattr(old_value, "tExp_Term43", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Term43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Term43"):
                opp_val = getattr(value, "tExp_Term43", None)
                setattr(value, "tExp_Term43", self)

    @property
    def tExp_Expression113(self):
        return self.__tExp_Expression113

    @tExp_Expression113.setter
    def tExp_Expression113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression113", None)
        self.__tExp_Expression113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_CatExpr112"):
                opp_val = getattr(old_value, "tExp_CatExpr112", None)
                if opp_val == self:
                    setattr(old_value, "tExp_CatExpr112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_CatExpr112"):
                opp_val = getattr(value, "tExp_CatExpr112", None)
                setattr(value, "tExp_CatExpr112", self)

    @property
    def tExp_Expression115(self):
        return self.__tExp_Expression115

    @tExp_Expression115.setter
    def tExp_Expression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression115", None)
        self.__tExp_Expression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_SeqExpr"):
                opp_val = getattr(old_value, "tExp_SeqExpr", None)
                if opp_val == self:
                    setattr(old_value, "tExp_SeqExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_SeqExpr"):
                opp_val = getattr(value, "tExp_SeqExpr", None)
                setattr(value, "tExp_SeqExpr", self)

    @property
    def tExp_Expression98(self):
        return self.__tExp_Expression98

    @tExp_Expression98.setter
    def tExp_Expression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression98", None)
        self.__tExp_Expression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_ShuffleExpr97"):
                opp_val = getattr(old_value, "tExp_ShuffleExpr97", None)
                if opp_val == self:
                    setattr(old_value, "tExp_ShuffleExpr97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_ShuffleExpr97"):
                opp_val = getattr(value, "tExp_ShuffleExpr97", None)
                setattr(value, "tExp_ShuffleExpr97", self)

    @property
    def tExp_Expression(self):
        return self.__tExp_Expression

    @tExp_Expression.setter
    def tExp_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression", None)
        self.__tExp_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Term19"):
                opp_val = getattr(old_value, "tExp_Term19", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Term19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Term19"):
                opp_val = getattr(value, "tExp_Term19", None)
                setattr(value, "tExp_Term19", self)

    @property
    def tExp_Expression34(self):
        return self.__tExp_Expression34

    @tExp_Expression34.setter
    def tExp_Expression34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression34", None)
        self.__tExp_Expression34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression32"):
                opp_val = getattr(old_value, "tExp_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression32"):
                opp_val = getattr(value, "tExp_Expression32", None)
                setattr(value, "tExp_Expression32", self)

    @property
    def tExp_Expression20(self):
        return self.__tExp_Expression20

    @tExp_Expression20.setter
    def tExp_Expression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression20", None)
        self.__tExp_Expression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression22"):
                opp_val = getattr(old_value, "tExp_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression22"):
                opp_val = getattr(value, "tExp_Expression22", None)
                setattr(value, "tExp_Expression22", self)

    @property
    def tExp_Expression22(self):
        return self.__tExp_Expression22

    @tExp_Expression22.setter
    def tExp_Expression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression22", None)
        self.__tExp_Expression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression20"):
                opp_val = getattr(old_value, "tExp_Expression20", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression20"):
                opp_val = getattr(value, "tExp_Expression20", None)
                setattr(value, "tExp_Expression20", self)

    @property
    def tExp_Expression121(self):
        return self.__tExp_Expression121

    @tExp_Expression121.setter
    def tExp_Expression121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression121", None)
        self.__tExp_Expression121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_TerminalExpr"):
                opp_val = getattr(old_value, "tExp_TerminalExpr", None)
                if opp_val == self:
                    setattr(old_value, "tExp_TerminalExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_TerminalExpr"):
                opp_val = getattr(value, "tExp_TerminalExpr", None)
                setattr(value, "tExp_TerminalExpr", self)

    @property
    def tExp_Expression32(self):
        return self.__tExp_Expression32

    @tExp_Expression32.setter
    def tExp_Expression32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression32", None)
        self.__tExp_Expression32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression34"):
                opp_val = getattr(old_value, "tExp_Expression34", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression34"):
                opp_val = getattr(value, "tExp_Expression34", None)
                setattr(value, "tExp_Expression34", self)

    @property
    def tExp_Expression38(self):
        return self.__tExp_Expression38

    @tExp_Expression38.setter
    def tExp_Expression38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression38", None)
        self.__tExp_Expression38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression40"):
                opp_val = getattr(old_value, "tExp_Expression40", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression40"):
                opp_val = getattr(value, "tExp_Expression40", None)
                setattr(value, "tExp_Expression40", self)

    @property
    def tExp_Expression119(self):
        return self.__tExp_Expression119

    @tExp_Expression119.setter
    def tExp_Expression119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression119", None)
        self.__tExp_Expression119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_VarExpr"):
                opp_val = getattr(old_value, "tExp_VarExpr", None)
                if opp_val == self:
                    setattr(old_value, "tExp_VarExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_VarExpr"):
                opp_val = getattr(value, "tExp_VarExpr", None)
                setattr(value, "tExp_VarExpr", self)

    @property
    def tExp_Expression108(self):
        return self.__tExp_Expression108

    @tExp_Expression108.setter
    def tExp_Expression108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression108", None)
        self.__tExp_Expression108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_AndExpr107"):
                opp_val = getattr(old_value, "tExp_AndExpr107", None)
                if opp_val == self:
                    setattr(old_value, "tExp_AndExpr107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_AndExpr107"):
                opp_val = getattr(value, "tExp_AndExpr107", None)
                setattr(value, "tExp_AndExpr107", self)

    @property
    def tExp_Expression110(self):
        return self.__tExp_Expression110

    @tExp_Expression110.setter
    def tExp_Expression110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression110", None)
        self.__tExp_Expression110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_CatExpr"):
                opp_val = getattr(old_value, "tExp_CatExpr", None)
                if opp_val == self:
                    setattr(old_value, "tExp_CatExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_CatExpr"):
                opp_val = getattr(value, "tExp_CatExpr", None)
                setattr(value, "tExp_CatExpr", self)

    @property
    def tExp_Expression30(self):
        return self.__tExp_Expression30

    @tExp_Expression30.setter
    def tExp_Expression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression30", None)
        self.__tExp_Expression30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_PrologExpression31"):
                    opp_val = getattr(item, "tExp_PrologExpression31", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_PrologExpression31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_PrologExpression31"):
                    opp_val = getattr(item, "tExp_PrologExpression31", None)
                    
                    setattr(item, "tExp_PrologExpression31", self)
                    

    @property
    def tExp_Expression103(self):
        return self.__tExp_Expression103

    @tExp_Expression103.setter
    def tExp_Expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression103", None)
        self.__tExp_Expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_UnionExpr102"):
                opp_val = getattr(old_value, "tExp_UnionExpr102", None)
                if opp_val == self:
                    setattr(old_value, "tExp_UnionExpr102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_UnionExpr102"):
                opp_val = getattr(value, "tExp_UnionExpr102", None)
                setattr(value, "tExp_UnionExpr102", self)

    @property
    def tExp_Expression117(self):
        return self.__tExp_Expression117

    @tExp_Expression117.setter
    def tExp_Expression117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression117", None)
        self.__tExp_Expression117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_FilterExpr"):
                opp_val = getattr(old_value, "tExp_FilterExpr", None)
                if opp_val == self:
                    setattr(old_value, "tExp_FilterExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_FilterExpr"):
                opp_val = getattr(value, "tExp_FilterExpr", None)
                setattr(value, "tExp_FilterExpr", self)

    @property
    def tExp_Expression100(self):
        return self.__tExp_Expression100

    @tExp_Expression100.setter
    def tExp_Expression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression100", None)
        self.__tExp_Expression100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_UnionExpr"):
                opp_val = getattr(old_value, "tExp_UnionExpr", None)
                if opp_val == self:
                    setattr(old_value, "tExp_UnionExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_UnionExpr"):
                opp_val = getattr(value, "tExp_UnionExpr", None)
                setattr(value, "tExp_UnionExpr", self)

    @property
    def tExp_Expression105(self):
        return self.__tExp_Expression105

    @tExp_Expression105.setter
    def tExp_Expression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression105", None)
        self.__tExp_Expression105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_AndExpr"):
                opp_val = getattr(old_value, "tExp_AndExpr", None)
                if opp_val == self:
                    setattr(old_value, "tExp_AndExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_AndExpr"):
                opp_val = getattr(value, "tExp_AndExpr", None)
                setattr(value, "tExp_AndExpr", self)

    @property
    def tExp_Expression44(self):
        return self.__tExp_Expression44

    @tExp_Expression44.setter
    def tExp_Expression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression44", None)
        self.__tExp_Expression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression46"):
                opp_val = getattr(old_value, "tExp_Expression46", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression46"):
                opp_val = getattr(value, "tExp_Expression46", None)
                setattr(value, "tExp_Expression46", self)

    @property
    def tExp_Expression27(self):
        return self.__tExp_Expression27

    @tExp_Expression27.setter
    def tExp_Expression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Expression__tExp_Expression27", None)
        self.__tExp_Expression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression28"):
                opp_val = getattr(old_value, "tExp_PrologExpression28", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression28"):
                opp_val = getattr(value, "tExp_PrologExpression28", None)
                setattr(value, "tExp_PrologExpression28", self)

class tExp_Channel:

    def __init__(self, name: str, reliability: str, tExp_Channel: "tExp_TraceExpression" = None, tExp_Channel57: "tExp_EventType" = None):
        self.name = name
        self.reliability = reliability
        self.tExp_Channel = tExp_Channel
        self.tExp_Channel57 = tExp_Channel57
        
    @property
    def reliability(self) -> str:
        return self.__reliability

    @reliability.setter
    def reliability(self, reliability: str):
        self.__reliability = reliability

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tExp_Channel(self):
        return self.__tExp_Channel

    @tExp_Channel.setter
    def tExp_Channel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Channel__tExp_Channel", None)
        self.__tExp_Channel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_TraceExpression17"):
                opp_val = getattr(old_value, "tExp_TraceExpression17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_TraceExpression17"):
                opp_val = getattr(value, "tExp_TraceExpression17", None)
                if opp_val is None:
                    setattr(value, "tExp_TraceExpression17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_Channel57(self):
        return self.__tExp_Channel57

    @tExp_Channel57.setter
    def tExp_Channel57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Channel__tExp_Channel57", None)
        self.__tExp_Channel57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_EventType56"):
                opp_val = getattr(old_value, "tExp_EventType56", None)
                if opp_val == self:
                    setattr(old_value, "tExp_EventType56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_EventType56"):
                opp_val = getattr(value, "tExp_EventType56", None)
                setattr(value, "tExp_EventType56", self)

class tExp_Constraint:

    def __init__(self, together: str, split: str, parMin: str, parMax: str, tExp_Constraint: "tExp_TraceExpression" = None, tExp_Constraint82: set["tExp_Role"] = None, tExp_Constraint85: set["tExp_Role"] = None):
        self.together = together
        self.split = split
        self.parMin = parMin
        self.parMax = parMax
        self.tExp_Constraint = tExp_Constraint
        self.tExp_Constraint82 = tExp_Constraint82 if tExp_Constraint82 is not None else set()
        self.tExp_Constraint85 = tExp_Constraint85 if tExp_Constraint85 is not None else set()
        
    @property
    def split(self) -> str:
        return self.__split

    @split.setter
    def split(self, split: str):
        self.__split = split

    @property
    def parMin(self) -> str:
        return self.__parMin

    @parMin.setter
    def parMin(self, parMin: str):
        self.__parMin = parMin

    @property
    def together(self) -> str:
        return self.__together

    @together.setter
    def together(self, together: str):
        self.__together = together

    @property
    def parMax(self) -> str:
        return self.__parMax

    @parMax.setter
    def parMax(self, parMax: str):
        self.__parMax = parMax

    @property
    def tExp_Constraint85(self):
        return self.__tExp_Constraint85

    @tExp_Constraint85.setter
    def tExp_Constraint85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Constraint__tExp_Constraint85", None)
        self.__tExp_Constraint85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_Role86"):
                    opp_val = getattr(item, "tExp_Role86", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_Role86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_Role86"):
                    opp_val = getattr(item, "tExp_Role86", None)
                    
                    setattr(item, "tExp_Role86", self)
                    

    @property
    def tExp_Constraint(self):
        return self.__tExp_Constraint

    @tExp_Constraint.setter
    def tExp_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Constraint__tExp_Constraint", None)
        self.__tExp_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_TraceExpression15"):
                opp_val = getattr(old_value, "tExp_TraceExpression15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_TraceExpression15"):
                opp_val = getattr(value, "tExp_TraceExpression15", None)
                if opp_val is None:
                    setattr(value, "tExp_TraceExpression15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_Constraint82(self):
        return self.__tExp_Constraint82

    @tExp_Constraint82.setter
    def tExp_Constraint82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Constraint__tExp_Constraint82", None)
        self.__tExp_Constraint82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_Role83"):
                    opp_val = getattr(item, "tExp_Role83", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_Role83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_Role83"):
                    opp_val = getattr(item, "tExp_Role83", None)
                    
                    setattr(item, "tExp_Role83", self)
                    

class tExp_Partition:

    pass
class tExp_EventType:

    def __init__(self, name: str, tExp_EventType25: "tExp_Expression" = None, tExp_EventType37: "tExp_Expression" = None, tExp_EventType: "tExp_TraceExpression" = None, tExp_EventType48: "tExp_PrologExpression" = None, tExp_EventType51: set["tExp_PrologExpression"] = None, tExp_EventType54: set["tExp_Msg"] = None, tExp_EventType56: "tExp_Channel" = None):
        self.name = name
        self.tExp_EventType25 = tExp_EventType25
        self.tExp_EventType37 = tExp_EventType37
        self.tExp_EventType = tExp_EventType
        self.tExp_EventType48 = tExp_EventType48
        self.tExp_EventType51 = tExp_EventType51 if tExp_EventType51 is not None else set()
        self.tExp_EventType54 = tExp_EventType54 if tExp_EventType54 is not None else set()
        self.tExp_EventType56 = tExp_EventType56
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tExp_EventType51(self):
        return self.__tExp_EventType51

    @tExp_EventType51.setter
    def tExp_EventType51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_EventType__tExp_EventType51", None)
        self.__tExp_EventType51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_PrologExpression52"):
                    opp_val = getattr(item, "tExp_PrologExpression52", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_PrologExpression52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_PrologExpression52"):
                    opp_val = getattr(item, "tExp_PrologExpression52", None)
                    
                    setattr(item, "tExp_PrologExpression52", self)
                    

    @property
    def tExp_EventType(self):
        return self.__tExp_EventType

    @tExp_EventType.setter
    def tExp_EventType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_EventType__tExp_EventType", None)
        self.__tExp_EventType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_TraceExpression11"):
                opp_val = getattr(old_value, "tExp_TraceExpression11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_TraceExpression11"):
                opp_val = getattr(value, "tExp_TraceExpression11", None)
                if opp_val is None:
                    setattr(value, "tExp_TraceExpression11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_EventType54(self):
        return self.__tExp_EventType54

    @tExp_EventType54.setter
    def tExp_EventType54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_EventType__tExp_EventType54", None)
        self.__tExp_EventType54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_Msg"):
                    opp_val = getattr(item, "tExp_Msg", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_Msg", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_Msg"):
                    opp_val = getattr(item, "tExp_Msg", None)
                    
                    setattr(item, "tExp_Msg", self)
                    

    @property
    def tExp_EventType56(self):
        return self.__tExp_EventType56

    @tExp_EventType56.setter
    def tExp_EventType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_EventType__tExp_EventType56", None)
        self.__tExp_EventType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Channel57"):
                opp_val = getattr(old_value, "tExp_Channel57", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Channel57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Channel57"):
                opp_val = getattr(value, "tExp_Channel57", None)
                setattr(value, "tExp_Channel57", self)

    @property
    def tExp_EventType37(self):
        return self.__tExp_EventType37

    @tExp_EventType37.setter
    def tExp_EventType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_EventType__tExp_EventType37", None)
        self.__tExp_EventType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression36"):
                opp_val = getattr(old_value, "tExp_Expression36", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression36"):
                opp_val = getattr(value, "tExp_Expression36", None)
                setattr(value, "tExp_Expression36", self)

    @property
    def tExp_EventType25(self):
        return self.__tExp_EventType25

    @tExp_EventType25.setter
    def tExp_EventType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_EventType__tExp_EventType25", None)
        self.__tExp_EventType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression24"):
                opp_val = getattr(old_value, "tExp_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression24"):
                opp_val = getattr(value, "tExp_Expression24", None)
                setattr(value, "tExp_Expression24", self)

    @property
    def tExp_EventType48(self):
        return self.__tExp_EventType48

    @tExp_EventType48.setter
    def tExp_EventType48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_EventType__tExp_EventType48", None)
        self.__tExp_EventType48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression49"):
                opp_val = getattr(old_value, "tExp_PrologExpression49", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression49"):
                opp_val = getattr(value, "tExp_PrologExpression49", None)
                setattr(value, "tExp_PrologExpression49", self)

class tExp_PrologExpression:

    def __init__(self, op: str, tExp_PrologExpression5: "tExp_PrologExpression" = None, tExp_PrologExpression3: "tExp_PrologExpression" = None, tExp_PrologExpression: "tExp_PrologExpression" = None, tExp_PrologExpression1: "tExp_PrologExpression" = None, tExp_PrologExpression28: "tExp_Expression" = None, tExp_PrologExpression31: "tExp_Expression" = None, tExp_PrologExpression49: "tExp_EventType" = None, tExp_PrologExpression52: "tExp_EventType" = None, tExp_PrologExpression72: "tExp_Msg" = None, tExp_PrologExpression75: "tExp_Msg" = None, tExp_PrologExpression88: "tExp_AtomExpression" = None, tExp_PrologExpression90: "tExp_ListExpression" = None, tExp_PrologExpression93: "tExp_ListExpression" = None):
        self.op = op
        self.tExp_PrologExpression5 = tExp_PrologExpression5
        self.tExp_PrologExpression3 = tExp_PrologExpression3
        self.tExp_PrologExpression = tExp_PrologExpression
        self.tExp_PrologExpression1 = tExp_PrologExpression1
        self.tExp_PrologExpression28 = tExp_PrologExpression28
        self.tExp_PrologExpression31 = tExp_PrologExpression31
        self.tExp_PrologExpression49 = tExp_PrologExpression49
        self.tExp_PrologExpression52 = tExp_PrologExpression52
        self.tExp_PrologExpression72 = tExp_PrologExpression72
        self.tExp_PrologExpression75 = tExp_PrologExpression75
        self.tExp_PrologExpression88 = tExp_PrologExpression88
        self.tExp_PrologExpression90 = tExp_PrologExpression90
        self.tExp_PrologExpression93 = tExp_PrologExpression93
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def tExp_PrologExpression88(self):
        return self.__tExp_PrologExpression88

    @tExp_PrologExpression88.setter
    def tExp_PrologExpression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression88", None)
        self.__tExp_PrologExpression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_AtomExpression"):
                opp_val = getattr(old_value, "tExp_AtomExpression", None)
                if opp_val == self:
                    setattr(old_value, "tExp_AtomExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_AtomExpression"):
                opp_val = getattr(value, "tExp_AtomExpression", None)
                setattr(value, "tExp_AtomExpression", self)

    @property
    def tExp_PrologExpression28(self):
        return self.__tExp_PrologExpression28

    @tExp_PrologExpression28.setter
    def tExp_PrologExpression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression28", None)
        self.__tExp_PrologExpression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression27"):
                opp_val = getattr(old_value, "tExp_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression27"):
                opp_val = getattr(value, "tExp_Expression27", None)
                setattr(value, "tExp_Expression27", self)

    @property
    def tExp_PrologExpression75(self):
        return self.__tExp_PrologExpression75

    @tExp_PrologExpression75.setter
    def tExp_PrologExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression75", None)
        self.__tExp_PrologExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Msg74"):
                opp_val = getattr(old_value, "tExp_Msg74", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Msg74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Msg74"):
                opp_val = getattr(value, "tExp_Msg74", None)
                setattr(value, "tExp_Msg74", self)

    @property
    def tExp_PrologExpression90(self):
        return self.__tExp_PrologExpression90

    @tExp_PrologExpression90.setter
    def tExp_PrologExpression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression90", None)
        self.__tExp_PrologExpression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_ListExpression"):
                opp_val = getattr(old_value, "tExp_ListExpression", None)
                if opp_val == self:
                    setattr(old_value, "tExp_ListExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_ListExpression"):
                opp_val = getattr(value, "tExp_ListExpression", None)
                setattr(value, "tExp_ListExpression", self)

    @property
    def tExp_PrologExpression(self):
        return self.__tExp_PrologExpression

    @tExp_PrologExpression.setter
    def tExp_PrologExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression", None)
        self.__tExp_PrologExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression1"):
                opp_val = getattr(old_value, "tExp_PrologExpression1", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression1"):
                opp_val = getattr(value, "tExp_PrologExpression1", None)
                setattr(value, "tExp_PrologExpression1", self)

    @property
    def tExp_PrologExpression72(self):
        return self.__tExp_PrologExpression72

    @tExp_PrologExpression72.setter
    def tExp_PrologExpression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression72", None)
        self.__tExp_PrologExpression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Msg71"):
                opp_val = getattr(old_value, "tExp_Msg71", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Msg71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Msg71"):
                opp_val = getattr(value, "tExp_Msg71", None)
                setattr(value, "tExp_Msg71", self)

    @property
    def tExp_PrologExpression1(self):
        return self.__tExp_PrologExpression1

    @tExp_PrologExpression1.setter
    def tExp_PrologExpression1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression1", None)
        self.__tExp_PrologExpression1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression"):
                opp_val = getattr(old_value, "tExp_PrologExpression", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression"):
                opp_val = getattr(value, "tExp_PrologExpression", None)
                setattr(value, "tExp_PrologExpression", self)

    @property
    def tExp_PrologExpression5(self):
        return self.__tExp_PrologExpression5

    @tExp_PrologExpression5.setter
    def tExp_PrologExpression5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression5", None)
        self.__tExp_PrologExpression5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression3"):
                opp_val = getattr(old_value, "tExp_PrologExpression3", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression3"):
                opp_val = getattr(value, "tExp_PrologExpression3", None)
                setattr(value, "tExp_PrologExpression3", self)

    @property
    def tExp_PrologExpression49(self):
        return self.__tExp_PrologExpression49

    @tExp_PrologExpression49.setter
    def tExp_PrologExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression49", None)
        self.__tExp_PrologExpression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_EventType48"):
                opp_val = getattr(old_value, "tExp_EventType48", None)
                if opp_val == self:
                    setattr(old_value, "tExp_EventType48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_EventType48"):
                opp_val = getattr(value, "tExp_EventType48", None)
                setattr(value, "tExp_EventType48", self)

    @property
    def tExp_PrologExpression31(self):
        return self.__tExp_PrologExpression31

    @tExp_PrologExpression31.setter
    def tExp_PrologExpression31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression31", None)
        self.__tExp_PrologExpression31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression30"):
                opp_val = getattr(old_value, "tExp_Expression30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression30"):
                opp_val = getattr(value, "tExp_Expression30", None)
                if opp_val is None:
                    setattr(value, "tExp_Expression30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_PrologExpression93(self):
        return self.__tExp_PrologExpression93

    @tExp_PrologExpression93.setter
    def tExp_PrologExpression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression93", None)
        self.__tExp_PrologExpression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_ListExpression92"):
                opp_val = getattr(old_value, "tExp_ListExpression92", None)
                if opp_val == self:
                    setattr(old_value, "tExp_ListExpression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_ListExpression92"):
                opp_val = getattr(value, "tExp_ListExpression92", None)
                setattr(value, "tExp_ListExpression92", self)

    @property
    def tExp_PrologExpression52(self):
        return self.__tExp_PrologExpression52

    @tExp_PrologExpression52.setter
    def tExp_PrologExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression52", None)
        self.__tExp_PrologExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_EventType51"):
                opp_val = getattr(old_value, "tExp_EventType51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_EventType51"):
                opp_val = getattr(value, "tExp_EventType51", None)
                if opp_val is None:
                    setattr(value, "tExp_EventType51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_PrologExpression3(self):
        return self.__tExp_PrologExpression3

    @tExp_PrologExpression3.setter
    def tExp_PrologExpression3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_PrologExpression__tExp_PrologExpression3", None)
        self.__tExp_PrologExpression3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_PrologExpression5"):
                opp_val = getattr(old_value, "tExp_PrologExpression5", None)
                if opp_val == self:
                    setattr(old_value, "tExp_PrologExpression5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_PrologExpression5"):
                opp_val = getattr(value, "tExp_PrologExpression5", None)
                setattr(value, "tExp_PrologExpression5", self)

class tExp_TraceExpression:

    def __init__(self, name: str, bodyL: str, rolesL: str, typesL: str, modulesL: str, modules: str, decentralizedL: str, decentralized: str, partitionL: str, constraintsL: str, guiL: str, gui: str, minimalL: str, minimal: str, thresholdL: str, threshold: str, channelsL: str, tExp_TraceExpression7: set["tExp_Term"] = None, tExp_TraceExpression9: set["tExp_Role"] = None, tExp_TraceExpression: "tExp_Domainmodel" = None, tExp_TraceExpression11: set["tExp_EventType"] = None, tExp_TraceExpression13: set["tExp_Partition"] = None, tExp_TraceExpression15: set["tExp_Constraint"] = None, tExp_TraceExpression17: set["tExp_Channel"] = None):
        self.name = name
        self.bodyL = bodyL
        self.rolesL = rolesL
        self.typesL = typesL
        self.modulesL = modulesL
        self.modules = modules
        self.decentralizedL = decentralizedL
        self.decentralized = decentralized
        self.partitionL = partitionL
        self.constraintsL = constraintsL
        self.guiL = guiL
        self.gui = gui
        self.minimalL = minimalL
        self.minimal = minimal
        self.thresholdL = thresholdL
        self.threshold = threshold
        self.channelsL = channelsL
        self.tExp_TraceExpression7 = tExp_TraceExpression7 if tExp_TraceExpression7 is not None else set()
        self.tExp_TraceExpression9 = tExp_TraceExpression9 if tExp_TraceExpression9 is not None else set()
        self.tExp_TraceExpression = tExp_TraceExpression
        self.tExp_TraceExpression11 = tExp_TraceExpression11 if tExp_TraceExpression11 is not None else set()
        self.tExp_TraceExpression13 = tExp_TraceExpression13 if tExp_TraceExpression13 is not None else set()
        self.tExp_TraceExpression15 = tExp_TraceExpression15 if tExp_TraceExpression15 is not None else set()
        self.tExp_TraceExpression17 = tExp_TraceExpression17 if tExp_TraceExpression17 is not None else set()
        
    @property
    def modules(self) -> str:
        return self.__modules

    @modules.setter
    def modules(self, modules: str):
        self.__modules = modules

    @property
    def rolesL(self) -> str:
        return self.__rolesL

    @rolesL.setter
    def rolesL(self, rolesL: str):
        self.__rolesL = rolesL

    @property
    def constraintsL(self) -> str:
        return self.__constraintsL

    @constraintsL.setter
    def constraintsL(self, constraintsL: str):
        self.__constraintsL = constraintsL

    @property
    def decentralized(self) -> str:
        return self.__decentralized

    @decentralized.setter
    def decentralized(self, decentralized: str):
        self.__decentralized = decentralized

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gui(self) -> str:
        return self.__gui

    @gui.setter
    def gui(self, gui: str):
        self.__gui = gui

    @property
    def thresholdL(self) -> str:
        return self.__thresholdL

    @thresholdL.setter
    def thresholdL(self, thresholdL: str):
        self.__thresholdL = thresholdL

    @property
    def modulesL(self) -> str:
        return self.__modulesL

    @modulesL.setter
    def modulesL(self, modulesL: str):
        self.__modulesL = modulesL

    @property
    def channelsL(self) -> str:
        return self.__channelsL

    @channelsL.setter
    def channelsL(self, channelsL: str):
        self.__channelsL = channelsL

    @property
    def threshold(self) -> str:
        return self.__threshold

    @threshold.setter
    def threshold(self, threshold: str):
        self.__threshold = threshold

    @property
    def decentralizedL(self) -> str:
        return self.__decentralizedL

    @decentralizedL.setter
    def decentralizedL(self, decentralizedL: str):
        self.__decentralizedL = decentralizedL

    @property
    def partitionL(self) -> str:
        return self.__partitionL

    @partitionL.setter
    def partitionL(self, partitionL: str):
        self.__partitionL = partitionL

    @property
    def bodyL(self) -> str:
        return self.__bodyL

    @bodyL.setter
    def bodyL(self, bodyL: str):
        self.__bodyL = bodyL

    @property
    def minimal(self) -> str:
        return self.__minimal

    @minimal.setter
    def minimal(self, minimal: str):
        self.__minimal = minimal

    @property
    def guiL(self) -> str:
        return self.__guiL

    @guiL.setter
    def guiL(self, guiL: str):
        self.__guiL = guiL

    @property
    def minimalL(self) -> str:
        return self.__minimalL

    @minimalL.setter
    def minimalL(self, minimalL: str):
        self.__minimalL = minimalL

    @property
    def typesL(self) -> str:
        return self.__typesL

    @typesL.setter
    def typesL(self, typesL: str):
        self.__typesL = typesL

    @property
    def tExp_TraceExpression17(self):
        return self.__tExp_TraceExpression17

    @tExp_TraceExpression17.setter
    def tExp_TraceExpression17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_TraceExpression__tExp_TraceExpression17", None)
        self.__tExp_TraceExpression17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_Channel"):
                    opp_val = getattr(item, "tExp_Channel", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_Channel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_Channel"):
                    opp_val = getattr(item, "tExp_Channel", None)
                    
                    setattr(item, "tExp_Channel", self)
                    

    @property
    def tExp_TraceExpression7(self):
        return self.__tExp_TraceExpression7

    @tExp_TraceExpression7.setter
    def tExp_TraceExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_TraceExpression__tExp_TraceExpression7", None)
        self.__tExp_TraceExpression7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_Term"):
                    opp_val = getattr(item, "tExp_Term", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_Term", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_Term"):
                    opp_val = getattr(item, "tExp_Term", None)
                    
                    setattr(item, "tExp_Term", self)
                    

    @property
    def tExp_TraceExpression15(self):
        return self.__tExp_TraceExpression15

    @tExp_TraceExpression15.setter
    def tExp_TraceExpression15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_TraceExpression__tExp_TraceExpression15", None)
        self.__tExp_TraceExpression15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_Constraint"):
                    opp_val = getattr(item, "tExp_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_Constraint"):
                    opp_val = getattr(item, "tExp_Constraint", None)
                    
                    setattr(item, "tExp_Constraint", self)
                    

    @property
    def tExp_TraceExpression13(self):
        return self.__tExp_TraceExpression13

    @tExp_TraceExpression13.setter
    def tExp_TraceExpression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_TraceExpression__tExp_TraceExpression13", None)
        self.__tExp_TraceExpression13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_Partition"):
                    opp_val = getattr(item, "tExp_Partition", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_Partition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_Partition"):
                    opp_val = getattr(item, "tExp_Partition", None)
                    
                    setattr(item, "tExp_Partition", self)
                    

    @property
    def tExp_TraceExpression11(self):
        return self.__tExp_TraceExpression11

    @tExp_TraceExpression11.setter
    def tExp_TraceExpression11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_TraceExpression__tExp_TraceExpression11", None)
        self.__tExp_TraceExpression11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_EventType"):
                    opp_val = getattr(item, "tExp_EventType", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_EventType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_EventType"):
                    opp_val = getattr(item, "tExp_EventType", None)
                    
                    setattr(item, "tExp_EventType", self)
                    

    @property
    def tExp_TraceExpression9(self):
        return self.__tExp_TraceExpression9

    @tExp_TraceExpression9.setter
    def tExp_TraceExpression9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_TraceExpression__tExp_TraceExpression9", None)
        self.__tExp_TraceExpression9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tExp_Role"):
                    opp_val = getattr(item, "tExp_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "tExp_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tExp_Role"):
                    opp_val = getattr(item, "tExp_Role", None)
                    
                    setattr(item, "tExp_Role", self)
                    

    @property
    def tExp_TraceExpression(self):
        return self.__tExp_TraceExpression

    @tExp_TraceExpression.setter
    def tExp_TraceExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_TraceExpression__tExp_TraceExpression", None)
        self.__tExp_TraceExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Domainmodel"):
                opp_val = getattr(old_value, "tExp_Domainmodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Domainmodel"):
                opp_val = getattr(value, "tExp_Domainmodel", None)
                if opp_val is None:
                    setattr(value, "tExp_Domainmodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tExp_Domainmodel:

    pass
class tExp_Role:

    def __init__(self, name: str, class: str, args: str, tExp_Role: "tExp_TraceExpression" = None, tExp_Role80: "tExp_Together" = None, tExp_Role60: "tExp_Msg" = None, tExp_Role63: "tExp_Msg" = None, tExp_Role66: "tExp_Msg" = None, tExp_Role69: "tExp_Msg" = None, tExp_Role83: "tExp_Constraint" = None, tExp_Role86: "tExp_Constraint" = None):
        self.name = name
        self.class = class
        self.args = args
        self.tExp_Role = tExp_Role
        self.tExp_Role80 = tExp_Role80
        self.tExp_Role60 = tExp_Role60
        self.tExp_Role63 = tExp_Role63
        self.tExp_Role66 = tExp_Role66
        self.tExp_Role69 = tExp_Role69
        self.tExp_Role83 = tExp_Role83
        self.tExp_Role86 = tExp_Role86
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def args(self) -> str:
        return self.__args

    @args.setter
    def args(self, args: str):
        self.__args = args

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def tExp_Role66(self):
        return self.__tExp_Role66

    @tExp_Role66.setter
    def tExp_Role66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Role__tExp_Role66", None)
        self.__tExp_Role66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Msg65"):
                opp_val = getattr(old_value, "tExp_Msg65", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Msg65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Msg65"):
                opp_val = getattr(value, "tExp_Msg65", None)
                setattr(value, "tExp_Msg65", self)

    @property
    def tExp_Role83(self):
        return self.__tExp_Role83

    @tExp_Role83.setter
    def tExp_Role83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Role__tExp_Role83", None)
        self.__tExp_Role83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Constraint82"):
                opp_val = getattr(old_value, "tExp_Constraint82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Constraint82"):
                opp_val = getattr(value, "tExp_Constraint82", None)
                if opp_val is None:
                    setattr(value, "tExp_Constraint82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_Role(self):
        return self.__tExp_Role

    @tExp_Role.setter
    def tExp_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Role__tExp_Role", None)
        self.__tExp_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_TraceExpression9"):
                opp_val = getattr(old_value, "tExp_TraceExpression9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_TraceExpression9"):
                opp_val = getattr(value, "tExp_TraceExpression9", None)
                if opp_val is None:
                    setattr(value, "tExp_TraceExpression9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_Role80(self):
        return self.__tExp_Role80

    @tExp_Role80.setter
    def tExp_Role80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Role__tExp_Role80", None)
        self.__tExp_Role80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Together79"):
                opp_val = getattr(old_value, "tExp_Together79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Together79"):
                opp_val = getattr(value, "tExp_Together79", None)
                if opp_val is None:
                    setattr(value, "tExp_Together79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_Role69(self):
        return self.__tExp_Role69

    @tExp_Role69.setter
    def tExp_Role69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Role__tExp_Role69", None)
        self.__tExp_Role69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Msg68"):
                opp_val = getattr(old_value, "tExp_Msg68", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Msg68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Msg68"):
                opp_val = getattr(value, "tExp_Msg68", None)
                setattr(value, "tExp_Msg68", self)

    @property
    def tExp_Role63(self):
        return self.__tExp_Role63

    @tExp_Role63.setter
    def tExp_Role63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Role__tExp_Role63", None)
        self.__tExp_Role63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Msg62"):
                opp_val = getattr(old_value, "tExp_Msg62", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Msg62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Msg62"):
                opp_val = getattr(value, "tExp_Msg62", None)
                setattr(value, "tExp_Msg62", self)

    @property
    def tExp_Role60(self):
        return self.__tExp_Role60

    @tExp_Role60.setter
    def tExp_Role60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Role__tExp_Role60", None)
        self.__tExp_Role60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Msg59"):
                opp_val = getattr(old_value, "tExp_Msg59", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Msg59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Msg59"):
                opp_val = getattr(value, "tExp_Msg59", None)
                setattr(value, "tExp_Msg59", self)

    @property
    def tExp_Role86(self):
        return self.__tExp_Role86

    @tExp_Role86.setter
    def tExp_Role86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Role__tExp_Role86", None)
        self.__tExp_Role86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Constraint85"):
                opp_val = getattr(old_value, "tExp_Constraint85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Constraint85"):
                opp_val = getattr(value, "tExp_Constraint85", None)
                if opp_val is None:
                    setattr(value, "tExp_Constraint85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tExp_Term:

    def __init__(self, name: str, tExp_Term: "tExp_TraceExpression" = None, tExp_Term19: "tExp_Expression" = None, tExp_Term43: "tExp_Expression" = None):
        self.name = name
        self.tExp_Term = tExp_Term
        self.tExp_Term19 = tExp_Term19
        self.tExp_Term43 = tExp_Term43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tExp_Term19(self):
        return self.__tExp_Term19

    @tExp_Term19.setter
    def tExp_Term19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Term__tExp_Term19", None)
        self.__tExp_Term19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression"):
                opp_val = getattr(old_value, "tExp_Expression", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression"):
                opp_val = getattr(value, "tExp_Expression", None)
                setattr(value, "tExp_Expression", self)

    @property
    def tExp_Term(self):
        return self.__tExp_Term

    @tExp_Term.setter
    def tExp_Term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Term__tExp_Term", None)
        self.__tExp_Term = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_TraceExpression7"):
                opp_val = getattr(old_value, "tExp_TraceExpression7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_TraceExpression7"):
                opp_val = getattr(value, "tExp_TraceExpression7", None)
                if opp_val is None:
                    setattr(value, "tExp_TraceExpression7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tExp_Term43(self):
        return self.__tExp_Term43

    @tExp_Term43.setter
    def tExp_Term43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tExp_Term__tExp_Term43", None)
        self.__tExp_Term43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tExp_Expression42"):
                opp_val = getattr(old_value, "tExp_Expression42", None)
                if opp_val == self:
                    setattr(old_value, "tExp_Expression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tExp_Expression42"):
                opp_val = getattr(value, "tExp_Expression42", None)
                setattr(value, "tExp_Expression42", self)
