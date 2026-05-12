from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComparisonOperator(Enum):
    lessThen = "lessThen"
    greaterThen = "greaterThen"
    lessEqual = "lessEqual"
    greaterEqual = "greaterEqual"
    equal = "equal"
    notEqual = "notEqual"
class MultiplicationOperator(Enum):
    multiply = "multiply"
    divide = "divide"
class OrderByDirection(Enum):
    asc = "asc"
    desc = "desc"
class AdditionOperator(Enum):
    add = "add"
    subtract = "subtract"
class TrimSpec(Enum):
    leading = "leading"
    trailing = "trailing"
    both = "both"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    logicalNot = "logicalNot"


############################################
# Definition of Classes
############################################

class Variable:

    pass
class jPQL_ParameterExpression(Variable):

    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index


class OrderBySpec:

    pass
class jPQL_Float:

    def __init__(self, integerValue: int, fractionValue: int, jPQL_Float: "jPQL_FloatLiteral" = None):
        self.integerValue = integerValue
        self.fractionValue = fractionValue
        self.jPQL_Float = jPQL_Float
        
        pass
    @property
    def integerValue(self):
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: int):
        self.__integerValue = integerValue


    @property
    def fractionValue(self):
        return self.__fractionValue

    @fractionValue.setter
    def fractionValue(self, fractionValue: int):
        self.__fractionValue = fractionValue


    @property
    def jPQL_Float(self):
        return self.__jPQL_Float

    @jPQL_Float.setter
    def jPQL_Float(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Float__jPQL_Float", None)
        self.__jPQL_Float = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FloatLiteral"):
                opp_val = getattr(old_value, "jPQL_FloatLiteral", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FloatLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FloatLiteral"):
                opp_val = getattr(value, "jPQL_FloatLiteral", None)
                setattr(value, "jPQL_FloatLiteral", self)

class FromJoin:

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


class jPQL_InnerJoin(FromJoin):

    pass
class jPQL_Join(FromJoin):

    pass
class jPQL_FromJoin:

    def __init__(self, isFetch: bool, jPQL_FromJoin: "jPQL_FromClass" = None, jPQL_FromJoin47: "jPQL_AliasAttributeExpression" = None, jPQL_FromJoin50: "jPQL_VariableDeclaration" = None):
        self.isFetch = isFetch
        self.jPQL_FromJoin = jPQL_FromJoin
        self.jPQL_FromJoin47 = jPQL_FromJoin47
        self.jPQL_FromJoin50 = jPQL_FromJoin50
        
        pass
    @property
    def isFetch(self):
        return self.__isFetch

    @isFetch.setter
    def isFetch(self, isFetch: bool):
        self.__isFetch = isFetch


    @property
    def jPQL_FromJoin47(self):
        return self.__jPQL_FromJoin47

    @jPQL_FromJoin47.setter
    def jPQL_FromJoin47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FromJoin__jPQL_FromJoin47", None)
        self.__jPQL_FromJoin47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_AliasAttributeExpression48"):
                opp_val = getattr(old_value, "jPQL_AliasAttributeExpression48", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_AliasAttributeExpression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_AliasAttributeExpression48"):
                opp_val = getattr(value, "jPQL_AliasAttributeExpression48", None)
                setattr(value, "jPQL_AliasAttributeExpression48", self)

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
            if hasattr(old_value, "jPQL_FromClass"):
                opp_val = getattr(old_value, "jPQL_FromClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromClass"):
                opp_val = getattr(value, "jPQL_FromClass", None)
                if opp_val is None:
                    setattr(value, "jPQL_FromClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jPQL_FromJoin50(self):
        return self.__jPQL_FromJoin50

    @jPQL_FromJoin50.setter
    def jPQL_FromJoin50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FromJoin__jPQL_FromJoin50", None)
        self.__jPQL_FromJoin50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_VariableDeclaration51"):
                opp_val = getattr(old_value, "jPQL_VariableDeclaration51", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_VariableDeclaration51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_VariableDeclaration51"):
                opp_val = getattr(value, "jPQL_VariableDeclaration51", None)
                setattr(value, "jPQL_VariableDeclaration51", self)

class Expression:

    pass
class jPQL_ExpressionTerm(Expression):

    pass
class jPQL_FunctionExpression(Expression):

    def __init__(self, name: str, trimSpec: str, jPQL_FunctionExpression: set["jPQL_Expression"] = None, jPQL_FunctionExpression78: "jPQL_Expression" = None, jPQL_FunctionExpression81: "jPQL_Expression" = None, jPQL_FunctionExpression84: "jPQL_Expression" = None, jPQL_FunctionExpression87: "jPQL_Expression" = None):
        self.name = name
        self.trimSpec = trimSpec
        self.jPQL_FunctionExpression = jPQL_FunctionExpression if jPQL_FunctionExpression is not None else set()
        self.jPQL_FunctionExpression78 = jPQL_FunctionExpression78
        self.jPQL_FunctionExpression81 = jPQL_FunctionExpression81
        self.jPQL_FunctionExpression84 = jPQL_FunctionExpression84
        self.jPQL_FunctionExpression87 = jPQL_FunctionExpression87
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def trimSpec(self):
        return self.__trimSpec

    @trimSpec.setter
    def trimSpec(self, trimSpec: str):
        self.__trimSpec = trimSpec


    @property
    def jPQL_FunctionExpression87(self):
        return self.__jPQL_FunctionExpression87

    @jPQL_FunctionExpression87.setter
    def jPQL_FunctionExpression87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FunctionExpression__jPQL_FunctionExpression87", None)
        self.__jPQL_FunctionExpression87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Expression88"):
                opp_val = getattr(old_value, "jPQL_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Expression88"):
                opp_val = getattr(value, "jPQL_Expression88", None)
                setattr(value, "jPQL_Expression88", self)

    @property
    def jPQL_FunctionExpression(self):
        return self.__jPQL_FunctionExpression

    @jPQL_FunctionExpression.setter
    def jPQL_FunctionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FunctionExpression__jPQL_FunctionExpression", None)
        self.__jPQL_FunctionExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jPQL_Expression76"):
                    opp_val = getattr(item, "jPQL_Expression76", None)
                    
                    if opp_val == self:
                        setattr(item, "jPQL_Expression76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jPQL_Expression76"):
                    opp_val = getattr(item, "jPQL_Expression76", None)
                    
                    setattr(item, "jPQL_Expression76", self)
                    

    @property
    def jPQL_FunctionExpression81(self):
        return self.__jPQL_FunctionExpression81

    @jPQL_FunctionExpression81.setter
    def jPQL_FunctionExpression81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FunctionExpression__jPQL_FunctionExpression81", None)
        self.__jPQL_FunctionExpression81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Expression82"):
                opp_val = getattr(old_value, "jPQL_Expression82", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Expression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Expression82"):
                opp_val = getattr(value, "jPQL_Expression82", None)
                setattr(value, "jPQL_Expression82", self)

    @property
    def jPQL_FunctionExpression78(self):
        return self.__jPQL_FunctionExpression78

    @jPQL_FunctionExpression78.setter
    def jPQL_FunctionExpression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FunctionExpression__jPQL_FunctionExpression78", None)
        self.__jPQL_FunctionExpression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Expression79"):
                opp_val = getattr(old_value, "jPQL_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Expression79"):
                opp_val = getattr(value, "jPQL_Expression79", None)
                setattr(value, "jPQL_Expression79", self)

    @property
    def jPQL_FunctionExpression84(self):
        return self.__jPQL_FunctionExpression84

    @jPQL_FunctionExpression84.setter
    def jPQL_FunctionExpression84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FunctionExpression__jPQL_FunctionExpression84", None)
        self.__jPQL_FunctionExpression84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Expression85"):
                opp_val = getattr(old_value, "jPQL_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Expression85"):
                opp_val = getattr(value, "jPQL_Expression85", None)
                setattr(value, "jPQL_Expression85", self)

class SelectAggregateExpression:

    pass
class jPQL_MaxAggregate(SelectAggregateExpression):

    pass
class jPQL_MinAggregate(SelectAggregateExpression):

    pass
class jPQL_CountAggregate(SelectAggregateExpression):

    pass
class jPQL_SumAggregate(SelectAggregateExpression):

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
                if hasattr(item, "jPQL_AliasAttributeExpression37"):
                    opp_val = getattr(item, "jPQL_AliasAttributeExpression37", None)
                    
                    if opp_val == self:
                        setattr(item, "jPQL_AliasAttributeExpression37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jPQL_AliasAttributeExpression37"):
                    opp_val = getattr(item, "jPQL_AliasAttributeExpression37", None)
                    
                    setattr(item, "jPQL_AliasAttributeExpression37", self)
                    

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
            if hasattr(old_value, "jPQL_AliasAttributeExpression35"):
                opp_val = getattr(old_value, "jPQL_AliasAttributeExpression35", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_AliasAttributeExpression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_AliasAttributeExpression35"):
                opp_val = getattr(value, "jPQL_AliasAttributeExpression35", None)
                setattr(value, "jPQL_AliasAttributeExpression35", self)

class jPQL_SelectExpression:

    pass
class jPQL_DeleteClause:

    pass
class jPQL_Literal(Variable):

    pass
class FromEntry:

    pass
class jPQL_FromCollection(FromEntry):

    pass
class jPQL_FromClass(FromEntry):

    def __init__(self, type: str, jPQL_FromClass: set["jPQL_FromJoin"] = None):
        self.type = type
        self.jPQL_FromClass = jPQL_FromClass if jPQL_FromClass is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def jPQL_FromClass(self):
        return self.__jPQL_FromClass

    @jPQL_FromClass.setter
    def jPQL_FromClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_FromClass__jPQL_FromClass", None)
        self.__jPQL_FromClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jPQL_FromJoin"):
                    opp_val = getattr(item, "jPQL_FromJoin", None)
                    
                    if opp_val == self:
                        setattr(item, "jPQL_FromJoin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jPQL_FromJoin"):
                    opp_val = getattr(item, "jPQL_FromJoin", None)
                    
                    setattr(item, "jPQL_FromJoin", self)
                    

class jPQL_VariableDeclaration:

    def __init__(self, name: str, jPQL_VariableDeclaration: "jPQL_FromEntry" = None, jPQL_VariableDeclaration51: "jPQL_FromJoin" = None, jPQL_VariableDeclaration74: "jPQL_AliasAttributeExpression" = None):
        self.name = name
        self.jPQL_VariableDeclaration = jPQL_VariableDeclaration
        self.jPQL_VariableDeclaration51 = jPQL_VariableDeclaration51
        self.jPQL_VariableDeclaration74 = jPQL_VariableDeclaration74
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def jPQL_VariableDeclaration51(self):
        return self.__jPQL_VariableDeclaration51

    @jPQL_VariableDeclaration51.setter
    def jPQL_VariableDeclaration51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_VariableDeclaration__jPQL_VariableDeclaration51", None)
        self.__jPQL_VariableDeclaration51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FromJoin50"):
                opp_val = getattr(old_value, "jPQL_FromJoin50", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FromJoin50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromJoin50"):
                opp_val = getattr(value, "jPQL_FromJoin50", None)
                setattr(value, "jPQL_FromJoin50", self)

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
            if hasattr(old_value, "jPQL_FromEntry42"):
                opp_val = getattr(old_value, "jPQL_FromEntry42", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FromEntry42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromEntry42"):
                opp_val = getattr(value, "jPQL_FromEntry42", None)
                setattr(value, "jPQL_FromEntry42", self)

    @property
    def jPQL_VariableDeclaration74(self):
        return self.__jPQL_VariableDeclaration74

    @jPQL_VariableDeclaration74.setter
    def jPQL_VariableDeclaration74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_VariableDeclaration__jPQL_VariableDeclaration74", None)
        self.__jPQL_VariableDeclaration74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_AliasAttributeExpression73"):
                opp_val = getattr(old_value, "jPQL_AliasAttributeExpression73", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_AliasAttributeExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_AliasAttributeExpression73"):
                opp_val = getattr(value, "jPQL_AliasAttributeExpression73", None)
                setattr(value, "jPQL_AliasAttributeExpression73", self)

class jPQL_UpdateClause:

    pass
class jPQL_OrderBySpec:

    pass
class jPQL_Expression(SelectExpression):

    def __init__(self, unaryOperator: str, isNot: bool, jPQL_Expression: "jPQL_HavingClause" = None, jPQL_Expression67: "jPQL_Literal" = None, jPQL_Expression70: "jPQL_Literal" = None, jPQL_Expression54: "jPQL_WhereClause" = None, jPQL_Expression57: "jPQL_Expression" = None, jPQL_Expression55: "jPQL_Expression" = None, jPQL_Expression60: "jPQL_Expression" = None, jPQL_Expression58: "jPQL_Expression" = None, jPQL_Expression62: set["jPQL_Variable"] = None, jPQL_Expression64: "jPQL_SelectStatement" = None, jPQL_Expression76: "jPQL_FunctionExpression" = None, jPQL_Expression79: "jPQL_FunctionExpression" = None, jPQL_Expression82: "jPQL_FunctionExpression" = None, jPQL_Expression85: "jPQL_FunctionExpression" = None, jPQL_Expression88: "jPQL_FunctionExpression" = None, jPQL_Expression93: "jPQL_AndExpression" = None, jPQL_Expression91: "jPQL_OrExpression" = None):
        self.unaryOperator = unaryOperator
        self.isNot = isNot
        self.jPQL_Expression = jPQL_Expression
        self.jPQL_Expression67 = jPQL_Expression67
        self.jPQL_Expression70 = jPQL_Expression70
        self.jPQL_Expression54 = jPQL_Expression54
        self.jPQL_Expression57 = jPQL_Expression57
        self.jPQL_Expression55 = jPQL_Expression55
        self.jPQL_Expression60 = jPQL_Expression60
        self.jPQL_Expression58 = jPQL_Expression58
        self.jPQL_Expression62 = jPQL_Expression62 if jPQL_Expression62 is not None else set()
        self.jPQL_Expression64 = jPQL_Expression64
        self.jPQL_Expression76 = jPQL_Expression76
        self.jPQL_Expression79 = jPQL_Expression79
        self.jPQL_Expression82 = jPQL_Expression82
        self.jPQL_Expression85 = jPQL_Expression85
        self.jPQL_Expression88 = jPQL_Expression88
        self.jPQL_Expression93 = jPQL_Expression93
        self.jPQL_Expression91 = jPQL_Expression91
        
        pass
    @property
    def unaryOperator(self):
        return self.__unaryOperator

    @unaryOperator.setter
    def unaryOperator(self, unaryOperator: str):
        self.__unaryOperator = unaryOperator


    @property
    def isNot(self):
        return self.__isNot

    @isNot.setter
    def isNot(self, isNot: bool):
        self.__isNot = isNot


    @property
    def jPQL_Expression62(self):
        return self.__jPQL_Expression62

    @jPQL_Expression62.setter
    def jPQL_Expression62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression62", None)
        self.__jPQL_Expression62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jPQL_Variable"):
                    opp_val = getattr(item, "jPQL_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "jPQL_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jPQL_Variable"):
                    opp_val = getattr(item, "jPQL_Variable", None)
                    
                    setattr(item, "jPQL_Variable", self)
                    

    @property
    def jPQL_Expression70(self):
        return self.__jPQL_Expression70

    @jPQL_Expression70.setter
    def jPQL_Expression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression70", None)
        self.__jPQL_Expression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Literal71"):
                opp_val = getattr(old_value, "jPQL_Literal71", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Literal71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Literal71"):
                opp_val = getattr(value, "jPQL_Literal71", None)
                setattr(value, "jPQL_Literal71", self)

    @property
    def jPQL_Expression93(self):
        return self.__jPQL_Expression93

    @jPQL_Expression93.setter
    def jPQL_Expression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression93", None)
        self.__jPQL_Expression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_AndExpression"):
                opp_val = getattr(old_value, "jPQL_AndExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_AndExpression"):
                opp_val = getattr(value, "jPQL_AndExpression", None)
                if opp_val is None:
                    setattr(value, "jPQL_AndExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jPQL_Expression91(self):
        return self.__jPQL_Expression91

    @jPQL_Expression91.setter
    def jPQL_Expression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression91", None)
        self.__jPQL_Expression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_OrExpression"):
                opp_val = getattr(old_value, "jPQL_OrExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_OrExpression"):
                opp_val = getattr(value, "jPQL_OrExpression", None)
                if opp_val is None:
                    setattr(value, "jPQL_OrExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jPQL_Expression60(self):
        return self.__jPQL_Expression60

    @jPQL_Expression60.setter
    def jPQL_Expression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression60", None)
        self.__jPQL_Expression60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Expression58"):
                opp_val = getattr(old_value, "jPQL_Expression58", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Expression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Expression58"):
                opp_val = getattr(value, "jPQL_Expression58", None)
                setattr(value, "jPQL_Expression58", self)

    @property
    def jPQL_Expression(self):
        return self.__jPQL_Expression

    @jPQL_Expression.setter
    def jPQL_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression", None)
        self.__jPQL_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_HavingClause13"):
                opp_val = getattr(old_value, "jPQL_HavingClause13", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_HavingClause13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_HavingClause13"):
                opp_val = getattr(value, "jPQL_HavingClause13", None)
                setattr(value, "jPQL_HavingClause13", self)

    @property
    def jPQL_Expression76(self):
        return self.__jPQL_Expression76

    @jPQL_Expression76.setter
    def jPQL_Expression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression76", None)
        self.__jPQL_Expression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FunctionExpression"):
                opp_val = getattr(old_value, "jPQL_FunctionExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FunctionExpression"):
                opp_val = getattr(value, "jPQL_FunctionExpression", None)
                if opp_val is None:
                    setattr(value, "jPQL_FunctionExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jPQL_Expression82(self):
        return self.__jPQL_Expression82

    @jPQL_Expression82.setter
    def jPQL_Expression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression82", None)
        self.__jPQL_Expression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FunctionExpression81"):
                opp_val = getattr(old_value, "jPQL_FunctionExpression81", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FunctionExpression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FunctionExpression81"):
                opp_val = getattr(value, "jPQL_FunctionExpression81", None)
                setattr(value, "jPQL_FunctionExpression81", self)

    @property
    def jPQL_Expression58(self):
        return self.__jPQL_Expression58

    @jPQL_Expression58.setter
    def jPQL_Expression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression58", None)
        self.__jPQL_Expression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Expression60"):
                opp_val = getattr(old_value, "jPQL_Expression60", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Expression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Expression60"):
                opp_val = getattr(value, "jPQL_Expression60", None)
                setattr(value, "jPQL_Expression60", self)

    @property
    def jPQL_Expression57(self):
        return self.__jPQL_Expression57

    @jPQL_Expression57.setter
    def jPQL_Expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression57", None)
        self.__jPQL_Expression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Expression55"):
                opp_val = getattr(old_value, "jPQL_Expression55", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Expression55"):
                opp_val = getattr(value, "jPQL_Expression55", None)
                setattr(value, "jPQL_Expression55", self)

    @property
    def jPQL_Expression79(self):
        return self.__jPQL_Expression79

    @jPQL_Expression79.setter
    def jPQL_Expression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression79", None)
        self.__jPQL_Expression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FunctionExpression78"):
                opp_val = getattr(old_value, "jPQL_FunctionExpression78", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FunctionExpression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FunctionExpression78"):
                opp_val = getattr(value, "jPQL_FunctionExpression78", None)
                setattr(value, "jPQL_FunctionExpression78", self)

    @property
    def jPQL_Expression85(self):
        return self.__jPQL_Expression85

    @jPQL_Expression85.setter
    def jPQL_Expression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression85", None)
        self.__jPQL_Expression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FunctionExpression84"):
                opp_val = getattr(old_value, "jPQL_FunctionExpression84", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FunctionExpression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FunctionExpression84"):
                opp_val = getattr(value, "jPQL_FunctionExpression84", None)
                setattr(value, "jPQL_FunctionExpression84", self)

    @property
    def jPQL_Expression67(self):
        return self.__jPQL_Expression67

    @jPQL_Expression67.setter
    def jPQL_Expression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression67", None)
        self.__jPQL_Expression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Literal68"):
                opp_val = getattr(old_value, "jPQL_Literal68", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Literal68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Literal68"):
                opp_val = getattr(value, "jPQL_Literal68", None)
                setattr(value, "jPQL_Literal68", self)

    @property
    def jPQL_Expression55(self):
        return self.__jPQL_Expression55

    @jPQL_Expression55.setter
    def jPQL_Expression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression55", None)
        self.__jPQL_Expression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_Expression57"):
                opp_val = getattr(old_value, "jPQL_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_Expression57"):
                opp_val = getattr(value, "jPQL_Expression57", None)
                setattr(value, "jPQL_Expression57", self)

    @property
    def jPQL_Expression64(self):
        return self.__jPQL_Expression64

    @jPQL_Expression64.setter
    def jPQL_Expression64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression64", None)
        self.__jPQL_Expression64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_SelectStatement65"):
                opp_val = getattr(old_value, "jPQL_SelectStatement65", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_SelectStatement65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_SelectStatement65"):
                opp_val = getattr(value, "jPQL_SelectStatement65", None)
                setattr(value, "jPQL_SelectStatement65", self)

    @property
    def jPQL_Expression88(self):
        return self.__jPQL_Expression88

    @jPQL_Expression88.setter
    def jPQL_Expression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression88", None)
        self.__jPQL_Expression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FunctionExpression87"):
                opp_val = getattr(old_value, "jPQL_FunctionExpression87", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FunctionExpression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FunctionExpression87"):
                opp_val = getattr(value, "jPQL_FunctionExpression87", None)
                setattr(value, "jPQL_FunctionExpression87", self)

    @property
    def jPQL_Expression54(self):
        return self.__jPQL_Expression54

    @jPQL_Expression54.setter
    def jPQL_Expression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_Expression__jPQL_Expression54", None)
        self.__jPQL_Expression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_WhereClause53"):
                opp_val = getattr(old_value, "jPQL_WhereClause53", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_WhereClause53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_WhereClause53"):
                opp_val = getattr(value, "jPQL_WhereClause53", None)
                setattr(value, "jPQL_WhereClause53", self)

class jPQL_HavingClause:

    pass
class jPQL_AliasAttributeExpression(Variable, OrderBySpec):

    def __init__(self, direction: str, attributes: str, jPQL_AliasAttributeExpression: "jPQL_GroupByClause" = None, jPQL_AliasAttributeExpression25: "jPQL_UpdateItem" = None, jPQL_AliasAttributeExpression35: "jPQL_SelectAggregateExpression" = None, jPQL_AliasAttributeExpression37: "jPQL_SelectConstructorExpression" = None, jPQL_AliasAttributeExpression45: "jPQL_FromCollection" = None, jPQL_AliasAttributeExpression48: "jPQL_FromJoin" = None, jPQL_AliasAttributeExpression73: "jPQL_VariableDeclaration" = None):
        self.direction = direction
        self.attributes = attributes
        self.jPQL_AliasAttributeExpression = jPQL_AliasAttributeExpression
        self.jPQL_AliasAttributeExpression25 = jPQL_AliasAttributeExpression25
        self.jPQL_AliasAttributeExpression35 = jPQL_AliasAttributeExpression35
        self.jPQL_AliasAttributeExpression37 = jPQL_AliasAttributeExpression37
        self.jPQL_AliasAttributeExpression45 = jPQL_AliasAttributeExpression45
        self.jPQL_AliasAttributeExpression48 = jPQL_AliasAttributeExpression48
        self.jPQL_AliasAttributeExpression73 = jPQL_AliasAttributeExpression73
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, attributes: str):
        self.__attributes = attributes


    @property
    def jPQL_AliasAttributeExpression73(self):
        return self.__jPQL_AliasAttributeExpression73

    @jPQL_AliasAttributeExpression73.setter
    def jPQL_AliasAttributeExpression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression73", None)
        self.__jPQL_AliasAttributeExpression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_VariableDeclaration74"):
                opp_val = getattr(old_value, "jPQL_VariableDeclaration74", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_VariableDeclaration74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_VariableDeclaration74"):
                opp_val = getattr(value, "jPQL_VariableDeclaration74", None)
                setattr(value, "jPQL_VariableDeclaration74", self)

    @property
    def jPQL_AliasAttributeExpression25(self):
        return self.__jPQL_AliasAttributeExpression25

    @jPQL_AliasAttributeExpression25.setter
    def jPQL_AliasAttributeExpression25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression25", None)
        self.__jPQL_AliasAttributeExpression25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_UpdateItem24"):
                opp_val = getattr(old_value, "jPQL_UpdateItem24", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_UpdateItem24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_UpdateItem24"):
                opp_val = getattr(value, "jPQL_UpdateItem24", None)
                setattr(value, "jPQL_UpdateItem24", self)

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
            if hasattr(old_value, "jPQL_GroupByClause9"):
                opp_val = getattr(old_value, "jPQL_GroupByClause9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_GroupByClause9"):
                opp_val = getattr(value, "jPQL_GroupByClause9", None)
                if opp_val is None:
                    setattr(value, "jPQL_GroupByClause9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jPQL_AliasAttributeExpression48(self):
        return self.__jPQL_AliasAttributeExpression48

    @jPQL_AliasAttributeExpression48.setter
    def jPQL_AliasAttributeExpression48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression48", None)
        self.__jPQL_AliasAttributeExpression48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jPQL_FromJoin47"):
                opp_val = getattr(old_value, "jPQL_FromJoin47", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_FromJoin47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_FromJoin47"):
                opp_val = getattr(value, "jPQL_FromJoin47", None)
                setattr(value, "jPQL_FromJoin47", self)

    @property
    def jPQL_AliasAttributeExpression35(self):
        return self.__jPQL_AliasAttributeExpression35

    @jPQL_AliasAttributeExpression35.setter
    def jPQL_AliasAttributeExpression35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression35", None)
        self.__jPQL_AliasAttributeExpression35 = value
        
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
    def jPQL_AliasAttributeExpression45(self):
        return self.__jPQL_AliasAttributeExpression45

    @jPQL_AliasAttributeExpression45.setter
    def jPQL_AliasAttributeExpression45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_AliasAttributeExpression__jPQL_AliasAttributeExpression45", None)
        self.__jPQL_AliasAttributeExpression45 = value
        
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

class jPQL_OrderByClause:

    pass
class jPQL_GroupByClause:

    pass
class jPQL_FromClause:

    pass
class jPQL_SelectClause:

    def __init__(self, isDistinct: bool, jPQL_SelectClause: "jPQL_SelectStatement" = None, jPQL_SelectClause33: set["jPQL_SelectExpression"] = None):
        self.isDistinct = isDistinct
        self.jPQL_SelectClause = jPQL_SelectClause
        self.jPQL_SelectClause33 = jPQL_SelectClause33 if jPQL_SelectClause33 is not None else set()
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


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
            if hasattr(old_value, "jPQL_SelectStatement"):
                opp_val = getattr(old_value, "jPQL_SelectStatement", None)
                if opp_val == self:
                    setattr(old_value, "jPQL_SelectStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jPQL_SelectStatement"):
                opp_val = getattr(value, "jPQL_SelectStatement", None)
                setattr(value, "jPQL_SelectStatement", self)

    @property
    def jPQL_SelectClause33(self):
        return self.__jPQL_SelectClause33

    @jPQL_SelectClause33.setter
    def jPQL_SelectClause33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jPQL_SelectClause__jPQL_SelectClause33", None)
        self.__jPQL_SelectClause33 = value if value is not None else set()
        
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
                    

class ExpressionTerm:

    pass
class jPQL_Variable(ExpressionTerm, Expression):

    pass
class JPQLQuery:

    pass
class jPQL_DeleteStatement(JPQLQuery):

    pass
class jPQL_UpdateStatement(JPQLQuery):

    pass
class jPQL_SelectStatement(JPQLQuery, ExpressionTerm):

    pass
class jPQL_WhereClause:

    pass
class jPQL_UpdateItem:

    pass
class jPQL_FromEntry:

    pass
class jPQL_SetClause:

    pass
class jPQL_JPQLQuery:

    pass
class jPQL_MultiplicationExpression(Expression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class jPQL_AdditionExpression(Expression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class jPQL_ComparisonOperatorExpression(Expression):

    def __init__(self, operator: str):
        self.operator = operator
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class jPQL_OrExpression(Expression):

    pass
class jPQL_AndExpression(Expression):

    pass
class Literal:

    pass
class jPQL_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class jPQL_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class jPQL_NullLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class jPQL_FloatLiteral(Literal):

    pass
class jPQL_IntegerLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

