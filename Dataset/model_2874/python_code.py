from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class CollectionInitialisationExpression:

    pass
class eol_expression_ExpressionList(CollectionInitialisationExpression):

    pass
class eol_expression_ExpressionRange(CollectionInitialisationExpression):

    pass
class OrderedCollection:

    pass
class eol_expression_SequenceExpression(OrderedCollection):

    pass
class UniqueCollection:

    pass
class eol_expression_OrderedSetExpression(UniqueCollection, OrderedCollection):

    pass
class eol_expression_SetExpression(UniqueCollection):

    pass
class CollectionExpression:

    pass
class eol_expression_OrderedCollection(CollectionExpression):

    pass
class eol_expression_UniqueCollection(CollectionExpression):

    pass
class eol_expression_BagExpression(CollectionExpression):

    pass
class SummableExpression:

    pass
class ComparableExpression:

    pass
class eol_expression_IntegerExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class eol_expression_RealExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class eol_expression_StringExpression(ComparableExpression, SummableExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class eol_expression_Statement(ABC):

    pass
class FeatureCallExpression:

    pass
class eol_expression_FOLMethodCallExpression(FeatureCallExpression):

    pass
class eol_expression_PropertyCallExpression(FeatureCallExpression):

    def __init__(self, extended: bool, eol_expression_PropertyCallExpression: "eol_expression_NameExpression" = None):
        self.extended = extended
        self.eol_expression_PropertyCallExpression = eol_expression_PropertyCallExpression
        
    @property
    def extended(self) -> bool:
        return self.__extended

    @extended.setter
    def extended(self, extended: bool):
        self.__extended = extended

    @property
    def eol_expression_PropertyCallExpression(self):
        return self.__eol_expression_PropertyCallExpression

    @eol_expression_PropertyCallExpression.setter
    def eol_expression_PropertyCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_PropertyCallExpression__eol_expression_PropertyCallExpression", None)
        self.__eol_expression_PropertyCallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_NameExpression17"):
                opp_val = getattr(old_value, "eol_expression_NameExpression17", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_NameExpression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_NameExpression17"):
                opp_val = getattr(value, "eol_expression_NameExpression17", None)
                setattr(value, "eol_expression_NameExpression17", self)

class eol_expression_MethodCallExpression(FeatureCallExpression):

    pass
class PrimitiveExpression:

    pass
class eol_expression_BooleanExpression(PrimitiveExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class eol_expression_SummableExpression(PrimitiveExpression):

    pass
class eol_expression_ComparableExpression(PrimitiveExpression):

    pass
class ComparisonOperatorExpression:

    pass
class eol_expression_NotEqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_expression_LessThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_expression_EqualsOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_expression_LessThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_expression_GreaterThanOperatorExpression(ComparisonOperatorExpression):

    pass
class eol_expression_GreaterThanOrEqualToOperatorExpression(ComparisonOperatorExpression):

    pass
class ArithmeticOperatorExpression:

    pass
class eol_expression_PlusOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_expression_MultiplyOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_expression_MinusOperatorExpression(ArithmeticOperatorExpression):

    pass
class eol_expression_DivideOperatorExpression(ArithmeticOperatorExpression):

    pass
class LogicalOperatorExpression:

    pass
class eol_expression_ImpliesOperatorExpression(LogicalOperatorExpression):

    pass
class eol_expression_XorOperatorExpression(LogicalOperatorExpression):

    pass
class eol_expression_OrOperatorExpression(LogicalOperatorExpression):

    pass
class eol_expression_AndOperatorExpression(LogicalOperatorExpression):

    pass
class BinaryOperatorExpression:

    pass
class eol_expression_ArithmeticOperatorExpression(BinaryOperatorExpression):

    pass
class eol_expression_ComparisonOperatorExpression(BinaryOperatorExpression):

    pass
class eol_expression_LogicalOperatorExpression(BinaryOperatorExpression):

    pass
class UnaryOperatorExpression:

    pass
class eol_expression_NegativeOperatorExpression(UnaryOperatorExpression):

    pass
class eol_expression_NotOperatorExpression(UnaryOperatorExpression):

    pass
class OperatorExpression:

    pass
class eol_expression_BinaryOperatorExpression(OperatorExpression):

    pass
class eol_expression_UnaryOperatorExpression(OperatorExpression):

    pass
class VariableDeclarationExpression:

    pass
class eol_expression_FormalParameterExpression(VariableDeclarationExpression):

    pass
class eol_expression_Expression(ABC):

    def __init__(self, inBrackets: bool, eol_expression_Expression: "eol_expression_Type" = None, eol_expression_Expression10: "eol_expression_FeatureCallExpression" = None, eol_expression_Expression2: "eol_expression_UnaryOperatorExpression" = None, eol_expression_Expression4: "eol_expression_BinaryOperatorExpression" = None, eol_expression_Expression7: "eol_expression_BinaryOperatorExpression" = None, eol_expression_Expression38: "eol_expression_CollectionExpression" = None, eol_expression_Expression12: "eol_expression_MethodCallExpression" = None, eol_expression_Expression21: "eol_expression_FOLMethodCallExpression" = None, eol_expression_Expression26: "eol_expression_KeyValueExpression" = None, eol_expression_Expression29: "eol_expression_KeyValueExpression" = None, eol_expression_Expression34: "eol_expression_NewExpression" = None, eol_expression_Expression50: "eol_expression_ExpressionRange" = None, eol_expression_Expression53: "eol_expression_ExpressionRange" = None, eol_expression_Expression55: "eol_expression_ExpressionList" = None):
        self.inBrackets = inBrackets
        self.eol_expression_Expression = eol_expression_Expression
        self.eol_expression_Expression10 = eol_expression_Expression10
        self.eol_expression_Expression2 = eol_expression_Expression2
        self.eol_expression_Expression4 = eol_expression_Expression4
        self.eol_expression_Expression7 = eol_expression_Expression7
        self.eol_expression_Expression38 = eol_expression_Expression38
        self.eol_expression_Expression12 = eol_expression_Expression12
        self.eol_expression_Expression21 = eol_expression_Expression21
        self.eol_expression_Expression26 = eol_expression_Expression26
        self.eol_expression_Expression29 = eol_expression_Expression29
        self.eol_expression_Expression34 = eol_expression_Expression34
        self.eol_expression_Expression50 = eol_expression_Expression50
        self.eol_expression_Expression53 = eol_expression_Expression53
        self.eol_expression_Expression55 = eol_expression_Expression55
        
    @property
    def inBrackets(self) -> bool:
        return self.__inBrackets

    @inBrackets.setter
    def inBrackets(self, inBrackets: bool):
        self.__inBrackets = inBrackets

    @property
    def eol_expression_Expression38(self):
        return self.__eol_expression_Expression38

    @eol_expression_Expression38.setter
    def eol_expression_Expression38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression38", None)
        self.__eol_expression_Expression38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_CollectionExpression"):
                opp_val = getattr(old_value, "eol_expression_CollectionExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_CollectionExpression"):
                opp_val = getattr(value, "eol_expression_CollectionExpression", None)
                if opp_val is None:
                    setattr(value, "eol_expression_CollectionExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_expression_Expression4(self):
        return self.__eol_expression_Expression4

    @eol_expression_Expression4.setter
    def eol_expression_Expression4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression4", None)
        self.__eol_expression_Expression4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_BinaryOperatorExpression"):
                opp_val = getattr(old_value, "eol_expression_BinaryOperatorExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_BinaryOperatorExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_BinaryOperatorExpression"):
                opp_val = getattr(value, "eol_expression_BinaryOperatorExpression", None)
                setattr(value, "eol_expression_BinaryOperatorExpression", self)

    @property
    def eol_expression_Expression21(self):
        return self.__eol_expression_Expression21

    @eol_expression_Expression21.setter
    def eol_expression_Expression21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression21", None)
        self.__eol_expression_Expression21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_FOLMethodCallExpression20"):
                opp_val = getattr(old_value, "eol_expression_FOLMethodCallExpression20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_FOLMethodCallExpression20"):
                opp_val = getattr(value, "eol_expression_FOLMethodCallExpression20", None)
                if opp_val is None:
                    setattr(value, "eol_expression_FOLMethodCallExpression20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_expression_Expression10(self):
        return self.__eol_expression_Expression10

    @eol_expression_Expression10.setter
    def eol_expression_Expression10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression10", None)
        self.__eol_expression_Expression10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_FeatureCallExpression"):
                opp_val = getattr(old_value, "eol_expression_FeatureCallExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_FeatureCallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_FeatureCallExpression"):
                opp_val = getattr(value, "eol_expression_FeatureCallExpression", None)
                setattr(value, "eol_expression_FeatureCallExpression", self)

    @property
    def eol_expression_Expression12(self):
        return self.__eol_expression_Expression12

    @eol_expression_Expression12.setter
    def eol_expression_Expression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression12", None)
        self.__eol_expression_Expression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_MethodCallExpression"):
                opp_val = getattr(old_value, "eol_expression_MethodCallExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_MethodCallExpression"):
                opp_val = getattr(value, "eol_expression_MethodCallExpression", None)
                if opp_val is None:
                    setattr(value, "eol_expression_MethodCallExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_expression_Expression29(self):
        return self.__eol_expression_Expression29

    @eol_expression_Expression29.setter
    def eol_expression_Expression29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression29", None)
        self.__eol_expression_Expression29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_KeyValueExpression28"):
                opp_val = getattr(old_value, "eol_expression_KeyValueExpression28", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_KeyValueExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_KeyValueExpression28"):
                opp_val = getattr(value, "eol_expression_KeyValueExpression28", None)
                setattr(value, "eol_expression_KeyValueExpression28", self)

    @property
    def eol_expression_Expression(self):
        return self.__eol_expression_Expression

    @eol_expression_Expression.setter
    def eol_expression_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression", None)
        self.__eol_expression_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_Type"):
                opp_val = getattr(old_value, "eol_expression_Type", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_Type"):
                opp_val = getattr(value, "eol_expression_Type", None)
                setattr(value, "eol_expression_Type", self)

    @property
    def eol_expression_Expression34(self):
        return self.__eol_expression_Expression34

    @eol_expression_Expression34.setter
    def eol_expression_Expression34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression34", None)
        self.__eol_expression_Expression34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_NewExpression33"):
                opp_val = getattr(old_value, "eol_expression_NewExpression33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_NewExpression33"):
                opp_val = getattr(value, "eol_expression_NewExpression33", None)
                if opp_val is None:
                    setattr(value, "eol_expression_NewExpression33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_expression_Expression7(self):
        return self.__eol_expression_Expression7

    @eol_expression_Expression7.setter
    def eol_expression_Expression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression7", None)
        self.__eol_expression_Expression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_BinaryOperatorExpression6"):
                opp_val = getattr(old_value, "eol_expression_BinaryOperatorExpression6", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_BinaryOperatorExpression6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_BinaryOperatorExpression6"):
                opp_val = getattr(value, "eol_expression_BinaryOperatorExpression6", None)
                setattr(value, "eol_expression_BinaryOperatorExpression6", self)

    @property
    def eol_expression_Expression55(self):
        return self.__eol_expression_Expression55

    @eol_expression_Expression55.setter
    def eol_expression_Expression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression55", None)
        self.__eol_expression_Expression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_ExpressionList"):
                opp_val = getattr(old_value, "eol_expression_ExpressionList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_ExpressionList"):
                opp_val = getattr(value, "eol_expression_ExpressionList", None)
                if opp_val is None:
                    setattr(value, "eol_expression_ExpressionList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eol_expression_Expression50(self):
        return self.__eol_expression_Expression50

    @eol_expression_Expression50.setter
    def eol_expression_Expression50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression50", None)
        self.__eol_expression_Expression50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_ExpressionRange"):
                opp_val = getattr(old_value, "eol_expression_ExpressionRange", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_ExpressionRange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_ExpressionRange"):
                opp_val = getattr(value, "eol_expression_ExpressionRange", None)
                setattr(value, "eol_expression_ExpressionRange", self)

    @property
    def eol_expression_Expression2(self):
        return self.__eol_expression_Expression2

    @eol_expression_Expression2.setter
    def eol_expression_Expression2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression2", None)
        self.__eol_expression_Expression2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_UnaryOperatorExpression"):
                opp_val = getattr(old_value, "eol_expression_UnaryOperatorExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_UnaryOperatorExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_UnaryOperatorExpression"):
                opp_val = getattr(value, "eol_expression_UnaryOperatorExpression", None)
                setattr(value, "eol_expression_UnaryOperatorExpression", self)

    @property
    def eol_expression_Expression26(self):
        return self.__eol_expression_Expression26

    @eol_expression_Expression26.setter
    def eol_expression_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression26", None)
        self.__eol_expression_Expression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_KeyValueExpression"):
                opp_val = getattr(old_value, "eol_expression_KeyValueExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_KeyValueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_KeyValueExpression"):
                opp_val = getattr(value, "eol_expression_KeyValueExpression", None)
                setattr(value, "eol_expression_KeyValueExpression", self)

    @property
    def eol_expression_Expression53(self):
        return self.__eol_expression_Expression53

    @eol_expression_Expression53.setter
    def eol_expression_Expression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_Expression__eol_expression_Expression53", None)
        self.__eol_expression_Expression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_ExpressionRange52"):
                opp_val = getattr(old_value, "eol_expression_ExpressionRange52", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_ExpressionRange52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_ExpressionRange52"):
                opp_val = getattr(value, "eol_expression_ExpressionRange52", None)
                setattr(value, "eol_expression_ExpressionRange52", self)

class Expression:

    pass
class eol_expression_CollectionExpression(Expression):

    pass
class eol_expression_VariableDeclarationExpression(Expression):

    def __init__(self, create: bool, eol_expression_VariableDeclarationExpression: "eol_expression_NameExpression" = None):
        self.create = create
        self.eol_expression_VariableDeclarationExpression = eol_expression_VariableDeclarationExpression
        
    @property
    def create(self) -> bool:
        return self.__create

    @create.setter
    def create(self, create: bool):
        self.__create = create

    @property
    def eol_expression_VariableDeclarationExpression(self):
        return self.__eol_expression_VariableDeclarationExpression

    @eol_expression_VariableDeclarationExpression.setter
    def eol_expression_VariableDeclarationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_VariableDeclarationExpression__eol_expression_VariableDeclarationExpression", None)
        self.__eol_expression_VariableDeclarationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_NameExpression"):
                opp_val = getattr(old_value, "eol_expression_NameExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_NameExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_NameExpression"):
                opp_val = getattr(value, "eol_expression_NameExpression", None)
                setattr(value, "eol_expression_NameExpression", self)

class eol_expression_NameExpression(Expression):

    def __init__(self, name: str, isType: bool, eol_expression_NameExpression: "eol_expression_VariableDeclarationExpression" = None, eol_expression_NameExpression15: "eol_expression_MethodCallExpression" = None, eol_expression_NameExpression17: "eol_expression_PropertyCallExpression" = None, eol_expression_NameExpression24: "eol_expression_FOLMethodCallExpression" = None, eol_expression_NameExpression31: "eol_expression_NewExpression" = None, eol_expression_NameExpression42: "eol_expression_EnumerationLiteralExpression" = None, eol_expression_NameExpression45: "eol_expression_EnumerationLiteralExpression" = None, eol_expression_NameExpression48: "eol_expression_EnumerationLiteralExpression" = None):
        self.name = name
        self.isType = isType
        self.eol_expression_NameExpression = eol_expression_NameExpression
        self.eol_expression_NameExpression15 = eol_expression_NameExpression15
        self.eol_expression_NameExpression17 = eol_expression_NameExpression17
        self.eol_expression_NameExpression24 = eol_expression_NameExpression24
        self.eol_expression_NameExpression31 = eol_expression_NameExpression31
        self.eol_expression_NameExpression42 = eol_expression_NameExpression42
        self.eol_expression_NameExpression45 = eol_expression_NameExpression45
        self.eol_expression_NameExpression48 = eol_expression_NameExpression48
        
    @property
    def isType(self) -> bool:
        return self.__isType

    @isType.setter
    def isType(self, isType: bool):
        self.__isType = isType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eol_expression_NameExpression42(self):
        return self.__eol_expression_NameExpression42

    @eol_expression_NameExpression42.setter
    def eol_expression_NameExpression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_NameExpression__eol_expression_NameExpression42", None)
        self.__eol_expression_NameExpression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_EnumerationLiteralExpression"):
                opp_val = getattr(old_value, "eol_expression_EnumerationLiteralExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_EnumerationLiteralExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_EnumerationLiteralExpression"):
                opp_val = getattr(value, "eol_expression_EnumerationLiteralExpression", None)
                setattr(value, "eol_expression_EnumerationLiteralExpression", self)

    @property
    def eol_expression_NameExpression45(self):
        return self.__eol_expression_NameExpression45

    @eol_expression_NameExpression45.setter
    def eol_expression_NameExpression45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_NameExpression__eol_expression_NameExpression45", None)
        self.__eol_expression_NameExpression45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_EnumerationLiteralExpression44"):
                opp_val = getattr(old_value, "eol_expression_EnumerationLiteralExpression44", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_EnumerationLiteralExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_EnumerationLiteralExpression44"):
                opp_val = getattr(value, "eol_expression_EnumerationLiteralExpression44", None)
                setattr(value, "eol_expression_EnumerationLiteralExpression44", self)

    @property
    def eol_expression_NameExpression(self):
        return self.__eol_expression_NameExpression

    @eol_expression_NameExpression.setter
    def eol_expression_NameExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_NameExpression__eol_expression_NameExpression", None)
        self.__eol_expression_NameExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_VariableDeclarationExpression"):
                opp_val = getattr(old_value, "eol_expression_VariableDeclarationExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_VariableDeclarationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_VariableDeclarationExpression"):
                opp_val = getattr(value, "eol_expression_VariableDeclarationExpression", None)
                setattr(value, "eol_expression_VariableDeclarationExpression", self)

    @property
    def eol_expression_NameExpression48(self):
        return self.__eol_expression_NameExpression48

    @eol_expression_NameExpression48.setter
    def eol_expression_NameExpression48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_NameExpression__eol_expression_NameExpression48", None)
        self.__eol_expression_NameExpression48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_EnumerationLiteralExpression47"):
                opp_val = getattr(old_value, "eol_expression_EnumerationLiteralExpression47", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_EnumerationLiteralExpression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_EnumerationLiteralExpression47"):
                opp_val = getattr(value, "eol_expression_EnumerationLiteralExpression47", None)
                setattr(value, "eol_expression_EnumerationLiteralExpression47", self)

    @property
    def eol_expression_NameExpression17(self):
        return self.__eol_expression_NameExpression17

    @eol_expression_NameExpression17.setter
    def eol_expression_NameExpression17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_NameExpression__eol_expression_NameExpression17", None)
        self.__eol_expression_NameExpression17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_PropertyCallExpression"):
                opp_val = getattr(old_value, "eol_expression_PropertyCallExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_PropertyCallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_PropertyCallExpression"):
                opp_val = getattr(value, "eol_expression_PropertyCallExpression", None)
                setattr(value, "eol_expression_PropertyCallExpression", self)

    @property
    def eol_expression_NameExpression31(self):
        return self.__eol_expression_NameExpression31

    @eol_expression_NameExpression31.setter
    def eol_expression_NameExpression31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_NameExpression__eol_expression_NameExpression31", None)
        self.__eol_expression_NameExpression31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_NewExpression"):
                opp_val = getattr(old_value, "eol_expression_NewExpression", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_NewExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_NewExpression"):
                opp_val = getattr(value, "eol_expression_NewExpression", None)
                setattr(value, "eol_expression_NewExpression", self)

    @property
    def eol_expression_NameExpression24(self):
        return self.__eol_expression_NameExpression24

    @eol_expression_NameExpression24.setter
    def eol_expression_NameExpression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_NameExpression__eol_expression_NameExpression24", None)
        self.__eol_expression_NameExpression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_FOLMethodCallExpression23"):
                opp_val = getattr(old_value, "eol_expression_FOLMethodCallExpression23", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_FOLMethodCallExpression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_FOLMethodCallExpression23"):
                opp_val = getattr(value, "eol_expression_FOLMethodCallExpression23", None)
                setattr(value, "eol_expression_FOLMethodCallExpression23", self)

    @property
    def eol_expression_NameExpression15(self):
        return self.__eol_expression_NameExpression15

    @eol_expression_NameExpression15.setter
    def eol_expression_NameExpression15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_NameExpression__eol_expression_NameExpression15", None)
        self.__eol_expression_NameExpression15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_MethodCallExpression14"):
                opp_val = getattr(old_value, "eol_expression_MethodCallExpression14", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_MethodCallExpression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_MethodCallExpression14"):
                opp_val = getattr(value, "eol_expression_MethodCallExpression14", None)
                setattr(value, "eol_expression_MethodCallExpression14", self)

class eol_expression_NewExpression(Expression):

    pass
class eol_expression_CollectionInitialisationExpression(Expression):

    pass
class eol_expression_KeyValueExpression(Expression):

    pass
class eol_expression_PrimitiveExpression(Expression):

    pass
class eol_expression_FeatureCallExpression(Expression):

    def __init__(self, arrow: bool, eol_expression_FeatureCallExpression: "eol_expression_Expression" = None):
        self.arrow = arrow
        self.eol_expression_FeatureCallExpression = eol_expression_FeatureCallExpression
        
    @property
    def arrow(self) -> bool:
        return self.__arrow

    @arrow.setter
    def arrow(self, arrow: bool):
        self.__arrow = arrow

    @property
    def eol_expression_FeatureCallExpression(self):
        return self.__eol_expression_FeatureCallExpression

    @eol_expression_FeatureCallExpression.setter
    def eol_expression_FeatureCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eol_expression_FeatureCallExpression__eol_expression_FeatureCallExpression", None)
        self.__eol_expression_FeatureCallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eol_expression_Expression10"):
                opp_val = getattr(old_value, "eol_expression_Expression10", None)
                if opp_val == self:
                    setattr(old_value, "eol_expression_Expression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eol_expression_Expression10"):
                opp_val = getattr(value, "eol_expression_Expression10", None)
                setattr(value, "eol_expression_Expression10", self)

class eol_expression_MapExpression(Expression):

    pass
class eol_expression_EnumerationLiteralExpression(Expression):

    pass
class eol_expression_OperatorExpression(Expression):

    pass
class eol_expression_Type:

    pass