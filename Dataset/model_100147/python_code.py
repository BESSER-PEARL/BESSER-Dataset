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

class InExpression:

    pass
class jPQL_InQueryExpression(InExpression):

    pass
class jPQL_InSeqExpression(InExpression):

    pass
class Value:

    pass
class jPQL_BooleanExpression(Value):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class jPQL_StringExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class jPQL_DateTimeExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class jPQL_NullExpression(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class jPQL_IntegerExpression(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class jPQL_Function:

    def __init__(self, name: str, jPQL_Function: set["jPQL_Variable"] = None):
        self.name = name
        self.jPQL_Function = jPQL_Function if jPQL_Function is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def jPQL_Function(self):
        return self.__jPQL_Function

    @jPQL_Function.setter
    def jPQL_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Function__jPQL_Function", None)
        self.__jPQL_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jPQL_Variable99"):
                    opp_val = getattr(item, "jPQL_Variable99", None)
                    
                    if opp_val == self:
                        setattr(item, "jPQL_Variable99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jPQL_Variable99"):
                    opp_val = getattr(item, "jPQL_Variable99", None)
                    
                    setattr(item, "jPQL_Variable99", self)
                    

class Variable:

    pass
class jPQL_ParameterExpression(Variable):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Expression:

    pass
class jPQL_ExpressionTerm(Expression):

    pass
class jPQL_BetweenExpression(Expression):

    def __init__(self, isNot: bool, jPQL_BetweenExpression: "jPQL_Variable" = None, jPQL_BetweenExpression90: "jPQL_Value" = None, jPQL_BetweenExpression93: "jPQL_Value" = None):
        self.isNot = isNot
        self.jPQL_BetweenExpression = jPQL_BetweenExpression
        self.jPQL_BetweenExpression90 = jPQL_BetweenExpression90
        self.jPQL_BetweenExpression93 = jPQL_BetweenExpression93
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jPQL_BetweenExpression90(self):
        return self.__jPQL_BetweenExpression90

    @jPQL_BetweenExpression90.setter
    def jPQL_BetweenExpression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_BetweenExpression__jPQL_BetweenExpression90", None)
        self.__jPQL_BetweenExpression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Value91"):
                opp_val = getattr(old_value, "jPQL_Value91", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Value91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Value91"):
                opp_val = getattr(value, "jPQL_Value91", None)
                setattr(value, "jPQL_Value91", self)

    @property
    def jPQL_BetweenExpression(self):
        return self.__jPQL_BetweenExpression

    @jPQL_BetweenExpression.setter
    def jPQL_BetweenExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_BetweenExpression__jPQL_BetweenExpression", None)
        self.__jPQL_BetweenExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Variable88"):
                opp_val = getattr(old_value, "jPQL_Variable88", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Variable88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Variable88"):
                opp_val = getattr(value, "jPQL_Variable88", None)
                setattr(value, "jPQL_Variable88", self)

    @property
    def jPQL_BetweenExpression93(self):
        return self.__jPQL_BetweenExpression93

    @jPQL_BetweenExpression93.setter
    def jPQL_BetweenExpression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_BetweenExpression__jPQL_BetweenExpression93", None)
        self.__jPQL_BetweenExpression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Value94"):
                opp_val = getattr(old_value, "jPQL_Value94", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Value94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Value94"):
                opp_val = getattr(value, "jPQL_Value94", None)
                setattr(value, "jPQL_Value94", self)

class jPQL_OrExpression(Expression):

    pass
class jPQL_AndExpression(Expression):

    pass
class jPQL_AnyExpression(Expression):

    pass
class jPQL_ExistsExpression(Expression):

    def __init__(self, isNot: bool, jPQL_ExistsExpression: "jPQL_SelectStatement" = None):
        self.isNot = isNot
        self.jPQL_ExistsExpression = jPQL_ExistsExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jPQL_ExistsExpression(self):
        return self.__jPQL_ExistsExpression

    @jPQL_ExistsExpression.setter
    def jPQL_ExistsExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_ExistsExpression__jPQL_ExistsExpression", None)
        self.__jPQL_ExistsExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_SelectStatement63"):
                opp_val = getattr(old_value, "jPQL_SelectStatement63", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_SelectStatement63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_SelectStatement63"):
                opp_val = getattr(value, "jPQL_SelectStatement63", None)
                setattr(value, "jPQL_SelectStatement63", self)

class jPQL_InExpression(Expression):

    def __init__(self, isNot: bool, jPQL_InExpression: "jPQL_Variable" = None):
        self.isNot = isNot
        self.jPQL_InExpression = jPQL_InExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jPQL_InExpression(self):
        return self.__jPQL_InExpression

    @jPQL_InExpression.setter
    def jPQL_InExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_InExpression__jPQL_InExpression", None)
        self.__jPQL_InExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Variable82"):
                opp_val = getattr(old_value, "jPQL_Variable82", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Variable82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Variable82"):
                opp_val = getattr(value, "jPQL_Variable82", None)
                setattr(value, "jPQL_Variable82", self)

class jPQL_AllExpression(Expression):

    pass
class jPQL_SomeExpression(Expression):

    pass
class jPQL_OperatorExpression(Expression):

    def __init__(self, operator: str, jPQL_OperatorExpression: "jPQL_Variable" = None, jPQL_OperatorExpression61: "jPQL_ExpressionTerm" = None):
        self.operator = operator
        self.jPQL_OperatorExpression = jPQL_OperatorExpression
        self.jPQL_OperatorExpression61 = jPQL_OperatorExpression61
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def jPQL_OperatorExpression(self):
        return self.__jPQL_OperatorExpression

    @jPQL_OperatorExpression.setter
    def jPQL_OperatorExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_OperatorExpression__jPQL_OperatorExpression", None)
        self.__jPQL_OperatorExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Variable"):
                opp_val = getattr(old_value, "jPQL_Variable", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Variable"):
                opp_val = getattr(value, "jPQL_Variable", None)
                setattr(value, "jPQL_Variable", self)

    @property
    def jPQL_OperatorExpression61(self):
        return self.__jPQL_OperatorExpression61

    @jPQL_OperatorExpression61.setter
    def jPQL_OperatorExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_OperatorExpression__jPQL_OperatorExpression61", None)
        self.__jPQL_OperatorExpression61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_ExpressionTerm"):
                opp_val = getattr(old_value, "jPQL_ExpressionTerm", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_ExpressionTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_ExpressionTerm"):
                opp_val = getattr(value, "jPQL_ExpressionTerm", None)
                setattr(value, "jPQL_ExpressionTerm", self)

class jPQL_LikeExpression(Expression):

    def __init__(self, isNot: bool, pattern: str, jPQL_LikeExpression: "jPQL_Variable" = None):
        self.isNot = isNot
        self.pattern = pattern
        self.jPQL_LikeExpression = jPQL_LikeExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def jPQL_LikeExpression(self):
        return self.__jPQL_LikeExpression

    @jPQL_LikeExpression.setter
    def jPQL_LikeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_LikeExpression__jPQL_LikeExpression", None)
        self.__jPQL_LikeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Variable80"):
                opp_val = getattr(old_value, "jPQL_Variable80", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Variable80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Variable80"):
                opp_val = getattr(value, "jPQL_Variable80", None)
                setattr(value, "jPQL_Variable80", self)

class jPQL_EmptyComparisonExpression(Expression):

    def __init__(self, isNot: bool, jPQL_EmptyComparisonExpression: "jPQL_Variable" = None):
        self.isNot = isNot
        self.jPQL_EmptyComparisonExpression = jPQL_EmptyComparisonExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jPQL_EmptyComparisonExpression(self):
        return self.__jPQL_EmptyComparisonExpression

    @jPQL_EmptyComparisonExpression.setter
    def jPQL_EmptyComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_EmptyComparisonExpression__jPQL_EmptyComparisonExpression", None)
        self.__jPQL_EmptyComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Variable78"):
                opp_val = getattr(old_value, "jPQL_Variable78", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Variable78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Variable78"):
                opp_val = getattr(value, "jPQL_Variable78", None)
                setattr(value, "jPQL_Variable78", self)

class jPQL_NullComparisonExpression(Expression):

    def __init__(self, isNot: bool, jPQL_NullComparisonExpression: "jPQL_Variable" = None):
        self.isNot = isNot
        self.jPQL_NullComparisonExpression = jPQL_NullComparisonExpression
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jPQL_NullComparisonExpression(self):
        return self.__jPQL_NullComparisonExpression

    @jPQL_NullComparisonExpression.setter
    def jPQL_NullComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_NullComparisonExpression__jPQL_NullComparisonExpression", None)
        self.__jPQL_NullComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Variable76"):
                opp_val = getattr(old_value, "jPQL_Variable76", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Variable76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Variable76"):
                opp_val = getattr(value, "jPQL_Variable76", None)
                setattr(value, "jPQL_Variable76", self)

class jPQL_CollectionExpression(Expression):

    def __init__(self, isNot: bool, jPQL_CollectionExpression: "jPQL_Variable" = None, jPQL_CollectionExpression73: "jPQL_AliasAttributeExpression" = None):
        self.isNot = isNot
        self.jPQL_CollectionExpression = jPQL_CollectionExpression
        self.jPQL_CollectionExpression73 = jPQL_CollectionExpression73
        
        pass
    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jPQL_CollectionExpression73(self):
        return self.__jPQL_CollectionExpression73

    @jPQL_CollectionExpression73.setter
    def jPQL_CollectionExpression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_CollectionExpression__jPQL_CollectionExpression73", None)
        self.__jPQL_CollectionExpression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_AliasAttributeExpression74"):
                opp_val = getattr(old_value, "jPQL_AliasAttributeExpression74", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_AliasAttributeExpression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_AliasAttributeExpression74"):
                opp_val = getattr(value, "jPQL_AliasAttributeExpression74", None)
                setattr(value, "jPQL_AliasAttributeExpression74", self)

    @property
    def jPQL_CollectionExpression(self):
        return self.__jPQL_CollectionExpression

    @jPQL_CollectionExpression.setter
    def jPQL_CollectionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_CollectionExpression__jPQL_CollectionExpression", None)
        self.__jPQL_CollectionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Variable71"):
                opp_val = getattr(old_value, "jPQL_Variable71", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Variable71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Variable71"):
                opp_val = getattr(value, "jPQL_Variable71", None)
                setattr(value, "jPQL_Variable71", self)

class jPQL_JvmType:

    pass
class FromEntry:

    pass
class jPQL_FromClass(FromEntry):

    pass
class jPQL_VariableDeclaration:

    def __init__(self, name: str, jPQL_VariableDeclaration55: "jPQL_FromJoin" = None, jPQL_VariableDeclaration: "jPQL_FromEntry" = None, jPQL_VariableDeclaration97: "jPQL_AliasAttributeExpression" = None):
        self.name = name
        self.jPQL_VariableDeclaration55 = jPQL_VariableDeclaration55
        self.jPQL_VariableDeclaration = jPQL_VariableDeclaration
        self.jPQL_VariableDeclaration97 = jPQL_VariableDeclaration97
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def jPQL_VariableDeclaration(self):
        return self.__jPQL_VariableDeclaration

    @jPQL_VariableDeclaration.setter
    def jPQL_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_VariableDeclaration__jPQL_VariableDeclaration", None)
        self.__jPQL_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FromEntry44"):
                opp_val = getattr(old_value, "jPQL_FromEntry44", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FromEntry44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromEntry44"):
                opp_val = getattr(value, "jPQL_FromEntry44", None)
                setattr(value, "jPQL_FromEntry44", self)

    @property
    def jPQL_VariableDeclaration97(self):
        return self.__jPQL_VariableDeclaration97

    @jPQL_VariableDeclaration97.setter
    def jPQL_VariableDeclaration97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_VariableDeclaration__jPQL_VariableDeclaration97", None)
        self.__jPQL_VariableDeclaration97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_AliasAttributeExpression96"):
                opp_val = getattr(old_value, "jPQL_AliasAttributeExpression96", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_AliasAttributeExpression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_AliasAttributeExpression96"):
                opp_val = getattr(value, "jPQL_AliasAttributeExpression96", None)
                setattr(value, "jPQL_AliasAttributeExpression96", self)

    @property
    def jPQL_VariableDeclaration55(self):
        return self.__jPQL_VariableDeclaration55

    @jPQL_VariableDeclaration55.setter
    def jPQL_VariableDeclaration55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_VariableDeclaration__jPQL_VariableDeclaration55", None)
        self.__jPQL_VariableDeclaration55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FromJoin54"):
                opp_val = getattr(old_value, "jPQL_FromJoin54", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FromJoin54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromJoin54"):
                opp_val = getattr(value, "jPQL_FromJoin54", None)
                setattr(value, "jPQL_FromJoin54", self)

class SelectAggregateExpression:

    pass
class jPQL_SumAggregate(SelectAggregateExpression):

    pass
class jPQL_CountAggregate(SelectAggregateExpression):

    pass
class jPQL_MaxAggregate(SelectAggregateExpression):

    pass
class jPQL_MinAggregate(SelectAggregateExpression):

    pass
class jPQL_AvgAggregate(SelectAggregateExpression):

    pass
class SelectExpression:

    pass
class jPQL_SelectConstructorExpression(SelectExpression):

    def __init__(self, name: str, jPQL_SelectConstructorExpression: set["jPQL_AliasAttributeExpression"] = None):
        self.name = name
        self.jPQL_SelectConstructorExpression = jPQL_SelectConstructorExpression if jPQL_SelectConstructorExpression is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def jPQL_SelectConstructorExpression(self):
        return self.__jPQL_SelectConstructorExpression

    @jPQL_SelectConstructorExpression.setter
    def jPQL_SelectConstructorExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_SelectConstructorExpression__jPQL_SelectConstructorExpression", None)
        self.__jPQL_SelectConstructorExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jPQL_AliasAttributeExpression39"):
                    opp_val = getattr(item, "jPQL_AliasAttributeExpression39", None)
                    
                    if opp_val == self:
                        setattr(item, "jPQL_AliasAttributeExpression39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jPQL_AliasAttributeExpression39"):
                    opp_val = getattr(item, "jPQL_AliasAttributeExpression39", None)
                    
                    setattr(item, "jPQL_AliasAttributeExpression39", self)
                    

class jPQL_SelectAggregateExpression(SelectExpression):

    def __init__(self, isDistinct: bool, jPQL_SelectAggregateExpression: "jPQL_AliasAttributeExpression" = None):
        self.isDistinct = isDistinct
        self.jPQL_SelectAggregateExpression = jPQL_SelectAggregateExpression
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def jPQL_SelectAggregateExpression(self):
        return self.__jPQL_SelectAggregateExpression

    @jPQL_SelectAggregateExpression.setter
    def jPQL_SelectAggregateExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_SelectAggregateExpression__jPQL_SelectAggregateExpression", None)
        self.__jPQL_SelectAggregateExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_AliasAttributeExpression37"):
                opp_val = getattr(old_value, "jPQL_AliasAttributeExpression37", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_AliasAttributeExpression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_AliasAttributeExpression37"):
                opp_val = getattr(value, "jPQL_AliasAttributeExpression37", None)
                setattr(value, "jPQL_AliasAttributeExpression37", self)

class FromJoin:

    pass
class jPQL_InnerJoin(FromJoin):

    pass
class jPQL_LeftJoin(FromJoin):

    def __init__(self, isOuter: bool):
        self.isOuter = isOuter
        
        pass
    @property
    def isOuter(self):
        return self.__isOuter

    @isOuter.setter
    def isOuter(self, isOuter: bool):
        self.__isOuter = isOuter


class jPQL_Join(FromJoin):

    pass
class jPQL_FromCollection(FromEntry):

    pass
class jPQL_FromJoin:

    def __init__(self, isFetch: bool, jPQL_FromJoin: "jPQL_FromClass" = None, jPQL_FromJoin51: "jPQL_AliasAttributeExpression" = None, jPQL_FromJoin54: "jPQL_VariableDeclaration" = None):
        self.isFetch = isFetch
        self.jPQL_FromJoin = jPQL_FromJoin
        self.jPQL_FromJoin51 = jPQL_FromJoin51
        self.jPQL_FromJoin54 = jPQL_FromJoin54
        
        pass
    @property
    def isFetch(self):
        return self.__isFetch

    @isFetch.setter
    def isFetch(self, isFetch: bool):
        self.__isFetch = isFetch


    @property
    def jPQL_FromJoin54(self):
        return self.__jPQL_FromJoin54

    @jPQL_FromJoin54.setter
    def jPQL_FromJoin54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FromJoin__jPQL_FromJoin54", None)
        self.__jPQL_FromJoin54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_VariableDeclaration55"):
                opp_val = getattr(old_value, "jPQL_VariableDeclaration55", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_VariableDeclaration55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_VariableDeclaration55"):
                opp_val = getattr(value, "jPQL_VariableDeclaration55", None)
                setattr(value, "jPQL_VariableDeclaration55", self)

    @property
    def jPQL_FromJoin51(self):
        return self.__jPQL_FromJoin51

    @jPQL_FromJoin51.setter
    def jPQL_FromJoin51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FromJoin__jPQL_FromJoin51", None)
        self.__jPQL_FromJoin51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_AliasAttributeExpression52"):
                opp_val = getattr(old_value, "jPQL_AliasAttributeExpression52", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_AliasAttributeExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_AliasAttributeExpression52"):
                opp_val = getattr(value, "jPQL_AliasAttributeExpression52", None)
                setattr(value, "jPQL_AliasAttributeExpression52", self)

    @property
    def jPQL_FromJoin(self):
        return self.__jPQL_FromJoin

    @jPQL_FromJoin.setter
    def jPQL_FromJoin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FromJoin__jPQL_FromJoin", None)
        self.__jPQL_FromJoin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FromClass47"):
                opp_val = getattr(old_value, "jPQL_FromClass47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromClass47"):
                opp_val = getattr(value, "jPQL_FromClass47", None)
                if opp_val is None:
                    setattr(value, "jPQL_FromClass47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jPQL_Value(Variable):

    pass
class jPQL_AliasAttributeExpression(Variable, SelectExpression):

    def __init__(self, attributes: str, jPQL_AliasAttributeExpression74: "jPQL_CollectionExpression" = None, jPQL_AliasAttributeExpression: "jPQL_UpdateItem" = None, jPQL_AliasAttributeExpression49: "jPQL_FromCollection" = None, jPQL_AliasAttributeExpression52: "jPQL_FromJoin" = None, jPQL_AliasAttributeExpression37: "jPQL_SelectAggregateExpression" = None, jPQL_AliasAttributeExpression39: "jPQL_SelectConstructorExpression" = None, jPQL_AliasAttributeExpression96: "jPQL_VariableDeclaration" = None):
        self.attributes = attributes
        self.jPQL_AliasAttributeExpression74 = jPQL_AliasAttributeExpression74
        self.jPQL_AliasAttributeExpression = jPQL_AliasAttributeExpression
        self.jPQL_AliasAttributeExpression49 = jPQL_AliasAttributeExpression49
        self.jPQL_AliasAttributeExpression52 = jPQL_AliasAttributeExpression52
        self.jPQL_AliasAttributeExpression37 = jPQL_AliasAttributeExpression37
        self.jPQL_AliasAttributeExpression39 = jPQL_AliasAttributeExpression39
        self.jPQL_AliasAttributeExpression96 = jPQL_AliasAttributeExpression96
        
        pass
    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: str):
        self.__attributes = attributes


    @property
    def jPQL_AliasAttributeExpression74(self):
        return self.__jPQL_AliasAttributeExpression74

    @jPQL_AliasAttributeExpression74.setter
    def jPQL_AliasAttributeExpression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression74", None)
        self.__jPQL_AliasAttributeExpression74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_CollectionExpression73"):
                opp_val = getattr(old_value, "jPQL_CollectionExpression73", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_CollectionExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_CollectionExpression73"):
                opp_val = getattr(value, "jPQL_CollectionExpression73", None)
                setattr(value, "jPQL_CollectionExpression73", self)

    @property
    def jPQL_AliasAttributeExpression39(self):
        return self.__jPQL_AliasAttributeExpression39

    @jPQL_AliasAttributeExpression39.setter
    def jPQL_AliasAttributeExpression39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression39", None)
        self.__jPQL_AliasAttributeExpression39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_SelectConstructorExpression"):
                opp_val = getattr(old_value, "jPQL_SelectConstructorExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_SelectConstructorExpression"):
                opp_val = getattr(value, "jPQL_SelectConstructorExpression", None)
                if opp_val is None:
                    setattr(value, "jPQL_SelectConstructorExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jPQL_AliasAttributeExpression49(self):
        return self.__jPQL_AliasAttributeExpression49

    @jPQL_AliasAttributeExpression49.setter
    def jPQL_AliasAttributeExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression49", None)
        self.__jPQL_AliasAttributeExpression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FromCollection"):
                opp_val = getattr(old_value, "jPQL_FromCollection", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FromCollection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromCollection"):
                opp_val = getattr(value, "jPQL_FromCollection", None)
                setattr(value, "jPQL_FromCollection", self)

    @property
    def jPQL_AliasAttributeExpression96(self):
        return self.__jPQL_AliasAttributeExpression96

    @jPQL_AliasAttributeExpression96.setter
    def jPQL_AliasAttributeExpression96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression96", None)
        self.__jPQL_AliasAttributeExpression96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_VariableDeclaration97"):
                opp_val = getattr(old_value, "jPQL_VariableDeclaration97", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_VariableDeclaration97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_VariableDeclaration97"):
                opp_val = getattr(value, "jPQL_VariableDeclaration97", None)
                setattr(value, "jPQL_VariableDeclaration97", self)

    @property
    def jPQL_AliasAttributeExpression52(self):
        return self.__jPQL_AliasAttributeExpression52

    @jPQL_AliasAttributeExpression52.setter
    def jPQL_AliasAttributeExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression52", None)
        self.__jPQL_AliasAttributeExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FromJoin51"):
                opp_val = getattr(old_value, "jPQL_FromJoin51", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FromJoin51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromJoin51"):
                opp_val = getattr(value, "jPQL_FromJoin51", None)
                setattr(value, "jPQL_FromJoin51", self)

    @property
    def jPQL_AliasAttributeExpression(self):
        return self.__jPQL_AliasAttributeExpression

    @jPQL_AliasAttributeExpression.setter
    def jPQL_AliasAttributeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression", None)
        self.__jPQL_AliasAttributeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_UpdateItem23"):
                opp_val = getattr(old_value, "jPQL_UpdateItem23", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_UpdateItem23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_UpdateItem23"):
                opp_val = getattr(value, "jPQL_UpdateItem23", None)
                setattr(value, "jPQL_UpdateItem23", self)

    @property
    def jPQL_AliasAttributeExpression37(self):
        return self.__jPQL_AliasAttributeExpression37

    @jPQL_AliasAttributeExpression37.setter
    def jPQL_AliasAttributeExpression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression37", None)
        self.__jPQL_AliasAttributeExpression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_SelectAggregateExpression"):
                opp_val = getattr(old_value, "jPQL_SelectAggregateExpression", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_SelectAggregateExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_SelectAggregateExpression"):
                opp_val = getattr(value, "jPQL_SelectAggregateExpression", None)
                setattr(value, "jPQL_SelectAggregateExpression", self)

class jPQL_UpdateItem:

    pass
class jPQL_SetClause:

    pass
class jPQL_UpdateClause:

    pass
class jPQL_FromEntry:

    pass
class jPQL_SelectExpression:

    pass
class jPQL_SelectClause:

    def __init__(self, isDistinct: bool, jPQL_SelectClause: "jPQL_SelectFromClause" = None, jPQL_SelectClause35: set["jPQL_SelectExpression"] = None):
        self.isDistinct = isDistinct
        self.jPQL_SelectClause = jPQL_SelectClause
        self.jPQL_SelectClause35 = jPQL_SelectClause35 if jPQL_SelectClause35 is not None else set()
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def jPQL_SelectClause35(self):
        return self.__jPQL_SelectClause35

    @jPQL_SelectClause35.setter
    def jPQL_SelectClause35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_SelectClause__jPQL_SelectClause35", None)
        self.__jPQL_SelectClause35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jPQL_SelectExpression"):
                    opp_val = getattr(item, "jPQL_SelectExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "jPQL_SelectExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jPQL_SelectExpression"):
                    opp_val = getattr(item, "jPQL_SelectExpression", None)
                    
                    setattr(item, "jPQL_SelectExpression", self)
                    

    @property
    def jPQL_SelectClause(self):
        return self.__jPQL_SelectClause

    @jPQL_SelectClause.setter
    def jPQL_SelectClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_SelectClause__jPQL_SelectClause", None)
        self.__jPQL_SelectClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_SelectFromClause30"):
                opp_val = getattr(old_value, "jPQL_SelectFromClause30", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_SelectFromClause30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_SelectFromClause30"):
                opp_val = getattr(value, "jPQL_SelectFromClause30", None)
                setattr(value, "jPQL_SelectFromClause30", self)

class jPQL_FromClause:

    pass
class jPQL_DeleteClause:

    pass
class jPQL_WhereClause:

    pass
class jPQL_Query:

    pass
class jPQL_QueryModule:

    pass
class jPQL_OrderItem:

    def __init__(self, feature: str, jPQL_OrderItem: "jPQL_OrderClause" = None, jPQL_OrderItem13: "jPQL_FromEntry" = None):
        self.feature = feature
        self.jPQL_OrderItem = jPQL_OrderItem
        self.jPQL_OrderItem13 = jPQL_OrderItem13
        
        pass
    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature


    @property
    def jPQL_OrderItem13(self):
        return self.__jPQL_OrderItem13

    @jPQL_OrderItem13.setter
    def jPQL_OrderItem13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_OrderItem__jPQL_OrderItem13", None)
        self.__jPQL_OrderItem13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FromEntry"):
                opp_val = getattr(old_value, "jPQL_FromEntry", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FromEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromEntry"):
                opp_val = getattr(value, "jPQL_FromEntry", None)
                setattr(value, "jPQL_FromEntry", self)

    @property
    def jPQL_OrderItem(self):
        return self.__jPQL_OrderItem

    @jPQL_OrderItem.setter
    def jPQL_OrderItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_OrderItem__jPQL_OrderItem", None)
        self.__jPQL_OrderItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_OrderClause11"):
                opp_val = getattr(old_value, "jPQL_OrderClause11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_OrderClause11"):
                opp_val = getattr(value, "jPQL_OrderClause11", None)
                if opp_val is None:
                    setattr(value, "jPQL_OrderClause11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jPQL_Expression:

    pass
class jPQL_OrderClause:

    def __init__(self, isAsc: bool, isDesc: bool, jPQL_OrderClause: "jPQL_SelectStatement" = None, jPQL_OrderClause11: set["jPQL_OrderItem"] = None):
        self.isAsc = isAsc
        self.isDesc = isDesc
        self.jPQL_OrderClause = jPQL_OrderClause
        self.jPQL_OrderClause11 = jPQL_OrderClause11 if jPQL_OrderClause11 is not None else set()
        
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
    def jPQL_OrderClause(self):
        return self.__jPQL_OrderClause

    @jPQL_OrderClause.setter
    def jPQL_OrderClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_OrderClause__jPQL_OrderClause", None)
        self.__jPQL_OrderClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_SelectStatement7"):
                opp_val = getattr(old_value, "jPQL_SelectStatement7", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_SelectStatement7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_SelectStatement7"):
                opp_val = getattr(value, "jPQL_SelectStatement7", None)
                setattr(value, "jPQL_SelectStatement7", self)

    @property
    def jPQL_OrderClause11(self):
        return self.__jPQL_OrderClause11

    @jPQL_OrderClause11.setter
    def jPQL_OrderClause11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_OrderClause__jPQL_OrderClause11", None)
        self.__jPQL_OrderClause11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jPQL_OrderItem"):
                    opp_val = getattr(item, "jPQL_OrderItem", None)
                    
                    if opp_val == self:
                        setattr(item, "jPQL_OrderItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jPQL_OrderItem"):
                    opp_val = getattr(item, "jPQL_OrderItem", None)
                    
                    setattr(item, "jPQL_OrderItem", self)
                    

class jPQL_HavingClause:

    pass
class jPQL_SelectFromClause:

    pass
class ExpressionTerm:

    pass
class jPQL_Variable(ExpressionTerm):

    pass
class Query:

    pass
class jPQL_UpdateStatement(Query):

    pass
class jPQL_DeleteStatement(Query):

    pass
class jPQL_SelectStatement(Query, ExpressionTerm):

    pass