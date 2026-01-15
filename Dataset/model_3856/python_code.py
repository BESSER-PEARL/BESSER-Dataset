from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SimpleTerm:

    pass
class sql_term_SimpleTermInteger(SimpleTerm):

    pass
class sql_term_SimpleTermFloat(SimpleTerm):

    pass
class sql_term_SimpleTermString(SimpleTerm):

    pass
class BooleanTerm:

    pass
class sql_term_BooleanTermFalse(BooleanTerm):

    pass
class sql_term_BooleanTermTrue(BooleanTerm):

    pass
class Term:

    pass
class sql_term_SimpleTerm(Term):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sql_term_NullTerm(Term):

    pass
class sql_term_ColumnTerm(Term):

    pass
class sql_term_BooleanTerm(Term):

    pass
class sql_term_Term(ABC):

    pass
class value_ValueFrontOperation:

    pass
class value_ValueOperation:

    pass
class term_Term:

    pass
class sql_term_StarTerm(Term):

    pass
class sql_term_CountStarTerm(Term):

    pass
class sql_term_SimpleTermChar(SimpleTerm):

    pass
class ValueFrontOperation:

    pass
class sql_value_ValueFrontOperationMinus(ValueFrontOperation):

    pass
class sql_value_ValueFrontOperationPlus(ValueFrontOperation):

    pass
class ValueOperation:

    pass
class sql_value_ValueFrontOperation(ValueOperation):

    pass
class sql_value_Value(ABC):

    pass
class ConditionOperation:

    pass
class sql_condition_ConditionOperationGreatEqual(ConditionOperation):

    pass
class sql_condition_ConditionOperationUnEqual2(ConditionOperation):

    pass
class sql_condition_ConditionOperationUnEqual(ConditionOperation):

    pass
class sql_condition_ConditionOperationGreater(ConditionOperation):

    pass
class sql_condition_ConditionOperationLesser(ConditionOperation):

    pass
class sql_condition_ConditionOperationLessEqual(ConditionOperation):

    pass
class sql_condition_ConditionOperationEqual(ConditionOperation):

    pass
class sql_condition_ConditionOperation(ABC):

    pass
class condition_ConditionOperation:

    pass
class SimpleCondition:

    pass
class sql_condition_BetweenCondition(SimpleCondition):

    pass
class sql_condition_ExistsCondition(SimpleCondition):

    pass
class sql_condition_IsNullCondition(SimpleCondition):

    pass
class sql_condition_LikeCondition(SimpleCondition):

    pass
class sql_condition_InCondition(SimpleCondition):

    pass
class sql_condition_OperationCondition(SimpleCondition):

    pass
class Value:

    pass
class sql_value_FunctionValue(Value):

    def __init__(self, functionName: str, sql_value_FunctionValue: set["value_Value"] = None):
        self.functionName = functionName
        self.sql_value_FunctionValue = sql_value_FunctionValue if sql_value_FunctionValue is not None else set()
        
    @property
    def functionName(self) -> str:
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName

    @property
    def sql_value_FunctionValue(self):
        return self.__sql_value_FunctionValue

    @sql_value_FunctionValue.setter
    def sql_value_FunctionValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_value_FunctionValue__sql_value_FunctionValue", None)
        self.__sql_value_FunctionValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "value_Value85"):
                    opp_val = getattr(item, "value_Value85", None)
                    
                    if opp_val == self:
                        setattr(item, "value_Value85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "value_Value85"):
                    opp_val = getattr(item, "value_Value85", None)
                    
                    setattr(item, "value_Value85", self)
                    

class sql_value_ConditionValue(Value):

    pass
class sql_value_SimpleValue(Value):

    pass
class sql_value_ValueOperationParallel(ValueOperation):

    pass
class sql_value_ValueOperationDivide(ValueOperation):

    pass
class sql_value_ValueOperationMultiply(ValueOperation):

    pass
class sql_value_ValueOperation(ABC):

    pass
class AndOrExpressionOperation:

    pass
class sql_expression_ExpressionOperationOr(AndOrExpressionOperation):

    pass
class sql_expression_ExpressionOperationAnd(AndOrExpressionOperation):

    pass
class ExpressionOperation:

    pass
class sql_expression_ExpressionOperationNot(ExpressionOperation):

    pass
class sql_expression_AndOrExpressionOperation(ExpressionOperation):

    pass
class sql_expression_ExpressionOperation(ABC):

    pass
class expression_ExpressionOperationNot:

    pass
class condition_Condition:

    pass
class expression_AndOrExpressionOperation:

    pass
class Expression:

    pass
class sql_expression_SimpleExpression(Expression):

    pass
class sql_expression_Expression(ABC):

    pass
class sql_limit_LimitExpression:

    def __init__(self, limit: str, offset: str):
        self.limit = limit
        self.offset = offset
        
    @property
    def limit(self) -> str:
        return self.__limit

    @limit.setter
    def limit(self, limit: str):
        self.__limit = limit

    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

class parameter_SelectParameterDistinct:

    pass
class SetOperation:

    pass
class sql_set_SetOperationExcept(SetOperation):

    pass
class sql_set_SetOperationMinus(SetOperation):

    pass
class sql_set_SetOperationIntersect(SetOperation):

    pass
class sql_set_SetOperationUnion(SetOperation):

    pass
class value_Value:

    pass
class Condition:

    pass
class sql_condition_SimpleCondition(Condition):

    pass
class sql_condition_Condition(ABC):

    pass
class sql_set_SetExpression:

    pass
class sql_having_HavingExpression:

    pass
class sql_groupBy_GroupByExpression:

    pass
class OrderByParameter:

    pass
class sql_orderBy_OrderByParameterDesc(OrderByParameter):

    pass
class sql_orderBy_OrderByParameterAsc(OrderByParameter):

    pass
class sql_orderBy_OrderByParameter(ABC):

    pass
class column_Column:

    pass
class OrderByExpression:

    pass
class sql_orderBy_OrderByAliasExpression(OrderByExpression):

    def __init__(self, alias: str):
        self.alias = alias
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

class sql_orderBy_OrderBySelectExpression(OrderByExpression):

    pass
class sql_orderBy_OrderByColumnExpression(OrderByExpression):

    pass
class orderBy_OrderByParameter:

    pass
class sql_orderBy_OrderByExpression(ABC):

    pass
class sql_where_WhereExpression:

    pass
class JoinOperation:

    pass
class sql_from_JoinOperationOuter(JoinOperation):

    pass
class sql_from_JoinOperationRight(JoinOperation):

    pass
class sql_from_JoinOperationLeft(JoinOperation):

    pass
class sql_from_JoinOperationInner(JoinOperation):

    pass
class sql_from_JoinOperation(ABC):

    pass
class sql_set_SetOperation(ABC):

    pass
class set_SetOperation:

    pass
class from_JoinOperation:

    pass
class sql_from_JoinTableExpression:

    pass
class from_JoinTableExpression:

    pass
class from_TableExpression:

    pass
class sql_from_TableListExpression:

    pass
class sql_from_Table:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class from_Table:

    pass
class SelectExpression:

    pass
class sql_from_TableExpression:

    def __init__(self, label: str, sql_from_TableExpression: "SelectExpression" = None, sql_from_TableExpression27: "from_Table" = None):
        self.label = label
        self.sql_from_TableExpression = sql_from_TableExpression
        self.sql_from_TableExpression27 = sql_from_TableExpression27
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def sql_from_TableExpression27(self):
        return self.__sql_from_TableExpression27

    @sql_from_TableExpression27.setter
    def sql_from_TableExpression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_from_TableExpression__sql_from_TableExpression27", None)
        self.__sql_from_TableExpression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from_Table"):
                opp_val = getattr(old_value, "from_Table", None)
                if opp_val == self:
                    setattr(old_value, "from_Table", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from_Table"):
                opp_val = getattr(value, "from_Table", None)
                setattr(value, "from_Table", self)

    @property
    def sql_from_TableExpression(self):
        return self.__sql_from_TableExpression

    @sql_from_TableExpression.setter
    def sql_from_TableExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_from_TableExpression__sql_from_TableExpression", None)
        self.__sql_from_TableExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SelectExpression"):
                opp_val = getattr(old_value, "SelectExpression", None)
                if opp_val == self:
                    setattr(old_value, "SelectExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SelectExpression"):
                opp_val = getattr(value, "SelectExpression", None)
                setattr(value, "SelectExpression", self)

class from_TableListExpression:

    pass
class sql_from_FromExpression:

    pass
class sql_column_Column:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ColumnOperation:

    pass
class sql_column_ColumnOperationAvg(ColumnOperation):

    pass
class sql_column_ColumnOperationSome(ColumnOperation):

    pass
class sql_column_ColumnOperationMin(ColumnOperation):

    pass
class sql_column_ColumnOperationEvery(ColumnOperation):

    pass
class sql_column_ColumnOperationSum(ColumnOperation):

    pass
class sql_column_ColumnOperationMax(ColumnOperation):

    pass
class sql_column_ColumnOperationCount(ColumnOperation):

    pass
class sql_column_ColumnOperation(ABC):

    pass
class column_ColumnOperation:

    pass
class sql_column_SingleColumnExpression:

    def __init__(self, alias: str, sql_column_SingleColumnExpression: "expression_Expression" = None, sql_column_SingleColumnExpression20: "column_ColumnOperation" = None, sql_column_SingleColumnExpression22: "parameter_SelectParameter" = None):
        self.alias = alias
        self.sql_column_SingleColumnExpression = sql_column_SingleColumnExpression
        self.sql_column_SingleColumnExpression20 = sql_column_SingleColumnExpression20
        self.sql_column_SingleColumnExpression22 = sql_column_SingleColumnExpression22
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def sql_column_SingleColumnExpression(self):
        return self.__sql_column_SingleColumnExpression

    @sql_column_SingleColumnExpression.setter
    def sql_column_SingleColumnExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_column_SingleColumnExpression__sql_column_SingleColumnExpression", None)
        self.__sql_column_SingleColumnExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_Expression"):
                opp_val = getattr(old_value, "expression_Expression", None)
                if opp_val == self:
                    setattr(old_value, "expression_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_Expression"):
                opp_val = getattr(value, "expression_Expression", None)
                setattr(value, "expression_Expression", self)

    @property
    def sql_column_SingleColumnExpression22(self):
        return self.__sql_column_SingleColumnExpression22

    @sql_column_SingleColumnExpression22.setter
    def sql_column_SingleColumnExpression22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_column_SingleColumnExpression__sql_column_SingleColumnExpression22", None)
        self.__sql_column_SingleColumnExpression22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameter_SelectParameter23"):
                opp_val = getattr(old_value, "parameter_SelectParameter23", None)
                if opp_val == self:
                    setattr(old_value, "parameter_SelectParameter23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameter_SelectParameter23"):
                opp_val = getattr(value, "parameter_SelectParameter23", None)
                setattr(value, "parameter_SelectParameter23", self)

    @property
    def sql_column_SingleColumnExpression20(self):
        return self.__sql_column_SingleColumnExpression20

    @sql_column_SingleColumnExpression20.setter
    def sql_column_SingleColumnExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sql_column_SingleColumnExpression__sql_column_SingleColumnExpression20", None)
        self.__sql_column_SingleColumnExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "column_ColumnOperation"):
                opp_val = getattr(old_value, "column_ColumnOperation", None)
                if opp_val == self:
                    setattr(old_value, "column_ColumnOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "column_ColumnOperation"):
                opp_val = getattr(value, "column_ColumnOperation", None)
                setattr(value, "column_ColumnOperation", self)

class column_SingleColumnExpression:

    pass
class sql_column_ColumnExpression:

    pass
class SelectParameter:

    pass
class sql_parameter_SelectParameterDistinct(SelectParameter):

    pass
class sql_parameter_SelectParameterAll(SelectParameter):

    pass
class sql_parameter_SelectParameter(ABC):

    pass
class limit_LimitExpression:

    pass
class orderBy_OrderByExpression:

    pass
class set_SetExpression:

    pass
class having_HavingExpression:

    pass
class groupBy_GroupByExpression:

    pass
class where_WhereExpression:

    pass
class from_FromExpression:

    pass
class column_ColumnExpression:

    pass
class parameter_SelectParameter:

    pass
class sql_select_SelectExpression:

    pass
class expression_Expression:

    pass
class sql_sqlDataTypes_DataType(ABC):

    pass
class DataType:

    pass
class sql_sqlDataTypes_Real(DataType):

    pass
class sql_sqlDataTypes_Double(DataType):

    pass
class sql_sqlDataTypes_Boolean(DataType):

    pass
class sql_sqlDataTypes_String(DataType):

    pass
class sql_sqlDataTypes_Float(DataType):

    pass
class sql_sqlDataTypes_Integer(DataType):

    pass
class Date:

    pass
class sql_sqlDataTypes_TimeStamp(Date):

    pass
class sql_sqlDataTypes_Date(DataType):

    pass