from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CrudOperationType(Enum):
    NULL = "NULL"
    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    ALL = "ALL"
class DataBaseConstraintType(Enum):
    NULL = "NULL"
    INDEX = "INDEX"
    UNIQUE = "UNIQUE"
    NATURAL = "NATURAL"
    PRIMARY = "PRIMARY"


############################################
# Definition of Classes
############################################

class dom_PresentableFeature(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class LiteralValue:

    pass
class dom_IntegerLiteralValue(LiteralValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dom_RealLiteralValue(LiteralValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dom_EmptyLiteralValue(LiteralValue):

    pass
class dom_NullLiteralValue(LiteralValue):

    pass
class dom_BooleanLiteralValue(LiteralValue):

    def __init__(self, isTrue: bool):
        self.isTrue = isTrue
        
    @property
    def isTrue(self) -> bool:
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue

class dom_AltWhenClause:

    pass
class dom_QueryParameterReference:

    pass
class dom_WhenClause:

    pass
class dom_StringLiteralValue(LiteralValue):

    def __init__(self, value: str, dom_StringLiteralValue: "dom_TrimFunction" = None):
        self.value = value
        self.dom_StringLiteralValue = dom_StringLiteralValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def dom_StringLiteralValue(self):
        return self.__dom_StringLiteralValue

    @dom_StringLiteralValue.setter
    def dom_StringLiteralValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_StringLiteralValue__dom_StringLiteralValue", None)
        self.__dom_StringLiteralValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_TrimFunction"):
                opp_val = getattr(old_value, "dom_TrimFunction", None)
                if opp_val == self:
                    setattr(old_value, "dom_TrimFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_TrimFunction"):
                opp_val = getattr(value, "dom_TrimFunction", None)
                setattr(value, "dom_TrimFunction", self)

class dom_JoinEntity:

    def __init__(self, name: str, dom_JoinEntity: "dom_Join" = None):
        self.name = name
        self.dom_JoinEntity = dom_JoinEntity
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_JoinEntity(self):
        return self.__dom_JoinEntity

    @dom_JoinEntity.setter
    def dom_JoinEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_JoinEntity__dom_JoinEntity", None)
        self.__dom_JoinEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Join270"):
                opp_val = getattr(old_value, "dom_Join270", None)
                if opp_val == self:
                    setattr(old_value, "dom_Join270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Join270"):
                opp_val = getattr(value, "dom_Join270", None)
                setattr(value, "dom_Join270", self)

class Expression:

    pass
class dom_FunctionCall(Expression):

    def __init__(self, function: str, dom_FunctionCall: set["dom_Expression"] = None):
        self.function = function
        self.dom_FunctionCall = dom_FunctionCall if dom_FunctionCall is not None else set()
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def dom_FunctionCall(self):
        return self.__dom_FunctionCall

    @dom_FunctionCall.setter
    def dom_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FunctionCall__dom_FunctionCall", None)
        self.__dom_FunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Expression281"):
                    opp_val = getattr(item, "dom_Expression281", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Expression281", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Expression281"):
                    opp_val = getattr(item, "dom_Expression281", None)
                    
                    setattr(item, "dom_Expression281", self)
                    

class dom_ParenthesizedExpression(Expression):

    pass
class dom_NotExpression(Expression):

    pass
class dom_CaseExpression(Expression):

    pass
class dom_InExpression(Expression):

    def __init__(self, not: bool, operator: str, dom_InExpression: "dom_Expression" = None, dom_InExpression338: "dom_Expression" = None):
        self.not = not
        self.operator = operator
        self.dom_InExpression = dom_InExpression
        self.dom_InExpression338 = dom_InExpression338
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def dom_InExpression(self):
        return self.__dom_InExpression

    @dom_InExpression.setter
    def dom_InExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_InExpression__dom_InExpression", None)
        self.__dom_InExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression336"):
                opp_val = getattr(old_value, "dom_Expression336", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression336"):
                opp_val = getattr(value, "dom_Expression336", None)
                setattr(value, "dom_Expression336", self)

    @property
    def dom_InExpression338(self):
        return self.__dom_InExpression338

    @dom_InExpression338.setter
    def dom_InExpression338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_InExpression__dom_InExpression338", None)
        self.__dom_InExpression338 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression339"):
                opp_val = getattr(old_value, "dom_Expression339", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression339", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression339"):
                opp_val = getattr(value, "dom_Expression339", None)
                setattr(value, "dom_Expression339", self)

class dom_TrimFunction(Expression):

    def __init__(self, function: str, mode: str, dom_TrimFunction: "dom_StringLiteralValue" = None, dom_TrimFunction284: "dom_Expression" = None):
        self.function = function
        self.mode = mode
        self.dom_TrimFunction = dom_TrimFunction
        self.dom_TrimFunction284 = dom_TrimFunction284
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def dom_TrimFunction(self):
        return self.__dom_TrimFunction

    @dom_TrimFunction.setter
    def dom_TrimFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_TrimFunction__dom_TrimFunction", None)
        self.__dom_TrimFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_StringLiteralValue"):
                opp_val = getattr(old_value, "dom_StringLiteralValue", None)
                if opp_val == self:
                    setattr(old_value, "dom_StringLiteralValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_StringLiteralValue"):
                opp_val = getattr(value, "dom_StringLiteralValue", None)
                setattr(value, "dom_StringLiteralValue", self)

    @property
    def dom_TrimFunction284(self):
        return self.__dom_TrimFunction284

    @dom_TrimFunction284.setter
    def dom_TrimFunction284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_TrimFunction__dom_TrimFunction284", None)
        self.__dom_TrimFunction284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression285"):
                opp_val = getattr(old_value, "dom_Expression285", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression285"):
                opp_val = getattr(value, "dom_Expression285", None)
                setattr(value, "dom_Expression285", self)

class dom_BinaryExpression(Expression):

    def __init__(self, operator: str, dom_BinaryExpression: "dom_Expression" = None, dom_BinaryExpression331: "dom_Expression" = None):
        self.operator = operator
        self.dom_BinaryExpression = dom_BinaryExpression
        self.dom_BinaryExpression331 = dom_BinaryExpression331
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dom_BinaryExpression331(self):
        return self.__dom_BinaryExpression331

    @dom_BinaryExpression331.setter
    def dom_BinaryExpression331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BinaryExpression__dom_BinaryExpression331", None)
        self.__dom_BinaryExpression331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression332"):
                opp_val = getattr(old_value, "dom_Expression332", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression332"):
                opp_val = getattr(value, "dom_Expression332", None)
                setattr(value, "dom_Expression332", self)

    @property
    def dom_BinaryExpression(self):
        return self.__dom_BinaryExpression

    @dom_BinaryExpression.setter
    def dom_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BinaryExpression__dom_BinaryExpression", None)
        self.__dom_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression329"):
                opp_val = getattr(old_value, "dom_Expression329", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression329"):
                opp_val = getattr(value, "dom_Expression329", None)
                setattr(value, "dom_Expression329", self)

class dom_AggregateFunction(Expression):

    def __init__(self, function: str, all: bool, distinct: bool, from: str, dom_AggregateFunction: "dom_Expression" = None, dom_AggregateFunction291: "dom_CollectionFunction" = None):
        self.function = function
        self.all = all
        self.distinct = distinct
        self.from = from
        self.dom_AggregateFunction = dom_AggregateFunction
        self.dom_AggregateFunction291 = dom_AggregateFunction291
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def dom_AggregateFunction291(self):
        return self.__dom_AggregateFunction291

    @dom_AggregateFunction291.setter
    def dom_AggregateFunction291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AggregateFunction__dom_AggregateFunction291", None)
        self.__dom_AggregateFunction291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_CollectionFunction"):
                opp_val = getattr(old_value, "dom_CollectionFunction", None)
                if opp_val == self:
                    setattr(old_value, "dom_CollectionFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_CollectionFunction"):
                opp_val = getattr(value, "dom_CollectionFunction", None)
                setattr(value, "dom_CollectionFunction", self)

    @property
    def dom_AggregateFunction(self):
        return self.__dom_AggregateFunction

    @dom_AggregateFunction.setter
    def dom_AggregateFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AggregateFunction__dom_AggregateFunction", None)
        self.__dom_AggregateFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression289"):
                opp_val = getattr(old_value, "dom_Expression289", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression289"):
                opp_val = getattr(value, "dom_Expression289", None)
                setattr(value, "dom_Expression289", self)

class dom_MemberOfExpression(Expression):

    def __init__(self, not: bool, operator: str, memberOf: str, dom_MemberOfExpression: "dom_Expression" = None):
        self.not = not
        self.operator = operator
        self.memberOf = memberOf
        self.dom_MemberOfExpression = dom_MemberOfExpression
        
    @property
    def memberOf(self) -> str:
        return self.__memberOf

    @memberOf.setter
    def memberOf(self, memberOf: str):
        self.__memberOf = memberOf

    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dom_MemberOfExpression(self):
        return self.__dom_MemberOfExpression

    @dom_MemberOfExpression.setter
    def dom_MemberOfExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_MemberOfExpression__dom_MemberOfExpression", None)
        self.__dom_MemberOfExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression357"):
                opp_val = getattr(old_value, "dom_Expression357", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression357"):
                opp_val = getattr(value, "dom_Expression357", None)
                setattr(value, "dom_Expression357", self)

class dom_AliasedExpression(Expression):

    def __init__(self, name: str, dom_AliasedExpression: "dom_Expression" = None):
        self.name = name
        self.dom_AliasedExpression = dom_AliasedExpression
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_AliasedExpression(self):
        return self.__dom_AliasedExpression

    @dom_AliasedExpression.setter
    def dom_AliasedExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AliasedExpression__dom_AliasedExpression", None)
        self.__dom_AliasedExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression327"):
                opp_val = getattr(old_value, "dom_Expression327", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression327"):
                opp_val = getattr(value, "dom_Expression327", None)
                setattr(value, "dom_Expression327", self)

class dom_QuantifiedExpression(Expression):

    def __init__(self, quantifier: str, name: str, dom_QuantifiedExpression: "dom_Expression" = None):
        self.quantifier = quantifier
        self.name = name
        self.dom_QuantifiedExpression = dom_QuantifiedExpression
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def quantifier(self) -> str:
        return self.__quantifier

    @quantifier.setter
    def quantifier(self, quantifier: str):
        self.__quantifier = quantifier

    @property
    def dom_QuantifiedExpression(self):
        return self.__dom_QuantifiedExpression

    @dom_QuantifiedExpression.setter
    def dom_QuantifiedExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_QuantifiedExpression__dom_QuantifiedExpression", None)
        self.__dom_QuantifiedExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression297"):
                opp_val = getattr(old_value, "dom_Expression297", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression297"):
                opp_val = getattr(value, "dom_Expression297", None)
                setattr(value, "dom_Expression297", self)

class dom_CastFunction(Expression):

    def __init__(self, function: str, name: str, dom_CastFunction: "dom_Expression" = None):
        self.function = function
        self.name = name
        self.dom_CastFunction = dom_CastFunction
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_CastFunction(self):
        return self.__dom_CastFunction

    @dom_CastFunction.setter
    def dom_CastFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CastFunction__dom_CastFunction", None)
        self.__dom_CastFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression287"):
                opp_val = getattr(old_value, "dom_Expression287", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression287", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression287"):
                opp_val = getattr(value, "dom_Expression287", None)
                setattr(value, "dom_Expression287", self)

class dom_QueryParameterValue(Expression):

    pass
class dom_BetweenExpression(Expression):

    def __init__(self, not: bool, operator: str, dom_BetweenExpression: "dom_Expression" = None, dom_BetweenExpression343: "dom_Expression" = None, dom_BetweenExpression346: "dom_Expression" = None):
        self.not = not
        self.operator = operator
        self.dom_BetweenExpression = dom_BetweenExpression
        self.dom_BetweenExpression343 = dom_BetweenExpression343
        self.dom_BetweenExpression346 = dom_BetweenExpression346
        
    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dom_BetweenExpression346(self):
        return self.__dom_BetweenExpression346

    @dom_BetweenExpression346.setter
    def dom_BetweenExpression346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BetweenExpression__dom_BetweenExpression346", None)
        self.__dom_BetweenExpression346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression347"):
                opp_val = getattr(old_value, "dom_Expression347", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression347"):
                opp_val = getattr(value, "dom_Expression347", None)
                setattr(value, "dom_Expression347", self)

    @property
    def dom_BetweenExpression(self):
        return self.__dom_BetweenExpression

    @dom_BetweenExpression.setter
    def dom_BetweenExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BetweenExpression__dom_BetweenExpression", None)
        self.__dom_BetweenExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression341"):
                opp_val = getattr(old_value, "dom_Expression341", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression341", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression341"):
                opp_val = getattr(value, "dom_Expression341", None)
                setattr(value, "dom_Expression341", self)

    @property
    def dom_BetweenExpression343(self):
        return self.__dom_BetweenExpression343

    @dom_BetweenExpression343.setter
    def dom_BetweenExpression343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BetweenExpression__dom_BetweenExpression343", None)
        self.__dom_BetweenExpression343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression344"):
                opp_val = getattr(old_value, "dom_Expression344", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression344"):
                opp_val = getattr(value, "dom_Expression344", None)
                setattr(value, "dom_Expression344", self)

class dom_UnaryExpression(Expression):

    def __init__(self, operator: str, dom_UnaryExpression: "dom_Expression" = None):
        self.operator = operator
        self.dom_UnaryExpression = dom_UnaryExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dom_UnaryExpression(self):
        return self.__dom_UnaryExpression

    @dom_UnaryExpression.setter
    def dom_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_UnaryExpression__dom_UnaryExpression", None)
        self.__dom_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression359"):
                opp_val = getattr(old_value, "dom_Expression359", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression359"):
                opp_val = getattr(value, "dom_Expression359", None)
                setattr(value, "dom_Expression359", self)

class dom_LiteralValue(Expression):

    pass
class dom_LikeExpression(Expression):

    def __init__(self, not: bool, operator: str, dom_LikeExpression: "dom_Expression" = None, dom_LikeExpression351: "dom_Expression" = None, dom_LikeExpression354: "dom_Expression" = None):
        self.not = not
        self.operator = operator
        self.dom_LikeExpression = dom_LikeExpression
        self.dom_LikeExpression351 = dom_LikeExpression351
        self.dom_LikeExpression354 = dom_LikeExpression354
        
    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dom_LikeExpression(self):
        return self.__dom_LikeExpression

    @dom_LikeExpression.setter
    def dom_LikeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_LikeExpression__dom_LikeExpression", None)
        self.__dom_LikeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression349"):
                opp_val = getattr(old_value, "dom_Expression349", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression349"):
                opp_val = getattr(value, "dom_Expression349", None)
                setattr(value, "dom_Expression349", self)

    @property
    def dom_LikeExpression351(self):
        return self.__dom_LikeExpression351

    @dom_LikeExpression351.setter
    def dom_LikeExpression351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_LikeExpression__dom_LikeExpression351", None)
        self.__dom_LikeExpression351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression352"):
                opp_val = getattr(old_value, "dom_Expression352", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression352"):
                opp_val = getattr(value, "dom_Expression352", None)
                setattr(value, "dom_Expression352", self)

    @property
    def dom_LikeExpression354(self):
        return self.__dom_LikeExpression354

    @dom_LikeExpression354.setter
    def dom_LikeExpression354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_LikeExpression__dom_LikeExpression354", None)
        self.__dom_LikeExpression354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression355"):
                opp_val = getattr(old_value, "dom_Expression355", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression355"):
                opp_val = getattr(value, "dom_Expression355", None)
                setattr(value, "dom_Expression355", self)

class dom_SubQuery(Expression):

    pass
class dom_CollectionFunction(Expression):

    def __init__(self, function: str, dom_CollectionFunction: "dom_AggregateFunction" = None, dom_CollectionFunction320: "dom_PropertyValue" = None):
        self.function = function
        self.dom_CollectionFunction = dom_CollectionFunction
        self.dom_CollectionFunction320 = dom_CollectionFunction320
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def dom_CollectionFunction320(self):
        return self.__dom_CollectionFunction320

    @dom_CollectionFunction320.setter
    def dom_CollectionFunction320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CollectionFunction__dom_CollectionFunction320", None)
        self.__dom_CollectionFunction320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_PropertyValue321"):
                opp_val = getattr(old_value, "dom_PropertyValue321", None)
                if opp_val == self:
                    setattr(old_value, "dom_PropertyValue321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_PropertyValue321"):
                opp_val = getattr(value, "dom_PropertyValue321", None)
                setattr(value, "dom_PropertyValue321", self)

    @property
    def dom_CollectionFunction(self):
        return self.__dom_CollectionFunction

    @dom_CollectionFunction.setter
    def dom_CollectionFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CollectionFunction__dom_CollectionFunction", None)
        self.__dom_CollectionFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_AggregateFunction291"):
                opp_val = getattr(old_value, "dom_AggregateFunction291", None)
                if opp_val == self:
                    setattr(old_value, "dom_AggregateFunction291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_AggregateFunction291"):
                opp_val = getattr(value, "dom_AggregateFunction291", None)
                setattr(value, "dom_AggregateFunction291", self)

class JoinEntity:

    pass
class FromRange:

    pass
class dom_InCollectionElements(FromRange):

    def __init__(self, name: str, reference: str):
        self.name = name
        self.reference = reference
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class dom_FromClass(JoinEntity, FromRange):

    def __init__(self, popertyFetch: bool, dom_FromClass: "dom_Entity" = None):
        self.popertyFetch = popertyFetch
        self.dom_FromClass = dom_FromClass
        
    @property
    def popertyFetch(self) -> bool:
        return self.__popertyFetch

    @popertyFetch.setter
    def popertyFetch(self, popertyFetch: bool):
        self.__popertyFetch = popertyFetch

    @property
    def dom_FromClass(self):
        return self.__dom_FromClass

    @dom_FromClass.setter
    def dom_FromClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FromClass__dom_FromClass", None)
        self.__dom_FromClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity268"):
                opp_val = getattr(old_value, "dom_Entity268", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity268"):
                opp_val = getattr(value, "dom_Entity268", None)
                setattr(value, "dom_Entity268", self)

class SelectStatement:

    pass
class dom_SelectObject(SelectStatement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class dom_SelectClass(SelectStatement):

    def __init__(self, class: str, dom_SelectClass: set["dom_Expression"] = None):
        self.class = class
        self.dom_SelectClass = dom_SelectClass if dom_SelectClass is not None else set()
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def dom_SelectClass(self):
        return self.__dom_SelectClass

    @dom_SelectClass.setter
    def dom_SelectClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_SelectClass__dom_SelectClass", None)
        self.__dom_SelectClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Expression266"):
                    opp_val = getattr(item, "dom_Expression266", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Expression266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Expression266"):
                    opp_val = getattr(item, "dom_Expression266", None)
                    
                    setattr(item, "dom_Expression266", self)
                    

class dom_SelectProperties(SelectStatement):

    def __init__(self, distinct: bool, dom_SelectProperties: set["dom_Expression"] = None):
        self.distinct = distinct
        self.dom_SelectProperties = dom_SelectProperties if dom_SelectProperties is not None else set()
        
    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def dom_SelectProperties(self):
        return self.__dom_SelectProperties

    @dom_SelectProperties.setter
    def dom_SelectProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_SelectProperties__dom_SelectProperties", None)
        self.__dom_SelectProperties = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Expression264"):
                    opp_val = getattr(item, "dom_Expression264", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Expression264", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Expression264"):
                    opp_val = getattr(item, "dom_Expression264", None)
                    
                    setattr(item, "dom_Expression264", self)
                    

class dom_InCollection(FromRange):

    def __init__(self, path: str, alias: str):
        self.path = path
        self.alias = alias
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class dom_InClass(FromRange):

    def __init__(self, name: str, class: str):
        self.name = name
        self.class = class
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

class dom_Join(JoinEntity):

    def __init__(self, type: str, fetch: bool, propertyFetch: bool, dom_Join: "dom_SelectStatement" = None, dom_Join270: "dom_JoinEntity" = None, dom_Join272: "dom_Attribute" = None, dom_Join275: "dom_Expression" = None):
        self.type = type
        self.fetch = fetch
        self.propertyFetch = propertyFetch
        self.dom_Join = dom_Join
        self.dom_Join270 = dom_Join270
        self.dom_Join272 = dom_Join272
        self.dom_Join275 = dom_Join275
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def fetch(self) -> bool:
        return self.__fetch

    @fetch.setter
    def fetch(self, fetch: bool):
        self.__fetch = fetch

    @property
    def propertyFetch(self) -> bool:
        return self.__propertyFetch

    @propertyFetch.setter
    def propertyFetch(self, propertyFetch: bool):
        self.__propertyFetch = propertyFetch

    @property
    def dom_Join270(self):
        return self.__dom_Join270

    @dom_Join270.setter
    def dom_Join270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Join__dom_Join270", None)
        self.__dom_Join270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_JoinEntity"):
                opp_val = getattr(old_value, "dom_JoinEntity", None)
                if opp_val == self:
                    setattr(old_value, "dom_JoinEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_JoinEntity"):
                opp_val = getattr(value, "dom_JoinEntity", None)
                setattr(value, "dom_JoinEntity", self)

    @property
    def dom_Join275(self):
        return self.__dom_Join275

    @dom_Join275.setter
    def dom_Join275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Join__dom_Join275", None)
        self.__dom_Join275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression276"):
                opp_val = getattr(old_value, "dom_Expression276", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression276"):
                opp_val = getattr(value, "dom_Expression276", None)
                setattr(value, "dom_Expression276", self)

    @property
    def dom_Join272(self):
        return self.__dom_Join272

    @dom_Join272.setter
    def dom_Join272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Join__dom_Join272", None)
        self.__dom_Join272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute273"):
                opp_val = getattr(old_value, "dom_Attribute273", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute273"):
                opp_val = getattr(value, "dom_Attribute273", None)
                setattr(value, "dom_Attribute273", self)

    @property
    def dom_Join(self):
        return self.__dom_Join

    @dom_Join.setter
    def dom_Join(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Join__dom_Join", None)
        self.__dom_Join = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_SelectStatement248"):
                opp_val = getattr(old_value, "dom_SelectStatement248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_SelectStatement248"):
                opp_val = getattr(value, "dom_SelectStatement248", None)
                if opp_val is None:
                    setattr(value, "dom_SelectStatement248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dom_FromRange:

    pass
class dom_PropertyValue(Expression):

    def __init__(self, name: str, segments: str, classProperty: bool, dom_PropertyValue: "dom_PropertyAssignment" = None, dom_PropertyValue278: set["dom_Expression"] = None, dom_PropertyValue321: "dom_CollectionFunction" = None):
        self.name = name
        self.segments = segments
        self.classProperty = classProperty
        self.dom_PropertyValue = dom_PropertyValue
        self.dom_PropertyValue278 = dom_PropertyValue278 if dom_PropertyValue278 is not None else set()
        self.dom_PropertyValue321 = dom_PropertyValue321
        
    @property
    def segments(self) -> str:
        return self.__segments

    @segments.setter
    def segments(self, segments: str):
        self.__segments = segments

    @property
    def classProperty(self) -> bool:
        return self.__classProperty

    @classProperty.setter
    def classProperty(self, classProperty: bool):
        self.__classProperty = classProperty

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_PropertyValue(self):
        return self.__dom_PropertyValue

    @dom_PropertyValue.setter
    def dom_PropertyValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_PropertyValue__dom_PropertyValue", None)
        self.__dom_PropertyValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_PropertyAssignment241"):
                opp_val = getattr(old_value, "dom_PropertyAssignment241", None)
                if opp_val == self:
                    setattr(old_value, "dom_PropertyAssignment241", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_PropertyAssignment241"):
                opp_val = getattr(value, "dom_PropertyAssignment241", None)
                setattr(value, "dom_PropertyAssignment241", self)

    @property
    def dom_PropertyValue321(self):
        return self.__dom_PropertyValue321

    @dom_PropertyValue321.setter
    def dom_PropertyValue321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_PropertyValue__dom_PropertyValue321", None)
        self.__dom_PropertyValue321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_CollectionFunction320"):
                opp_val = getattr(old_value, "dom_CollectionFunction320", None)
                if opp_val == self:
                    setattr(old_value, "dom_CollectionFunction320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_CollectionFunction320"):
                opp_val = getattr(value, "dom_CollectionFunction320", None)
                setattr(value, "dom_CollectionFunction320", self)

    @property
    def dom_PropertyValue278(self):
        return self.__dom_PropertyValue278

    @dom_PropertyValue278.setter
    def dom_PropertyValue278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_PropertyValue__dom_PropertyValue278", None)
        self.__dom_PropertyValue278 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Expression279"):
                    opp_val = getattr(item, "dom_Expression279", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Expression279", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Expression279"):
                    opp_val = getattr(item, "dom_Expression279", None)
                    
                    setattr(item, "dom_Expression279", self)
                    

class dom_SortOrderElement:

    def __init__(self, sortOrder: str, dom_SortOrderElement: "dom_SelectStatement" = None, dom_SortOrderElement261: "dom_Expression" = None):
        self.sortOrder = sortOrder
        self.dom_SortOrderElement = dom_SortOrderElement
        self.dom_SortOrderElement261 = dom_SortOrderElement261
        
    @property
    def sortOrder(self) -> str:
        return self.__sortOrder

    @sortOrder.setter
    def sortOrder(self, sortOrder: str):
        self.__sortOrder = sortOrder

    @property
    def dom_SortOrderElement(self):
        return self.__dom_SortOrderElement

    @dom_SortOrderElement.setter
    def dom_SortOrderElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_SortOrderElement__dom_SortOrderElement", None)
        self.__dom_SortOrderElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_SelectStatement259"):
                opp_val = getattr(old_value, "dom_SelectStatement259", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_SelectStatement259"):
                opp_val = getattr(value, "dom_SelectStatement259", None)
                if opp_val is None:
                    setattr(value, "dom_SelectStatement259", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_SortOrderElement261(self):
        return self.__dom_SortOrderElement261

    @dom_SortOrderElement261.setter
    def dom_SortOrderElement261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_SortOrderElement__dom_SortOrderElement261", None)
        self.__dom_SortOrderElement261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression262"):
                opp_val = getattr(old_value, "dom_Expression262", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression262"):
                opp_val = getattr(value, "dom_Expression262", None)
                setattr(value, "dom_Expression262", self)

class dom_PropertyAssignment:

    pass
class dom_CallOutputParameter:

    def __init__(self, name: str, dom_CallOutputParameter216: "dom_Attribute" = None, dom_CallOutputParameter219: "dom_Attribute" = None, dom_CallOutputParameter: "dom_CallableStatement" = None):
        self.name = name
        self.dom_CallOutputParameter216 = dom_CallOutputParameter216
        self.dom_CallOutputParameter219 = dom_CallOutputParameter219
        self.dom_CallOutputParameter = dom_CallOutputParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_CallOutputParameter(self):
        return self.__dom_CallOutputParameter

    @dom_CallOutputParameter.setter
    def dom_CallOutputParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CallOutputParameter__dom_CallOutputParameter", None)
        self.__dom_CallOutputParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_CallableStatement208"):
                opp_val = getattr(old_value, "dom_CallableStatement208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_CallableStatement208"):
                opp_val = getattr(value, "dom_CallableStatement208", None)
                if opp_val is None:
                    setattr(value, "dom_CallableStatement208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_CallOutputParameter219(self):
        return self.__dom_CallOutputParameter219

    @dom_CallOutputParameter219.setter
    def dom_CallOutputParameter219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CallOutputParameter__dom_CallOutputParameter219", None)
        self.__dom_CallOutputParameter219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute220"):
                opp_val = getattr(old_value, "dom_Attribute220", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute220"):
                opp_val = getattr(value, "dom_Attribute220", None)
                setattr(value, "dom_Attribute220", self)

    @property
    def dom_CallOutputParameter216(self):
        return self.__dom_CallOutputParameter216

    @dom_CallOutputParameter216.setter
    def dom_CallOutputParameter216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CallOutputParameter__dom_CallOutputParameter216", None)
        self.__dom_CallOutputParameter216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute217"):
                opp_val = getattr(old_value, "dom_Attribute217", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute217"):
                opp_val = getattr(value, "dom_Attribute217", None)
                setattr(value, "dom_Attribute217", self)

class dom_CallInputParameter:

    def __init__(self, name: str, dom_CallInputParameter: "dom_CallableStatement" = None, dom_CallInputParameter210: "dom_QueryParameter" = None, dom_CallInputParameter213: "dom_Attribute" = None):
        self.name = name
        self.dom_CallInputParameter = dom_CallInputParameter
        self.dom_CallInputParameter210 = dom_CallInputParameter210
        self.dom_CallInputParameter213 = dom_CallInputParameter213
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_CallInputParameter213(self):
        return self.__dom_CallInputParameter213

    @dom_CallInputParameter213.setter
    def dom_CallInputParameter213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CallInputParameter__dom_CallInputParameter213", None)
        self.__dom_CallInputParameter213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute214"):
                opp_val = getattr(old_value, "dom_Attribute214", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute214"):
                opp_val = getattr(value, "dom_Attribute214", None)
                setattr(value, "dom_Attribute214", self)

    @property
    def dom_CallInputParameter210(self):
        return self.__dom_CallInputParameter210

    @dom_CallInputParameter210.setter
    def dom_CallInputParameter210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CallInputParameter__dom_CallInputParameter210", None)
        self.__dom_CallInputParameter210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_QueryParameter211"):
                opp_val = getattr(old_value, "dom_QueryParameter211", None)
                if opp_val == self:
                    setattr(old_value, "dom_QueryParameter211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_QueryParameter211"):
                opp_val = getattr(value, "dom_QueryParameter211", None)
                setattr(value, "dom_QueryParameter211", self)

    @property
    def dom_CallInputParameter(self):
        return self.__dom_CallInputParameter

    @dom_CallInputParameter.setter
    def dom_CallInputParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CallInputParameter__dom_CallInputParameter", None)
        self.__dom_CallInputParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_CallableStatement"):
                opp_val = getattr(old_value, "dom_CallableStatement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_CallableStatement"):
                opp_val = getattr(value, "dom_CallableStatement", None)
                if opp_val is None:
                    setattr(value, "dom_CallableStatement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class QlStatement:

    pass
class dom_SelectStatement(QlStatement):

    pass
class dom_DeleteStatement(QlStatement):

    def __init__(self, name: str, dom_DeleteStatement: "dom_Entity" = None, dom_DeleteStatement231: "dom_Expression" = None):
        self.name = name
        self.dom_DeleteStatement = dom_DeleteStatement
        self.dom_DeleteStatement231 = dom_DeleteStatement231
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_DeleteStatement(self):
        return self.__dom_DeleteStatement

    @dom_DeleteStatement.setter
    def dom_DeleteStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DeleteStatement__dom_DeleteStatement", None)
        self.__dom_DeleteStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity229"):
                opp_val = getattr(old_value, "dom_Entity229", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity229"):
                opp_val = getattr(value, "dom_Entity229", None)
                setattr(value, "dom_Entity229", self)

    @property
    def dom_DeleteStatement231(self):
        return self.__dom_DeleteStatement231

    @dom_DeleteStatement231.setter
    def dom_DeleteStatement231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DeleteStatement__dom_DeleteStatement231", None)
        self.__dom_DeleteStatement231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression232"):
                opp_val = getattr(old_value, "dom_Expression232", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression232"):
                opp_val = getattr(value, "dom_Expression232", None)
                setattr(value, "dom_Expression232", self)

class dom_UpdateStatement(QlStatement):

    def __init__(self, name: str, versioned: bool, dom_UpdateStatement: "dom_Entity" = None, dom_UpdateStatement236: set["dom_PropertyAssignment"] = None, dom_UpdateStatement238: "dom_Expression" = None):
        self.name = name
        self.versioned = versioned
        self.dom_UpdateStatement = dom_UpdateStatement
        self.dom_UpdateStatement236 = dom_UpdateStatement236 if dom_UpdateStatement236 is not None else set()
        self.dom_UpdateStatement238 = dom_UpdateStatement238
        
    @property
    def versioned(self) -> bool:
        return self.__versioned

    @versioned.setter
    def versioned(self, versioned: bool):
        self.__versioned = versioned

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_UpdateStatement236(self):
        return self.__dom_UpdateStatement236

    @dom_UpdateStatement236.setter
    def dom_UpdateStatement236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_UpdateStatement__dom_UpdateStatement236", None)
        self.__dom_UpdateStatement236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_PropertyAssignment"):
                    opp_val = getattr(item, "dom_PropertyAssignment", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_PropertyAssignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_PropertyAssignment"):
                    opp_val = getattr(item, "dom_PropertyAssignment", None)
                    
                    setattr(item, "dom_PropertyAssignment", self)
                    

    @property
    def dom_UpdateStatement238(self):
        return self.__dom_UpdateStatement238

    @dom_UpdateStatement238.setter
    def dom_UpdateStatement238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_UpdateStatement__dom_UpdateStatement238", None)
        self.__dom_UpdateStatement238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression239"):
                opp_val = getattr(old_value, "dom_Expression239", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression239"):
                opp_val = getattr(value, "dom_Expression239", None)
                setattr(value, "dom_Expression239", self)

    @property
    def dom_UpdateStatement(self):
        return self.__dom_UpdateStatement

    @dom_UpdateStatement.setter
    def dom_UpdateStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_UpdateStatement__dom_UpdateStatement", None)
        self.__dom_UpdateStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity234"):
                opp_val = getattr(old_value, "dom_Entity234", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity234"):
                opp_val = getattr(value, "dom_Entity234", None)
                setattr(value, "dom_Entity234", self)

class dom_CallableStatement(QlStatement):

    def __init__(self, functionCall: bool, name: str, dom_CallableStatement: set["dom_CallInputParameter"] = None, dom_CallableStatement208: set["dom_CallOutputParameter"] = None):
        self.functionCall = functionCall
        self.name = name
        self.dom_CallableStatement = dom_CallableStatement if dom_CallableStatement is not None else set()
        self.dom_CallableStatement208 = dom_CallableStatement208 if dom_CallableStatement208 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def functionCall(self) -> bool:
        return self.__functionCall

    @functionCall.setter
    def functionCall(self, functionCall: bool):
        self.__functionCall = functionCall

    @property
    def dom_CallableStatement208(self):
        return self.__dom_CallableStatement208

    @dom_CallableStatement208.setter
    def dom_CallableStatement208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CallableStatement__dom_CallableStatement208", None)
        self.__dom_CallableStatement208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_CallOutputParameter"):
                    opp_val = getattr(item, "dom_CallOutputParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_CallOutputParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_CallOutputParameter"):
                    opp_val = getattr(item, "dom_CallOutputParameter", None)
                    
                    setattr(item, "dom_CallOutputParameter", self)
                    

    @property
    def dom_CallableStatement(self):
        return self.__dom_CallableStatement

    @dom_CallableStatement.setter
    def dom_CallableStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_CallableStatement__dom_CallableStatement", None)
        self.__dom_CallableStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_CallInputParameter"):
                    opp_val = getattr(item, "dom_CallInputParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_CallInputParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_CallInputParameter"):
                    opp_val = getattr(item, "dom_CallInputParameter", None)
                    
                    setattr(item, "dom_CallInputParameter", self)
                    

class dom_InsertStatement(QlStatement):

    pass
class dom_Function:

    pass
class dom_SqlType:

    pass
class DaoFeature:

    pass
class dom_QlStatement:

    pass
class dom_QueryParameter:

    pass
class dom_ManyToMany(DaoFeature):

    def __init__(self, tableName: str, columnName: str, inverse: bool, dom_ManyToMany: "dom_Dao" = None):
        self.tableName = tableName
        self.columnName = columnName
        self.inverse = inverse
        self.dom_ManyToMany = dom_ManyToMany
        
    @property
    def inverse(self) -> bool:
        return self.__inverse

    @inverse.setter
    def inverse(self, inverse: bool):
        self.__inverse = inverse

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def dom_ManyToMany(self):
        return self.__dom_ManyToMany

    @dom_ManyToMany.setter
    def dom_ManyToMany(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_ManyToMany__dom_ManyToMany", None)
        self.__dom_ManyToMany = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao150"):
                opp_val = getattr(old_value, "dom_Dao150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao150"):
                opp_val = getattr(value, "dom_Dao150", None)
                if opp_val is None:
                    setattr(value, "dom_Dao150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dom_OneToMany(DaoFeature):

    def __init__(self, columnName: str, dom_OneToMany: "dom_Dao" = None, dom_OneToMany191: set["dom_Column"] = None):
        self.columnName = columnName
        self.dom_OneToMany = dom_OneToMany
        self.dom_OneToMany191 = dom_OneToMany191 if dom_OneToMany191 is not None else set()
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def dom_OneToMany(self):
        return self.__dom_OneToMany

    @dom_OneToMany.setter
    def dom_OneToMany(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_OneToMany__dom_OneToMany", None)
        self.__dom_OneToMany = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao148"):
                opp_val = getattr(old_value, "dom_Dao148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao148"):
                opp_val = getattr(value, "dom_Dao148", None)
                if opp_val is None:
                    setattr(value, "dom_Dao148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_OneToMany191(self):
        return self.__dom_OneToMany191

    @dom_OneToMany191.setter
    def dom_OneToMany191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_OneToMany__dom_OneToMany191", None)
        self.__dom_OneToMany191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Column192"):
                    opp_val = getattr(item, "dom_Column192", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Column192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Column192"):
                    opp_val = getattr(item, "dom_Column192", None)
                    
                    setattr(item, "dom_Column192", self)
                    

class dom_OneToOne(DaoFeature):

    pass
class dom_ManyToOne(DaoFeature):

    def __init__(self, columnName: str, derived: bool, dom_ManyToOne: "dom_Dao" = None, dom_ManyToOne183: "dom_Type" = None, dom_ManyToOne186: "dom_SqlType" = None, dom_ManyToOne188: set["dom_Column"] = None):
        self.columnName = columnName
        self.derived = derived
        self.dom_ManyToOne = dom_ManyToOne
        self.dom_ManyToOne183 = dom_ManyToOne183
        self.dom_ManyToOne186 = dom_ManyToOne186
        self.dom_ManyToOne188 = dom_ManyToOne188 if dom_ManyToOne188 is not None else set()
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def dom_ManyToOne(self):
        return self.__dom_ManyToOne

    @dom_ManyToOne.setter
    def dom_ManyToOne(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_ManyToOne__dom_ManyToOne", None)
        self.__dom_ManyToOne = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao144"):
                opp_val = getattr(old_value, "dom_Dao144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao144"):
                opp_val = getattr(value, "dom_Dao144", None)
                if opp_val is None:
                    setattr(value, "dom_Dao144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_ManyToOne188(self):
        return self.__dom_ManyToOne188

    @dom_ManyToOne188.setter
    def dom_ManyToOne188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_ManyToOne__dom_ManyToOne188", None)
        self.__dom_ManyToOne188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Column189"):
                    opp_val = getattr(item, "dom_Column189", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Column189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Column189"):
                    opp_val = getattr(item, "dom_Column189", None)
                    
                    setattr(item, "dom_Column189", self)
                    

    @property
    def dom_ManyToOne183(self):
        return self.__dom_ManyToOne183

    @dom_ManyToOne183.setter
    def dom_ManyToOne183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_ManyToOne__dom_ManyToOne183", None)
        self.__dom_ManyToOne183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Type184"):
                opp_val = getattr(old_value, "dom_Type184", None)
                if opp_val == self:
                    setattr(old_value, "dom_Type184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Type184"):
                opp_val = getattr(value, "dom_Type184", None)
                setattr(value, "dom_Type184", self)

    @property
    def dom_ManyToOne186(self):
        return self.__dom_ManyToOne186

    @dom_ManyToOne186.setter
    def dom_ManyToOne186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_ManyToOne__dom_ManyToOne186", None)
        self.__dom_ManyToOne186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_SqlType"):
                opp_val = getattr(old_value, "dom_SqlType", None)
                if opp_val == self:
                    setattr(old_value, "dom_SqlType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_SqlType"):
                opp_val = getattr(value, "dom_SqlType", None)
                setattr(value, "dom_SqlType", self)

class dom_Column(DaoFeature):

    def __init__(self, columnName: str, dom_Column156: "dom_Dao" = None, dom_Column159: "dom_Dao" = None, dom_Column: "dom_Dao" = None, dom_Column153: "dom_Dao" = None, dom_Column174: "dom_DataTypeAndTypeParameter" = None, dom_Column177: "dom_Type" = None, dom_Column181: "dom_Column" = None, dom_Column179: set["dom_Column"] = None, dom_Column189: "dom_ManyToOne" = None, dom_Column192: "dom_OneToMany" = None):
        self.columnName = columnName
        self.dom_Column156 = dom_Column156
        self.dom_Column159 = dom_Column159
        self.dom_Column = dom_Column
        self.dom_Column153 = dom_Column153
        self.dom_Column174 = dom_Column174
        self.dom_Column177 = dom_Column177
        self.dom_Column181 = dom_Column181
        self.dom_Column179 = dom_Column179 if dom_Column179 is not None else set()
        self.dom_Column189 = dom_Column189
        self.dom_Column192 = dom_Column192
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def dom_Column174(self):
        return self.__dom_Column174

    @dom_Column174.setter
    def dom_Column174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column174", None)
        self.__dom_Column174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataTypeAndTypeParameter175"):
                opp_val = getattr(old_value, "dom_DataTypeAndTypeParameter175", None)
                if opp_val == self:
                    setattr(old_value, "dom_DataTypeAndTypeParameter175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataTypeAndTypeParameter175"):
                opp_val = getattr(value, "dom_DataTypeAndTypeParameter175", None)
                setattr(value, "dom_DataTypeAndTypeParameter175", self)

    @property
    def dom_Column177(self):
        return self.__dom_Column177

    @dom_Column177.setter
    def dom_Column177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column177", None)
        self.__dom_Column177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Type178"):
                opp_val = getattr(old_value, "dom_Type178", None)
                if opp_val == self:
                    setattr(old_value, "dom_Type178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Type178"):
                opp_val = getattr(value, "dom_Type178", None)
                setattr(value, "dom_Type178", self)

    @property
    def dom_Column156(self):
        return self.__dom_Column156

    @dom_Column156.setter
    def dom_Column156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column156", None)
        self.__dom_Column156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao155"):
                opp_val = getattr(old_value, "dom_Dao155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao155"):
                opp_val = getattr(value, "dom_Dao155", None)
                if opp_val is None:
                    setattr(value, "dom_Dao155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Column(self):
        return self.__dom_Column

    @dom_Column.setter
    def dom_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column", None)
        self.__dom_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao142"):
                opp_val = getattr(old_value, "dom_Dao142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao142"):
                opp_val = getattr(value, "dom_Dao142", None)
                if opp_val is None:
                    setattr(value, "dom_Dao142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Column181(self):
        return self.__dom_Column181

    @dom_Column181.setter
    def dom_Column181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column181", None)
        self.__dom_Column181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Column179"):
                opp_val = getattr(old_value, "dom_Column179", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Column179"):
                opp_val = getattr(value, "dom_Column179", None)
                if opp_val is None:
                    setattr(value, "dom_Column179", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Column189(self):
        return self.__dom_Column189

    @dom_Column189.setter
    def dom_Column189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column189", None)
        self.__dom_Column189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ManyToOne188"):
                opp_val = getattr(old_value, "dom_ManyToOne188", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ManyToOne188"):
                opp_val = getattr(value, "dom_ManyToOne188", None)
                if opp_val is None:
                    setattr(value, "dom_ManyToOne188", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Column159(self):
        return self.__dom_Column159

    @dom_Column159.setter
    def dom_Column159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column159", None)
        self.__dom_Column159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao158"):
                opp_val = getattr(old_value, "dom_Dao158", None)
                if opp_val == self:
                    setattr(old_value, "dom_Dao158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao158"):
                opp_val = getattr(value, "dom_Dao158", None)
                setattr(value, "dom_Dao158", self)

    @property
    def dom_Column179(self):
        return self.__dom_Column179

    @dom_Column179.setter
    def dom_Column179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column179", None)
        self.__dom_Column179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Column181"):
                    opp_val = getattr(item, "dom_Column181", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Column181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Column181"):
                    opp_val = getattr(item, "dom_Column181", None)
                    
                    setattr(item, "dom_Column181", self)
                    

    @property
    def dom_Column192(self):
        return self.__dom_Column192

    @dom_Column192.setter
    def dom_Column192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column192", None)
        self.__dom_Column192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_OneToMany191"):
                opp_val = getattr(old_value, "dom_OneToMany191", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_OneToMany191"):
                opp_val = getattr(value, "dom_OneToMany191", None)
                if opp_val is None:
                    setattr(value, "dom_OneToMany191", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Column153(self):
        return self.__dom_Column153

    @dom_Column153.setter
    def dom_Column153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Column__dom_Column153", None)
        self.__dom_Column153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao152"):
                opp_val = getattr(old_value, "dom_Dao152", None)
                if opp_val == self:
                    setattr(old_value, "dom_Dao152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao152"):
                opp_val = getattr(value, "dom_Dao152", None)
                setattr(value, "dom_Dao152", self)

class dom_DataBaseConstraint:

    def __init__(self, type: str, name: str, dom_DataBaseConstraint: "dom_Dao" = None, dom_DataBaseConstraint162: "dom_Dao" = None, dom_DataBaseConstraint165: "dom_Dao" = None, dom_DataBaseConstraint194: set["dom_Attribute"] = None, dom_DataBaseConstraint197: set["dom_Attribute"] = None):
        self.type = type
        self.name = name
        self.dom_DataBaseConstraint = dom_DataBaseConstraint
        self.dom_DataBaseConstraint162 = dom_DataBaseConstraint162
        self.dom_DataBaseConstraint165 = dom_DataBaseConstraint165
        self.dom_DataBaseConstraint194 = dom_DataBaseConstraint194 if dom_DataBaseConstraint194 is not None else set()
        self.dom_DataBaseConstraint197 = dom_DataBaseConstraint197 if dom_DataBaseConstraint197 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dom_DataBaseConstraint165(self):
        return self.__dom_DataBaseConstraint165

    @dom_DataBaseConstraint165.setter
    def dom_DataBaseConstraint165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DataBaseConstraint__dom_DataBaseConstraint165", None)
        self.__dom_DataBaseConstraint165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao164"):
                opp_val = getattr(old_value, "dom_Dao164", None)
                if opp_val == self:
                    setattr(old_value, "dom_Dao164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao164"):
                opp_val = getattr(value, "dom_Dao164", None)
                setattr(value, "dom_Dao164", self)

    @property
    def dom_DataBaseConstraint197(self):
        return self.__dom_DataBaseConstraint197

    @dom_DataBaseConstraint197.setter
    def dom_DataBaseConstraint197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DataBaseConstraint__dom_DataBaseConstraint197", None)
        self.__dom_DataBaseConstraint197 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Attribute198"):
                    opp_val = getattr(item, "dom_Attribute198", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Attribute198", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Attribute198"):
                    opp_val = getattr(item, "dom_Attribute198", None)
                    
                    setattr(item, "dom_Attribute198", self)
                    

    @property
    def dom_DataBaseConstraint(self):
        return self.__dom_DataBaseConstraint

    @dom_DataBaseConstraint.setter
    def dom_DataBaseConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DataBaseConstraint__dom_DataBaseConstraint", None)
        self.__dom_DataBaseConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao140"):
                opp_val = getattr(old_value, "dom_Dao140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao140"):
                opp_val = getattr(value, "dom_Dao140", None)
                if opp_val is None:
                    setattr(value, "dom_Dao140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_DataBaseConstraint162(self):
        return self.__dom_DataBaseConstraint162

    @dom_DataBaseConstraint162.setter
    def dom_DataBaseConstraint162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DataBaseConstraint__dom_DataBaseConstraint162", None)
        self.__dom_DataBaseConstraint162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao161"):
                opp_val = getattr(old_value, "dom_Dao161", None)
                if opp_val == self:
                    setattr(old_value, "dom_Dao161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao161"):
                opp_val = getattr(value, "dom_Dao161", None)
                setattr(value, "dom_Dao161", self)

    @property
    def dom_DataBaseConstraint194(self):
        return self.__dom_DataBaseConstraint194

    @dom_DataBaseConstraint194.setter
    def dom_DataBaseConstraint194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DataBaseConstraint__dom_DataBaseConstraint194", None)
        self.__dom_DataBaseConstraint194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Attribute195"):
                    opp_val = getattr(item, "dom_Attribute195", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Attribute195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Attribute195"):
                    opp_val = getattr(item, "dom_Attribute195", None)
                    
                    setattr(item, "dom_Attribute195", self)
                    

class dom_DaoFeature(ABC):

    pass
class dom_ValidatorReference:

    pass
class dom_Constraint:

    pass
class dom_AttributeSortOrder:

    def __init__(self, asc: bool, desc: bool, dom_AttributeSortOrder: "dom_AttributeGroup" = None, dom_AttributeSortOrder127: "dom_Attribute" = None):
        self.asc = asc
        self.desc = desc
        self.dom_AttributeSortOrder = dom_AttributeSortOrder
        self.dom_AttributeSortOrder127 = dom_AttributeSortOrder127
        
    @property
    def asc(self) -> bool:
        return self.__asc

    @asc.setter
    def asc(self, asc: bool):
        self.__asc = asc

    @property
    def desc(self) -> bool:
        return self.__desc

    @desc.setter
    def desc(self, desc: bool):
        self.__desc = desc

    @property
    def dom_AttributeSortOrder127(self):
        return self.__dom_AttributeSortOrder127

    @dom_AttributeSortOrder127.setter
    def dom_AttributeSortOrder127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeSortOrder__dom_AttributeSortOrder127", None)
        self.__dom_AttributeSortOrder127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute128"):
                opp_val = getattr(old_value, "dom_Attribute128", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute128"):
                opp_val = getattr(value, "dom_Attribute128", None)
                setattr(value, "dom_Attribute128", self)

    @property
    def dom_AttributeSortOrder(self):
        return self.__dom_AttributeSortOrder

    @dom_AttributeSortOrder.setter
    def dom_AttributeSortOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeSortOrder__dom_AttributeSortOrder", None)
        self.__dom_AttributeSortOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_AttributeGroup122"):
                opp_val = getattr(old_value, "dom_AttributeGroup122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_AttributeGroup122"):
                opp_val = getattr(value, "dom_AttributeGroup122", None)
                if opp_val is None:
                    setattr(value, "dom_AttributeGroup122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ExpressionFlag:

    pass
class dom_ReadOnlyFlag(ExpressionFlag):

    pass
class dom_RequiredFlag(ExpressionFlag):

    pass
class dom_EqualityExpr:

    pass
class AttributeFlag:

    pass
class dom_TransientFlag(AttributeFlag):

    pass
class dom_ExpressionFlag(AttributeFlag):

    pass
class dom_BoolLiteral:

    pass
class dom_DerivedFlag(AttributeFlag):

    pass
class dom_AvailableFlag(ExpressionFlag):

    pass
class AttributeProperty:

    pass
class dom_AttributeValidationProperty(AttributeProperty):

    pass
class dom_AttributeTextProperty(AttributeProperty):

    def __init__(self, labelText: str, tooltipText: str, unitText: str, hstoreColumn: str, dom_AttributeTextProperty: "dom_Attribute" = None):
        self.labelText = labelText
        self.tooltipText = tooltipText
        self.unitText = unitText
        self.hstoreColumn = hstoreColumn
        self.dom_AttributeTextProperty = dom_AttributeTextProperty
        
    @property
    def hstoreColumn(self) -> str:
        return self.__hstoreColumn

    @hstoreColumn.setter
    def hstoreColumn(self, hstoreColumn: str):
        self.__hstoreColumn = hstoreColumn

    @property
    def labelText(self) -> str:
        return self.__labelText

    @labelText.setter
    def labelText(self, labelText: str):
        self.__labelText = labelText

    @property
    def unitText(self) -> str:
        return self.__unitText

    @unitText.setter
    def unitText(self, unitText: str):
        self.__unitText = unitText

    @property
    def tooltipText(self) -> str:
        return self.__tooltipText

    @tooltipText.setter
    def tooltipText(self, tooltipText: str):
        self.__tooltipText = tooltipText

    @property
    def dom_AttributeTextProperty(self):
        return self.__dom_AttributeTextProperty

    @dom_AttributeTextProperty.setter
    def dom_AttributeTextProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeTextProperty__dom_AttributeTextProperty", None)
        self.__dom_AttributeTextProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute120"):
                opp_val = getattr(old_value, "dom_Attribute120", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute120"):
                opp_val = getattr(value, "dom_Attribute120", None)
                setattr(value, "dom_Attribute120", self)

class dom_AttributeFlag(AttributeProperty):

    pass
class dom_IncrementerReference:

    pass
class dom_DataTypeAndTypeParameter:

    pass
class dom_ConditionsBlock:

    pass
class dom_PropertyMapping:

    def __init__(self, biDirectional: bool, toLeft: bool, toRight: bool, dom_PropertyMapping60: "dom_Attribute" = None, dom_PropertyMapping: "dom_Mapper" = None, dom_PropertyMapping57: "dom_Attribute" = None):
        self.biDirectional = biDirectional
        self.toLeft = toLeft
        self.toRight = toRight
        self.dom_PropertyMapping60 = dom_PropertyMapping60
        self.dom_PropertyMapping = dom_PropertyMapping
        self.dom_PropertyMapping57 = dom_PropertyMapping57
        
    @property
    def toLeft(self) -> bool:
        return self.__toLeft

    @toLeft.setter
    def toLeft(self, toLeft: bool):
        self.__toLeft = toLeft

    @property
    def toRight(self) -> bool:
        return self.__toRight

    @toRight.setter
    def toRight(self, toRight: bool):
        self.__toRight = toRight

    @property
    def biDirectional(self) -> bool:
        return self.__biDirectional

    @biDirectional.setter
    def biDirectional(self, biDirectional: bool):
        self.__biDirectional = biDirectional

    @property
    def dom_PropertyMapping(self):
        return self.__dom_PropertyMapping

    @dom_PropertyMapping.setter
    def dom_PropertyMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_PropertyMapping__dom_PropertyMapping", None)
        self.__dom_PropertyMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Mapper55"):
                opp_val = getattr(old_value, "dom_Mapper55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Mapper55"):
                opp_val = getattr(value, "dom_Mapper55", None)
                if opp_val is None:
                    setattr(value, "dom_Mapper55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_PropertyMapping60(self):
        return self.__dom_PropertyMapping60

    @dom_PropertyMapping60.setter
    def dom_PropertyMapping60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_PropertyMapping__dom_PropertyMapping60", None)
        self.__dom_PropertyMapping60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute61"):
                opp_val = getattr(old_value, "dom_Attribute61", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute61"):
                opp_val = getattr(value, "dom_Attribute61", None)
                setattr(value, "dom_Attribute61", self)

    @property
    def dom_PropertyMapping57(self):
        return self.__dom_PropertyMapping57

    @dom_PropertyMapping57.setter
    def dom_PropertyMapping57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_PropertyMapping__dom_PropertyMapping57", None)
        self.__dom_PropertyMapping57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute58"):
                opp_val = getattr(old_value, "dom_Attribute58", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute58"):
                opp_val = getattr(value, "dom_Attribute58", None)
                setattr(value, "dom_Attribute58", self)

class dom_AttributeProperty:

    pass
class PresentableFeature:

    pass
class ComplexType:

    pass
class dom_ValueObject(ComplexType):

    pass
class dom_Expression:

    pass
class dom_DataView(ComplexType):

    pass
class dom_Type:

    pass
class QueryParameterReference:

    pass
class QueryParameter:

    pass
class dom_DaoOperation:

    def __init__(self, many: bool, name: str, dom_DaoOperation: "dom_DelegateOperation" = None, dom_DaoOperation29: "dom_Type" = None):
        self.many = many
        self.name = name
        self.dom_DaoOperation = dom_DaoOperation
        self.dom_DaoOperation29 = dom_DaoOperation29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def dom_DaoOperation(self):
        return self.__dom_DaoOperation

    @dom_DaoOperation.setter
    def dom_DaoOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DaoOperation__dom_DaoOperation", None)
        self.__dom_DaoOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DelegateOperation22"):
                opp_val = getattr(old_value, "dom_DelegateOperation22", None)
                if opp_val == self:
                    setattr(old_value, "dom_DelegateOperation22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DelegateOperation22"):
                opp_val = getattr(value, "dom_DelegateOperation22", None)
                setattr(value, "dom_DelegateOperation22", self)

    @property
    def dom_DaoOperation29(self):
        return self.__dom_DaoOperation29

    @dom_DaoOperation29.setter
    def dom_DaoOperation29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DaoOperation__dom_DaoOperation29", None)
        self.__dom_DaoOperation29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Type30"):
                opp_val = getattr(old_value, "dom_Type30", None)
                if opp_val == self:
                    setattr(old_value, "dom_Type30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Type30"):
                opp_val = getattr(value, "dom_Type30", None)
                setattr(value, "dom_Type30", self)

class dom_SimpleType:

    pass
class IDocumentable:

    pass
class dom_AttributeGroup(IDocumentable):

    def __init__(self, key: bool, unique: bool, filter: bool, sortorder: bool, name: str, dom_AttributeGroup: "dom_Entity" = None, dom_AttributeGroup74: "dom_Entity" = None, dom_AttributeGroup77: "dom_Entity" = None, dom_AttributeGroup102: "dom_Attribute" = None, dom_AttributeGroup122: set["dom_AttributeSortOrder"] = None, dom_AttributeGroup124: set["dom_Attribute"] = None):
        self.key = key
        self.unique = unique
        self.filter = filter
        self.sortorder = sortorder
        self.name = name
        self.dom_AttributeGroup = dom_AttributeGroup
        self.dom_AttributeGroup74 = dom_AttributeGroup74
        self.dom_AttributeGroup77 = dom_AttributeGroup77
        self.dom_AttributeGroup102 = dom_AttributeGroup102
        self.dom_AttributeGroup122 = dom_AttributeGroup122 if dom_AttributeGroup122 is not None else set()
        self.dom_AttributeGroup124 = dom_AttributeGroup124 if dom_AttributeGroup124 is not None else set()
        
    @property
    def sortorder(self) -> bool:
        return self.__sortorder

    @sortorder.setter
    def sortorder(self, sortorder: bool):
        self.__sortorder = sortorder

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def filter(self) -> bool:
        return self.__filter

    @filter.setter
    def filter(self, filter: bool):
        self.__filter = filter

    @property
    def key(self) -> bool:
        return self.__key

    @key.setter
    def key(self, key: bool):
        self.__key = key

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_AttributeGroup122(self):
        return self.__dom_AttributeGroup122

    @dom_AttributeGroup122.setter
    def dom_AttributeGroup122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeGroup__dom_AttributeGroup122", None)
        self.__dom_AttributeGroup122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_AttributeSortOrder"):
                    opp_val = getattr(item, "dom_AttributeSortOrder", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_AttributeSortOrder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_AttributeSortOrder"):
                    opp_val = getattr(item, "dom_AttributeSortOrder", None)
                    
                    setattr(item, "dom_AttributeSortOrder", self)
                    

    @property
    def dom_AttributeGroup124(self):
        return self.__dom_AttributeGroup124

    @dom_AttributeGroup124.setter
    def dom_AttributeGroup124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeGroup__dom_AttributeGroup124", None)
        self.__dom_AttributeGroup124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Attribute125"):
                    opp_val = getattr(item, "dom_Attribute125", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Attribute125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Attribute125"):
                    opp_val = getattr(item, "dom_Attribute125", None)
                    
                    setattr(item, "dom_Attribute125", self)
                    

    @property
    def dom_AttributeGroup77(self):
        return self.__dom_AttributeGroup77

    @dom_AttributeGroup77.setter
    def dom_AttributeGroup77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeGroup__dom_AttributeGroup77", None)
        self.__dom_AttributeGroup77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity76"):
                opp_val = getattr(old_value, "dom_Entity76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity76"):
                opp_val = getattr(value, "dom_Entity76", None)
                if opp_val is None:
                    setattr(value, "dom_Entity76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_AttributeGroup(self):
        return self.__dom_AttributeGroup

    @dom_AttributeGroup.setter
    def dom_AttributeGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeGroup__dom_AttributeGroup", None)
        self.__dom_AttributeGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity66"):
                opp_val = getattr(old_value, "dom_Entity66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity66"):
                opp_val = getattr(value, "dom_Entity66", None)
                if opp_val is None:
                    setattr(value, "dom_Entity66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_AttributeGroup74(self):
        return self.__dom_AttributeGroup74

    @dom_AttributeGroup74.setter
    def dom_AttributeGroup74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeGroup__dom_AttributeGroup74", None)
        self.__dom_AttributeGroup74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity73"):
                opp_val = getattr(old_value, "dom_Entity73", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity73"):
                opp_val = getattr(value, "dom_Entity73", None)
                setattr(value, "dom_Entity73", self)

    @property
    def dom_AttributeGroup102(self):
        return self.__dom_AttributeGroup102

    @dom_AttributeGroup102.setter
    def dom_AttributeGroup102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_AttributeGroup__dom_AttributeGroup102", None)
        self.__dom_AttributeGroup102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute101"):
                opp_val = getattr(old_value, "dom_Attribute101", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute101"):
                opp_val = getattr(value, "dom_Attribute101", None)
                setattr(value, "dom_Attribute101", self)

class dom_FeatureReference(IDocumentable, PresentableFeature):

    def __init__(self, all: bool, dom_FeatureReference42: "dom_DataView" = None, dom_FeatureReference: "dom_DataView" = None, dom_FeatureReference37: "dom_Entity" = None, dom_FeatureReference39: "dom_Attribute" = None, dom_FeatureReference45: set["dom_AttributeProperty"] = None, dom_FeatureReference47: "dom_Attribute" = None):
        self.all = all
        self.dom_FeatureReference42 = dom_FeatureReference42
        self.dom_FeatureReference = dom_FeatureReference
        self.dom_FeatureReference37 = dom_FeatureReference37
        self.dom_FeatureReference39 = dom_FeatureReference39
        self.dom_FeatureReference45 = dom_FeatureReference45 if dom_FeatureReference45 is not None else set()
        self.dom_FeatureReference47 = dom_FeatureReference47
        
    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def dom_FeatureReference(self):
        return self.__dom_FeatureReference

    @dom_FeatureReference.setter
    def dom_FeatureReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FeatureReference__dom_FeatureReference", None)
        self.__dom_FeatureReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataView35"):
                opp_val = getattr(old_value, "dom_DataView35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataView35"):
                opp_val = getattr(value, "dom_DataView35", None)
                if opp_val is None:
                    setattr(value, "dom_DataView35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_FeatureReference37(self):
        return self.__dom_FeatureReference37

    @dom_FeatureReference37.setter
    def dom_FeatureReference37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FeatureReference__dom_FeatureReference37", None)
        self.__dom_FeatureReference37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity"):
                opp_val = getattr(old_value, "dom_Entity", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity"):
                opp_val = getattr(value, "dom_Entity", None)
                setattr(value, "dom_Entity", self)

    @property
    def dom_FeatureReference42(self):
        return self.__dom_FeatureReference42

    @dom_FeatureReference42.setter
    def dom_FeatureReference42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FeatureReference__dom_FeatureReference42", None)
        self.__dom_FeatureReference42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataView43"):
                opp_val = getattr(old_value, "dom_DataView43", None)
                if opp_val == self:
                    setattr(old_value, "dom_DataView43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataView43"):
                opp_val = getattr(value, "dom_DataView43", None)
                setattr(value, "dom_DataView43", self)

    @property
    def dom_FeatureReference47(self):
        return self.__dom_FeatureReference47

    @dom_FeatureReference47.setter
    def dom_FeatureReference47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FeatureReference__dom_FeatureReference47", None)
        self.__dom_FeatureReference47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute48"):
                opp_val = getattr(old_value, "dom_Attribute48", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute48"):
                opp_val = getattr(value, "dom_Attribute48", None)
                setattr(value, "dom_Attribute48", self)

    @property
    def dom_FeatureReference39(self):
        return self.__dom_FeatureReference39

    @dom_FeatureReference39.setter
    def dom_FeatureReference39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FeatureReference__dom_FeatureReference39", None)
        self.__dom_FeatureReference39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute40"):
                opp_val = getattr(old_value, "dom_Attribute40", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute40"):
                opp_val = getattr(value, "dom_Attribute40", None)
                setattr(value, "dom_Attribute40", self)

    @property
    def dom_FeatureReference45(self):
        return self.__dom_FeatureReference45

    @dom_FeatureReference45.setter
    def dom_FeatureReference45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FeatureReference__dom_FeatureReference45", None)
        self.__dom_FeatureReference45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_AttributeProperty"):
                    opp_val = getattr(item, "dom_AttributeProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_AttributeProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_AttributeProperty"):
                    opp_val = getattr(item, "dom_AttributeProperty", None)
                    
                    setattr(item, "dom_AttributeProperty", self)
                    

class ReferenceableByXmadslVariable:

    pass
class dom_IElementWithNoName(QueryParameterReference, ReferenceableByXmadslVariable):

    def __init__(self, noName: str):
        self.noName = noName
        
    @property
    def noName(self) -> str:
        return self.__noName

    @noName.setter
    def noName(self, noName: str):
        self.__noName = noName

class dom_Property(IDocumentable, ReferenceableByXmadslVariable):

    def __init__(self, name: str, defaultValue: str, dom_Property: "dom_SimpleType" = None, dom_Property200: "dom_ApplicationSession" = None):
        self.name = name
        self.defaultValue = defaultValue
        self.dom_Property = dom_Property
        self.dom_Property200 = dom_Property200
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def dom_Property200(self):
        return self.__dom_Property200

    @dom_Property200.setter
    def dom_Property200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Property__dom_Property200", None)
        self.__dom_Property200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ApplicationSession"):
                opp_val = getattr(old_value, "dom_ApplicationSession", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ApplicationSession"):
                opp_val = getattr(value, "dom_ApplicationSession", None)
                if opp_val is None:
                    setattr(value, "dom_ApplicationSession", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Property(self):
        return self.__dom_Property

    @dom_Property.setter
    def dom_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Property__dom_Property", None)
        self.__dom_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_SimpleType"):
                opp_val = getattr(old_value, "dom_SimpleType", None)
                if opp_val == self:
                    setattr(old_value, "dom_SimpleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_SimpleType"):
                opp_val = getattr(value, "dom_SimpleType", None)
                setattr(value, "dom_SimpleType", self)

class dom_DelegateOperation(IDocumentable):

    def __init__(self, crudOperationType: str, many: bool, name: str, dom_DelegateOperation: "dom_Service" = None, dom_DelegateOperation22: "dom_DaoOperation" = None, dom_DelegateOperation24: "dom_DataView" = None, dom_DelegateOperation14: "dom_Operation" = None, dom_DelegateOperation18: "dom_DataView" = None, dom_DelegateOperation20: "dom_Dao" = None, dom_DelegateOperation27: "dom_Expression" = None):
        self.crudOperationType = crudOperationType
        self.many = many
        self.name = name
        self.dom_DelegateOperation = dom_DelegateOperation
        self.dom_DelegateOperation22 = dom_DelegateOperation22
        self.dom_DelegateOperation24 = dom_DelegateOperation24
        self.dom_DelegateOperation14 = dom_DelegateOperation14
        self.dom_DelegateOperation18 = dom_DelegateOperation18
        self.dom_DelegateOperation20 = dom_DelegateOperation20
        self.dom_DelegateOperation27 = dom_DelegateOperation27
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def crudOperationType(self) -> str:
        return self.__crudOperationType

    @crudOperationType.setter
    def crudOperationType(self, crudOperationType: str):
        self.__crudOperationType = crudOperationType

    @property
    def dom_DelegateOperation24(self):
        return self.__dom_DelegateOperation24

    @dom_DelegateOperation24.setter
    def dom_DelegateOperation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DelegateOperation__dom_DelegateOperation24", None)
        self.__dom_DelegateOperation24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataView25"):
                opp_val = getattr(old_value, "dom_DataView25", None)
                if opp_val == self:
                    setattr(old_value, "dom_DataView25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataView25"):
                opp_val = getattr(value, "dom_DataView25", None)
                setattr(value, "dom_DataView25", self)

    @property
    def dom_DelegateOperation20(self):
        return self.__dom_DelegateOperation20

    @dom_DelegateOperation20.setter
    def dom_DelegateOperation20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DelegateOperation__dom_DelegateOperation20", None)
        self.__dom_DelegateOperation20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao"):
                opp_val = getattr(old_value, "dom_Dao", None)
                if opp_val == self:
                    setattr(old_value, "dom_Dao", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao"):
                opp_val = getattr(value, "dom_Dao", None)
                setattr(value, "dom_Dao", self)

    @property
    def dom_DelegateOperation14(self):
        return self.__dom_DelegateOperation14

    @dom_DelegateOperation14.setter
    def dom_DelegateOperation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DelegateOperation__dom_DelegateOperation14", None)
        self.__dom_DelegateOperation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Operation13"):
                opp_val = getattr(old_value, "dom_Operation13", None)
                if opp_val == self:
                    setattr(old_value, "dom_Operation13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Operation13"):
                opp_val = getattr(value, "dom_Operation13", None)
                setattr(value, "dom_Operation13", self)

    @property
    def dom_DelegateOperation22(self):
        return self.__dom_DelegateOperation22

    @dom_DelegateOperation22.setter
    def dom_DelegateOperation22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DelegateOperation__dom_DelegateOperation22", None)
        self.__dom_DelegateOperation22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DaoOperation"):
                opp_val = getattr(old_value, "dom_DaoOperation", None)
                if opp_val == self:
                    setattr(old_value, "dom_DaoOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DaoOperation"):
                opp_val = getattr(value, "dom_DaoOperation", None)
                setattr(value, "dom_DaoOperation", self)

    @property
    def dom_DelegateOperation(self):
        return self.__dom_DelegateOperation

    @dom_DelegateOperation.setter
    def dom_DelegateOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DelegateOperation__dom_DelegateOperation", None)
        self.__dom_DelegateOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Service8"):
                opp_val = getattr(old_value, "dom_Service8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Service8"):
                opp_val = getattr(value, "dom_Service8", None)
                if opp_val is None:
                    setattr(value, "dom_Service8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_DelegateOperation27(self):
        return self.__dom_DelegateOperation27

    @dom_DelegateOperation27.setter
    def dom_DelegateOperation27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DelegateOperation__dom_DelegateOperation27", None)
        self.__dom_DelegateOperation27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression"):
                opp_val = getattr(old_value, "dom_Expression", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression"):
                opp_val = getattr(value, "dom_Expression", None)
                setattr(value, "dom_Expression", self)

    @property
    def dom_DelegateOperation18(self):
        return self.__dom_DelegateOperation18

    @dom_DelegateOperation18.setter
    def dom_DelegateOperation18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_DelegateOperation__dom_DelegateOperation18", None)
        self.__dom_DelegateOperation18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataView"):
                opp_val = getattr(old_value, "dom_DataView", None)
                if opp_val == self:
                    setattr(old_value, "dom_DataView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataView"):
                opp_val = getattr(value, "dom_DataView", None)
                setattr(value, "dom_DataView", self)

class dom_Dependant(ABC):

    pass
class Dependant:

    pass
class dom_Entity(Dependant, ComplexType):

    pass
class dom_Parameter(QueryParameterReference, QueryParameter):

    def __init__(self, many: bool, name: str, dom_Parameter: "dom_Operation" = None, dom_Parameter16: "dom_Type" = None):
        self.many = many
        self.name = name
        self.dom_Parameter = dom_Parameter
        self.dom_Parameter16 = dom_Parameter16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def dom_Parameter16(self):
        return self.__dom_Parameter16

    @dom_Parameter16.setter
    def dom_Parameter16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Parameter__dom_Parameter16", None)
        self.__dom_Parameter16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Type"):
                opp_val = getattr(old_value, "dom_Type", None)
                if opp_val == self:
                    setattr(old_value, "dom_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Type"):
                opp_val = getattr(value, "dom_Type", None)
                setattr(value, "dom_Type", self)

    @property
    def dom_Parameter(self):
        return self.__dom_Parameter

    @dom_Parameter.setter
    def dom_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Parameter__dom_Parameter", None)
        self.__dom_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Operation11"):
                opp_val = getattr(old_value, "dom_Operation11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Operation11"):
                opp_val = getattr(value, "dom_Operation11", None)
                if opp_val is None:
                    setattr(value, "dom_Operation11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DaoOperation:

    pass
class dom_QueryOperation(IDocumentable, DaoOperation):

    pass
class dom_Operation(IDocumentable, DaoOperation):

    def __init__(self, expression: str, dom_Operation: "dom_Service" = None, dom_Operation11: set["dom_Parameter"] = None, dom_Operation13: "dom_DelegateOperation" = None, dom_Operation136: "dom_Dao" = None):
        self.expression = expression
        self.dom_Operation = dom_Operation
        self.dom_Operation11 = dom_Operation11 if dom_Operation11 is not None else set()
        self.dom_Operation13 = dom_Operation13
        self.dom_Operation136 = dom_Operation136
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def dom_Operation136(self):
        return self.__dom_Operation136

    @dom_Operation136.setter
    def dom_Operation136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Operation__dom_Operation136", None)
        self.__dom_Operation136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Dao135"):
                opp_val = getattr(old_value, "dom_Dao135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Dao135"):
                opp_val = getattr(value, "dom_Dao135", None)
                if opp_val is None:
                    setattr(value, "dom_Dao135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Operation11(self):
        return self.__dom_Operation11

    @dom_Operation11.setter
    def dom_Operation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Operation__dom_Operation11", None)
        self.__dom_Operation11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Parameter"):
                    opp_val = getattr(item, "dom_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Parameter"):
                    opp_val = getattr(item, "dom_Parameter", None)
                    
                    setattr(item, "dom_Parameter", self)
                    

    @property
    def dom_Operation(self):
        return self.__dom_Operation

    @dom_Operation.setter
    def dom_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Operation__dom_Operation", None)
        self.__dom_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Service6"):
                opp_val = getattr(old_value, "dom_Service6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Service6"):
                opp_val = getattr(value, "dom_Service6", None)
                if opp_val is None:
                    setattr(value, "dom_Service6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Operation13(self):
        return self.__dom_Operation13

    @dom_Operation13.setter
    def dom_Operation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Operation__dom_Operation13", None)
        self.__dom_Operation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DelegateOperation14"):
                opp_val = getattr(old_value, "dom_DelegateOperation14", None)
                if opp_val == self:
                    setattr(old_value, "dom_DelegateOperation14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DelegateOperation14"):
                opp_val = getattr(value, "dom_DelegateOperation14", None)
                setattr(value, "dom_DelegateOperation14", self)

class dom_Attribute(IDocumentable, QueryParameterReference, ReferenceableByXmadslVariable, PresentableFeature):

    def __init__(self, identifier: bool, version: bool, composition: bool, many: bool, defaultValue: str, dataTypeName: str, reference: bool, readOnly: bool, required: bool, derived: bool, transient: bool, dom_Attribute: "dom_ComplexType" = None, dom_Attribute3: "dom_ComplexType" = None, dom_Attribute40: "dom_FeatureReference" = None, dom_Attribute61: "dom_PropertyMapping" = None, dom_Attribute48: "dom_FeatureReference" = None, dom_Attribute58: "dom_PropertyMapping" = None, dom_Attribute86: "dom_Entity" = None, dom_Attribute89: "dom_Entity" = None, dom_Attribute80: "dom_Entity" = None, dom_Attribute83: "dom_Entity" = None, dom_Attribute104: "dom_Type" = None, dom_Attribute108: "dom_Attribute" = None, dom_Attribute106: "dom_Attribute" = None, dom_Attribute91: "dom_DataTypeAndTypeParameter" = None, dom_Attribute93: "dom_IncrementerReference" = None, dom_Attribute96: "dom_Attribute" = None, dom_Attribute94: "dom_Attribute" = None, dom_Attribute98: set["dom_AttributeProperty"] = None, dom_Attribute101: "dom_AttributeGroup" = None, dom_Attribute111: "dom_Attribute" = None, dom_Attribute109: set["dom_Attribute"] = None, dom_Attribute120: "dom_AttributeTextProperty" = None, dom_Attribute125: "dom_AttributeGroup" = None, dom_Attribute128: "dom_AttributeSortOrder" = None, dom_Attribute130: "dom_DaoFeature" = None, dom_Attribute172: "dom_QueryParameter" = None, dom_Attribute195: "dom_DataBaseConstraint" = None, dom_Attribute198: "dom_DataBaseConstraint" = None, dom_Attribute217: "dom_CallOutputParameter" = None, dom_Attribute220: "dom_CallOutputParameter" = None, dom_Attribute214: "dom_CallInputParameter" = None, dom_Attribute273: "dom_Join" = None, dom_Attribute295: "dom_QueryParameterValue" = None):
        self.identifier = identifier
        self.version = version
        self.composition = composition
        self.many = many
        self.defaultValue = defaultValue
        self.dataTypeName = dataTypeName
        self.reference = reference
        self.readOnly = readOnly
        self.required = required
        self.derived = derived
        self.transient = transient
        self.dom_Attribute = dom_Attribute
        self.dom_Attribute3 = dom_Attribute3
        self.dom_Attribute40 = dom_Attribute40
        self.dom_Attribute61 = dom_Attribute61
        self.dom_Attribute48 = dom_Attribute48
        self.dom_Attribute58 = dom_Attribute58
        self.dom_Attribute86 = dom_Attribute86
        self.dom_Attribute89 = dom_Attribute89
        self.dom_Attribute80 = dom_Attribute80
        self.dom_Attribute83 = dom_Attribute83
        self.dom_Attribute104 = dom_Attribute104
        self.dom_Attribute108 = dom_Attribute108
        self.dom_Attribute106 = dom_Attribute106
        self.dom_Attribute91 = dom_Attribute91
        self.dom_Attribute93 = dom_Attribute93
        self.dom_Attribute96 = dom_Attribute96
        self.dom_Attribute94 = dom_Attribute94
        self.dom_Attribute98 = dom_Attribute98 if dom_Attribute98 is not None else set()
        self.dom_Attribute101 = dom_Attribute101
        self.dom_Attribute111 = dom_Attribute111
        self.dom_Attribute109 = dom_Attribute109 if dom_Attribute109 is not None else set()
        self.dom_Attribute120 = dom_Attribute120
        self.dom_Attribute125 = dom_Attribute125
        self.dom_Attribute128 = dom_Attribute128
        self.dom_Attribute130 = dom_Attribute130
        self.dom_Attribute172 = dom_Attribute172
        self.dom_Attribute195 = dom_Attribute195
        self.dom_Attribute198 = dom_Attribute198
        self.dom_Attribute217 = dom_Attribute217
        self.dom_Attribute220 = dom_Attribute220
        self.dom_Attribute214 = dom_Attribute214
        self.dom_Attribute273 = dom_Attribute273
        self.dom_Attribute295 = dom_Attribute295
        
    @property
    def identifier(self) -> bool:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: bool):
        self.__identifier = identifier

    @property
    def composition(self) -> bool:
        return self.__composition

    @composition.setter
    def composition(self, composition: bool):
        self.__composition = composition

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def version(self) -> bool:
        return self.__version

    @version.setter
    def version(self, version: bool):
        self.__version = version

    @property
    def dataTypeName(self) -> str:
        return self.__dataTypeName

    @dataTypeName.setter
    def dataTypeName(self, dataTypeName: str):
        self.__dataTypeName = dataTypeName

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def reference(self) -> bool:
        return self.__reference

    @reference.setter
    def reference(self, reference: bool):
        self.__reference = reference

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def dom_Attribute3(self):
        return self.__dom_Attribute3

    @dom_Attribute3.setter
    def dom_Attribute3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute3", None)
        self.__dom_Attribute3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ComplexType2"):
                opp_val = getattr(old_value, "dom_ComplexType2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ComplexType2"):
                opp_val = getattr(value, "dom_ComplexType2", None)
                if opp_val is None:
                    setattr(value, "dom_ComplexType2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Attribute86(self):
        return self.__dom_Attribute86

    @dom_Attribute86.setter
    def dom_Attribute86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute86", None)
        self.__dom_Attribute86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity85"):
                opp_val = getattr(old_value, "dom_Entity85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity85"):
                opp_val = getattr(value, "dom_Entity85", None)
                if opp_val is None:
                    setattr(value, "dom_Entity85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Attribute98(self):
        return self.__dom_Attribute98

    @dom_Attribute98.setter
    def dom_Attribute98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute98", None)
        self.__dom_Attribute98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_AttributeProperty99"):
                    opp_val = getattr(item, "dom_AttributeProperty99", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_AttributeProperty99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_AttributeProperty99"):
                    opp_val = getattr(item, "dom_AttributeProperty99", None)
                    
                    setattr(item, "dom_AttributeProperty99", self)
                    

    @property
    def dom_Attribute40(self):
        return self.__dom_Attribute40

    @dom_Attribute40.setter
    def dom_Attribute40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute40", None)
        self.__dom_Attribute40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_FeatureReference39"):
                opp_val = getattr(old_value, "dom_FeatureReference39", None)
                if opp_val == self:
                    setattr(old_value, "dom_FeatureReference39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_FeatureReference39"):
                opp_val = getattr(value, "dom_FeatureReference39", None)
                setattr(value, "dom_FeatureReference39", self)

    @property
    def dom_Attribute195(self):
        return self.__dom_Attribute195

    @dom_Attribute195.setter
    def dom_Attribute195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute195", None)
        self.__dom_Attribute195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataBaseConstraint194"):
                opp_val = getattr(old_value, "dom_DataBaseConstraint194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataBaseConstraint194"):
                opp_val = getattr(value, "dom_DataBaseConstraint194", None)
                if opp_val is None:
                    setattr(value, "dom_DataBaseConstraint194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Attribute220(self):
        return self.__dom_Attribute220

    @dom_Attribute220.setter
    def dom_Attribute220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute220", None)
        self.__dom_Attribute220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_CallOutputParameter219"):
                opp_val = getattr(old_value, "dom_CallOutputParameter219", None)
                if opp_val == self:
                    setattr(old_value, "dom_CallOutputParameter219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_CallOutputParameter219"):
                opp_val = getattr(value, "dom_CallOutputParameter219", None)
                setattr(value, "dom_CallOutputParameter219", self)

    @property
    def dom_Attribute101(self):
        return self.__dom_Attribute101

    @dom_Attribute101.setter
    def dom_Attribute101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute101", None)
        self.__dom_Attribute101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_AttributeGroup102"):
                opp_val = getattr(old_value, "dom_AttributeGroup102", None)
                if opp_val == self:
                    setattr(old_value, "dom_AttributeGroup102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_AttributeGroup102"):
                opp_val = getattr(value, "dom_AttributeGroup102", None)
                setattr(value, "dom_AttributeGroup102", self)

    @property
    def dom_Attribute198(self):
        return self.__dom_Attribute198

    @dom_Attribute198.setter
    def dom_Attribute198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute198", None)
        self.__dom_Attribute198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataBaseConstraint197"):
                opp_val = getattr(old_value, "dom_DataBaseConstraint197", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataBaseConstraint197"):
                opp_val = getattr(value, "dom_DataBaseConstraint197", None)
                if opp_val is None:
                    setattr(value, "dom_DataBaseConstraint197", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Attribute94(self):
        return self.__dom_Attribute94

    @dom_Attribute94.setter
    def dom_Attribute94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute94", None)
        self.__dom_Attribute94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute96"):
                opp_val = getattr(old_value, "dom_Attribute96", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute96"):
                opp_val = getattr(value, "dom_Attribute96", None)
                setattr(value, "dom_Attribute96", self)

    @property
    def dom_Attribute(self):
        return self.__dom_Attribute

    @dom_Attribute.setter
    def dom_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute", None)
        self.__dom_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ComplexType"):
                opp_val = getattr(old_value, "dom_ComplexType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ComplexType"):
                opp_val = getattr(value, "dom_ComplexType", None)
                if opp_val is None:
                    setattr(value, "dom_ComplexType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Attribute96(self):
        return self.__dom_Attribute96

    @dom_Attribute96.setter
    def dom_Attribute96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute96", None)
        self.__dom_Attribute96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute94"):
                opp_val = getattr(old_value, "dom_Attribute94", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute94"):
                opp_val = getattr(value, "dom_Attribute94", None)
                setattr(value, "dom_Attribute94", self)

    @property
    def dom_Attribute58(self):
        return self.__dom_Attribute58

    @dom_Attribute58.setter
    def dom_Attribute58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute58", None)
        self.__dom_Attribute58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_PropertyMapping57"):
                opp_val = getattr(old_value, "dom_PropertyMapping57", None)
                if opp_val == self:
                    setattr(old_value, "dom_PropertyMapping57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_PropertyMapping57"):
                opp_val = getattr(value, "dom_PropertyMapping57", None)
                setattr(value, "dom_PropertyMapping57", self)

    @property
    def dom_Attribute108(self):
        return self.__dom_Attribute108

    @dom_Attribute108.setter
    def dom_Attribute108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute108", None)
        self.__dom_Attribute108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute106"):
                opp_val = getattr(old_value, "dom_Attribute106", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute106"):
                opp_val = getattr(value, "dom_Attribute106", None)
                setattr(value, "dom_Attribute106", self)

    @property
    def dom_Attribute217(self):
        return self.__dom_Attribute217

    @dom_Attribute217.setter
    def dom_Attribute217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute217", None)
        self.__dom_Attribute217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_CallOutputParameter216"):
                opp_val = getattr(old_value, "dom_CallOutputParameter216", None)
                if opp_val == self:
                    setattr(old_value, "dom_CallOutputParameter216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_CallOutputParameter216"):
                opp_val = getattr(value, "dom_CallOutputParameter216", None)
                setattr(value, "dom_CallOutputParameter216", self)

    @property
    def dom_Attribute214(self):
        return self.__dom_Attribute214

    @dom_Attribute214.setter
    def dom_Attribute214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute214", None)
        self.__dom_Attribute214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_CallInputParameter213"):
                opp_val = getattr(old_value, "dom_CallInputParameter213", None)
                if opp_val == self:
                    setattr(old_value, "dom_CallInputParameter213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_CallInputParameter213"):
                opp_val = getattr(value, "dom_CallInputParameter213", None)
                setattr(value, "dom_CallInputParameter213", self)

    @property
    def dom_Attribute295(self):
        return self.__dom_Attribute295

    @dom_Attribute295.setter
    def dom_Attribute295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute295", None)
        self.__dom_Attribute295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_QueryParameterValue294"):
                opp_val = getattr(old_value, "dom_QueryParameterValue294", None)
                if opp_val == self:
                    setattr(old_value, "dom_QueryParameterValue294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_QueryParameterValue294"):
                opp_val = getattr(value, "dom_QueryParameterValue294", None)
                setattr(value, "dom_QueryParameterValue294", self)

    @property
    def dom_Attribute83(self):
        return self.__dom_Attribute83

    @dom_Attribute83.setter
    def dom_Attribute83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute83", None)
        self.__dom_Attribute83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity82"):
                opp_val = getattr(old_value, "dom_Entity82", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity82"):
                opp_val = getattr(value, "dom_Entity82", None)
                setattr(value, "dom_Entity82", self)

    @property
    def dom_Attribute128(self):
        return self.__dom_Attribute128

    @dom_Attribute128.setter
    def dom_Attribute128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute128", None)
        self.__dom_Attribute128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_AttributeSortOrder127"):
                opp_val = getattr(old_value, "dom_AttributeSortOrder127", None)
                if opp_val == self:
                    setattr(old_value, "dom_AttributeSortOrder127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_AttributeSortOrder127"):
                opp_val = getattr(value, "dom_AttributeSortOrder127", None)
                setattr(value, "dom_AttributeSortOrder127", self)

    @property
    def dom_Attribute109(self):
        return self.__dom_Attribute109

    @dom_Attribute109.setter
    def dom_Attribute109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute109", None)
        self.__dom_Attribute109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Attribute111"):
                    opp_val = getattr(item, "dom_Attribute111", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Attribute111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Attribute111"):
                    opp_val = getattr(item, "dom_Attribute111", None)
                    
                    setattr(item, "dom_Attribute111", self)
                    

    @property
    def dom_Attribute130(self):
        return self.__dom_Attribute130

    @dom_Attribute130.setter
    def dom_Attribute130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute130", None)
        self.__dom_Attribute130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DaoFeature"):
                opp_val = getattr(old_value, "dom_DaoFeature", None)
                if opp_val == self:
                    setattr(old_value, "dom_DaoFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DaoFeature"):
                opp_val = getattr(value, "dom_DaoFeature", None)
                setattr(value, "dom_DaoFeature", self)

    @property
    def dom_Attribute91(self):
        return self.__dom_Attribute91

    @dom_Attribute91.setter
    def dom_Attribute91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute91", None)
        self.__dom_Attribute91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataTypeAndTypeParameter"):
                opp_val = getattr(old_value, "dom_DataTypeAndTypeParameter", None)
                if opp_val == self:
                    setattr(old_value, "dom_DataTypeAndTypeParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataTypeAndTypeParameter"):
                opp_val = getattr(value, "dom_DataTypeAndTypeParameter", None)
                setattr(value, "dom_DataTypeAndTypeParameter", self)

    @property
    def dom_Attribute172(self):
        return self.__dom_Attribute172

    @dom_Attribute172.setter
    def dom_Attribute172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute172", None)
        self.__dom_Attribute172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_QueryParameter171"):
                opp_val = getattr(old_value, "dom_QueryParameter171", None)
                if opp_val == self:
                    setattr(old_value, "dom_QueryParameter171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_QueryParameter171"):
                opp_val = getattr(value, "dom_QueryParameter171", None)
                setattr(value, "dom_QueryParameter171", self)

    @property
    def dom_Attribute80(self):
        return self.__dom_Attribute80

    @dom_Attribute80.setter
    def dom_Attribute80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute80", None)
        self.__dom_Attribute80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity79"):
                opp_val = getattr(old_value, "dom_Entity79", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity79"):
                opp_val = getattr(value, "dom_Entity79", None)
                setattr(value, "dom_Entity79", self)

    @property
    def dom_Attribute125(self):
        return self.__dom_Attribute125

    @dom_Attribute125.setter
    def dom_Attribute125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute125", None)
        self.__dom_Attribute125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_AttributeGroup124"):
                opp_val = getattr(old_value, "dom_AttributeGroup124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_AttributeGroup124"):
                opp_val = getattr(value, "dom_AttributeGroup124", None)
                if opp_val is None:
                    setattr(value, "dom_AttributeGroup124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Attribute111(self):
        return self.__dom_Attribute111

    @dom_Attribute111.setter
    def dom_Attribute111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute111", None)
        self.__dom_Attribute111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute109"):
                opp_val = getattr(old_value, "dom_Attribute109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute109"):
                opp_val = getattr(value, "dom_Attribute109", None)
                if opp_val is None:
                    setattr(value, "dom_Attribute109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Attribute61(self):
        return self.__dom_Attribute61

    @dom_Attribute61.setter
    def dom_Attribute61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute61", None)
        self.__dom_Attribute61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_PropertyMapping60"):
                opp_val = getattr(old_value, "dom_PropertyMapping60", None)
                if opp_val == self:
                    setattr(old_value, "dom_PropertyMapping60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_PropertyMapping60"):
                opp_val = getattr(value, "dom_PropertyMapping60", None)
                setattr(value, "dom_PropertyMapping60", self)

    @property
    def dom_Attribute273(self):
        return self.__dom_Attribute273

    @dom_Attribute273.setter
    def dom_Attribute273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute273", None)
        self.__dom_Attribute273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Join272"):
                opp_val = getattr(old_value, "dom_Join272", None)
                if opp_val == self:
                    setattr(old_value, "dom_Join272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Join272"):
                opp_val = getattr(value, "dom_Join272", None)
                setattr(value, "dom_Join272", self)

    @property
    def dom_Attribute106(self):
        return self.__dom_Attribute106

    @dom_Attribute106.setter
    def dom_Attribute106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute106", None)
        self.__dom_Attribute106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Attribute108"):
                opp_val = getattr(old_value, "dom_Attribute108", None)
                if opp_val == self:
                    setattr(old_value, "dom_Attribute108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Attribute108"):
                opp_val = getattr(value, "dom_Attribute108", None)
                setattr(value, "dom_Attribute108", self)

    @property
    def dom_Attribute120(self):
        return self.__dom_Attribute120

    @dom_Attribute120.setter
    def dom_Attribute120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute120", None)
        self.__dom_Attribute120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_AttributeTextProperty"):
                opp_val = getattr(old_value, "dom_AttributeTextProperty", None)
                if opp_val == self:
                    setattr(old_value, "dom_AttributeTextProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_AttributeTextProperty"):
                opp_val = getattr(value, "dom_AttributeTextProperty", None)
                setattr(value, "dom_AttributeTextProperty", self)

    @property
    def dom_Attribute89(self):
        return self.__dom_Attribute89

    @dom_Attribute89.setter
    def dom_Attribute89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute89", None)
        self.__dom_Attribute89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity88"):
                opp_val = getattr(old_value, "dom_Entity88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity88"):
                opp_val = getattr(value, "dom_Entity88", None)
                if opp_val is None:
                    setattr(value, "dom_Entity88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dom_Attribute93(self):
        return self.__dom_Attribute93

    @dom_Attribute93.setter
    def dom_Attribute93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute93", None)
        self.__dom_Attribute93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_IncrementerReference"):
                opp_val = getattr(old_value, "dom_IncrementerReference", None)
                if opp_val == self:
                    setattr(old_value, "dom_IncrementerReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_IncrementerReference"):
                opp_val = getattr(value, "dom_IncrementerReference", None)
                setattr(value, "dom_IncrementerReference", self)

    @property
    def dom_Attribute48(self):
        return self.__dom_Attribute48

    @dom_Attribute48.setter
    def dom_Attribute48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute48", None)
        self.__dom_Attribute48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_FeatureReference47"):
                opp_val = getattr(old_value, "dom_FeatureReference47", None)
                if opp_val == self:
                    setattr(old_value, "dom_FeatureReference47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_FeatureReference47"):
                opp_val = getattr(value, "dom_FeatureReference47", None)
                setattr(value, "dom_FeatureReference47", self)

    @property
    def dom_Attribute104(self):
        return self.__dom_Attribute104

    @dom_Attribute104.setter
    def dom_Attribute104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Attribute__dom_Attribute104", None)
        self.__dom_Attribute104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Type105"):
                opp_val = getattr(old_value, "dom_Type105", None)
                if opp_val == self:
                    setattr(old_value, "dom_Type105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Type105"):
                opp_val = getattr(value, "dom_Type105", None)
                setattr(value, "dom_Type105", self)

class Type:

    pass
class ModelElement:

    pass
class dom_ApplicationSession(ModelElement):

    pass
class dom_Dao(Dependant, ModelElement):

    def __init__(self, discriminator: str, qualifier: str, tableName: str, dom_Dao: "dom_DelegateOperation" = None, dom_Dao71: "dom_Entity" = None, dom_Dao135: set["dom_Operation"] = None, dom_Dao132: "dom_Entity" = None, dom_Dao155: set["dom_Column"] = None, dom_Dao138: set["dom_QueryOperation"] = None, dom_Dao140: set["dom_DataBaseConstraint"] = None, dom_Dao142: set["dom_Column"] = None, dom_Dao144: set["dom_ManyToOne"] = None, dom_Dao146: set["dom_OneToOne"] = None, dom_Dao148: set["dom_OneToMany"] = None, dom_Dao150: set["dom_ManyToMany"] = None, dom_Dao152: "dom_Column" = None, dom_Dao158: "dom_Column" = None, dom_Dao161: "dom_DataBaseConstraint" = None, dom_Dao164: "dom_DataBaseConstraint" = None):
        self.discriminator = discriminator
        self.qualifier = qualifier
        self.tableName = tableName
        self.dom_Dao = dom_Dao
        self.dom_Dao71 = dom_Dao71
        self.dom_Dao135 = dom_Dao135 if dom_Dao135 is not None else set()
        self.dom_Dao132 = dom_Dao132
        self.dom_Dao155 = dom_Dao155 if dom_Dao155 is not None else set()
        self.dom_Dao138 = dom_Dao138 if dom_Dao138 is not None else set()
        self.dom_Dao140 = dom_Dao140 if dom_Dao140 is not None else set()
        self.dom_Dao142 = dom_Dao142 if dom_Dao142 is not None else set()
        self.dom_Dao144 = dom_Dao144 if dom_Dao144 is not None else set()
        self.dom_Dao146 = dom_Dao146 if dom_Dao146 is not None else set()
        self.dom_Dao148 = dom_Dao148 if dom_Dao148 is not None else set()
        self.dom_Dao150 = dom_Dao150 if dom_Dao150 is not None else set()
        self.dom_Dao152 = dom_Dao152
        self.dom_Dao158 = dom_Dao158
        self.dom_Dao161 = dom_Dao161
        self.dom_Dao164 = dom_Dao164
        
    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def discriminator(self) -> str:
        return self.__discriminator

    @discriminator.setter
    def discriminator(self, discriminator: str):
        self.__discriminator = discriminator

    @property
    def dom_Dao161(self):
        return self.__dom_Dao161

    @dom_Dao161.setter
    def dom_Dao161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao161", None)
        self.__dom_Dao161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataBaseConstraint162"):
                opp_val = getattr(old_value, "dom_DataBaseConstraint162", None)
                if opp_val == self:
                    setattr(old_value, "dom_DataBaseConstraint162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataBaseConstraint162"):
                opp_val = getattr(value, "dom_DataBaseConstraint162", None)
                setattr(value, "dom_DataBaseConstraint162", self)

    @property
    def dom_Dao146(self):
        return self.__dom_Dao146

    @dom_Dao146.setter
    def dom_Dao146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao146", None)
        self.__dom_Dao146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_OneToOne"):
                    opp_val = getattr(item, "dom_OneToOne", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_OneToOne", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_OneToOne"):
                    opp_val = getattr(item, "dom_OneToOne", None)
                    
                    setattr(item, "dom_OneToOne", self)
                    

    @property
    def dom_Dao138(self):
        return self.__dom_Dao138

    @dom_Dao138.setter
    def dom_Dao138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao138", None)
        self.__dom_Dao138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_QueryOperation"):
                    opp_val = getattr(item, "dom_QueryOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_QueryOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_QueryOperation"):
                    opp_val = getattr(item, "dom_QueryOperation", None)
                    
                    setattr(item, "dom_QueryOperation", self)
                    

    @property
    def dom_Dao71(self):
        return self.__dom_Dao71

    @dom_Dao71.setter
    def dom_Dao71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao71", None)
        self.__dom_Dao71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity70"):
                opp_val = getattr(old_value, "dom_Entity70", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity70"):
                opp_val = getattr(value, "dom_Entity70", None)
                setattr(value, "dom_Entity70", self)

    @property
    def dom_Dao155(self):
        return self.__dom_Dao155

    @dom_Dao155.setter
    def dom_Dao155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao155", None)
        self.__dom_Dao155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Column156"):
                    opp_val = getattr(item, "dom_Column156", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Column156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Column156"):
                    opp_val = getattr(item, "dom_Column156", None)
                    
                    setattr(item, "dom_Column156", self)
                    

    @property
    def dom_Dao152(self):
        return self.__dom_Dao152

    @dom_Dao152.setter
    def dom_Dao152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao152", None)
        self.__dom_Dao152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Column153"):
                opp_val = getattr(old_value, "dom_Column153", None)
                if opp_val == self:
                    setattr(old_value, "dom_Column153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Column153"):
                opp_val = getattr(value, "dom_Column153", None)
                setattr(value, "dom_Column153", self)

    @property
    def dom_Dao(self):
        return self.__dom_Dao

    @dom_Dao.setter
    def dom_Dao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao", None)
        self.__dom_Dao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DelegateOperation20"):
                opp_val = getattr(old_value, "dom_DelegateOperation20", None)
                if opp_val == self:
                    setattr(old_value, "dom_DelegateOperation20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DelegateOperation20"):
                opp_val = getattr(value, "dom_DelegateOperation20", None)
                setattr(value, "dom_DelegateOperation20", self)

    @property
    def dom_Dao148(self):
        return self.__dom_Dao148

    @dom_Dao148.setter
    def dom_Dao148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao148", None)
        self.__dom_Dao148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_OneToMany"):
                    opp_val = getattr(item, "dom_OneToMany", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_OneToMany", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_OneToMany"):
                    opp_val = getattr(item, "dom_OneToMany", None)
                    
                    setattr(item, "dom_OneToMany", self)
                    

    @property
    def dom_Dao150(self):
        return self.__dom_Dao150

    @dom_Dao150.setter
    def dom_Dao150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao150", None)
        self.__dom_Dao150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_ManyToMany"):
                    opp_val = getattr(item, "dom_ManyToMany", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_ManyToMany", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_ManyToMany"):
                    opp_val = getattr(item, "dom_ManyToMany", None)
                    
                    setattr(item, "dom_ManyToMany", self)
                    

    @property
    def dom_Dao142(self):
        return self.__dom_Dao142

    @dom_Dao142.setter
    def dom_Dao142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao142", None)
        self.__dom_Dao142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Column"):
                    opp_val = getattr(item, "dom_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Column"):
                    opp_val = getattr(item, "dom_Column", None)
                    
                    setattr(item, "dom_Column", self)
                    

    @property
    def dom_Dao144(self):
        return self.__dom_Dao144

    @dom_Dao144.setter
    def dom_Dao144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao144", None)
        self.__dom_Dao144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_ManyToOne"):
                    opp_val = getattr(item, "dom_ManyToOne", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_ManyToOne", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_ManyToOne"):
                    opp_val = getattr(item, "dom_ManyToOne", None)
                    
                    setattr(item, "dom_ManyToOne", self)
                    

    @property
    def dom_Dao158(self):
        return self.__dom_Dao158

    @dom_Dao158.setter
    def dom_Dao158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao158", None)
        self.__dom_Dao158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Column159"):
                opp_val = getattr(old_value, "dom_Column159", None)
                if opp_val == self:
                    setattr(old_value, "dom_Column159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Column159"):
                opp_val = getattr(value, "dom_Column159", None)
                setattr(value, "dom_Column159", self)

    @property
    def dom_Dao140(self):
        return self.__dom_Dao140

    @dom_Dao140.setter
    def dom_Dao140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao140", None)
        self.__dom_Dao140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_DataBaseConstraint"):
                    opp_val = getattr(item, "dom_DataBaseConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_DataBaseConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_DataBaseConstraint"):
                    opp_val = getattr(item, "dom_DataBaseConstraint", None)
                    
                    setattr(item, "dom_DataBaseConstraint", self)
                    

    @property
    def dom_Dao132(self):
        return self.__dom_Dao132

    @dom_Dao132.setter
    def dom_Dao132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao132", None)
        self.__dom_Dao132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Entity133"):
                opp_val = getattr(old_value, "dom_Entity133", None)
                if opp_val == self:
                    setattr(old_value, "dom_Entity133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Entity133"):
                opp_val = getattr(value, "dom_Entity133", None)
                setattr(value, "dom_Entity133", self)

    @property
    def dom_Dao135(self):
        return self.__dom_Dao135

    @dom_Dao135.setter
    def dom_Dao135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao135", None)
        self.__dom_Dao135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Operation136"):
                    opp_val = getattr(item, "dom_Operation136", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Operation136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Operation136"):
                    opp_val = getattr(item, "dom_Operation136", None)
                    
                    setattr(item, "dom_Operation136", self)
                    

    @property
    def dom_Dao164(self):
        return self.__dom_Dao164

    @dom_Dao164.setter
    def dom_Dao164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Dao__dom_Dao164", None)
        self.__dom_Dao164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_DataBaseConstraint165"):
                opp_val = getattr(old_value, "dom_DataBaseConstraint165", None)
                if opp_val == self:
                    setattr(old_value, "dom_DataBaseConstraint165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_DataBaseConstraint165"):
                opp_val = getattr(value, "dom_DataBaseConstraint165", None)
                setattr(value, "dom_DataBaseConstraint165", self)

class dom_Mapper(ModelElement):

    def __init__(self, biDirectional: bool, toLeft: bool, toRight: bool, dom_Mapper: "dom_ComplexType" = None, dom_Mapper52: "dom_ComplexType" = None, dom_Mapper55: set["dom_PropertyMapping"] = None):
        self.biDirectional = biDirectional
        self.toLeft = toLeft
        self.toRight = toRight
        self.dom_Mapper = dom_Mapper
        self.dom_Mapper52 = dom_Mapper52
        self.dom_Mapper55 = dom_Mapper55 if dom_Mapper55 is not None else set()
        
    @property
    def toRight(self) -> bool:
        return self.__toRight

    @toRight.setter
    def toRight(self, toRight: bool):
        self.__toRight = toRight

    @property
    def toLeft(self) -> bool:
        return self.__toLeft

    @toLeft.setter
    def toLeft(self, toLeft: bool):
        self.__toLeft = toLeft

    @property
    def biDirectional(self) -> bool:
        return self.__biDirectional

    @biDirectional.setter
    def biDirectional(self, biDirectional: bool):
        self.__biDirectional = biDirectional

    @property
    def dom_Mapper(self):
        return self.__dom_Mapper

    @dom_Mapper.setter
    def dom_Mapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Mapper__dom_Mapper", None)
        self.__dom_Mapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ComplexType50"):
                opp_val = getattr(old_value, "dom_ComplexType50", None)
                if opp_val == self:
                    setattr(old_value, "dom_ComplexType50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ComplexType50"):
                opp_val = getattr(value, "dom_ComplexType50", None)
                setattr(value, "dom_ComplexType50", self)

    @property
    def dom_Mapper55(self):
        return self.__dom_Mapper55

    @dom_Mapper55.setter
    def dom_Mapper55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Mapper__dom_Mapper55", None)
        self.__dom_Mapper55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_PropertyMapping"):
                    opp_val = getattr(item, "dom_PropertyMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_PropertyMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_PropertyMapping"):
                    opp_val = getattr(item, "dom_PropertyMapping", None)
                    
                    setattr(item, "dom_PropertyMapping", self)
                    

    @property
    def dom_Mapper52(self):
        return self.__dom_Mapper52

    @dom_Mapper52.setter
    def dom_Mapper52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Mapper__dom_Mapper52", None)
        self.__dom_Mapper52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ComplexType53"):
                opp_val = getattr(old_value, "dom_ComplexType53", None)
                if opp_val == self:
                    setattr(old_value, "dom_ComplexType53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ComplexType53"):
                opp_val = getattr(value, "dom_ComplexType53", None)
                setattr(value, "dom_ComplexType53", self)

class dom_Service(Dependant, ModelElement):

    pass
class dom_ComplexType(Type, ModelElement):

    pass