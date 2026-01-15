from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class backtrackingContentAssistTest_LetVariable:

    def __init__(self, name: str, backtrackingContentAssistTest_LetVariable: "backtrackingContentAssistTest_LetExp" = None, backtrackingContentAssistTest_LetVariable127: "backtrackingContentAssistTest_TypeExp" = None, backtrackingContentAssistTest_LetVariable130: "backtrackingContentAssistTest_Expression" = None):
        self.name = name
        self.backtrackingContentAssistTest_LetVariable = backtrackingContentAssistTest_LetVariable
        self.backtrackingContentAssistTest_LetVariable127 = backtrackingContentAssistTest_LetVariable127
        self.backtrackingContentAssistTest_LetVariable130 = backtrackingContentAssistTest_LetVariable130
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def backtrackingContentAssistTest_LetVariable(self):
        return self.__backtrackingContentAssistTest_LetVariable

    @backtrackingContentAssistTest_LetVariable.setter
    def backtrackingContentAssistTest_LetVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_LetVariable__backtrackingContentAssistTest_LetVariable", None)
        self.__backtrackingContentAssistTest_LetVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_LetExp"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_LetExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_LetExp"):
                opp_val = getattr(value, "backtrackingContentAssistTest_LetExp", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_LetExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backtrackingContentAssistTest_LetVariable127(self):
        return self.__backtrackingContentAssistTest_LetVariable127

    @backtrackingContentAssistTest_LetVariable127.setter
    def backtrackingContentAssistTest_LetVariable127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_LetVariable__backtrackingContentAssistTest_LetVariable127", None)
        self.__backtrackingContentAssistTest_LetVariable127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TypeExp128"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TypeExp128", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_TypeExp128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TypeExp128"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TypeExp128", None)
                setattr(value, "backtrackingContentAssistTest_TypeExp128", self)

    @property
    def backtrackingContentAssistTest_LetVariable130(self):
        return self.__backtrackingContentAssistTest_LetVariable130

    @backtrackingContentAssistTest_LetVariable130.setter
    def backtrackingContentAssistTest_LetVariable130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_LetVariable__backtrackingContentAssistTest_LetVariable130", None)
        self.__backtrackingContentAssistTest_LetVariable130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression131"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression131", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression131"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression131", None)
                setattr(value, "backtrackingContentAssistTest_Expression131", self)

class NameExp:

    pass
class backtrackingContentAssistTest_SimpleNameExp(NameExp):

    def __init__(self, element: str):
        self.element = element
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

class backtrackingContentAssistTest_PathNameExp(NameExp):

    def __init__(self, namespace: str, backtrackingContentAssistTest_PathNameExp: "backtrackingContentAssistTest_NameExp" = None):
        self.namespace = namespace
        self.backtrackingContentAssistTest_PathNameExp = backtrackingContentAssistTest_PathNameExp
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def backtrackingContentAssistTest_PathNameExp(self):
        return self.__backtrackingContentAssistTest_PathNameExp

    @backtrackingContentAssistTest_PathNameExp.setter
    def backtrackingContentAssistTest_PathNameExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_PathNameExp__backtrackingContentAssistTest_PathNameExp", None)
        self.__backtrackingContentAssistTest_PathNameExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_NameExp113"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_NameExp113", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_NameExp113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_NameExp113"):
                opp_val = getattr(value, "backtrackingContentAssistTest_NameExp113", None)
                setattr(value, "backtrackingContentAssistTest_NameExp113", self)

class backtrackingContentAssistTest_iteratorAccumulator:

    def __init__(self, name: str, backtrackingContentAssistTest_iteratorAccumulator: "backtrackingContentAssistTest_TypeExp" = None, backtrackingContentAssistTest_iteratorAccumulator94: "backtrackingContentAssistTest_Expression" = None):
        self.name = name
        self.backtrackingContentAssistTest_iteratorAccumulator = backtrackingContentAssistTest_iteratorAccumulator
        self.backtrackingContentAssistTest_iteratorAccumulator94 = backtrackingContentAssistTest_iteratorAccumulator94
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def backtrackingContentAssistTest_iteratorAccumulator(self):
        return self.__backtrackingContentAssistTest_iteratorAccumulator

    @backtrackingContentAssistTest_iteratorAccumulator.setter
    def backtrackingContentAssistTest_iteratorAccumulator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_iteratorAccumulator__backtrackingContentAssistTest_iteratorAccumulator", None)
        self.__backtrackingContentAssistTest_iteratorAccumulator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TypeExp92"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TypeExp92", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_TypeExp92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TypeExp92"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TypeExp92", None)
                setattr(value, "backtrackingContentAssistTest_TypeExp92", self)

    @property
    def backtrackingContentAssistTest_iteratorAccumulator94(self):
        return self.__backtrackingContentAssistTest_iteratorAccumulator94

    @backtrackingContentAssistTest_iteratorAccumulator94.setter
    def backtrackingContentAssistTest_iteratorAccumulator94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_iteratorAccumulator__backtrackingContentAssistTest_iteratorAccumulator94", None)
        self.__backtrackingContentAssistTest_iteratorAccumulator94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression95"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression95", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression95"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression95", None)
                setattr(value, "backtrackingContentAssistTest_Expression95", self)

class backtrackingContentAssistTest_EObject:

    pass
class PrimitiveLiteralExp:

    pass
class backtrackingContentAssistTest_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class backtrackingContentAssistTest_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, isTrue: bool):
        self.isTrue = isTrue
        
    @property
    def isTrue(self) -> bool:
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue

class backtrackingContentAssistTest_NumberLiteralExp(PrimitiveLiteralExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class backtrackingContentAssistTest_iteratorVariable:

    def __init__(self, name: str, backtrackingContentAssistTest_iteratorVariable: "backtrackingContentAssistTest_TypeExp" = None, backtrackingContentAssistTest_iteratorVariable99: "backtrackingContentAssistTest_RoundBracketExp" = None):
        self.name = name
        self.backtrackingContentAssistTest_iteratorVariable = backtrackingContentAssistTest_iteratorVariable
        self.backtrackingContentAssistTest_iteratorVariable99 = backtrackingContentAssistTest_iteratorVariable99
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def backtrackingContentAssistTest_iteratorVariable99(self):
        return self.__backtrackingContentAssistTest_iteratorVariable99

    @backtrackingContentAssistTest_iteratorVariable99.setter
    def backtrackingContentAssistTest_iteratorVariable99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_iteratorVariable__backtrackingContentAssistTest_iteratorVariable99", None)
        self.__backtrackingContentAssistTest_iteratorVariable99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_RoundBracketExp98"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_RoundBracketExp98", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_RoundBracketExp98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_RoundBracketExp98"):
                opp_val = getattr(value, "backtrackingContentAssistTest_RoundBracketExp98", None)
                setattr(value, "backtrackingContentAssistTest_RoundBracketExp98", self)

    @property
    def backtrackingContentAssistTest_iteratorVariable(self):
        return self.__backtrackingContentAssistTest_iteratorVariable

    @backtrackingContentAssistTest_iteratorVariable.setter
    def backtrackingContentAssistTest_iteratorVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_iteratorVariable__backtrackingContentAssistTest_iteratorVariable", None)
        self.__backtrackingContentAssistTest_iteratorVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TypeExp90"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TypeExp90", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_TypeExp90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TypeExp90"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TypeExp90", None)
                setattr(value, "backtrackingContentAssistTest_TypeExp90", self)

class backtrackingContentAssistTest_NullLiteralExp(PrimitiveLiteralExp):

    pass
class backtrackingContentAssistTest_InvalidLiteralExp(PrimitiveLiteralExp):

    pass
class backtrackingContentAssistTest_TupleLiteralPart:

    def __init__(self, name: str, backtrackingContentAssistTest_TupleLiteralPart: "backtrackingContentAssistTest_TupleLiteralExp" = None, backtrackingContentAssistTest_TupleLiteralPart84: "backtrackingContentAssistTest_TypeExp" = None, backtrackingContentAssistTest_TupleLiteralPart87: "backtrackingContentAssistTest_Expression" = None):
        self.name = name
        self.backtrackingContentAssistTest_TupleLiteralPart = backtrackingContentAssistTest_TupleLiteralPart
        self.backtrackingContentAssistTest_TupleLiteralPart84 = backtrackingContentAssistTest_TupleLiteralPart84
        self.backtrackingContentAssistTest_TupleLiteralPart87 = backtrackingContentAssistTest_TupleLiteralPart87
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def backtrackingContentAssistTest_TupleLiteralPart87(self):
        return self.__backtrackingContentAssistTest_TupleLiteralPart87

    @backtrackingContentAssistTest_TupleLiteralPart87.setter
    def backtrackingContentAssistTest_TupleLiteralPart87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_TupleLiteralPart__backtrackingContentAssistTest_TupleLiteralPart87", None)
        self.__backtrackingContentAssistTest_TupleLiteralPart87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression88"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression88"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression88", None)
                setattr(value, "backtrackingContentAssistTest_Expression88", self)

    @property
    def backtrackingContentAssistTest_TupleLiteralPart84(self):
        return self.__backtrackingContentAssistTest_TupleLiteralPart84

    @backtrackingContentAssistTest_TupleLiteralPart84.setter
    def backtrackingContentAssistTest_TupleLiteralPart84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_TupleLiteralPart__backtrackingContentAssistTest_TupleLiteralPart84", None)
        self.__backtrackingContentAssistTest_TupleLiteralPart84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TypeExp85"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TypeExp85", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_TypeExp85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TypeExp85"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TypeExp85", None)
                setattr(value, "backtrackingContentAssistTest_TypeExp85", self)

    @property
    def backtrackingContentAssistTest_TupleLiteralPart(self):
        return self.__backtrackingContentAssistTest_TupleLiteralPart

    @backtrackingContentAssistTest_TupleLiteralPart.setter
    def backtrackingContentAssistTest_TupleLiteralPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_TupleLiteralPart__backtrackingContentAssistTest_TupleLiteralPart", None)
        self.__backtrackingContentAssistTest_TupleLiteralPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TupleLiteralExp"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TupleLiteralExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TupleLiteralExp"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TupleLiteralExp", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_TupleLiteralExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class backtrackingContentAssistTest_tuplePart:

    def __init__(self, name: str, backtrackingContentAssistTest_tuplePart: "backtrackingContentAssistTest_TupleType" = None, backtrackingContentAssistTest_tuplePart73: "backtrackingContentAssistTest_TypeExp" = None):
        self.name = name
        self.backtrackingContentAssistTest_tuplePart = backtrackingContentAssistTest_tuplePart
        self.backtrackingContentAssistTest_tuplePart73 = backtrackingContentAssistTest_tuplePart73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def backtrackingContentAssistTest_tuplePart(self):
        return self.__backtrackingContentAssistTest_tuplePart

    @backtrackingContentAssistTest_tuplePart.setter
    def backtrackingContentAssistTest_tuplePart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_tuplePart__backtrackingContentAssistTest_tuplePart", None)
        self.__backtrackingContentAssistTest_tuplePart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TupleType"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TupleType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TupleType"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TupleType", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_TupleType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backtrackingContentAssistTest_tuplePart73(self):
        return self.__backtrackingContentAssistTest_tuplePart73

    @backtrackingContentAssistTest_tuplePart73.setter
    def backtrackingContentAssistTest_tuplePart73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_tuplePart__backtrackingContentAssistTest_tuplePart73", None)
        self.__backtrackingContentAssistTest_tuplePart73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TypeExp74"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TypeExp74", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_TypeExp74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TypeExp74"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TypeExp74", None)
                setattr(value, "backtrackingContentAssistTest_TypeExp74", self)

class CollectionLiteralExp:

    pass
class Expression:

    pass
class backtrackingContentAssistTest_InfixExp(Expression):

    def __init__(self, op: str, backtrackingContentAssistTest_InfixExp: "backtrackingContentAssistTest_Expression" = None, backtrackingContentAssistTest_InfixExp135: "backtrackingContentAssistTest_NavigatingExp" = None):
        self.op = op
        self.backtrackingContentAssistTest_InfixExp = backtrackingContentAssistTest_InfixExp
        self.backtrackingContentAssistTest_InfixExp135 = backtrackingContentAssistTest_InfixExp135
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def backtrackingContentAssistTest_InfixExp135(self):
        return self.__backtrackingContentAssistTest_InfixExp135

    @backtrackingContentAssistTest_InfixExp135.setter
    def backtrackingContentAssistTest_InfixExp135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_InfixExp__backtrackingContentAssistTest_InfixExp135", None)
        self.__backtrackingContentAssistTest_InfixExp135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_NavigatingExp"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_NavigatingExp", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_NavigatingExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_NavigatingExp"):
                opp_val = getattr(value, "backtrackingContentAssistTest_NavigatingExp", None)
                setattr(value, "backtrackingContentAssistTest_NavigatingExp", self)

    @property
    def backtrackingContentAssistTest_InfixExp(self):
        return self.__backtrackingContentAssistTest_InfixExp

    @backtrackingContentAssistTest_InfixExp.setter
    def backtrackingContentAssistTest_InfixExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_InfixExp__backtrackingContentAssistTest_InfixExp", None)
        self.__backtrackingContentAssistTest_InfixExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression133"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression133", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression133"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression133", None)
                setattr(value, "backtrackingContentAssistTest_Expression133", self)

class backtrackingContentAssistTest_NestedExp(Expression):

    pass
class backtrackingContentAssistTest_TupleLiteralExp(Expression):

    pass
class backtrackingContentAssistTest_PreExp(Expression):

    pass
class backtrackingContentAssistTest_PrimitiveLiteralExp(Expression):

    pass
class backtrackingContentAssistTest_LetExp(Expression):

    pass
class backtrackingContentAssistTest_SelfExp(Expression):

    pass
class backtrackingContentAssistTest_PrefixExp(Expression):

    def __init__(self, op: str, backtrackingContentAssistTest_PrefixExp: "backtrackingContentAssistTest_Expression" = None):
        self.op = op
        self.backtrackingContentAssistTest_PrefixExp = backtrackingContentAssistTest_PrefixExp
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def backtrackingContentAssistTest_PrefixExp(self):
        return self.__backtrackingContentAssistTest_PrefixExp

    @backtrackingContentAssistTest_PrefixExp.setter
    def backtrackingContentAssistTest_PrefixExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_PrefixExp__backtrackingContentAssistTest_PrefixExp", None)
        self.__backtrackingContentAssistTest_PrefixExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression142"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression142", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression142"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression142", None)
                setattr(value, "backtrackingContentAssistTest_Expression142", self)

class backtrackingContentAssistTest_SquareBracketExp(Expression):

    def __init__(self, pre: bool, backtrackingContentAssistTest_SquareBracketExp: "backtrackingContentAssistTest_NameExp" = None, backtrackingContentAssistTest_SquareBracketExp108: set["backtrackingContentAssistTest_Expression"] = None):
        self.pre = pre
        self.backtrackingContentAssistTest_SquareBracketExp = backtrackingContentAssistTest_SquareBracketExp
        self.backtrackingContentAssistTest_SquareBracketExp108 = backtrackingContentAssistTest_SquareBracketExp108 if backtrackingContentAssistTest_SquareBracketExp108 is not None else set()
        
    @property
    def pre(self) -> bool:
        return self.__pre

    @pre.setter
    def pre(self, pre: bool):
        self.__pre = pre

    @property
    def backtrackingContentAssistTest_SquareBracketExp108(self):
        return self.__backtrackingContentAssistTest_SquareBracketExp108

    @backtrackingContentAssistTest_SquareBracketExp108.setter
    def backtrackingContentAssistTest_SquareBracketExp108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_SquareBracketExp__backtrackingContentAssistTest_SquareBracketExp108", None)
        self.__backtrackingContentAssistTest_SquareBracketExp108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "backtrackingContentAssistTest_Expression109"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Expression109", None)
                    
                    if opp_val == self:
                        setattr(item, "backtrackingContentAssistTest_Expression109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "backtrackingContentAssistTest_Expression109"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Expression109", None)
                    
                    setattr(item, "backtrackingContentAssistTest_Expression109", self)
                    

    @property
    def backtrackingContentAssistTest_SquareBracketExp(self):
        return self.__backtrackingContentAssistTest_SquareBracketExp

    @backtrackingContentAssistTest_SquareBracketExp.setter
    def backtrackingContentAssistTest_SquareBracketExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_SquareBracketExp__backtrackingContentAssistTest_SquareBracketExp", None)
        self.__backtrackingContentAssistTest_SquareBracketExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_NameExp106"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_NameExp106", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_NameExp106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_NameExp106"):
                opp_val = getattr(value, "backtrackingContentAssistTest_NameExp106", None)
                setattr(value, "backtrackingContentAssistTest_NameExp106", self)

class backtrackingContentAssistTest_IfExp(Expression):

    pass
class backtrackingContentAssistTest_RoundBracketExp(Expression):

    def __init__(self, pre: bool, backtrackingContentAssistTest_RoundBracketExp98: "backtrackingContentAssistTest_iteratorVariable" = None, backtrackingContentAssistTest_RoundBracketExp101: "backtrackingContentAssistTest_EObject" = None, backtrackingContentAssistTest_RoundBracketExp103: set["backtrackingContentAssistTest_Expression"] = None, backtrackingContentAssistTest_RoundBracketExp: "backtrackingContentAssistTest_NameExp" = None):
        self.pre = pre
        self.backtrackingContentAssistTest_RoundBracketExp98 = backtrackingContentAssistTest_RoundBracketExp98
        self.backtrackingContentAssistTest_RoundBracketExp101 = backtrackingContentAssistTest_RoundBracketExp101
        self.backtrackingContentAssistTest_RoundBracketExp103 = backtrackingContentAssistTest_RoundBracketExp103 if backtrackingContentAssistTest_RoundBracketExp103 is not None else set()
        self.backtrackingContentAssistTest_RoundBracketExp = backtrackingContentAssistTest_RoundBracketExp
        
    @property
    def pre(self) -> bool:
        return self.__pre

    @pre.setter
    def pre(self, pre: bool):
        self.__pre = pre

    @property
    def backtrackingContentAssistTest_RoundBracketExp103(self):
        return self.__backtrackingContentAssistTest_RoundBracketExp103

    @backtrackingContentAssistTest_RoundBracketExp103.setter
    def backtrackingContentAssistTest_RoundBracketExp103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_RoundBracketExp__backtrackingContentAssistTest_RoundBracketExp103", None)
        self.__backtrackingContentAssistTest_RoundBracketExp103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "backtrackingContentAssistTest_Expression104"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Expression104", None)
                    
                    if opp_val == self:
                        setattr(item, "backtrackingContentAssistTest_Expression104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "backtrackingContentAssistTest_Expression104"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Expression104", None)
                    
                    setattr(item, "backtrackingContentAssistTest_Expression104", self)
                    

    @property
    def backtrackingContentAssistTest_RoundBracketExp(self):
        return self.__backtrackingContentAssistTest_RoundBracketExp

    @backtrackingContentAssistTest_RoundBracketExp.setter
    def backtrackingContentAssistTest_RoundBracketExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_RoundBracketExp__backtrackingContentAssistTest_RoundBracketExp", None)
        self.__backtrackingContentAssistTest_RoundBracketExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_NameExp"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_NameExp", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_NameExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_NameExp"):
                opp_val = getattr(value, "backtrackingContentAssistTest_NameExp", None)
                setattr(value, "backtrackingContentAssistTest_NameExp", self)

    @property
    def backtrackingContentAssistTest_RoundBracketExp101(self):
        return self.__backtrackingContentAssistTest_RoundBracketExp101

    @backtrackingContentAssistTest_RoundBracketExp101.setter
    def backtrackingContentAssistTest_RoundBracketExp101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_RoundBracketExp__backtrackingContentAssistTest_RoundBracketExp101", None)
        self.__backtrackingContentAssistTest_RoundBracketExp101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_EObject"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_EObject", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_EObject"):
                opp_val = getattr(value, "backtrackingContentAssistTest_EObject", None)
                setattr(value, "backtrackingContentAssistTest_EObject", self)

    @property
    def backtrackingContentAssistTest_RoundBracketExp98(self):
        return self.__backtrackingContentAssistTest_RoundBracketExp98

    @backtrackingContentAssistTest_RoundBracketExp98.setter
    def backtrackingContentAssistTest_RoundBracketExp98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_RoundBracketExp__backtrackingContentAssistTest_RoundBracketExp98", None)
        self.__backtrackingContentAssistTest_RoundBracketExp98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_iteratorVariable99"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_iteratorVariable99", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_iteratorVariable99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_iteratorVariable99"):
                opp_val = getattr(value, "backtrackingContentAssistTest_iteratorVariable99", None)
                setattr(value, "backtrackingContentAssistTest_iteratorVariable99", self)

class backtrackingContentAssistTest_OclMessage(Expression):

    def __init__(self, op: str, messageName: str, backtrackingContentAssistTest_OclMessage: "backtrackingContentAssistTest_Expression" = None, backtrackingContentAssistTest_OclMessage139: set["backtrackingContentAssistTest_OclMessageArg"] = None):
        self.op = op
        self.messageName = messageName
        self.backtrackingContentAssistTest_OclMessage = backtrackingContentAssistTest_OclMessage
        self.backtrackingContentAssistTest_OclMessage139 = backtrackingContentAssistTest_OclMessage139 if backtrackingContentAssistTest_OclMessage139 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def messageName(self) -> str:
        return self.__messageName

    @messageName.setter
    def messageName(self, messageName: str):
        self.__messageName = messageName

    @property
    def backtrackingContentAssistTest_OclMessage139(self):
        return self.__backtrackingContentAssistTest_OclMessage139

    @backtrackingContentAssistTest_OclMessage139.setter
    def backtrackingContentAssistTest_OclMessage139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_OclMessage__backtrackingContentAssistTest_OclMessage139", None)
        self.__backtrackingContentAssistTest_OclMessage139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "backtrackingContentAssistTest_OclMessageArg140"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_OclMessageArg140", None)
                    
                    if opp_val == self:
                        setattr(item, "backtrackingContentAssistTest_OclMessageArg140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "backtrackingContentAssistTest_OclMessageArg140"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_OclMessageArg140", None)
                    
                    setattr(item, "backtrackingContentAssistTest_OclMessageArg140", self)
                    

    @property
    def backtrackingContentAssistTest_OclMessage(self):
        return self.__backtrackingContentAssistTest_OclMessage

    @backtrackingContentAssistTest_OclMessage.setter
    def backtrackingContentAssistTest_OclMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_OclMessage__backtrackingContentAssistTest_OclMessage", None)
        self.__backtrackingContentAssistTest_OclMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression137"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression137", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression137"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression137", None)
                setattr(value, "backtrackingContentAssistTest_Expression137", self)

class TypeExp:

    pass
class backtrackingContentAssistTest_TupleType(TypeExp):

    def __init__(self, name: str, backtrackingContentAssistTest_TupleType: set["backtrackingContentAssistTest_tuplePart"] = None):
        self.name = name
        self.backtrackingContentAssistTest_TupleType = backtrackingContentAssistTest_TupleType if backtrackingContentAssistTest_TupleType is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def backtrackingContentAssistTest_TupleType(self):
        return self.__backtrackingContentAssistTest_TupleType

    @backtrackingContentAssistTest_TupleType.setter
    def backtrackingContentAssistTest_TupleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_TupleType__backtrackingContentAssistTest_TupleType", None)
        self.__backtrackingContentAssistTest_TupleType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "backtrackingContentAssistTest_tuplePart"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_tuplePart", None)
                    
                    if opp_val == self:
                        setattr(item, "backtrackingContentAssistTest_tuplePart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "backtrackingContentAssistTest_tuplePart"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_tuplePart", None)
                    
                    setattr(item, "backtrackingContentAssistTest_tuplePart", self)
                    

class backtrackingContentAssistTest_CollectionType(CollectionLiteralExp, TypeExp):

    def __init__(self, typeIdentifier: str):
        self.typeIdentifier = typeIdentifier
        
    @property
    def typeIdentifier(self) -> str:
        return self.__typeIdentifier

    @typeIdentifier.setter
    def typeIdentifier(self, typeIdentifier: str):
        self.__typeIdentifier = typeIdentifier

class backtrackingContentAssistTest_NameExp(TypeExp):

    pass
class backtrackingContentAssistTest_PrimitiveType(TypeExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class backtrackingContentAssistTest_CollectionLiteralPart:

    pass
class backtrackingContentAssistTest_CollectionLiteralExp(Expression):

    pass
class PackageRef:

    pass
class backtrackingContentAssistTest_QualifiedPackageRef(PackageRef):

    def __init__(self, namespace: str, backtrackingContentAssistTest_QualifiedPackageRef: "backtrackingContentAssistTest_PackageRef" = None):
        self.namespace = namespace
        self.backtrackingContentAssistTest_QualifiedPackageRef = backtrackingContentAssistTest_QualifiedPackageRef
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def backtrackingContentAssistTest_QualifiedPackageRef(self):
        return self.__backtrackingContentAssistTest_QualifiedPackageRef

    @backtrackingContentAssistTest_QualifiedPackageRef.setter
    def backtrackingContentAssistTest_QualifiedPackageRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_QualifiedPackageRef__backtrackingContentAssistTest_QualifiedPackageRef", None)
        self.__backtrackingContentAssistTest_QualifiedPackageRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_PackageRef68"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_PackageRef68", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_PackageRef68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_PackageRef68"):
                opp_val = getattr(value, "backtrackingContentAssistTest_PackageRef68", None)
                setattr(value, "backtrackingContentAssistTest_PackageRef68", self)

class PropertyRef:

    pass
class backtrackingContentAssistTest_QualifiedPropertyRef(PropertyRef):

    def __init__(self, namespace: str, backtrackingContentAssistTest_QualifiedPropertyRef: "backtrackingContentAssistTest_PropertyRef" = None):
        self.namespace = namespace
        self.backtrackingContentAssistTest_QualifiedPropertyRef = backtrackingContentAssistTest_QualifiedPropertyRef
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def backtrackingContentAssistTest_QualifiedPropertyRef(self):
        return self.__backtrackingContentAssistTest_QualifiedPropertyRef

    @backtrackingContentAssistTest_QualifiedPropertyRef.setter
    def backtrackingContentAssistTest_QualifiedPropertyRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_QualifiedPropertyRef__backtrackingContentAssistTest_QualifiedPropertyRef", None)
        self.__backtrackingContentAssistTest_QualifiedPropertyRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_PropertyRef66"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_PropertyRef66", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_PropertyRef66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_PropertyRef66"):
                opp_val = getattr(value, "backtrackingContentAssistTest_PropertyRef66", None)
                setattr(value, "backtrackingContentAssistTest_PropertyRef66", self)

class backtrackingContentAssistTest_OclMessageArg:

    pass
class backtrackingContentAssistTest_NavigatingExp:

    pass
class OclMessageArg:

    pass
class NavigatingExp:

    pass
class backtrackingContentAssistTest_SimplePropertyRef(PropertyRef):

    def __init__(self, feature: str):
        self.feature = feature
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

class backtrackingContentAssistTest_SimplePackageRef(PackageRef):

    def __init__(self, package: str):
        self.package = package
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

class backtrackingContentAssistTest_PropertyRef:

    pass
class OperationRef:

    pass
class backtrackingContentAssistTest_SimpleOperationRef(OperationRef):

    def __init__(self, operation: str):
        self.operation = operation
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

class backtrackingContentAssistTest_QualifiedOperationRef(OperationRef):

    def __init__(self, namespace: str, backtrackingContentAssistTest_QualifiedOperationRef: "backtrackingContentAssistTest_OperationRef" = None):
        self.namespace = namespace
        self.backtrackingContentAssistTest_QualifiedOperationRef = backtrackingContentAssistTest_QualifiedOperationRef
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def backtrackingContentAssistTest_QualifiedOperationRef(self):
        return self.__backtrackingContentAssistTest_QualifiedOperationRef

    @backtrackingContentAssistTest_QualifiedOperationRef.setter
    def backtrackingContentAssistTest_QualifiedOperationRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_QualifiedOperationRef__backtrackingContentAssistTest_QualifiedOperationRef", None)
        self.__backtrackingContentAssistTest_QualifiedOperationRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_OperationRef64"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_OperationRef64", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_OperationRef64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_OperationRef64"):
                opp_val = getattr(value, "backtrackingContentAssistTest_OperationRef64", None)
                setattr(value, "backtrackingContentAssistTest_OperationRef64", self)

class ClassifierRef:

    pass
class backtrackingContentAssistTest_SimpleClassifierRef(ClassifierRef):

    def __init__(self, classifier: str):
        self.classifier = classifier
        
    @property
    def classifier(self) -> str:
        return self.__classifier

    @classifier.setter
    def classifier(self, classifier: str):
        self.__classifier = classifier

class backtrackingContentAssistTest_QualifiedClassifierRef(ClassifierRef):

    def __init__(self, namespace: str, backtrackingContentAssistTest_QualifiedClassifierRef: "backtrackingContentAssistTest_ClassifierRef" = None):
        self.namespace = namespace
        self.backtrackingContentAssistTest_QualifiedClassifierRef = backtrackingContentAssistTest_QualifiedClassifierRef
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def backtrackingContentAssistTest_QualifiedClassifierRef(self):
        return self.__backtrackingContentAssistTest_QualifiedClassifierRef

    @backtrackingContentAssistTest_QualifiedClassifierRef.setter
    def backtrackingContentAssistTest_QualifiedClassifierRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_QualifiedClassifierRef__backtrackingContentAssistTest_QualifiedClassifierRef", None)
        self.__backtrackingContentAssistTest_QualifiedClassifierRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_ClassifierRef62"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_ClassifierRef62", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_ClassifierRef62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_ClassifierRef62"):
                opp_val = getattr(value, "backtrackingContentAssistTest_ClassifierRef62", None)
                setattr(value, "backtrackingContentAssistTest_ClassifierRef62", self)

class backtrackingContentAssistTest_Post:

    def __init__(self, constraintName: str, backtrackingContentAssistTest_Post: "backtrackingContentAssistTest_OperationContextDecl" = None, backtrackingContentAssistTest_Post46: "backtrackingContentAssistTest_Expression" = None):
        self.constraintName = constraintName
        self.backtrackingContentAssistTest_Post = backtrackingContentAssistTest_Post
        self.backtrackingContentAssistTest_Post46 = backtrackingContentAssistTest_Post46
        
    @property
    def constraintName(self) -> str:
        return self.__constraintName

    @constraintName.setter
    def constraintName(self, constraintName: str):
        self.__constraintName = constraintName

    @property
    def backtrackingContentAssistTest_Post(self):
        return self.__backtrackingContentAssistTest_Post

    @backtrackingContentAssistTest_Post.setter
    def backtrackingContentAssistTest_Post(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Post__backtrackingContentAssistTest_Post", None)
        self.__backtrackingContentAssistTest_Post = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_OperationContextDecl33"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_OperationContextDecl33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_OperationContextDecl33"):
                opp_val = getattr(value, "backtrackingContentAssistTest_OperationContextDecl33", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_OperationContextDecl33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backtrackingContentAssistTest_Post46(self):
        return self.__backtrackingContentAssistTest_Post46

    @backtrackingContentAssistTest_Post46.setter
    def backtrackingContentAssistTest_Post46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Post__backtrackingContentAssistTest_Post46", None)
        self.__backtrackingContentAssistTest_Post46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression47"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression47"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression47", None)
                setattr(value, "backtrackingContentAssistTest_Expression47", self)

class backtrackingContentAssistTest_Pre:

    def __init__(self, constraintName: str, backtrackingContentAssistTest_Pre: "backtrackingContentAssistTest_OperationContextDecl" = None, backtrackingContentAssistTest_Pre49: "backtrackingContentAssistTest_Expression" = None):
        self.constraintName = constraintName
        self.backtrackingContentAssistTest_Pre = backtrackingContentAssistTest_Pre
        self.backtrackingContentAssistTest_Pre49 = backtrackingContentAssistTest_Pre49
        
    @property
    def constraintName(self) -> str:
        return self.__constraintName

    @constraintName.setter
    def constraintName(self, constraintName: str):
        self.__constraintName = constraintName

    @property
    def backtrackingContentAssistTest_Pre(self):
        return self.__backtrackingContentAssistTest_Pre

    @backtrackingContentAssistTest_Pre.setter
    def backtrackingContentAssistTest_Pre(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Pre__backtrackingContentAssistTest_Pre", None)
        self.__backtrackingContentAssistTest_Pre = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_OperationContextDecl31"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_OperationContextDecl31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_OperationContextDecl31"):
                opp_val = getattr(value, "backtrackingContentAssistTest_OperationContextDecl31", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_OperationContextDecl31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backtrackingContentAssistTest_Pre49(self):
        return self.__backtrackingContentAssistTest_Pre49

    @backtrackingContentAssistTest_Pre49.setter
    def backtrackingContentAssistTest_Pre49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Pre__backtrackingContentAssistTest_Pre49", None)
        self.__backtrackingContentAssistTest_Pre49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression50"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression50"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression50", None)
                setattr(value, "backtrackingContentAssistTest_Expression50", self)

class backtrackingContentAssistTest_PackageRef:

    pass
class backtrackingContentAssistTest_Init:

    pass
class backtrackingContentAssistTest_Der:

    pass
class backtrackingContentAssistTest_OperationRef:

    pass
class backtrackingContentAssistTest_Definition:

    def __init__(self, static: bool, constraintName: str, constrainedName: str, backtrackingContentAssistTest_Definition10: set["backtrackingContentAssistTest_Parameter"] = None, backtrackingContentAssistTest_Definition12: "backtrackingContentAssistTest_TypeExp" = None, backtrackingContentAssistTest_Definition14: "backtrackingContentAssistTest_Expression" = None, backtrackingContentAssistTest_Definition: "backtrackingContentAssistTest_ClassifierContextDecl" = None):
        self.static = static
        self.constraintName = constraintName
        self.constrainedName = constrainedName
        self.backtrackingContentAssistTest_Definition10 = backtrackingContentAssistTest_Definition10 if backtrackingContentAssistTest_Definition10 is not None else set()
        self.backtrackingContentAssistTest_Definition12 = backtrackingContentAssistTest_Definition12
        self.backtrackingContentAssistTest_Definition14 = backtrackingContentAssistTest_Definition14
        self.backtrackingContentAssistTest_Definition = backtrackingContentAssistTest_Definition
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def constraintName(self) -> str:
        return self.__constraintName

    @constraintName.setter
    def constraintName(self, constraintName: str):
        self.__constraintName = constraintName

    @property
    def constrainedName(self) -> str:
        return self.__constrainedName

    @constrainedName.setter
    def constrainedName(self, constrainedName: str):
        self.__constrainedName = constrainedName

    @property
    def backtrackingContentAssistTest_Definition12(self):
        return self.__backtrackingContentAssistTest_Definition12

    @backtrackingContentAssistTest_Definition12.setter
    def backtrackingContentAssistTest_Definition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Definition__backtrackingContentAssistTest_Definition12", None)
        self.__backtrackingContentAssistTest_Definition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TypeExp"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TypeExp", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_TypeExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TypeExp"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TypeExp", None)
                setattr(value, "backtrackingContentAssistTest_TypeExp", self)

    @property
    def backtrackingContentAssistTest_Definition(self):
        return self.__backtrackingContentAssistTest_Definition

    @backtrackingContentAssistTest_Definition.setter
    def backtrackingContentAssistTest_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Definition__backtrackingContentAssistTest_Definition", None)
        self.__backtrackingContentAssistTest_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_ClassifierContextDecl8"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_ClassifierContextDecl8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_ClassifierContextDecl8"):
                opp_val = getattr(value, "backtrackingContentAssistTest_ClassifierContextDecl8", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_ClassifierContextDecl8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backtrackingContentAssistTest_Definition10(self):
        return self.__backtrackingContentAssistTest_Definition10

    @backtrackingContentAssistTest_Definition10.setter
    def backtrackingContentAssistTest_Definition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Definition__backtrackingContentAssistTest_Definition10", None)
        self.__backtrackingContentAssistTest_Definition10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "backtrackingContentAssistTest_Parameter"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "backtrackingContentAssistTest_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "backtrackingContentAssistTest_Parameter"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Parameter", None)
                    
                    setattr(item, "backtrackingContentAssistTest_Parameter", self)
                    

    @property
    def backtrackingContentAssistTest_Definition14(self):
        return self.__backtrackingContentAssistTest_Definition14

    @backtrackingContentAssistTest_Definition14.setter
    def backtrackingContentAssistTest_Definition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Definition__backtrackingContentAssistTest_Definition14", None)
        self.__backtrackingContentAssistTest_Definition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression15"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression15", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression15"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression15", None)
                setattr(value, "backtrackingContentAssistTest_Expression15", self)

class backtrackingContentAssistTest_TypeExp(Expression):

    pass
class backtrackingContentAssistTest_Parameter:

    def __init__(self, name: str, backtrackingContentAssistTest_Parameter: "backtrackingContentAssistTest_Definition" = None, backtrackingContentAssistTest_Parameter26: "backtrackingContentAssistTest_OperationContextDecl" = None, backtrackingContentAssistTest_Parameter43: "backtrackingContentAssistTest_TypeExp" = None):
        self.name = name
        self.backtrackingContentAssistTest_Parameter = backtrackingContentAssistTest_Parameter
        self.backtrackingContentAssistTest_Parameter26 = backtrackingContentAssistTest_Parameter26
        self.backtrackingContentAssistTest_Parameter43 = backtrackingContentAssistTest_Parameter43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def backtrackingContentAssistTest_Parameter(self):
        return self.__backtrackingContentAssistTest_Parameter

    @backtrackingContentAssistTest_Parameter.setter
    def backtrackingContentAssistTest_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Parameter__backtrackingContentAssistTest_Parameter", None)
        self.__backtrackingContentAssistTest_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Definition10"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Definition10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Definition10"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Definition10", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_Definition10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backtrackingContentAssistTest_Parameter43(self):
        return self.__backtrackingContentAssistTest_Parameter43

    @backtrackingContentAssistTest_Parameter43.setter
    def backtrackingContentAssistTest_Parameter43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Parameter__backtrackingContentAssistTest_Parameter43", None)
        self.__backtrackingContentAssistTest_Parameter43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_TypeExp44"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_TypeExp44", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_TypeExp44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_TypeExp44"):
                opp_val = getattr(value, "backtrackingContentAssistTest_TypeExp44", None)
                setattr(value, "backtrackingContentAssistTest_TypeExp44", self)

    @property
    def backtrackingContentAssistTest_Parameter26(self):
        return self.__backtrackingContentAssistTest_Parameter26

    @backtrackingContentAssistTest_Parameter26.setter
    def backtrackingContentAssistTest_Parameter26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Parameter__backtrackingContentAssistTest_Parameter26", None)
        self.__backtrackingContentAssistTest_Parameter26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_OperationContextDecl25"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_OperationContextDecl25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_OperationContextDecl25"):
                opp_val = getattr(value, "backtrackingContentAssistTest_OperationContextDecl25", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_OperationContextDecl25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class backtrackingContentAssistTest_Expression(OclMessageArg, NavigatingExp):

    pass
class backtrackingContentAssistTest_Body:

    def __init__(self, constraintName: str, backtrackingContentAssistTest_Body: "backtrackingContentAssistTest_Expression" = None, backtrackingContentAssistTest_Body36: "backtrackingContentAssistTest_OperationContextDecl" = None):
        self.constraintName = constraintName
        self.backtrackingContentAssistTest_Body = backtrackingContentAssistTest_Body
        self.backtrackingContentAssistTest_Body36 = backtrackingContentAssistTest_Body36
        
    @property
    def constraintName(self) -> str:
        return self.__constraintName

    @constraintName.setter
    def constraintName(self, constraintName: str):
        self.__constraintName = constraintName

    @property
    def backtrackingContentAssistTest_Body36(self):
        return self.__backtrackingContentAssistTest_Body36

    @backtrackingContentAssistTest_Body36.setter
    def backtrackingContentAssistTest_Body36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Body__backtrackingContentAssistTest_Body36", None)
        self.__backtrackingContentAssistTest_Body36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_OperationContextDecl35"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_OperationContextDecl35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_OperationContextDecl35"):
                opp_val = getattr(value, "backtrackingContentAssistTest_OperationContextDecl35", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_OperationContextDecl35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def backtrackingContentAssistTest_Body(self):
        return self.__backtrackingContentAssistTest_Body

    @backtrackingContentAssistTest_Body.setter
    def backtrackingContentAssistTest_Body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Body__backtrackingContentAssistTest_Body", None)
        self.__backtrackingContentAssistTest_Body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression", None)
                setattr(value, "backtrackingContentAssistTest_Expression", self)

class backtrackingContentAssistTest_ContextDecl:

    pass
class backtrackingContentAssistTest_Invariant:

    def __init__(self, constraintName: str, backtrackingContentAssistTest_Invariant: "backtrackingContentAssistTest_ClassifierContextDecl" = None, backtrackingContentAssistTest_Invariant21: "backtrackingContentAssistTest_Expression" = None):
        self.constraintName = constraintName
        self.backtrackingContentAssistTest_Invariant = backtrackingContentAssistTest_Invariant
        self.backtrackingContentAssistTest_Invariant21 = backtrackingContentAssistTest_Invariant21
        
    @property
    def constraintName(self) -> str:
        return self.__constraintName

    @constraintName.setter
    def constraintName(self, constraintName: str):
        self.__constraintName = constraintName

    @property
    def backtrackingContentAssistTest_Invariant21(self):
        return self.__backtrackingContentAssistTest_Invariant21

    @backtrackingContentAssistTest_Invariant21.setter
    def backtrackingContentAssistTest_Invariant21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Invariant__backtrackingContentAssistTest_Invariant21", None)
        self.__backtrackingContentAssistTest_Invariant21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_Expression22"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_Expression22"):
                opp_val = getattr(value, "backtrackingContentAssistTest_Expression22", None)
                setattr(value, "backtrackingContentAssistTest_Expression22", self)

    @property
    def backtrackingContentAssistTest_Invariant(self):
        return self.__backtrackingContentAssistTest_Invariant

    @backtrackingContentAssistTest_Invariant.setter
    def backtrackingContentAssistTest_Invariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_Invariant__backtrackingContentAssistTest_Invariant", None)
        self.__backtrackingContentAssistTest_Invariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_ClassifierContextDecl6"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_ClassifierContextDecl6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_ClassifierContextDecl6"):
                opp_val = getattr(value, "backtrackingContentAssistTest_ClassifierContextDecl6", None)
                if opp_val is None:
                    setattr(value, "backtrackingContentAssistTest_ClassifierContextDecl6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class backtrackingContentAssistTest_ClassifierRef:

    pass
class ContextDecl:

    pass
class backtrackingContentAssistTest_PropertyContextDecl(ContextDecl):

    pass
class backtrackingContentAssistTest_OperationContextDecl(ContextDecl):

    pass
class backtrackingContentAssistTest_ClassifierContextDecl(ContextDecl):

    def __init__(self, selfName: str, backtrackingContentAssistTest_ClassifierContextDecl: "backtrackingContentAssistTest_ClassifierRef" = None, backtrackingContentAssistTest_ClassifierContextDecl6: set["backtrackingContentAssistTest_Invariant"] = None, backtrackingContentAssistTest_ClassifierContextDecl8: set["backtrackingContentAssistTest_Definition"] = None):
        self.selfName = selfName
        self.backtrackingContentAssistTest_ClassifierContextDecl = backtrackingContentAssistTest_ClassifierContextDecl
        self.backtrackingContentAssistTest_ClassifierContextDecl6 = backtrackingContentAssistTest_ClassifierContextDecl6 if backtrackingContentAssistTest_ClassifierContextDecl6 is not None else set()
        self.backtrackingContentAssistTest_ClassifierContextDecl8 = backtrackingContentAssistTest_ClassifierContextDecl8 if backtrackingContentAssistTest_ClassifierContextDecl8 is not None else set()
        
    @property
    def selfName(self) -> str:
        return self.__selfName

    @selfName.setter
    def selfName(self, selfName: str):
        self.__selfName = selfName

    @property
    def backtrackingContentAssistTest_ClassifierContextDecl6(self):
        return self.__backtrackingContentAssistTest_ClassifierContextDecl6

    @backtrackingContentAssistTest_ClassifierContextDecl6.setter
    def backtrackingContentAssistTest_ClassifierContextDecl6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_ClassifierContextDecl__backtrackingContentAssistTest_ClassifierContextDecl6", None)
        self.__backtrackingContentAssistTest_ClassifierContextDecl6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "backtrackingContentAssistTest_Invariant"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Invariant", None)
                    
                    if opp_val == self:
                        setattr(item, "backtrackingContentAssistTest_Invariant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "backtrackingContentAssistTest_Invariant"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Invariant", None)
                    
                    setattr(item, "backtrackingContentAssistTest_Invariant", self)
                    

    @property
    def backtrackingContentAssistTest_ClassifierContextDecl8(self):
        return self.__backtrackingContentAssistTest_ClassifierContextDecl8

    @backtrackingContentAssistTest_ClassifierContextDecl8.setter
    def backtrackingContentAssistTest_ClassifierContextDecl8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_ClassifierContextDecl__backtrackingContentAssistTest_ClassifierContextDecl8", None)
        self.__backtrackingContentAssistTest_ClassifierContextDecl8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "backtrackingContentAssistTest_Definition"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Definition", None)
                    
                    if opp_val == self:
                        setattr(item, "backtrackingContentAssistTest_Definition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "backtrackingContentAssistTest_Definition"):
                    opp_val = getattr(item, "backtrackingContentAssistTest_Definition", None)
                    
                    setattr(item, "backtrackingContentAssistTest_Definition", self)
                    

    @property
    def backtrackingContentAssistTest_ClassifierContextDecl(self):
        return self.__backtrackingContentAssistTest_ClassifierContextDecl

    @backtrackingContentAssistTest_ClassifierContextDecl.setter
    def backtrackingContentAssistTest_ClassifierContextDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_backtrackingContentAssistTest_ClassifierContextDecl__backtrackingContentAssistTest_ClassifierContextDecl", None)
        self.__backtrackingContentAssistTest_ClassifierContextDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backtrackingContentAssistTest_ClassifierRef"):
                opp_val = getattr(old_value, "backtrackingContentAssistTest_ClassifierRef", None)
                if opp_val == self:
                    setattr(old_value, "backtrackingContentAssistTest_ClassifierRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backtrackingContentAssistTest_ClassifierRef"):
                opp_val = getattr(value, "backtrackingContentAssistTest_ClassifierRef", None)
                setattr(value, "backtrackingContentAssistTest_ClassifierRef", self)

class backtrackingContentAssistTest_PackageDeclaration:

    pass
class backtrackingContentAssistTest_Document:

    pass