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
    instanceof = "instanceof"
class MultiplicationOperator(Enum):
    multiply = "multiply"
    divide = "divide"
    modulo = "modulo"
class AdditionOperator(Enum):
    add = "add"
    subtract = "subtract"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    bitwiseNot = "bitwiseNot"
    logicalNot = "logicalNot"
class OrderByDirection(Enum):
    asc = "asc"
    ascending = "ascending"
    desc = "desc"
    descending = "descending"


############################################
# Definition of Classes
############################################

class jDOQL_OrderBySpec:

    pass
class jDOQL_HavingClause:

    pass
class jDOQL_ParameterDeclaration:

    def __init__(self, type: str, declaredParameterName: str, jDOQL_ParameterDeclaration: "jDOQL_ParametersClause" = None):
        self.type = type
        self.declaredParameterName = declaredParameterName
        self.jDOQL_ParameterDeclaration = jDOQL_ParameterDeclaration
        
        pass
    @property
    def declaredParameterName(self):
        return self.__declaredParameterName

    @declaredParameterName.setter
    def declaredParameterName(self, declaredParameterName: str):
        self.__declaredParameterName = declaredParameterName


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def jDOQL_ParameterDeclaration(self):
        return self.__jDOQL_ParameterDeclaration

    @jDOQL_ParameterDeclaration.setter
    def jDOQL_ParameterDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_ParameterDeclaration__jDOQL_ParameterDeclaration", None)
        self.__jDOQL_ParameterDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_ParametersClause49"):
                opp_val = getattr(old_value, "jDOQL_ParametersClause49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_ParametersClause49"):
                opp_val = getattr(value, "jDOQL_ParametersClause49", None)
                if opp_val is None:
                    setattr(value, "jDOQL_ParametersClause49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OrderBySpec:

    pass
class ResultSpec:

    pass
class jDOQL_ResultNaming:

    def __init__(self, identifier: str, jDOQL_ResultNaming: "jDOQL_Expression" = None):
        self.identifier = identifier
        self.jDOQL_ResultNaming = jDOQL_ResultNaming
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def jDOQL_ResultNaming(self):
        return self.__jDOQL_ResultNaming

    @jDOQL_ResultNaming.setter
    def jDOQL_ResultNaming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_ResultNaming__jDOQL_ResultNaming", None)
        self.__jDOQL_ResultNaming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression67"):
                opp_val = getattr(old_value, "jDOQL_Expression67", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression67"):
                opp_val = getattr(value, "jDOQL_Expression67", None)
                setattr(value, "jDOQL_Expression67", self)

class jDOQL_Expression(OrderBySpec, ResultSpec):

    def __init__(self, direction: str, castType: str, unaryOperator: str, literal: str, this: str, id: str, parameterName: str, name: str, isDistinct: bool, jDOQL_Expression94: "jDOQL_Expression" = None, jDOQL_Expression92: "jDOQL_Expression" = None, jDOQL_Expression97: "jDOQL_Expression" = None, jDOQL_Expression95: "jDOQL_Expression" = None, jDOQL_Expression100: "jDOQL_Expression" = None, jDOQL_Expression98: "jDOQL_Expression" = None, jDOQL_Expression103: "jDOQL_Expression" = None, jDOQL_Expression101: "jDOQL_Expression" = None, jDOQL_Expression73: "jDOQL_Expression" = None, jDOQL_Expression71: "jDOQL_Expression" = None, jDOQL_Expression76: "jDOQL_Expression" = None, jDOQL_Expression74: "jDOQL_Expression" = None, jDOQL_Expression79: "jDOQL_Expression" = None, jDOQL_Expression77: "jDOQL_Expression" = None, jDOQL_Expression82: "jDOQL_Expression" = None, jDOQL_Expression80: "jDOQL_Expression" = None, jDOQL_Expression85: "jDOQL_Expression" = None, jDOQL_Expression83: "jDOQL_Expression" = None, jDOQL_Expression88: "jDOQL_Expression" = None, jDOQL_Expression86: "jDOQL_Expression" = None, jDOQL_Expression91: "jDOQL_Expression" = None, jDOQL_Expression89: "jDOQL_Expression" = None, jDOQL_Expression117: "jDOQL_ConditionalOrExpression" = None, jDOQL_Expression119: "jDOQL_ConditionalAndExpression" = None, jDOQL_Expression121: "jDOQL_SimpleOrExpression" = None, jDOQL_Expression106: "jDOQL_Expression" = None, jDOQL_Expression104: "jDOQL_Expression" = None, jDOQL_Expression109: "jDOQL_Expression" = None, jDOQL_Expression107: "jDOQL_Expression" = None, jDOQL_Expression112: "jDOQL_Expression" = None, jDOQL_Expression110: "jDOQL_Expression" = None, jDOQL_Expression115: "jDOQL_Expression" = None, jDOQL_Expression113: "jDOQL_Expression" = None, jDOQL_Expression123: "jDOQL_SimpleAndExpression" = None, jDOQL_Expression125: "jDOQL_ComparisonOperatorExpression" = None, jDOQL_Expression127: "jDOQL_AdditionExpression" = None, jDOQL_Expression129: "jDOQL_MultiplicationExpression" = None, jDOQL_Expression131: "jDOQL_FieldAccessExpression" = None, jDOQL_Expression45: "jDOQL_WhereClause" = None, jDOQL_Expression: "jDOQL_SubqueryResultClause" = None, jDOQL_Expression40: "jDOQL_SubqueryFromClause" = None, jDOQL_Expression65: "jDOQL_RangeClause" = None, jDOQL_Expression67: "jDOQL_ResultNaming" = None, jDOQL_Expression70: "jDOQL_Expression" = None, jDOQL_Expression68: "jDOQL_Expression" = None, jDOQL_Expression52: "jDOQL_GroupByClause" = None, jDOQL_Expression57: "jDOQL_HavingClause" = None, jDOQL_Expression62: "jDOQL_RangeClause" = None):
        self.direction = direction
        self.castType = castType
        self.unaryOperator = unaryOperator
        self.literal = literal
        self.this = this
        self.id = id
        self.parameterName = parameterName
        self.name = name
        self.isDistinct = isDistinct
        self.jDOQL_Expression94 = jDOQL_Expression94
        self.jDOQL_Expression92 = jDOQL_Expression92
        self.jDOQL_Expression97 = jDOQL_Expression97
        self.jDOQL_Expression95 = jDOQL_Expression95
        self.jDOQL_Expression100 = jDOQL_Expression100
        self.jDOQL_Expression98 = jDOQL_Expression98
        self.jDOQL_Expression103 = jDOQL_Expression103
        self.jDOQL_Expression101 = jDOQL_Expression101
        self.jDOQL_Expression73 = jDOQL_Expression73
        self.jDOQL_Expression71 = jDOQL_Expression71
        self.jDOQL_Expression76 = jDOQL_Expression76
        self.jDOQL_Expression74 = jDOQL_Expression74
        self.jDOQL_Expression79 = jDOQL_Expression79
        self.jDOQL_Expression77 = jDOQL_Expression77
        self.jDOQL_Expression82 = jDOQL_Expression82
        self.jDOQL_Expression80 = jDOQL_Expression80
        self.jDOQL_Expression85 = jDOQL_Expression85
        self.jDOQL_Expression83 = jDOQL_Expression83
        self.jDOQL_Expression88 = jDOQL_Expression88
        self.jDOQL_Expression86 = jDOQL_Expression86
        self.jDOQL_Expression91 = jDOQL_Expression91
        self.jDOQL_Expression89 = jDOQL_Expression89
        self.jDOQL_Expression117 = jDOQL_Expression117
        self.jDOQL_Expression119 = jDOQL_Expression119
        self.jDOQL_Expression121 = jDOQL_Expression121
        self.jDOQL_Expression106 = jDOQL_Expression106
        self.jDOQL_Expression104 = jDOQL_Expression104
        self.jDOQL_Expression109 = jDOQL_Expression109
        self.jDOQL_Expression107 = jDOQL_Expression107
        self.jDOQL_Expression112 = jDOQL_Expression112
        self.jDOQL_Expression110 = jDOQL_Expression110
        self.jDOQL_Expression115 = jDOQL_Expression115
        self.jDOQL_Expression113 = jDOQL_Expression113
        self.jDOQL_Expression123 = jDOQL_Expression123
        self.jDOQL_Expression125 = jDOQL_Expression125
        self.jDOQL_Expression127 = jDOQL_Expression127
        self.jDOQL_Expression129 = jDOQL_Expression129
        self.jDOQL_Expression131 = jDOQL_Expression131
        self.jDOQL_Expression45 = jDOQL_Expression45
        self.jDOQL_Expression = jDOQL_Expression
        self.jDOQL_Expression40 = jDOQL_Expression40
        self.jDOQL_Expression65 = jDOQL_Expression65
        self.jDOQL_Expression67 = jDOQL_Expression67
        self.jDOQL_Expression70 = jDOQL_Expression70
        self.jDOQL_Expression68 = jDOQL_Expression68
        self.jDOQL_Expression52 = jDOQL_Expression52
        self.jDOQL_Expression57 = jDOQL_Expression57
        self.jDOQL_Expression62 = jDOQL_Expression62
        
        pass
    @property
    def literal(self):
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def this(self):
        return self.__this

    @this.setter
    def this(self, this: str):
        self.__this = this


    @property
    def castType(self):
        return self.__castType

    @castType.setter
    def castType(self, castType: str):
        self.__castType = castType


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def unaryOperator(self):
        return self.__unaryOperator

    @unaryOperator.setter
    def unaryOperator(self, unaryOperator: str):
        self.__unaryOperator = unaryOperator


    @property
    def parameterName(self):
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName


    @property
    def jDOQL_Expression94(self):
        return self.__jDOQL_Expression94

    @jDOQL_Expression94.setter
    def jDOQL_Expression94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression94", None)
        self.__jDOQL_Expression94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression92"):
                opp_val = getattr(old_value, "jDOQL_Expression92", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression92"):
                opp_val = getattr(value, "jDOQL_Expression92", None)
                setattr(value, "jDOQL_Expression92", self)

    @property
    def jDOQL_Expression131(self):
        return self.__jDOQL_Expression131

    @jDOQL_Expression131.setter
    def jDOQL_Expression131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression131", None)
        self.__jDOQL_Expression131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_FieldAccessExpression"):
                opp_val = getattr(old_value, "jDOQL_FieldAccessExpression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_FieldAccessExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_FieldAccessExpression"):
                opp_val = getattr(value, "jDOQL_FieldAccessExpression", None)
                setattr(value, "jDOQL_FieldAccessExpression", self)

    @property
    def jDOQL_Expression74(self):
        return self.__jDOQL_Expression74

    @jDOQL_Expression74.setter
    def jDOQL_Expression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression74", None)
        self.__jDOQL_Expression74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression76"):
                opp_val = getattr(old_value, "jDOQL_Expression76", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression76"):
                opp_val = getattr(value, "jDOQL_Expression76", None)
                setattr(value, "jDOQL_Expression76", self)

    @property
    def jDOQL_Expression109(self):
        return self.__jDOQL_Expression109

    @jDOQL_Expression109.setter
    def jDOQL_Expression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression109", None)
        self.__jDOQL_Expression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression107"):
                opp_val = getattr(old_value, "jDOQL_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression107"):
                opp_val = getattr(value, "jDOQL_Expression107", None)
                setattr(value, "jDOQL_Expression107", self)

    @property
    def jDOQL_Expression103(self):
        return self.__jDOQL_Expression103

    @jDOQL_Expression103.setter
    def jDOQL_Expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression103", None)
        self.__jDOQL_Expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression101"):
                opp_val = getattr(old_value, "jDOQL_Expression101", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression101"):
                opp_val = getattr(value, "jDOQL_Expression101", None)
                setattr(value, "jDOQL_Expression101", self)

    @property
    def jDOQL_Expression101(self):
        return self.__jDOQL_Expression101

    @jDOQL_Expression101.setter
    def jDOQL_Expression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression101", None)
        self.__jDOQL_Expression101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression103"):
                opp_val = getattr(old_value, "jDOQL_Expression103", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression103"):
                opp_val = getattr(value, "jDOQL_Expression103", None)
                setattr(value, "jDOQL_Expression103", self)

    @property
    def jDOQL_Expression112(self):
        return self.__jDOQL_Expression112

    @jDOQL_Expression112.setter
    def jDOQL_Expression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression112", None)
        self.__jDOQL_Expression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression110"):
                opp_val = getattr(old_value, "jDOQL_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression110"):
                opp_val = getattr(value, "jDOQL_Expression110", None)
                setattr(value, "jDOQL_Expression110", self)

    @property
    def jDOQL_Expression88(self):
        return self.__jDOQL_Expression88

    @jDOQL_Expression88.setter
    def jDOQL_Expression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression88", None)
        self.__jDOQL_Expression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression86"):
                opp_val = getattr(old_value, "jDOQL_Expression86", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression86"):
                opp_val = getattr(value, "jDOQL_Expression86", None)
                setattr(value, "jDOQL_Expression86", self)

    @property
    def jDOQL_Expression65(self):
        return self.__jDOQL_Expression65

    @jDOQL_Expression65.setter
    def jDOQL_Expression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression65", None)
        self.__jDOQL_Expression65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_RangeClause64"):
                opp_val = getattr(old_value, "jDOQL_RangeClause64", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_RangeClause64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_RangeClause64"):
                opp_val = getattr(value, "jDOQL_RangeClause64", None)
                setattr(value, "jDOQL_RangeClause64", self)

    @property
    def jDOQL_Expression95(self):
        return self.__jDOQL_Expression95

    @jDOQL_Expression95.setter
    def jDOQL_Expression95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression95", None)
        self.__jDOQL_Expression95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression97"):
                opp_val = getattr(old_value, "jDOQL_Expression97", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression97"):
                opp_val = getattr(value, "jDOQL_Expression97", None)
                setattr(value, "jDOQL_Expression97", self)

    @property
    def jDOQL_Expression70(self):
        return self.__jDOQL_Expression70

    @jDOQL_Expression70.setter
    def jDOQL_Expression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression70", None)
        self.__jDOQL_Expression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression68"):
                opp_val = getattr(old_value, "jDOQL_Expression68", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression68"):
                opp_val = getattr(value, "jDOQL_Expression68", None)
                setattr(value, "jDOQL_Expression68", self)

    @property
    def jDOQL_Expression127(self):
        return self.__jDOQL_Expression127

    @jDOQL_Expression127.setter
    def jDOQL_Expression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression127", None)
        self.__jDOQL_Expression127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_AdditionExpression"):
                opp_val = getattr(old_value, "jDOQL_AdditionExpression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_AdditionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_AdditionExpression"):
                opp_val = getattr(value, "jDOQL_AdditionExpression", None)
                setattr(value, "jDOQL_AdditionExpression", self)

    @property
    def jDOQL_Expression91(self):
        return self.__jDOQL_Expression91

    @jDOQL_Expression91.setter
    def jDOQL_Expression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression91", None)
        self.__jDOQL_Expression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression89"):
                opp_val = getattr(old_value, "jDOQL_Expression89", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression89"):
                opp_val = getattr(value, "jDOQL_Expression89", None)
                setattr(value, "jDOQL_Expression89", self)

    @property
    def jDOQL_Expression(self):
        return self.__jDOQL_Expression

    @jDOQL_Expression.setter
    def jDOQL_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression", None)
        self.__jDOQL_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SubqueryResultClause"):
                opp_val = getattr(old_value, "jDOQL_SubqueryResultClause", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SubqueryResultClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SubqueryResultClause"):
                opp_val = getattr(value, "jDOQL_SubqueryResultClause", None)
                setattr(value, "jDOQL_SubqueryResultClause", self)

    @property
    def jDOQL_Expression119(self):
        return self.__jDOQL_Expression119

    @jDOQL_Expression119.setter
    def jDOQL_Expression119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression119", None)
        self.__jDOQL_Expression119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_ConditionalAndExpression"):
                opp_val = getattr(old_value, "jDOQL_ConditionalAndExpression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_ConditionalAndExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_ConditionalAndExpression"):
                opp_val = getattr(value, "jDOQL_ConditionalAndExpression", None)
                setattr(value, "jDOQL_ConditionalAndExpression", self)

    @property
    def jDOQL_Expression73(self):
        return self.__jDOQL_Expression73

    @jDOQL_Expression73.setter
    def jDOQL_Expression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression73", None)
        self.__jDOQL_Expression73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression71"):
                opp_val = getattr(old_value, "jDOQL_Expression71", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression71"):
                opp_val = getattr(value, "jDOQL_Expression71", None)
                setattr(value, "jDOQL_Expression71", self)

    @property
    def jDOQL_Expression85(self):
        return self.__jDOQL_Expression85

    @jDOQL_Expression85.setter
    def jDOQL_Expression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression85", None)
        self.__jDOQL_Expression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression83"):
                opp_val = getattr(old_value, "jDOQL_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression83"):
                opp_val = getattr(value, "jDOQL_Expression83", None)
                setattr(value, "jDOQL_Expression83", self)

    @property
    def jDOQL_Expression97(self):
        return self.__jDOQL_Expression97

    @jDOQL_Expression97.setter
    def jDOQL_Expression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression97", None)
        self.__jDOQL_Expression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression95"):
                opp_val = getattr(old_value, "jDOQL_Expression95", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression95"):
                opp_val = getattr(value, "jDOQL_Expression95", None)
                setattr(value, "jDOQL_Expression95", self)

    @property
    def jDOQL_Expression121(self):
        return self.__jDOQL_Expression121

    @jDOQL_Expression121.setter
    def jDOQL_Expression121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression121", None)
        self.__jDOQL_Expression121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SimpleOrExpression"):
                opp_val = getattr(old_value, "jDOQL_SimpleOrExpression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SimpleOrExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SimpleOrExpression"):
                opp_val = getattr(value, "jDOQL_SimpleOrExpression", None)
                setattr(value, "jDOQL_SimpleOrExpression", self)

    @property
    def jDOQL_Expression67(self):
        return self.__jDOQL_Expression67

    @jDOQL_Expression67.setter
    def jDOQL_Expression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression67", None)
        self.__jDOQL_Expression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_ResultNaming"):
                opp_val = getattr(old_value, "jDOQL_ResultNaming", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_ResultNaming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_ResultNaming"):
                opp_val = getattr(value, "jDOQL_ResultNaming", None)
                setattr(value, "jDOQL_ResultNaming", self)

    @property
    def jDOQL_Expression45(self):
        return self.__jDOQL_Expression45

    @jDOQL_Expression45.setter
    def jDOQL_Expression45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression45", None)
        self.__jDOQL_Expression45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_WhereClause44"):
                opp_val = getattr(old_value, "jDOQL_WhereClause44", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_WhereClause44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_WhereClause44"):
                opp_val = getattr(value, "jDOQL_WhereClause44", None)
                setattr(value, "jDOQL_WhereClause44", self)

    @property
    def jDOQL_Expression62(self):
        return self.__jDOQL_Expression62

    @jDOQL_Expression62.setter
    def jDOQL_Expression62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression62", None)
        self.__jDOQL_Expression62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_RangeClause61"):
                opp_val = getattr(old_value, "jDOQL_RangeClause61", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_RangeClause61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_RangeClause61"):
                opp_val = getattr(value, "jDOQL_RangeClause61", None)
                setattr(value, "jDOQL_RangeClause61", self)

    @property
    def jDOQL_Expression77(self):
        return self.__jDOQL_Expression77

    @jDOQL_Expression77.setter
    def jDOQL_Expression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression77", None)
        self.__jDOQL_Expression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression79"):
                opp_val = getattr(old_value, "jDOQL_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression79"):
                opp_val = getattr(value, "jDOQL_Expression79", None)
                setattr(value, "jDOQL_Expression79", self)

    @property
    def jDOQL_Expression92(self):
        return self.__jDOQL_Expression92

    @jDOQL_Expression92.setter
    def jDOQL_Expression92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression92", None)
        self.__jDOQL_Expression92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression94"):
                opp_val = getattr(old_value, "jDOQL_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression94"):
                opp_val = getattr(value, "jDOQL_Expression94", None)
                setattr(value, "jDOQL_Expression94", self)

    @property
    def jDOQL_Expression115(self):
        return self.__jDOQL_Expression115

    @jDOQL_Expression115.setter
    def jDOQL_Expression115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression115", None)
        self.__jDOQL_Expression115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression113"):
                opp_val = getattr(old_value, "jDOQL_Expression113", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression113"):
                opp_val = getattr(value, "jDOQL_Expression113", None)
                setattr(value, "jDOQL_Expression113", self)

    @property
    def jDOQL_Expression52(self):
        return self.__jDOQL_Expression52

    @jDOQL_Expression52.setter
    def jDOQL_Expression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression52", None)
        self.__jDOQL_Expression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_GroupByClause51"):
                opp_val = getattr(old_value, "jDOQL_GroupByClause51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_GroupByClause51"):
                opp_val = getattr(value, "jDOQL_GroupByClause51", None)
                if opp_val is None:
                    setattr(value, "jDOQL_GroupByClause51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def jDOQL_Expression110(self):
        return self.__jDOQL_Expression110

    @jDOQL_Expression110.setter
    def jDOQL_Expression110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression110", None)
        self.__jDOQL_Expression110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression112"):
                opp_val = getattr(old_value, "jDOQL_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression112"):
                opp_val = getattr(value, "jDOQL_Expression112", None)
                setattr(value, "jDOQL_Expression112", self)

    @property
    def jDOQL_Expression106(self):
        return self.__jDOQL_Expression106

    @jDOQL_Expression106.setter
    def jDOQL_Expression106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression106", None)
        self.__jDOQL_Expression106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression104"):
                opp_val = getattr(old_value, "jDOQL_Expression104", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression104"):
                opp_val = getattr(value, "jDOQL_Expression104", None)
                setattr(value, "jDOQL_Expression104", self)

    @property
    def jDOQL_Expression57(self):
        return self.__jDOQL_Expression57

    @jDOQL_Expression57.setter
    def jDOQL_Expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression57", None)
        self.__jDOQL_Expression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_HavingClause56"):
                opp_val = getattr(old_value, "jDOQL_HavingClause56", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_HavingClause56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_HavingClause56"):
                opp_val = getattr(value, "jDOQL_HavingClause56", None)
                setattr(value, "jDOQL_HavingClause56", self)

    @property
    def jDOQL_Expression80(self):
        return self.__jDOQL_Expression80

    @jDOQL_Expression80.setter
    def jDOQL_Expression80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression80", None)
        self.__jDOQL_Expression80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression82"):
                opp_val = getattr(old_value, "jDOQL_Expression82", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression82"):
                opp_val = getattr(value, "jDOQL_Expression82", None)
                setattr(value, "jDOQL_Expression82", self)

    @property
    def jDOQL_Expression98(self):
        return self.__jDOQL_Expression98

    @jDOQL_Expression98.setter
    def jDOQL_Expression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression98", None)
        self.__jDOQL_Expression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression100"):
                opp_val = getattr(old_value, "jDOQL_Expression100", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression100"):
                opp_val = getattr(value, "jDOQL_Expression100", None)
                setattr(value, "jDOQL_Expression100", self)

    @property
    def jDOQL_Expression40(self):
        return self.__jDOQL_Expression40

    @jDOQL_Expression40.setter
    def jDOQL_Expression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression40", None)
        self.__jDOQL_Expression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SubqueryFromClause39"):
                opp_val = getattr(old_value, "jDOQL_SubqueryFromClause39", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SubqueryFromClause39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SubqueryFromClause39"):
                opp_val = getattr(value, "jDOQL_SubqueryFromClause39", None)
                setattr(value, "jDOQL_SubqueryFromClause39", self)

    @property
    def jDOQL_Expression107(self):
        return self.__jDOQL_Expression107

    @jDOQL_Expression107.setter
    def jDOQL_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression107", None)
        self.__jDOQL_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression109"):
                opp_val = getattr(old_value, "jDOQL_Expression109", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression109"):
                opp_val = getattr(value, "jDOQL_Expression109", None)
                setattr(value, "jDOQL_Expression109", self)

    @property
    def jDOQL_Expression68(self):
        return self.__jDOQL_Expression68

    @jDOQL_Expression68.setter
    def jDOQL_Expression68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression68", None)
        self.__jDOQL_Expression68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression70"):
                opp_val = getattr(old_value, "jDOQL_Expression70", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression70"):
                opp_val = getattr(value, "jDOQL_Expression70", None)
                setattr(value, "jDOQL_Expression70", self)

    @property
    def jDOQL_Expression100(self):
        return self.__jDOQL_Expression100

    @jDOQL_Expression100.setter
    def jDOQL_Expression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression100", None)
        self.__jDOQL_Expression100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression98"):
                opp_val = getattr(old_value, "jDOQL_Expression98", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression98"):
                opp_val = getattr(value, "jDOQL_Expression98", None)
                setattr(value, "jDOQL_Expression98", self)

    @property
    def jDOQL_Expression117(self):
        return self.__jDOQL_Expression117

    @jDOQL_Expression117.setter
    def jDOQL_Expression117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression117", None)
        self.__jDOQL_Expression117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_ConditionalOrExpression"):
                opp_val = getattr(old_value, "jDOQL_ConditionalOrExpression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_ConditionalOrExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_ConditionalOrExpression"):
                opp_val = getattr(value, "jDOQL_ConditionalOrExpression", None)
                setattr(value, "jDOQL_ConditionalOrExpression", self)

    @property
    def jDOQL_Expression123(self):
        return self.__jDOQL_Expression123

    @jDOQL_Expression123.setter
    def jDOQL_Expression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression123", None)
        self.__jDOQL_Expression123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SimpleAndExpression"):
                opp_val = getattr(old_value, "jDOQL_SimpleAndExpression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SimpleAndExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SimpleAndExpression"):
                opp_val = getattr(value, "jDOQL_SimpleAndExpression", None)
                setattr(value, "jDOQL_SimpleAndExpression", self)

    @property
    def jDOQL_Expression104(self):
        return self.__jDOQL_Expression104

    @jDOQL_Expression104.setter
    def jDOQL_Expression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression104", None)
        self.__jDOQL_Expression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression106"):
                opp_val = getattr(old_value, "jDOQL_Expression106", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression106"):
                opp_val = getattr(value, "jDOQL_Expression106", None)
                setattr(value, "jDOQL_Expression106", self)

    @property
    def jDOQL_Expression86(self):
        return self.__jDOQL_Expression86

    @jDOQL_Expression86.setter
    def jDOQL_Expression86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression86", None)
        self.__jDOQL_Expression86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression88"):
                opp_val = getattr(old_value, "jDOQL_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression88"):
                opp_val = getattr(value, "jDOQL_Expression88", None)
                setattr(value, "jDOQL_Expression88", self)

    @property
    def jDOQL_Expression83(self):
        return self.__jDOQL_Expression83

    @jDOQL_Expression83.setter
    def jDOQL_Expression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression83", None)
        self.__jDOQL_Expression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression85"):
                opp_val = getattr(old_value, "jDOQL_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression85"):
                opp_val = getattr(value, "jDOQL_Expression85", None)
                setattr(value, "jDOQL_Expression85", self)

    @property
    def jDOQL_Expression129(self):
        return self.__jDOQL_Expression129

    @jDOQL_Expression129.setter
    def jDOQL_Expression129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression129", None)
        self.__jDOQL_Expression129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_MultiplicationExpression"):
                opp_val = getattr(old_value, "jDOQL_MultiplicationExpression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_MultiplicationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_MultiplicationExpression"):
                opp_val = getattr(value, "jDOQL_MultiplicationExpression", None)
                setattr(value, "jDOQL_MultiplicationExpression", self)

    @property
    def jDOQL_Expression113(self):
        return self.__jDOQL_Expression113

    @jDOQL_Expression113.setter
    def jDOQL_Expression113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression113", None)
        self.__jDOQL_Expression113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression115"):
                opp_val = getattr(old_value, "jDOQL_Expression115", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression115"):
                opp_val = getattr(value, "jDOQL_Expression115", None)
                setattr(value, "jDOQL_Expression115", self)

    @property
    def jDOQL_Expression89(self):
        return self.__jDOQL_Expression89

    @jDOQL_Expression89.setter
    def jDOQL_Expression89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression89", None)
        self.__jDOQL_Expression89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression91"):
                opp_val = getattr(old_value, "jDOQL_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression91"):
                opp_val = getattr(value, "jDOQL_Expression91", None)
                setattr(value, "jDOQL_Expression91", self)

    @property
    def jDOQL_Expression76(self):
        return self.__jDOQL_Expression76

    @jDOQL_Expression76.setter
    def jDOQL_Expression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression76", None)
        self.__jDOQL_Expression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression74"):
                opp_val = getattr(old_value, "jDOQL_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression74"):
                opp_val = getattr(value, "jDOQL_Expression74", None)
                setattr(value, "jDOQL_Expression74", self)

    @property
    def jDOQL_Expression79(self):
        return self.__jDOQL_Expression79

    @jDOQL_Expression79.setter
    def jDOQL_Expression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression79", None)
        self.__jDOQL_Expression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression77"):
                opp_val = getattr(old_value, "jDOQL_Expression77", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression77"):
                opp_val = getattr(value, "jDOQL_Expression77", None)
                setattr(value, "jDOQL_Expression77", self)

    @property
    def jDOQL_Expression71(self):
        return self.__jDOQL_Expression71

    @jDOQL_Expression71.setter
    def jDOQL_Expression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression71", None)
        self.__jDOQL_Expression71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression73"):
                opp_val = getattr(old_value, "jDOQL_Expression73", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression73"):
                opp_val = getattr(value, "jDOQL_Expression73", None)
                setattr(value, "jDOQL_Expression73", self)

    @property
    def jDOQL_Expression125(self):
        return self.__jDOQL_Expression125

    @jDOQL_Expression125.setter
    def jDOQL_Expression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression125", None)
        self.__jDOQL_Expression125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_ComparisonOperatorExpression"):
                opp_val = getattr(old_value, "jDOQL_ComparisonOperatorExpression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_ComparisonOperatorExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_ComparisonOperatorExpression"):
                opp_val = getattr(value, "jDOQL_ComparisonOperatorExpression", None)
                setattr(value, "jDOQL_ComparisonOperatorExpression", self)

    @property
    def jDOQL_Expression82(self):
        return self.__jDOQL_Expression82

    @jDOQL_Expression82.setter
    def jDOQL_Expression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Expression__jDOQL_Expression82", None)
        self.__jDOQL_Expression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression80"):
                opp_val = getattr(old_value, "jDOQL_Expression80", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression80"):
                opp_val = getattr(value, "jDOQL_Expression80", None)
                setattr(value, "jDOQL_Expression80", self)

class jDOQL_SubqueryResultClause:

    def __init__(self, isDistinct: bool, jDOQL_SubqueryResultClause: "jDOQL_Expression" = None):
        self.isDistinct = isDistinct
        self.jDOQL_SubqueryResultClause = jDOQL_SubqueryResultClause
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def jDOQL_SubqueryResultClause(self):
        return self.__jDOQL_SubqueryResultClause

    @jDOQL_SubqueryResultClause.setter
    def jDOQL_SubqueryResultClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_SubqueryResultClause__jDOQL_SubqueryResultClause", None)
        self.__jDOQL_SubqueryResultClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression"):
                opp_val = getattr(old_value, "jDOQL_Expression", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression"):
                opp_val = getattr(value, "jDOQL_Expression", None)
                setattr(value, "jDOQL_Expression", self)

class jDOQL_ResultSpec:

    pass
class jDOQL_ResultClause:

    def __init__(self, isDistinct: bool, jDOQL_ResultClause: set["jDOQL_ResultSpec"] = None):
        self.isDistinct = isDistinct
        self.jDOQL_ResultClause = jDOQL_ResultClause if jDOQL_ResultClause is not None else set()
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def jDOQL_ResultClause(self):
        return self.__jDOQL_ResultClause

    @jDOQL_ResultClause.setter
    def jDOQL_ResultClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_ResultClause__jDOQL_ResultClause", None)
        self.__jDOQL_ResultClause = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "jDOQL_ResultSpec"):
                    opp_val = getattr(item, "jDOQL_ResultSpec", None)
                    
                    if opp_val == self:
                        setattr(item, "jDOQL_ResultSpec", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "jDOQL_ResultSpec"):
                    opp_val = getattr(item, "jDOQL_ResultSpec", None)
                    
                    setattr(item, "jDOQL_ResultSpec", self)
                    

class jDOQL_IntoClause:

    def __init__(self, resultClassName: str, jDOQL_IntoClause: "jDOQL_SelectClause" = None):
        self.resultClassName = resultClassName
        self.jDOQL_IntoClause = jDOQL_IntoClause
        
        pass
    @property
    def resultClassName(self):
        return self.__resultClassName

    @resultClassName.setter
    def resultClassName(self, resultClassName: str):
        self.__resultClassName = resultClassName


    @property
    def jDOQL_IntoClause(self):
        return self.__jDOQL_IntoClause

    @jDOQL_IntoClause.setter
    def jDOQL_IntoClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_IntoClause__jDOQL_IntoClause", None)
        self.__jDOQL_IntoClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SelectClause35"):
                opp_val = getattr(old_value, "jDOQL_SelectClause35", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SelectClause35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SelectClause35"):
                opp_val = getattr(value, "jDOQL_SelectClause35", None)
                setattr(value, "jDOQL_SelectClause35", self)

class jDOQL_EObject:

    pass
class SubquerySelectClause:

    pass
class jDOQL_VariableDeclaration:

    def __init__(self, type: str, variableName: str, jDOQL_VariableDeclaration: "jDOQL_VariablesClause" = None):
        self.type = type
        self.variableName = variableName
        self.jDOQL_VariableDeclaration = jDOQL_VariableDeclaration
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def variableName(self):
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName


    @property
    def jDOQL_VariableDeclaration(self):
        return self.__jDOQL_VariableDeclaration

    @jDOQL_VariableDeclaration.setter
    def jDOQL_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_VariableDeclaration__jDOQL_VariableDeclaration", None)
        self.__jDOQL_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_VariablesClause47"):
                opp_val = getattr(old_value, "jDOQL_VariablesClause47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_VariablesClause47"):
                opp_val = getattr(value, "jDOQL_VariablesClause47", None)
                if opp_val is None:
                    setattr(value, "jDOQL_VariablesClause47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class jDOQL_SubquerySelectClause:

    pass
class jDOQL_Alias:

    def __init__(self, identifier: str, jDOQL_Alias: "jDOQL_SubqueryFromClause" = None):
        self.identifier = identifier
        self.jDOQL_Alias = jDOQL_Alias
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def jDOQL_Alias(self):
        return self.__jDOQL_Alias

    @jDOQL_Alias.setter
    def jDOQL_Alias(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_Alias__jDOQL_Alias", None)
        self.__jDOQL_Alias = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SubqueryFromClause42"):
                opp_val = getattr(old_value, "jDOQL_SubqueryFromClause42", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SubqueryFromClause42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SubqueryFromClause42"):
                opp_val = getattr(value, "jDOQL_SubqueryFromClause42", None)
                setattr(value, "jDOQL_SubqueryFromClause42", self)

class Expression:

    pass
class jDOQL_SimpleOrExpression(Expression):

    pass
class jDOQL_ConditionalOrExpression(Expression):

    pass
class jDOQL_SimpleAndExpression(Expression):

    pass
class jDOQL_ComparisonOperatorExpression(Expression):

    def __init__(self, operator: str, jDOQL_ComparisonOperatorExpression: "jDOQL_Expression" = None):
        self.operator = operator
        self.jDOQL_ComparisonOperatorExpression = jDOQL_ComparisonOperatorExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def jDOQL_ComparisonOperatorExpression(self):
        return self.__jDOQL_ComparisonOperatorExpression

    @jDOQL_ComparisonOperatorExpression.setter
    def jDOQL_ComparisonOperatorExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_ComparisonOperatorExpression__jDOQL_ComparisonOperatorExpression", None)
        self.__jDOQL_ComparisonOperatorExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression125"):
                opp_val = getattr(old_value, "jDOQL_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression125"):
                opp_val = getattr(value, "jDOQL_Expression125", None)
                setattr(value, "jDOQL_Expression125", self)

class jDOQL_FieldAccessExpression(Expression):

    pass
class jDOQL_AdditionExpression(Expression):

    def __init__(self, operator: str, jDOQL_AdditionExpression: "jDOQL_Expression" = None):
        self.operator = operator
        self.jDOQL_AdditionExpression = jDOQL_AdditionExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def jDOQL_AdditionExpression(self):
        return self.__jDOQL_AdditionExpression

    @jDOQL_AdditionExpression.setter
    def jDOQL_AdditionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_AdditionExpression__jDOQL_AdditionExpression", None)
        self.__jDOQL_AdditionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression127"):
                opp_val = getattr(old_value, "jDOQL_Expression127", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression127"):
                opp_val = getattr(value, "jDOQL_Expression127", None)
                setattr(value, "jDOQL_Expression127", self)

class jDOQL_ConditionalAndExpression(Expression):

    pass
class jDOQL_MultiplicationExpression(Expression):

    def __init__(self, operator: str, jDOQL_MultiplicationExpression: "jDOQL_Expression" = None):
        self.operator = operator
        self.jDOQL_MultiplicationExpression = jDOQL_MultiplicationExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def jDOQL_MultiplicationExpression(self):
        return self.__jDOQL_MultiplicationExpression

    @jDOQL_MultiplicationExpression.setter
    def jDOQL_MultiplicationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_MultiplicationExpression__jDOQL_MultiplicationExpression", None)
        self.__jDOQL_MultiplicationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression129"):
                opp_val = getattr(old_value, "jDOQL_Expression129", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression129"):
                opp_val = getattr(value, "jDOQL_Expression129", None)
                setattr(value, "jDOQL_Expression129", self)

class jDOQL_Subquery(Expression):

    pass
class jDOQL_RangeClause:

    pass
class jDOQL_OrderByClause:

    pass
class jDOQL_GroupByClause:

    pass
class jDOQL_ImportClause:

    def __init__(self, importDeclarations: str, jDOQL_ImportClause: "jDOQL_SingleStringJDOQL" = None, jDOQL_ImportClause31: "jDOQL_Subquery" = None):
        self.importDeclarations = importDeclarations
        self.jDOQL_ImportClause = jDOQL_ImportClause
        self.jDOQL_ImportClause31 = jDOQL_ImportClause31
        
        pass
    @property
    def importDeclarations(self):
        return self.__importDeclarations

    @importDeclarations.setter
    def importDeclarations(self, importDeclarations: str):
        self.__importDeclarations = importDeclarations


    @property
    def jDOQL_ImportClause(self):
        return self.__jDOQL_ImportClause

    @jDOQL_ImportClause.setter
    def jDOQL_ImportClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_ImportClause__jDOQL_ImportClause", None)
        self.__jDOQL_ImportClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SingleStringJDOQL10"):
                opp_val = getattr(old_value, "jDOQL_SingleStringJDOQL10", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SingleStringJDOQL10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SingleStringJDOQL10"):
                opp_val = getattr(value, "jDOQL_SingleStringJDOQL10", None)
                setattr(value, "jDOQL_SingleStringJDOQL10", self)

    @property
    def jDOQL_ImportClause31(self):
        return self.__jDOQL_ImportClause31

    @jDOQL_ImportClause31.setter
    def jDOQL_ImportClause31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_ImportClause__jDOQL_ImportClause31", None)
        self.__jDOQL_ImportClause31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Subquery30"):
                opp_val = getattr(old_value, "jDOQL_Subquery30", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Subquery30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Subquery30"):
                opp_val = getattr(value, "jDOQL_Subquery30", None)
                setattr(value, "jDOQL_Subquery30", self)

class jDOQL_ParametersClause:

    pass
class jDOQL_VariablesClause:

    pass
class jDOQL_WhereClause:

    pass
class jDOQL_FromClause:

    def __init__(self, candidateClassName: str, isExcludeSubclasses: bool, jDOQL_FromClause: "jDOQL_SingleStringJDOQL" = None):
        self.candidateClassName = candidateClassName
        self.isExcludeSubclasses = isExcludeSubclasses
        self.jDOQL_FromClause = jDOQL_FromClause
        
        pass
    @property
    def isExcludeSubclasses(self):
        return self.__isExcludeSubclasses

    @isExcludeSubclasses.setter
    def isExcludeSubclasses(self, isExcludeSubclasses: bool):
        self.__isExcludeSubclasses = isExcludeSubclasses


    @property
    def candidateClassName(self):
        return self.__candidateClassName

    @candidateClassName.setter
    def candidateClassName(self, candidateClassName: str):
        self.__candidateClassName = candidateClassName


    @property
    def jDOQL_FromClause(self):
        return self.__jDOQL_FromClause

    @jDOQL_FromClause.setter
    def jDOQL_FromClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_FromClause__jDOQL_FromClause", None)
        self.__jDOQL_FromClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SingleStringJDOQL2"):
                opp_val = getattr(old_value, "jDOQL_SingleStringJDOQL2", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SingleStringJDOQL2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SingleStringJDOQL2"):
                opp_val = getattr(value, "jDOQL_SingleStringJDOQL2", None)
                setattr(value, "jDOQL_SingleStringJDOQL2", self)

class jDOQL_SelectClause(SubquerySelectClause):

    def __init__(self, isUnique: bool, jDOQL_SelectClause: "jDOQL_SingleStringJDOQL" = None, jDOQL_SelectClause33: "jDOQL_EObject" = None, jDOQL_SelectClause35: "jDOQL_IntoClause" = None):
        self.isUnique = isUnique
        self.jDOQL_SelectClause = jDOQL_SelectClause
        self.jDOQL_SelectClause33 = jDOQL_SelectClause33
        self.jDOQL_SelectClause35 = jDOQL_SelectClause35
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique


    @property
    def jDOQL_SelectClause35(self):
        return self.__jDOQL_SelectClause35

    @jDOQL_SelectClause35.setter
    def jDOQL_SelectClause35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_SelectClause__jDOQL_SelectClause35", None)
        self.__jDOQL_SelectClause35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_IntoClause"):
                opp_val = getattr(old_value, "jDOQL_IntoClause", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_IntoClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_IntoClause"):
                opp_val = getattr(value, "jDOQL_IntoClause", None)
                setattr(value, "jDOQL_IntoClause", self)

    @property
    def jDOQL_SelectClause33(self):
        return self.__jDOQL_SelectClause33

    @jDOQL_SelectClause33.setter
    def jDOQL_SelectClause33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_SelectClause__jDOQL_SelectClause33", None)
        self.__jDOQL_SelectClause33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_EObject"):
                opp_val = getattr(old_value, "jDOQL_EObject", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_EObject"):
                opp_val = getattr(value, "jDOQL_EObject", None)
                setattr(value, "jDOQL_EObject", self)

    @property
    def jDOQL_SelectClause(self):
        return self.__jDOQL_SelectClause

    @jDOQL_SelectClause.setter
    def jDOQL_SelectClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_SelectClause__jDOQL_SelectClause", None)
        self.__jDOQL_SelectClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_SingleStringJDOQL"):
                opp_val = getattr(old_value, "jDOQL_SingleStringJDOQL", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_SingleStringJDOQL", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_SingleStringJDOQL"):
                opp_val = getattr(value, "jDOQL_SingleStringJDOQL", None)
                setattr(value, "jDOQL_SingleStringJDOQL", self)

class jDOQL_SingleStringJDOQL:

    pass
class jDOQL_SubqueryFromClause:

    def __init__(self, isExcludeSubclasses: bool, candidateClassName: str, jDOQL_SubqueryFromClause: "jDOQL_Subquery" = None, jDOQL_SubqueryFromClause42: "jDOQL_Alias" = None, jDOQL_SubqueryFromClause39: "jDOQL_Expression" = None):
        self.isExcludeSubclasses = isExcludeSubclasses
        self.candidateClassName = candidateClassName
        self.jDOQL_SubqueryFromClause = jDOQL_SubqueryFromClause
        self.jDOQL_SubqueryFromClause42 = jDOQL_SubqueryFromClause42
        self.jDOQL_SubqueryFromClause39 = jDOQL_SubqueryFromClause39
        
        pass
    @property
    def candidateClassName(self):
        return self.__candidateClassName

    @candidateClassName.setter
    def candidateClassName(self, candidateClassName: str):
        self.__candidateClassName = candidateClassName


    @property
    def isExcludeSubclasses(self):
        return self.__isExcludeSubclasses

    @isExcludeSubclasses.setter
    def isExcludeSubclasses(self, isExcludeSubclasses: bool):
        self.__isExcludeSubclasses = isExcludeSubclasses


    @property
    def jDOQL_SubqueryFromClause39(self):
        return self.__jDOQL_SubqueryFromClause39

    @jDOQL_SubqueryFromClause39.setter
    def jDOQL_SubqueryFromClause39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_SubqueryFromClause__jDOQL_SubqueryFromClause39", None)
        self.__jDOQL_SubqueryFromClause39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Expression40"):
                opp_val = getattr(old_value, "jDOQL_Expression40", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Expression40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Expression40"):
                opp_val = getattr(value, "jDOQL_Expression40", None)
                setattr(value, "jDOQL_Expression40", self)

    @property
    def jDOQL_SubqueryFromClause(self):
        return self.__jDOQL_SubqueryFromClause

    @jDOQL_SubqueryFromClause.setter
    def jDOQL_SubqueryFromClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_SubqueryFromClause__jDOQL_SubqueryFromClause", None)
        self.__jDOQL_SubqueryFromClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Subquery19"):
                opp_val = getattr(old_value, "jDOQL_Subquery19", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Subquery19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Subquery19"):
                opp_val = getattr(value, "jDOQL_Subquery19", None)
                setattr(value, "jDOQL_Subquery19", self)

    @property
    def jDOQL_SubqueryFromClause42(self):
        return self.__jDOQL_SubqueryFromClause42

    @jDOQL_SubqueryFromClause42.setter
    def jDOQL_SubqueryFromClause42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jDOQL_SubqueryFromClause__jDOQL_SubqueryFromClause42", None)
        self.__jDOQL_SubqueryFromClause42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jDOQL_Alias"):
                opp_val = getattr(old_value, "jDOQL_Alias", None)
                if opp_val == self:
                    setattr(old_value, "jDOQL_Alias", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jDOQL_Alias"):
                opp_val = getattr(value, "jDOQL_Alias", None)
                setattr(value, "jDOQL_Alias", self)
