from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    lessThen = "lessThen"
    greaterThen = "greaterThen"
    lessEqual = "lessEqual"
    greaterEqual = "greaterEqual"
    equal = "equal"
    notEqual = "notEqual"


############################################
# Definition of Classes
############################################

class Value:

    pass
class jpql_BooleanExpression(Value):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class jpql_NullExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class jpql_StringExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class jpql_IntegerExpression(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class jpql_Function:

    def __init__(self, name: str, jpql_Function: set["jpql_Variable"] = None):
        self.name = name
        self.jpql_Function = jpql_Function if jpql_Function is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def jpql_Function(self):
        return self.__jpql_Function

    @jpql_Function.setter
    def jpql_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_Function__jpql_Function", None)
        self.__jpql_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpql_Variable104"):
                    opp_val = getattr(item, "jpql_Variable104", None)
                    
                    if opp_val == self:
                        setattr(item, "jpql_Variable104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpql_Variable104"):
                    opp_val = getattr(item, "jpql_Variable104", None)
                    
                    setattr(item, "jpql_Variable104", self)
                    

class jpql_DateTimeExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Variable:

    pass
class jpql_ParameterExpression(Variable):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class InExpression:

    pass
class jpql_InQueryExpression(InExpression):

    pass
class jpql_InSeqExpression(InExpression):

    pass
class Expression:

    pass
class jpql_ExpressionTerm(Expression):

    pass
class jpql_InExpression(Expression):

    def __init__(self, isNot: bool, jpql_InExpression: "jpql_Variable" = None):
        self.isNot = isNot
        self.jpql_InExpression = jpql_InExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jpql_InExpression(self):
        return self.__jpql_InExpression

    @jpql_InExpression.setter
    def jpql_InExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_InExpression__jpql_InExpression", None)
        self.__jpql_InExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Variable87"):
                opp_val = getattr(old_value, "jpql_Variable87", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Variable87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Variable87"):
                opp_val = getattr(value, "jpql_Variable87", None)
                setattr(value, "jpql_Variable87", self)

class jpql_OrExpression(Expression):

    pass
class jpql_EmptyComparisonExpression(Expression):

    def __init__(self, isNot: bool, jpql_EmptyComparisonExpression: "jpql_Variable" = None):
        self.isNot = isNot
        self.jpql_EmptyComparisonExpression = jpql_EmptyComparisonExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jpql_EmptyComparisonExpression(self):
        return self.__jpql_EmptyComparisonExpression

    @jpql_EmptyComparisonExpression.setter
    def jpql_EmptyComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_EmptyComparisonExpression__jpql_EmptyComparisonExpression", None)
        self.__jpql_EmptyComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Variable83"):
                opp_val = getattr(old_value, "jpql_Variable83", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Variable83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Variable83"):
                opp_val = getattr(value, "jpql_Variable83", None)
                setattr(value, "jpql_Variable83", self)

class jpql_BetweenExpression(Expression):

    def __init__(self, isNot: bool, jpql_BetweenExpression: "jpql_Variable" = None, jpql_BetweenExpression95: "jpql_Value" = None, jpql_BetweenExpression98: "jpql_Value" = None):
        self.isNot = isNot
        self.jpql_BetweenExpression = jpql_BetweenExpression
        self.jpql_BetweenExpression95 = jpql_BetweenExpression95
        self.jpql_BetweenExpression98 = jpql_BetweenExpression98
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jpql_BetweenExpression(self):
        return self.__jpql_BetweenExpression

    @jpql_BetweenExpression.setter
    def jpql_BetweenExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_BetweenExpression__jpql_BetweenExpression", None)
        self.__jpql_BetweenExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Variable93"):
                opp_val = getattr(old_value, "jpql_Variable93", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Variable93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Variable93"):
                opp_val = getattr(value, "jpql_Variable93", None)
                setattr(value, "jpql_Variable93", self)

    @property
    def jpql_BetweenExpression98(self):
        return self.__jpql_BetweenExpression98

    @jpql_BetweenExpression98.setter
    def jpql_BetweenExpression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_BetweenExpression__jpql_BetweenExpression98", None)
        self.__jpql_BetweenExpression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Value99"):
                opp_val = getattr(old_value, "jpql_Value99", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Value99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Value99"):
                opp_val = getattr(value, "jpql_Value99", None)
                setattr(value, "jpql_Value99", self)

    @property
    def jpql_BetweenExpression95(self):
        return self.__jpql_BetweenExpression95

    @jpql_BetweenExpression95.setter
    def jpql_BetweenExpression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_BetweenExpression__jpql_BetweenExpression95", None)
        self.__jpql_BetweenExpression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Value96"):
                opp_val = getattr(old_value, "jpql_Value96", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Value96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Value96"):
                opp_val = getattr(value, "jpql_Value96", None)
                setattr(value, "jpql_Value96", self)

class jpql_LikeExpression(Expression):

    def __init__(self, isNot: bool, pattern: str, jpql_LikeExpression: "jpql_Variable" = None):
        self.isNot = isNot
        self.pattern = pattern
        self.jpql_LikeExpression = jpql_LikeExpression
        
        pass
    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jpql_LikeExpression(self):
        return self.__jpql_LikeExpression

    @jpql_LikeExpression.setter
    def jpql_LikeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_LikeExpression__jpql_LikeExpression", None)
        self.__jpql_LikeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Variable85"):
                opp_val = getattr(old_value, "jpql_Variable85", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Variable85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Variable85"):
                opp_val = getattr(value, "jpql_Variable85", None)
                setattr(value, "jpql_Variable85", self)

class jpql_AndExpression(Expression):

    pass
class jpql_OperatorExpression(Expression):

    def __init__(self, operator: str, jpql_OperatorExpression: "jpql_Variable" = None, jpql_OperatorExpression66: "jpql_ExpressionTerm" = None):
        self.operator = operator
        self.jpql_OperatorExpression = jpql_OperatorExpression
        self.jpql_OperatorExpression66 = jpql_OperatorExpression66
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def jpql_OperatorExpression(self):
        return self.__jpql_OperatorExpression

    @jpql_OperatorExpression.setter
    def jpql_OperatorExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_OperatorExpression__jpql_OperatorExpression", None)
        self.__jpql_OperatorExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Variable"):
                opp_val = getattr(old_value, "jpql_Variable", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Variable"):
                opp_val = getattr(value, "jpql_Variable", None)
                setattr(value, "jpql_Variable", self)

    @property
    def jpql_OperatorExpression66(self):
        return self.__jpql_OperatorExpression66

    @jpql_OperatorExpression66.setter
    def jpql_OperatorExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_OperatorExpression__jpql_OperatorExpression66", None)
        self.__jpql_OperatorExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_ExpressionTerm"):
                opp_val = getattr(old_value, "jpql_ExpressionTerm", None)
                if opp_val == self:
                    setattr(old_value, "jpql_ExpressionTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_ExpressionTerm"):
                opp_val = getattr(value, "jpql_ExpressionTerm", None)
                setattr(value, "jpql_ExpressionTerm", self)

class FromJoin:

    pass
class jpql_LeftJoin(FromJoin):

    def __init__(self, isOuter: bool):
        self.isOuter = isOuter
        
        pass
    @property
    def isOuter(self):
        return self.__isOuter

    @isOuter.setter
    def isOuter(self, isOuter: bool):
        self.__isOuter = isOuter


class jpql_InnerJoin(FromJoin):

    pass
class jpql_Join(FromJoin):

    pass
class jpql_NullComparisonExpression(Expression):

    def __init__(self, isNot: bool, jpql_NullComparisonExpression: "jpql_Variable" = None):
        self.isNot = isNot
        self.jpql_NullComparisonExpression = jpql_NullComparisonExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jpql_NullComparisonExpression(self):
        return self.__jpql_NullComparisonExpression

    @jpql_NullComparisonExpression.setter
    def jpql_NullComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_NullComparisonExpression__jpql_NullComparisonExpression", None)
        self.__jpql_NullComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Variable81"):
                opp_val = getattr(old_value, "jpql_Variable81", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Variable81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Variable81"):
                opp_val = getattr(value, "jpql_Variable81", None)
                setattr(value, "jpql_Variable81", self)

class jpql_CollectionExpression(Expression):

    def __init__(self, isNot: bool, jpql_CollectionExpression: "jpql_Variable" = None, jpql_CollectionExpression78: "jpql_AliasAttributeExpression" = None):
        self.isNot = isNot
        self.jpql_CollectionExpression = jpql_CollectionExpression
        self.jpql_CollectionExpression78 = jpql_CollectionExpression78
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jpql_CollectionExpression(self):
        return self.__jpql_CollectionExpression

    @jpql_CollectionExpression.setter
    def jpql_CollectionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_CollectionExpression__jpql_CollectionExpression", None)
        self.__jpql_CollectionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_Variable76"):
                opp_val = getattr(old_value, "jpql_Variable76", None)
                if opp_val == self:
                    setattr(old_value, "jpql_Variable76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_Variable76"):
                opp_val = getattr(value, "jpql_Variable76", None)
                setattr(value, "jpql_Variable76", self)

    @property
    def jpql_CollectionExpression78(self):
        return self.__jpql_CollectionExpression78

    @jpql_CollectionExpression78.setter
    def jpql_CollectionExpression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_CollectionExpression__jpql_CollectionExpression78", None)
        self.__jpql_CollectionExpression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_AliasAttributeExpression79"):
                opp_val = getattr(old_value, "jpql_AliasAttributeExpression79", None)
                if opp_val == self:
                    setattr(old_value, "jpql_AliasAttributeExpression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_AliasAttributeExpression79"):
                opp_val = getattr(value, "jpql_AliasAttributeExpression79", None)
                setattr(value, "jpql_AliasAttributeExpression79", self)

class jpql_SomeExpression(Expression):

    pass
class jpql_AnyExpression(Expression):

    pass
class jpql_AllExpression(Expression):

    pass
class jpql_ExistsExpression(Expression):

    def __init__(self, isNot: bool, jpql_ExistsExpression: "jpql_SelectStatement" = None):
        self.isNot = isNot
        self.jpql_ExistsExpression = jpql_ExistsExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jpql_ExistsExpression(self):
        return self.__jpql_ExistsExpression

    @jpql_ExistsExpression.setter
    def jpql_ExistsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_ExistsExpression__jpql_ExistsExpression", None)
        self.__jpql_ExistsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_SelectStatement68"):
                opp_val = getattr(old_value, "jpql_SelectStatement68", None)
                if opp_val == self:
                    setattr(old_value, "jpql_SelectStatement68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_SelectStatement68"):
                opp_val = getattr(value, "jpql_SelectStatement68", None)
                setattr(value, "jpql_SelectStatement68", self)

class SelectAggregateExpression:

    pass
class jpql_CountAggregate(SelectAggregateExpression):

    pass
class jpql_SumAggregate(SelectAggregateExpression):

    pass
class jpql_MaxAggregate(SelectAggregateExpression):

    pass
class jpql_MinAggregate(SelectAggregateExpression):

    pass
class jpql_AvgAggregate(SelectAggregateExpression):

    pass
class SelectExpression:

    pass
class jpql_SelectConstructorExpression(SelectExpression):

    def __init__(self, name: str, jpql_SelectConstructorExpression: set["jpql_AliasAttributeExpression"] = None):
        self.name = name
        self.jpql_SelectConstructorExpression = jpql_SelectConstructorExpression if jpql_SelectConstructorExpression is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def jpql_SelectConstructorExpression(self):
        return self.__jpql_SelectConstructorExpression

    @jpql_SelectConstructorExpression.setter
    def jpql_SelectConstructorExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_SelectConstructorExpression__jpql_SelectConstructorExpression", None)
        self.__jpql_SelectConstructorExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpql_AliasAttributeExpression46"):
                    opp_val = getattr(item, "jpql_AliasAttributeExpression46", None)
                    
                    if opp_val == self:
                        setattr(item, "jpql_AliasAttributeExpression46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpql_AliasAttributeExpression46"):
                    opp_val = getattr(item, "jpql_AliasAttributeExpression46", None)
                    
                    setattr(item, "jpql_AliasAttributeExpression46", self)
                    

class jpql_SelectAggregateExpression(SelectExpression):

    def __init__(self, isDistinct: bool, jpql_SelectAggregateExpression: "jpql_AliasAttributeExpression" = None):
        self.isDistinct = isDistinct
        self.jpql_SelectAggregateExpression = jpql_SelectAggregateExpression
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def jpql_SelectAggregateExpression(self):
        return self.__jpql_SelectAggregateExpression

    @jpql_SelectAggregateExpression.setter
    def jpql_SelectAggregateExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_SelectAggregateExpression__jpql_SelectAggregateExpression", None)
        self.__jpql_SelectAggregateExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_AliasAttributeExpression44"):
                opp_val = getattr(old_value, "jpql_AliasAttributeExpression44", None)
                if opp_val == self:
                    setattr(old_value, "jpql_AliasAttributeExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_AliasAttributeExpression44"):
                opp_val = getattr(value, "jpql_AliasAttributeExpression44", None)
                setattr(value, "jpql_AliasAttributeExpression44", self)

class jpql_SelectExpression:

    pass
class jpql_FromJoin:

    def __init__(self, isFetch: bool, jpql_FromJoin: "jpql_FromClass" = None, jpql_FromJoin56: "jpql_AliasAttributeExpression" = None, jpql_FromJoin59: "jpql_VariableDeclaration" = None):
        self.isFetch = isFetch
        self.jpql_FromJoin = jpql_FromJoin
        self.jpql_FromJoin56 = jpql_FromJoin56
        self.jpql_FromJoin59 = jpql_FromJoin59
        
        pass
    @property
    def isFetch(self):
        return self.__isFetch

    @isFetch.setter
    def isFetch(self, isFetch: bool):
        self.__isFetch = isFetch


    @property
    def jpql_FromJoin59(self):
        return self.__jpql_FromJoin59

    @jpql_FromJoin59.setter
    def jpql_FromJoin59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_FromJoin__jpql_FromJoin59", None)
        self.__jpql_FromJoin59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_VariableDeclaration60"):
                opp_val = getattr(old_value, "jpql_VariableDeclaration60", None)
                if opp_val == self:
                    setattr(old_value, "jpql_VariableDeclaration60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_VariableDeclaration60"):
                opp_val = getattr(value, "jpql_VariableDeclaration60", None)
                setattr(value, "jpql_VariableDeclaration60", self)

    @property
    def jpql_FromJoin(self):
        return self.__jpql_FromJoin

    @jpql_FromJoin.setter
    def jpql_FromJoin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_FromJoin__jpql_FromJoin", None)
        self.__jpql_FromJoin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_FromClass"):
                opp_val = getattr(old_value, "jpql_FromClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_FromClass"):
                opp_val = getattr(value, "jpql_FromClass", None)
                if opp_val is None:
                    setattr(value, "jpql_FromClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpql_FromJoin56(self):
        return self.__jpql_FromJoin56

    @jpql_FromJoin56.setter
    def jpql_FromJoin56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_FromJoin__jpql_FromJoin56", None)
        self.__jpql_FromJoin56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_AliasAttributeExpression57"):
                opp_val = getattr(old_value, "jpql_AliasAttributeExpression57", None)
                if opp_val == self:
                    setattr(old_value, "jpql_AliasAttributeExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_AliasAttributeExpression57"):
                opp_val = getattr(value, "jpql_AliasAttributeExpression57", None)
                setattr(value, "jpql_AliasAttributeExpression57", self)

class FromEntry:

    pass
class jpql_FromCollection(FromEntry):

    pass
class jpql_FromClass(FromEntry):

    def __init__(self, type: str, jpql_FromClass: set["jpql_FromJoin"] = None):
        self.type = type
        self.jpql_FromClass = jpql_FromClass if jpql_FromClass is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def jpql_FromClass(self):
        return self.__jpql_FromClass

    @jpql_FromClass.setter
    def jpql_FromClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_FromClass__jpql_FromClass", None)
        self.__jpql_FromClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpql_FromJoin"):
                    opp_val = getattr(item, "jpql_FromJoin", None)
                    
                    if opp_val == self:
                        setattr(item, "jpql_FromJoin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpql_FromJoin"):
                    opp_val = getattr(item, "jpql_FromJoin", None)
                    
                    setattr(item, "jpql_FromJoin", self)
                    

class jpql_VariableDeclaration:

    def __init__(self, name: str, jpql_VariableDeclaration: "jpql_FromEntry" = None, jpql_VariableDeclaration60: "jpql_FromJoin" = None, jpql_VariableDeclaration102: "jpql_AliasAttributeExpression" = None):
        self.name = name
        self.jpql_VariableDeclaration = jpql_VariableDeclaration
        self.jpql_VariableDeclaration60 = jpql_VariableDeclaration60
        self.jpql_VariableDeclaration102 = jpql_VariableDeclaration102
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def jpql_VariableDeclaration102(self):
        return self.__jpql_VariableDeclaration102

    @jpql_VariableDeclaration102.setter
    def jpql_VariableDeclaration102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_VariableDeclaration__jpql_VariableDeclaration102", None)
        self.__jpql_VariableDeclaration102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_AliasAttributeExpression101"):
                opp_val = getattr(old_value, "jpql_AliasAttributeExpression101", None)
                if opp_val == self:
                    setattr(old_value, "jpql_AliasAttributeExpression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_AliasAttributeExpression101"):
                opp_val = getattr(value, "jpql_AliasAttributeExpression101", None)
                setattr(value, "jpql_AliasAttributeExpression101", self)

    @property
    def jpql_VariableDeclaration60(self):
        return self.__jpql_VariableDeclaration60

    @jpql_VariableDeclaration60.setter
    def jpql_VariableDeclaration60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_VariableDeclaration__jpql_VariableDeclaration60", None)
        self.__jpql_VariableDeclaration60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_FromJoin59"):
                opp_val = getattr(old_value, "jpql_FromJoin59", None)
                if opp_val == self:
                    setattr(old_value, "jpql_FromJoin59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_FromJoin59"):
                opp_val = getattr(value, "jpql_FromJoin59", None)
                setattr(value, "jpql_FromJoin59", self)

    @property
    def jpql_VariableDeclaration(self):
        return self.__jpql_VariableDeclaration

    @jpql_VariableDeclaration.setter
    def jpql_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_VariableDeclaration__jpql_VariableDeclaration", None)
        self.__jpql_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_FromEntry51"):
                opp_val = getattr(old_value, "jpql_FromEntry51", None)
                if opp_val == self:
                    setattr(old_value, "jpql_FromEntry51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_FromEntry51"):
                opp_val = getattr(value, "jpql_FromEntry51", None)
                setattr(value, "jpql_FromEntry51", self)

class jpql_SetClause:

    pass
class jpql_UpdateClause:

    pass
class jpql_FromEntry:

    pass
class jpql_OrderItem:

    def __init__(self, feature: str, jpql_OrderItem: "jpql_OrderClause" = None, jpql_OrderItem20: "jpql_FromEntry" = None):
        self.feature = feature
        self.jpql_OrderItem = jpql_OrderItem
        self.jpql_OrderItem20 = jpql_OrderItem20
        
        pass
    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature


    @property
    def jpql_OrderItem20(self):
        return self.__jpql_OrderItem20

    @jpql_OrderItem20.setter
    def jpql_OrderItem20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_OrderItem__jpql_OrderItem20", None)
        self.__jpql_OrderItem20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_FromEntry"):
                opp_val = getattr(old_value, "jpql_FromEntry", None)
                if opp_val == self:
                    setattr(old_value, "jpql_FromEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_FromEntry"):
                opp_val = getattr(value, "jpql_FromEntry", None)
                setattr(value, "jpql_FromEntry", self)

    @property
    def jpql_OrderItem(self):
        return self.__jpql_OrderItem

    @jpql_OrderItem.setter
    def jpql_OrderItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_OrderItem__jpql_OrderItem", None)
        self.__jpql_OrderItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_OrderClause18"):
                opp_val = getattr(old_value, "jpql_OrderClause18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_OrderClause18"):
                opp_val = getattr(value, "jpql_OrderClause18", None)
                if opp_val is None:
                    setattr(value, "jpql_OrderClause18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpql_Expression:

    pass
class jpql_SelectClause:

    def __init__(self, isDistinct: bool, jpql_SelectClause: "jpql_SelectFromClause" = None, jpql_SelectClause42: set["jpql_SelectExpression"] = None):
        self.isDistinct = isDistinct
        self.jpql_SelectClause = jpql_SelectClause
        self.jpql_SelectClause42 = jpql_SelectClause42 if jpql_SelectClause42 is not None else set()
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def jpql_SelectClause(self):
        return self.__jpql_SelectClause

    @jpql_SelectClause.setter
    def jpql_SelectClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_SelectClause__jpql_SelectClause", None)
        self.__jpql_SelectClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_SelectFromClause37"):
                opp_val = getattr(old_value, "jpql_SelectFromClause37", None)
                if opp_val == self:
                    setattr(old_value, "jpql_SelectFromClause37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_SelectFromClause37"):
                opp_val = getattr(value, "jpql_SelectFromClause37", None)
                setattr(value, "jpql_SelectFromClause37", self)

    @property
    def jpql_SelectClause42(self):
        return self.__jpql_SelectClause42

    @jpql_SelectClause42.setter
    def jpql_SelectClause42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_SelectClause__jpql_SelectClause42", None)
        self.__jpql_SelectClause42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpql_SelectExpression"):
                    opp_val = getattr(item, "jpql_SelectExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "jpql_SelectExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpql_SelectExpression"):
                    opp_val = getattr(item, "jpql_SelectExpression", None)
                    
                    setattr(item, "jpql_SelectExpression", self)
                    

class jpql_FromClause:

    pass
class jpql_DeleteClause:

    pass
class jpql_Value(Variable):

    pass
class jpql_AliasAttributeExpression(SelectExpression, Variable):

    def __init__(self, attributes: str, jpql_AliasAttributeExpression46: "jpql_SelectConstructorExpression" = None, jpql_AliasAttributeExpression54: "jpql_FromCollection" = None, jpql_AliasAttributeExpression57: "jpql_FromJoin" = None, jpql_AliasAttributeExpression44: "jpql_SelectAggregateExpression" = None, jpql_AliasAttributeExpression79: "jpql_CollectionExpression" = None, jpql_AliasAttributeExpression101: "jpql_VariableDeclaration" = None, jpql_AliasAttributeExpression: "jpql_UpdateItem" = None):
        self.attributes = attributes
        self.jpql_AliasAttributeExpression46 = jpql_AliasAttributeExpression46
        self.jpql_AliasAttributeExpression54 = jpql_AliasAttributeExpression54
        self.jpql_AliasAttributeExpression57 = jpql_AliasAttributeExpression57
        self.jpql_AliasAttributeExpression44 = jpql_AliasAttributeExpression44
        self.jpql_AliasAttributeExpression79 = jpql_AliasAttributeExpression79
        self.jpql_AliasAttributeExpression101 = jpql_AliasAttributeExpression101
        self.jpql_AliasAttributeExpression = jpql_AliasAttributeExpression
        
        pass
    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: str):
        self.__attributes = attributes


    @property
    def jpql_AliasAttributeExpression44(self):
        return self.__jpql_AliasAttributeExpression44

    @jpql_AliasAttributeExpression44.setter
    def jpql_AliasAttributeExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_AliasAttributeExpression__jpql_AliasAttributeExpression44", None)
        self.__jpql_AliasAttributeExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_SelectAggregateExpression"):
                opp_val = getattr(old_value, "jpql_SelectAggregateExpression", None)
                if opp_val == self:
                    setattr(old_value, "jpql_SelectAggregateExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_SelectAggregateExpression"):
                opp_val = getattr(value, "jpql_SelectAggregateExpression", None)
                setattr(value, "jpql_SelectAggregateExpression", self)

    @property
    def jpql_AliasAttributeExpression101(self):
        return self.__jpql_AliasAttributeExpression101

    @jpql_AliasAttributeExpression101.setter
    def jpql_AliasAttributeExpression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_AliasAttributeExpression__jpql_AliasAttributeExpression101", None)
        self.__jpql_AliasAttributeExpression101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_VariableDeclaration102"):
                opp_val = getattr(old_value, "jpql_VariableDeclaration102", None)
                if opp_val == self:
                    setattr(old_value, "jpql_VariableDeclaration102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_VariableDeclaration102"):
                opp_val = getattr(value, "jpql_VariableDeclaration102", None)
                setattr(value, "jpql_VariableDeclaration102", self)

    @property
    def jpql_AliasAttributeExpression46(self):
        return self.__jpql_AliasAttributeExpression46

    @jpql_AliasAttributeExpression46.setter
    def jpql_AliasAttributeExpression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_AliasAttributeExpression__jpql_AliasAttributeExpression46", None)
        self.__jpql_AliasAttributeExpression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_SelectConstructorExpression"):
                opp_val = getattr(old_value, "jpql_SelectConstructorExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_SelectConstructorExpression"):
                opp_val = getattr(value, "jpql_SelectConstructorExpression", None)
                if opp_val is None:
                    setattr(value, "jpql_SelectConstructorExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpql_AliasAttributeExpression79(self):
        return self.__jpql_AliasAttributeExpression79

    @jpql_AliasAttributeExpression79.setter
    def jpql_AliasAttributeExpression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_AliasAttributeExpression__jpql_AliasAttributeExpression79", None)
        self.__jpql_AliasAttributeExpression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_CollectionExpression78"):
                opp_val = getattr(old_value, "jpql_CollectionExpression78", None)
                if opp_val == self:
                    setattr(old_value, "jpql_CollectionExpression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_CollectionExpression78"):
                opp_val = getattr(value, "jpql_CollectionExpression78", None)
                setattr(value, "jpql_CollectionExpression78", self)

    @property
    def jpql_AliasAttributeExpression(self):
        return self.__jpql_AliasAttributeExpression

    @jpql_AliasAttributeExpression.setter
    def jpql_AliasAttributeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_AliasAttributeExpression__jpql_AliasAttributeExpression", None)
        self.__jpql_AliasAttributeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_UpdateItem30"):
                opp_val = getattr(old_value, "jpql_UpdateItem30", None)
                if opp_val == self:
                    setattr(old_value, "jpql_UpdateItem30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_UpdateItem30"):
                opp_val = getattr(value, "jpql_UpdateItem30", None)
                setattr(value, "jpql_UpdateItem30", self)

    @property
    def jpql_AliasAttributeExpression54(self):
        return self.__jpql_AliasAttributeExpression54

    @jpql_AliasAttributeExpression54.setter
    def jpql_AliasAttributeExpression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_AliasAttributeExpression__jpql_AliasAttributeExpression54", None)
        self.__jpql_AliasAttributeExpression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_FromCollection"):
                opp_val = getattr(old_value, "jpql_FromCollection", None)
                if opp_val == self:
                    setattr(old_value, "jpql_FromCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_FromCollection"):
                opp_val = getattr(value, "jpql_FromCollection", None)
                setattr(value, "jpql_FromCollection", self)

    @property
    def jpql_AliasAttributeExpression57(self):
        return self.__jpql_AliasAttributeExpression57

    @jpql_AliasAttributeExpression57.setter
    def jpql_AliasAttributeExpression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_AliasAttributeExpression__jpql_AliasAttributeExpression57", None)
        self.__jpql_AliasAttributeExpression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_FromJoin56"):
                opp_val = getattr(old_value, "jpql_FromJoin56", None)
                if opp_val == self:
                    setattr(old_value, "jpql_FromJoin56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_FromJoin56"):
                opp_val = getattr(value, "jpql_FromJoin56", None)
                setattr(value, "jpql_FromJoin56", self)

class jpql_UpdateItem:

    pass
class jpql_Import:

    def __init__(self, importURI: str, jpql_Import: "jpql_QueryModule" = None):
        self.importURI = importURI
        self.jpql_Import = jpql_Import
        
        pass
    @property
    def importURI(self):
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI


    @property
    def jpql_Import(self):
        return self.__jpql_Import

    @jpql_Import.setter
    def jpql_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_Import__jpql_Import", None)
        self.__jpql_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_QueryModule"):
                opp_val = getattr(old_value, "jpql_QueryModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_QueryModule"):
                opp_val = getattr(value, "jpql_QueryModule", None)
                if opp_val is None:
                    setattr(value, "jpql_QueryModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jpql_QueryModule:

    pass
class jpql_OrderClause:

    def __init__(self, isAsc: bool, isDesc: bool, jpql_OrderClause18: set["jpql_OrderItem"] = None, jpql_OrderClause: "jpql_SelectStatement" = None):
        self.isAsc = isAsc
        self.isDesc = isDesc
        self.jpql_OrderClause18 = jpql_OrderClause18 if jpql_OrderClause18 is not None else set()
        self.jpql_OrderClause = jpql_OrderClause
        
        pass
    @property
    def isDesc(self):
        return self.__isDesc

    @isDesc.setter
    def isDesc(self, isDesc: bool):
        self.__isDesc = isDesc


    @property
    def isAsc(self):
        return self.__isAsc

    @isAsc.setter
    def isAsc(self, isAsc: bool):
        self.__isAsc = isAsc


    @property
    def jpql_OrderClause(self):
        return self.__jpql_OrderClause

    @jpql_OrderClause.setter
    def jpql_OrderClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_OrderClause__jpql_OrderClause", None)
        self.__jpql_OrderClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_SelectStatement14"):
                opp_val = getattr(old_value, "jpql_SelectStatement14", None)
                if opp_val == self:
                    setattr(old_value, "jpql_SelectStatement14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_SelectStatement14"):
                opp_val = getattr(value, "jpql_SelectStatement14", None)
                setattr(value, "jpql_SelectStatement14", self)

    @property
    def jpql_OrderClause18(self):
        return self.__jpql_OrderClause18

    @jpql_OrderClause18.setter
    def jpql_OrderClause18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_OrderClause__jpql_OrderClause18", None)
        self.__jpql_OrderClause18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jpql_OrderItem"):
                    opp_val = getattr(item, "jpql_OrderItem", None)
                    
                    if opp_val == self:
                        setattr(item, "jpql_OrderItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jpql_OrderItem"):
                    opp_val = getattr(item, "jpql_OrderItem", None)
                    
                    setattr(item, "jpql_OrderItem", self)
                    

class jpql_HavingClause:

    pass
class jpql_SelectFromClause:

    pass
class ExpressionTerm:

    pass
class jpql_Variable(ExpressionTerm):

    pass
class JPQLQuery:

    pass
class jpql_DeleteStatement(JPQLQuery):

    pass
class jpql_UpdateStatement(JPQLQuery):

    pass
class jpql_SelectStatement(ExpressionTerm, JPQLQuery):

    pass
class jpql_WhereClause:

    pass
class jpql_NamedQuery:

    def __init__(self, name: str, jpql_NamedQuery: "jpql_QueryModule" = None, jpql_NamedQuery6: "jpql_JPQLQuery" = None):
        self.name = name
        self.jpql_NamedQuery = jpql_NamedQuery
        self.jpql_NamedQuery6 = jpql_NamedQuery6
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def jpql_NamedQuery(self):
        return self.__jpql_NamedQuery

    @jpql_NamedQuery.setter
    def jpql_NamedQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_NamedQuery__jpql_NamedQuery", None)
        self.__jpql_NamedQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_QueryModule4"):
                opp_val = getattr(old_value, "jpql_QueryModule4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_QueryModule4"):
                opp_val = getattr(value, "jpql_QueryModule4", None)
                if opp_val is None:
                    setattr(value, "jpql_QueryModule4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jpql_NamedQuery6(self):
        return self.__jpql_NamedQuery6

    @jpql_NamedQuery6.setter
    def jpql_NamedQuery6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jpql_NamedQuery__jpql_NamedQuery6", None)
        self.__jpql_NamedQuery6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jpql_JPQLQuery7"):
                opp_val = getattr(old_value, "jpql_JPQLQuery7", None)
                if opp_val == self:
                    setattr(old_value, "jpql_JPQLQuery7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jpql_JPQLQuery7"):
                opp_val = getattr(value, "jpql_JPQLQuery7", None)
                setattr(value, "jpql_JPQLQuery7", self)

class jpql_JPQLQuery:

    pass