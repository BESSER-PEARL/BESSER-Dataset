from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PredicateComparisonOperator(Enum):
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    LESS_THAN = "LESS_THAN"
class NullOrderingType(Enum):
    NONE = "NONE"
    NULLS_FIRST = "NULLS_FIRST"
    NULLS_LAST = "NULLS_LAST"
class UpdatabilityType(Enum):
    READ_ONLY = "READ_ONLY"
    UPDATE = "UPDATE"
class ValueExpressionCombinedOperator(Enum):
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    CONCATENATE = "CONCATENATE"
class ValueExpressionLabeledDurationType(Enum):
    YEARS = "YEARS"
    MONTHS = "MONTHS"
    DAYS = "DAYS"
    HOURS = "HOURS"
    MINUTES = "MINUTES"
    SECONDS = "SECONDS"
    MICROSECONDS = "MICROSECONDS"
class QueryCombinedOperator(Enum):
    UNION = "UNION"
    UNION_ALL = "UNION_ALL"
    INTERSECT = "INTERSECT"
    INTERSECT_ALL = "INTERSECT_ALL"
    EXCEPT = "EXCEPT"
    EXCEPT_ALL = "EXCEPT_ALL"
class ValueExpressionUnaryOperator(Enum):
    NONE = "NONE"
    PLUS = "PLUS"
    MINUS = "MINUS"
class SuperGroupType(Enum):
    CUBE = "CUBE"
    GRANDTOTAL = "GRANDTOTAL"
    ROLLUP = "ROLLUP"
class TableJoinedOperator(Enum):
    EXPLICIT_INNER = "EXPLICIT_INNER"
    LEFT_OUTER = "LEFT_OUTER"
    RIGHT_OUTER = "RIGHT_OUTER"
    FULL_OUTER = "FULL_OUTER"
    DEFAULT_INNER = "DEFAULT_INNER"
class PredicateQuantifiedType(Enum):
    SOME = "SOME"
    ANY = "ANY"
    ALL = "ALL"
class SearchConditionCombinedOperator(Enum):
    AND = "AND"
    OR = "OR"
class OrderingSpecType(Enum):
    NONE = "NONE"
    ASC = "ASC"
    DESC = "DESC"


############################################
# Definition of Classes
############################################

class statements_SQLControlStatement:

    pass
class Procedure:

    pass
class MergeOperationSpecification:

    pass
class UpdateSource:

    pass
class statements_SQLDataChangeStatement:

    pass
class SQLObject:

    pass
class query_SQLQueryObject(SQLObject):

    def __init__(self):
        
        pass
    def setSQL(self, query_sqlText):
        # TODO: Implement setSQL method
        pass

    def getSQL(self) :
        # TODO: Implement getSQL method
        pass

class Table:

    pass
class ValueExpressionCase:

    pass
class query_ValueExpressionCaseSearch(ValueExpressionCase):

    pass
class Grouping:

    pass
class query_SuperGroup(Grouping):

    def __init__(self, superGroupType: str, SuperGroup: "query_SuperGroupElement" = None, superGroup: set["query_SuperGroupElement"] = None):
        self.superGroupType = superGroupType
        self.SuperGroup = SuperGroup
        self.superGroup = superGroup if superGroup is not None else set()
        
        pass
    @property
    def superGroupType(self):
        return self.__superGroupType

    @superGroupType.setter
    def superGroupType(self, superGroupType: str):
        self.__superGroupType = superGroupType


    @property
    def superGroup(self):
        return self.__superGroup

    @superGroup.setter
    def superGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_SuperGroup__superGroup", None)
        self.__superGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SuperGroupElement"):
                    opp_val = getattr(item, "SuperGroupElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SuperGroupElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SuperGroupElement"):
                    opp_val = getattr(item, "SuperGroupElement", None)
                    
                    setattr(item, "SuperGroupElement", self)
                    

    @property
    def SuperGroup(self):
        return self.__SuperGroup

    @SuperGroup.setter
    def SuperGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_SuperGroup__SuperGroup", None)
        self.__SuperGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superGroupElementList"):
                opp_val = getattr(old_value, "superGroupElementList", None)
                if opp_val == self:
                    setattr(old_value, "superGroupElementList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superGroupElementList"):
                opp_val = getattr(value, "superGroupElementList", None)
                setattr(value, "superGroupElementList", self)

class SuperGroupElement:

    pass
class query_SuperGroupElementExpression(SuperGroupElement):

    pass
class query_SuperGroupElementSublist(SuperGroupElement):

    pass
class GroupingSetsElement:

    pass
class query_GroupingSetsElementSublist(GroupingSetsElement):

    pass
class query_GroupingSetsElementExpression(GroupingSetsElement):

    pass
class GroupingSpecification:

    pass
class query_Grouping(GroupingSpecification):

    pass
class query_GroupingSets(GroupingSpecification):

    pass
class QueryValueExpression:

    pass
class query_ValueExpressionAtomic(QueryValueExpression):

    pass
class Function:

    pass
class query_MergeInsertSpecification(MergeOperationSpecification):

    pass
class ValueExpressionAtomic:

    pass
class query_ValueExpressionCase(ValueExpressionAtomic):

    pass
class query_ValueExpressionDefaultValue(ValueExpressionAtomic):

    pass
class query_ValueExpressionNullValue(ValueExpressionAtomic):

    pass
class query_ValueExpressionSimple(ValueExpressionAtomic):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class PredicateQuantified:

    pass
class PredicateIn:

    pass
class Predicate:

    pass
class query_PredicateIn(Predicate):

    def __init__(self, notIn: bool):
        self.notIn = notIn
        
        pass
    @property
    def notIn(self):
        return self.__notIn

    @notIn.setter
    def notIn(self, notIn: bool):
        self.__notIn = notIn


class query_PredicateQuantified(Predicate):

    pass
class QueryResultSpecification:

    pass
class query_ValueExpressionVariable(ValueExpressionAtomic):

    pass
class OrderBySpecification:

    pass
class query_OrderByResultColumn(OrderBySpecification):

    pass
class query_OrderByOrdinal(OrderBySpecification):

    def __init__(self, ordinalValue: int):
        self.ordinalValue = ordinalValue
        
        pass
    @property
    def ordinalValue(self):
        return self.__ordinalValue

    @ordinalValue.setter
    def ordinalValue(self, ordinalValue: int):
        self.__ordinalValue = ordinalValue


class QuerySearchCondition:

    pass
class query_Predicate(QuerySearchCondition):

    def __init__(self, negatedPredicate: bool, hasSelectivity: bool, selectivityValue: str):
        self.negatedPredicate = negatedPredicate
        self.hasSelectivity = hasSelectivity
        self.selectivityValue = selectivityValue
        
        pass
    @property
    def hasSelectivity(self):
        return self.__hasSelectivity

    @hasSelectivity.setter
    def hasSelectivity(self, hasSelectivity: bool):
        self.__hasSelectivity = hasSelectivity


    @property
    def selectivityValue(self):
        return self.__selectivityValue

    @selectivityValue.setter
    def selectivityValue(self, selectivityValue: str):
        self.__selectivityValue = selectivityValue


    @property
    def negatedPredicate(self):
        return self.__negatedPredicate

    @negatedPredicate.setter
    def negatedPredicate(self, negatedPredicate: bool):
        self.__negatedPredicate = negatedPredicate


class query_ResultTableAllColumns(QueryResultSpecification):

    pass
class TableReference:

    pass
class query_TableExpression(TableReference):

    pass
class query_TableNested(TableReference):

    pass
class QueryExpressionBody:

    pass
class query_QueryValues(QueryExpressionBody):

    pass
class query_ValueExpressionScalarSelect(ValueExpressionAtomic):

    pass
class query_ValueExpressionRow(QueryValueExpression):

    pass
class query_UpdateSourceExprList(UpdateSource):

    pass
class expressions_QueryExpression:

    pass
class query_ValueExpressionCaseSimple(ValueExpressionCase):

    pass
class query_ValueExpressionNested(QueryValueExpression):

    pass
class query_ValueExpressionLabeledDuration(ValueExpressionAtomic):

    def __init__(self, labeledDurationType: str, ValueExpressionLabeledDuration: "query_QueryValueExpression" = None, valueExprLabeledDuration: "query_QueryValueExpression" = None):
        self.labeledDurationType = labeledDurationType
        self.ValueExpressionLabeledDuration = ValueExpressionLabeledDuration
        self.valueExprLabeledDuration = valueExprLabeledDuration
        
        pass
    @property
    def labeledDurationType(self):
        return self.__labeledDurationType

    @labeledDurationType.setter
    def labeledDurationType(self, labeledDurationType: str):
        self.__labeledDurationType = labeledDurationType


    @property
    def valueExprLabeledDuration(self):
        return self.__valueExprLabeledDuration

    @valueExprLabeledDuration.setter
    def valueExprLabeledDuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionLabeledDuration__valueExprLabeledDuration", None)
        self.__valueExprLabeledDuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression279"):
                opp_val = getattr(old_value, "QueryValueExpression279", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression279"):
                opp_val = getattr(value, "QueryValueExpression279", None)
                setattr(value, "QueryValueExpression279", self)

    @property
    def ValueExpressionLabeledDuration(self):
        return self.__ValueExpressionLabeledDuration

    @ValueExpressionLabeledDuration.setter
    def ValueExpressionLabeledDuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionLabeledDuration__ValueExpressionLabeledDuration", None)
        self.__ValueExpressionLabeledDuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExpr123"):
                opp_val = getattr(old_value, "valueExpr123", None)
                if opp_val == self:
                    setattr(old_value, "valueExpr123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExpr123"):
                opp_val = getattr(value, "valueExpr123", None)
                setattr(value, "valueExpr123", self)

class query_ValueExpressionCombined(QueryValueExpression):

    def __init__(self, combinedOperator: str, ValueExpressionCombined: "query_QueryValueExpression" = None, ValueExpressionCombined107: "query_QueryValueExpression" = None, valueExprCombinedRight: "query_QueryValueExpression" = None, valueExprCombinedLeft: "query_QueryValueExpression" = None):
        self.combinedOperator = combinedOperator
        self.ValueExpressionCombined = ValueExpressionCombined
        self.ValueExpressionCombined107 = ValueExpressionCombined107
        self.valueExprCombinedRight = valueExprCombinedRight
        self.valueExprCombinedLeft = valueExprCombinedLeft
        
        pass
    @property
    def combinedOperator(self):
        return self.__combinedOperator

    @combinedOperator.setter
    def combinedOperator(self, combinedOperator: str):
        self.__combinedOperator = combinedOperator


    @property
    def valueExprCombinedRight(self):
        return self.__valueExprCombinedRight

    @valueExprCombinedRight.setter
    def valueExprCombinedRight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionCombined__valueExprCombinedRight", None)
        self.__valueExprCombinedRight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression290"):
                opp_val = getattr(old_value, "QueryValueExpression290", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression290"):
                opp_val = getattr(value, "QueryValueExpression290", None)
                setattr(value, "QueryValueExpression290", self)

    @property
    def ValueExpressionCombined107(self):
        return self.__ValueExpressionCombined107

    @ValueExpressionCombined107.setter
    def ValueExpressionCombined107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionCombined__ValueExpressionCombined107", None)
        self.__ValueExpressionCombined107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rightValueExpr106"):
                opp_val = getattr(old_value, "rightValueExpr106", None)
                if opp_val == self:
                    setattr(old_value, "rightValueExpr106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rightValueExpr106"):
                opp_val = getattr(value, "rightValueExpr106", None)
                setattr(value, "rightValueExpr106", self)

    @property
    def valueExprCombinedLeft(self):
        return self.__valueExprCombinedLeft

    @valueExprCombinedLeft.setter
    def valueExprCombinedLeft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionCombined__valueExprCombinedLeft", None)
        self.__valueExprCombinedLeft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression288"):
                opp_val = getattr(old_value, "QueryValueExpression288", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression288"):
                opp_val = getattr(value, "QueryValueExpression288", None)
                setattr(value, "QueryValueExpression288", self)

    @property
    def ValueExpressionCombined(self):
        return self.__ValueExpressionCombined

    @ValueExpressionCombined.setter
    def ValueExpressionCombined(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionCombined__ValueExpressionCombined", None)
        self.__ValueExpressionCombined = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leftValueExpr104"):
                opp_val = getattr(old_value, "leftValueExpr104", None)
                if opp_val == self:
                    setattr(old_value, "leftValueExpr104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leftValueExpr104"):
                opp_val = getattr(value, "leftValueExpr104", None)
                setattr(value, "leftValueExpr104", self)

class query_ValueExpressionFunction(ValueExpressionAtomic):

    def __init__(self, specialRegister: bool, distinct: bool, columnFunction: bool, ValueExpressionFunction: "query_QueryValueExpression" = None, valueExprFunction: set["query_QueryValueExpression"] = None, query_ValueExpressionFunction: "Function" = None):
        self.specialRegister = specialRegister
        self.distinct = distinct
        self.columnFunction = columnFunction
        self.ValueExpressionFunction = ValueExpressionFunction
        self.valueExprFunction = valueExprFunction if valueExprFunction is not None else set()
        self.query_ValueExpressionFunction = query_ValueExpressionFunction
        
        pass
    @property
    def columnFunction(self):
        return self.__columnFunction

    @columnFunction.setter
    def columnFunction(self, columnFunction: bool):
        self.__columnFunction = columnFunction


    @property
    def distinct(self):
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct


    @property
    def specialRegister(self):
        return self.__specialRegister

    @specialRegister.setter
    def specialRegister(self, specialRegister: bool):
        self.__specialRegister = specialRegister


    @property
    def query_ValueExpressionFunction(self):
        return self.__query_ValueExpressionFunction

    @query_ValueExpressionFunction.setter
    def query_ValueExpressionFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionFunction__query_ValueExpressionFunction", None)
        self.__query_ValueExpressionFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Function"):
                opp_val = getattr(old_value, "Function", None)
                if opp_val == self:
                    setattr(old_value, "Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Function"):
                opp_val = getattr(value, "Function", None)
                setattr(value, "Function", self)

    @property
    def valueExprFunction(self):
        return self.__valueExprFunction

    @valueExprFunction.setter
    def valueExprFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionFunction__valueExprFunction", None)
        self.__valueExprFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QueryValueExpression285"):
                    opp_val = getattr(item, "QueryValueExpression285", None)
                    
                    if opp_val == self:
                        setattr(item, "QueryValueExpression285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QueryValueExpression285"):
                    opp_val = getattr(item, "QueryValueExpression285", None)
                    
                    setattr(item, "QueryValueExpression285", self)
                    

    @property
    def ValueExpressionFunction(self):
        return self.__ValueExpressionFunction

    @ValueExpressionFunction.setter
    def ValueExpressionFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_ValueExpressionFunction__ValueExpressionFunction", None)
        self.__ValueExpressionFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterList"):
                opp_val = getattr(old_value, "parameterList", None)
                if opp_val == self:
                    setattr(old_value, "parameterList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterList"):
                opp_val = getattr(value, "parameterList", None)
                setattr(value, "parameterList", self)

class query_ValueExpressionCast(ValueExpressionAtomic):

    pass
class query_GroupingExpression(Grouping):

    pass
class query_PredicateQuantifiedValueSelect(PredicateQuantified):

    def __init__(self, quantifiedType: str, comparisonOperator: str, PredicateQuantifiedValueSelect: "query_QueryValueExpression" = None, PredicateQuantifiedValueSelect149: "query_QueryExpressionRoot" = None, quantifiedValueSelectRight: "query_QueryExpressionRoot" = None, quantifiedValueSelectLeft: "query_QueryValueExpression" = None):
        self.quantifiedType = quantifiedType
        self.comparisonOperator = comparisonOperator
        self.PredicateQuantifiedValueSelect = PredicateQuantifiedValueSelect
        self.PredicateQuantifiedValueSelect149 = PredicateQuantifiedValueSelect149
        self.quantifiedValueSelectRight = quantifiedValueSelectRight
        self.quantifiedValueSelectLeft = quantifiedValueSelectLeft
        
        pass
    @property
    def comparisonOperator(self):
        return self.__comparisonOperator

    @comparisonOperator.setter
    def comparisonOperator(self, comparisonOperator: str):
        self.__comparisonOperator = comparisonOperator


    @property
    def quantifiedType(self):
        return self.__quantifiedType

    @quantifiedType.setter
    def quantifiedType(self, quantifiedType: str):
        self.__quantifiedType = quantifiedType


    @property
    def quantifiedValueSelectLeft(self):
        return self.__quantifiedValueSelectLeft

    @quantifiedValueSelectLeft.setter
    def quantifiedValueSelectLeft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateQuantifiedValueSelect__quantifiedValueSelectLeft", None)
        self.__quantifiedValueSelectLeft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression244"):
                opp_val = getattr(old_value, "QueryValueExpression244", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression244"):
                opp_val = getattr(value, "QueryValueExpression244", None)
                setattr(value, "QueryValueExpression244", self)

    @property
    def quantifiedValueSelectRight(self):
        return self.__quantifiedValueSelectRight

    @quantifiedValueSelectRight.setter
    def quantifiedValueSelectRight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateQuantifiedValueSelect__quantifiedValueSelectRight", None)
        self.__quantifiedValueSelectRight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryExpressionRoot242"):
                opp_val = getattr(old_value, "QueryExpressionRoot242", None)
                if opp_val == self:
                    setattr(old_value, "QueryExpressionRoot242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryExpressionRoot242"):
                opp_val = getattr(value, "QueryExpressionRoot242", None)
                setattr(value, "QueryExpressionRoot242", self)

    @property
    def PredicateQuantifiedValueSelect149(self):
        return self.__PredicateQuantifiedValueSelect149

    @PredicateQuantifiedValueSelect149.setter
    def PredicateQuantifiedValueSelect149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateQuantifiedValueSelect__PredicateQuantifiedValueSelect149", None)
        self.__PredicateQuantifiedValueSelect149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queryExpr148"):
                opp_val = getattr(old_value, "queryExpr148", None)
                if opp_val == self:
                    setattr(old_value, "queryExpr148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queryExpr148"):
                opp_val = getattr(value, "queryExpr148", None)
                setattr(value, "queryExpr148", self)

    @property
    def PredicateQuantifiedValueSelect(self):
        return self.__PredicateQuantifiedValueSelect

    @PredicateQuantifiedValueSelect.setter
    def PredicateQuantifiedValueSelect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateQuantifiedValueSelect__PredicateQuantifiedValueSelect", None)
        self.__PredicateQuantifiedValueSelect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExpr93"):
                opp_val = getattr(old_value, "valueExpr93", None)
                if opp_val == self:
                    setattr(old_value, "valueExpr93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExpr93"):
                opp_val = getattr(value, "valueExpr93", None)
                setattr(value, "valueExpr93", self)

class query_PredicateQuantifiedRowSelect(PredicateQuantified):

    def __init__(self, quantifiedType: str, PredicateQuantifiedRowSelect: "query_QueryValueExpression" = None, PredicateQuantifiedRowSelect146: "query_QueryExpressionRoot" = None, quantifiedRowSelectLeft: set["query_QueryValueExpression"] = None, quantifiedRowSelectRight: "query_QueryExpressionRoot" = None):
        self.quantifiedType = quantifiedType
        self.PredicateQuantifiedRowSelect = PredicateQuantifiedRowSelect
        self.PredicateQuantifiedRowSelect146 = PredicateQuantifiedRowSelect146
        self.quantifiedRowSelectLeft = quantifiedRowSelectLeft if quantifiedRowSelectLeft is not None else set()
        self.quantifiedRowSelectRight = quantifiedRowSelectRight
        
        pass
    @property
    def quantifiedType(self):
        return self.__quantifiedType

    @quantifiedType.setter
    def quantifiedType(self, quantifiedType: str):
        self.__quantifiedType = quantifiedType


    @property
    def PredicateQuantifiedRowSelect146(self):
        return self.__PredicateQuantifiedRowSelect146

    @PredicateQuantifiedRowSelect146.setter
    def PredicateQuantifiedRowSelect146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateQuantifiedRowSelect__PredicateQuantifiedRowSelect146", None)
        self.__PredicateQuantifiedRowSelect146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queryExpr145"):
                opp_val = getattr(old_value, "queryExpr145", None)
                if opp_val == self:
                    setattr(old_value, "queryExpr145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queryExpr145"):
                opp_val = getattr(value, "queryExpr145", None)
                setattr(value, "queryExpr145", self)

    @property
    def quantifiedRowSelectLeft(self):
        return self.__quantifiedRowSelectLeft

    @quantifiedRowSelectLeft.setter
    def quantifiedRowSelectLeft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateQuantifiedRowSelect__quantifiedRowSelectLeft", None)
        self.__quantifiedRowSelectLeft = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QueryValueExpression248"):
                    opp_val = getattr(item, "QueryValueExpression248", None)
                    
                    if opp_val == self:
                        setattr(item, "QueryValueExpression248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QueryValueExpression248"):
                    opp_val = getattr(item, "QueryValueExpression248", None)
                    
                    setattr(item, "QueryValueExpression248", self)
                    

    @property
    def quantifiedRowSelectRight(self):
        return self.__quantifiedRowSelectRight

    @quantifiedRowSelectRight.setter
    def quantifiedRowSelectRight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateQuantifiedRowSelect__quantifiedRowSelectRight", None)
        self.__quantifiedRowSelectRight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryExpressionRoot246"):
                opp_val = getattr(old_value, "QueryExpressionRoot246", None)
                if opp_val == self:
                    setattr(old_value, "QueryExpressionRoot246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryExpressionRoot246"):
                opp_val = getattr(value, "QueryExpressionRoot246", None)
                setattr(value, "QueryExpressionRoot246", self)

    @property
    def PredicateQuantifiedRowSelect(self):
        return self.__PredicateQuantifiedRowSelect

    @PredicateQuantifiedRowSelect.setter
    def PredicateQuantifiedRowSelect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateQuantifiedRowSelect__PredicateQuantifiedRowSelect", None)
        self.__PredicateQuantifiedRowSelect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprList91"):
                opp_val = getattr(old_value, "valueExprList91", None)
                if opp_val == self:
                    setattr(old_value, "valueExprList91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprList91"):
                opp_val = getattr(value, "valueExprList91", None)
                setattr(value, "valueExprList91", self)

class query_PredicateInValueSelect(PredicateIn):

    pass
class query_PredicateInValueRowSelect(PredicateIn):

    pass
class query_PredicateInValueList(PredicateIn):

    pass
class query_PredicateBetween(Predicate):

    def __init__(self, notBetween: bool, PredicateBetween: "query_QueryValueExpression" = None, PredicateBetween97: "query_QueryValueExpression" = None, PredicateBetween99: "query_QueryValueExpression" = None, betweenLeft: "query_QueryValueExpression" = None, betweenRight1: "query_QueryValueExpression" = None, betweenRight2: "query_QueryValueExpression" = None):
        self.notBetween = notBetween
        self.PredicateBetween = PredicateBetween
        self.PredicateBetween97 = PredicateBetween97
        self.PredicateBetween99 = PredicateBetween99
        self.betweenLeft = betweenLeft
        self.betweenRight1 = betweenRight1
        self.betweenRight2 = betweenRight2
        
        pass
    @property
    def notBetween(self):
        return self.__notBetween

    @notBetween.setter
    def notBetween(self, notBetween: bool):
        self.__notBetween = notBetween


    @property
    def PredicateBetween(self):
        return self.__PredicateBetween

    @PredicateBetween.setter
    def PredicateBetween(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBetween__PredicateBetween", None)
        self.__PredicateBetween = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leftValueExpr95"):
                opp_val = getattr(old_value, "leftValueExpr95", None)
                if opp_val == self:
                    setattr(old_value, "leftValueExpr95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leftValueExpr95"):
                opp_val = getattr(value, "leftValueExpr95", None)
                setattr(value, "leftValueExpr95", self)

    @property
    def betweenRight2(self):
        return self.__betweenRight2

    @betweenRight2.setter
    def betweenRight2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBetween__betweenRight2", None)
        self.__betweenRight2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression230"):
                opp_val = getattr(old_value, "QueryValueExpression230", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression230"):
                opp_val = getattr(value, "QueryValueExpression230", None)
                setattr(value, "QueryValueExpression230", self)

    @property
    def betweenLeft(self):
        return self.__betweenLeft

    @betweenLeft.setter
    def betweenLeft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBetween__betweenLeft", None)
        self.__betweenLeft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression226"):
                opp_val = getattr(old_value, "QueryValueExpression226", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression226"):
                opp_val = getattr(value, "QueryValueExpression226", None)
                setattr(value, "QueryValueExpression226", self)

    @property
    def betweenRight1(self):
        return self.__betweenRight1

    @betweenRight1.setter
    def betweenRight1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBetween__betweenRight1", None)
        self.__betweenRight1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression228"):
                opp_val = getattr(old_value, "QueryValueExpression228", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression228"):
                opp_val = getattr(value, "QueryValueExpression228", None)
                setattr(value, "QueryValueExpression228", self)

    @property
    def PredicateBetween99(self):
        return self.__PredicateBetween99

    @PredicateBetween99.setter
    def PredicateBetween99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBetween__PredicateBetween99", None)
        self.__PredicateBetween99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rightValueExpr2"):
                opp_val = getattr(old_value, "rightValueExpr2", None)
                if opp_val == self:
                    setattr(old_value, "rightValueExpr2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rightValueExpr2"):
                opp_val = getattr(value, "rightValueExpr2", None)
                setattr(value, "rightValueExpr2", self)

    @property
    def PredicateBetween97(self):
        return self.__PredicateBetween97

    @PredicateBetween97.setter
    def PredicateBetween97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBetween__PredicateBetween97", None)
        self.__PredicateBetween97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rightValueExpr1"):
                opp_val = getattr(old_value, "rightValueExpr1", None)
                if opp_val == self:
                    setattr(old_value, "rightValueExpr1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rightValueExpr1"):
                opp_val = getattr(value, "rightValueExpr1", None)
                setattr(value, "rightValueExpr1", self)

class query_PredicateLike(Predicate):

    def __init__(self, notLike: bool, PredicateLike121: "query_QueryValueExpression" = None, PredicateLike79: "query_QueryValueExpression" = None, PredicateLike: "query_QueryValueExpression" = None, likePattern: "query_QueryValueExpression" = None, likeMatching: "query_QueryValueExpression" = None, likeEscape: "query_QueryValueExpression" = None):
        self.notLike = notLike
        self.PredicateLike121 = PredicateLike121
        self.PredicateLike79 = PredicateLike79
        self.PredicateLike = PredicateLike
        self.likePattern = likePattern
        self.likeMatching = likeMatching
        self.likeEscape = likeEscape
        
        pass
    @property
    def notLike(self):
        return self.__notLike

    @notLike.setter
    def notLike(self, notLike: bool):
        self.__notLike = notLike


    @property
    def PredicateLike(self):
        return self.__PredicateLike

    @PredicateLike.setter
    def PredicateLike(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateLike__PredicateLike", None)
        self.__PredicateLike = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patternValueExpr"):
                opp_val = getattr(old_value, "patternValueExpr", None)
                if opp_val == self:
                    setattr(old_value, "patternValueExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patternValueExpr"):
                opp_val = getattr(value, "patternValueExpr", None)
                setattr(value, "patternValueExpr", self)

    @property
    def likePattern(self):
        return self.__likePattern

    @likePattern.setter
    def likePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateLike__likePattern", None)
        self.__likePattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression234"):
                opp_val = getattr(old_value, "QueryValueExpression234", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression234"):
                opp_val = getattr(value, "QueryValueExpression234", None)
                setattr(value, "QueryValueExpression234", self)

    @property
    def PredicateLike121(self):
        return self.__PredicateLike121

    @PredicateLike121.setter
    def PredicateLike121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateLike__PredicateLike121", None)
        self.__PredicateLike121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "escapeValueExpr"):
                opp_val = getattr(old_value, "escapeValueExpr", None)
                if opp_val == self:
                    setattr(old_value, "escapeValueExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "escapeValueExpr"):
                opp_val = getattr(value, "escapeValueExpr", None)
                setattr(value, "escapeValueExpr", self)

    @property
    def likeMatching(self):
        return self.__likeMatching

    @likeMatching.setter
    def likeMatching(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateLike__likeMatching", None)
        self.__likeMatching = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression236"):
                opp_val = getattr(old_value, "QueryValueExpression236", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression236"):
                opp_val = getattr(value, "QueryValueExpression236", None)
                setattr(value, "QueryValueExpression236", self)

    @property
    def likeEscape(self):
        return self.__likeEscape

    @likeEscape.setter
    def likeEscape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateLike__likeEscape", None)
        self.__likeEscape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression238"):
                opp_val = getattr(old_value, "QueryValueExpression238", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression238"):
                opp_val = getattr(value, "QueryValueExpression238", None)
                setattr(value, "QueryValueExpression238", self)

    @property
    def PredicateLike79(self):
        return self.__PredicateLike79

    @PredicateLike79.setter
    def PredicateLike79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateLike__PredicateLike79", None)
        self.__PredicateLike79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "matchingValueExpr"):
                opp_val = getattr(old_value, "matchingValueExpr", None)
                if opp_val == self:
                    setattr(old_value, "matchingValueExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "matchingValueExpr"):
                opp_val = getattr(value, "matchingValueExpr", None)
                setattr(value, "matchingValueExpr", self)

class query_PredicateBasic(Predicate):

    def __init__(self, comparisonOperator: str, PredicateBasic: "query_QueryValueExpression" = None, PredicateBasic76: "query_QueryValueExpression" = None, basicRight: "query_QueryValueExpression" = None, basicLeft: "query_QueryValueExpression" = None):
        self.comparisonOperator = comparisonOperator
        self.PredicateBasic = PredicateBasic
        self.PredicateBasic76 = PredicateBasic76
        self.basicRight = basicRight
        self.basicLeft = basicLeft
        
        pass
    @property
    def comparisonOperator(self):
        return self.__comparisonOperator

    @comparisonOperator.setter
    def comparisonOperator(self, comparisonOperator: str):
        self.__comparisonOperator = comparisonOperator


    @property
    def PredicateBasic76(self):
        return self.__PredicateBasic76

    @PredicateBasic76.setter
    def PredicateBasic76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBasic__PredicateBasic76", None)
        self.__PredicateBasic76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leftValueExpr"):
                opp_val = getattr(old_value, "leftValueExpr", None)
                if opp_val == self:
                    setattr(old_value, "leftValueExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leftValueExpr"):
                opp_val = getattr(value, "leftValueExpr", None)
                setattr(value, "leftValueExpr", self)

    @property
    def PredicateBasic(self):
        return self.__PredicateBasic

    @PredicateBasic.setter
    def PredicateBasic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBasic__PredicateBasic", None)
        self.__PredicateBasic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rightValueExpr"):
                opp_val = getattr(old_value, "rightValueExpr", None)
                if opp_val == self:
                    setattr(old_value, "rightValueExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rightValueExpr"):
                opp_val = getattr(value, "rightValueExpr", None)
                setattr(value, "rightValueExpr", self)

    @property
    def basicLeft(self):
        return self.__basicLeft

    @basicLeft.setter
    def basicLeft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBasic__basicLeft", None)
        self.__basicLeft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression224"):
                opp_val = getattr(old_value, "QueryValueExpression224", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression224"):
                opp_val = getattr(value, "QueryValueExpression224", None)
                setattr(value, "QueryValueExpression224", self)

    @property
    def basicRight(self):
        return self.__basicRight

    @basicRight.setter
    def basicRight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateBasic__basicRight", None)
        self.__basicRight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression222"):
                opp_val = getattr(old_value, "QueryValueExpression222", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression222"):
                opp_val = getattr(value, "QueryValueExpression222", None)
                setattr(value, "QueryValueExpression222", self)

class query_ResultColumn(QueryResultSpecification):

    pass
class query_OrderByValueExpression(OrderBySpecification):

    pass
class query_PredicateIsNull(Predicate):

    def __init__(self, notNull: bool, PredicateIsNull: "query_QueryValueExpression" = None, predicateNull: "query_QueryValueExpression" = None):
        self.notNull = notNull
        self.PredicateIsNull = PredicateIsNull
        self.predicateNull = predicateNull
        
        pass
    @property
    def notNull(self):
        return self.__notNull

    @notNull.setter
    def notNull(self, notNull: bool):
        self.__notNull = notNull


    @property
    def PredicateIsNull(self):
        return self.__PredicateIsNull

    @PredicateIsNull.setter
    def PredicateIsNull(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateIsNull__PredicateIsNull", None)
        self.__PredicateIsNull = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExpr81"):
                opp_val = getattr(old_value, "valueExpr81", None)
                if opp_val == self:
                    setattr(old_value, "valueExpr81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExpr81"):
                opp_val = getattr(value, "valueExpr81", None)
                setattr(value, "valueExpr81", self)

    @property
    def predicateNull(self):
        return self.__predicateNull

    @predicateNull.setter
    def predicateNull(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_PredicateIsNull__predicateNull", None)
        self.__predicateNull = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryValueExpression240"):
                opp_val = getattr(old_value, "QueryValueExpression240", None)
                if opp_val == self:
                    setattr(old_value, "QueryValueExpression240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryValueExpression240"):
                opp_val = getattr(value, "QueryValueExpression240", None)
                setattr(value, "QueryValueExpression240", self)

class query_QueryNested(QueryExpressionBody):

    pass
class query_UpdateSourceQuery(UpdateSource):

    pass
class query_PredicateExists(Predicate):

    pass
class DataType:

    pass
class expressions_ValueExpression:

    pass
class TableExpression:

    pass
class query_TableFunction(TableExpression):

    pass
class query_TableQueryLateral(TableExpression):

    pass
class query_WithTableReference(TableExpression):

    pass
class query_QueryExpressionBody(TableExpression):

    def __init__(self, rowFetchLimit: int, query: "query_QueryExpressionRoot" = None, leftQuery: "query_QueryCombined" = None, rightQuery: "query_QueryCombined" = None, queryExpr: "query_PredicateExists" = None, queryExpr62: "query_UpdateSourceQuery" = None, withTableQueryExpr: "query_WithTableSpecification" = None, nestedQuery: "query_QueryNested" = None, query66: set["query_OrderBySpecification"] = None, QueryExpressionBody184: "query_WithTableSpecification" = None, QueryExpressionBody: "query_QueryExpressionRoot" = None, QueryExpressionBody232: "query_PredicateExists" = None, QueryExpressionBody197: "query_QueryCombined" = None, QueryExpressionBody200: "query_QueryCombined" = None, QueryExpressionBody372: "query_OrderBySpecification" = None, QueryExpressionBody383: "query_UpdateSourceQuery" = None, QueryExpressionBody389: "query_QueryNested" = None, query_QueryExpressionBody: "query_TableQueryLateral" = None):
        self.rowFetchLimit = rowFetchLimit
        self.query = query
        self.leftQuery = leftQuery
        self.rightQuery = rightQuery
        self.queryExpr = queryExpr
        self.queryExpr62 = queryExpr62
        self.withTableQueryExpr = withTableQueryExpr
        self.nestedQuery = nestedQuery
        self.query66 = query66 if query66 is not None else set()
        self.QueryExpressionBody184 = QueryExpressionBody184
        self.QueryExpressionBody = QueryExpressionBody
        self.QueryExpressionBody232 = QueryExpressionBody232
        self.QueryExpressionBody197 = QueryExpressionBody197
        self.QueryExpressionBody200 = QueryExpressionBody200
        self.QueryExpressionBody372 = QueryExpressionBody372
        self.QueryExpressionBody383 = QueryExpressionBody383
        self.QueryExpressionBody389 = QueryExpressionBody389
        self.query_QueryExpressionBody = query_QueryExpressionBody
        
        pass
    @property
    def rowFetchLimit(self):
        return self.__rowFetchLimit

    @rowFetchLimit.setter
    def rowFetchLimit(self, rowFetchLimit: int):
        self.__rowFetchLimit = rowFetchLimit


    @property
    def rightQuery(self):
        return self.__rightQuery

    @rightQuery.setter
    def rightQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__rightQuery", None)
        self.__rightQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryCombined59"):
                opp_val = getattr(old_value, "QueryCombined59", None)
                if opp_val == self:
                    setattr(old_value, "QueryCombined59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryCombined59"):
                opp_val = getattr(value, "QueryCombined59", None)
                setattr(value, "QueryCombined59", self)

    @property
    def QueryExpressionBody232(self):
        return self.__QueryExpressionBody232

    @QueryExpressionBody232.setter
    def QueryExpressionBody232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__QueryExpressionBody232", None)
        self.__QueryExpressionBody232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predicateExists"):
                opp_val = getattr(old_value, "predicateExists", None)
                if opp_val == self:
                    setattr(old_value, "predicateExists", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predicateExists"):
                opp_val = getattr(value, "predicateExists", None)
                setattr(value, "predicateExists", self)

    @property
    def QueryExpressionBody383(self):
        return self.__QueryExpressionBody383

    @QueryExpressionBody383.setter
    def QueryExpressionBody383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__QueryExpressionBody383", None)
        self.__QueryExpressionBody383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "updateSourceQuery"):
                opp_val = getattr(old_value, "updateSourceQuery", None)
                if opp_val == self:
                    setattr(old_value, "updateSourceQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "updateSourceQuery"):
                opp_val = getattr(value, "updateSourceQuery", None)
                setattr(value, "updateSourceQuery", self)

    @property
    def nestedQuery(self):
        return self.__nestedQuery

    @nestedQuery.setter
    def nestedQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__nestedQuery", None)
        self.__nestedQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryNested"):
                opp_val = getattr(old_value, "QueryNested", None)
                if opp_val == self:
                    setattr(old_value, "QueryNested", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryNested"):
                opp_val = getattr(value, "QueryNested", None)
                setattr(value, "QueryNested", self)

    @property
    def QueryExpressionBody372(self):
        return self.__QueryExpressionBody372

    @QueryExpressionBody372.setter
    def QueryExpressionBody372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__QueryExpressionBody372", None)
        self.__QueryExpressionBody372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sortSpecList"):
                opp_val = getattr(old_value, "sortSpecList", None)
                if opp_val == self:
                    setattr(old_value, "sortSpecList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sortSpecList"):
                opp_val = getattr(value, "sortSpecList", None)
                setattr(value, "sortSpecList", self)

    @property
    def queryExpr(self):
        return self.__queryExpr

    @queryExpr.setter
    def queryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__queryExpr", None)
        self.__queryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateExists"):
                opp_val = getattr(old_value, "PredicateExists", None)
                if opp_val == self:
                    setattr(old_value, "PredicateExists", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateExists"):
                opp_val = getattr(value, "PredicateExists", None)
                setattr(value, "PredicateExists", self)

    @property
    def withTableQueryExpr(self):
        return self.__withTableQueryExpr

    @withTableQueryExpr.setter
    def withTableQueryExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__withTableQueryExpr", None)
        self.__withTableQueryExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WithTableSpecification"):
                opp_val = getattr(old_value, "WithTableSpecification", None)
                if opp_val == self:
                    setattr(old_value, "WithTableSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WithTableSpecification"):
                opp_val = getattr(value, "WithTableSpecification", None)
                setattr(value, "WithTableSpecification", self)

    @property
    def QueryExpressionBody197(self):
        return self.__QueryExpressionBody197

    @QueryExpressionBody197.setter
    def QueryExpressionBody197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__QueryExpressionBody197", None)
        self.__QueryExpressionBody197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "combinedLeft196"):
                opp_val = getattr(old_value, "combinedLeft196", None)
                if opp_val == self:
                    setattr(old_value, "combinedLeft196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "combinedLeft196"):
                opp_val = getattr(value, "combinedLeft196", None)
                setattr(value, "combinedLeft196", self)

    @property
    def leftQuery(self):
        return self.__leftQuery

    @leftQuery.setter
    def leftQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__leftQuery", None)
        self.__leftQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryCombined"):
                opp_val = getattr(old_value, "QueryCombined", None)
                if opp_val == self:
                    setattr(old_value, "QueryCombined", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryCombined"):
                opp_val = getattr(value, "QueryCombined", None)
                setattr(value, "QueryCombined", self)

    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__query", None)
        self.__query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryExpressionRoot56"):
                opp_val = getattr(old_value, "QueryExpressionRoot56", None)
                if opp_val == self:
                    setattr(old_value, "QueryExpressionRoot56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryExpressionRoot56"):
                opp_val = getattr(value, "QueryExpressionRoot56", None)
                setattr(value, "QueryExpressionRoot56", self)

    @property
    def QueryExpressionBody200(self):
        return self.__QueryExpressionBody200

    @QueryExpressionBody200.setter
    def QueryExpressionBody200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__QueryExpressionBody200", None)
        self.__QueryExpressionBody200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "combinedRight199"):
                opp_val = getattr(old_value, "combinedRight199", None)
                if opp_val == self:
                    setattr(old_value, "combinedRight199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "combinedRight199"):
                opp_val = getattr(value, "combinedRight199", None)
                setattr(value, "combinedRight199", self)

    @property
    def query66(self):
        return self.__query66

    @query66.setter
    def query66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__query66", None)
        self.__query66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrderBySpecification67"):
                    opp_val = getattr(item, "OrderBySpecification67", None)
                    
                    if opp_val == self:
                        setattr(item, "OrderBySpecification67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrderBySpecification67"):
                    opp_val = getattr(item, "OrderBySpecification67", None)
                    
                    setattr(item, "OrderBySpecification67", self)
                    

    @property
    def QueryExpressionBody184(self):
        return self.__QueryExpressionBody184

    @QueryExpressionBody184.setter
    def QueryExpressionBody184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__QueryExpressionBody184", None)
        self.__QueryExpressionBody184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "withTableSpecification"):
                opp_val = getattr(old_value, "withTableSpecification", None)
                if opp_val == self:
                    setattr(old_value, "withTableSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "withTableSpecification"):
                opp_val = getattr(value, "withTableSpecification", None)
                setattr(value, "withTableSpecification", self)

    @property
    def query_QueryExpressionBody(self):
        return self.__query_QueryExpressionBody

    @query_QueryExpressionBody.setter
    def query_QueryExpressionBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__query_QueryExpressionBody", None)
        self.__query_QueryExpressionBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query_TableQueryLateral"):
                opp_val = getattr(old_value, "query_TableQueryLateral", None)
                if opp_val == self:
                    setattr(old_value, "query_TableQueryLateral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query_TableQueryLateral"):
                opp_val = getattr(value, "query_TableQueryLateral", None)
                setattr(value, "query_TableQueryLateral", self)

    @property
    def queryExpr62(self):
        return self.__queryExpr62

    @queryExpr62.setter
    def queryExpr62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__queryExpr62", None)
        self.__queryExpr62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UpdateSourceQuery"):
                opp_val = getattr(old_value, "UpdateSourceQuery", None)
                if opp_val == self:
                    setattr(old_value, "UpdateSourceQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UpdateSourceQuery"):
                opp_val = getattr(value, "UpdateSourceQuery", None)
                setattr(value, "UpdateSourceQuery", self)

    @property
    def QueryExpressionBody(self):
        return self.__QueryExpressionBody

    @QueryExpressionBody.setter
    def QueryExpressionBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__QueryExpressionBody", None)
        self.__QueryExpressionBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queryExpression"):
                opp_val = getattr(old_value, "queryExpression", None)
                if opp_val == self:
                    setattr(old_value, "queryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queryExpression"):
                opp_val = getattr(value, "queryExpression", None)
                setattr(value, "queryExpression", self)

    @property
    def QueryExpressionBody389(self):
        return self.__QueryExpressionBody389

    @QueryExpressionBody389.setter
    def QueryExpressionBody389(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryExpressionBody__QueryExpressionBody389", None)
        self.__QueryExpressionBody389 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queryNest"):
                opp_val = getattr(old_value, "queryNest", None)
                if opp_val == self:
                    setattr(old_value, "queryNest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queryNest"):
                opp_val = getattr(value, "queryNest", None)
                setattr(value, "queryNest", self)

class query_SearchConditionNested(QuerySearchCondition):

    pass
class query_QuerySelect(QueryExpressionBody):

    def __init__(self, distinct: bool, QuerySelect: "query_QuerySearchCondition" = None, QuerySelect50: "query_QuerySearchCondition" = None, QuerySelect163: "query_TableReference" = None, QuerySelect214: "query_GroupingSpecification" = None, querySelectHaving: "query_QuerySearchCondition" = None, querySelectWhere: "query_QuerySearchCondition" = None, querySelect: set["query_GroupingSpecification"] = None, querySelect207: set["query_QueryResultSpecification"] = None, querySelect209: set["query_TableReference"] = None, querySelect212: set["query_ValueExpressionVariable"] = None, QuerySelect216: "query_QueryResultSpecification" = None, QuerySelect275: "query_ValueExpressionVariable" = None):
        self.distinct = distinct
        self.QuerySelect = QuerySelect
        self.QuerySelect50 = QuerySelect50
        self.QuerySelect163 = QuerySelect163
        self.QuerySelect214 = QuerySelect214
        self.querySelectHaving = querySelectHaving
        self.querySelectWhere = querySelectWhere
        self.querySelect = querySelect if querySelect is not None else set()
        self.querySelect207 = querySelect207 if querySelect207 is not None else set()
        self.querySelect209 = querySelect209 if querySelect209 is not None else set()
        self.querySelect212 = querySelect212 if querySelect212 is not None else set()
        self.QuerySelect216 = QuerySelect216
        self.QuerySelect275 = QuerySelect275
        
        pass
    @property
    def distinct(self):
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct


    @property
    def QuerySelect216(self):
        return self.__QuerySelect216

    @QuerySelect216.setter
    def QuerySelect216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__QuerySelect216", None)
        self.__QuerySelect216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selectClause"):
                opp_val = getattr(old_value, "selectClause", None)
                if opp_val == self:
                    setattr(old_value, "selectClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selectClause"):
                opp_val = getattr(value, "selectClause", None)
                setattr(value, "selectClause", self)

    @property
    def QuerySelect163(self):
        return self.__QuerySelect163

    @QuerySelect163.setter
    def QuerySelect163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__QuerySelect163", None)
        self.__QuerySelect163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromClause"):
                opp_val = getattr(old_value, "fromClause", None)
                if opp_val == self:
                    setattr(old_value, "fromClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromClause"):
                opp_val = getattr(value, "fromClause", None)
                setattr(value, "fromClause", self)

    @property
    def querySelect212(self):
        return self.__querySelect212

    @querySelect212.setter
    def querySelect212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__querySelect212", None)
        self.__querySelect212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ValueExpressionVariable"):
                    opp_val = getattr(item, "ValueExpressionVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "ValueExpressionVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ValueExpressionVariable"):
                    opp_val = getattr(item, "ValueExpressionVariable", None)
                    
                    setattr(item, "ValueExpressionVariable", self)
                    

    @property
    def querySelectWhere(self):
        return self.__querySelectWhere

    @querySelectWhere.setter
    def querySelectWhere(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__querySelectWhere", None)
        self.__querySelectWhere = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySearchCondition204"):
                opp_val = getattr(old_value, "QuerySearchCondition204", None)
                if opp_val == self:
                    setattr(old_value, "QuerySearchCondition204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySearchCondition204"):
                opp_val = getattr(value, "QuerySearchCondition204", None)
                setattr(value, "QuerySearchCondition204", self)

    @property
    def querySelect(self):
        return self.__querySelect

    @querySelect.setter
    def querySelect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__querySelect", None)
        self.__querySelect = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GroupingSpecification"):
                    opp_val = getattr(item, "GroupingSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "GroupingSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GroupingSpecification"):
                    opp_val = getattr(item, "GroupingSpecification", None)
                    
                    setattr(item, "GroupingSpecification", self)
                    

    @property
    def querySelect209(self):
        return self.__querySelect209

    @querySelect209.setter
    def querySelect209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__querySelect209", None)
        self.__querySelect209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TableReference210"):
                    opp_val = getattr(item, "TableReference210", None)
                    
                    if opp_val == self:
                        setattr(item, "TableReference210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TableReference210"):
                    opp_val = getattr(item, "TableReference210", None)
                    
                    setattr(item, "TableReference210", self)
                    

    @property
    def querySelectHaving(self):
        return self.__querySelectHaving

    @querySelectHaving.setter
    def querySelectHaving(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__querySelectHaving", None)
        self.__querySelectHaving = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySearchCondition202"):
                opp_val = getattr(old_value, "QuerySearchCondition202", None)
                if opp_val == self:
                    setattr(old_value, "QuerySearchCondition202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySearchCondition202"):
                opp_val = getattr(value, "QuerySearchCondition202", None)
                setattr(value, "QuerySearchCondition202", self)

    @property
    def querySelect207(self):
        return self.__querySelect207

    @querySelect207.setter
    def querySelect207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__querySelect207", None)
        self.__querySelect207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "QueryResultSpecification"):
                    opp_val = getattr(item, "QueryResultSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "QueryResultSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "QueryResultSpecification"):
                    opp_val = getattr(item, "QueryResultSpecification", None)
                    
                    setattr(item, "QueryResultSpecification", self)
                    

    @property
    def QuerySelect214(self):
        return self.__QuerySelect214

    @QuerySelect214.setter
    def QuerySelect214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__QuerySelect214", None)
        self.__QuerySelect214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupByClause"):
                opp_val = getattr(old_value, "groupByClause", None)
                if opp_val == self:
                    setattr(old_value, "groupByClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupByClause"):
                opp_val = getattr(value, "groupByClause", None)
                setattr(value, "groupByClause", self)

    @property
    def QuerySelect(self):
        return self.__QuerySelect

    @QuerySelect.setter
    def QuerySelect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__QuerySelect", None)
        self.__QuerySelect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "havingClause"):
                opp_val = getattr(old_value, "havingClause", None)
                if opp_val == self:
                    setattr(old_value, "havingClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "havingClause"):
                opp_val = getattr(value, "havingClause", None)
                setattr(value, "havingClause", self)

    @property
    def QuerySelect275(self):
        return self.__QuerySelect275

    @QuerySelect275.setter
    def QuerySelect275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__QuerySelect275", None)
        self.__QuerySelect275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "intoClause"):
                opp_val = getattr(old_value, "intoClause", None)
                if opp_val == self:
                    setattr(old_value, "intoClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "intoClause"):
                opp_val = getattr(value, "intoClause", None)
                setattr(value, "intoClause", self)

    @property
    def QuerySelect50(self):
        return self.__QuerySelect50

    @QuerySelect50.setter
    def QuerySelect50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySelect__QuerySelect50", None)
        self.__QuerySelect50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "whereClause49"):
                opp_val = getattr(old_value, "whereClause49", None)
                if opp_val == self:
                    setattr(old_value, "whereClause49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "whereClause49"):
                opp_val = getattr(value, "whereClause49", None)
                setattr(value, "whereClause49", self)

class query_QueryCombined(QueryExpressionBody):

    def __init__(self, combinedOperator: str, QueryCombined: "query_QueryExpressionBody" = None, QueryCombined59: "query_QueryExpressionBody" = None, combinedLeft196: "query_QueryExpressionBody" = None, combinedRight199: "query_QueryExpressionBody" = None):
        self.combinedOperator = combinedOperator
        self.QueryCombined = QueryCombined
        self.QueryCombined59 = QueryCombined59
        self.combinedLeft196 = combinedLeft196
        self.combinedRight199 = combinedRight199
        
        pass
    @property
    def combinedOperator(self):
        return self.__combinedOperator

    @combinedOperator.setter
    def combinedOperator(self, combinedOperator: str):
        self.__combinedOperator = combinedOperator


    @property
    def QueryCombined(self):
        return self.__QueryCombined

    @QueryCombined.setter
    def QueryCombined(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryCombined__QueryCombined", None)
        self.__QueryCombined = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leftQuery"):
                opp_val = getattr(old_value, "leftQuery", None)
                if opp_val == self:
                    setattr(old_value, "leftQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leftQuery"):
                opp_val = getattr(value, "leftQuery", None)
                setattr(value, "leftQuery", self)

    @property
    def QueryCombined59(self):
        return self.__QueryCombined59

    @QueryCombined59.setter
    def QueryCombined59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryCombined__QueryCombined59", None)
        self.__QueryCombined59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rightQuery"):
                opp_val = getattr(old_value, "rightQuery", None)
                if opp_val == self:
                    setattr(old_value, "rightQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rightQuery"):
                opp_val = getattr(value, "rightQuery", None)
                setattr(value, "rightQuery", self)

    @property
    def combinedRight199(self):
        return self.__combinedRight199

    @combinedRight199.setter
    def combinedRight199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryCombined__combinedRight199", None)
        self.__combinedRight199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryExpressionBody200"):
                opp_val = getattr(old_value, "QueryExpressionBody200", None)
                if opp_val == self:
                    setattr(old_value, "QueryExpressionBody200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryExpressionBody200"):
                opp_val = getattr(value, "QueryExpressionBody200", None)
                setattr(value, "QueryExpressionBody200", self)

    @property
    def combinedLeft196(self):
        return self.__combinedLeft196

    @combinedLeft196.setter
    def combinedLeft196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryCombined__combinedLeft196", None)
        self.__combinedLeft196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryExpressionBody197"):
                opp_val = getattr(old_value, "QueryExpressionBody197", None)
                if opp_val == self:
                    setattr(old_value, "QueryExpressionBody197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryExpressionBody197"):
                opp_val = getattr(value, "QueryExpressionBody197", None)
                setattr(value, "QueryExpressionBody197", self)

class query_SearchConditionCombined(QuerySearchCondition):

    def __init__(self, combinedOperator: str, SearchConditionCombined46: "query_QuerySearchCondition" = None, SearchConditionCombined: "query_QuerySearchCondition" = None, combinedLeft: "query_QuerySearchCondition" = None, combinedRight: "query_QuerySearchCondition" = None):
        self.combinedOperator = combinedOperator
        self.SearchConditionCombined46 = SearchConditionCombined46
        self.SearchConditionCombined = SearchConditionCombined
        self.combinedLeft = combinedLeft
        self.combinedRight = combinedRight
        
        pass
    @property
    def combinedOperator(self):
        return self.__combinedOperator

    @combinedOperator.setter
    def combinedOperator(self, combinedOperator: str):
        self.__combinedOperator = combinedOperator


    @property
    def combinedLeft(self):
        return self.__combinedLeft

    @combinedLeft.setter
    def combinedLeft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_SearchConditionCombined__combinedLeft", None)
        self.__combinedLeft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySearchCondition190"):
                opp_val = getattr(old_value, "QuerySearchCondition190", None)
                if opp_val == self:
                    setattr(old_value, "QuerySearchCondition190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySearchCondition190"):
                opp_val = getattr(value, "QuerySearchCondition190", None)
                setattr(value, "QuerySearchCondition190", self)

    @property
    def SearchConditionCombined(self):
        return self.__SearchConditionCombined

    @SearchConditionCombined.setter
    def SearchConditionCombined(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_SearchConditionCombined__SearchConditionCombined", None)
        self.__SearchConditionCombined = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leftCondition"):
                opp_val = getattr(old_value, "leftCondition", None)
                if opp_val == self:
                    setattr(old_value, "leftCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leftCondition"):
                opp_val = getattr(value, "leftCondition", None)
                setattr(value, "leftCondition", self)

    @property
    def SearchConditionCombined46(self):
        return self.__SearchConditionCombined46

    @SearchConditionCombined46.setter
    def SearchConditionCombined46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_SearchConditionCombined__SearchConditionCombined46", None)
        self.__SearchConditionCombined46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rightCondition"):
                opp_val = getattr(old_value, "rightCondition", None)
                if opp_val == self:
                    setattr(old_value, "rightCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rightCondition"):
                opp_val = getattr(value, "rightCondition", None)
                setattr(value, "rightCondition", self)

    @property
    def combinedRight(self):
        return self.__combinedRight

    @combinedRight.setter
    def combinedRight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_SearchConditionCombined__combinedRight", None)
        self.__combinedRight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySearchCondition192"):
                opp_val = getattr(old_value, "QuerySearchCondition192", None)
                if opp_val == self:
                    setattr(old_value, "QuerySearchCondition192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySearchCondition192"):
                opp_val = getattr(value, "QuerySearchCondition192", None)
                setattr(value, "QuerySearchCondition192", self)

class query_TableJoined(TableReference):

    def __init__(self, joinOperator: str, TableJoined: "query_QuerySearchCondition" = None, tableJoined: "query_QuerySearchCondition" = None, tableJoinedRight: "query_TableReference" = None, tableJoinedLeft: "query_TableReference" = None, TableJoined159: "query_TableReference" = None, TableJoined161: "query_TableReference" = None):
        self.joinOperator = joinOperator
        self.TableJoined = TableJoined
        self.tableJoined = tableJoined
        self.tableJoinedRight = tableJoinedRight
        self.tableJoinedLeft = tableJoinedLeft
        self.TableJoined159 = TableJoined159
        self.TableJoined161 = TableJoined161
        
        pass
    @property
    def joinOperator(self):
        return self.__joinOperator

    @joinOperator.setter
    def joinOperator(self, joinOperator: str):
        self.__joinOperator = joinOperator


    @property
    def TableJoined159(self):
        return self.__TableJoined159

    @TableJoined159.setter
    def TableJoined159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_TableJoined__TableJoined159", None)
        self.__TableJoined159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableRefRight"):
                opp_val = getattr(old_value, "tableRefRight", None)
                if opp_val == self:
                    setattr(old_value, "tableRefRight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableRefRight"):
                opp_val = getattr(value, "tableRefRight", None)
                setattr(value, "tableRefRight", self)

    @property
    def TableJoined(self):
        return self.__TableJoined

    @TableJoined.setter
    def TableJoined(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_TableJoined__TableJoined", None)
        self.__TableJoined = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "joinCondition"):
                opp_val = getattr(old_value, "joinCondition", None)
                if opp_val == self:
                    setattr(old_value, "joinCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "joinCondition"):
                opp_val = getattr(value, "joinCondition", None)
                setattr(value, "joinCondition", self)

    @property
    def tableJoined(self):
        return self.__tableJoined

    @tableJoined.setter
    def tableJoined(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_TableJoined__tableJoined", None)
        self.__tableJoined = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySearchCondition177"):
                opp_val = getattr(old_value, "QuerySearchCondition177", None)
                if opp_val == self:
                    setattr(old_value, "QuerySearchCondition177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySearchCondition177"):
                opp_val = getattr(value, "QuerySearchCondition177", None)
                setattr(value, "QuerySearchCondition177", self)

    @property
    def tableJoinedRight(self):
        return self.__tableJoinedRight

    @tableJoinedRight.setter
    def tableJoinedRight(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_TableJoined__tableJoinedRight", None)
        self.__tableJoinedRight = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableReference"):
                opp_val = getattr(old_value, "TableReference", None)
                if opp_val == self:
                    setattr(old_value, "TableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableReference"):
                opp_val = getattr(value, "TableReference", None)
                setattr(value, "TableReference", self)

    @property
    def TableJoined161(self):
        return self.__TableJoined161

    @TableJoined161.setter
    def TableJoined161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_TableJoined__TableJoined161", None)
        self.__TableJoined161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableRefLeft"):
                opp_val = getattr(old_value, "tableRefLeft", None)
                if opp_val == self:
                    setattr(old_value, "tableRefLeft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableRefLeft"):
                opp_val = getattr(value, "tableRefLeft", None)
                setattr(value, "tableRefLeft", self)

    @property
    def tableJoinedLeft(self):
        return self.__tableJoinedLeft

    @tableJoinedLeft.setter
    def tableJoinedLeft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_TableJoined__tableJoinedLeft", None)
        self.__tableJoinedLeft = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableReference180"):
                opp_val = getattr(old_value, "TableReference180", None)
                if opp_val == self:
                    setattr(old_value, "TableReference180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableReference180"):
                opp_val = getattr(value, "TableReference180", None)
                setattr(value, "TableReference180", self)

class expressions_SearchCondition:

    pass
class query_MergeUpdateSpecification(MergeOperationSpecification):

    pass
class QueryStatement:

    pass
class query_QueryChangeStatement(QueryStatement, statements_SQLDataChangeStatement):

    pass
class query_QuerySelectStatement(QueryStatement):

    pass
class query_ValueExpressionColumn(ValueExpressionAtomic):

    pass
class query_TableInDatabase(TableExpression):

    pass
class statements_SQLDataStatement:

    pass
class SQLQueryObject:

    pass
class query_CallStatement(SQLQueryObject, statements_SQLControlStatement):

    pass
class query_ColumnName(SQLQueryObject):

    pass
class query_GroupingSetsElement(SQLQueryObject):

    pass
class query_UpdatabilityExpression(SQLQueryObject):

    def __init__(self, updatabilityType: str, UpdatabilityExpression: "query_QuerySelectStatement" = None, updatabilityExpr: set["query_UpdateOfColumn"] = None, UpdatabilityExpression413: "query_UpdateOfColumn" = None, updatabilityExpr416: "query_QuerySelectStatement" = None):
        self.updatabilityType = updatabilityType
        self.UpdatabilityExpression = UpdatabilityExpression
        self.updatabilityExpr = updatabilityExpr if updatabilityExpr is not None else set()
        self.UpdatabilityExpression413 = UpdatabilityExpression413
        self.updatabilityExpr416 = updatabilityExpr416
        
        pass
    @property
    def updatabilityType(self):
        return self.__updatabilityType

    @updatabilityType.setter
    def updatabilityType(self, updatabilityType: str):
        self.__updatabilityType = updatabilityType


    @property
    def UpdatabilityExpression413(self):
        return self.__UpdatabilityExpression413

    @UpdatabilityExpression413.setter
    def UpdatabilityExpression413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_UpdatabilityExpression__UpdatabilityExpression413", None)
        self.__UpdatabilityExpression413 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "updateOfColumnList"):
                opp_val = getattr(old_value, "updateOfColumnList", None)
                if opp_val == self:
                    setattr(old_value, "updateOfColumnList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "updateOfColumnList"):
                opp_val = getattr(value, "updateOfColumnList", None)
                setattr(value, "updateOfColumnList", self)

    @property
    def updatabilityExpr(self):
        return self.__updatabilityExpr

    @updatabilityExpr.setter
    def updatabilityExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_UpdatabilityExpression__updatabilityExpr", None)
        self.__updatabilityExpr = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UpdateOfColumn"):
                    opp_val = getattr(item, "UpdateOfColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "UpdateOfColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UpdateOfColumn"):
                    opp_val = getattr(item, "UpdateOfColumn", None)
                    
                    setattr(item, "UpdateOfColumn", self)
                    

    @property
    def updatabilityExpr416(self):
        return self.__updatabilityExpr416

    @updatabilityExpr416.setter
    def updatabilityExpr416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_UpdatabilityExpression__updatabilityExpr416", None)
        self.__updatabilityExpr416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySelectStatement417"):
                opp_val = getattr(old_value, "QuerySelectStatement417", None)
                if opp_val == self:
                    setattr(old_value, "QuerySelectStatement417", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySelectStatement417"):
                opp_val = getattr(value, "QuerySelectStatement417", None)
                setattr(value, "QuerySelectStatement417", self)

    @property
    def UpdatabilityExpression(self):
        return self.__UpdatabilityExpression

    @UpdatabilityExpression.setter
    def UpdatabilityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_UpdatabilityExpression__UpdatabilityExpression", None)
        self.__UpdatabilityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selectStatement18"):
                opp_val = getattr(old_value, "selectStatement18", None)
                if opp_val == self:
                    setattr(old_value, "selectStatement18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selectStatement18"):
                opp_val = getattr(value, "selectStatement18", None)
                setattr(value, "selectStatement18", self)

class query_TableReference(SQLQueryObject):

    pass
class query_ProcedureReference(SQLQueryObject):

    pass
class query_MergeOperationSpecification(SQLQueryObject):

    pass
class query_ValueExpressionCaseSimpleContent(SQLQueryObject):

    pass
class query_QuerySearchCondition(expressions_SearchCondition, SQLQueryObject):

    def __init__(self, negatedCondition: bool, QuerySearchCondition25: "query_QueryUpdateStatement" = None, rightCondition: "query_SearchConditionCombined" = None, whereClause: "query_QueryUpdateStatement" = None, whereClause41: "query_QueryDeleteStatement" = None, joinCondition: "query_TableJoined" = None, leftCondition: "query_SearchConditionCombined" = None, havingClause: "query_QuerySelect" = None, whereClause49: "query_QuerySelect" = None, searchCondition: "query_ValueExpressionCaseSearchContent" = None, nestedCondition: "query_SearchConditionNested" = None, searchCondition54: "query_MergeOnCondition" = None, QuerySearchCondition: "query_QueryDeleteStatement" = None, QuerySearchCondition177: "query_TableJoined" = None, QuerySearchCondition190: "query_SearchConditionCombined" = None, QuerySearchCondition192: "query_SearchConditionCombined" = None, QuerySearchCondition202: "query_QuerySelect" = None, QuerySearchCondition204: "query_QuerySelect" = None, QuerySearchCondition323: "query_ValueExpressionCaseSearchContent" = None, QuerySearchCondition365: "query_SearchConditionNested" = None, QuerySearchCondition404: "query_MergeOnCondition" = None):
        self.negatedCondition = negatedCondition
        self.QuerySearchCondition25 = QuerySearchCondition25
        self.rightCondition = rightCondition
        self.whereClause = whereClause
        self.whereClause41 = whereClause41
        self.joinCondition = joinCondition
        self.leftCondition = leftCondition
        self.havingClause = havingClause
        self.whereClause49 = whereClause49
        self.searchCondition = searchCondition
        self.nestedCondition = nestedCondition
        self.searchCondition54 = searchCondition54
        self.QuerySearchCondition = QuerySearchCondition
        self.QuerySearchCondition177 = QuerySearchCondition177
        self.QuerySearchCondition190 = QuerySearchCondition190
        self.QuerySearchCondition192 = QuerySearchCondition192
        self.QuerySearchCondition202 = QuerySearchCondition202
        self.QuerySearchCondition204 = QuerySearchCondition204
        self.QuerySearchCondition323 = QuerySearchCondition323
        self.QuerySearchCondition365 = QuerySearchCondition365
        self.QuerySearchCondition404 = QuerySearchCondition404
        
        pass
    @property
    def negatedCondition(self):
        return self.__negatedCondition

    @negatedCondition.setter
    def negatedCondition(self, negatedCondition: bool):
        self.__negatedCondition = negatedCondition


    @property
    def QuerySearchCondition25(self):
        return self.__QuerySearchCondition25

    @QuerySearchCondition25.setter
    def QuerySearchCondition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition25", None)
        self.__QuerySearchCondition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "updateStatement24"):
                opp_val = getattr(old_value, "updateStatement24", None)
                if opp_val == self:
                    setattr(old_value, "updateStatement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "updateStatement24"):
                opp_val = getattr(value, "updateStatement24", None)
                setattr(value, "updateStatement24", self)

    @property
    def joinCondition(self):
        return self.__joinCondition

    @joinCondition.setter
    def joinCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__joinCondition", None)
        self.__joinCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableJoined"):
                opp_val = getattr(old_value, "TableJoined", None)
                if opp_val == self:
                    setattr(old_value, "TableJoined", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableJoined"):
                opp_val = getattr(value, "TableJoined", None)
                setattr(value, "TableJoined", self)

    @property
    def QuerySearchCondition204(self):
        return self.__QuerySearchCondition204

    @QuerySearchCondition204.setter
    def QuerySearchCondition204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition204", None)
        self.__QuerySearchCondition204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "querySelectWhere"):
                opp_val = getattr(old_value, "querySelectWhere", None)
                if opp_val == self:
                    setattr(old_value, "querySelectWhere", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "querySelectWhere"):
                opp_val = getattr(value, "querySelectWhere", None)
                setattr(value, "querySelectWhere", self)

    @property
    def QuerySearchCondition404(self):
        return self.__QuerySearchCondition404

    @QuerySearchCondition404.setter
    def QuerySearchCondition404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition404", None)
        self.__QuerySearchCondition404 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mergeOnCondition"):
                opp_val = getattr(old_value, "mergeOnCondition", None)
                if opp_val == self:
                    setattr(old_value, "mergeOnCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mergeOnCondition"):
                opp_val = getattr(value, "mergeOnCondition", None)
                setattr(value, "mergeOnCondition", self)

    @property
    def nestedCondition(self):
        return self.__nestedCondition

    @nestedCondition.setter
    def nestedCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__nestedCondition", None)
        self.__nestedCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SearchConditionNested"):
                opp_val = getattr(old_value, "SearchConditionNested", None)
                if opp_val == self:
                    setattr(old_value, "SearchConditionNested", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SearchConditionNested"):
                opp_val = getattr(value, "SearchConditionNested", None)
                setattr(value, "SearchConditionNested", self)

    @property
    def QuerySearchCondition192(self):
        return self.__QuerySearchCondition192

    @QuerySearchCondition192.setter
    def QuerySearchCondition192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition192", None)
        self.__QuerySearchCondition192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "combinedRight"):
                opp_val = getattr(old_value, "combinedRight", None)
                if opp_val == self:
                    setattr(old_value, "combinedRight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "combinedRight"):
                opp_val = getattr(value, "combinedRight", None)
                setattr(value, "combinedRight", self)

    @property
    def QuerySearchCondition(self):
        return self.__QuerySearchCondition

    @QuerySearchCondition.setter
    def QuerySearchCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition", None)
        self.__QuerySearchCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deleteStatement2"):
                opp_val = getattr(old_value, "deleteStatement2", None)
                if opp_val == self:
                    setattr(old_value, "deleteStatement2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deleteStatement2"):
                opp_val = getattr(value, "deleteStatement2", None)
                setattr(value, "deleteStatement2", self)

    @property
    def rightCondition(self):
        return self.__rightCondition

    @rightCondition.setter
    def rightCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__rightCondition", None)
        self.__rightCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SearchConditionCombined46"):
                opp_val = getattr(old_value, "SearchConditionCombined46", None)
                if opp_val == self:
                    setattr(old_value, "SearchConditionCombined46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SearchConditionCombined46"):
                opp_val = getattr(value, "SearchConditionCombined46", None)
                setattr(value, "SearchConditionCombined46", self)

    @property
    def QuerySearchCondition177(self):
        return self.__QuerySearchCondition177

    @QuerySearchCondition177.setter
    def QuerySearchCondition177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition177", None)
        self.__QuerySearchCondition177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableJoined"):
                opp_val = getattr(old_value, "tableJoined", None)
                if opp_val == self:
                    setattr(old_value, "tableJoined", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableJoined"):
                opp_val = getattr(value, "tableJoined", None)
                setattr(value, "tableJoined", self)

    @property
    def QuerySearchCondition190(self):
        return self.__QuerySearchCondition190

    @QuerySearchCondition190.setter
    def QuerySearchCondition190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition190", None)
        self.__QuerySearchCondition190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "combinedLeft"):
                opp_val = getattr(old_value, "combinedLeft", None)
                if opp_val == self:
                    setattr(old_value, "combinedLeft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "combinedLeft"):
                opp_val = getattr(value, "combinedLeft", None)
                setattr(value, "combinedLeft", self)

    @property
    def whereClause49(self):
        return self.__whereClause49

    @whereClause49.setter
    def whereClause49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__whereClause49", None)
        self.__whereClause49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySelect50"):
                opp_val = getattr(old_value, "QuerySelect50", None)
                if opp_val == self:
                    setattr(old_value, "QuerySelect50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySelect50"):
                opp_val = getattr(value, "QuerySelect50", None)
                setattr(value, "QuerySelect50", self)

    @property
    def QuerySearchCondition365(self):
        return self.__QuerySearchCondition365

    @QuerySearchCondition365.setter
    def QuerySearchCondition365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition365", None)
        self.__QuerySearchCondition365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nest364"):
                opp_val = getattr(old_value, "nest364", None)
                if opp_val == self:
                    setattr(old_value, "nest364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nest364"):
                opp_val = getattr(value, "nest364", None)
                setattr(value, "nest364", self)

    @property
    def havingClause(self):
        return self.__havingClause

    @havingClause.setter
    def havingClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__havingClause", None)
        self.__havingClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySelect"):
                opp_val = getattr(old_value, "QuerySelect", None)
                if opp_val == self:
                    setattr(old_value, "QuerySelect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySelect"):
                opp_val = getattr(value, "QuerySelect", None)
                setattr(value, "QuerySelect", self)

    @property
    def searchCondition54(self):
        return self.__searchCondition54

    @searchCondition54.setter
    def searchCondition54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__searchCondition54", None)
        self.__searchCondition54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MergeOnCondition"):
                opp_val = getattr(old_value, "MergeOnCondition", None)
                if opp_val == self:
                    setattr(old_value, "MergeOnCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MergeOnCondition"):
                opp_val = getattr(value, "MergeOnCondition", None)
                setattr(value, "MergeOnCondition", self)

    @property
    def QuerySearchCondition323(self):
        return self.__QuerySearchCondition323

    @QuerySearchCondition323.setter
    def QuerySearchCondition323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition323", None)
        self.__QuerySearchCondition323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCaseSearchContent322"):
                opp_val = getattr(old_value, "valueExprCaseSearchContent322", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCaseSearchContent322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCaseSearchContent322"):
                opp_val = getattr(value, "valueExprCaseSearchContent322", None)
                setattr(value, "valueExprCaseSearchContent322", self)

    @property
    def searchCondition(self):
        return self.__searchCondition

    @searchCondition.setter
    def searchCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__searchCondition", None)
        self.__searchCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCaseSearchContent"):
                opp_val = getattr(old_value, "ValueExpressionCaseSearchContent", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCaseSearchContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCaseSearchContent"):
                opp_val = getattr(value, "ValueExpressionCaseSearchContent", None)
                setattr(value, "ValueExpressionCaseSearchContent", self)

    @property
    def leftCondition(self):
        return self.__leftCondition

    @leftCondition.setter
    def leftCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__leftCondition", None)
        self.__leftCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SearchConditionCombined"):
                opp_val = getattr(old_value, "SearchConditionCombined", None)
                if opp_val == self:
                    setattr(old_value, "SearchConditionCombined", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SearchConditionCombined"):
                opp_val = getattr(value, "SearchConditionCombined", None)
                setattr(value, "SearchConditionCombined", self)

    @property
    def whereClause41(self):
        return self.__whereClause41

    @whereClause41.setter
    def whereClause41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__whereClause41", None)
        self.__whereClause41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryDeleteStatement42"):
                opp_val = getattr(old_value, "QueryDeleteStatement42", None)
                if opp_val == self:
                    setattr(old_value, "QueryDeleteStatement42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryDeleteStatement42"):
                opp_val = getattr(value, "QueryDeleteStatement42", None)
                setattr(value, "QueryDeleteStatement42", self)

    @property
    def whereClause(self):
        return self.__whereClause

    @whereClause.setter
    def whereClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__whereClause", None)
        self.__whereClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryUpdateStatement39"):
                opp_val = getattr(old_value, "QueryUpdateStatement39", None)
                if opp_val == self:
                    setattr(old_value, "QueryUpdateStatement39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryUpdateStatement39"):
                opp_val = getattr(value, "QueryUpdateStatement39", None)
                setattr(value, "QueryUpdateStatement39", self)

    @property
    def QuerySearchCondition202(self):
        return self.__QuerySearchCondition202

    @QuerySearchCondition202.setter
    def QuerySearchCondition202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QuerySearchCondition__QuerySearchCondition202", None)
        self.__QuerySearchCondition202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "querySelectHaving"):
                opp_val = getattr(old_value, "querySelectHaving", None)
                if opp_val == self:
                    setattr(old_value, "querySelectHaving", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "querySelectHaving"):
                opp_val = getattr(value, "querySelectHaving", None)
                setattr(value, "querySelectHaving", self)

class query_UpdateSource(SQLQueryObject):

    pass
class query_OrderBySpecification(SQLQueryObject):

    def __init__(self, OrderingSpecOption: str, NullOrderingOption: str, descending: bool, OrderBySpecification: "query_QuerySelectStatement" = None, OrderBySpecification67: "query_QueryExpressionBody" = None, orderByClause: "query_QuerySelectStatement" = None, sortSpecList: "query_QueryExpressionBody" = None):
        self.OrderingSpecOption = OrderingSpecOption
        self.NullOrderingOption = NullOrderingOption
        self.descending = descending
        self.OrderBySpecification = OrderBySpecification
        self.OrderBySpecification67 = OrderBySpecification67
        self.orderByClause = orderByClause
        self.sortSpecList = sortSpecList
        
        pass
    @property
    def OrderingSpecOption(self):
        return self.__OrderingSpecOption

    @OrderingSpecOption.setter
    def OrderingSpecOption(self, OrderingSpecOption: str):
        self.__OrderingSpecOption = OrderingSpecOption


    @property
    def descending(self):
        return self.__descending

    @descending.setter
    def descending(self, descending: bool):
        self.__descending = descending


    @property
    def NullOrderingOption(self):
        return self.__NullOrderingOption

    @NullOrderingOption.setter
    def NullOrderingOption(self, NullOrderingOption: str):
        self.__NullOrderingOption = NullOrderingOption


    @property
    def OrderBySpecification67(self):
        return self.__OrderBySpecification67

    @OrderBySpecification67.setter
    def OrderBySpecification67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_OrderBySpecification__OrderBySpecification67", None)
        self.__OrderBySpecification67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "query66"):
                opp_val = getattr(old_value, "query66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "query66"):
                opp_val = getattr(value, "query66", None)
                if opp_val is None:
                    setattr(value, "query66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def orderByClause(self):
        return self.__orderByClause

    @orderByClause.setter
    def orderByClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_OrderBySpecification__orderByClause", None)
        self.__orderByClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QuerySelectStatement370"):
                opp_val = getattr(old_value, "QuerySelectStatement370", None)
                if opp_val == self:
                    setattr(old_value, "QuerySelectStatement370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QuerySelectStatement370"):
                opp_val = getattr(value, "QuerySelectStatement370", None)
                setattr(value, "QuerySelectStatement370", self)

    @property
    def sortSpecList(self):
        return self.__sortSpecList

    @sortSpecList.setter
    def sortSpecList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_OrderBySpecification__sortSpecList", None)
        self.__sortSpecList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryExpressionBody372"):
                opp_val = getattr(old_value, "QueryExpressionBody372", None)
                if opp_val == self:
                    setattr(old_value, "QueryExpressionBody372", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryExpressionBody372"):
                opp_val = getattr(value, "QueryExpressionBody372", None)
                setattr(value, "QueryExpressionBody372", self)

    @property
    def OrderBySpecification(self):
        return self.__OrderBySpecification

    @OrderBySpecification.setter
    def OrderBySpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_OrderBySpecification__OrderBySpecification", None)
        self.__OrderBySpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selectStatement16"):
                opp_val = getattr(old_value, "selectStatement16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selectStatement16"):
                opp_val = getattr(value, "selectStatement16", None)
                if opp_val is None:
                    setattr(value, "selectStatement16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class query_QueryValueExpression(SQLQueryObject, expressions_ValueExpression):

    def __init__(self, unaryOperator: str, valueExpr113: "query_ValueExpressionCaseSimple" = None, whenValueExpr: "query_ValueExpressionCaseSimpleContent" = None, resultValueExpr: "query_ValueExpressionCaseSimpleContent" = None, valueExpr118: "query_ValueExpressionCaseSearchContent" = None, escapeValueExpr: "query_PredicateLike" = None, nestedValueExpr: "query_ValueExpressionNested" = None, valueExprList126: "query_UpdateSourceExprList" = None, parameterList128: "query_TableFunction" = None, matchingValueExpr: "query_PredicateLike" = None, query_QueryValueExpression: "DataType" = None, exprList: "query_ValuesRow" = None, valueExpr: "query_OrderByValueExpression" = None, valueExpr73: "query_ResultColumn" = None, rightValueExpr: "query_PredicateBasic" = None, leftValueExpr: "query_PredicateBasic" = None, patternValueExpr: "query_PredicateLike" = None, leftValueExpr95: "query_PredicateBetween" = None, valueExpr81: "query_PredicateIsNull" = None, valueExprList: "query_PredicateInValueList" = None, valueExpr84: "query_PredicateInValueList" = None, valueExprList87: "query_PredicateInValueRowSelect" = None, valueExpr89: "query_PredicateInValueSelect" = None, valueExprList91: "query_PredicateQuantifiedRowSelect" = None, valueExpr93: "query_PredicateQuantifiedValueSelect" = None, valueExpr109: "query_GroupingExpression" = None, rightValueExpr1: "query_PredicateBetween" = None, rightValueExpr2: "query_PredicateBetween" = None, valueExpr101: "query_ValueExpressionCast" = None, parameterList: "query_ValueExpressionFunction" = None, leftValueExpr104: "query_ValueExpressionCombined" = None, rightValueExpr106: "query_ValueExpressionCombined" = None, valueExpr123: "query_ValueExpressionLabeledDuration" = None, valueExpr111: "query_ValueExpressionCaseElse" = None, valueExprList130: "query_ValueExpressionRow" = None, argumentList: "query_CallStatement" = None, QueryValueExpression: "query_ValuesRow" = None, QueryValueExpression226: "query_PredicateBetween" = None, QueryValueExpression228: "query_PredicateBetween" = None, QueryValueExpression230: "query_PredicateBetween" = None, QueryValueExpression234: "query_PredicateLike" = None, QueryValueExpression236: "query_PredicateLike" = None, QueryValueExpression238: "query_PredicateLike" = None, QueryValueExpression248: "query_PredicateQuantifiedRowSelect" = None, QueryValueExpression240: "query_PredicateIsNull" = None, QueryValueExpression244: "query_PredicateQuantifiedValueSelect" = None, QueryValueExpression194: "query_OrderByValueExpression" = None, QueryValueExpression222: "query_PredicateBasic" = None, QueryValueExpression219: "query_ResultColumn" = None, QueryValueExpression224: "query_PredicateBasic" = None, QueryValueExpression285: "query_ValueExpressionFunction" = None, QueryValueExpression290: "query_ValueExpressionCombined" = None, QueryValueExpression300: "query_GroupingExpression" = None, QueryValueExpression318: "query_ValueExpressionCaseElse" = None, QueryValueExpression320: "query_ValueExpressionCaseSearchContent" = None, QueryValueExpression258: "query_PredicateInValueRowSelect" = None, QueryValueExpression252: "query_PredicateInValueSelect" = None, QueryValueExpression254: "query_PredicateInValueList" = None, QueryValueExpression256: "query_PredicateInValueList" = None, QueryValueExpression279: "query_ValueExpressionLabeledDuration" = None, QueryValueExpression288: "query_ValueExpressionCombined" = None, QueryValueExpression283: "query_ValueExpressionCast" = None, QueryValueExpression381: "query_UpdateSourceExprList" = None, QueryValueExpression391: "query_ValueExpressionRow" = None, QueryValueExpression315: "query_ValueExpressionCaseSimple" = None, QueryValueExpression328: "query_ValueExpressionCaseSimpleContent" = None, QueryValueExpression330: "query_ValueExpressionCaseSimpleContent" = None, QueryValueExpression345: "query_TableFunction" = None, QueryValueExpression368: "query_ValueExpressionNested" = None, QueryValueExpression419: "query_CallStatement" = None):
        self.unaryOperator = unaryOperator
        self.valueExpr113 = valueExpr113
        self.whenValueExpr = whenValueExpr
        self.resultValueExpr = resultValueExpr
        self.valueExpr118 = valueExpr118
        self.escapeValueExpr = escapeValueExpr
        self.nestedValueExpr = nestedValueExpr
        self.valueExprList126 = valueExprList126
        self.parameterList128 = parameterList128
        self.matchingValueExpr = matchingValueExpr
        self.query_QueryValueExpression = query_QueryValueExpression
        self.exprList = exprList
        self.valueExpr = valueExpr
        self.valueExpr73 = valueExpr73
        self.rightValueExpr = rightValueExpr
        self.leftValueExpr = leftValueExpr
        self.patternValueExpr = patternValueExpr
        self.leftValueExpr95 = leftValueExpr95
        self.valueExpr81 = valueExpr81
        self.valueExprList = valueExprList
        self.valueExpr84 = valueExpr84
        self.valueExprList87 = valueExprList87
        self.valueExpr89 = valueExpr89
        self.valueExprList91 = valueExprList91
        self.valueExpr93 = valueExpr93
        self.valueExpr109 = valueExpr109
        self.rightValueExpr1 = rightValueExpr1
        self.rightValueExpr2 = rightValueExpr2
        self.valueExpr101 = valueExpr101
        self.parameterList = parameterList
        self.leftValueExpr104 = leftValueExpr104
        self.rightValueExpr106 = rightValueExpr106
        self.valueExpr123 = valueExpr123
        self.valueExpr111 = valueExpr111
        self.valueExprList130 = valueExprList130
        self.argumentList = argumentList
        self.QueryValueExpression = QueryValueExpression
        self.QueryValueExpression226 = QueryValueExpression226
        self.QueryValueExpression228 = QueryValueExpression228
        self.QueryValueExpression230 = QueryValueExpression230
        self.QueryValueExpression234 = QueryValueExpression234
        self.QueryValueExpression236 = QueryValueExpression236
        self.QueryValueExpression238 = QueryValueExpression238
        self.QueryValueExpression248 = QueryValueExpression248
        self.QueryValueExpression240 = QueryValueExpression240
        self.QueryValueExpression244 = QueryValueExpression244
        self.QueryValueExpression194 = QueryValueExpression194
        self.QueryValueExpression222 = QueryValueExpression222
        self.QueryValueExpression219 = QueryValueExpression219
        self.QueryValueExpression224 = QueryValueExpression224
        self.QueryValueExpression285 = QueryValueExpression285
        self.QueryValueExpression290 = QueryValueExpression290
        self.QueryValueExpression300 = QueryValueExpression300
        self.QueryValueExpression318 = QueryValueExpression318
        self.QueryValueExpression320 = QueryValueExpression320
        self.QueryValueExpression258 = QueryValueExpression258
        self.QueryValueExpression252 = QueryValueExpression252
        self.QueryValueExpression254 = QueryValueExpression254
        self.QueryValueExpression256 = QueryValueExpression256
        self.QueryValueExpression279 = QueryValueExpression279
        self.QueryValueExpression288 = QueryValueExpression288
        self.QueryValueExpression283 = QueryValueExpression283
        self.QueryValueExpression381 = QueryValueExpression381
        self.QueryValueExpression391 = QueryValueExpression391
        self.QueryValueExpression315 = QueryValueExpression315
        self.QueryValueExpression328 = QueryValueExpression328
        self.QueryValueExpression330 = QueryValueExpression330
        self.QueryValueExpression345 = QueryValueExpression345
        self.QueryValueExpression368 = QueryValueExpression368
        self.QueryValueExpression419 = QueryValueExpression419
        
        pass
    @property
    def unaryOperator(self):
        return self.__unaryOperator

    @unaryOperator.setter
    def unaryOperator(self, unaryOperator: str):
        self.__unaryOperator = unaryOperator


    @property
    def QueryValueExpression300(self):
        return self.__QueryValueExpression300

    @QueryValueExpression300.setter
    def QueryValueExpression300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression300", None)
        self.__QueryValueExpression300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupingExpr"):
                opp_val = getattr(old_value, "groupingExpr", None)
                if opp_val == self:
                    setattr(old_value, "groupingExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupingExpr"):
                opp_val = getattr(value, "groupingExpr", None)
                setattr(value, "groupingExpr", self)

    @property
    def valueExpr109(self):
        return self.__valueExpr109

    @valueExpr109.setter
    def valueExpr109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr109", None)
        self.__valueExpr109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GroupingExpression"):
                opp_val = getattr(old_value, "GroupingExpression", None)
                if opp_val == self:
                    setattr(old_value, "GroupingExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GroupingExpression"):
                opp_val = getattr(value, "GroupingExpression", None)
                setattr(value, "GroupingExpression", self)

    @property
    def QueryValueExpression315(self):
        return self.__QueryValueExpression315

    @QueryValueExpression315.setter
    def QueryValueExpression315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression315", None)
        self.__QueryValueExpression315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCaseSimple314"):
                opp_val = getattr(old_value, "valueExprCaseSimple314", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCaseSimple314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCaseSimple314"):
                opp_val = getattr(value, "valueExprCaseSimple314", None)
                setattr(value, "valueExprCaseSimple314", self)

    @property
    def valueExpr84(self):
        return self.__valueExpr84

    @valueExpr84.setter
    def valueExpr84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr84", None)
        self.__valueExpr84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateInValueList85"):
                opp_val = getattr(old_value, "PredicateInValueList85", None)
                if opp_val == self:
                    setattr(old_value, "PredicateInValueList85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateInValueList85"):
                opp_val = getattr(value, "PredicateInValueList85", None)
                setattr(value, "PredicateInValueList85", self)

    @property
    def QueryValueExpression381(self):
        return self.__QueryValueExpression381

    @QueryValueExpression381.setter
    def QueryValueExpression381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression381", None)
        self.__QueryValueExpression381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "updateSourceExprList"):
                opp_val = getattr(old_value, "updateSourceExprList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "updateSourceExprList"):
                opp_val = getattr(value, "updateSourceExprList", None)
                if opp_val is None:
                    setattr(value, "updateSourceExprList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QueryValueExpression(self):
        return self.__QueryValueExpression

    @QueryValueExpression.setter
    def QueryValueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression", None)
        self.__QueryValueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valuesRow"):
                opp_val = getattr(old_value, "valuesRow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valuesRow"):
                opp_val = getattr(value, "valuesRow", None)
                if opp_val is None:
                    setattr(value, "valuesRow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QueryValueExpression228(self):
        return self.__QueryValueExpression228

    @QueryValueExpression228.setter
    def QueryValueExpression228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression228", None)
        self.__QueryValueExpression228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "betweenRight1"):
                opp_val = getattr(old_value, "betweenRight1", None)
                if opp_val == self:
                    setattr(old_value, "betweenRight1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "betweenRight1"):
                opp_val = getattr(value, "betweenRight1", None)
                setattr(value, "betweenRight1", self)

    @property
    def QueryValueExpression234(self):
        return self.__QueryValueExpression234

    @QueryValueExpression234.setter
    def QueryValueExpression234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression234", None)
        self.__QueryValueExpression234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "likePattern"):
                opp_val = getattr(old_value, "likePattern", None)
                if opp_val == self:
                    setattr(old_value, "likePattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "likePattern"):
                opp_val = getattr(value, "likePattern", None)
                setattr(value, "likePattern", self)

    @property
    def valueExpr123(self):
        return self.__valueExpr123

    @valueExpr123.setter
    def valueExpr123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr123", None)
        self.__valueExpr123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionLabeledDuration"):
                opp_val = getattr(old_value, "ValueExpressionLabeledDuration", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionLabeledDuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionLabeledDuration"):
                opp_val = getattr(value, "ValueExpressionLabeledDuration", None)
                setattr(value, "ValueExpressionLabeledDuration", self)

    @property
    def valueExpr81(self):
        return self.__valueExpr81

    @valueExpr81.setter
    def valueExpr81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr81", None)
        self.__valueExpr81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateIsNull"):
                opp_val = getattr(old_value, "PredicateIsNull", None)
                if opp_val == self:
                    setattr(old_value, "PredicateIsNull", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateIsNull"):
                opp_val = getattr(value, "PredicateIsNull", None)
                setattr(value, "PredicateIsNull", self)

    @property
    def rightValueExpr2(self):
        return self.__rightValueExpr2

    @rightValueExpr2.setter
    def rightValueExpr2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__rightValueExpr2", None)
        self.__rightValueExpr2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateBetween99"):
                opp_val = getattr(old_value, "PredicateBetween99", None)
                if opp_val == self:
                    setattr(old_value, "PredicateBetween99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateBetween99"):
                opp_val = getattr(value, "PredicateBetween99", None)
                setattr(value, "PredicateBetween99", self)

    @property
    def parameterList(self):
        return self.__parameterList

    @parameterList.setter
    def parameterList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__parameterList", None)
        self.__parameterList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionFunction"):
                opp_val = getattr(old_value, "ValueExpressionFunction", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionFunction"):
                opp_val = getattr(value, "ValueExpressionFunction", None)
                setattr(value, "ValueExpressionFunction", self)

    @property
    def QueryValueExpression290(self):
        return self.__QueryValueExpression290

    @QueryValueExpression290.setter
    def QueryValueExpression290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression290", None)
        self.__QueryValueExpression290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCombinedRight"):
                opp_val = getattr(old_value, "valueExprCombinedRight", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCombinedRight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCombinedRight"):
                opp_val = getattr(value, "valueExprCombinedRight", None)
                setattr(value, "valueExprCombinedRight", self)

    @property
    def QueryValueExpression252(self):
        return self.__QueryValueExpression252

    @QueryValueExpression252.setter
    def QueryValueExpression252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression252", None)
        self.__QueryValueExpression252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inValueSelectLeft"):
                opp_val = getattr(old_value, "inValueSelectLeft", None)
                if opp_val == self:
                    setattr(old_value, "inValueSelectLeft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inValueSelectLeft"):
                opp_val = getattr(value, "inValueSelectLeft", None)
                setattr(value, "inValueSelectLeft", self)

    @property
    def QueryValueExpression258(self):
        return self.__QueryValueExpression258

    @QueryValueExpression258.setter
    def QueryValueExpression258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression258", None)
        self.__QueryValueExpression258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inValueRowSelectLeft"):
                opp_val = getattr(old_value, "inValueRowSelectLeft", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inValueRowSelectLeft"):
                opp_val = getattr(value, "inValueRowSelectLeft", None)
                if opp_val is None:
                    setattr(value, "inValueRowSelectLeft", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QueryValueExpression222(self):
        return self.__QueryValueExpression222

    @QueryValueExpression222.setter
    def QueryValueExpression222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression222", None)
        self.__QueryValueExpression222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicRight"):
                opp_val = getattr(old_value, "basicRight", None)
                if opp_val == self:
                    setattr(old_value, "basicRight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicRight"):
                opp_val = getattr(value, "basicRight", None)
                setattr(value, "basicRight", self)

    @property
    def valueExpr111(self):
        return self.__valueExpr111

    @valueExpr111.setter
    def valueExpr111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr111", None)
        self.__valueExpr111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCaseElse"):
                opp_val = getattr(old_value, "ValueExpressionCaseElse", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCaseElse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCaseElse"):
                opp_val = getattr(value, "ValueExpressionCaseElse", None)
                setattr(value, "ValueExpressionCaseElse", self)

    @property
    def valueExpr101(self):
        return self.__valueExpr101

    @valueExpr101.setter
    def valueExpr101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr101", None)
        self.__valueExpr101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCast"):
                opp_val = getattr(old_value, "ValueExpressionCast", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCast", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCast"):
                opp_val = getattr(value, "ValueExpressionCast", None)
                setattr(value, "ValueExpressionCast", self)

    @property
    def QueryValueExpression238(self):
        return self.__QueryValueExpression238

    @QueryValueExpression238.setter
    def QueryValueExpression238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression238", None)
        self.__QueryValueExpression238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "likeEscape"):
                opp_val = getattr(old_value, "likeEscape", None)
                if opp_val == self:
                    setattr(old_value, "likeEscape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "likeEscape"):
                opp_val = getattr(value, "likeEscape", None)
                setattr(value, "likeEscape", self)

    @property
    def QueryValueExpression345(self):
        return self.__QueryValueExpression345

    @QueryValueExpression345.setter
    def QueryValueExpression345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression345", None)
        self.__QueryValueExpression345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableFunction"):
                opp_val = getattr(old_value, "tableFunction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableFunction"):
                opp_val = getattr(value, "tableFunction", None)
                if opp_val is None:
                    setattr(value, "tableFunction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def whenValueExpr(self):
        return self.__whenValueExpr

    @whenValueExpr.setter
    def whenValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__whenValueExpr", None)
        self.__whenValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCaseSimpleContent"):
                opp_val = getattr(old_value, "ValueExpressionCaseSimpleContent", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCaseSimpleContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCaseSimpleContent"):
                opp_val = getattr(value, "ValueExpressionCaseSimpleContent", None)
                setattr(value, "ValueExpressionCaseSimpleContent", self)

    @property
    def leftValueExpr95(self):
        return self.__leftValueExpr95

    @leftValueExpr95.setter
    def leftValueExpr95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__leftValueExpr95", None)
        self.__leftValueExpr95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateBetween"):
                opp_val = getattr(old_value, "PredicateBetween", None)
                if opp_val == self:
                    setattr(old_value, "PredicateBetween", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateBetween"):
                opp_val = getattr(value, "PredicateBetween", None)
                setattr(value, "PredicateBetween", self)

    @property
    def QueryValueExpression230(self):
        return self.__QueryValueExpression230

    @QueryValueExpression230.setter
    def QueryValueExpression230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression230", None)
        self.__QueryValueExpression230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "betweenRight2"):
                opp_val = getattr(old_value, "betweenRight2", None)
                if opp_val == self:
                    setattr(old_value, "betweenRight2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "betweenRight2"):
                opp_val = getattr(value, "betweenRight2", None)
                setattr(value, "betweenRight2", self)

    @property
    def QueryValueExpression328(self):
        return self.__QueryValueExpression328

    @QueryValueExpression328.setter
    def QueryValueExpression328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression328", None)
        self.__QueryValueExpression328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCaseSimpleContentWhen"):
                opp_val = getattr(old_value, "valueExprCaseSimpleContentWhen", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCaseSimpleContentWhen", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCaseSimpleContentWhen"):
                opp_val = getattr(value, "valueExprCaseSimpleContentWhen", None)
                setattr(value, "valueExprCaseSimpleContentWhen", self)

    @property
    def leftValueExpr(self):
        return self.__leftValueExpr

    @leftValueExpr.setter
    def leftValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__leftValueExpr", None)
        self.__leftValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateBasic76"):
                opp_val = getattr(old_value, "PredicateBasic76", None)
                if opp_val == self:
                    setattr(old_value, "PredicateBasic76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateBasic76"):
                opp_val = getattr(value, "PredicateBasic76", None)
                setattr(value, "PredicateBasic76", self)

    @property
    def patternValueExpr(self):
        return self.__patternValueExpr

    @patternValueExpr.setter
    def patternValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__patternValueExpr", None)
        self.__patternValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateLike"):
                opp_val = getattr(old_value, "PredicateLike", None)
                if opp_val == self:
                    setattr(old_value, "PredicateLike", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateLike"):
                opp_val = getattr(value, "PredicateLike", None)
                setattr(value, "PredicateLike", self)

    @property
    def QueryValueExpression254(self):
        return self.__QueryValueExpression254

    @QueryValueExpression254.setter
    def QueryValueExpression254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression254", None)
        self.__QueryValueExpression254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inValueListRight"):
                opp_val = getattr(old_value, "inValueListRight", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inValueListRight"):
                opp_val = getattr(value, "inValueListRight", None)
                if opp_val is None:
                    setattr(value, "inValueListRight", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QueryValueExpression248(self):
        return self.__QueryValueExpression248

    @QueryValueExpression248.setter
    def QueryValueExpression248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression248", None)
        self.__QueryValueExpression248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "quantifiedRowSelectLeft"):
                opp_val = getattr(old_value, "quantifiedRowSelectLeft", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "quantifiedRowSelectLeft"):
                opp_val = getattr(value, "quantifiedRowSelectLeft", None)
                if opp_val is None:
                    setattr(value, "quantifiedRowSelectLeft", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rightValueExpr(self):
        return self.__rightValueExpr

    @rightValueExpr.setter
    def rightValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__rightValueExpr", None)
        self.__rightValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateBasic"):
                opp_val = getattr(old_value, "PredicateBasic", None)
                if opp_val == self:
                    setattr(old_value, "PredicateBasic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateBasic"):
                opp_val = getattr(value, "PredicateBasic", None)
                setattr(value, "PredicateBasic", self)

    @property
    def valueExpr93(self):
        return self.__valueExpr93

    @valueExpr93.setter
    def valueExpr93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr93", None)
        self.__valueExpr93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateQuantifiedValueSelect"):
                opp_val = getattr(old_value, "PredicateQuantifiedValueSelect", None)
                if opp_val == self:
                    setattr(old_value, "PredicateQuantifiedValueSelect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateQuantifiedValueSelect"):
                opp_val = getattr(value, "PredicateQuantifiedValueSelect", None)
                setattr(value, "PredicateQuantifiedValueSelect", self)

    @property
    def valueExprList(self):
        return self.__valueExprList

    @valueExprList.setter
    def valueExprList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExprList", None)
        self.__valueExprList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateInValueList"):
                opp_val = getattr(old_value, "PredicateInValueList", None)
                if opp_val == self:
                    setattr(old_value, "PredicateInValueList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateInValueList"):
                opp_val = getattr(value, "PredicateInValueList", None)
                setattr(value, "PredicateInValueList", self)

    @property
    def valueExprList91(self):
        return self.__valueExprList91

    @valueExprList91.setter
    def valueExprList91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExprList91", None)
        self.__valueExprList91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateQuantifiedRowSelect"):
                opp_val = getattr(old_value, "PredicateQuantifiedRowSelect", None)
                if opp_val == self:
                    setattr(old_value, "PredicateQuantifiedRowSelect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateQuantifiedRowSelect"):
                opp_val = getattr(value, "PredicateQuantifiedRowSelect", None)
                setattr(value, "PredicateQuantifiedRowSelect", self)

    @property
    def QueryValueExpression283(self):
        return self.__QueryValueExpression283

    @QueryValueExpression283.setter
    def QueryValueExpression283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression283", None)
        self.__QueryValueExpression283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCast"):
                opp_val = getattr(old_value, "valueExprCast", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCast", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCast"):
                opp_val = getattr(value, "valueExprCast", None)
                setattr(value, "valueExprCast", self)

    @property
    def QueryValueExpression226(self):
        return self.__QueryValueExpression226

    @QueryValueExpression226.setter
    def QueryValueExpression226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression226", None)
        self.__QueryValueExpression226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "betweenLeft"):
                opp_val = getattr(old_value, "betweenLeft", None)
                if opp_val == self:
                    setattr(old_value, "betweenLeft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "betweenLeft"):
                opp_val = getattr(value, "betweenLeft", None)
                setattr(value, "betweenLeft", self)

    @property
    def exprList(self):
        return self.__exprList

    @exprList.setter
    def exprList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__exprList", None)
        self.__exprList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValuesRow70"):
                opp_val = getattr(old_value, "ValuesRow70", None)
                if opp_val == self:
                    setattr(old_value, "ValuesRow70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValuesRow70"):
                opp_val = getattr(value, "ValuesRow70", None)
                setattr(value, "ValuesRow70", self)

    @property
    def QueryValueExpression240(self):
        return self.__QueryValueExpression240

    @QueryValueExpression240.setter
    def QueryValueExpression240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression240", None)
        self.__QueryValueExpression240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predicateNull"):
                opp_val = getattr(old_value, "predicateNull", None)
                if opp_val == self:
                    setattr(old_value, "predicateNull", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predicateNull"):
                opp_val = getattr(value, "predicateNull", None)
                setattr(value, "predicateNull", self)

    @property
    def QueryValueExpression320(self):
        return self.__QueryValueExpression320

    @QueryValueExpression320.setter
    def QueryValueExpression320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression320", None)
        self.__QueryValueExpression320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCaseSearchContent"):
                opp_val = getattr(old_value, "valueExprCaseSearchContent", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCaseSearchContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCaseSearchContent"):
                opp_val = getattr(value, "valueExprCaseSearchContent", None)
                setattr(value, "valueExprCaseSearchContent", self)

    @property
    def valueExprList126(self):
        return self.__valueExprList126

    @valueExprList126.setter
    def valueExprList126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExprList126", None)
        self.__valueExprList126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UpdateSourceExprList"):
                opp_val = getattr(old_value, "UpdateSourceExprList", None)
                if opp_val == self:
                    setattr(old_value, "UpdateSourceExprList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UpdateSourceExprList"):
                opp_val = getattr(value, "UpdateSourceExprList", None)
                setattr(value, "UpdateSourceExprList", self)

    @property
    def QueryValueExpression330(self):
        return self.__QueryValueExpression330

    @QueryValueExpression330.setter
    def QueryValueExpression330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression330", None)
        self.__QueryValueExpression330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCaseSimpleContentResult"):
                opp_val = getattr(old_value, "valueExprCaseSimpleContentResult", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCaseSimpleContentResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCaseSimpleContentResult"):
                opp_val = getattr(value, "valueExprCaseSimpleContentResult", None)
                setattr(value, "valueExprCaseSimpleContentResult", self)

    @property
    def nestedValueExpr(self):
        return self.__nestedValueExpr

    @nestedValueExpr.setter
    def nestedValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__nestedValueExpr", None)
        self.__nestedValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionNested"):
                opp_val = getattr(old_value, "ValueExpressionNested", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionNested", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionNested"):
                opp_val = getattr(value, "ValueExpressionNested", None)
                setattr(value, "ValueExpressionNested", self)

    @property
    def QueryValueExpression236(self):
        return self.__QueryValueExpression236

    @QueryValueExpression236.setter
    def QueryValueExpression236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression236", None)
        self.__QueryValueExpression236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "likeMatching"):
                opp_val = getattr(old_value, "likeMatching", None)
                if opp_val == self:
                    setattr(old_value, "likeMatching", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "likeMatching"):
                opp_val = getattr(value, "likeMatching", None)
                setattr(value, "likeMatching", self)

    @property
    def matchingValueExpr(self):
        return self.__matchingValueExpr

    @matchingValueExpr.setter
    def matchingValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__matchingValueExpr", None)
        self.__matchingValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateLike79"):
                opp_val = getattr(old_value, "PredicateLike79", None)
                if opp_val == self:
                    setattr(old_value, "PredicateLike79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateLike79"):
                opp_val = getattr(value, "PredicateLike79", None)
                setattr(value, "PredicateLike79", self)

    @property
    def rightValueExpr1(self):
        return self.__rightValueExpr1

    @rightValueExpr1.setter
    def rightValueExpr1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__rightValueExpr1", None)
        self.__rightValueExpr1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateBetween97"):
                opp_val = getattr(old_value, "PredicateBetween97", None)
                if opp_val == self:
                    setattr(old_value, "PredicateBetween97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateBetween97"):
                opp_val = getattr(value, "PredicateBetween97", None)
                setattr(value, "PredicateBetween97", self)

    @property
    def QueryValueExpression224(self):
        return self.__QueryValueExpression224

    @QueryValueExpression224.setter
    def QueryValueExpression224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression224", None)
        self.__QueryValueExpression224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicLeft"):
                opp_val = getattr(old_value, "basicLeft", None)
                if opp_val == self:
                    setattr(old_value, "basicLeft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicLeft"):
                opp_val = getattr(value, "basicLeft", None)
                setattr(value, "basicLeft", self)

    @property
    def QueryValueExpression391(self):
        return self.__QueryValueExpression391

    @QueryValueExpression391.setter
    def QueryValueExpression391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression391", None)
        self.__QueryValueExpression391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprRow"):
                opp_val = getattr(old_value, "valueExprRow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprRow"):
                opp_val = getattr(value, "valueExprRow", None)
                if opp_val is None:
                    setattr(value, "valueExprRow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def QueryValueExpression219(self):
        return self.__QueryValueExpression219

    @QueryValueExpression219.setter
    def QueryValueExpression219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression219", None)
        self.__QueryValueExpression219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resultColumn"):
                opp_val = getattr(old_value, "resultColumn", None)
                if opp_val == self:
                    setattr(old_value, "resultColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resultColumn"):
                opp_val = getattr(value, "resultColumn", None)
                setattr(value, "resultColumn", self)

    @property
    def QueryValueExpression288(self):
        return self.__QueryValueExpression288

    @QueryValueExpression288.setter
    def QueryValueExpression288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression288", None)
        self.__QueryValueExpression288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCombinedLeft"):
                opp_val = getattr(old_value, "valueExprCombinedLeft", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCombinedLeft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCombinedLeft"):
                opp_val = getattr(value, "valueExprCombinedLeft", None)
                setattr(value, "valueExprCombinedLeft", self)

    @property
    def argumentList(self):
        return self.__argumentList

    @argumentList.setter
    def argumentList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__argumentList", None)
        self.__argumentList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CallStatement"):
                opp_val = getattr(old_value, "CallStatement", None)
                if opp_val == self:
                    setattr(old_value, "CallStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CallStatement"):
                opp_val = getattr(value, "CallStatement", None)
                setattr(value, "CallStatement", self)

    @property
    def QueryValueExpression244(self):
        return self.__QueryValueExpression244

    @QueryValueExpression244.setter
    def QueryValueExpression244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression244", None)
        self.__QueryValueExpression244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "quantifiedValueSelectLeft"):
                opp_val = getattr(old_value, "quantifiedValueSelectLeft", None)
                if opp_val == self:
                    setattr(old_value, "quantifiedValueSelectLeft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "quantifiedValueSelectLeft"):
                opp_val = getattr(value, "quantifiedValueSelectLeft", None)
                setattr(value, "quantifiedValueSelectLeft", self)

    @property
    def QueryValueExpression194(self):
        return self.__QueryValueExpression194

    @QueryValueExpression194.setter
    def QueryValueExpression194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression194", None)
        self.__QueryValueExpression194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orderByValueExpr"):
                opp_val = getattr(old_value, "orderByValueExpr", None)
                if opp_val == self:
                    setattr(old_value, "orderByValueExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orderByValueExpr"):
                opp_val = getattr(value, "orderByValueExpr", None)
                setattr(value, "orderByValueExpr", self)

    @property
    def valueExprList130(self):
        return self.__valueExprList130

    @valueExprList130.setter
    def valueExprList130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExprList130", None)
        self.__valueExprList130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionRow"):
                opp_val = getattr(old_value, "ValueExpressionRow", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionRow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionRow"):
                opp_val = getattr(value, "ValueExpressionRow", None)
                setattr(value, "ValueExpressionRow", self)

    @property
    def valueExpr118(self):
        return self.__valueExpr118

    @valueExpr118.setter
    def valueExpr118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr118", None)
        self.__valueExpr118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCaseSearchContent119"):
                opp_val = getattr(old_value, "ValueExpressionCaseSearchContent119", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCaseSearchContent119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCaseSearchContent119"):
                opp_val = getattr(value, "ValueExpressionCaseSearchContent119", None)
                setattr(value, "ValueExpressionCaseSearchContent119", self)

    @property
    def escapeValueExpr(self):
        return self.__escapeValueExpr

    @escapeValueExpr.setter
    def escapeValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__escapeValueExpr", None)
        self.__escapeValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateLike121"):
                opp_val = getattr(old_value, "PredicateLike121", None)
                if opp_val == self:
                    setattr(old_value, "PredicateLike121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateLike121"):
                opp_val = getattr(value, "PredicateLike121", None)
                setattr(value, "PredicateLike121", self)

    @property
    def QueryValueExpression419(self):
        return self.__QueryValueExpression419

    @QueryValueExpression419.setter
    def QueryValueExpression419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression419", None)
        self.__QueryValueExpression419 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "callStatement"):
                opp_val = getattr(old_value, "callStatement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "callStatement"):
                opp_val = getattr(value, "callStatement", None)
                if opp_val is None:
                    setattr(value, "callStatement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def leftValueExpr104(self):
        return self.__leftValueExpr104

    @leftValueExpr104.setter
    def leftValueExpr104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__leftValueExpr104", None)
        self.__leftValueExpr104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCombined"):
                opp_val = getattr(old_value, "ValueExpressionCombined", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCombined", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCombined"):
                opp_val = getattr(value, "ValueExpressionCombined", None)
                setattr(value, "ValueExpressionCombined", self)

    @property
    def QueryValueExpression368(self):
        return self.__QueryValueExpression368

    @QueryValueExpression368.setter
    def QueryValueExpression368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression368", None)
        self.__QueryValueExpression368 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nest367"):
                opp_val = getattr(old_value, "nest367", None)
                if opp_val == self:
                    setattr(old_value, "nest367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nest367"):
                opp_val = getattr(value, "nest367", None)
                setattr(value, "nest367", self)

    @property
    def QueryValueExpression318(self):
        return self.__QueryValueExpression318

    @QueryValueExpression318.setter
    def QueryValueExpression318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression318", None)
        self.__QueryValueExpression318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprCaseElse"):
                opp_val = getattr(old_value, "valueExprCaseElse", None)
                if opp_val == self:
                    setattr(old_value, "valueExprCaseElse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprCaseElse"):
                opp_val = getattr(value, "valueExprCaseElse", None)
                setattr(value, "valueExprCaseElse", self)

    @property
    def rightValueExpr106(self):
        return self.__rightValueExpr106

    @rightValueExpr106.setter
    def rightValueExpr106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__rightValueExpr106", None)
        self.__rightValueExpr106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCombined107"):
                opp_val = getattr(old_value, "ValueExpressionCombined107", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCombined107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCombined107"):
                opp_val = getattr(value, "ValueExpressionCombined107", None)
                setattr(value, "ValueExpressionCombined107", self)

    @property
    def QueryValueExpression285(self):
        return self.__QueryValueExpression285

    @QueryValueExpression285.setter
    def QueryValueExpression285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression285", None)
        self.__QueryValueExpression285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprFunction"):
                opp_val = getattr(old_value, "valueExprFunction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprFunction"):
                opp_val = getattr(value, "valueExprFunction", None)
                if opp_val is None:
                    setattr(value, "valueExprFunction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def valueExpr89(self):
        return self.__valueExpr89

    @valueExpr89.setter
    def valueExpr89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr89", None)
        self.__valueExpr89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateInValueSelect"):
                opp_val = getattr(old_value, "PredicateInValueSelect", None)
                if opp_val == self:
                    setattr(old_value, "PredicateInValueSelect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateInValueSelect"):
                opp_val = getattr(value, "PredicateInValueSelect", None)
                setattr(value, "PredicateInValueSelect", self)

    @property
    def parameterList128(self):
        return self.__parameterList128

    @parameterList128.setter
    def parameterList128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__parameterList128", None)
        self.__parameterList128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TableFunction"):
                opp_val = getattr(old_value, "TableFunction", None)
                if opp_val == self:
                    setattr(old_value, "TableFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TableFunction"):
                opp_val = getattr(value, "TableFunction", None)
                setattr(value, "TableFunction", self)

    @property
    def valueExpr73(self):
        return self.__valueExpr73

    @valueExpr73.setter
    def valueExpr73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr73", None)
        self.__valueExpr73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResultColumn"):
                opp_val = getattr(old_value, "ResultColumn", None)
                if opp_val == self:
                    setattr(old_value, "ResultColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResultColumn"):
                opp_val = getattr(value, "ResultColumn", None)
                setattr(value, "ResultColumn", self)

    @property
    def valueExpr113(self):
        return self.__valueExpr113

    @valueExpr113.setter
    def valueExpr113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr113", None)
        self.__valueExpr113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCaseSimple"):
                opp_val = getattr(old_value, "ValueExpressionCaseSimple", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCaseSimple", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCaseSimple"):
                opp_val = getattr(value, "ValueExpressionCaseSimple", None)
                setattr(value, "ValueExpressionCaseSimple", self)

    @property
    def resultValueExpr(self):
        return self.__resultValueExpr

    @resultValueExpr.setter
    def resultValueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__resultValueExpr", None)
        self.__resultValueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpressionCaseSimpleContent116"):
                opp_val = getattr(old_value, "ValueExpressionCaseSimpleContent116", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpressionCaseSimpleContent116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpressionCaseSimpleContent116"):
                opp_val = getattr(value, "ValueExpressionCaseSimpleContent116", None)
                setattr(value, "ValueExpressionCaseSimpleContent116", self)

    @property
    def QueryValueExpression279(self):
        return self.__QueryValueExpression279

    @QueryValueExpression279.setter
    def QueryValueExpression279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression279", None)
        self.__QueryValueExpression279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "valueExprLabeledDuration"):
                opp_val = getattr(old_value, "valueExprLabeledDuration", None)
                if opp_val == self:
                    setattr(old_value, "valueExprLabeledDuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "valueExprLabeledDuration"):
                opp_val = getattr(value, "valueExprLabeledDuration", None)
                setattr(value, "valueExprLabeledDuration", self)

    @property
    def query_QueryValueExpression(self):
        return self.__query_QueryValueExpression

    @query_QueryValueExpression.setter
    def query_QueryValueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__query_QueryValueExpression", None)
        self.__query_QueryValueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def valueExprList87(self):
        return self.__valueExprList87

    @valueExprList87.setter
    def valueExprList87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExprList87", None)
        self.__valueExprList87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PredicateInValueRowSelect"):
                opp_val = getattr(old_value, "PredicateInValueRowSelect", None)
                if opp_val == self:
                    setattr(old_value, "PredicateInValueRowSelect", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PredicateInValueRowSelect"):
                opp_val = getattr(value, "PredicateInValueRowSelect", None)
                setattr(value, "PredicateInValueRowSelect", self)

    @property
    def QueryValueExpression256(self):
        return self.__QueryValueExpression256

    @QueryValueExpression256.setter
    def QueryValueExpression256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__QueryValueExpression256", None)
        self.__QueryValueExpression256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inValueListLeft"):
                opp_val = getattr(old_value, "inValueListLeft", None)
                if opp_val == self:
                    setattr(old_value, "inValueListLeft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inValueListLeft"):
                opp_val = getattr(value, "inValueListLeft", None)
                setattr(value, "inValueListLeft", self)

    @property
    def valueExpr(self):
        return self.__valueExpr

    @valueExpr.setter
    def valueExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_query_QueryValueExpression__valueExpr", None)
        self.__valueExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrderByValueExpression"):
                opp_val = getattr(old_value, "OrderByValueExpression", None)
                if opp_val == self:
                    setattr(old_value, "OrderByValueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrderByValueExpression"):
                opp_val = getattr(value, "OrderByValueExpression", None)
                setattr(value, "OrderByValueExpression", self)

class query_MergeOnCondition(SQLQueryObject):

    pass
class query_WithTableSpecification(SQLQueryObject):

    pass
class query_GroupingSpecification(SQLQueryObject):

    pass
class query_UpdateAssignmentExpression(SQLQueryObject):

    pass
class query_QueryExpressionRoot(SQLQueryObject, expressions_QueryExpression):

    pass
class query_MergeTargetTable(SQLQueryObject):

    pass
class query_UpdateOfColumn(SQLQueryObject):

    pass
class query_SuperGroupElement(SQLQueryObject):

    pass
class query_ValueExpressionCaseElse(SQLQueryObject):

    pass
class query_ValuesRow(SQLQueryObject):

    pass
class query_CursorReference(SQLQueryObject):

    pass
class query_QueryResultSpecification(SQLQueryObject):

    pass
class query_ValueExpressionCaseSearchContent(SQLQueryObject):

    pass
class query_TableCorrelation(SQLQueryObject):

    pass
class query_MergeSourceTable(SQLQueryObject):

    pass
class query_QueryStatement(SQLQueryObject, statements_SQLDataStatement):

    pass
class QueryChangeStatement:

    pass
class query_QueryInsertStatement(QueryChangeStatement):

    pass
class query_QueryMergeStatement(QueryChangeStatement):

    pass
class query_QueryUpdateStatement(QueryChangeStatement):

    pass
class query_QueryDeleteStatement(QueryChangeStatement):

    pass