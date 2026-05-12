####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
sql_sqlDataTypes_String = Class(name="sql_sqlDataTypes_String")
DataType = Class(name="DataType")
sql_sqlDataTypes_DataType = Class(name="sql_sqlDataTypes_DataType", is_abstract=True)
sql_sqlDataTypes_Boolean = Class(name="sql_sqlDataTypes_Boolean")
sql_sqlDataTypes_Date = Class(name="sql_sqlDataTypes_Date")
sql_sqlDataTypes_Real = Class(name="sql_sqlDataTypes_Real")
sql_sqlDataTypes_Integer = Class(name="sql_sqlDataTypes_Integer")
sql_sqlDataTypes_TimeStamp = Class(name="sql_sqlDataTypes_TimeStamp")
Date = Class(name="Date")
where_WhereExpression = Class(name="where_WhereExpression")
groupBy_GroupByExpression = Class(name="groupBy_GroupByExpression")
sql_sqlDataTypes_Float = Class(name="sql_sqlDataTypes_Float")
sql_sqlDataTypes_Double = Class(name="sql_sqlDataTypes_Double")
sql_select_SelectExpression = Class(name="sql_select_SelectExpression")
parameter_SelectParameter = Class(name="parameter_SelectParameter")
column_ColumnExpression = Class(name="column_ColumnExpression")
from_FromExpression = Class(name="from_FromExpression")
sql_parameter_SelectParameterAll = Class(name="sql_parameter_SelectParameterAll")
SelectParameter = Class(name="SelectParameter")
sql_parameter_SelectParameterDistinct = Class(name="sql_parameter_SelectParameterDistinct")
having_HavingExpression = Class(name="having_HavingExpression")
set_SetExpression = Class(name="set_SetExpression")
orderBy_OrderByExpression = Class(name="orderBy_OrderByExpression")
limit_LimitExpression = Class(name="limit_LimitExpression")
sql_parameter_SelectParameter = Class(name="sql_parameter_SelectParameter", is_abstract=True)
sql_column_ColumnOperationCount = Class(name="sql_column_ColumnOperationCount")
ColumnOperation = Class(name="ColumnOperation")
sql_column_ColumnOperationMin = Class(name="sql_column_ColumnOperationMin")
sql_column_ColumnOperationMax = Class(name="sql_column_ColumnOperationMax")
sql_column_ColumnExpression = Class(name="sql_column_ColumnExpression")
column_SingleColumnExpression = Class(name="column_SingleColumnExpression")
sql_column_SingleColumnExpression = Class(name="sql_column_SingleColumnExpression")
expression_Expression = Class(name="expression_Expression")
column_ColumnOperation = Class(name="column_ColumnOperation")
sql_column_ColumnOperation = Class(name="sql_column_ColumnOperation", is_abstract=True)
from_Table = Class(name="from_Table")
sql_from_Table = Class(name="sql_from_Table")
sql_column_ColumnOperationSum = Class(name="sql_column_ColumnOperationSum")
sql_column_ColumnOperationAvg = Class(name="sql_column_ColumnOperationAvg")
sql_column_ColumnOperationEvery = Class(name="sql_column_ColumnOperationEvery")
sql_column_ColumnOperationSome = Class(name="sql_column_ColumnOperationSome")
sql_column_Column = Class(name="sql_column_Column")
sql_from_FromExpression = Class(name="sql_from_FromExpression")
from_TableListExpression = Class(name="from_TableListExpression")
sql_from_TableExpression = Class(name="sql_from_TableExpression")
SelectExpression = Class(name="SelectExpression")
sql_from_JoinOperation = Class(name="sql_from_JoinOperation", is_abstract=True)
sql_from_JoinOperationInner = Class(name="sql_from_JoinOperationInner")
JoinOperation = Class(name="JoinOperation")
sql_from_TableListExpression = Class(name="sql_from_TableListExpression")
from_TableExpression = Class(name="from_TableExpression")
from_JoinTableExpression = Class(name="from_JoinTableExpression")
sql_from_JoinTableExpression = Class(name="sql_from_JoinTableExpression")
from_JoinOperation = Class(name="from_JoinOperation")
sql_orderBy_OrderByAliasExpression = Class(name="sql_orderBy_OrderByAliasExpression")
sql_from_JoinOperationLeft = Class(name="sql_from_JoinOperationLeft")
sql_from_JoinOperationRight = Class(name="sql_from_JoinOperationRight")
sql_from_JoinOperationOuter = Class(name="sql_from_JoinOperationOuter")
sql_where_WhereExpression = Class(name="sql_where_WhereExpression")
sql_orderBy_OrderByExpression = Class(name="sql_orderBy_OrderByExpression", is_abstract=True)
orderBy_OrderByParameter = Class(name="orderBy_OrderByParameter")
sql_orderBy_OrderByColumnExpression = Class(name="sql_orderBy_OrderByColumnExpression")
OrderByExpression = Class(name="OrderByExpression")
column_Column = Class(name="column_Column")
sql_orderBy_OrderByParameterAsc = Class(name="sql_orderBy_OrderByParameterAsc")
OrderByParameter = Class(name="OrderByParameter")
sql_orderBy_OrderBySelectExpression = Class(name="sql_orderBy_OrderBySelectExpression")
sql_orderBy_OrderByParameter = Class(name="sql_orderBy_OrderByParameter", is_abstract=True)
sql_groupBy_GroupByExpression = Class(name="sql_groupBy_GroupByExpression")
sql_orderBy_OrderByParameterDesc = Class(name="sql_orderBy_OrderByParameterDesc")
sql_set_SetOperation = Class(name="sql_set_SetOperation", is_abstract=True)
sql_set_SetOperationUnion = Class(name="sql_set_SetOperationUnion")
SetOperation = Class(name="SetOperation")
sql_set_SetOperationMinus = Class(name="sql_set_SetOperationMinus")
parameter_SelectParameterDistinct = Class(name="parameter_SelectParameterDistinct")
sql_having_HavingExpression = Class(name="sql_having_HavingExpression")
sql_set_SetOperationExcept = Class(name="sql_set_SetOperationExcept")
sql_set_SetExpression = Class(name="sql_set_SetExpression")
set_SetOperation = Class(name="set_SetOperation")
sql_expression_Expression = Class(name="sql_expression_Expression", is_abstract=True)
sql_expression_SimpleExpression = Class(name="sql_expression_SimpleExpression")
Expression = Class(name="Expression")
expression_AndOrExpressionOperation = Class(name="expression_AndOrExpressionOperation")
condition_Condition = Class(name="condition_Condition")
sql_set_SetOperationIntersect = Class(name="sql_set_SetOperationIntersect")
sql_limit_LimitExpression = Class(name="sql_limit_LimitExpression")
sql_expression_ExpressionOperationOr = Class(name="sql_expression_ExpressionOperationOr")
sql_condition_Condition = Class(name="sql_condition_Condition", is_abstract=True)
sql_condition_SimpleCondition = Class(name="sql_condition_SimpleCondition")
Condition = Class(name="Condition")
value_Value = Class(name="value_Value")
sql_condition_OperationCondition = Class(name="sql_condition_OperationCondition")
SimpleCondition = Class(name="SimpleCondition")
expression_ExpressionOperationNot = Class(name="expression_ExpressionOperationNot")
sql_expression_ExpressionOperation = Class(name="sql_expression_ExpressionOperation", is_abstract=True)
sql_expression_AndOrExpressionOperation = Class(name="sql_expression_AndOrExpressionOperation")
ExpressionOperation = Class(name="ExpressionOperation")
sql_expression_ExpressionOperationNot = Class(name="sql_expression_ExpressionOperationNot")
sql_expression_ExpressionOperationAnd = Class(name="sql_expression_ExpressionOperationAnd")
AndOrExpressionOperation = Class(name="AndOrExpressionOperation")
sql_condition_ExistsCondition = Class(name="sql_condition_ExistsCondition")
sql_condition_BetweenCondition = Class(name="sql_condition_BetweenCondition")
sql_condition_InCondition = Class(name="sql_condition_InCondition")
condition_ConditionOperation = Class(name="condition_ConditionOperation")
sql_condition_IsNullCondition = Class(name="sql_condition_IsNullCondition")
sql_condition_LikeCondition = Class(name="sql_condition_LikeCondition")
sql_condition_ConditionOperation = Class(name="sql_condition_ConditionOperation", is_abstract=True)
sql_condition_ConditionOperationLesser = Class(name="sql_condition_ConditionOperationLesser")
sql_condition_ConditionOperationLessEqual = Class(name="sql_condition_ConditionOperationLessEqual")
sql_condition_ConditionOperationEqual = Class(name="sql_condition_ConditionOperationEqual")
ConditionOperation = Class(name="ConditionOperation")
sql_condition_ConditionOperationGreater = Class(name="sql_condition_ConditionOperationGreater")
sql_condition_ConditionOperationGreatEqual = Class(name="sql_condition_ConditionOperationGreatEqual")
sql_condition_ConditionOperationUnEqual2 = Class(name="sql_condition_ConditionOperationUnEqual2")
sql_value_Value = Class(name="sql_value_Value", is_abstract=True)
sql_value_ValueFrontOperation = Class(name="sql_value_ValueFrontOperation", is_abstract=True)
ValueOperation = Class(name="ValueOperation")
sql_value_ValueFrontOperationPlus = Class(name="sql_value_ValueFrontOperationPlus")
ValueFrontOperation = Class(name="ValueFrontOperation")
sql_value_ValueFrontOperationMinus = Class(name="sql_value_ValueFrontOperationMinus")
sql_value_ValueOperation = Class(name="sql_value_ValueOperation", is_abstract=True)
sql_value_ValueOperationMultiply = Class(name="sql_value_ValueOperationMultiply")
sql_condition_ConditionOperationUnEqual = Class(name="sql_condition_ConditionOperationUnEqual")
sql_value_ValueOperationDivide = Class(name="sql_value_ValueOperationDivide")
sql_value_ValueOperationParallel = Class(name="sql_value_ValueOperationParallel")
sql_value_SimpleValue = Class(name="sql_value_SimpleValue")
Value = Class(name="Value")
term_Term = Class(name="term_Term")
value_ValueOperation = Class(name="value_ValueOperation")
value_ValueFrontOperation = Class(name="value_ValueFrontOperation")
sql_value_ConditionValue = Class(name="sql_value_ConditionValue")
sql_value_FunctionValue = Class(name="sql_value_FunctionValue")
sql_term_Term = Class(name="sql_term_Term", is_abstract=True)
sql_term_BooleanTerm = Class(name="sql_term_BooleanTerm", is_abstract=True)
Term = Class(name="Term")
sql_term_BooleanTermTrue = Class(name="sql_term_BooleanTermTrue")
BooleanTerm = Class(name="BooleanTerm")
sql_term_BooleanTermFalse = Class(name="sql_term_BooleanTermFalse")
sql_term_NullTerm = Class(name="sql_term_NullTerm")
sql_term_ColumnTerm = Class(name="sql_term_ColumnTerm")
sql_term_SimpleTerm = Class(name="sql_term_SimpleTerm", is_abstract=True)
sql_term_SimpleTermString = Class(name="sql_term_SimpleTermString")
SimpleTerm = Class(name="SimpleTerm")
sql_term_SimpleTermFloat = Class(name="sql_term_SimpleTermFloat")
sql_term_SimpleTermInteger = Class(name="sql_term_SimpleTermInteger")
sql_term_SimpleTermChar = Class(name="sql_term_SimpleTermChar")
sql_term_CountStarTerm = Class(name="sql_term_CountStarTerm")
sql_term_StarTerm = Class(name="sql_term_StarTerm")

# sql_sqlDataTypes_String class attributes and methods

# DataType class attributes and methods

# sql_sqlDataTypes_DataType class attributes and methods

# sql_sqlDataTypes_Boolean class attributes and methods

# sql_sqlDataTypes_Date class attributes and methods

# sql_sqlDataTypes_Real class attributes and methods

# sql_sqlDataTypes_Integer class attributes and methods

# sql_sqlDataTypes_TimeStamp class attributes and methods

# Date class attributes and methods

# where_WhereExpression class attributes and methods

# groupBy_GroupByExpression class attributes and methods

# sql_sqlDataTypes_Float class attributes and methods

# sql_sqlDataTypes_Double class attributes and methods

# sql_select_SelectExpression class attributes and methods

# parameter_SelectParameter class attributes and methods

# column_ColumnExpression class attributes and methods

# from_FromExpression class attributes and methods

# sql_parameter_SelectParameterAll class attributes and methods

# SelectParameter class attributes and methods

# sql_parameter_SelectParameterDistinct class attributes and methods

# having_HavingExpression class attributes and methods

# set_SetExpression class attributes and methods

# orderBy_OrderByExpression class attributes and methods

# limit_LimitExpression class attributes and methods

# sql_parameter_SelectParameter class attributes and methods

# sql_column_ColumnOperationCount class attributes and methods

# ColumnOperation class attributes and methods

# sql_column_ColumnOperationMin class attributes and methods

# sql_column_ColumnOperationMax class attributes and methods

# sql_column_ColumnExpression class attributes and methods

# column_SingleColumnExpression class attributes and methods

# sql_column_SingleColumnExpression class attributes and methods
sql_column_SingleColumnExpression_alias: Property = Property(name="alias", type=StringType)
sql_column_SingleColumnExpression.attributes={sql_column_SingleColumnExpression_alias}

# expression_Expression class attributes and methods

# column_ColumnOperation class attributes and methods

# sql_column_ColumnOperation class attributes and methods

# from_Table class attributes and methods

# sql_from_Table class attributes and methods
sql_from_Table_name: Property = Property(name="name", type=StringType)
sql_from_Table.attributes={sql_from_Table_name}

# sql_column_ColumnOperationSum class attributes and methods

# sql_column_ColumnOperationAvg class attributes and methods

# sql_column_ColumnOperationEvery class attributes and methods

# sql_column_ColumnOperationSome class attributes and methods

# sql_column_Column class attributes and methods
sql_column_Column_name: Property = Property(name="name", type=StringType)
sql_column_Column.attributes={sql_column_Column_name}

# sql_from_FromExpression class attributes and methods

# from_TableListExpression class attributes and methods

# sql_from_TableExpression class attributes and methods
sql_from_TableExpression_label: Property = Property(name="label", type=StringType)
sql_from_TableExpression.attributes={sql_from_TableExpression_label}

# SelectExpression class attributes and methods

# sql_from_JoinOperation class attributes and methods

# sql_from_JoinOperationInner class attributes and methods

# JoinOperation class attributes and methods

# sql_from_TableListExpression class attributes and methods

# from_TableExpression class attributes and methods

# from_JoinTableExpression class attributes and methods

# sql_from_JoinTableExpression class attributes and methods

# from_JoinOperation class attributes and methods

# sql_orderBy_OrderByAliasExpression class attributes and methods
sql_orderBy_OrderByAliasExpression_alias: Property = Property(name="alias", type=StringType)
sql_orderBy_OrderByAliasExpression.attributes={sql_orderBy_OrderByAliasExpression_alias}

# sql_from_JoinOperationLeft class attributes and methods

# sql_from_JoinOperationRight class attributes and methods

# sql_from_JoinOperationOuter class attributes and methods

# sql_where_WhereExpression class attributes and methods

# sql_orderBy_OrderByExpression class attributes and methods

# orderBy_OrderByParameter class attributes and methods

# sql_orderBy_OrderByColumnExpression class attributes and methods

# OrderByExpression class attributes and methods

# column_Column class attributes and methods

# sql_orderBy_OrderByParameterAsc class attributes and methods

# OrderByParameter class attributes and methods

# sql_orderBy_OrderBySelectExpression class attributes and methods

# sql_orderBy_OrderByParameter class attributes and methods

# sql_groupBy_GroupByExpression class attributes and methods

# sql_orderBy_OrderByParameterDesc class attributes and methods

# sql_set_SetOperation class attributes and methods

# sql_set_SetOperationUnion class attributes and methods

# SetOperation class attributes and methods

# sql_set_SetOperationMinus class attributes and methods

# parameter_SelectParameterDistinct class attributes and methods

# sql_having_HavingExpression class attributes and methods

# sql_set_SetOperationExcept class attributes and methods

# sql_set_SetExpression class attributes and methods

# set_SetOperation class attributes and methods

# sql_expression_Expression class attributes and methods

# sql_expression_SimpleExpression class attributes and methods

# Expression class attributes and methods

# expression_AndOrExpressionOperation class attributes and methods

# condition_Condition class attributes and methods

# sql_set_SetOperationIntersect class attributes and methods

# sql_limit_LimitExpression class attributes and methods
sql_limit_LimitExpression_limit: Property = Property(name="limit", type=StringType)
sql_limit_LimitExpression_offset: Property = Property(name="offset", type=StringType)
sql_limit_LimitExpression.attributes={sql_limit_LimitExpression_offset, sql_limit_LimitExpression_limit}

# sql_expression_ExpressionOperationOr class attributes and methods

# sql_condition_Condition class attributes and methods

# sql_condition_SimpleCondition class attributes and methods

# Condition class attributes and methods

# value_Value class attributes and methods

# sql_condition_OperationCondition class attributes and methods

# SimpleCondition class attributes and methods

# expression_ExpressionOperationNot class attributes and methods

# sql_expression_ExpressionOperation class attributes and methods

# sql_expression_AndOrExpressionOperation class attributes and methods

# ExpressionOperation class attributes and methods

# sql_expression_ExpressionOperationNot class attributes and methods

# sql_expression_ExpressionOperationAnd class attributes and methods

# AndOrExpressionOperation class attributes and methods

# sql_condition_ExistsCondition class attributes and methods

# sql_condition_BetweenCondition class attributes and methods

# sql_condition_InCondition class attributes and methods

# condition_ConditionOperation class attributes and methods

# sql_condition_IsNullCondition class attributes and methods

# sql_condition_LikeCondition class attributes and methods

# sql_condition_ConditionOperation class attributes and methods

# sql_condition_ConditionOperationLesser class attributes and methods

# sql_condition_ConditionOperationLessEqual class attributes and methods

# sql_condition_ConditionOperationEqual class attributes and methods

# ConditionOperation class attributes and methods

# sql_condition_ConditionOperationGreater class attributes and methods

# sql_condition_ConditionOperationGreatEqual class attributes and methods

# sql_condition_ConditionOperationUnEqual2 class attributes and methods

# sql_value_Value class attributes and methods

# sql_value_ValueFrontOperation class attributes and methods

# ValueOperation class attributes and methods

# sql_value_ValueFrontOperationPlus class attributes and methods

# ValueFrontOperation class attributes and methods

# sql_value_ValueFrontOperationMinus class attributes and methods

# sql_value_ValueOperation class attributes and methods

# sql_value_ValueOperationMultiply class attributes and methods

# sql_condition_ConditionOperationUnEqual class attributes and methods

# sql_value_ValueOperationDivide class attributes and methods

# sql_value_ValueOperationParallel class attributes and methods

# sql_value_SimpleValue class attributes and methods

# Value class attributes and methods

# term_Term class attributes and methods

# value_ValueOperation class attributes and methods

# value_ValueFrontOperation class attributes and methods

# sql_value_ConditionValue class attributes and methods

# sql_value_FunctionValue class attributes and methods
sql_value_FunctionValue_functionName: Property = Property(name="functionName", type=StringType)
sql_value_FunctionValue.attributes={sql_value_FunctionValue_functionName}

# sql_term_Term class attributes and methods

# sql_term_BooleanTerm class attributes and methods

# Term class attributes and methods

# sql_term_BooleanTermTrue class attributes and methods

# BooleanTerm class attributes and methods

# sql_term_BooleanTermFalse class attributes and methods

# sql_term_NullTerm class attributes and methods

# sql_term_ColumnTerm class attributes and methods

# sql_term_SimpleTerm class attributes and methods
sql_term_SimpleTerm_value: Property = Property(name="value", type=StringType)
sql_term_SimpleTerm.attributes={sql_term_SimpleTerm_value}

# sql_term_SimpleTermString class attributes and methods

# SimpleTerm class attributes and methods

# sql_term_SimpleTermFloat class attributes and methods

# sql_term_SimpleTermInteger class attributes and methods

# sql_term_SimpleTermChar class attributes and methods

# sql_term_CountStarTerm class attributes and methods

# sql_term_StarTerm class attributes and methods

# Relationships
where5: BinaryAssociation = BinaryAssociation(
    name="where5",
    ends={
        Property(name="where_WhereExpression", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression6", type=where_WhereExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupBy7: BinaryAssociation = BinaryAssociation(
    name="groupBy7",
    ends={
        Property(name="groupBy_GroupByExpression", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression8", type=groupBy_GroupByExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter0: BinaryAssociation = BinaryAssociation(
    name="parameter0",
    ends={
        Property(name="parameter_SelectParameter", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression", type=parameter_SelectParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="column_ColumnExpression", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression2", type=column_ColumnExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from_3: BinaryAssociation = BinaryAssociation(
    name="from_3",
    ends={
        Property(name="from_FromExpression", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression4", type=from_FromExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
having9: BinaryAssociation = BinaryAssociation(
    name="having9",
    ends={
        Property(name="having_HavingExpression", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression10", type=having_HavingExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set11: BinaryAssociation = BinaryAssociation(
    name="set11",
    ends={
        Property(name="set_SetExpression", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression12", type=set_SetExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderBy13: BinaryAssociation = BinaryAssociation(
    name="orderBy13",
    ends={
        Property(name="orderBy_OrderByExpression", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression14", type=orderBy_OrderByExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limit15: BinaryAssociation = BinaryAssociation(
    name="limit15",
    ends={
        Property(name="limit_LimitExpression", type=sql_select_SelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_select_SelectExpression16", type=limit_LimitExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnExpressions17: BinaryAssociation = BinaryAssociation(
    name="columnExpressions17",
    ends={
        Property(name="column_SingleColumnExpression", type=sql_column_ColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_column_ColumnExpression", type=column_SingleColumnExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression18: BinaryAssociation = BinaryAssociation(
    name="expression18",
    ends={
        Property(name="expression_Expression", type=sql_column_SingleColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_column_SingleColumnExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation19: BinaryAssociation = BinaryAssociation(
    name="operation19",
    ends={
        Property(name="column_ColumnOperation", type=sql_column_SingleColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_column_SingleColumnExpression20", type=column_ColumnOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter21: BinaryAssociation = BinaryAssociation(
    name="parameter21",
    ends={
        Property(name="parameter_SelectParameter23", type=sql_column_SingleColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_column_SingleColumnExpression22", type=parameter_SelectParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table26: BinaryAssociation = BinaryAssociation(
    name="table26",
    ends={
        Property(name="from_Table", type=sql_from_TableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_from_TableExpression27", type=from_Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tables24: BinaryAssociation = BinaryAssociation(
    name="tables24",
    ends={
        Property(name="from_TableListExpression", type=sql_from_FromExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_from_FromExpression", type=from_TableListExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
selectExpression25: BinaryAssociation = BinaryAssociation(
    name="selectExpression25",
    ends={
        Property(name="SelectExpression", type=sql_from_TableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_from_TableExpression", type=SelectExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression35: BinaryAssociation = BinaryAssociation(
    name="expression35",
    ends={
        Property(name="sql_from_JoinTableExpression36", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="expression_Expression37", type=sql_from_JoinTableExpression, multiplicity=Multiplicity(1, 1))
    }
)
table28: BinaryAssociation = BinaryAssociation(
    name="table28",
    ends={
        Property(name="from_TableExpression", type=sql_from_TableListExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_from_TableListExpression", type=from_TableExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
joinTable29: BinaryAssociation = BinaryAssociation(
    name="joinTable29",
    ends={
        Property(name="from_JoinTableExpression", type=sql_from_TableListExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_from_TableListExpression30", type=from_JoinTableExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
join31: BinaryAssociation = BinaryAssociation(
    name="join31",
    ends={
        Property(name="from_JoinOperation", type=sql_from_JoinTableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_from_JoinTableExpression", type=from_JoinOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
joinTable32: BinaryAssociation = BinaryAssociation(
    name="joinTable32",
    ends={
        Property(name="from_TableExpression34", type=sql_from_JoinTableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_from_JoinTableExpression33", type=from_TableExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columnReference41: BinaryAssociation = BinaryAssociation(
    name="columnReference41",
    ends={
        Property(name="column_Column", type=sql_orderBy_OrderByColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_orderBy_OrderByColumnExpression", type=column_Column, multiplicity=Multiplicity(1, 1))
    }
)
expression38: BinaryAssociation = BinaryAssociation(
    name="expression38",
    ends={
        Property(name="expression_Expression39", type=sql_where_WhereExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_where_WhereExpression", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter40: BinaryAssociation = BinaryAssociation(
    name="parameter40",
    ends={
        Property(name="orderBy_OrderByParameter", type=sql_orderBy_OrderByExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_orderBy_OrderByExpression", type=orderBy_OrderByParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectExpression42: BinaryAssociation = BinaryAssociation(
    name="selectExpression42",
    ends={
        Property(name="SelectExpression43", type=sql_orderBy_OrderBySelectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_orderBy_OrderBySelectExpression", type=SelectExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selectParameter52: BinaryAssociation = BinaryAssociation(
    name="selectParameter52",
    ends={
        Property(name="parameter_SelectParameter53", type=sql_set_SetOperationUnion, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_set_SetOperationUnion", type=parameter_SelectParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression44: BinaryAssociation = BinaryAssociation(
    name="expression44",
    ends={
        Property(name="expression_Expression45", type=sql_groupBy_GroupByExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_groupBy_GroupByExpression", type=expression_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
selectParameter54: BinaryAssociation = BinaryAssociation(
    name="selectParameter54",
    ends={
        Property(name="parameter_SelectParameterDistinct", type=sql_set_SetOperationMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_set_SetOperationMinus", type=parameter_SelectParameterDistinct, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression46: BinaryAssociation = BinaryAssociation(
    name="expression46",
    ends={
        Property(name="expression_Expression47", type=sql_having_HavingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_having_HavingExpression", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selectExpression48: BinaryAssociation = BinaryAssociation(
    name="selectExpression48",
    ends={
        Property(name="SelectExpression49", type=sql_set_SetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_set_SetExpression", type=SelectExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
setOperation50: BinaryAssociation = BinaryAssociation(
    name="setOperation50",
    ends={
        Property(name="set_SetOperation", type=sql_set_SetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_set_SetExpression51", type=set_SetOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations59: BinaryAssociation = BinaryAssociation(
    name="operations59",
    ends={
        Property(name="expression_AndOrExpressionOperation", type=sql_expression_SimpleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_expression_SimpleExpression", type=expression_AndOrExpressionOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditions60: BinaryAssociation = BinaryAssociation(
    name="conditions60",
    ends={
        Property(name="condition_Condition", type=sql_expression_SimpleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_expression_SimpleExpression61", type=condition_Condition, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
selectParameter55: BinaryAssociation = BinaryAssociation(
    name="selectParameter55",
    ends={
        Property(name="parameter_SelectParameterDistinct56", type=sql_set_SetOperationExcept, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_set_SetOperationExcept", type=parameter_SelectParameterDistinct, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectParameter57: BinaryAssociation = BinaryAssociation(
    name="selectParameter57",
    ends={
        Property(name="parameter_SelectParameterDistinct58", type=sql_set_SetOperationIntersect, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_set_SetOperationIntersect", type=parameter_SelectParameterDistinct, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values64: BinaryAssociation = BinaryAssociation(
    name="values64",
    ends={
        Property(name="value_Value", type=sql_condition_SimpleCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_condition_SimpleCondition", type=value_Value, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
notOperation62: BinaryAssociation = BinaryAssociation(
    name="notOperation62",
    ends={
        Property(name="expression_ExpressionOperationNot", type=sql_expression_SimpleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_expression_SimpleExpression63", type=expression_ExpressionOperationNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectExpression68: BinaryAssociation = BinaryAssociation(
    name="selectExpression68",
    ends={
        Property(name="SelectExpression69", type=sql_condition_ExistsCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_condition_ExistsCondition", type=SelectExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation65: BinaryAssociation = BinaryAssociation(
    name="operation65",
    ends={
        Property(name="condition_ConditionOperation", type=sql_condition_OperationCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_condition_OperationCondition", type=condition_ConditionOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operationNot66: BinaryAssociation = BinaryAssociation(
    name="operationNot66",
    ends={
        Property(name="expression_ExpressionOperationNot67", type=sql_condition_IsNullCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_condition_IsNullCondition", type=expression_ExpressionOperationNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationNot72: BinaryAssociation = BinaryAssociation(
    name="operationNot72",
    ends={
        Property(name="expression_ExpressionOperationNot74", type=sql_condition_InCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_condition_InCondition73", type=expression_ExpressionOperationNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectExpression70: BinaryAssociation = BinaryAssociation(
    name="selectExpression70",
    ends={
        Property(name="SelectExpression71", type=sql_condition_InCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_condition_InCondition", type=SelectExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operationNot75: BinaryAssociation = BinaryAssociation(
    name="operationNot75",
    ends={
        Property(name="expression_ExpressionOperationNot76", type=sql_condition_LikeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_condition_LikeCondition", type=expression_ExpressionOperationNot, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms77: BinaryAssociation = BinaryAssociation(
    name="terms77",
    ends={
        Property(name="term_Term", type=sql_value_SimpleValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_value_SimpleValue", type=term_Term, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
operations78: BinaryAssociation = BinaryAssociation(
    name="operations78",
    ends={
        Property(name="value_ValueOperation", type=sql_value_SimpleValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_value_SimpleValue79", type=value_ValueOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
frontOperation80: BinaryAssociation = BinaryAssociation(
    name="frontOperation80",
    ends={
        Property(name="value_ValueFrontOperation", type=sql_value_SimpleValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_value_SimpleValue81", type=value_ValueFrontOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition82: BinaryAssociation = BinaryAssociation(
    name="condition82",
    ends={
        Property(name="condition_Condition83", type=sql_value_ConditionValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_value_ConditionValue", type=condition_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters84: BinaryAssociation = BinaryAssociation(
    name="parameters84",
    ends={
        Property(name="value_Value85", type=sql_value_FunctionValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_value_FunctionValue", type=value_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableReference86: BinaryAssociation = BinaryAssociation(
    name="tableReference86",
    ends={
        Property(name="from_Table87", type=sql_term_ColumnTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_term_ColumnTerm", type=from_Table, multiplicity=Multiplicity(0, 1))
    }
)
column88: BinaryAssociation = BinaryAssociation(
    name="column88",
    ends={
        Property(name="column_Column90", type=sql_term_ColumnTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_term_ColumnTerm89", type=column_Column, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnReference91: BinaryAssociation = BinaryAssociation(
    name="columnReference91",
    ends={
        Property(name="column_Column93", type=sql_term_ColumnTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="sql_term_ColumnTerm92", type=column_Column, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sql_sqlDataTypes_String_DataType = Generalization(general=DataType, specific=sql_sqlDataTypes_String)
gen_sql_sqlDataTypes_Boolean_DataType = Generalization(general=DataType, specific=sql_sqlDataTypes_Boolean)
gen_sql_sqlDataTypes_Real_DataType = Generalization(general=DataType, specific=sql_sqlDataTypes_Real)
gen_sql_sqlDataTypes_Date_DataType = Generalization(general=DataType, specific=sql_sqlDataTypes_Date)
gen_sql_sqlDataTypes_TimeStamp_Date = Generalization(general=Date, specific=sql_sqlDataTypes_TimeStamp)
gen_sql_sqlDataTypes_Integer_DataType = Generalization(general=DataType, specific=sql_sqlDataTypes_Integer)
gen_sql_sqlDataTypes_Float_DataType = Generalization(general=DataType, specific=sql_sqlDataTypes_Float)
gen_sql_sqlDataTypes_Double_DataType = Generalization(general=DataType, specific=sql_sqlDataTypes_Double)
gen_sql_parameter_SelectParameterAll_SelectParameter = Generalization(general=SelectParameter, specific=sql_parameter_SelectParameterAll)
gen_sql_parameter_SelectParameterDistinct_SelectParameter = Generalization(general=SelectParameter, specific=sql_parameter_SelectParameterDistinct)
gen_sql_column_ColumnOperationCount_ColumnOperation = Generalization(general=ColumnOperation, specific=sql_column_ColumnOperationCount)
gen_sql_column_ColumnOperationMin_ColumnOperation = Generalization(general=ColumnOperation, specific=sql_column_ColumnOperationMin)
gen_sql_column_ColumnOperationMax_ColumnOperation = Generalization(general=ColumnOperation, specific=sql_column_ColumnOperationMax)
gen_sql_column_ColumnOperationSum_ColumnOperation = Generalization(general=ColumnOperation, specific=sql_column_ColumnOperationSum)
gen_sql_column_ColumnOperationAvg_ColumnOperation = Generalization(general=ColumnOperation, specific=sql_column_ColumnOperationAvg)
gen_sql_column_ColumnOperationEvery_ColumnOperation = Generalization(general=ColumnOperation, specific=sql_column_ColumnOperationEvery)
gen_sql_column_ColumnOperationSome_ColumnOperation = Generalization(general=ColumnOperation, specific=sql_column_ColumnOperationSome)
gen_sql_from_JoinOperationInner_JoinOperation = Generalization(general=JoinOperation, specific=sql_from_JoinOperationInner)
gen_sql_orderBy_OrderByAliasExpression_OrderByExpression = Generalization(general=OrderByExpression, specific=sql_orderBy_OrderByAliasExpression)
gen_sql_from_JoinOperationLeft_JoinOperation = Generalization(general=JoinOperation, specific=sql_from_JoinOperationLeft)
gen_sql_from_JoinOperationRight_JoinOperation = Generalization(general=JoinOperation, specific=sql_from_JoinOperationRight)
gen_sql_from_JoinOperationOuter_JoinOperation = Generalization(general=JoinOperation, specific=sql_from_JoinOperationOuter)
gen_sql_orderBy_OrderByColumnExpression_OrderByExpression = Generalization(general=OrderByExpression, specific=sql_orderBy_OrderByColumnExpression)
gen_sql_orderBy_OrderByParameterAsc_OrderByParameter = Generalization(general=OrderByParameter, specific=sql_orderBy_OrderByParameterAsc)
gen_sql_orderBy_OrderBySelectExpression_OrderByExpression = Generalization(general=OrderByExpression, specific=sql_orderBy_OrderBySelectExpression)
gen_sql_orderBy_OrderByParameterDesc_OrderByParameter = Generalization(general=OrderByParameter, specific=sql_orderBy_OrderByParameterDesc)
gen_sql_set_SetOperationUnion_SetOperation = Generalization(general=SetOperation, specific=sql_set_SetOperationUnion)
gen_sql_set_SetOperationMinus_SetOperation = Generalization(general=SetOperation, specific=sql_set_SetOperationMinus)
gen_sql_set_SetOperationExcept_SetOperation = Generalization(general=SetOperation, specific=sql_set_SetOperationExcept)
gen_sql_expression_SimpleExpression_Expression = Generalization(general=Expression, specific=sql_expression_SimpleExpression)
gen_sql_set_SetOperationIntersect_SetOperation = Generalization(general=SetOperation, specific=sql_set_SetOperationIntersect)
gen_sql_expression_ExpressionOperationOr_AndOrExpressionOperation = Generalization(general=AndOrExpressionOperation, specific=sql_expression_ExpressionOperationOr)
gen_sql_condition_SimpleCondition_Condition = Generalization(general=Condition, specific=sql_condition_SimpleCondition)
gen_sql_expression_AndOrExpressionOperation_ExpressionOperation = Generalization(general=ExpressionOperation, specific=sql_expression_AndOrExpressionOperation)
gen_sql_expression_ExpressionOperationNot_ExpressionOperation = Generalization(general=ExpressionOperation, specific=sql_expression_ExpressionOperationNot)
gen_sql_expression_ExpressionOperationAnd_AndOrExpressionOperation = Generalization(general=AndOrExpressionOperation, specific=sql_expression_ExpressionOperationAnd)
gen_sql_condition_ExistsCondition_SimpleCondition = Generalization(general=SimpleCondition, specific=sql_condition_ExistsCondition)
gen_sql_condition_BetweenCondition_SimpleCondition = Generalization(general=SimpleCondition, specific=sql_condition_BetweenCondition)
gen_sql_condition_InCondition_SimpleCondition = Generalization(general=SimpleCondition, specific=sql_condition_InCondition)
gen_sql_condition_OperationCondition_SimpleCondition = Generalization(general=SimpleCondition, specific=sql_condition_OperationCondition)
gen_sql_condition_IsNullCondition_SimpleCondition = Generalization(general=SimpleCondition, specific=sql_condition_IsNullCondition)
gen_sql_condition_LikeCondition_SimpleCondition = Generalization(general=SimpleCondition, specific=sql_condition_LikeCondition)
gen_sql_condition_ConditionOperationLesser_ConditionOperation = Generalization(general=ConditionOperation, specific=sql_condition_ConditionOperationLesser)
gen_sql_condition_ConditionOperationEqual_ConditionOperation = Generalization(general=ConditionOperation, specific=sql_condition_ConditionOperationEqual)
gen_sql_condition_ConditionOperationGreater_ConditionOperation = Generalization(general=ConditionOperation, specific=sql_condition_ConditionOperationGreater)
gen_sql_condition_ConditionOperationGreatEqual_ConditionOperation = Generalization(general=ConditionOperation, specific=sql_condition_ConditionOperationGreatEqual)
gen_sql_condition_ConditionOperationLessEqual_ConditionOperation = Generalization(general=ConditionOperation, specific=sql_condition_ConditionOperationLessEqual)
gen_sql_condition_ConditionOperationUnEqual_ConditionOperation = Generalization(general=ConditionOperation, specific=sql_condition_ConditionOperationUnEqual)
gen_sql_condition_ConditionOperationUnEqual2_ConditionOperation = Generalization(general=ConditionOperation, specific=sql_condition_ConditionOperationUnEqual2)
gen_sql_value_ValueFrontOperation_ValueOperation = Generalization(general=ValueOperation, specific=sql_value_ValueFrontOperation)
gen_sql_value_ValueFrontOperationPlus_ValueFrontOperation = Generalization(general=ValueFrontOperation, specific=sql_value_ValueFrontOperationPlus)
gen_sql_value_ValueFrontOperationMinus_ValueFrontOperation = Generalization(general=ValueFrontOperation, specific=sql_value_ValueFrontOperationMinus)
gen_sql_value_ValueOperationMultiply_ValueOperation = Generalization(general=ValueOperation, specific=sql_value_ValueOperationMultiply)
gen_sql_value_ValueOperationParallel_ValueOperation = Generalization(general=ValueOperation, specific=sql_value_ValueOperationParallel)
gen_sql_value_SimpleValue_Value = Generalization(general=Value, specific=sql_value_SimpleValue)
gen_sql_value_ConditionValue_Value = Generalization(general=Value, specific=sql_value_ConditionValue)
gen_sql_value_FunctionValue_Value = Generalization(general=Value, specific=sql_value_FunctionValue)
gen_sql_value_ValueOperationDivide_ValueOperation = Generalization(general=ValueOperation, specific=sql_value_ValueOperationDivide)
gen_sql_term_BooleanTerm_Term = Generalization(general=Term, specific=sql_term_BooleanTerm)
gen_sql_term_BooleanTermTrue_BooleanTerm = Generalization(general=BooleanTerm, specific=sql_term_BooleanTermTrue)
gen_sql_term_BooleanTermFalse_BooleanTerm = Generalization(general=BooleanTerm, specific=sql_term_BooleanTermFalse)
gen_sql_term_NullTerm_Term = Generalization(general=Term, specific=sql_term_NullTerm)
gen_sql_term_ColumnTerm_Term = Generalization(general=Term, specific=sql_term_ColumnTerm)
gen_sql_term_SimpleTerm_Term = Generalization(general=Term, specific=sql_term_SimpleTerm)
gen_sql_term_SimpleTermString_SimpleTerm = Generalization(general=SimpleTerm, specific=sql_term_SimpleTermString)
gen_sql_term_SimpleTermFloat_SimpleTerm = Generalization(general=SimpleTerm, specific=sql_term_SimpleTermFloat)
gen_sql_term_SimpleTermInteger_SimpleTerm = Generalization(general=SimpleTerm, specific=sql_term_SimpleTermInteger)
gen_sql_term_SimpleTermChar_SimpleTerm = Generalization(general=SimpleTerm, specific=sql_term_SimpleTermChar)
gen_sql_term_CountStarTerm_Term = Generalization(general=Term, specific=sql_term_CountStarTerm)
gen_sql_term_StarTerm_Term = Generalization(general=Term, specific=sql_term_StarTerm)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_sqlDataTypes_String, DataType, sql_sqlDataTypes_DataType, sql_sqlDataTypes_Boolean, sql_sqlDataTypes_Date, sql_sqlDataTypes_Real, sql_sqlDataTypes_Integer, sql_sqlDataTypes_TimeStamp, Date, where_WhereExpression, groupBy_GroupByExpression, sql_sqlDataTypes_Float, sql_sqlDataTypes_Double, sql_select_SelectExpression, parameter_SelectParameter, column_ColumnExpression, from_FromExpression, sql_parameter_SelectParameterAll, SelectParameter, sql_parameter_SelectParameterDistinct, having_HavingExpression, set_SetExpression, orderBy_OrderByExpression, limit_LimitExpression, sql_parameter_SelectParameter, sql_column_ColumnOperationCount, ColumnOperation, sql_column_ColumnOperationMin, sql_column_ColumnOperationMax, sql_column_ColumnExpression, column_SingleColumnExpression, sql_column_SingleColumnExpression, expression_Expression, column_ColumnOperation, sql_column_ColumnOperation, from_Table, sql_from_Table, sql_column_ColumnOperationSum, sql_column_ColumnOperationAvg, sql_column_ColumnOperationEvery, sql_column_ColumnOperationSome, sql_column_Column, sql_from_FromExpression, from_TableListExpression, sql_from_TableExpression, SelectExpression, sql_from_JoinOperation, sql_from_JoinOperationInner, JoinOperation, sql_from_TableListExpression, from_TableExpression, from_JoinTableExpression, sql_from_JoinTableExpression, from_JoinOperation, sql_orderBy_OrderByAliasExpression, sql_from_JoinOperationLeft, sql_from_JoinOperationRight, sql_from_JoinOperationOuter, sql_where_WhereExpression, sql_orderBy_OrderByExpression, orderBy_OrderByParameter, sql_orderBy_OrderByColumnExpression, OrderByExpression, column_Column, sql_orderBy_OrderByParameterAsc, OrderByParameter, sql_orderBy_OrderBySelectExpression, sql_orderBy_OrderByParameter, sql_groupBy_GroupByExpression, sql_orderBy_OrderByParameterDesc, sql_set_SetOperation, sql_set_SetOperationUnion, SetOperation, sql_set_SetOperationMinus, parameter_SelectParameterDistinct, sql_having_HavingExpression, sql_set_SetOperationExcept, sql_set_SetExpression, set_SetOperation, sql_expression_Expression, sql_expression_SimpleExpression, Expression, expression_AndOrExpressionOperation, condition_Condition, sql_set_SetOperationIntersect, sql_limit_LimitExpression, sql_expression_ExpressionOperationOr, sql_condition_Condition, sql_condition_SimpleCondition, Condition, value_Value, sql_condition_OperationCondition, SimpleCondition, expression_ExpressionOperationNot, sql_expression_ExpressionOperation, sql_expression_AndOrExpressionOperation, ExpressionOperation, sql_expression_ExpressionOperationNot, sql_expression_ExpressionOperationAnd, AndOrExpressionOperation, sql_condition_ExistsCondition, sql_condition_BetweenCondition, sql_condition_InCondition, condition_ConditionOperation, sql_condition_IsNullCondition, sql_condition_LikeCondition, sql_condition_ConditionOperation, sql_condition_ConditionOperationLesser, sql_condition_ConditionOperationLessEqual, sql_condition_ConditionOperationEqual, ConditionOperation, sql_condition_ConditionOperationGreater, sql_condition_ConditionOperationGreatEqual, sql_condition_ConditionOperationUnEqual2, sql_value_Value, sql_value_ValueFrontOperation, ValueOperation, sql_value_ValueFrontOperationPlus, ValueFrontOperation, sql_value_ValueFrontOperationMinus, sql_value_ValueOperation, sql_value_ValueOperationMultiply, sql_condition_ConditionOperationUnEqual, sql_value_ValueOperationDivide, sql_value_ValueOperationParallel, sql_value_SimpleValue, Value, term_Term, value_ValueOperation, value_ValueFrontOperation, sql_value_ConditionValue, sql_value_FunctionValue, sql_term_Term, sql_term_BooleanTerm, Term, sql_term_BooleanTermTrue, BooleanTerm, sql_term_BooleanTermFalse, sql_term_NullTerm, sql_term_ColumnTerm, sql_term_SimpleTerm, sql_term_SimpleTermString, SimpleTerm, sql_term_SimpleTermFloat, sql_term_SimpleTermInteger, sql_term_SimpleTermChar, sql_term_CountStarTerm, sql_term_StarTerm},
    associations={where5, groupBy7, parameter0, columns1, from_3, having9, set11, orderBy13, limit15, columnExpressions17, expression18, operation19, parameter21, table26, tables24, selectExpression25, expression35, table28, joinTable29, join31, joinTable32, columnReference41, expression38, parameter40, selectExpression42, selectParameter52, expression44, selectParameter54, expression46, selectExpression48, setOperation50, operations59, conditions60, selectParameter55, selectParameter57, values64, notOperation62, selectExpression68, operation65, operationNot66, operationNot72, selectExpression70, operationNot75, terms77, operations78, frontOperation80, condition82, parameters84, tableReference86, column88, columnReference91},
    generalizations={gen_sql_sqlDataTypes_String_DataType, gen_sql_sqlDataTypes_Boolean_DataType, gen_sql_sqlDataTypes_Real_DataType, gen_sql_sqlDataTypes_Date_DataType, gen_sql_sqlDataTypes_TimeStamp_Date, gen_sql_sqlDataTypes_Integer_DataType, gen_sql_sqlDataTypes_Float_DataType, gen_sql_sqlDataTypes_Double_DataType, gen_sql_parameter_SelectParameterAll_SelectParameter, gen_sql_parameter_SelectParameterDistinct_SelectParameter, gen_sql_column_ColumnOperationCount_ColumnOperation, gen_sql_column_ColumnOperationMin_ColumnOperation, gen_sql_column_ColumnOperationMax_ColumnOperation, gen_sql_column_ColumnOperationSum_ColumnOperation, gen_sql_column_ColumnOperationAvg_ColumnOperation, gen_sql_column_ColumnOperationEvery_ColumnOperation, gen_sql_column_ColumnOperationSome_ColumnOperation, gen_sql_from_JoinOperationInner_JoinOperation, gen_sql_orderBy_OrderByAliasExpression_OrderByExpression, gen_sql_from_JoinOperationLeft_JoinOperation, gen_sql_from_JoinOperationRight_JoinOperation, gen_sql_from_JoinOperationOuter_JoinOperation, gen_sql_orderBy_OrderByColumnExpression_OrderByExpression, gen_sql_orderBy_OrderByParameterAsc_OrderByParameter, gen_sql_orderBy_OrderBySelectExpression_OrderByExpression, gen_sql_orderBy_OrderByParameterDesc_OrderByParameter, gen_sql_set_SetOperationUnion_SetOperation, gen_sql_set_SetOperationMinus_SetOperation, gen_sql_set_SetOperationExcept_SetOperation, gen_sql_expression_SimpleExpression_Expression, gen_sql_set_SetOperationIntersect_SetOperation, gen_sql_expression_ExpressionOperationOr_AndOrExpressionOperation, gen_sql_condition_SimpleCondition_Condition, gen_sql_expression_AndOrExpressionOperation_ExpressionOperation, gen_sql_expression_ExpressionOperationNot_ExpressionOperation, gen_sql_expression_ExpressionOperationAnd_AndOrExpressionOperation, gen_sql_condition_ExistsCondition_SimpleCondition, gen_sql_condition_BetweenCondition_SimpleCondition, gen_sql_condition_InCondition_SimpleCondition, gen_sql_condition_OperationCondition_SimpleCondition, gen_sql_condition_IsNullCondition_SimpleCondition, gen_sql_condition_LikeCondition_SimpleCondition, gen_sql_condition_ConditionOperationLesser_ConditionOperation, gen_sql_condition_ConditionOperationEqual_ConditionOperation, gen_sql_condition_ConditionOperationGreater_ConditionOperation, gen_sql_condition_ConditionOperationGreatEqual_ConditionOperation, gen_sql_condition_ConditionOperationLessEqual_ConditionOperation, gen_sql_condition_ConditionOperationUnEqual_ConditionOperation, gen_sql_condition_ConditionOperationUnEqual2_ConditionOperation, gen_sql_value_ValueFrontOperation_ValueOperation, gen_sql_value_ValueFrontOperationPlus_ValueFrontOperation, gen_sql_value_ValueFrontOperationMinus_ValueFrontOperation, gen_sql_value_ValueOperationMultiply_ValueOperation, gen_sql_value_ValueOperationParallel_ValueOperation, gen_sql_value_SimpleValue_Value, gen_sql_value_ConditionValue_Value, gen_sql_value_FunctionValue_Value, gen_sql_value_ValueOperationDivide_ValueOperation, gen_sql_term_BooleanTerm_Term, gen_sql_term_BooleanTermTrue_BooleanTerm, gen_sql_term_BooleanTermFalse_BooleanTerm, gen_sql_term_NullTerm_Term, gen_sql_term_ColumnTerm_Term, gen_sql_term_SimpleTerm_Term, gen_sql_term_SimpleTermString_SimpleTerm, gen_sql_term_SimpleTermFloat_SimpleTerm, gen_sql_term_SimpleTermInteger_SimpleTerm, gen_sql_term_SimpleTermChar_SimpleTerm, gen_sql_term_CountStarTerm_Term, gen_sql_term_StarTerm_Term},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)