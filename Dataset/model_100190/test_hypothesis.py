import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SimpleTerm,
    sql_term_SimpleTermChar,
    sql_term_SimpleTermInteger,
    sql_term_SimpleTermFloat,
    sql_term_SimpleTermString,
    BooleanTerm,
    sql_term_BooleanTermFalse,
    sql_term_BooleanTermTrue,
    Term,
    sql_term_NullTerm,
    sql_term_ColumnTerm,
    sql_term_SimpleTerm,
    sql_term_CountStarTerm,
    sql_term_StarTerm,
    sql_term_BooleanTerm,
    sql_term_Term,
    value_ValueFrontOperation,
    value_ValueOperation,
    term_Term,
    Value,
    sql_value_FunctionValue,
    sql_value_ConditionValue,
    sql_value_SimpleValue,
    sql_value_ValueOperation,
    ValueFrontOperation,
    sql_value_ValueFrontOperationMinus,
    sql_value_ValueFrontOperationPlus,
    ValueOperation,
    sql_value_ValueOperationMultiply,
    sql_value_ValueOperationParallel,
    sql_value_ValueOperationDivide,
    sql_value_ValueFrontOperation,
    sql_value_Value,
    ConditionOperation,
    sql_condition_ConditionOperationUnEqual2,
    sql_condition_ConditionOperationGreatEqual,
    sql_condition_ConditionOperationGreater,
    sql_condition_ConditionOperationUnEqual,
    sql_condition_ConditionOperationEqual,
    sql_condition_ConditionOperationLessEqual,
    sql_condition_ConditionOperationLesser,
    sql_condition_ConditionOperation,
    condition_ConditionOperation,
    AndOrExpressionOperation,
    sql_expression_ExpressionOperationAnd,
    ExpressionOperation,
    sql_expression_ExpressionOperationNot,
    sql_expression_AndOrExpressionOperation,
    sql_expression_ExpressionOperation,
    expression_ExpressionOperationNot,
    SimpleCondition,
    sql_condition_BetweenCondition,
    sql_condition_LikeCondition,
    sql_condition_IsNullCondition,
    sql_condition_InCondition,
    sql_condition_ExistsCondition,
    sql_condition_OperationCondition,
    value_Value,
    Condition,
    sql_condition_SimpleCondition,
    sql_condition_Condition,
    sql_expression_ExpressionOperationOr,
    sql_limit_LimitExpression,
    condition_Condition,
    expression_AndOrExpressionOperation,
    Expression,
    sql_expression_SimpleExpression,
    sql_expression_Expression,
    set_SetOperation,
    sql_set_SetExpression,
    sql_having_HavingExpression,
    parameter_SelectParameterDistinct,
    SetOperation,
    sql_set_SetOperationMinus,
    sql_set_SetOperationExcept,
    sql_set_SetOperationIntersect,
    sql_set_SetOperationUnion,
    sql_set_SetOperation,
    sql_groupBy_GroupByExpression,
    sql_orderBy_OrderByParameter,
    OrderByParameter,
    sql_orderBy_OrderByParameterDesc,
    sql_orderBy_OrderByParameterAsc,
    column_Column,
    OrderByExpression,
    sql_orderBy_OrderBySelectExpression,
    sql_orderBy_OrderByColumnExpression,
    orderBy_OrderByParameter,
    sql_orderBy_OrderByExpression,
    sql_where_WhereExpression,
    sql_orderBy_OrderByAliasExpression,
    from_JoinOperation,
    sql_from_JoinTableExpression,
    from_JoinTableExpression,
    from_TableExpression,
    sql_from_TableListExpression,
    JoinOperation,
    sql_from_JoinOperationOuter,
    sql_from_JoinOperationRight,
    sql_from_JoinOperationLeft,
    sql_from_JoinOperationInner,
    sql_from_JoinOperation,
    SelectExpression,
    sql_from_TableExpression,
    from_TableListExpression,
    sql_from_FromExpression,
    sql_column_Column,
    sql_from_Table,
    from_Table,
    sql_column_ColumnOperation,
    column_ColumnOperation,
    expression_Expression,
    sql_column_SingleColumnExpression,
    column_SingleColumnExpression,
    sql_column_ColumnExpression,
    ColumnOperation,
    sql_column_ColumnOperationMax,
    sql_column_ColumnOperationAvg,
    sql_column_ColumnOperationSome,
    sql_column_ColumnOperationMin,
    sql_column_ColumnOperationEvery,
    sql_column_ColumnOperationSum,
    sql_column_ColumnOperationCount,
    sql_parameter_SelectParameter,
    limit_LimitExpression,
    orderBy_OrderByExpression,
    set_SetExpression,
    having_HavingExpression,
    SelectParameter,
    sql_parameter_SelectParameterDistinct,
    sql_parameter_SelectParameterAll,
    from_FromExpression,
    column_ColumnExpression,
    parameter_SelectParameter,
    sql_select_SelectExpression,
    groupBy_GroupByExpression,
    where_WhereExpression,
    Date,
    sql_sqlDataTypes_TimeStamp,
    sql_sqlDataTypes_DataType,
    DataType,
    sql_sqlDataTypes_Date,
    sql_sqlDataTypes_Real,
    sql_sqlDataTypes_Integer,
    sql_sqlDataTypes_Double,
    sql_sqlDataTypes_Float,
    sql_sqlDataTypes_Boolean,
    sql_sqlDataTypes_String,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleterm_is_not_abstract():
    assert not inspect.isabstract(SimpleTerm)


def test_simpleterm_constructor_exists():
    assert callable(SimpleTerm.__init__)


def test_simpleterm_constructor_args():
    sig = inspect.signature(SimpleTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_simpletermchar_is_not_abstract():
    assert not inspect.isabstract(sql_term_SimpleTermChar)


def test_sql_term_simpletermchar_constructor_exists():
    assert callable(sql_term_SimpleTermChar.__init__)


def test_sql_term_simpletermchar_constructor_args():
    sig = inspect.signature(sql_term_SimpleTermChar.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_simpleterminteger_is_not_abstract():
    assert not inspect.isabstract(sql_term_SimpleTermInteger)


def test_sql_term_simpleterminteger_constructor_exists():
    assert callable(sql_term_SimpleTermInteger.__init__)


def test_sql_term_simpleterminteger_constructor_args():
    sig = inspect.signature(sql_term_SimpleTermInteger.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_simpletermfloat_is_not_abstract():
    assert not inspect.isabstract(sql_term_SimpleTermFloat)


def test_sql_term_simpletermfloat_constructor_exists():
    assert callable(sql_term_SimpleTermFloat.__init__)


def test_sql_term_simpletermfloat_constructor_args():
    sig = inspect.signature(sql_term_SimpleTermFloat.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_simpletermstring_is_not_abstract():
    assert not inspect.isabstract(sql_term_SimpleTermString)


def test_sql_term_simpletermstring_constructor_exists():
    assert callable(sql_term_SimpleTermString.__init__)


def test_sql_term_simpletermstring_constructor_args():
    sig = inspect.signature(sql_term_SimpleTermString.__init__)
    params = list(sig.parameters.keys())



def test_booleanterm_is_not_abstract():
    assert not inspect.isabstract(BooleanTerm)


def test_booleanterm_constructor_exists():
    assert callable(BooleanTerm.__init__)


def test_booleanterm_constructor_args():
    sig = inspect.signature(BooleanTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_booleantermfalse_is_not_abstract():
    assert not inspect.isabstract(sql_term_BooleanTermFalse)


def test_sql_term_booleantermfalse_constructor_exists():
    assert callable(sql_term_BooleanTermFalse.__init__)


def test_sql_term_booleantermfalse_constructor_args():
    sig = inspect.signature(sql_term_BooleanTermFalse.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_booleantermtrue_is_not_abstract():
    assert not inspect.isabstract(sql_term_BooleanTermTrue)


def test_sql_term_booleantermtrue_constructor_exists():
    assert callable(sql_term_BooleanTermTrue.__init__)


def test_sql_term_booleantermtrue_constructor_args():
    sig = inspect.signature(sql_term_BooleanTermTrue.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_nullterm_is_not_abstract():
    assert not inspect.isabstract(sql_term_NullTerm)


def test_sql_term_nullterm_constructor_exists():
    assert callable(sql_term_NullTerm.__init__)


def test_sql_term_nullterm_constructor_args():
    sig = inspect.signature(sql_term_NullTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_columnterm_is_not_abstract():
    assert not inspect.isabstract(sql_term_ColumnTerm)


def test_sql_term_columnterm_constructor_exists():
    assert callable(sql_term_ColumnTerm.__init__)


def test_sql_term_columnterm_constructor_args():
    sig = inspect.signature(sql_term_ColumnTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_simpleterm_is_not_abstract():
    assert not inspect.isabstract(sql_term_SimpleTerm)


def test_sql_term_simpleterm_constructor_exists():
    assert callable(sql_term_SimpleTerm.__init__)


def test_sql_term_simpleterm_constructor_args():
    sig = inspect.signature(sql_term_SimpleTerm.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql_term_simpleterm_has_value():
    assert hasattr(sql_term_SimpleTerm, "value")
    descriptor = None
    for klass in sql_term_SimpleTerm.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql_term_countstarterm_is_not_abstract():
    assert not inspect.isabstract(sql_term_CountStarTerm)


def test_sql_term_countstarterm_constructor_exists():
    assert callable(sql_term_CountStarTerm.__init__)


def test_sql_term_countstarterm_constructor_args():
    sig = inspect.signature(sql_term_CountStarTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_starterm_is_not_abstract():
    assert not inspect.isabstract(sql_term_StarTerm)


def test_sql_term_starterm_constructor_exists():
    assert callable(sql_term_StarTerm.__init__)


def test_sql_term_starterm_constructor_args():
    sig = inspect.signature(sql_term_StarTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_booleanterm_is_not_abstract():
    assert not inspect.isabstract(sql_term_BooleanTerm)


def test_sql_term_booleanterm_constructor_exists():
    assert callable(sql_term_BooleanTerm.__init__)


def test_sql_term_booleanterm_constructor_args():
    sig = inspect.signature(sql_term_BooleanTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql_term_term_is_not_abstract():
    assert not inspect.isabstract(sql_term_Term)


def test_sql_term_term_constructor_exists():
    assert callable(sql_term_Term.__init__)


def test_sql_term_term_constructor_args():
    sig = inspect.signature(sql_term_Term.__init__)
    params = list(sig.parameters.keys())



def test_value_valuefrontoperation_is_not_abstract():
    assert not inspect.isabstract(value_ValueFrontOperation)


def test_value_valuefrontoperation_constructor_exists():
    assert callable(value_ValueFrontOperation.__init__)


def test_value_valuefrontoperation_constructor_args():
    sig = inspect.signature(value_ValueFrontOperation.__init__)
    params = list(sig.parameters.keys())



def test_value_valueoperation_is_not_abstract():
    assert not inspect.isabstract(value_ValueOperation)


def test_value_valueoperation_constructor_exists():
    assert callable(value_ValueOperation.__init__)


def test_value_valueoperation_constructor_args():
    sig = inspect.signature(value_ValueOperation.__init__)
    params = list(sig.parameters.keys())



def test_term_term_is_not_abstract():
    assert not inspect.isabstract(term_Term)


def test_term_term_constructor_exists():
    assert callable(term_Term.__init__)


def test_term_term_constructor_args():
    sig = inspect.signature(term_Term.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_functionvalue_is_not_abstract():
    assert not inspect.isabstract(sql_value_FunctionValue)


def test_sql_value_functionvalue_constructor_exists():
    assert callable(sql_value_FunctionValue.__init__)


def test_sql_value_functionvalue_constructor_args():
    sig = inspect.signature(sql_value_FunctionValue.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_sql_value_functionvalue_has_functionName():
    assert hasattr(sql_value_FunctionValue, "functionName")
    descriptor = None
    for klass in sql_value_FunctionValue.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_sql_value_conditionvalue_is_not_abstract():
    assert not inspect.isabstract(sql_value_ConditionValue)


def test_sql_value_conditionvalue_constructor_exists():
    assert callable(sql_value_ConditionValue.__init__)


def test_sql_value_conditionvalue_constructor_args():
    sig = inspect.signature(sql_value_ConditionValue.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_simplevalue_is_not_abstract():
    assert not inspect.isabstract(sql_value_SimpleValue)


def test_sql_value_simplevalue_constructor_exists():
    assert callable(sql_value_SimpleValue.__init__)


def test_sql_value_simplevalue_constructor_args():
    sig = inspect.signature(sql_value_SimpleValue.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_valueoperation_is_not_abstract():
    assert not inspect.isabstract(sql_value_ValueOperation)


def test_sql_value_valueoperation_constructor_exists():
    assert callable(sql_value_ValueOperation.__init__)


def test_sql_value_valueoperation_constructor_args():
    sig = inspect.signature(sql_value_ValueOperation.__init__)
    params = list(sig.parameters.keys())



def test_valuefrontoperation_is_not_abstract():
    assert not inspect.isabstract(ValueFrontOperation)


def test_valuefrontoperation_constructor_exists():
    assert callable(ValueFrontOperation.__init__)


def test_valuefrontoperation_constructor_args():
    sig = inspect.signature(ValueFrontOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_valuefrontoperationminus_is_not_abstract():
    assert not inspect.isabstract(sql_value_ValueFrontOperationMinus)


def test_sql_value_valuefrontoperationminus_constructor_exists():
    assert callable(sql_value_ValueFrontOperationMinus.__init__)


def test_sql_value_valuefrontoperationminus_constructor_args():
    sig = inspect.signature(sql_value_ValueFrontOperationMinus.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_valuefrontoperationplus_is_not_abstract():
    assert not inspect.isabstract(sql_value_ValueFrontOperationPlus)


def test_sql_value_valuefrontoperationplus_constructor_exists():
    assert callable(sql_value_ValueFrontOperationPlus.__init__)


def test_sql_value_valuefrontoperationplus_constructor_args():
    sig = inspect.signature(sql_value_ValueFrontOperationPlus.__init__)
    params = list(sig.parameters.keys())



def test_valueoperation_is_not_abstract():
    assert not inspect.isabstract(ValueOperation)


def test_valueoperation_constructor_exists():
    assert callable(ValueOperation.__init__)


def test_valueoperation_constructor_args():
    sig = inspect.signature(ValueOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_valueoperationmultiply_is_not_abstract():
    assert not inspect.isabstract(sql_value_ValueOperationMultiply)


def test_sql_value_valueoperationmultiply_constructor_exists():
    assert callable(sql_value_ValueOperationMultiply.__init__)


def test_sql_value_valueoperationmultiply_constructor_args():
    sig = inspect.signature(sql_value_ValueOperationMultiply.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_valueoperationparallel_is_not_abstract():
    assert not inspect.isabstract(sql_value_ValueOperationParallel)


def test_sql_value_valueoperationparallel_constructor_exists():
    assert callable(sql_value_ValueOperationParallel.__init__)


def test_sql_value_valueoperationparallel_constructor_args():
    sig = inspect.signature(sql_value_ValueOperationParallel.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_valueoperationdivide_is_not_abstract():
    assert not inspect.isabstract(sql_value_ValueOperationDivide)


def test_sql_value_valueoperationdivide_constructor_exists():
    assert callable(sql_value_ValueOperationDivide.__init__)


def test_sql_value_valueoperationdivide_constructor_args():
    sig = inspect.signature(sql_value_ValueOperationDivide.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_valuefrontoperation_is_not_abstract():
    assert not inspect.isabstract(sql_value_ValueFrontOperation)


def test_sql_value_valuefrontoperation_constructor_exists():
    assert callable(sql_value_ValueFrontOperation.__init__)


def test_sql_value_valuefrontoperation_constructor_args():
    sig = inspect.signature(sql_value_ValueFrontOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_value_value_is_not_abstract():
    assert not inspect.isabstract(sql_value_Value)


def test_sql_value_value_constructor_exists():
    assert callable(sql_value_Value.__init__)


def test_sql_value_value_constructor_args():
    sig = inspect.signature(sql_value_Value.__init__)
    params = list(sig.parameters.keys())



def test_conditionoperation_is_not_abstract():
    assert not inspect.isabstract(ConditionOperation)


def test_conditionoperation_constructor_exists():
    assert callable(ConditionOperation.__init__)


def test_conditionoperation_constructor_args():
    sig = inspect.signature(ConditionOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_conditionoperationunequal2_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ConditionOperationUnEqual2)


def test_sql_condition_conditionoperationunequal2_constructor_exists():
    assert callable(sql_condition_ConditionOperationUnEqual2.__init__)


def test_sql_condition_conditionoperationunequal2_constructor_args():
    sig = inspect.signature(sql_condition_ConditionOperationUnEqual2.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_conditionoperationgreatequal_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ConditionOperationGreatEqual)


def test_sql_condition_conditionoperationgreatequal_constructor_exists():
    assert callable(sql_condition_ConditionOperationGreatEqual.__init__)


def test_sql_condition_conditionoperationgreatequal_constructor_args():
    sig = inspect.signature(sql_condition_ConditionOperationGreatEqual.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_conditionoperationgreater_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ConditionOperationGreater)


def test_sql_condition_conditionoperationgreater_constructor_exists():
    assert callable(sql_condition_ConditionOperationGreater.__init__)


def test_sql_condition_conditionoperationgreater_constructor_args():
    sig = inspect.signature(sql_condition_ConditionOperationGreater.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_conditionoperationunequal_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ConditionOperationUnEqual)


def test_sql_condition_conditionoperationunequal_constructor_exists():
    assert callable(sql_condition_ConditionOperationUnEqual.__init__)


def test_sql_condition_conditionoperationunequal_constructor_args():
    sig = inspect.signature(sql_condition_ConditionOperationUnEqual.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_conditionoperationequal_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ConditionOperationEqual)


def test_sql_condition_conditionoperationequal_constructor_exists():
    assert callable(sql_condition_ConditionOperationEqual.__init__)


def test_sql_condition_conditionoperationequal_constructor_args():
    sig = inspect.signature(sql_condition_ConditionOperationEqual.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_conditionoperationlessequal_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ConditionOperationLessEqual)


def test_sql_condition_conditionoperationlessequal_constructor_exists():
    assert callable(sql_condition_ConditionOperationLessEqual.__init__)


def test_sql_condition_conditionoperationlessequal_constructor_args():
    sig = inspect.signature(sql_condition_ConditionOperationLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_conditionoperationlesser_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ConditionOperationLesser)


def test_sql_condition_conditionoperationlesser_constructor_exists():
    assert callable(sql_condition_ConditionOperationLesser.__init__)


def test_sql_condition_conditionoperationlesser_constructor_args():
    sig = inspect.signature(sql_condition_ConditionOperationLesser.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_conditionoperation_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ConditionOperation)


def test_sql_condition_conditionoperation_constructor_exists():
    assert callable(sql_condition_ConditionOperation.__init__)


def test_sql_condition_conditionoperation_constructor_args():
    sig = inspect.signature(sql_condition_ConditionOperation.__init__)
    params = list(sig.parameters.keys())



def test_condition_conditionoperation_is_not_abstract():
    assert not inspect.isabstract(condition_ConditionOperation)


def test_condition_conditionoperation_constructor_exists():
    assert callable(condition_ConditionOperation.__init__)


def test_condition_conditionoperation_constructor_args():
    sig = inspect.signature(condition_ConditionOperation.__init__)
    params = list(sig.parameters.keys())



def test_andorexpressionoperation_is_not_abstract():
    assert not inspect.isabstract(AndOrExpressionOperation)


def test_andorexpressionoperation_constructor_exists():
    assert callable(AndOrExpressionOperation.__init__)


def test_andorexpressionoperation_constructor_args():
    sig = inspect.signature(AndOrExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_expressionoperationand_is_not_abstract():
    assert not inspect.isabstract(sql_expression_ExpressionOperationAnd)


def test_sql_expression_expressionoperationand_constructor_exists():
    assert callable(sql_expression_ExpressionOperationAnd.__init__)


def test_sql_expression_expressionoperationand_constructor_args():
    sig = inspect.signature(sql_expression_ExpressionOperationAnd.__init__)
    params = list(sig.parameters.keys())



def test_expressionoperation_is_not_abstract():
    assert not inspect.isabstract(ExpressionOperation)


def test_expressionoperation_constructor_exists():
    assert callable(ExpressionOperation.__init__)


def test_expressionoperation_constructor_args():
    sig = inspect.signature(ExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_expressionoperationnot_is_not_abstract():
    assert not inspect.isabstract(sql_expression_ExpressionOperationNot)


def test_sql_expression_expressionoperationnot_constructor_exists():
    assert callable(sql_expression_ExpressionOperationNot.__init__)


def test_sql_expression_expressionoperationnot_constructor_args():
    sig = inspect.signature(sql_expression_ExpressionOperationNot.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_andorexpressionoperation_is_not_abstract():
    assert not inspect.isabstract(sql_expression_AndOrExpressionOperation)


def test_sql_expression_andorexpressionoperation_constructor_exists():
    assert callable(sql_expression_AndOrExpressionOperation.__init__)


def test_sql_expression_andorexpressionoperation_constructor_args():
    sig = inspect.signature(sql_expression_AndOrExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_expressionoperation_is_not_abstract():
    assert not inspect.isabstract(sql_expression_ExpressionOperation)


def test_sql_expression_expressionoperation_constructor_exists():
    assert callable(sql_expression_ExpressionOperation.__init__)


def test_sql_expression_expressionoperation_constructor_args():
    sig = inspect.signature(sql_expression_ExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_expression_expressionoperationnot_is_not_abstract():
    assert not inspect.isabstract(expression_ExpressionOperationNot)


def test_expression_expressionoperationnot_constructor_exists():
    assert callable(expression_ExpressionOperationNot.__init__)


def test_expression_expressionoperationnot_constructor_args():
    sig = inspect.signature(expression_ExpressionOperationNot.__init__)
    params = list(sig.parameters.keys())



def test_simplecondition_is_not_abstract():
    assert not inspect.isabstract(SimpleCondition)


def test_simplecondition_constructor_exists():
    assert callable(SimpleCondition.__init__)


def test_simplecondition_constructor_args():
    sig = inspect.signature(SimpleCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_betweencondition_is_not_abstract():
    assert not inspect.isabstract(sql_condition_BetweenCondition)


def test_sql_condition_betweencondition_constructor_exists():
    assert callable(sql_condition_BetweenCondition.__init__)


def test_sql_condition_betweencondition_constructor_args():
    sig = inspect.signature(sql_condition_BetweenCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_likecondition_is_not_abstract():
    assert not inspect.isabstract(sql_condition_LikeCondition)


def test_sql_condition_likecondition_constructor_exists():
    assert callable(sql_condition_LikeCondition.__init__)


def test_sql_condition_likecondition_constructor_args():
    sig = inspect.signature(sql_condition_LikeCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_isnullcondition_is_not_abstract():
    assert not inspect.isabstract(sql_condition_IsNullCondition)


def test_sql_condition_isnullcondition_constructor_exists():
    assert callable(sql_condition_IsNullCondition.__init__)


def test_sql_condition_isnullcondition_constructor_args():
    sig = inspect.signature(sql_condition_IsNullCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_incondition_is_not_abstract():
    assert not inspect.isabstract(sql_condition_InCondition)


def test_sql_condition_incondition_constructor_exists():
    assert callable(sql_condition_InCondition.__init__)


def test_sql_condition_incondition_constructor_args():
    sig = inspect.signature(sql_condition_InCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_existscondition_is_not_abstract():
    assert not inspect.isabstract(sql_condition_ExistsCondition)


def test_sql_condition_existscondition_constructor_exists():
    assert callable(sql_condition_ExistsCondition.__init__)


def test_sql_condition_existscondition_constructor_args():
    sig = inspect.signature(sql_condition_ExistsCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_operationcondition_is_not_abstract():
    assert not inspect.isabstract(sql_condition_OperationCondition)


def test_sql_condition_operationcondition_constructor_exists():
    assert callable(sql_condition_OperationCondition.__init__)


def test_sql_condition_operationcondition_constructor_args():
    sig = inspect.signature(sql_condition_OperationCondition.__init__)
    params = list(sig.parameters.keys())



def test_value_value_is_not_abstract():
    assert not inspect.isabstract(value_Value)


def test_value_value_constructor_exists():
    assert callable(value_Value.__init__)


def test_value_value_constructor_args():
    sig = inspect.signature(value_Value.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_simplecondition_is_not_abstract():
    assert not inspect.isabstract(sql_condition_SimpleCondition)


def test_sql_condition_simplecondition_constructor_exists():
    assert callable(sql_condition_SimpleCondition.__init__)


def test_sql_condition_simplecondition_constructor_args():
    sig = inspect.signature(sql_condition_SimpleCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql_condition_condition_is_not_abstract():
    assert not inspect.isabstract(sql_condition_Condition)


def test_sql_condition_condition_constructor_exists():
    assert callable(sql_condition_Condition.__init__)


def test_sql_condition_condition_constructor_args():
    sig = inspect.signature(sql_condition_Condition.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_expressionoperationor_is_not_abstract():
    assert not inspect.isabstract(sql_expression_ExpressionOperationOr)


def test_sql_expression_expressionoperationor_constructor_exists():
    assert callable(sql_expression_ExpressionOperationOr.__init__)


def test_sql_expression_expressionoperationor_constructor_args():
    sig = inspect.signature(sql_expression_ExpressionOperationOr.__init__)
    params = list(sig.parameters.keys())



def test_sql_limit_limitexpression_is_not_abstract():
    assert not inspect.isabstract(sql_limit_LimitExpression)


def test_sql_limit_limitexpression_constructor_exists():
    assert callable(sql_limit_LimitExpression.__init__)


def test_sql_limit_limitexpression_constructor_args():
    sig = inspect.signature(sql_limit_LimitExpression.__init__)
    params = list(sig.parameters.keys())
    assert "limit" in params, "Missing parameter 'limit'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_sql_limit_limitexpression_has_limit():
    assert hasattr(sql_limit_LimitExpression, "limit")
    descriptor = None
    for klass in sql_limit_LimitExpression.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_sql_limit_limitexpression_has_offset():
    assert hasattr(sql_limit_LimitExpression, "offset")
    descriptor = None
    for klass in sql_limit_LimitExpression.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_condition_condition_is_not_abstract():
    assert not inspect.isabstract(condition_Condition)


def test_condition_condition_constructor_exists():
    assert callable(condition_Condition.__init__)


def test_condition_condition_constructor_args():
    sig = inspect.signature(condition_Condition.__init__)
    params = list(sig.parameters.keys())



def test_expression_andorexpressionoperation_is_not_abstract():
    assert not inspect.isabstract(expression_AndOrExpressionOperation)


def test_expression_andorexpressionoperation_constructor_exists():
    assert callable(expression_AndOrExpressionOperation.__init__)


def test_expression_andorexpressionoperation_constructor_args():
    sig = inspect.signature(expression_AndOrExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(sql_expression_SimpleExpression)


def test_sql_expression_simpleexpression_constructor_exists():
    assert callable(sql_expression_SimpleExpression.__init__)


def test_sql_expression_simpleexpression_constructor_args():
    sig = inspect.signature(sql_expression_SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_expression_expression_is_not_abstract():
    assert not inspect.isabstract(sql_expression_Expression)


def test_sql_expression_expression_constructor_exists():
    assert callable(sql_expression_Expression.__init__)


def test_sql_expression_expression_constructor_args():
    sig = inspect.signature(sql_expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_set_setoperation_is_not_abstract():
    assert not inspect.isabstract(set_SetOperation)


def test_set_setoperation_constructor_exists():
    assert callable(set_SetOperation.__init__)


def test_set_setoperation_constructor_args():
    sig = inspect.signature(set_SetOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_set_setexpression_is_not_abstract():
    assert not inspect.isabstract(sql_set_SetExpression)


def test_sql_set_setexpression_constructor_exists():
    assert callable(sql_set_SetExpression.__init__)


def test_sql_set_setexpression_constructor_args():
    sig = inspect.signature(sql_set_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_having_havingexpression_is_not_abstract():
    assert not inspect.isabstract(sql_having_HavingExpression)


def test_sql_having_havingexpression_constructor_exists():
    assert callable(sql_having_HavingExpression.__init__)


def test_sql_having_havingexpression_constructor_args():
    sig = inspect.signature(sql_having_HavingExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameter_selectparameterdistinct_is_not_abstract():
    assert not inspect.isabstract(parameter_SelectParameterDistinct)


def test_parameter_selectparameterdistinct_constructor_exists():
    assert callable(parameter_SelectParameterDistinct.__init__)


def test_parameter_selectparameterdistinct_constructor_args():
    sig = inspect.signature(parameter_SelectParameterDistinct.__init__)
    params = list(sig.parameters.keys())



def test_setoperation_is_not_abstract():
    assert not inspect.isabstract(SetOperation)


def test_setoperation_constructor_exists():
    assert callable(SetOperation.__init__)


def test_setoperation_constructor_args():
    sig = inspect.signature(SetOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_set_setoperationminus_is_not_abstract():
    assert not inspect.isabstract(sql_set_SetOperationMinus)


def test_sql_set_setoperationminus_constructor_exists():
    assert callable(sql_set_SetOperationMinus.__init__)


def test_sql_set_setoperationminus_constructor_args():
    sig = inspect.signature(sql_set_SetOperationMinus.__init__)
    params = list(sig.parameters.keys())



def test_sql_set_setoperationexcept_is_not_abstract():
    assert not inspect.isabstract(sql_set_SetOperationExcept)


def test_sql_set_setoperationexcept_constructor_exists():
    assert callable(sql_set_SetOperationExcept.__init__)


def test_sql_set_setoperationexcept_constructor_args():
    sig = inspect.signature(sql_set_SetOperationExcept.__init__)
    params = list(sig.parameters.keys())



def test_sql_set_setoperationintersect_is_not_abstract():
    assert not inspect.isabstract(sql_set_SetOperationIntersect)


def test_sql_set_setoperationintersect_constructor_exists():
    assert callable(sql_set_SetOperationIntersect.__init__)


def test_sql_set_setoperationintersect_constructor_args():
    sig = inspect.signature(sql_set_SetOperationIntersect.__init__)
    params = list(sig.parameters.keys())



def test_sql_set_setoperationunion_is_not_abstract():
    assert not inspect.isabstract(sql_set_SetOperationUnion)


def test_sql_set_setoperationunion_constructor_exists():
    assert callable(sql_set_SetOperationUnion.__init__)


def test_sql_set_setoperationunion_constructor_args():
    sig = inspect.signature(sql_set_SetOperationUnion.__init__)
    params = list(sig.parameters.keys())



def test_sql_set_setoperation_is_not_abstract():
    assert not inspect.isabstract(sql_set_SetOperation)


def test_sql_set_setoperation_constructor_exists():
    assert callable(sql_set_SetOperation.__init__)


def test_sql_set_setoperation_constructor_args():
    sig = inspect.signature(sql_set_SetOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_groupby_groupbyexpression_is_not_abstract():
    assert not inspect.isabstract(sql_groupBy_GroupByExpression)


def test_sql_groupby_groupbyexpression_constructor_exists():
    assert callable(sql_groupBy_GroupByExpression.__init__)


def test_sql_groupby_groupbyexpression_constructor_args():
    sig = inspect.signature(sql_groupBy_GroupByExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderby_orderbyparameter_is_not_abstract():
    assert not inspect.isabstract(sql_orderBy_OrderByParameter)


def test_sql_orderby_orderbyparameter_constructor_exists():
    assert callable(sql_orderBy_OrderByParameter.__init__)


def test_sql_orderby_orderbyparameter_constructor_args():
    sig = inspect.signature(sql_orderBy_OrderByParameter.__init__)
    params = list(sig.parameters.keys())



def test_orderbyparameter_is_not_abstract():
    assert not inspect.isabstract(OrderByParameter)


def test_orderbyparameter_constructor_exists():
    assert callable(OrderByParameter.__init__)


def test_orderbyparameter_constructor_args():
    sig = inspect.signature(OrderByParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderby_orderbyparameterdesc_is_not_abstract():
    assert not inspect.isabstract(sql_orderBy_OrderByParameterDesc)


def test_sql_orderby_orderbyparameterdesc_constructor_exists():
    assert callable(sql_orderBy_OrderByParameterDesc.__init__)


def test_sql_orderby_orderbyparameterdesc_constructor_args():
    sig = inspect.signature(sql_orderBy_OrderByParameterDesc.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderby_orderbyparameterasc_is_not_abstract():
    assert not inspect.isabstract(sql_orderBy_OrderByParameterAsc)


def test_sql_orderby_orderbyparameterasc_constructor_exists():
    assert callable(sql_orderBy_OrderByParameterAsc.__init__)


def test_sql_orderby_orderbyparameterasc_constructor_args():
    sig = inspect.signature(sql_orderBy_OrderByParameterAsc.__init__)
    params = list(sig.parameters.keys())



def test_column_column_is_not_abstract():
    assert not inspect.isabstract(column_Column)


def test_column_column_constructor_exists():
    assert callable(column_Column.__init__)


def test_column_column_constructor_args():
    sig = inspect.signature(column_Column.__init__)
    params = list(sig.parameters.keys())



def test_orderbyexpression_is_not_abstract():
    assert not inspect.isabstract(OrderByExpression)


def test_orderbyexpression_constructor_exists():
    assert callable(OrderByExpression.__init__)


def test_orderbyexpression_constructor_args():
    sig = inspect.signature(OrderByExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderby_orderbyselectexpression_is_not_abstract():
    assert not inspect.isabstract(sql_orderBy_OrderBySelectExpression)


def test_sql_orderby_orderbyselectexpression_constructor_exists():
    assert callable(sql_orderBy_OrderBySelectExpression.__init__)


def test_sql_orderby_orderbyselectexpression_constructor_args():
    sig = inspect.signature(sql_orderBy_OrderBySelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderby_orderbycolumnexpression_is_not_abstract():
    assert not inspect.isabstract(sql_orderBy_OrderByColumnExpression)


def test_sql_orderby_orderbycolumnexpression_constructor_exists():
    assert callable(sql_orderBy_OrderByColumnExpression.__init__)


def test_sql_orderby_orderbycolumnexpression_constructor_args():
    sig = inspect.signature(sql_orderBy_OrderByColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_orderby_orderbyparameter_is_not_abstract():
    assert not inspect.isabstract(orderBy_OrderByParameter)


def test_orderby_orderbyparameter_constructor_exists():
    assert callable(orderBy_OrderByParameter.__init__)


def test_orderby_orderbyparameter_constructor_args():
    sig = inspect.signature(orderBy_OrderByParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderby_orderbyexpression_is_not_abstract():
    assert not inspect.isabstract(sql_orderBy_OrderByExpression)


def test_sql_orderby_orderbyexpression_constructor_exists():
    assert callable(sql_orderBy_OrderByExpression.__init__)


def test_sql_orderby_orderbyexpression_constructor_args():
    sig = inspect.signature(sql_orderBy_OrderByExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_where_whereexpression_is_not_abstract():
    assert not inspect.isabstract(sql_where_WhereExpression)


def test_sql_where_whereexpression_constructor_exists():
    assert callable(sql_where_WhereExpression.__init__)


def test_sql_where_whereexpression_constructor_args():
    sig = inspect.signature(sql_where_WhereExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_orderby_orderbyaliasexpression_is_not_abstract():
    assert not inspect.isabstract(sql_orderBy_OrderByAliasExpression)


def test_sql_orderby_orderbyaliasexpression_constructor_exists():
    assert callable(sql_orderBy_OrderByAliasExpression.__init__)


def test_sql_orderby_orderbyaliasexpression_constructor_args():
    sig = inspect.signature(sql_orderBy_OrderByAliasExpression.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sql_orderby_orderbyaliasexpression_has_alias():
    assert hasattr(sql_orderBy_OrderByAliasExpression, "alias")
    descriptor = None
    for klass in sql_orderBy_OrderByAliasExpression.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_from_joinoperation_is_not_abstract():
    assert not inspect.isabstract(from_JoinOperation)


def test_from_joinoperation_constructor_exists():
    assert callable(from_JoinOperation.__init__)


def test_from_joinoperation_constructor_args():
    sig = inspect.signature(from_JoinOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_jointableexpression_is_not_abstract():
    assert not inspect.isabstract(sql_from_JoinTableExpression)


def test_sql_from_jointableexpression_constructor_exists():
    assert callable(sql_from_JoinTableExpression.__init__)


def test_sql_from_jointableexpression_constructor_args():
    sig = inspect.signature(sql_from_JoinTableExpression.__init__)
    params = list(sig.parameters.keys())



def test_from_jointableexpression_is_not_abstract():
    assert not inspect.isabstract(from_JoinTableExpression)


def test_from_jointableexpression_constructor_exists():
    assert callable(from_JoinTableExpression.__init__)


def test_from_jointableexpression_constructor_args():
    sig = inspect.signature(from_JoinTableExpression.__init__)
    params = list(sig.parameters.keys())



def test_from_tableexpression_is_not_abstract():
    assert not inspect.isabstract(from_TableExpression)


def test_from_tableexpression_constructor_exists():
    assert callable(from_TableExpression.__init__)


def test_from_tableexpression_constructor_args():
    sig = inspect.signature(from_TableExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_tablelistexpression_is_not_abstract():
    assert not inspect.isabstract(sql_from_TableListExpression)


def test_sql_from_tablelistexpression_constructor_exists():
    assert callable(sql_from_TableListExpression.__init__)


def test_sql_from_tablelistexpression_constructor_args():
    sig = inspect.signature(sql_from_TableListExpression.__init__)
    params = list(sig.parameters.keys())



def test_joinoperation_is_not_abstract():
    assert not inspect.isabstract(JoinOperation)


def test_joinoperation_constructor_exists():
    assert callable(JoinOperation.__init__)


def test_joinoperation_constructor_args():
    sig = inspect.signature(JoinOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_joinoperationouter_is_not_abstract():
    assert not inspect.isabstract(sql_from_JoinOperationOuter)


def test_sql_from_joinoperationouter_constructor_exists():
    assert callable(sql_from_JoinOperationOuter.__init__)


def test_sql_from_joinoperationouter_constructor_args():
    sig = inspect.signature(sql_from_JoinOperationOuter.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_joinoperationright_is_not_abstract():
    assert not inspect.isabstract(sql_from_JoinOperationRight)


def test_sql_from_joinoperationright_constructor_exists():
    assert callable(sql_from_JoinOperationRight.__init__)


def test_sql_from_joinoperationright_constructor_args():
    sig = inspect.signature(sql_from_JoinOperationRight.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_joinoperationleft_is_not_abstract():
    assert not inspect.isabstract(sql_from_JoinOperationLeft)


def test_sql_from_joinoperationleft_constructor_exists():
    assert callable(sql_from_JoinOperationLeft.__init__)


def test_sql_from_joinoperationleft_constructor_args():
    sig = inspect.signature(sql_from_JoinOperationLeft.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_joinoperationinner_is_not_abstract():
    assert not inspect.isabstract(sql_from_JoinOperationInner)


def test_sql_from_joinoperationinner_constructor_exists():
    assert callable(sql_from_JoinOperationInner.__init__)


def test_sql_from_joinoperationinner_constructor_args():
    sig = inspect.signature(sql_from_JoinOperationInner.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_joinoperation_is_not_abstract():
    assert not inspect.isabstract(sql_from_JoinOperation)


def test_sql_from_joinoperation_constructor_exists():
    assert callable(sql_from_JoinOperation.__init__)


def test_sql_from_joinoperation_constructor_args():
    sig = inspect.signature(sql_from_JoinOperation.__init__)
    params = list(sig.parameters.keys())



def test_selectexpression_is_not_abstract():
    assert not inspect.isabstract(SelectExpression)


def test_selectexpression_constructor_exists():
    assert callable(SelectExpression.__init__)


def test_selectexpression_constructor_args():
    sig = inspect.signature(SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_tableexpression_is_not_abstract():
    assert not inspect.isabstract(sql_from_TableExpression)


def test_sql_from_tableexpression_constructor_exists():
    assert callable(sql_from_TableExpression.__init__)


def test_sql_from_tableexpression_constructor_args():
    sig = inspect.signature(sql_from_TableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_sql_from_tableexpression_has_label():
    assert hasattr(sql_from_TableExpression, "label")
    descriptor = None
    for klass in sql_from_TableExpression.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_from_tablelistexpression_is_not_abstract():
    assert not inspect.isabstract(from_TableListExpression)


def test_from_tablelistexpression_constructor_exists():
    assert callable(from_TableListExpression.__init__)


def test_from_tablelistexpression_constructor_args():
    sig = inspect.signature(from_TableListExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_from_fromexpression_is_not_abstract():
    assert not inspect.isabstract(sql_from_FromExpression)


def test_sql_from_fromexpression_constructor_exists():
    assert callable(sql_from_FromExpression.__init__)


def test_sql_from_fromexpression_constructor_args():
    sig = inspect.signature(sql_from_FromExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_column_is_not_abstract():
    assert not inspect.isabstract(sql_column_Column)


def test_sql_column_column_constructor_exists():
    assert callable(sql_column_Column.__init__)


def test_sql_column_column_constructor_args():
    sig = inspect.signature(sql_column_Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_column_column_has_name():
    assert hasattr(sql_column_Column, "name")
    descriptor = None
    for klass in sql_column_Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql_from_table_is_not_abstract():
    assert not inspect.isabstract(sql_from_Table)


def test_sql_from_table_constructor_exists():
    assert callable(sql_from_Table.__init__)


def test_sql_from_table_constructor_args():
    sig = inspect.signature(sql_from_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql_from_table_has_name():
    assert hasattr(sql_from_Table, "name")
    descriptor = None
    for klass in sql_from_Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_from_table_is_not_abstract():
    assert not inspect.isabstract(from_Table)


def test_from_table_constructor_exists():
    assert callable(from_Table.__init__)


def test_from_table_constructor_args():
    sig = inspect.signature(from_Table.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnoperation_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnOperation)


def test_sql_column_columnoperation_constructor_exists():
    assert callable(sql_column_ColumnOperation.__init__)


def test_sql_column_columnoperation_constructor_args():
    sig = inspect.signature(sql_column_ColumnOperation.__init__)
    params = list(sig.parameters.keys())



def test_column_columnoperation_is_not_abstract():
    assert not inspect.isabstract(column_ColumnOperation)


def test_column_columnoperation_constructor_exists():
    assert callable(column_ColumnOperation.__init__)


def test_column_columnoperation_constructor_args():
    sig = inspect.signature(column_ColumnOperation.__init__)
    params = list(sig.parameters.keys())



def test_expression_expression_is_not_abstract():
    assert not inspect.isabstract(expression_Expression)


def test_expression_expression_constructor_exists():
    assert callable(expression_Expression.__init__)


def test_expression_expression_constructor_args():
    sig = inspect.signature(expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_singlecolumnexpression_is_not_abstract():
    assert not inspect.isabstract(sql_column_SingleColumnExpression)


def test_sql_column_singlecolumnexpression_constructor_exists():
    assert callable(sql_column_SingleColumnExpression.__init__)


def test_sql_column_singlecolumnexpression_constructor_args():
    sig = inspect.signature(sql_column_SingleColumnExpression.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sql_column_singlecolumnexpression_has_alias():
    assert hasattr(sql_column_SingleColumnExpression, "alias")
    descriptor = None
    for klass in sql_column_SingleColumnExpression.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_column_singlecolumnexpression_is_not_abstract():
    assert not inspect.isabstract(column_SingleColumnExpression)


def test_column_singlecolumnexpression_constructor_exists():
    assert callable(column_SingleColumnExpression.__init__)


def test_column_singlecolumnexpression_constructor_args():
    sig = inspect.signature(column_SingleColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnexpression_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnExpression)


def test_sql_column_columnexpression_constructor_exists():
    assert callable(sql_column_ColumnExpression.__init__)


def test_sql_column_columnexpression_constructor_args():
    sig = inspect.signature(sql_column_ColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_columnoperation_is_not_abstract():
    assert not inspect.isabstract(ColumnOperation)


def test_columnoperation_constructor_exists():
    assert callable(ColumnOperation.__init__)


def test_columnoperation_constructor_args():
    sig = inspect.signature(ColumnOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnoperationmax_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnOperationMax)


def test_sql_column_columnoperationmax_constructor_exists():
    assert callable(sql_column_ColumnOperationMax.__init__)


def test_sql_column_columnoperationmax_constructor_args():
    sig = inspect.signature(sql_column_ColumnOperationMax.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnoperationavg_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnOperationAvg)


def test_sql_column_columnoperationavg_constructor_exists():
    assert callable(sql_column_ColumnOperationAvg.__init__)


def test_sql_column_columnoperationavg_constructor_args():
    sig = inspect.signature(sql_column_ColumnOperationAvg.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnoperationsome_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnOperationSome)


def test_sql_column_columnoperationsome_constructor_exists():
    assert callable(sql_column_ColumnOperationSome.__init__)


def test_sql_column_columnoperationsome_constructor_args():
    sig = inspect.signature(sql_column_ColumnOperationSome.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnoperationmin_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnOperationMin)


def test_sql_column_columnoperationmin_constructor_exists():
    assert callable(sql_column_ColumnOperationMin.__init__)


def test_sql_column_columnoperationmin_constructor_args():
    sig = inspect.signature(sql_column_ColumnOperationMin.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnoperationevery_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnOperationEvery)


def test_sql_column_columnoperationevery_constructor_exists():
    assert callable(sql_column_ColumnOperationEvery.__init__)


def test_sql_column_columnoperationevery_constructor_args():
    sig = inspect.signature(sql_column_ColumnOperationEvery.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnoperationsum_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnOperationSum)


def test_sql_column_columnoperationsum_constructor_exists():
    assert callable(sql_column_ColumnOperationSum.__init__)


def test_sql_column_columnoperationsum_constructor_args():
    sig = inspect.signature(sql_column_ColumnOperationSum.__init__)
    params = list(sig.parameters.keys())



def test_sql_column_columnoperationcount_is_not_abstract():
    assert not inspect.isabstract(sql_column_ColumnOperationCount)


def test_sql_column_columnoperationcount_constructor_exists():
    assert callable(sql_column_ColumnOperationCount.__init__)


def test_sql_column_columnoperationcount_constructor_args():
    sig = inspect.signature(sql_column_ColumnOperationCount.__init__)
    params = list(sig.parameters.keys())



def test_sql_parameter_selectparameter_is_not_abstract():
    assert not inspect.isabstract(sql_parameter_SelectParameter)


def test_sql_parameter_selectparameter_constructor_exists():
    assert callable(sql_parameter_SelectParameter.__init__)


def test_sql_parameter_selectparameter_constructor_args():
    sig = inspect.signature(sql_parameter_SelectParameter.__init__)
    params = list(sig.parameters.keys())



def test_limit_limitexpression_is_not_abstract():
    assert not inspect.isabstract(limit_LimitExpression)


def test_limit_limitexpression_constructor_exists():
    assert callable(limit_LimitExpression.__init__)


def test_limit_limitexpression_constructor_args():
    sig = inspect.signature(limit_LimitExpression.__init__)
    params = list(sig.parameters.keys())



def test_orderby_orderbyexpression_is_not_abstract():
    assert not inspect.isabstract(orderBy_OrderByExpression)


def test_orderby_orderbyexpression_constructor_exists():
    assert callable(orderBy_OrderByExpression.__init__)


def test_orderby_orderbyexpression_constructor_args():
    sig = inspect.signature(orderBy_OrderByExpression.__init__)
    params = list(sig.parameters.keys())



def test_set_setexpression_is_not_abstract():
    assert not inspect.isabstract(set_SetExpression)


def test_set_setexpression_constructor_exists():
    assert callable(set_SetExpression.__init__)


def test_set_setexpression_constructor_args():
    sig = inspect.signature(set_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_having_havingexpression_is_not_abstract():
    assert not inspect.isabstract(having_HavingExpression)


def test_having_havingexpression_constructor_exists():
    assert callable(having_HavingExpression.__init__)


def test_having_havingexpression_constructor_args():
    sig = inspect.signature(having_HavingExpression.__init__)
    params = list(sig.parameters.keys())



def test_selectparameter_is_not_abstract():
    assert not inspect.isabstract(SelectParameter)


def test_selectparameter_constructor_exists():
    assert callable(SelectParameter.__init__)


def test_selectparameter_constructor_args():
    sig = inspect.signature(SelectParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql_parameter_selectparameterdistinct_is_not_abstract():
    assert not inspect.isabstract(sql_parameter_SelectParameterDistinct)


def test_sql_parameter_selectparameterdistinct_constructor_exists():
    assert callable(sql_parameter_SelectParameterDistinct.__init__)


def test_sql_parameter_selectparameterdistinct_constructor_args():
    sig = inspect.signature(sql_parameter_SelectParameterDistinct.__init__)
    params = list(sig.parameters.keys())



def test_sql_parameter_selectparameterall_is_not_abstract():
    assert not inspect.isabstract(sql_parameter_SelectParameterAll)


def test_sql_parameter_selectparameterall_constructor_exists():
    assert callable(sql_parameter_SelectParameterAll.__init__)


def test_sql_parameter_selectparameterall_constructor_args():
    sig = inspect.signature(sql_parameter_SelectParameterAll.__init__)
    params = list(sig.parameters.keys())



def test_from_fromexpression_is_not_abstract():
    assert not inspect.isabstract(from_FromExpression)


def test_from_fromexpression_constructor_exists():
    assert callable(from_FromExpression.__init__)


def test_from_fromexpression_constructor_args():
    sig = inspect.signature(from_FromExpression.__init__)
    params = list(sig.parameters.keys())



def test_column_columnexpression_is_not_abstract():
    assert not inspect.isabstract(column_ColumnExpression)


def test_column_columnexpression_constructor_exists():
    assert callable(column_ColumnExpression.__init__)


def test_column_columnexpression_constructor_args():
    sig = inspect.signature(column_ColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameter_selectparameter_is_not_abstract():
    assert not inspect.isabstract(parameter_SelectParameter)


def test_parameter_selectparameter_constructor_exists():
    assert callable(parameter_SelectParameter.__init__)


def test_parameter_selectparameter_constructor_args():
    sig = inspect.signature(parameter_SelectParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql_select_selectexpression_is_not_abstract():
    assert not inspect.isabstract(sql_select_SelectExpression)


def test_sql_select_selectexpression_constructor_exists():
    assert callable(sql_select_SelectExpression.__init__)


def test_sql_select_selectexpression_constructor_args():
    sig = inspect.signature(sql_select_SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_groupby_groupbyexpression_is_not_abstract():
    assert not inspect.isabstract(groupBy_GroupByExpression)


def test_groupby_groupbyexpression_constructor_exists():
    assert callable(groupBy_GroupByExpression.__init__)


def test_groupby_groupbyexpression_constructor_args():
    sig = inspect.signature(groupBy_GroupByExpression.__init__)
    params = list(sig.parameters.keys())



def test_where_whereexpression_is_not_abstract():
    assert not inspect.isabstract(where_WhereExpression)


def test_where_whereexpression_constructor_exists():
    assert callable(where_WhereExpression.__init__)


def test_where_whereexpression_constructor_args():
    sig = inspect.signature(where_WhereExpression.__init__)
    params = list(sig.parameters.keys())



def test_date_is_not_abstract():
    assert not inspect.isabstract(Date)


def test_date_constructor_exists():
    assert callable(Date.__init__)


def test_date_constructor_args():
    sig = inspect.signature(Date.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_timestamp_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_TimeStamp)


def test_sql_sqldatatypes_timestamp_constructor_exists():
    assert callable(sql_sqlDataTypes_TimeStamp.__init__)


def test_sql_sqldatatypes_timestamp_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_TimeStamp.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_datatype_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_DataType)


def test_sql_sqldatatypes_datatype_constructor_exists():
    assert callable(sql_sqlDataTypes_DataType.__init__)


def test_sql_sqldatatypes_datatype_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_DataType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_date_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_Date)


def test_sql_sqldatatypes_date_constructor_exists():
    assert callable(sql_sqlDataTypes_Date.__init__)


def test_sql_sqldatatypes_date_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_Date.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_real_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_Real)


def test_sql_sqldatatypes_real_constructor_exists():
    assert callable(sql_sqlDataTypes_Real.__init__)


def test_sql_sqldatatypes_real_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_Real.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_integer_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_Integer)


def test_sql_sqldatatypes_integer_constructor_exists():
    assert callable(sql_sqlDataTypes_Integer.__init__)


def test_sql_sqldatatypes_integer_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_Integer.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_double_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_Double)


def test_sql_sqldatatypes_double_constructor_exists():
    assert callable(sql_sqlDataTypes_Double.__init__)


def test_sql_sqldatatypes_double_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_Double.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_float_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_Float)


def test_sql_sqldatatypes_float_constructor_exists():
    assert callable(sql_sqlDataTypes_Float.__init__)


def test_sql_sqldatatypes_float_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_Float.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_boolean_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_Boolean)


def test_sql_sqldatatypes_boolean_constructor_exists():
    assert callable(sql_sqlDataTypes_Boolean.__init__)


def test_sql_sqldatatypes_boolean_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_sql_sqldatatypes_string_is_not_abstract():
    assert not inspect.isabstract(sql_sqlDataTypes_String)


def test_sql_sqldatatypes_string_constructor_exists():
    assert callable(sql_sqlDataTypes_String.__init__)


def test_sql_sqldatatypes_string_constructor_args():
    sig = inspect.signature(sql_sqlDataTypes_String.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
SimpleTerm_strategy = st.builds(
    SimpleTerm,
)
sql_term_SimpleTermChar_strategy = st.builds(
    sql_term_SimpleTermChar,
)
sql_term_SimpleTermInteger_strategy = st.builds(
    sql_term_SimpleTermInteger,
)
sql_term_SimpleTermFloat_strategy = st.builds(
    sql_term_SimpleTermFloat,
)
sql_term_SimpleTermString_strategy = st.builds(
    sql_term_SimpleTermString,
)
BooleanTerm_strategy = st.builds(
    BooleanTerm,
)
sql_term_BooleanTermFalse_strategy = st.builds(
    sql_term_BooleanTermFalse,
)
sql_term_BooleanTermTrue_strategy = st.builds(
    sql_term_BooleanTermTrue,
)
Term_strategy = st.builds(
    Term,
)
sql_term_NullTerm_strategy = st.builds(
    sql_term_NullTerm,
)
sql_term_ColumnTerm_strategy = st.builds(
    sql_term_ColumnTerm,
)
sql_term_SimpleTerm_strategy = st.builds(
    sql_term_SimpleTerm,
    value=
        safe_text
)
sql_term_CountStarTerm_strategy = st.builds(
    sql_term_CountStarTerm,
)
sql_term_StarTerm_strategy = st.builds(
    sql_term_StarTerm,
)
sql_term_BooleanTerm_strategy = st.builds(
    sql_term_BooleanTerm,
)
sql_term_Term_strategy = st.builds(
    sql_term_Term,
)
value_ValueFrontOperation_strategy = st.builds(
    value_ValueFrontOperation,
)
value_ValueOperation_strategy = st.builds(
    value_ValueOperation,
)
term_Term_strategy = st.builds(
    term_Term,
)
Value_strategy = st.builds(
    Value,
)
sql_value_FunctionValue_strategy = st.builds(
    sql_value_FunctionValue,
    functionName=
        safe_text
)
sql_value_ConditionValue_strategy = st.builds(
    sql_value_ConditionValue,
)
sql_value_SimpleValue_strategy = st.builds(
    sql_value_SimpleValue,
)
sql_value_ValueOperation_strategy = st.builds(
    sql_value_ValueOperation,
)
ValueFrontOperation_strategy = st.builds(
    ValueFrontOperation,
)
sql_value_ValueFrontOperationMinus_strategy = st.builds(
    sql_value_ValueFrontOperationMinus,
)
sql_value_ValueFrontOperationPlus_strategy = st.builds(
    sql_value_ValueFrontOperationPlus,
)
ValueOperation_strategy = st.builds(
    ValueOperation,
)
sql_value_ValueOperationMultiply_strategy = st.builds(
    sql_value_ValueOperationMultiply,
)
sql_value_ValueOperationParallel_strategy = st.builds(
    sql_value_ValueOperationParallel,
)
sql_value_ValueOperationDivide_strategy = st.builds(
    sql_value_ValueOperationDivide,
)
sql_value_ValueFrontOperation_strategy = st.builds(
    sql_value_ValueFrontOperation,
)
sql_value_Value_strategy = st.builds(
    sql_value_Value,
)
ConditionOperation_strategy = st.builds(
    ConditionOperation,
)
sql_condition_ConditionOperationUnEqual2_strategy = st.builds(
    sql_condition_ConditionOperationUnEqual2,
)
sql_condition_ConditionOperationGreatEqual_strategy = st.builds(
    sql_condition_ConditionOperationGreatEqual,
)
sql_condition_ConditionOperationGreater_strategy = st.builds(
    sql_condition_ConditionOperationGreater,
)
sql_condition_ConditionOperationUnEqual_strategy = st.builds(
    sql_condition_ConditionOperationUnEqual,
)
sql_condition_ConditionOperationEqual_strategy = st.builds(
    sql_condition_ConditionOperationEqual,
)
sql_condition_ConditionOperationLessEqual_strategy = st.builds(
    sql_condition_ConditionOperationLessEqual,
)
sql_condition_ConditionOperationLesser_strategy = st.builds(
    sql_condition_ConditionOperationLesser,
)
sql_condition_ConditionOperation_strategy = st.builds(
    sql_condition_ConditionOperation,
)
condition_ConditionOperation_strategy = st.builds(
    condition_ConditionOperation,
)
AndOrExpressionOperation_strategy = st.builds(
    AndOrExpressionOperation,
)
sql_expression_ExpressionOperationAnd_strategy = st.builds(
    sql_expression_ExpressionOperationAnd,
)
ExpressionOperation_strategy = st.builds(
    ExpressionOperation,
)
sql_expression_ExpressionOperationNot_strategy = st.builds(
    sql_expression_ExpressionOperationNot,
)
sql_expression_AndOrExpressionOperation_strategy = st.builds(
    sql_expression_AndOrExpressionOperation,
)
sql_expression_ExpressionOperation_strategy = st.builds(
    sql_expression_ExpressionOperation,
)
expression_ExpressionOperationNot_strategy = st.builds(
    expression_ExpressionOperationNot,
)
SimpleCondition_strategy = st.builds(
    SimpleCondition,
)
sql_condition_BetweenCondition_strategy = st.builds(
    sql_condition_BetweenCondition,
)
sql_condition_LikeCondition_strategy = st.builds(
    sql_condition_LikeCondition,
)
sql_condition_IsNullCondition_strategy = st.builds(
    sql_condition_IsNullCondition,
)
sql_condition_InCondition_strategy = st.builds(
    sql_condition_InCondition,
)
sql_condition_ExistsCondition_strategy = st.builds(
    sql_condition_ExistsCondition,
)
sql_condition_OperationCondition_strategy = st.builds(
    sql_condition_OperationCondition,
)
value_Value_strategy = st.builds(
    value_Value,
)
Condition_strategy = st.builds(
    Condition,
)
sql_condition_SimpleCondition_strategy = st.builds(
    sql_condition_SimpleCondition,
)
sql_condition_Condition_strategy = st.builds(
    sql_condition_Condition,
)
sql_expression_ExpressionOperationOr_strategy = st.builds(
    sql_expression_ExpressionOperationOr,
)
sql_limit_LimitExpression_strategy = st.builds(
    sql_limit_LimitExpression,
    limit=
        safe_text,
    offset=
        safe_text
)
condition_Condition_strategy = st.builds(
    condition_Condition,
)
expression_AndOrExpressionOperation_strategy = st.builds(
    expression_AndOrExpressionOperation,
)
Expression_strategy = st.builds(
    Expression,
)
sql_expression_SimpleExpression_strategy = st.builds(
    sql_expression_SimpleExpression,
)
sql_expression_Expression_strategy = st.builds(
    sql_expression_Expression,
)
set_SetOperation_strategy = st.builds(
    set_SetOperation,
)
sql_set_SetExpression_strategy = st.builds(
    sql_set_SetExpression,
)
sql_having_HavingExpression_strategy = st.builds(
    sql_having_HavingExpression,
)
parameter_SelectParameterDistinct_strategy = st.builds(
    parameter_SelectParameterDistinct,
)
SetOperation_strategy = st.builds(
    SetOperation,
)
sql_set_SetOperationMinus_strategy = st.builds(
    sql_set_SetOperationMinus,
)
sql_set_SetOperationExcept_strategy = st.builds(
    sql_set_SetOperationExcept,
)
sql_set_SetOperationIntersect_strategy = st.builds(
    sql_set_SetOperationIntersect,
)
sql_set_SetOperationUnion_strategy = st.builds(
    sql_set_SetOperationUnion,
)
sql_set_SetOperation_strategy = st.builds(
    sql_set_SetOperation,
)
sql_groupBy_GroupByExpression_strategy = st.builds(
    sql_groupBy_GroupByExpression,
)
sql_orderBy_OrderByParameter_strategy = st.builds(
    sql_orderBy_OrderByParameter,
)
OrderByParameter_strategy = st.builds(
    OrderByParameter,
)
sql_orderBy_OrderByParameterDesc_strategy = st.builds(
    sql_orderBy_OrderByParameterDesc,
)
sql_orderBy_OrderByParameterAsc_strategy = st.builds(
    sql_orderBy_OrderByParameterAsc,
)
column_Column_strategy = st.builds(
    column_Column,
)
OrderByExpression_strategy = st.builds(
    OrderByExpression,
)
sql_orderBy_OrderBySelectExpression_strategy = st.builds(
    sql_orderBy_OrderBySelectExpression,
)
sql_orderBy_OrderByColumnExpression_strategy = st.builds(
    sql_orderBy_OrderByColumnExpression,
)
orderBy_OrderByParameter_strategy = st.builds(
    orderBy_OrderByParameter,
)
sql_orderBy_OrderByExpression_strategy = st.builds(
    sql_orderBy_OrderByExpression,
)
sql_where_WhereExpression_strategy = st.builds(
    sql_where_WhereExpression,
)
sql_orderBy_OrderByAliasExpression_strategy = st.builds(
    sql_orderBy_OrderByAliasExpression,
    alias=
        safe_text
)
from_JoinOperation_strategy = st.builds(
    from_JoinOperation,
)
sql_from_JoinTableExpression_strategy = st.builds(
    sql_from_JoinTableExpression,
)
from_JoinTableExpression_strategy = st.builds(
    from_JoinTableExpression,
)
from_TableExpression_strategy = st.builds(
    from_TableExpression,
)
sql_from_TableListExpression_strategy = st.builds(
    sql_from_TableListExpression,
)
JoinOperation_strategy = st.builds(
    JoinOperation,
)
sql_from_JoinOperationOuter_strategy = st.builds(
    sql_from_JoinOperationOuter,
)
sql_from_JoinOperationRight_strategy = st.builds(
    sql_from_JoinOperationRight,
)
sql_from_JoinOperationLeft_strategy = st.builds(
    sql_from_JoinOperationLeft,
)
sql_from_JoinOperationInner_strategy = st.builds(
    sql_from_JoinOperationInner,
)
sql_from_JoinOperation_strategy = st.builds(
    sql_from_JoinOperation,
)
SelectExpression_strategy = st.builds(
    SelectExpression,
)
sql_from_TableExpression_strategy = st.builds(
    sql_from_TableExpression,
    label=
        safe_text
)
from_TableListExpression_strategy = st.builds(
    from_TableListExpression,
)
sql_from_FromExpression_strategy = st.builds(
    sql_from_FromExpression,
)
sql_column_Column_strategy = st.builds(
    sql_column_Column,
    name=
        safe_text
)
sql_from_Table_strategy = st.builds(
    sql_from_Table,
    name=
        safe_text
)
from_Table_strategy = st.builds(
    from_Table,
)
sql_column_ColumnOperation_strategy = st.builds(
    sql_column_ColumnOperation,
)
column_ColumnOperation_strategy = st.builds(
    column_ColumnOperation,
)
expression_Expression_strategy = st.builds(
    expression_Expression,
)
sql_column_SingleColumnExpression_strategy = st.builds(
    sql_column_SingleColumnExpression,
    alias=
        safe_text
)
column_SingleColumnExpression_strategy = st.builds(
    column_SingleColumnExpression,
)
sql_column_ColumnExpression_strategy = st.builds(
    sql_column_ColumnExpression,
)
ColumnOperation_strategy = st.builds(
    ColumnOperation,
)
sql_column_ColumnOperationMax_strategy = st.builds(
    sql_column_ColumnOperationMax,
)
sql_column_ColumnOperationAvg_strategy = st.builds(
    sql_column_ColumnOperationAvg,
)
sql_column_ColumnOperationSome_strategy = st.builds(
    sql_column_ColumnOperationSome,
)
sql_column_ColumnOperationMin_strategy = st.builds(
    sql_column_ColumnOperationMin,
)
sql_column_ColumnOperationEvery_strategy = st.builds(
    sql_column_ColumnOperationEvery,
)
sql_column_ColumnOperationSum_strategy = st.builds(
    sql_column_ColumnOperationSum,
)
sql_column_ColumnOperationCount_strategy = st.builds(
    sql_column_ColumnOperationCount,
)
sql_parameter_SelectParameter_strategy = st.builds(
    sql_parameter_SelectParameter,
)
limit_LimitExpression_strategy = st.builds(
    limit_LimitExpression,
)
orderBy_OrderByExpression_strategy = st.builds(
    orderBy_OrderByExpression,
)
set_SetExpression_strategy = st.builds(
    set_SetExpression,
)
having_HavingExpression_strategy = st.builds(
    having_HavingExpression,
)
SelectParameter_strategy = st.builds(
    SelectParameter,
)
sql_parameter_SelectParameterDistinct_strategy = st.builds(
    sql_parameter_SelectParameterDistinct,
)
sql_parameter_SelectParameterAll_strategy = st.builds(
    sql_parameter_SelectParameterAll,
)
from_FromExpression_strategy = st.builds(
    from_FromExpression,
)
column_ColumnExpression_strategy = st.builds(
    column_ColumnExpression,
)
parameter_SelectParameter_strategy = st.builds(
    parameter_SelectParameter,
)
sql_select_SelectExpression_strategy = st.builds(
    sql_select_SelectExpression,
)
groupBy_GroupByExpression_strategy = st.builds(
    groupBy_GroupByExpression,
)
where_WhereExpression_strategy = st.builds(
    where_WhereExpression,
)
Date_strategy = st.builds(
    Date,
)
sql_sqlDataTypes_TimeStamp_strategy = st.builds(
    sql_sqlDataTypes_TimeStamp,
)
sql_sqlDataTypes_DataType_strategy = st.builds(
    sql_sqlDataTypes_DataType,
)
DataType_strategy = st.builds(
    DataType,
)
sql_sqlDataTypes_Date_strategy = st.builds(
    sql_sqlDataTypes_Date,
)
sql_sqlDataTypes_Real_strategy = st.builds(
    sql_sqlDataTypes_Real,
)
sql_sqlDataTypes_Integer_strategy = st.builds(
    sql_sqlDataTypes_Integer,
)
sql_sqlDataTypes_Double_strategy = st.builds(
    sql_sqlDataTypes_Double,
)
sql_sqlDataTypes_Float_strategy = st.builds(
    sql_sqlDataTypes_Float,
)
sql_sqlDataTypes_Boolean_strategy = st.builds(
    sql_sqlDataTypes_Boolean,
)
sql_sqlDataTypes_String_strategy = st.builds(
    sql_sqlDataTypes_String,
)

@given(instance=SimpleTerm_strategy)
@settings(max_examples=50)
def test_simpleterm_instantiation(instance):
    assert isinstance(instance, SimpleTerm)

@given(instance=sql_term_SimpleTermChar_strategy)
@settings(max_examples=50)
def test_sql_term_simpletermchar_instantiation(instance):
    assert isinstance(instance, sql_term_SimpleTermChar)

@given(instance=sql_term_SimpleTermInteger_strategy)
@settings(max_examples=50)
def test_sql_term_simpleterminteger_instantiation(instance):
    assert isinstance(instance, sql_term_SimpleTermInteger)

@given(instance=sql_term_SimpleTermFloat_strategy)
@settings(max_examples=50)
def test_sql_term_simpletermfloat_instantiation(instance):
    assert isinstance(instance, sql_term_SimpleTermFloat)

@given(instance=sql_term_SimpleTermString_strategy)
@settings(max_examples=50)
def test_sql_term_simpletermstring_instantiation(instance):
    assert isinstance(instance, sql_term_SimpleTermString)

@given(instance=BooleanTerm_strategy)
@settings(max_examples=50)
def test_booleanterm_instantiation(instance):
    assert isinstance(instance, BooleanTerm)

@given(instance=sql_term_BooleanTermFalse_strategy)
@settings(max_examples=50)
def test_sql_term_booleantermfalse_instantiation(instance):
    assert isinstance(instance, sql_term_BooleanTermFalse)

@given(instance=sql_term_BooleanTermTrue_strategy)
@settings(max_examples=50)
def test_sql_term_booleantermtrue_instantiation(instance):
    assert isinstance(instance, sql_term_BooleanTermTrue)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=sql_term_NullTerm_strategy)
@settings(max_examples=50)
def test_sql_term_nullterm_instantiation(instance):
    assert isinstance(instance, sql_term_NullTerm)

@given(instance=sql_term_ColumnTerm_strategy)
@settings(max_examples=50)
def test_sql_term_columnterm_instantiation(instance):
    assert isinstance(instance, sql_term_ColumnTerm)

@given(instance=sql_term_SimpleTerm_strategy)
@settings(max_examples=50)
def test_sql_term_simpleterm_instantiation(instance):
    assert isinstance(instance, sql_term_SimpleTerm)



@given(instance=sql_term_SimpleTerm_strategy)
def test_sql_term_simpleterm_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql_term_CountStarTerm_strategy)
@settings(max_examples=50)
def test_sql_term_countstarterm_instantiation(instance):
    assert isinstance(instance, sql_term_CountStarTerm)

@given(instance=sql_term_StarTerm_strategy)
@settings(max_examples=50)
def test_sql_term_starterm_instantiation(instance):
    assert isinstance(instance, sql_term_StarTerm)

@given(instance=sql_term_BooleanTerm_strategy)
@settings(max_examples=50)
def test_sql_term_booleanterm_instantiation(instance):
    assert isinstance(instance, sql_term_BooleanTerm)

@given(instance=sql_term_Term_strategy)
@settings(max_examples=50)
def test_sql_term_term_instantiation(instance):
    assert isinstance(instance, sql_term_Term)

@given(instance=value_ValueFrontOperation_strategy)
@settings(max_examples=50)
def test_value_valuefrontoperation_instantiation(instance):
    assert isinstance(instance, value_ValueFrontOperation)

@given(instance=value_ValueOperation_strategy)
@settings(max_examples=50)
def test_value_valueoperation_instantiation(instance):
    assert isinstance(instance, value_ValueOperation)

@given(instance=term_Term_strategy)
@settings(max_examples=50)
def test_term_term_instantiation(instance):
    assert isinstance(instance, term_Term)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=sql_value_FunctionValue_strategy)
@settings(max_examples=50)
def test_sql_value_functionvalue_instantiation(instance):
    assert isinstance(instance, sql_value_FunctionValue)



@given(instance=sql_value_FunctionValue_strategy)
def test_sql_value_functionvalue_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=sql_value_ConditionValue_strategy)
@settings(max_examples=50)
def test_sql_value_conditionvalue_instantiation(instance):
    assert isinstance(instance, sql_value_ConditionValue)

@given(instance=sql_value_SimpleValue_strategy)
@settings(max_examples=50)
def test_sql_value_simplevalue_instantiation(instance):
    assert isinstance(instance, sql_value_SimpleValue)

@given(instance=sql_value_ValueOperation_strategy)
@settings(max_examples=50)
def test_sql_value_valueoperation_instantiation(instance):
    assert isinstance(instance, sql_value_ValueOperation)

@given(instance=ValueFrontOperation_strategy)
@settings(max_examples=50)
def test_valuefrontoperation_instantiation(instance):
    assert isinstance(instance, ValueFrontOperation)

@given(instance=sql_value_ValueFrontOperationMinus_strategy)
@settings(max_examples=50)
def test_sql_value_valuefrontoperationminus_instantiation(instance):
    assert isinstance(instance, sql_value_ValueFrontOperationMinus)

@given(instance=sql_value_ValueFrontOperationPlus_strategy)
@settings(max_examples=50)
def test_sql_value_valuefrontoperationplus_instantiation(instance):
    assert isinstance(instance, sql_value_ValueFrontOperationPlus)

@given(instance=ValueOperation_strategy)
@settings(max_examples=50)
def test_valueoperation_instantiation(instance):
    assert isinstance(instance, ValueOperation)

@given(instance=sql_value_ValueOperationMultiply_strategy)
@settings(max_examples=50)
def test_sql_value_valueoperationmultiply_instantiation(instance):
    assert isinstance(instance, sql_value_ValueOperationMultiply)

@given(instance=sql_value_ValueOperationParallel_strategy)
@settings(max_examples=50)
def test_sql_value_valueoperationparallel_instantiation(instance):
    assert isinstance(instance, sql_value_ValueOperationParallel)

@given(instance=sql_value_ValueOperationDivide_strategy)
@settings(max_examples=50)
def test_sql_value_valueoperationdivide_instantiation(instance):
    assert isinstance(instance, sql_value_ValueOperationDivide)

@given(instance=sql_value_ValueFrontOperation_strategy)
@settings(max_examples=50)
def test_sql_value_valuefrontoperation_instantiation(instance):
    assert isinstance(instance, sql_value_ValueFrontOperation)

@given(instance=sql_value_Value_strategy)
@settings(max_examples=50)
def test_sql_value_value_instantiation(instance):
    assert isinstance(instance, sql_value_Value)

@given(instance=ConditionOperation_strategy)
@settings(max_examples=50)
def test_conditionoperation_instantiation(instance):
    assert isinstance(instance, ConditionOperation)

@given(instance=sql_condition_ConditionOperationUnEqual2_strategy)
@settings(max_examples=50)
def test_sql_condition_conditionoperationunequal2_instantiation(instance):
    assert isinstance(instance, sql_condition_ConditionOperationUnEqual2)

@given(instance=sql_condition_ConditionOperationGreatEqual_strategy)
@settings(max_examples=50)
def test_sql_condition_conditionoperationgreatequal_instantiation(instance):
    assert isinstance(instance, sql_condition_ConditionOperationGreatEqual)

@given(instance=sql_condition_ConditionOperationGreater_strategy)
@settings(max_examples=50)
def test_sql_condition_conditionoperationgreater_instantiation(instance):
    assert isinstance(instance, sql_condition_ConditionOperationGreater)

@given(instance=sql_condition_ConditionOperationUnEqual_strategy)
@settings(max_examples=50)
def test_sql_condition_conditionoperationunequal_instantiation(instance):
    assert isinstance(instance, sql_condition_ConditionOperationUnEqual)

@given(instance=sql_condition_ConditionOperationEqual_strategy)
@settings(max_examples=50)
def test_sql_condition_conditionoperationequal_instantiation(instance):
    assert isinstance(instance, sql_condition_ConditionOperationEqual)

@given(instance=sql_condition_ConditionOperationLessEqual_strategy)
@settings(max_examples=50)
def test_sql_condition_conditionoperationlessequal_instantiation(instance):
    assert isinstance(instance, sql_condition_ConditionOperationLessEqual)

@given(instance=sql_condition_ConditionOperationLesser_strategy)
@settings(max_examples=50)
def test_sql_condition_conditionoperationlesser_instantiation(instance):
    assert isinstance(instance, sql_condition_ConditionOperationLesser)

@given(instance=sql_condition_ConditionOperation_strategy)
@settings(max_examples=50)
def test_sql_condition_conditionoperation_instantiation(instance):
    assert isinstance(instance, sql_condition_ConditionOperation)

@given(instance=condition_ConditionOperation_strategy)
@settings(max_examples=50)
def test_condition_conditionoperation_instantiation(instance):
    assert isinstance(instance, condition_ConditionOperation)

@given(instance=AndOrExpressionOperation_strategy)
@settings(max_examples=50)
def test_andorexpressionoperation_instantiation(instance):
    assert isinstance(instance, AndOrExpressionOperation)

@given(instance=sql_expression_ExpressionOperationAnd_strategy)
@settings(max_examples=50)
def test_sql_expression_expressionoperationand_instantiation(instance):
    assert isinstance(instance, sql_expression_ExpressionOperationAnd)

@given(instance=ExpressionOperation_strategy)
@settings(max_examples=50)
def test_expressionoperation_instantiation(instance):
    assert isinstance(instance, ExpressionOperation)

@given(instance=sql_expression_ExpressionOperationNot_strategy)
@settings(max_examples=50)
def test_sql_expression_expressionoperationnot_instantiation(instance):
    assert isinstance(instance, sql_expression_ExpressionOperationNot)

@given(instance=sql_expression_AndOrExpressionOperation_strategy)
@settings(max_examples=50)
def test_sql_expression_andorexpressionoperation_instantiation(instance):
    assert isinstance(instance, sql_expression_AndOrExpressionOperation)

@given(instance=sql_expression_ExpressionOperation_strategy)
@settings(max_examples=50)
def test_sql_expression_expressionoperation_instantiation(instance):
    assert isinstance(instance, sql_expression_ExpressionOperation)

@given(instance=expression_ExpressionOperationNot_strategy)
@settings(max_examples=50)
def test_expression_expressionoperationnot_instantiation(instance):
    assert isinstance(instance, expression_ExpressionOperationNot)

@given(instance=SimpleCondition_strategy)
@settings(max_examples=50)
def test_simplecondition_instantiation(instance):
    assert isinstance(instance, SimpleCondition)

@given(instance=sql_condition_BetweenCondition_strategy)
@settings(max_examples=50)
def test_sql_condition_betweencondition_instantiation(instance):
    assert isinstance(instance, sql_condition_BetweenCondition)

@given(instance=sql_condition_LikeCondition_strategy)
@settings(max_examples=50)
def test_sql_condition_likecondition_instantiation(instance):
    assert isinstance(instance, sql_condition_LikeCondition)

@given(instance=sql_condition_IsNullCondition_strategy)
@settings(max_examples=50)
def test_sql_condition_isnullcondition_instantiation(instance):
    assert isinstance(instance, sql_condition_IsNullCondition)

@given(instance=sql_condition_InCondition_strategy)
@settings(max_examples=50)
def test_sql_condition_incondition_instantiation(instance):
    assert isinstance(instance, sql_condition_InCondition)

@given(instance=sql_condition_ExistsCondition_strategy)
@settings(max_examples=50)
def test_sql_condition_existscondition_instantiation(instance):
    assert isinstance(instance, sql_condition_ExistsCondition)

@given(instance=sql_condition_OperationCondition_strategy)
@settings(max_examples=50)
def test_sql_condition_operationcondition_instantiation(instance):
    assert isinstance(instance, sql_condition_OperationCondition)

@given(instance=value_Value_strategy)
@settings(max_examples=50)
def test_value_value_instantiation(instance):
    assert isinstance(instance, value_Value)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=sql_condition_SimpleCondition_strategy)
@settings(max_examples=50)
def test_sql_condition_simplecondition_instantiation(instance):
    assert isinstance(instance, sql_condition_SimpleCondition)

@given(instance=sql_condition_Condition_strategy)
@settings(max_examples=50)
def test_sql_condition_condition_instantiation(instance):
    assert isinstance(instance, sql_condition_Condition)

@given(instance=sql_expression_ExpressionOperationOr_strategy)
@settings(max_examples=50)
def test_sql_expression_expressionoperationor_instantiation(instance):
    assert isinstance(instance, sql_expression_ExpressionOperationOr)

@given(instance=sql_limit_LimitExpression_strategy)
@settings(max_examples=50)
def test_sql_limit_limitexpression_instantiation(instance):
    assert isinstance(instance, sql_limit_LimitExpression)



@given(instance=sql_limit_LimitExpression_strategy)
def test_sql_limit_limitexpression_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original



@given(instance=sql_limit_LimitExpression_strategy)
def test_sql_limit_limitexpression_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=condition_Condition_strategy)
@settings(max_examples=50)
def test_condition_condition_instantiation(instance):
    assert isinstance(instance, condition_Condition)

@given(instance=expression_AndOrExpressionOperation_strategy)
@settings(max_examples=50)
def test_expression_andorexpressionoperation_instantiation(instance):
    assert isinstance(instance, expression_AndOrExpressionOperation)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sql_expression_SimpleExpression_strategy)
@settings(max_examples=50)
def test_sql_expression_simpleexpression_instantiation(instance):
    assert isinstance(instance, sql_expression_SimpleExpression)

@given(instance=sql_expression_Expression_strategy)
@settings(max_examples=50)
def test_sql_expression_expression_instantiation(instance):
    assert isinstance(instance, sql_expression_Expression)

@given(instance=set_SetOperation_strategy)
@settings(max_examples=50)
def test_set_setoperation_instantiation(instance):
    assert isinstance(instance, set_SetOperation)

@given(instance=sql_set_SetExpression_strategy)
@settings(max_examples=50)
def test_sql_set_setexpression_instantiation(instance):
    assert isinstance(instance, sql_set_SetExpression)

@given(instance=sql_having_HavingExpression_strategy)
@settings(max_examples=50)
def test_sql_having_havingexpression_instantiation(instance):
    assert isinstance(instance, sql_having_HavingExpression)

@given(instance=parameter_SelectParameterDistinct_strategy)
@settings(max_examples=50)
def test_parameter_selectparameterdistinct_instantiation(instance):
    assert isinstance(instance, parameter_SelectParameterDistinct)

@given(instance=SetOperation_strategy)
@settings(max_examples=50)
def test_setoperation_instantiation(instance):
    assert isinstance(instance, SetOperation)

@given(instance=sql_set_SetOperationMinus_strategy)
@settings(max_examples=50)
def test_sql_set_setoperationminus_instantiation(instance):
    assert isinstance(instance, sql_set_SetOperationMinus)

@given(instance=sql_set_SetOperationExcept_strategy)
@settings(max_examples=50)
def test_sql_set_setoperationexcept_instantiation(instance):
    assert isinstance(instance, sql_set_SetOperationExcept)

@given(instance=sql_set_SetOperationIntersect_strategy)
@settings(max_examples=50)
def test_sql_set_setoperationintersect_instantiation(instance):
    assert isinstance(instance, sql_set_SetOperationIntersect)

@given(instance=sql_set_SetOperationUnion_strategy)
@settings(max_examples=50)
def test_sql_set_setoperationunion_instantiation(instance):
    assert isinstance(instance, sql_set_SetOperationUnion)

@given(instance=sql_set_SetOperation_strategy)
@settings(max_examples=50)
def test_sql_set_setoperation_instantiation(instance):
    assert isinstance(instance, sql_set_SetOperation)

@given(instance=sql_groupBy_GroupByExpression_strategy)
@settings(max_examples=50)
def test_sql_groupby_groupbyexpression_instantiation(instance):
    assert isinstance(instance, sql_groupBy_GroupByExpression)

@given(instance=sql_orderBy_OrderByParameter_strategy)
@settings(max_examples=50)
def test_sql_orderby_orderbyparameter_instantiation(instance):
    assert isinstance(instance, sql_orderBy_OrderByParameter)

@given(instance=OrderByParameter_strategy)
@settings(max_examples=50)
def test_orderbyparameter_instantiation(instance):
    assert isinstance(instance, OrderByParameter)

@given(instance=sql_orderBy_OrderByParameterDesc_strategy)
@settings(max_examples=50)
def test_sql_orderby_orderbyparameterdesc_instantiation(instance):
    assert isinstance(instance, sql_orderBy_OrderByParameterDesc)

@given(instance=sql_orderBy_OrderByParameterAsc_strategy)
@settings(max_examples=50)
def test_sql_orderby_orderbyparameterasc_instantiation(instance):
    assert isinstance(instance, sql_orderBy_OrderByParameterAsc)

@given(instance=column_Column_strategy)
@settings(max_examples=50)
def test_column_column_instantiation(instance):
    assert isinstance(instance, column_Column)

@given(instance=OrderByExpression_strategy)
@settings(max_examples=50)
def test_orderbyexpression_instantiation(instance):
    assert isinstance(instance, OrderByExpression)

@given(instance=sql_orderBy_OrderBySelectExpression_strategy)
@settings(max_examples=50)
def test_sql_orderby_orderbyselectexpression_instantiation(instance):
    assert isinstance(instance, sql_orderBy_OrderBySelectExpression)

@given(instance=sql_orderBy_OrderByColumnExpression_strategy)
@settings(max_examples=50)
def test_sql_orderby_orderbycolumnexpression_instantiation(instance):
    assert isinstance(instance, sql_orderBy_OrderByColumnExpression)

@given(instance=orderBy_OrderByParameter_strategy)
@settings(max_examples=50)
def test_orderby_orderbyparameter_instantiation(instance):
    assert isinstance(instance, orderBy_OrderByParameter)

@given(instance=sql_orderBy_OrderByExpression_strategy)
@settings(max_examples=50)
def test_sql_orderby_orderbyexpression_instantiation(instance):
    assert isinstance(instance, sql_orderBy_OrderByExpression)

@given(instance=sql_where_WhereExpression_strategy)
@settings(max_examples=50)
def test_sql_where_whereexpression_instantiation(instance):
    assert isinstance(instance, sql_where_WhereExpression)

@given(instance=sql_orderBy_OrderByAliasExpression_strategy)
@settings(max_examples=50)
def test_sql_orderby_orderbyaliasexpression_instantiation(instance):
    assert isinstance(instance, sql_orderBy_OrderByAliasExpression)



@given(instance=sql_orderBy_OrderByAliasExpression_strategy)
def test_sql_orderby_orderbyaliasexpression_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=from_JoinOperation_strategy)
@settings(max_examples=50)
def test_from_joinoperation_instantiation(instance):
    assert isinstance(instance, from_JoinOperation)

@given(instance=sql_from_JoinTableExpression_strategy)
@settings(max_examples=50)
def test_sql_from_jointableexpression_instantiation(instance):
    assert isinstance(instance, sql_from_JoinTableExpression)

@given(instance=from_JoinTableExpression_strategy)
@settings(max_examples=50)
def test_from_jointableexpression_instantiation(instance):
    assert isinstance(instance, from_JoinTableExpression)

@given(instance=from_TableExpression_strategy)
@settings(max_examples=50)
def test_from_tableexpression_instantiation(instance):
    assert isinstance(instance, from_TableExpression)

@given(instance=sql_from_TableListExpression_strategy)
@settings(max_examples=50)
def test_sql_from_tablelistexpression_instantiation(instance):
    assert isinstance(instance, sql_from_TableListExpression)

@given(instance=JoinOperation_strategy)
@settings(max_examples=50)
def test_joinoperation_instantiation(instance):
    assert isinstance(instance, JoinOperation)

@given(instance=sql_from_JoinOperationOuter_strategy)
@settings(max_examples=50)
def test_sql_from_joinoperationouter_instantiation(instance):
    assert isinstance(instance, sql_from_JoinOperationOuter)

@given(instance=sql_from_JoinOperationRight_strategy)
@settings(max_examples=50)
def test_sql_from_joinoperationright_instantiation(instance):
    assert isinstance(instance, sql_from_JoinOperationRight)

@given(instance=sql_from_JoinOperationLeft_strategy)
@settings(max_examples=50)
def test_sql_from_joinoperationleft_instantiation(instance):
    assert isinstance(instance, sql_from_JoinOperationLeft)

@given(instance=sql_from_JoinOperationInner_strategy)
@settings(max_examples=50)
def test_sql_from_joinoperationinner_instantiation(instance):
    assert isinstance(instance, sql_from_JoinOperationInner)

@given(instance=sql_from_JoinOperation_strategy)
@settings(max_examples=50)
def test_sql_from_joinoperation_instantiation(instance):
    assert isinstance(instance, sql_from_JoinOperation)

@given(instance=SelectExpression_strategy)
@settings(max_examples=50)
def test_selectexpression_instantiation(instance):
    assert isinstance(instance, SelectExpression)

@given(instance=sql_from_TableExpression_strategy)
@settings(max_examples=50)
def test_sql_from_tableexpression_instantiation(instance):
    assert isinstance(instance, sql_from_TableExpression)



@given(instance=sql_from_TableExpression_strategy)
def test_sql_from_tableexpression_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=from_TableListExpression_strategy)
@settings(max_examples=50)
def test_from_tablelistexpression_instantiation(instance):
    assert isinstance(instance, from_TableListExpression)

@given(instance=sql_from_FromExpression_strategy)
@settings(max_examples=50)
def test_sql_from_fromexpression_instantiation(instance):
    assert isinstance(instance, sql_from_FromExpression)

@given(instance=sql_column_Column_strategy)
@settings(max_examples=50)
def test_sql_column_column_instantiation(instance):
    assert isinstance(instance, sql_column_Column)



@given(instance=sql_column_Column_strategy)
def test_sql_column_column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql_from_Table_strategy)
@settings(max_examples=50)
def test_sql_from_table_instantiation(instance):
    assert isinstance(instance, sql_from_Table)



@given(instance=sql_from_Table_strategy)
def test_sql_from_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=from_Table_strategy)
@settings(max_examples=50)
def test_from_table_instantiation(instance):
    assert isinstance(instance, from_Table)

@given(instance=sql_column_ColumnOperation_strategy)
@settings(max_examples=50)
def test_sql_column_columnoperation_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnOperation)

@given(instance=column_ColumnOperation_strategy)
@settings(max_examples=50)
def test_column_columnoperation_instantiation(instance):
    assert isinstance(instance, column_ColumnOperation)

@given(instance=expression_Expression_strategy)
@settings(max_examples=50)
def test_expression_expression_instantiation(instance):
    assert isinstance(instance, expression_Expression)

@given(instance=sql_column_SingleColumnExpression_strategy)
@settings(max_examples=50)
def test_sql_column_singlecolumnexpression_instantiation(instance):
    assert isinstance(instance, sql_column_SingleColumnExpression)



@given(instance=sql_column_SingleColumnExpression_strategy)
def test_sql_column_singlecolumnexpression_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=column_SingleColumnExpression_strategy)
@settings(max_examples=50)
def test_column_singlecolumnexpression_instantiation(instance):
    assert isinstance(instance, column_SingleColumnExpression)

@given(instance=sql_column_ColumnExpression_strategy)
@settings(max_examples=50)
def test_sql_column_columnexpression_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnExpression)

@given(instance=ColumnOperation_strategy)
@settings(max_examples=50)
def test_columnoperation_instantiation(instance):
    assert isinstance(instance, ColumnOperation)

@given(instance=sql_column_ColumnOperationMax_strategy)
@settings(max_examples=50)
def test_sql_column_columnoperationmax_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnOperationMax)

@given(instance=sql_column_ColumnOperationAvg_strategy)
@settings(max_examples=50)
def test_sql_column_columnoperationavg_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnOperationAvg)

@given(instance=sql_column_ColumnOperationSome_strategy)
@settings(max_examples=50)
def test_sql_column_columnoperationsome_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnOperationSome)

@given(instance=sql_column_ColumnOperationMin_strategy)
@settings(max_examples=50)
def test_sql_column_columnoperationmin_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnOperationMin)

@given(instance=sql_column_ColumnOperationEvery_strategy)
@settings(max_examples=50)
def test_sql_column_columnoperationevery_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnOperationEvery)

@given(instance=sql_column_ColumnOperationSum_strategy)
@settings(max_examples=50)
def test_sql_column_columnoperationsum_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnOperationSum)

@given(instance=sql_column_ColumnOperationCount_strategy)
@settings(max_examples=50)
def test_sql_column_columnoperationcount_instantiation(instance):
    assert isinstance(instance, sql_column_ColumnOperationCount)

@given(instance=sql_parameter_SelectParameter_strategy)
@settings(max_examples=50)
def test_sql_parameter_selectparameter_instantiation(instance):
    assert isinstance(instance, sql_parameter_SelectParameter)

@given(instance=limit_LimitExpression_strategy)
@settings(max_examples=50)
def test_limit_limitexpression_instantiation(instance):
    assert isinstance(instance, limit_LimitExpression)

@given(instance=orderBy_OrderByExpression_strategy)
@settings(max_examples=50)
def test_orderby_orderbyexpression_instantiation(instance):
    assert isinstance(instance, orderBy_OrderByExpression)

@given(instance=set_SetExpression_strategy)
@settings(max_examples=50)
def test_set_setexpression_instantiation(instance):
    assert isinstance(instance, set_SetExpression)

@given(instance=having_HavingExpression_strategy)
@settings(max_examples=50)
def test_having_havingexpression_instantiation(instance):
    assert isinstance(instance, having_HavingExpression)

@given(instance=SelectParameter_strategy)
@settings(max_examples=50)
def test_selectparameter_instantiation(instance):
    assert isinstance(instance, SelectParameter)

@given(instance=sql_parameter_SelectParameterDistinct_strategy)
@settings(max_examples=50)
def test_sql_parameter_selectparameterdistinct_instantiation(instance):
    assert isinstance(instance, sql_parameter_SelectParameterDistinct)

@given(instance=sql_parameter_SelectParameterAll_strategy)
@settings(max_examples=50)
def test_sql_parameter_selectparameterall_instantiation(instance):
    assert isinstance(instance, sql_parameter_SelectParameterAll)

@given(instance=from_FromExpression_strategy)
@settings(max_examples=50)
def test_from_fromexpression_instantiation(instance):
    assert isinstance(instance, from_FromExpression)

@given(instance=column_ColumnExpression_strategy)
@settings(max_examples=50)
def test_column_columnexpression_instantiation(instance):
    assert isinstance(instance, column_ColumnExpression)

@given(instance=parameter_SelectParameter_strategy)
@settings(max_examples=50)
def test_parameter_selectparameter_instantiation(instance):
    assert isinstance(instance, parameter_SelectParameter)

@given(instance=sql_select_SelectExpression_strategy)
@settings(max_examples=50)
def test_sql_select_selectexpression_instantiation(instance):
    assert isinstance(instance, sql_select_SelectExpression)

@given(instance=groupBy_GroupByExpression_strategy)
@settings(max_examples=50)
def test_groupby_groupbyexpression_instantiation(instance):
    assert isinstance(instance, groupBy_GroupByExpression)

@given(instance=where_WhereExpression_strategy)
@settings(max_examples=50)
def test_where_whereexpression_instantiation(instance):
    assert isinstance(instance, where_WhereExpression)

@given(instance=Date_strategy)
@settings(max_examples=50)
def test_date_instantiation(instance):
    assert isinstance(instance, Date)

@given(instance=sql_sqlDataTypes_TimeStamp_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_timestamp_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_TimeStamp)

@given(instance=sql_sqlDataTypes_DataType_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_datatype_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_DataType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=sql_sqlDataTypes_Date_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_date_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_Date)

@given(instance=sql_sqlDataTypes_Real_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_real_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_Real)

@given(instance=sql_sqlDataTypes_Integer_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_integer_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_Integer)

@given(instance=sql_sqlDataTypes_Double_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_double_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_Double)

@given(instance=sql_sqlDataTypes_Float_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_float_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_Float)

@given(instance=sql_sqlDataTypes_Boolean_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_boolean_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_Boolean)

@given(instance=sql_sqlDataTypes_String_strategy)
@settings(max_examples=50)
def test_sql_sqldatatypes_string_instantiation(instance):
    assert isinstance(instance, sql_sqlDataTypes_String)
