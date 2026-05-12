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
class mql_StringExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class mql_DateTimeExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class mql_BooleanExpression(Value):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class mql_NullExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class mql_IntegerExpression(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class mql_Function:

    def __init__(self, name: str, mql_Function: set["mql_Variable"] = None):
        self.name = name
        self.mql_Function = mql_Function if mql_Function is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mql_Function(self):
        return self.__mql_Function

    @mql_Function.setter
    def mql_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_Function__mql_Function", None)
        self.__mql_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mql_Variable104"):
                    opp_val = getattr(item, "mql_Variable104", None)
                    
                    if opp_val == self:
                        setattr(item, "mql_Variable104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mql_Variable104"):
                    opp_val = getattr(item, "mql_Variable104", None)
                    
                    setattr(item, "mql_Variable104", self)
                    

class Variable:

    pass
class mql_ParameterExpression(Variable):

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
class mql_InQueryExpression(InExpression):

    pass
class mql_InSeqExpression(InExpression):

    pass
class Expression:

    pass
class mql_EmptyComparisonExpression(Expression):

    def __init__(self, isNot: bool, mql_EmptyComparisonExpression: "mql_Variable" = None):
        self.isNot = isNot
        self.mql_EmptyComparisonExpression = mql_EmptyComparisonExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def mql_EmptyComparisonExpression(self):
        return self.__mql_EmptyComparisonExpression

    @mql_EmptyComparisonExpression.setter
    def mql_EmptyComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_EmptyComparisonExpression__mql_EmptyComparisonExpression", None)
        self.__mql_EmptyComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Variable83"):
                opp_val = getattr(old_value, "mql_Variable83", None)
                if opp_val == self:
                    setattr(old_value, "mql_Variable83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Variable83"):
                opp_val = getattr(value, "mql_Variable83", None)
                setattr(value, "mql_Variable83", self)

class mql_AndExpression(Expression):

    pass
class mql_ExistsExpression(Expression):

    def __init__(self, isNot: bool, mql_ExistsExpression: "mql_SelectStatement" = None):
        self.isNot = isNot
        self.mql_ExistsExpression = mql_ExistsExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def mql_ExistsExpression(self):
        return self.__mql_ExistsExpression

    @mql_ExistsExpression.setter
    def mql_ExistsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_ExistsExpression__mql_ExistsExpression", None)
        self.__mql_ExistsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_SelectStatement68"):
                opp_val = getattr(old_value, "mql_SelectStatement68", None)
                if opp_val == self:
                    setattr(old_value, "mql_SelectStatement68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_SelectStatement68"):
                opp_val = getattr(value, "mql_SelectStatement68", None)
                setattr(value, "mql_SelectStatement68", self)

class mql_BetweenExpression(Expression):

    def __init__(self, isNot: bool, mql_BetweenExpression: "mql_Variable" = None, mql_BetweenExpression95: "mql_Value" = None, mql_BetweenExpression98: "mql_Value" = None):
        self.isNot = isNot
        self.mql_BetweenExpression = mql_BetweenExpression
        self.mql_BetweenExpression95 = mql_BetweenExpression95
        self.mql_BetweenExpression98 = mql_BetweenExpression98
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def mql_BetweenExpression95(self):
        return self.__mql_BetweenExpression95

    @mql_BetweenExpression95.setter
    def mql_BetweenExpression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_BetweenExpression__mql_BetweenExpression95", None)
        self.__mql_BetweenExpression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Value96"):
                opp_val = getattr(old_value, "mql_Value96", None)
                if opp_val == self:
                    setattr(old_value, "mql_Value96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Value96"):
                opp_val = getattr(value, "mql_Value96", None)
                setattr(value, "mql_Value96", self)

    @property
    def mql_BetweenExpression98(self):
        return self.__mql_BetweenExpression98

    @mql_BetweenExpression98.setter
    def mql_BetweenExpression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_BetweenExpression__mql_BetweenExpression98", None)
        self.__mql_BetweenExpression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Value99"):
                opp_val = getattr(old_value, "mql_Value99", None)
                if opp_val == self:
                    setattr(old_value, "mql_Value99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Value99"):
                opp_val = getattr(value, "mql_Value99", None)
                setattr(value, "mql_Value99", self)

    @property
    def mql_BetweenExpression(self):
        return self.__mql_BetweenExpression

    @mql_BetweenExpression.setter
    def mql_BetweenExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_BetweenExpression__mql_BetweenExpression", None)
        self.__mql_BetweenExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Variable93"):
                opp_val = getattr(old_value, "mql_Variable93", None)
                if opp_val == self:
                    setattr(old_value, "mql_Variable93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Variable93"):
                opp_val = getattr(value, "mql_Variable93", None)
                setattr(value, "mql_Variable93", self)

class mql_InExpression(Expression):

    def __init__(self, isNot: bool, mql_InExpression: "mql_Variable" = None):
        self.isNot = isNot
        self.mql_InExpression = mql_InExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def mql_InExpression(self):
        return self.__mql_InExpression

    @mql_InExpression.setter
    def mql_InExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_InExpression__mql_InExpression", None)
        self.__mql_InExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Variable87"):
                opp_val = getattr(old_value, "mql_Variable87", None)
                if opp_val == self:
                    setattr(old_value, "mql_Variable87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Variable87"):
                opp_val = getattr(value, "mql_Variable87", None)
                setattr(value, "mql_Variable87", self)

class mql_OrExpression(Expression):

    pass
class mql_AnyExpression(Expression):

    pass
class mql_ExpressionTerm(Expression):

    pass
class mql_LikeExpression(Expression):

    def __init__(self, isNot: bool, pattern: str, mql_LikeExpression: "mql_Variable" = None):
        self.isNot = isNot
        self.pattern = pattern
        self.mql_LikeExpression = mql_LikeExpression
        
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
    def mql_LikeExpression(self):
        return self.__mql_LikeExpression

    @mql_LikeExpression.setter
    def mql_LikeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_LikeExpression__mql_LikeExpression", None)
        self.__mql_LikeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Variable85"):
                opp_val = getattr(old_value, "mql_Variable85", None)
                if opp_val == self:
                    setattr(old_value, "mql_Variable85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Variable85"):
                opp_val = getattr(value, "mql_Variable85", None)
                setattr(value, "mql_Variable85", self)

class mql_NullComparisonExpression(Expression):

    def __init__(self, isNot: bool, mql_NullComparisonExpression: "mql_Variable" = None):
        self.isNot = isNot
        self.mql_NullComparisonExpression = mql_NullComparisonExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def mql_NullComparisonExpression(self):
        return self.__mql_NullComparisonExpression

    @mql_NullComparisonExpression.setter
    def mql_NullComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_NullComparisonExpression__mql_NullComparisonExpression", None)
        self.__mql_NullComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Variable81"):
                opp_val = getattr(old_value, "mql_Variable81", None)
                if opp_val == self:
                    setattr(old_value, "mql_Variable81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Variable81"):
                opp_val = getattr(value, "mql_Variable81", None)
                setattr(value, "mql_Variable81", self)

class mql_SomeExpression(Expression):

    pass
class mql_AllExpression(Expression):

    pass
class mql_CollectionExpression(Expression):

    def __init__(self, isNot: bool, mql_CollectionExpression78: "mql_AliasAttributeExpression" = None, mql_CollectionExpression: "mql_Variable" = None):
        self.isNot = isNot
        self.mql_CollectionExpression78 = mql_CollectionExpression78
        self.mql_CollectionExpression = mql_CollectionExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def mql_CollectionExpression78(self):
        return self.__mql_CollectionExpression78

    @mql_CollectionExpression78.setter
    def mql_CollectionExpression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_CollectionExpression__mql_CollectionExpression78", None)
        self.__mql_CollectionExpression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_AliasAttributeExpression79"):
                opp_val = getattr(old_value, "mql_AliasAttributeExpression79", None)
                if opp_val == self:
                    setattr(old_value, "mql_AliasAttributeExpression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_AliasAttributeExpression79"):
                opp_val = getattr(value, "mql_AliasAttributeExpression79", None)
                setattr(value, "mql_AliasAttributeExpression79", self)

    @property
    def mql_CollectionExpression(self):
        return self.__mql_CollectionExpression

    @mql_CollectionExpression.setter
    def mql_CollectionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_CollectionExpression__mql_CollectionExpression", None)
        self.__mql_CollectionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Variable76"):
                opp_val = getattr(old_value, "mql_Variable76", None)
                if opp_val == self:
                    setattr(old_value, "mql_Variable76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Variable76"):
                opp_val = getattr(value, "mql_Variable76", None)
                setattr(value, "mql_Variable76", self)

class mql_OperatorExpression(Expression):

    def __init__(self, operator: str, mql_OperatorExpression: "mql_Variable" = None, mql_OperatorExpression66: "mql_ExpressionTerm" = None):
        self.operator = operator
        self.mql_OperatorExpression = mql_OperatorExpression
        self.mql_OperatorExpression66 = mql_OperatorExpression66
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def mql_OperatorExpression(self):
        return self.__mql_OperatorExpression

    @mql_OperatorExpression.setter
    def mql_OperatorExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_OperatorExpression__mql_OperatorExpression", None)
        self.__mql_OperatorExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_Variable"):
                opp_val = getattr(old_value, "mql_Variable", None)
                if opp_val == self:
                    setattr(old_value, "mql_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_Variable"):
                opp_val = getattr(value, "mql_Variable", None)
                setattr(value, "mql_Variable", self)

    @property
    def mql_OperatorExpression66(self):
        return self.__mql_OperatorExpression66

    @mql_OperatorExpression66.setter
    def mql_OperatorExpression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_OperatorExpression__mql_OperatorExpression66", None)
        self.__mql_OperatorExpression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_ExpressionTerm"):
                opp_val = getattr(old_value, "mql_ExpressionTerm", None)
                if opp_val == self:
                    setattr(old_value, "mql_ExpressionTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_ExpressionTerm"):
                opp_val = getattr(value, "mql_ExpressionTerm", None)
                setattr(value, "mql_ExpressionTerm", self)

class FromJoin:

    pass
class mql_InnerJoin(FromJoin):

    pass
class mql_LeftJoin(FromJoin):

    def __init__(self, isOuter: bool):
        self.isOuter = isOuter
        
        pass
    @property
    def isOuter(self):
        return self.__isOuter

    @isOuter.setter
    def isOuter(self, isOuter: bool):
        self.__isOuter = isOuter


class mql_Join(FromJoin):

    pass
class mql_SelectClause:

    def __init__(self, isDistinct: bool, mql_SelectClause: "mql_SelectFromClause" = None, mql_SelectClause42: set["mql_SelectExpression"] = None):
        self.isDistinct = isDistinct
        self.mql_SelectClause = mql_SelectClause
        self.mql_SelectClause42 = mql_SelectClause42 if mql_SelectClause42 is not None else set()
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def mql_SelectClause42(self):
        return self.__mql_SelectClause42

    @mql_SelectClause42.setter
    def mql_SelectClause42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_SelectClause__mql_SelectClause42", None)
        self.__mql_SelectClause42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mql_SelectExpression"):
                    opp_val = getattr(item, "mql_SelectExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "mql_SelectExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mql_SelectExpression"):
                    opp_val = getattr(item, "mql_SelectExpression", None)
                    
                    setattr(item, "mql_SelectExpression", self)
                    

    @property
    def mql_SelectClause(self):
        return self.__mql_SelectClause

    @mql_SelectClause.setter
    def mql_SelectClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_SelectClause__mql_SelectClause", None)
        self.__mql_SelectClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_SelectFromClause37"):
                opp_val = getattr(old_value, "mql_SelectFromClause37", None)
                if opp_val == self:
                    setattr(old_value, "mql_SelectFromClause37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_SelectFromClause37"):
                opp_val = getattr(value, "mql_SelectFromClause37", None)
                setattr(value, "mql_SelectFromClause37", self)

class mql_FromJoin:

    def __init__(self, isFetch: bool, mql_FromJoin: "mql_FromClass" = None, mql_FromJoin59: "mql_VariableDeclaration" = None, mql_FromJoin56: "mql_AliasAttributeExpression" = None):
        self.isFetch = isFetch
        self.mql_FromJoin = mql_FromJoin
        self.mql_FromJoin59 = mql_FromJoin59
        self.mql_FromJoin56 = mql_FromJoin56
        
        pass
    @property
    def isFetch(self):
        return self.__isFetch

    @isFetch.setter
    def isFetch(self, isFetch: bool):
        self.__isFetch = isFetch


    @property
    def mql_FromJoin56(self):
        return self.__mql_FromJoin56

    @mql_FromJoin56.setter
    def mql_FromJoin56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_FromJoin__mql_FromJoin56", None)
        self.__mql_FromJoin56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_AliasAttributeExpression57"):
                opp_val = getattr(old_value, "mql_AliasAttributeExpression57", None)
                if opp_val == self:
                    setattr(old_value, "mql_AliasAttributeExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_AliasAttributeExpression57"):
                opp_val = getattr(value, "mql_AliasAttributeExpression57", None)
                setattr(value, "mql_AliasAttributeExpression57", self)

    @property
    def mql_FromJoin(self):
        return self.__mql_FromJoin

    @mql_FromJoin.setter
    def mql_FromJoin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_FromJoin__mql_FromJoin", None)
        self.__mql_FromJoin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_FromClass"):
                opp_val = getattr(old_value, "mql_FromClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_FromClass"):
                opp_val = getattr(value, "mql_FromClass", None)
                if opp_val is None:
                    setattr(value, "mql_FromClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mql_FromJoin59(self):
        return self.__mql_FromJoin59

    @mql_FromJoin59.setter
    def mql_FromJoin59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_FromJoin__mql_FromJoin59", None)
        self.__mql_FromJoin59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_VariableDeclaration60"):
                opp_val = getattr(old_value, "mql_VariableDeclaration60", None)
                if opp_val == self:
                    setattr(old_value, "mql_VariableDeclaration60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_VariableDeclaration60"):
                opp_val = getattr(value, "mql_VariableDeclaration60", None)
                setattr(value, "mql_VariableDeclaration60", self)

class FromEntry:

    pass
class mql_FromCollection(FromEntry):

    pass
class mql_FromClass(FromEntry):

    def __init__(self, type: str, mql_FromClass: set["mql_FromJoin"] = None):
        self.type = type
        self.mql_FromClass = mql_FromClass if mql_FromClass is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def mql_FromClass(self):
        return self.__mql_FromClass

    @mql_FromClass.setter
    def mql_FromClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_FromClass__mql_FromClass", None)
        self.__mql_FromClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mql_FromJoin"):
                    opp_val = getattr(item, "mql_FromJoin", None)
                    
                    if opp_val == self:
                        setattr(item, "mql_FromJoin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mql_FromJoin"):
                    opp_val = getattr(item, "mql_FromJoin", None)
                    
                    setattr(item, "mql_FromJoin", self)
                    

class mql_VariableDeclaration:

    def __init__(self, name: str, mql_VariableDeclaration: "mql_FromEntry" = None, mql_VariableDeclaration60: "mql_FromJoin" = None, mql_VariableDeclaration102: "mql_AliasAttributeExpression" = None):
        self.name = name
        self.mql_VariableDeclaration = mql_VariableDeclaration
        self.mql_VariableDeclaration60 = mql_VariableDeclaration60
        self.mql_VariableDeclaration102 = mql_VariableDeclaration102
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mql_VariableDeclaration(self):
        return self.__mql_VariableDeclaration

    @mql_VariableDeclaration.setter
    def mql_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_VariableDeclaration__mql_VariableDeclaration", None)
        self.__mql_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_FromEntry51"):
                opp_val = getattr(old_value, "mql_FromEntry51", None)
                if opp_val == self:
                    setattr(old_value, "mql_FromEntry51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_FromEntry51"):
                opp_val = getattr(value, "mql_FromEntry51", None)
                setattr(value, "mql_FromEntry51", self)

    @property
    def mql_VariableDeclaration102(self):
        return self.__mql_VariableDeclaration102

    @mql_VariableDeclaration102.setter
    def mql_VariableDeclaration102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_VariableDeclaration__mql_VariableDeclaration102", None)
        self.__mql_VariableDeclaration102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_AliasAttributeExpression101"):
                opp_val = getattr(old_value, "mql_AliasAttributeExpression101", None)
                if opp_val == self:
                    setattr(old_value, "mql_AliasAttributeExpression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_AliasAttributeExpression101"):
                opp_val = getattr(value, "mql_AliasAttributeExpression101", None)
                setattr(value, "mql_AliasAttributeExpression101", self)

    @property
    def mql_VariableDeclaration60(self):
        return self.__mql_VariableDeclaration60

    @mql_VariableDeclaration60.setter
    def mql_VariableDeclaration60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_VariableDeclaration__mql_VariableDeclaration60", None)
        self.__mql_VariableDeclaration60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_FromJoin59"):
                opp_val = getattr(old_value, "mql_FromJoin59", None)
                if opp_val == self:
                    setattr(old_value, "mql_FromJoin59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_FromJoin59"):
                opp_val = getattr(value, "mql_FromJoin59", None)
                setattr(value, "mql_FromJoin59", self)

class SelectAggregateExpression:

    pass
class mql_MaxAggregate(SelectAggregateExpression):

    pass
class mql_MinAggregate(SelectAggregateExpression):

    pass
class mql_SumAggregate(SelectAggregateExpression):

    pass
class mql_CountAggregate(SelectAggregateExpression):

    pass
class mql_AvgAggregate(SelectAggregateExpression):

    pass
class SelectExpression:

    pass
class mql_SelectConstructorExpression(SelectExpression):

    def __init__(self, name: str, mql_SelectConstructorExpression: set["mql_AliasAttributeExpression"] = None):
        self.name = name
        self.mql_SelectConstructorExpression = mql_SelectConstructorExpression if mql_SelectConstructorExpression is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mql_SelectConstructorExpression(self):
        return self.__mql_SelectConstructorExpression

    @mql_SelectConstructorExpression.setter
    def mql_SelectConstructorExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_SelectConstructorExpression__mql_SelectConstructorExpression", None)
        self.__mql_SelectConstructorExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mql_AliasAttributeExpression46"):
                    opp_val = getattr(item, "mql_AliasAttributeExpression46", None)
                    
                    if opp_val == self:
                        setattr(item, "mql_AliasAttributeExpression46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mql_AliasAttributeExpression46"):
                    opp_val = getattr(item, "mql_AliasAttributeExpression46", None)
                    
                    setattr(item, "mql_AliasAttributeExpression46", self)
                    

class mql_SelectAggregateExpression(SelectExpression):

    def __init__(self, isDistinct: bool, mql_SelectAggregateExpression: "mql_AliasAttributeExpression" = None):
        self.isDistinct = isDistinct
        self.mql_SelectAggregateExpression = mql_SelectAggregateExpression
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def mql_SelectAggregateExpression(self):
        return self.__mql_SelectAggregateExpression

    @mql_SelectAggregateExpression.setter
    def mql_SelectAggregateExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_SelectAggregateExpression__mql_SelectAggregateExpression", None)
        self.__mql_SelectAggregateExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_AliasAttributeExpression44"):
                opp_val = getattr(old_value, "mql_AliasAttributeExpression44", None)
                if opp_val == self:
                    setattr(old_value, "mql_AliasAttributeExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_AliasAttributeExpression44"):
                opp_val = getattr(value, "mql_AliasAttributeExpression44", None)
                setattr(value, "mql_AliasAttributeExpression44", self)

class mql_SelectExpression:

    pass
class mql_Expression:

    pass
class mql_OrderClause:

    def __init__(self, isAsc: bool, isDesc: bool, mql_OrderClause18: set["mql_OrderItem"] = None, mql_OrderClause: "mql_SelectStatement" = None):
        self.isAsc = isAsc
        self.isDesc = isDesc
        self.mql_OrderClause18 = mql_OrderClause18 if mql_OrderClause18 is not None else set()
        self.mql_OrderClause = mql_OrderClause
        
        pass
    @property
    def isAsc(self):
        return self.__isAsc

    @isAsc.setter
    def isAsc(self, isAsc: bool):
        self.__isAsc = isAsc


    @property
    def isDesc(self):
        return self.__isDesc

    @isDesc.setter
    def isDesc(self, isDesc: bool):
        self.__isDesc = isDesc


    @property
    def mql_OrderClause(self):
        return self.__mql_OrderClause

    @mql_OrderClause.setter
    def mql_OrderClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_OrderClause__mql_OrderClause", None)
        self.__mql_OrderClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_SelectStatement14"):
                opp_val = getattr(old_value, "mql_SelectStatement14", None)
                if opp_val == self:
                    setattr(old_value, "mql_SelectStatement14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_SelectStatement14"):
                opp_val = getattr(value, "mql_SelectStatement14", None)
                setattr(value, "mql_SelectStatement14", self)

    @property
    def mql_OrderClause18(self):
        return self.__mql_OrderClause18

    @mql_OrderClause18.setter
    def mql_OrderClause18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_OrderClause__mql_OrderClause18", None)
        self.__mql_OrderClause18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mql_OrderItem"):
                    opp_val = getattr(item, "mql_OrderItem", None)
                    
                    if opp_val == self:
                        setattr(item, "mql_OrderItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mql_OrderItem"):
                    opp_val = getattr(item, "mql_OrderItem", None)
                    
                    setattr(item, "mql_OrderItem", self)
                    

class mql_HavingClause:

    pass
class mql_FromClause:

    pass
class mql_DeleteClause:

    pass
class mql_Value(Variable):

    pass
class mql_AliasAttributeExpression(SelectExpression, Variable):

    def __init__(self, attributes: str, mql_AliasAttributeExpression44: "mql_SelectAggregateExpression" = None, mql_AliasAttributeExpression46: "mql_SelectConstructorExpression" = None, mql_AliasAttributeExpression54: "mql_FromCollection" = None, mql_AliasAttributeExpression57: "mql_FromJoin" = None, mql_AliasAttributeExpression79: "mql_CollectionExpression" = None, mql_AliasAttributeExpression101: "mql_VariableDeclaration" = None, mql_AliasAttributeExpression: "mql_UpdateItem" = None):
        self.attributes = attributes
        self.mql_AliasAttributeExpression44 = mql_AliasAttributeExpression44
        self.mql_AliasAttributeExpression46 = mql_AliasAttributeExpression46
        self.mql_AliasAttributeExpression54 = mql_AliasAttributeExpression54
        self.mql_AliasAttributeExpression57 = mql_AliasAttributeExpression57
        self.mql_AliasAttributeExpression79 = mql_AliasAttributeExpression79
        self.mql_AliasAttributeExpression101 = mql_AliasAttributeExpression101
        self.mql_AliasAttributeExpression = mql_AliasAttributeExpression
        
        pass
    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: str):
        self.__attributes = attributes


    @property
    def mql_AliasAttributeExpression(self):
        return self.__mql_AliasAttributeExpression

    @mql_AliasAttributeExpression.setter
    def mql_AliasAttributeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_AliasAttributeExpression__mql_AliasAttributeExpression", None)
        self.__mql_AliasAttributeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_UpdateItem30"):
                opp_val = getattr(old_value, "mql_UpdateItem30", None)
                if opp_val == self:
                    setattr(old_value, "mql_UpdateItem30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_UpdateItem30"):
                opp_val = getattr(value, "mql_UpdateItem30", None)
                setattr(value, "mql_UpdateItem30", self)

    @property
    def mql_AliasAttributeExpression44(self):
        return self.__mql_AliasAttributeExpression44

    @mql_AliasAttributeExpression44.setter
    def mql_AliasAttributeExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_AliasAttributeExpression__mql_AliasAttributeExpression44", None)
        self.__mql_AliasAttributeExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_SelectAggregateExpression"):
                opp_val = getattr(old_value, "mql_SelectAggregateExpression", None)
                if opp_val == self:
                    setattr(old_value, "mql_SelectAggregateExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_SelectAggregateExpression"):
                opp_val = getattr(value, "mql_SelectAggregateExpression", None)
                setattr(value, "mql_SelectAggregateExpression", self)

    @property
    def mql_AliasAttributeExpression79(self):
        return self.__mql_AliasAttributeExpression79

    @mql_AliasAttributeExpression79.setter
    def mql_AliasAttributeExpression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_AliasAttributeExpression__mql_AliasAttributeExpression79", None)
        self.__mql_AliasAttributeExpression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_CollectionExpression78"):
                opp_val = getattr(old_value, "mql_CollectionExpression78", None)
                if opp_val == self:
                    setattr(old_value, "mql_CollectionExpression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_CollectionExpression78"):
                opp_val = getattr(value, "mql_CollectionExpression78", None)
                setattr(value, "mql_CollectionExpression78", self)

    @property
    def mql_AliasAttributeExpression57(self):
        return self.__mql_AliasAttributeExpression57

    @mql_AliasAttributeExpression57.setter
    def mql_AliasAttributeExpression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_AliasAttributeExpression__mql_AliasAttributeExpression57", None)
        self.__mql_AliasAttributeExpression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_FromJoin56"):
                opp_val = getattr(old_value, "mql_FromJoin56", None)
                if opp_val == self:
                    setattr(old_value, "mql_FromJoin56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_FromJoin56"):
                opp_val = getattr(value, "mql_FromJoin56", None)
                setattr(value, "mql_FromJoin56", self)

    @property
    def mql_AliasAttributeExpression54(self):
        return self.__mql_AliasAttributeExpression54

    @mql_AliasAttributeExpression54.setter
    def mql_AliasAttributeExpression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_AliasAttributeExpression__mql_AliasAttributeExpression54", None)
        self.__mql_AliasAttributeExpression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_FromCollection"):
                opp_val = getattr(old_value, "mql_FromCollection", None)
                if opp_val == self:
                    setattr(old_value, "mql_FromCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_FromCollection"):
                opp_val = getattr(value, "mql_FromCollection", None)
                setattr(value, "mql_FromCollection", self)

    @property
    def mql_AliasAttributeExpression46(self):
        return self.__mql_AliasAttributeExpression46

    @mql_AliasAttributeExpression46.setter
    def mql_AliasAttributeExpression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_AliasAttributeExpression__mql_AliasAttributeExpression46", None)
        self.__mql_AliasAttributeExpression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_SelectConstructorExpression"):
                opp_val = getattr(old_value, "mql_SelectConstructorExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_SelectConstructorExpression"):
                opp_val = getattr(value, "mql_SelectConstructorExpression", None)
                if opp_val is None:
                    setattr(value, "mql_SelectConstructorExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mql_AliasAttributeExpression101(self):
        return self.__mql_AliasAttributeExpression101

    @mql_AliasAttributeExpression101.setter
    def mql_AliasAttributeExpression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_AliasAttributeExpression__mql_AliasAttributeExpression101", None)
        self.__mql_AliasAttributeExpression101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_VariableDeclaration102"):
                opp_val = getattr(old_value, "mql_VariableDeclaration102", None)
                if opp_val == self:
                    setattr(old_value, "mql_VariableDeclaration102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_VariableDeclaration102"):
                opp_val = getattr(value, "mql_VariableDeclaration102", None)
                setattr(value, "mql_VariableDeclaration102", self)

class mql_UpdateItem:

    pass
class mql_SetClause:

    pass
class mql_UpdateClause:

    pass
class mql_FromEntry:

    pass
class mql_OrderItem:

    def __init__(self, feature: str, mql_OrderItem: "mql_OrderClause" = None, mql_OrderItem20: "mql_FromEntry" = None):
        self.feature = feature
        self.mql_OrderItem = mql_OrderItem
        self.mql_OrderItem20 = mql_OrderItem20
        
        pass
    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature


    @property
    def mql_OrderItem(self):
        return self.__mql_OrderItem

    @mql_OrderItem.setter
    def mql_OrderItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_OrderItem__mql_OrderItem", None)
        self.__mql_OrderItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_OrderClause18"):
                opp_val = getattr(old_value, "mql_OrderClause18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_OrderClause18"):
                opp_val = getattr(value, "mql_OrderClause18", None)
                if opp_val is None:
                    setattr(value, "mql_OrderClause18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mql_OrderItem20(self):
        return self.__mql_OrderItem20

    @mql_OrderItem20.setter
    def mql_OrderItem20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_OrderItem__mql_OrderItem20", None)
        self.__mql_OrderItem20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_FromEntry"):
                opp_val = getattr(old_value, "mql_FromEntry", None)
                if opp_val == self:
                    setattr(old_value, "mql_FromEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_FromEntry"):
                opp_val = getattr(value, "mql_FromEntry", None)
                setattr(value, "mql_FromEntry", self)

class mql_SelectFromClause:

    pass
class ExpressionTerm:

    pass
class mql_Variable(ExpressionTerm):

    pass
class MQuery:

    pass
class mql_UpdateStatement(MQuery):

    pass
class mql_DeleteStatement(MQuery):

    pass
class mql_SelectStatement(ExpressionTerm, MQuery):

    pass
class mql_WhereClause:

    pass
class mql_NamedQuery:

    def __init__(self, name: str, mql_NamedQuery: "mql_QueryModule" = None, mql_NamedQuery6: "mql_MQuery" = None):
        self.name = name
        self.mql_NamedQuery = mql_NamedQuery
        self.mql_NamedQuery6 = mql_NamedQuery6
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mql_NamedQuery6(self):
        return self.__mql_NamedQuery6

    @mql_NamedQuery6.setter
    def mql_NamedQuery6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_NamedQuery__mql_NamedQuery6", None)
        self.__mql_NamedQuery6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_MQuery7"):
                opp_val = getattr(old_value, "mql_MQuery7", None)
                if opp_val == self:
                    setattr(old_value, "mql_MQuery7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_MQuery7"):
                opp_val = getattr(value, "mql_MQuery7", None)
                setattr(value, "mql_MQuery7", self)

    @property
    def mql_NamedQuery(self):
        return self.__mql_NamedQuery

    @mql_NamedQuery.setter
    def mql_NamedQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_NamedQuery__mql_NamedQuery", None)
        self.__mql_NamedQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_QueryModule4"):
                opp_val = getattr(old_value, "mql_QueryModule4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_QueryModule4"):
                opp_val = getattr(value, "mql_QueryModule4", None)
                if opp_val is None:
                    setattr(value, "mql_QueryModule4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mql_MQuery:

    pass
class mql_Import:

    def __init__(self, importURI: str, mql_Import: "mql_QueryModule" = None):
        self.importURI = importURI
        self.mql_Import = mql_Import
        
        pass
    @property
    def importURI(self):
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI


    @property
    def mql_Import(self):
        return self.__mql_Import

    @mql_Import.setter
    def mql_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mql_Import__mql_Import", None)
        self.__mql_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mql_QueryModule"):
                opp_val = getattr(old_value, "mql_QueryModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mql_QueryModule"):
                opp_val = getattr(value, "mql_QueryModule", None)
                if opp_val is None:
                    setattr(value, "mql_QueryModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mql_QueryModule:

    pass