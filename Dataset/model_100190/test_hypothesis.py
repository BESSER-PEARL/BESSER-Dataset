import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleTerm,
    sql::term::SimpleTermFloat,
    sql::term::SimpleTermInteger,
    sql::term::SimpleTermChar,
    sql::term::SimpleTermString,
    BooleanTerm,
    sql::term::BooleanTermFalse,
    sql::term::BooleanTermTrue,
    Term,
    sql::term::CountStarTerm,
    sql::term::ColumnTerm,
    sql::term::SimpleTerm,
    sql::term::StarTerm,
    sql::term::NullTerm,
    sql::term::BooleanTerm,
    sql::term::Term,
    value::ValueFrontOperation,
    value::ValueOperation,
    term::Term,
    Value,
    sql::value::ConditionValue,
    sql::value::FunctionValue,
    sql::value::SimpleValue,
    sql::value::ValueOperation,
    ValueFrontOperation,
    sql::value::ValueFrontOperationMinus,
    sql::value::ValueFrontOperationPlus,
    ValueOperation,
    sql::value::ValueOperationDivide,
    sql::value::ValueOperationParallel,
    sql::value::ValueOperationMultiply,
    sql::value::ValueFrontOperation,
    sql::value::Value,
    ConditionOperation,
    sql::condition::ConditionOperationUnEqual,
    sql::condition::ConditionOperationGreater,
    sql::condition::ConditionOperationGreatEqual,
    sql::condition::ConditionOperationUnEqual2,
    sql::condition::ConditionOperationEqual,
    sql::condition::ConditionOperationLessEqual,
    sql::condition::ConditionOperationLesser,
    sql::condition::ConditionOperation,
    condition::ConditionOperation,
    AndOrExpressionOperation,
    sql::expression::ExpressionOperationAnd,
    ExpressionOperation,
    sql::expression::ExpressionOperationNot,
    sql::expression::AndOrExpressionOperation,
    sql::expression::ExpressionOperation,
    expression::ExpressionOperationNot,
    SimpleCondition,
    sql::condition::IsNullCondition,
    sql::condition::ExistsCondition,
    sql::condition::InCondition,
    sql::condition::LikeCondition,
    sql::condition::BetweenCondition,
    sql::condition::OperationCondition,
    value::Value,
    Condition,
    sql::condition::SimpleCondition,
    sql::condition::Condition,
    sql::expression::ExpressionOperationOr,
    sql::limit::LimitExpression,
    condition::Condition,
    expression::AndOrExpressionOperation,
    Expression,
    sql::expression::SimpleExpression,
    sql::expression::Expression,
    set::SetOperation,
    sql::set::SetExpression,
    sql::having::HavingExpression,
    sql::sqlDataTypes::DataType,
    DataType,
    sql::sqlDataTypes::Boolean,
    sql::sqlDataTypes::Real,
    sql::sqlDataTypes::Date,
    sql::sqlDataTypes::String,
    parameter::SelectParameterDistinct,
    SetOperation,
    sql::set::SetOperationExcept,
    sql::set::SetOperationMinus,
    sql::set::SetOperationIntersect,
    sql::set::SetOperationUnion,
    sql::set::SetOperation,
    sql::groupBy::GroupByExpression,
    sql::orderBy::OrderByParameter,
    OrderByParameter,
    sql::orderBy::OrderByParameterDesc,
    sql::orderBy::OrderByParameterAsc,
    column::Column,
    OrderByExpression,
    sql::orderBy::OrderBySelectExpression,
    sql::orderBy::OrderByColumnExpression,
    orderBy::OrderByParameter,
    sql::orderBy::OrderByExpression,
    sql::where::WhereExpression,
    sql::orderBy::OrderByAliasExpression,
    from::JoinOperation,
    sql::from::JoinTableExpression,
    from::JoinTableExpression,
    from::TableExpression,
    sql::from::TableListExpression,
    JoinOperation,
    sql::from::JoinOperationLeft,
    sql::from::JoinOperationOuter,
    sql::from::JoinOperationRight,
    sql::from::JoinOperationInner,
    sql::from::JoinOperation,
    SelectExpression,
    sql::from::TableExpression,
    from::TableListExpression,
    sql::from::FromExpression,
    sql::column::Column,
    sql::from::Table,
    from::Table,
    sql::column::ColumnOperation,
    column::ColumnOperation,
    expression::Expression,
    sql::column::SingleColumnExpression,
    column::SingleColumnExpression,
    sql::column::ColumnExpression,
    ColumnOperation,
    sql::column::ColumnOperationAvg,
    sql::column::ColumnOperationSum,
    sql::column::ColumnOperationEvery,
    sql::column::ColumnOperationSome,
    sql::column::ColumnOperationMax,
    sql::column::ColumnOperationMin,
    sql::column::ColumnOperationCount,
    sql::parameter::SelectParameter,
    limit::LimitExpression,
    orderBy::OrderByExpression,
    set::SetExpression,
    having::HavingExpression,
    SelectParameter,
    sql::parameter::SelectParameterDistinct,
    sql::parameter::SelectParameterAll,
    from::FromExpression,
    column::ColumnExpression,
    parameter::SelectParameter,
    sql::select::SelectExpression,
    sql::sqlDataTypes::Double,
    sql::sqlDataTypes::Float,
    groupBy::GroupByExpression,
    where::WhereExpression,
    Date,
    sql::sqlDataTypes::TimeStamp,
    sql::sqlDataTypes::Integer,
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



def test_sql::term::simpletermfloat_is_not_abstract():
    assert not inspect.isabstract(sql::term::SimpleTermFloat)


def test_sql::term::simpletermfloat_constructor_exists():
    assert callable(sql::term::SimpleTermFloat.__init__)


def test_sql::term::simpletermfloat_constructor_args():
    sig = inspect.signature(sql::term::SimpleTermFloat.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::simpleterminteger_is_not_abstract():
    assert not inspect.isabstract(sql::term::SimpleTermInteger)


def test_sql::term::simpleterminteger_constructor_exists():
    assert callable(sql::term::SimpleTermInteger.__init__)


def test_sql::term::simpleterminteger_constructor_args():
    sig = inspect.signature(sql::term::SimpleTermInteger.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::simpletermchar_is_not_abstract():
    assert not inspect.isabstract(sql::term::SimpleTermChar)


def test_sql::term::simpletermchar_constructor_exists():
    assert callable(sql::term::SimpleTermChar.__init__)


def test_sql::term::simpletermchar_constructor_args():
    sig = inspect.signature(sql::term::SimpleTermChar.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::simpletermstring_is_not_abstract():
    assert not inspect.isabstract(sql::term::SimpleTermString)


def test_sql::term::simpletermstring_constructor_exists():
    assert callable(sql::term::SimpleTermString.__init__)


def test_sql::term::simpletermstring_constructor_args():
    sig = inspect.signature(sql::term::SimpleTermString.__init__)
    params = list(sig.parameters.keys())



def test_booleanterm_is_not_abstract():
    assert not inspect.isabstract(BooleanTerm)


def test_booleanterm_constructor_exists():
    assert callable(BooleanTerm.__init__)


def test_booleanterm_constructor_args():
    sig = inspect.signature(BooleanTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::booleantermfalse_is_not_abstract():
    assert not inspect.isabstract(sql::term::BooleanTermFalse)


def test_sql::term::booleantermfalse_constructor_exists():
    assert callable(sql::term::BooleanTermFalse.__init__)


def test_sql::term::booleantermfalse_constructor_args():
    sig = inspect.signature(sql::term::BooleanTermFalse.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::booleantermtrue_is_not_abstract():
    assert not inspect.isabstract(sql::term::BooleanTermTrue)


def test_sql::term::booleantermtrue_constructor_exists():
    assert callable(sql::term::BooleanTermTrue.__init__)


def test_sql::term::booleantermtrue_constructor_args():
    sig = inspect.signature(sql::term::BooleanTermTrue.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::countstarterm_is_not_abstract():
    assert not inspect.isabstract(sql::term::CountStarTerm)


def test_sql::term::countstarterm_constructor_exists():
    assert callable(sql::term::CountStarTerm.__init__)


def test_sql::term::countstarterm_constructor_args():
    sig = inspect.signature(sql::term::CountStarTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::columnterm_is_not_abstract():
    assert not inspect.isabstract(sql::term::ColumnTerm)


def test_sql::term::columnterm_constructor_exists():
    assert callable(sql::term::ColumnTerm.__init__)


def test_sql::term::columnterm_constructor_args():
    sig = inspect.signature(sql::term::ColumnTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::simpleterm_is_not_abstract():
    assert not inspect.isabstract(sql::term::SimpleTerm)


def test_sql::term::simpleterm_constructor_exists():
    assert callable(sql::term::SimpleTerm.__init__)


def test_sql::term::simpleterm_constructor_args():
    sig = inspect.signature(sql::term::SimpleTerm.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sql::term::simpleterm_has_value():
    assert hasattr(sql::term::SimpleTerm, "value")
    descriptor = None
    for klass in sql::term::SimpleTerm.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sql::term::starterm_is_not_abstract():
    assert not inspect.isabstract(sql::term::StarTerm)


def test_sql::term::starterm_constructor_exists():
    assert callable(sql::term::StarTerm.__init__)


def test_sql::term::starterm_constructor_args():
    sig = inspect.signature(sql::term::StarTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::nullterm_is_not_abstract():
    assert not inspect.isabstract(sql::term::NullTerm)


def test_sql::term::nullterm_constructor_exists():
    assert callable(sql::term::NullTerm.__init__)


def test_sql::term::nullterm_constructor_args():
    sig = inspect.signature(sql::term::NullTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::booleanterm_is_not_abstract():
    assert not inspect.isabstract(sql::term::BooleanTerm)


def test_sql::term::booleanterm_constructor_exists():
    assert callable(sql::term::BooleanTerm.__init__)


def test_sql::term::booleanterm_constructor_args():
    sig = inspect.signature(sql::term::BooleanTerm.__init__)
    params = list(sig.parameters.keys())



def test_sql::term::term_is_not_abstract():
    assert not inspect.isabstract(sql::term::Term)


def test_sql::term::term_constructor_exists():
    assert callable(sql::term::Term.__init__)


def test_sql::term::term_constructor_args():
    sig = inspect.signature(sql::term::Term.__init__)
    params = list(sig.parameters.keys())



def test_value::valuefrontoperation_is_not_abstract():
    assert not inspect.isabstract(value::ValueFrontOperation)


def test_value::valuefrontoperation_constructor_exists():
    assert callable(value::ValueFrontOperation.__init__)


def test_value::valuefrontoperation_constructor_args():
    sig = inspect.signature(value::ValueFrontOperation.__init__)
    params = list(sig.parameters.keys())



def test_value::valueoperation_is_not_abstract():
    assert not inspect.isabstract(value::ValueOperation)


def test_value::valueoperation_constructor_exists():
    assert callable(value::ValueOperation.__init__)


def test_value::valueoperation_constructor_args():
    sig = inspect.signature(value::ValueOperation.__init__)
    params = list(sig.parameters.keys())



def test_term::term_is_not_abstract():
    assert not inspect.isabstract(term::Term)


def test_term::term_constructor_exists():
    assert callable(term::Term.__init__)


def test_term::term_constructor_args():
    sig = inspect.signature(term::Term.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::conditionvalue_is_not_abstract():
    assert not inspect.isabstract(sql::value::ConditionValue)


def test_sql::value::conditionvalue_constructor_exists():
    assert callable(sql::value::ConditionValue.__init__)


def test_sql::value::conditionvalue_constructor_args():
    sig = inspect.signature(sql::value::ConditionValue.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::functionvalue_is_not_abstract():
    assert not inspect.isabstract(sql::value::FunctionValue)


def test_sql::value::functionvalue_constructor_exists():
    assert callable(sql::value::FunctionValue.__init__)


def test_sql::value::functionvalue_constructor_args():
    sig = inspect.signature(sql::value::FunctionValue.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"

def test_sql::value::functionvalue_has_functionName():
    assert hasattr(sql::value::FunctionValue, "functionName")
    descriptor = None
    for klass in sql::value::FunctionValue.__mro__:
        if "functionName" in klass.__dict__:
            descriptor = klass.__dict__["functionName"]
            break
    assert isinstance(descriptor, property)



def test_sql::value::simplevalue_is_not_abstract():
    assert not inspect.isabstract(sql::value::SimpleValue)


def test_sql::value::simplevalue_constructor_exists():
    assert callable(sql::value::SimpleValue.__init__)


def test_sql::value::simplevalue_constructor_args():
    sig = inspect.signature(sql::value::SimpleValue.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::valueoperation_is_not_abstract():
    assert not inspect.isabstract(sql::value::ValueOperation)


def test_sql::value::valueoperation_constructor_exists():
    assert callable(sql::value::ValueOperation.__init__)


def test_sql::value::valueoperation_constructor_args():
    sig = inspect.signature(sql::value::ValueOperation.__init__)
    params = list(sig.parameters.keys())



def test_valuefrontoperation_is_not_abstract():
    assert not inspect.isabstract(ValueFrontOperation)


def test_valuefrontoperation_constructor_exists():
    assert callable(ValueFrontOperation.__init__)


def test_valuefrontoperation_constructor_args():
    sig = inspect.signature(ValueFrontOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::valuefrontoperationminus_is_not_abstract():
    assert not inspect.isabstract(sql::value::ValueFrontOperationMinus)


def test_sql::value::valuefrontoperationminus_constructor_exists():
    assert callable(sql::value::ValueFrontOperationMinus.__init__)


def test_sql::value::valuefrontoperationminus_constructor_args():
    sig = inspect.signature(sql::value::ValueFrontOperationMinus.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::valuefrontoperationplus_is_not_abstract():
    assert not inspect.isabstract(sql::value::ValueFrontOperationPlus)


def test_sql::value::valuefrontoperationplus_constructor_exists():
    assert callable(sql::value::ValueFrontOperationPlus.__init__)


def test_sql::value::valuefrontoperationplus_constructor_args():
    sig = inspect.signature(sql::value::ValueFrontOperationPlus.__init__)
    params = list(sig.parameters.keys())



def test_valueoperation_is_not_abstract():
    assert not inspect.isabstract(ValueOperation)


def test_valueoperation_constructor_exists():
    assert callable(ValueOperation.__init__)


def test_valueoperation_constructor_args():
    sig = inspect.signature(ValueOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::valueoperationdivide_is_not_abstract():
    assert not inspect.isabstract(sql::value::ValueOperationDivide)


def test_sql::value::valueoperationdivide_constructor_exists():
    assert callable(sql::value::ValueOperationDivide.__init__)


def test_sql::value::valueoperationdivide_constructor_args():
    sig = inspect.signature(sql::value::ValueOperationDivide.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::valueoperationparallel_is_not_abstract():
    assert not inspect.isabstract(sql::value::ValueOperationParallel)


def test_sql::value::valueoperationparallel_constructor_exists():
    assert callable(sql::value::ValueOperationParallel.__init__)


def test_sql::value::valueoperationparallel_constructor_args():
    sig = inspect.signature(sql::value::ValueOperationParallel.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::valueoperationmultiply_is_not_abstract():
    assert not inspect.isabstract(sql::value::ValueOperationMultiply)


def test_sql::value::valueoperationmultiply_constructor_exists():
    assert callable(sql::value::ValueOperationMultiply.__init__)


def test_sql::value::valueoperationmultiply_constructor_args():
    sig = inspect.signature(sql::value::ValueOperationMultiply.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::valuefrontoperation_is_not_abstract():
    assert not inspect.isabstract(sql::value::ValueFrontOperation)


def test_sql::value::valuefrontoperation_constructor_exists():
    assert callable(sql::value::ValueFrontOperation.__init__)


def test_sql::value::valuefrontoperation_constructor_args():
    sig = inspect.signature(sql::value::ValueFrontOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::value::value_is_not_abstract():
    assert not inspect.isabstract(sql::value::Value)


def test_sql::value::value_constructor_exists():
    assert callable(sql::value::Value.__init__)


def test_sql::value::value_constructor_args():
    sig = inspect.signature(sql::value::Value.__init__)
    params = list(sig.parameters.keys())



def test_conditionoperation_is_not_abstract():
    assert not inspect.isabstract(ConditionOperation)


def test_conditionoperation_constructor_exists():
    assert callable(ConditionOperation.__init__)


def test_conditionoperation_constructor_args():
    sig = inspect.signature(ConditionOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::conditionoperationunequal_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ConditionOperationUnEqual)


def test_sql::condition::conditionoperationunequal_constructor_exists():
    assert callable(sql::condition::ConditionOperationUnEqual.__init__)


def test_sql::condition::conditionoperationunequal_constructor_args():
    sig = inspect.signature(sql::condition::ConditionOperationUnEqual.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::conditionoperationgreater_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ConditionOperationGreater)


def test_sql::condition::conditionoperationgreater_constructor_exists():
    assert callable(sql::condition::ConditionOperationGreater.__init__)


def test_sql::condition::conditionoperationgreater_constructor_args():
    sig = inspect.signature(sql::condition::ConditionOperationGreater.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::conditionoperationgreatequal_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ConditionOperationGreatEqual)


def test_sql::condition::conditionoperationgreatequal_constructor_exists():
    assert callable(sql::condition::ConditionOperationGreatEqual.__init__)


def test_sql::condition::conditionoperationgreatequal_constructor_args():
    sig = inspect.signature(sql::condition::ConditionOperationGreatEqual.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::conditionoperationunequal2_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ConditionOperationUnEqual2)


def test_sql::condition::conditionoperationunequal2_constructor_exists():
    assert callable(sql::condition::ConditionOperationUnEqual2.__init__)


def test_sql::condition::conditionoperationunequal2_constructor_args():
    sig = inspect.signature(sql::condition::ConditionOperationUnEqual2.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::conditionoperationequal_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ConditionOperationEqual)


def test_sql::condition::conditionoperationequal_constructor_exists():
    assert callable(sql::condition::ConditionOperationEqual.__init__)


def test_sql::condition::conditionoperationequal_constructor_args():
    sig = inspect.signature(sql::condition::ConditionOperationEqual.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::conditionoperationlessequal_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ConditionOperationLessEqual)


def test_sql::condition::conditionoperationlessequal_constructor_exists():
    assert callable(sql::condition::ConditionOperationLessEqual.__init__)


def test_sql::condition::conditionoperationlessequal_constructor_args():
    sig = inspect.signature(sql::condition::ConditionOperationLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::conditionoperationlesser_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ConditionOperationLesser)


def test_sql::condition::conditionoperationlesser_constructor_exists():
    assert callable(sql::condition::ConditionOperationLesser.__init__)


def test_sql::condition::conditionoperationlesser_constructor_args():
    sig = inspect.signature(sql::condition::ConditionOperationLesser.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::conditionoperation_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ConditionOperation)


def test_sql::condition::conditionoperation_constructor_exists():
    assert callable(sql::condition::ConditionOperation.__init__)


def test_sql::condition::conditionoperation_constructor_args():
    sig = inspect.signature(sql::condition::ConditionOperation.__init__)
    params = list(sig.parameters.keys())



def test_condition::conditionoperation_is_not_abstract():
    assert not inspect.isabstract(condition::ConditionOperation)


def test_condition::conditionoperation_constructor_exists():
    assert callable(condition::ConditionOperation.__init__)


def test_condition::conditionoperation_constructor_args():
    sig = inspect.signature(condition::ConditionOperation.__init__)
    params = list(sig.parameters.keys())



def test_andorexpressionoperation_is_not_abstract():
    assert not inspect.isabstract(AndOrExpressionOperation)


def test_andorexpressionoperation_constructor_exists():
    assert callable(AndOrExpressionOperation.__init__)


def test_andorexpressionoperation_constructor_args():
    sig = inspect.signature(AndOrExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::expressionoperationand_is_not_abstract():
    assert not inspect.isabstract(sql::expression::ExpressionOperationAnd)


def test_sql::expression::expressionoperationand_constructor_exists():
    assert callable(sql::expression::ExpressionOperationAnd.__init__)


def test_sql::expression::expressionoperationand_constructor_args():
    sig = inspect.signature(sql::expression::ExpressionOperationAnd.__init__)
    params = list(sig.parameters.keys())



def test_expressionoperation_is_not_abstract():
    assert not inspect.isabstract(ExpressionOperation)


def test_expressionoperation_constructor_exists():
    assert callable(ExpressionOperation.__init__)


def test_expressionoperation_constructor_args():
    sig = inspect.signature(ExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::expressionoperationnot_is_not_abstract():
    assert not inspect.isabstract(sql::expression::ExpressionOperationNot)


def test_sql::expression::expressionoperationnot_constructor_exists():
    assert callable(sql::expression::ExpressionOperationNot.__init__)


def test_sql::expression::expressionoperationnot_constructor_args():
    sig = inspect.signature(sql::expression::ExpressionOperationNot.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::andorexpressionoperation_is_not_abstract():
    assert not inspect.isabstract(sql::expression::AndOrExpressionOperation)


def test_sql::expression::andorexpressionoperation_constructor_exists():
    assert callable(sql::expression::AndOrExpressionOperation.__init__)


def test_sql::expression::andorexpressionoperation_constructor_args():
    sig = inspect.signature(sql::expression::AndOrExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::expressionoperation_is_not_abstract():
    assert not inspect.isabstract(sql::expression::ExpressionOperation)


def test_sql::expression::expressionoperation_constructor_exists():
    assert callable(sql::expression::ExpressionOperation.__init__)


def test_sql::expression::expressionoperation_constructor_args():
    sig = inspect.signature(sql::expression::ExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_expression::expressionoperationnot_is_not_abstract():
    assert not inspect.isabstract(expression::ExpressionOperationNot)


def test_expression::expressionoperationnot_constructor_exists():
    assert callable(expression::ExpressionOperationNot.__init__)


def test_expression::expressionoperationnot_constructor_args():
    sig = inspect.signature(expression::ExpressionOperationNot.__init__)
    params = list(sig.parameters.keys())



def test_simplecondition_is_not_abstract():
    assert not inspect.isabstract(SimpleCondition)


def test_simplecondition_constructor_exists():
    assert callable(SimpleCondition.__init__)


def test_simplecondition_constructor_args():
    sig = inspect.signature(SimpleCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::isnullcondition_is_not_abstract():
    assert not inspect.isabstract(sql::condition::IsNullCondition)


def test_sql::condition::isnullcondition_constructor_exists():
    assert callable(sql::condition::IsNullCondition.__init__)


def test_sql::condition::isnullcondition_constructor_args():
    sig = inspect.signature(sql::condition::IsNullCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::existscondition_is_not_abstract():
    assert not inspect.isabstract(sql::condition::ExistsCondition)


def test_sql::condition::existscondition_constructor_exists():
    assert callable(sql::condition::ExistsCondition.__init__)


def test_sql::condition::existscondition_constructor_args():
    sig = inspect.signature(sql::condition::ExistsCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::incondition_is_not_abstract():
    assert not inspect.isabstract(sql::condition::InCondition)


def test_sql::condition::incondition_constructor_exists():
    assert callable(sql::condition::InCondition.__init__)


def test_sql::condition::incondition_constructor_args():
    sig = inspect.signature(sql::condition::InCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::likecondition_is_not_abstract():
    assert not inspect.isabstract(sql::condition::LikeCondition)


def test_sql::condition::likecondition_constructor_exists():
    assert callable(sql::condition::LikeCondition.__init__)


def test_sql::condition::likecondition_constructor_args():
    sig = inspect.signature(sql::condition::LikeCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::betweencondition_is_not_abstract():
    assert not inspect.isabstract(sql::condition::BetweenCondition)


def test_sql::condition::betweencondition_constructor_exists():
    assert callable(sql::condition::BetweenCondition.__init__)


def test_sql::condition::betweencondition_constructor_args():
    sig = inspect.signature(sql::condition::BetweenCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::operationcondition_is_not_abstract():
    assert not inspect.isabstract(sql::condition::OperationCondition)


def test_sql::condition::operationcondition_constructor_exists():
    assert callable(sql::condition::OperationCondition.__init__)


def test_sql::condition::operationcondition_constructor_args():
    sig = inspect.signature(sql::condition::OperationCondition.__init__)
    params = list(sig.parameters.keys())



def test_value::value_is_not_abstract():
    assert not inspect.isabstract(value::Value)


def test_value::value_constructor_exists():
    assert callable(value::Value.__init__)


def test_value::value_constructor_args():
    sig = inspect.signature(value::Value.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::simplecondition_is_not_abstract():
    assert not inspect.isabstract(sql::condition::SimpleCondition)


def test_sql::condition::simplecondition_constructor_exists():
    assert callable(sql::condition::SimpleCondition.__init__)


def test_sql::condition::simplecondition_constructor_args():
    sig = inspect.signature(sql::condition::SimpleCondition.__init__)
    params = list(sig.parameters.keys())



def test_sql::condition::condition_is_not_abstract():
    assert not inspect.isabstract(sql::condition::Condition)


def test_sql::condition::condition_constructor_exists():
    assert callable(sql::condition::Condition.__init__)


def test_sql::condition::condition_constructor_args():
    sig = inspect.signature(sql::condition::Condition.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::expressionoperationor_is_not_abstract():
    assert not inspect.isabstract(sql::expression::ExpressionOperationOr)


def test_sql::expression::expressionoperationor_constructor_exists():
    assert callable(sql::expression::ExpressionOperationOr.__init__)


def test_sql::expression::expressionoperationor_constructor_args():
    sig = inspect.signature(sql::expression::ExpressionOperationOr.__init__)
    params = list(sig.parameters.keys())



def test_sql::limit::limitexpression_is_not_abstract():
    assert not inspect.isabstract(sql::limit::LimitExpression)


def test_sql::limit::limitexpression_constructor_exists():
    assert callable(sql::limit::LimitExpression.__init__)


def test_sql::limit::limitexpression_constructor_args():
    sig = inspect.signature(sql::limit::LimitExpression.__init__)
    params = list(sig.parameters.keys())
    assert "limit" in params, "Missing parameter 'limit'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_sql::limit::limitexpression_has_limit():
    assert hasattr(sql::limit::LimitExpression, "limit")
    descriptor = None
    for klass in sql::limit::LimitExpression.__mro__:
        if "limit" in klass.__dict__:
            descriptor = klass.__dict__["limit"]
            break
    assert isinstance(descriptor, property)

def test_sql::limit::limitexpression_has_offset():
    assert hasattr(sql::limit::LimitExpression, "offset")
    descriptor = None
    for klass in sql::limit::LimitExpression.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_condition::condition_is_not_abstract():
    assert not inspect.isabstract(condition::Condition)


def test_condition::condition_constructor_exists():
    assert callable(condition::Condition.__init__)


def test_condition::condition_constructor_args():
    sig = inspect.signature(condition::Condition.__init__)
    params = list(sig.parameters.keys())



def test_expression::andorexpressionoperation_is_not_abstract():
    assert not inspect.isabstract(expression::AndOrExpressionOperation)


def test_expression::andorexpressionoperation_constructor_exists():
    assert callable(expression::AndOrExpressionOperation.__init__)


def test_expression::andorexpressionoperation_constructor_args():
    sig = inspect.signature(expression::AndOrExpressionOperation.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::simpleexpression_is_not_abstract():
    assert not inspect.isabstract(sql::expression::SimpleExpression)


def test_sql::expression::simpleexpression_constructor_exists():
    assert callable(sql::expression::SimpleExpression.__init__)


def test_sql::expression::simpleexpression_constructor_args():
    sig = inspect.signature(sql::expression::SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::expression::expression_is_not_abstract():
    assert not inspect.isabstract(sql::expression::Expression)


def test_sql::expression::expression_constructor_exists():
    assert callable(sql::expression::Expression.__init__)


def test_sql::expression::expression_constructor_args():
    sig = inspect.signature(sql::expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_set::setoperation_is_not_abstract():
    assert not inspect.isabstract(set::SetOperation)


def test_set::setoperation_constructor_exists():
    assert callable(set::SetOperation.__init__)


def test_set::setoperation_constructor_args():
    sig = inspect.signature(set::SetOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::set::setexpression_is_not_abstract():
    assert not inspect.isabstract(sql::set::SetExpression)


def test_sql::set::setexpression_constructor_exists():
    assert callable(sql::set::SetExpression.__init__)


def test_sql::set::setexpression_constructor_args():
    sig = inspect.signature(sql::set::SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::having::havingexpression_is_not_abstract():
    assert not inspect.isabstract(sql::having::HavingExpression)


def test_sql::having::havingexpression_constructor_exists():
    assert callable(sql::having::HavingExpression.__init__)


def test_sql::having::havingexpression_constructor_args():
    sig = inspect.signature(sql::having::HavingExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::datatype_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::DataType)


def test_sql::sqldatatypes::datatype_constructor_exists():
    assert callable(sql::sqlDataTypes::DataType.__init__)


def test_sql::sqldatatypes::datatype_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::DataType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::boolean_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::Boolean)


def test_sql::sqldatatypes::boolean_constructor_exists():
    assert callable(sql::sqlDataTypes::Boolean.__init__)


def test_sql::sqldatatypes::boolean_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::real_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::Real)


def test_sql::sqldatatypes::real_constructor_exists():
    assert callable(sql::sqlDataTypes::Real.__init__)


def test_sql::sqldatatypes::real_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::Real.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::date_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::Date)


def test_sql::sqldatatypes::date_constructor_exists():
    assert callable(sql::sqlDataTypes::Date.__init__)


def test_sql::sqldatatypes::date_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::Date.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::string_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::String)


def test_sql::sqldatatypes::string_constructor_exists():
    assert callable(sql::sqlDataTypes::String.__init__)


def test_sql::sqldatatypes::string_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::String.__init__)
    params = list(sig.parameters.keys())



def test_parameter::selectparameterdistinct_is_not_abstract():
    assert not inspect.isabstract(parameter::SelectParameterDistinct)


def test_parameter::selectparameterdistinct_constructor_exists():
    assert callable(parameter::SelectParameterDistinct.__init__)


def test_parameter::selectparameterdistinct_constructor_args():
    sig = inspect.signature(parameter::SelectParameterDistinct.__init__)
    params = list(sig.parameters.keys())



def test_setoperation_is_not_abstract():
    assert not inspect.isabstract(SetOperation)


def test_setoperation_constructor_exists():
    assert callable(SetOperation.__init__)


def test_setoperation_constructor_args():
    sig = inspect.signature(SetOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::set::setoperationexcept_is_not_abstract():
    assert not inspect.isabstract(sql::set::SetOperationExcept)


def test_sql::set::setoperationexcept_constructor_exists():
    assert callable(sql::set::SetOperationExcept.__init__)


def test_sql::set::setoperationexcept_constructor_args():
    sig = inspect.signature(sql::set::SetOperationExcept.__init__)
    params = list(sig.parameters.keys())



def test_sql::set::setoperationminus_is_not_abstract():
    assert not inspect.isabstract(sql::set::SetOperationMinus)


def test_sql::set::setoperationminus_constructor_exists():
    assert callable(sql::set::SetOperationMinus.__init__)


def test_sql::set::setoperationminus_constructor_args():
    sig = inspect.signature(sql::set::SetOperationMinus.__init__)
    params = list(sig.parameters.keys())



def test_sql::set::setoperationintersect_is_not_abstract():
    assert not inspect.isabstract(sql::set::SetOperationIntersect)


def test_sql::set::setoperationintersect_constructor_exists():
    assert callable(sql::set::SetOperationIntersect.__init__)


def test_sql::set::setoperationintersect_constructor_args():
    sig = inspect.signature(sql::set::SetOperationIntersect.__init__)
    params = list(sig.parameters.keys())



def test_sql::set::setoperationunion_is_not_abstract():
    assert not inspect.isabstract(sql::set::SetOperationUnion)


def test_sql::set::setoperationunion_constructor_exists():
    assert callable(sql::set::SetOperationUnion.__init__)


def test_sql::set::setoperationunion_constructor_args():
    sig = inspect.signature(sql::set::SetOperationUnion.__init__)
    params = list(sig.parameters.keys())



def test_sql::set::setoperation_is_not_abstract():
    assert not inspect.isabstract(sql::set::SetOperation)


def test_sql::set::setoperation_constructor_exists():
    assert callable(sql::set::SetOperation.__init__)


def test_sql::set::setoperation_constructor_args():
    sig = inspect.signature(sql::set::SetOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::groupby::groupbyexpression_is_not_abstract():
    assert not inspect.isabstract(sql::groupBy::GroupByExpression)


def test_sql::groupby::groupbyexpression_constructor_exists():
    assert callable(sql::groupBy::GroupByExpression.__init__)


def test_sql::groupby::groupbyexpression_constructor_args():
    sig = inspect.signature(sql::groupBy::GroupByExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderby::orderbyparameter_is_not_abstract():
    assert not inspect.isabstract(sql::orderBy::OrderByParameter)


def test_sql::orderby::orderbyparameter_constructor_exists():
    assert callable(sql::orderBy::OrderByParameter.__init__)


def test_sql::orderby::orderbyparameter_constructor_args():
    sig = inspect.signature(sql::orderBy::OrderByParameter.__init__)
    params = list(sig.parameters.keys())



def test_orderbyparameter_is_not_abstract():
    assert not inspect.isabstract(OrderByParameter)


def test_orderbyparameter_constructor_exists():
    assert callable(OrderByParameter.__init__)


def test_orderbyparameter_constructor_args():
    sig = inspect.signature(OrderByParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderby::orderbyparameterdesc_is_not_abstract():
    assert not inspect.isabstract(sql::orderBy::OrderByParameterDesc)


def test_sql::orderby::orderbyparameterdesc_constructor_exists():
    assert callable(sql::orderBy::OrderByParameterDesc.__init__)


def test_sql::orderby::orderbyparameterdesc_constructor_args():
    sig = inspect.signature(sql::orderBy::OrderByParameterDesc.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderby::orderbyparameterasc_is_not_abstract():
    assert not inspect.isabstract(sql::orderBy::OrderByParameterAsc)


def test_sql::orderby::orderbyparameterasc_constructor_exists():
    assert callable(sql::orderBy::OrderByParameterAsc.__init__)


def test_sql::orderby::orderbyparameterasc_constructor_args():
    sig = inspect.signature(sql::orderBy::OrderByParameterAsc.__init__)
    params = list(sig.parameters.keys())



def test_column::column_is_not_abstract():
    assert not inspect.isabstract(column::Column)


def test_column::column_constructor_exists():
    assert callable(column::Column.__init__)


def test_column::column_constructor_args():
    sig = inspect.signature(column::Column.__init__)
    params = list(sig.parameters.keys())



def test_orderbyexpression_is_not_abstract():
    assert not inspect.isabstract(OrderByExpression)


def test_orderbyexpression_constructor_exists():
    assert callable(OrderByExpression.__init__)


def test_orderbyexpression_constructor_args():
    sig = inspect.signature(OrderByExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderby::orderbyselectexpression_is_not_abstract():
    assert not inspect.isabstract(sql::orderBy::OrderBySelectExpression)


def test_sql::orderby::orderbyselectexpression_constructor_exists():
    assert callable(sql::orderBy::OrderBySelectExpression.__init__)


def test_sql::orderby::orderbyselectexpression_constructor_args():
    sig = inspect.signature(sql::orderBy::OrderBySelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderby::orderbycolumnexpression_is_not_abstract():
    assert not inspect.isabstract(sql::orderBy::OrderByColumnExpression)


def test_sql::orderby::orderbycolumnexpression_constructor_exists():
    assert callable(sql::orderBy::OrderByColumnExpression.__init__)


def test_sql::orderby::orderbycolumnexpression_constructor_args():
    sig = inspect.signature(sql::orderBy::OrderByColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_orderby::orderbyparameter_is_not_abstract():
    assert not inspect.isabstract(orderBy::OrderByParameter)


def test_orderby::orderbyparameter_constructor_exists():
    assert callable(orderBy::OrderByParameter.__init__)


def test_orderby::orderbyparameter_constructor_args():
    sig = inspect.signature(orderBy::OrderByParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderby::orderbyexpression_is_not_abstract():
    assert not inspect.isabstract(sql::orderBy::OrderByExpression)


def test_sql::orderby::orderbyexpression_constructor_exists():
    assert callable(sql::orderBy::OrderByExpression.__init__)


def test_sql::orderby::orderbyexpression_constructor_args():
    sig = inspect.signature(sql::orderBy::OrderByExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::where::whereexpression_is_not_abstract():
    assert not inspect.isabstract(sql::where::WhereExpression)


def test_sql::where::whereexpression_constructor_exists():
    assert callable(sql::where::WhereExpression.__init__)


def test_sql::where::whereexpression_constructor_args():
    sig = inspect.signature(sql::where::WhereExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::orderby::orderbyaliasexpression_is_not_abstract():
    assert not inspect.isabstract(sql::orderBy::OrderByAliasExpression)


def test_sql::orderby::orderbyaliasexpression_constructor_exists():
    assert callable(sql::orderBy::OrderByAliasExpression.__init__)


def test_sql::orderby::orderbyaliasexpression_constructor_args():
    sig = inspect.signature(sql::orderBy::OrderByAliasExpression.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sql::orderby::orderbyaliasexpression_has_alias():
    assert hasattr(sql::orderBy::OrderByAliasExpression, "alias")
    descriptor = None
    for klass in sql::orderBy::OrderByAliasExpression.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_from::joinoperation_is_not_abstract():
    assert not inspect.isabstract(from::JoinOperation)


def test_from::joinoperation_constructor_exists():
    assert callable(from::JoinOperation.__init__)


def test_from::joinoperation_constructor_args():
    sig = inspect.signature(from::JoinOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::jointableexpression_is_not_abstract():
    assert not inspect.isabstract(sql::from::JoinTableExpression)


def test_sql::from::jointableexpression_constructor_exists():
    assert callable(sql::from::JoinTableExpression.__init__)


def test_sql::from::jointableexpression_constructor_args():
    sig = inspect.signature(sql::from::JoinTableExpression.__init__)
    params = list(sig.parameters.keys())



def test_from::jointableexpression_is_not_abstract():
    assert not inspect.isabstract(from::JoinTableExpression)


def test_from::jointableexpression_constructor_exists():
    assert callable(from::JoinTableExpression.__init__)


def test_from::jointableexpression_constructor_args():
    sig = inspect.signature(from::JoinTableExpression.__init__)
    params = list(sig.parameters.keys())



def test_from::tableexpression_is_not_abstract():
    assert not inspect.isabstract(from::TableExpression)


def test_from::tableexpression_constructor_exists():
    assert callable(from::TableExpression.__init__)


def test_from::tableexpression_constructor_args():
    sig = inspect.signature(from::TableExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::tablelistexpression_is_not_abstract():
    assert not inspect.isabstract(sql::from::TableListExpression)


def test_sql::from::tablelistexpression_constructor_exists():
    assert callable(sql::from::TableListExpression.__init__)


def test_sql::from::tablelistexpression_constructor_args():
    sig = inspect.signature(sql::from::TableListExpression.__init__)
    params = list(sig.parameters.keys())



def test_joinoperation_is_not_abstract():
    assert not inspect.isabstract(JoinOperation)


def test_joinoperation_constructor_exists():
    assert callable(JoinOperation.__init__)


def test_joinoperation_constructor_args():
    sig = inspect.signature(JoinOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::joinoperationleft_is_not_abstract():
    assert not inspect.isabstract(sql::from::JoinOperationLeft)


def test_sql::from::joinoperationleft_constructor_exists():
    assert callable(sql::from::JoinOperationLeft.__init__)


def test_sql::from::joinoperationleft_constructor_args():
    sig = inspect.signature(sql::from::JoinOperationLeft.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::joinoperationouter_is_not_abstract():
    assert not inspect.isabstract(sql::from::JoinOperationOuter)


def test_sql::from::joinoperationouter_constructor_exists():
    assert callable(sql::from::JoinOperationOuter.__init__)


def test_sql::from::joinoperationouter_constructor_args():
    sig = inspect.signature(sql::from::JoinOperationOuter.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::joinoperationright_is_not_abstract():
    assert not inspect.isabstract(sql::from::JoinOperationRight)


def test_sql::from::joinoperationright_constructor_exists():
    assert callable(sql::from::JoinOperationRight.__init__)


def test_sql::from::joinoperationright_constructor_args():
    sig = inspect.signature(sql::from::JoinOperationRight.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::joinoperationinner_is_not_abstract():
    assert not inspect.isabstract(sql::from::JoinOperationInner)


def test_sql::from::joinoperationinner_constructor_exists():
    assert callable(sql::from::JoinOperationInner.__init__)


def test_sql::from::joinoperationinner_constructor_args():
    sig = inspect.signature(sql::from::JoinOperationInner.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::joinoperation_is_not_abstract():
    assert not inspect.isabstract(sql::from::JoinOperation)


def test_sql::from::joinoperation_constructor_exists():
    assert callable(sql::from::JoinOperation.__init__)


def test_sql::from::joinoperation_constructor_args():
    sig = inspect.signature(sql::from::JoinOperation.__init__)
    params = list(sig.parameters.keys())



def test_selectexpression_is_not_abstract():
    assert not inspect.isabstract(SelectExpression)


def test_selectexpression_constructor_exists():
    assert callable(SelectExpression.__init__)


def test_selectexpression_constructor_args():
    sig = inspect.signature(SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::tableexpression_is_not_abstract():
    assert not inspect.isabstract(sql::from::TableExpression)


def test_sql::from::tableexpression_constructor_exists():
    assert callable(sql::from::TableExpression.__init__)


def test_sql::from::tableexpression_constructor_args():
    sig = inspect.signature(sql::from::TableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_sql::from::tableexpression_has_label():
    assert hasattr(sql::from::TableExpression, "label")
    descriptor = None
    for klass in sql::from::TableExpression.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_from::tablelistexpression_is_not_abstract():
    assert not inspect.isabstract(from::TableListExpression)


def test_from::tablelistexpression_constructor_exists():
    assert callable(from::TableListExpression.__init__)


def test_from::tablelistexpression_constructor_args():
    sig = inspect.signature(from::TableListExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::from::fromexpression_is_not_abstract():
    assert not inspect.isabstract(sql::from::FromExpression)


def test_sql::from::fromexpression_constructor_exists():
    assert callable(sql::from::FromExpression.__init__)


def test_sql::from::fromexpression_constructor_args():
    sig = inspect.signature(sql::from::FromExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::column_is_not_abstract():
    assert not inspect.isabstract(sql::column::Column)


def test_sql::column::column_constructor_exists():
    assert callable(sql::column::Column.__init__)


def test_sql::column::column_constructor_args():
    sig = inspect.signature(sql::column::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::column::column_has_name():
    assert hasattr(sql::column::Column, "name")
    descriptor = None
    for klass in sql::column::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sql::from::table_is_not_abstract():
    assert not inspect.isabstract(sql::from::Table)


def test_sql::from::table_constructor_exists():
    assert callable(sql::from::Table.__init__)


def test_sql::from::table_constructor_args():
    sig = inspect.signature(sql::from::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sql::from::table_has_name():
    assert hasattr(sql::from::Table, "name")
    descriptor = None
    for klass in sql::from::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_from::table_is_not_abstract():
    assert not inspect.isabstract(from::Table)


def test_from::table_constructor_exists():
    assert callable(from::Table.__init__)


def test_from::table_constructor_args():
    sig = inspect.signature(from::Table.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnoperation_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnOperation)


def test_sql::column::columnoperation_constructor_exists():
    assert callable(sql::column::ColumnOperation.__init__)


def test_sql::column::columnoperation_constructor_args():
    sig = inspect.signature(sql::column::ColumnOperation.__init__)
    params = list(sig.parameters.keys())



def test_column::columnoperation_is_not_abstract():
    assert not inspect.isabstract(column::ColumnOperation)


def test_column::columnoperation_constructor_exists():
    assert callable(column::ColumnOperation.__init__)


def test_column::columnoperation_constructor_args():
    sig = inspect.signature(column::ColumnOperation.__init__)
    params = list(sig.parameters.keys())



def test_expression::expression_is_not_abstract():
    assert not inspect.isabstract(expression::Expression)


def test_expression::expression_constructor_exists():
    assert callable(expression::Expression.__init__)


def test_expression::expression_constructor_args():
    sig = inspect.signature(expression::Expression.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::singlecolumnexpression_is_not_abstract():
    assert not inspect.isabstract(sql::column::SingleColumnExpression)


def test_sql::column::singlecolumnexpression_constructor_exists():
    assert callable(sql::column::SingleColumnExpression.__init__)


def test_sql::column::singlecolumnexpression_constructor_args():
    sig = inspect.signature(sql::column::SingleColumnExpression.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"

def test_sql::column::singlecolumnexpression_has_alias():
    assert hasattr(sql::column::SingleColumnExpression, "alias")
    descriptor = None
    for klass in sql::column::SingleColumnExpression.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_column::singlecolumnexpression_is_not_abstract():
    assert not inspect.isabstract(column::SingleColumnExpression)


def test_column::singlecolumnexpression_constructor_exists():
    assert callable(column::SingleColumnExpression.__init__)


def test_column::singlecolumnexpression_constructor_args():
    sig = inspect.signature(column::SingleColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnexpression_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnExpression)


def test_sql::column::columnexpression_constructor_exists():
    assert callable(sql::column::ColumnExpression.__init__)


def test_sql::column::columnexpression_constructor_args():
    sig = inspect.signature(sql::column::ColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_columnoperation_is_not_abstract():
    assert not inspect.isabstract(ColumnOperation)


def test_columnoperation_constructor_exists():
    assert callable(ColumnOperation.__init__)


def test_columnoperation_constructor_args():
    sig = inspect.signature(ColumnOperation.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnoperationavg_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnOperationAvg)


def test_sql::column::columnoperationavg_constructor_exists():
    assert callable(sql::column::ColumnOperationAvg.__init__)


def test_sql::column::columnoperationavg_constructor_args():
    sig = inspect.signature(sql::column::ColumnOperationAvg.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnoperationsum_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnOperationSum)


def test_sql::column::columnoperationsum_constructor_exists():
    assert callable(sql::column::ColumnOperationSum.__init__)


def test_sql::column::columnoperationsum_constructor_args():
    sig = inspect.signature(sql::column::ColumnOperationSum.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnoperationevery_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnOperationEvery)


def test_sql::column::columnoperationevery_constructor_exists():
    assert callable(sql::column::ColumnOperationEvery.__init__)


def test_sql::column::columnoperationevery_constructor_args():
    sig = inspect.signature(sql::column::ColumnOperationEvery.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnoperationsome_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnOperationSome)


def test_sql::column::columnoperationsome_constructor_exists():
    assert callable(sql::column::ColumnOperationSome.__init__)


def test_sql::column::columnoperationsome_constructor_args():
    sig = inspect.signature(sql::column::ColumnOperationSome.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnoperationmax_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnOperationMax)


def test_sql::column::columnoperationmax_constructor_exists():
    assert callable(sql::column::ColumnOperationMax.__init__)


def test_sql::column::columnoperationmax_constructor_args():
    sig = inspect.signature(sql::column::ColumnOperationMax.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnoperationmin_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnOperationMin)


def test_sql::column::columnoperationmin_constructor_exists():
    assert callable(sql::column::ColumnOperationMin.__init__)


def test_sql::column::columnoperationmin_constructor_args():
    sig = inspect.signature(sql::column::ColumnOperationMin.__init__)
    params = list(sig.parameters.keys())



def test_sql::column::columnoperationcount_is_not_abstract():
    assert not inspect.isabstract(sql::column::ColumnOperationCount)


def test_sql::column::columnoperationcount_constructor_exists():
    assert callable(sql::column::ColumnOperationCount.__init__)


def test_sql::column::columnoperationcount_constructor_args():
    sig = inspect.signature(sql::column::ColumnOperationCount.__init__)
    params = list(sig.parameters.keys())



def test_sql::parameter::selectparameter_is_not_abstract():
    assert not inspect.isabstract(sql::parameter::SelectParameter)


def test_sql::parameter::selectparameter_constructor_exists():
    assert callable(sql::parameter::SelectParameter.__init__)


def test_sql::parameter::selectparameter_constructor_args():
    sig = inspect.signature(sql::parameter::SelectParameter.__init__)
    params = list(sig.parameters.keys())



def test_limit::limitexpression_is_not_abstract():
    assert not inspect.isabstract(limit::LimitExpression)


def test_limit::limitexpression_constructor_exists():
    assert callable(limit::LimitExpression.__init__)


def test_limit::limitexpression_constructor_args():
    sig = inspect.signature(limit::LimitExpression.__init__)
    params = list(sig.parameters.keys())



def test_orderby::orderbyexpression_is_not_abstract():
    assert not inspect.isabstract(orderBy::OrderByExpression)


def test_orderby::orderbyexpression_constructor_exists():
    assert callable(orderBy::OrderByExpression.__init__)


def test_orderby::orderbyexpression_constructor_args():
    sig = inspect.signature(orderBy::OrderByExpression.__init__)
    params = list(sig.parameters.keys())



def test_set::setexpression_is_not_abstract():
    assert not inspect.isabstract(set::SetExpression)


def test_set::setexpression_constructor_exists():
    assert callable(set::SetExpression.__init__)


def test_set::setexpression_constructor_args():
    sig = inspect.signature(set::SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_having::havingexpression_is_not_abstract():
    assert not inspect.isabstract(having::HavingExpression)


def test_having::havingexpression_constructor_exists():
    assert callable(having::HavingExpression.__init__)


def test_having::havingexpression_constructor_args():
    sig = inspect.signature(having::HavingExpression.__init__)
    params = list(sig.parameters.keys())



def test_selectparameter_is_not_abstract():
    assert not inspect.isabstract(SelectParameter)


def test_selectparameter_constructor_exists():
    assert callable(SelectParameter.__init__)


def test_selectparameter_constructor_args():
    sig = inspect.signature(SelectParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql::parameter::selectparameterdistinct_is_not_abstract():
    assert not inspect.isabstract(sql::parameter::SelectParameterDistinct)


def test_sql::parameter::selectparameterdistinct_constructor_exists():
    assert callable(sql::parameter::SelectParameterDistinct.__init__)


def test_sql::parameter::selectparameterdistinct_constructor_args():
    sig = inspect.signature(sql::parameter::SelectParameterDistinct.__init__)
    params = list(sig.parameters.keys())



def test_sql::parameter::selectparameterall_is_not_abstract():
    assert not inspect.isabstract(sql::parameter::SelectParameterAll)


def test_sql::parameter::selectparameterall_constructor_exists():
    assert callable(sql::parameter::SelectParameterAll.__init__)


def test_sql::parameter::selectparameterall_constructor_args():
    sig = inspect.signature(sql::parameter::SelectParameterAll.__init__)
    params = list(sig.parameters.keys())



def test_from::fromexpression_is_not_abstract():
    assert not inspect.isabstract(from::FromExpression)


def test_from::fromexpression_constructor_exists():
    assert callable(from::FromExpression.__init__)


def test_from::fromexpression_constructor_args():
    sig = inspect.signature(from::FromExpression.__init__)
    params = list(sig.parameters.keys())



def test_column::columnexpression_is_not_abstract():
    assert not inspect.isabstract(column::ColumnExpression)


def test_column::columnexpression_constructor_exists():
    assert callable(column::ColumnExpression.__init__)


def test_column::columnexpression_constructor_args():
    sig = inspect.signature(column::ColumnExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameter::selectparameter_is_not_abstract():
    assert not inspect.isabstract(parameter::SelectParameter)


def test_parameter::selectparameter_constructor_exists():
    assert callable(parameter::SelectParameter.__init__)


def test_parameter::selectparameter_constructor_args():
    sig = inspect.signature(parameter::SelectParameter.__init__)
    params = list(sig.parameters.keys())



def test_sql::select::selectexpression_is_not_abstract():
    assert not inspect.isabstract(sql::select::SelectExpression)


def test_sql::select::selectexpression_constructor_exists():
    assert callable(sql::select::SelectExpression.__init__)


def test_sql::select::selectexpression_constructor_args():
    sig = inspect.signature(sql::select::SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::double_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::Double)


def test_sql::sqldatatypes::double_constructor_exists():
    assert callable(sql::sqlDataTypes::Double.__init__)


def test_sql::sqldatatypes::double_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::Double.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::float_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::Float)


def test_sql::sqldatatypes::float_constructor_exists():
    assert callable(sql::sqlDataTypes::Float.__init__)


def test_sql::sqldatatypes::float_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::Float.__init__)
    params = list(sig.parameters.keys())



def test_groupby::groupbyexpression_is_not_abstract():
    assert not inspect.isabstract(groupBy::GroupByExpression)


def test_groupby::groupbyexpression_constructor_exists():
    assert callable(groupBy::GroupByExpression.__init__)


def test_groupby::groupbyexpression_constructor_args():
    sig = inspect.signature(groupBy::GroupByExpression.__init__)
    params = list(sig.parameters.keys())



def test_where::whereexpression_is_not_abstract():
    assert not inspect.isabstract(where::WhereExpression)


def test_where::whereexpression_constructor_exists():
    assert callable(where::WhereExpression.__init__)


def test_where::whereexpression_constructor_args():
    sig = inspect.signature(where::WhereExpression.__init__)
    params = list(sig.parameters.keys())



def test_date_is_not_abstract():
    assert not inspect.isabstract(Date)


def test_date_constructor_exists():
    assert callable(Date.__init__)


def test_date_constructor_args():
    sig = inspect.signature(Date.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::timestamp_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::TimeStamp)


def test_sql::sqldatatypes::timestamp_constructor_exists():
    assert callable(sql::sqlDataTypes::TimeStamp.__init__)


def test_sql::sqldatatypes::timestamp_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::TimeStamp.__init__)
    params = list(sig.parameters.keys())



def test_sql::sqldatatypes::integer_is_not_abstract():
    assert not inspect.isabstract(sql::sqlDataTypes::Integer)


def test_sql::sqldatatypes::integer_constructor_exists():
    assert callable(sql::sqlDataTypes::Integer.__init__)


def test_sql::sqldatatypes::integer_constructor_args():
    sig = inspect.signature(sql::sqlDataTypes::Integer.__init__)
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
sql::term::SimpleTermFloat_strategy = st.builds(
    sql::term::SimpleTermFloat,
)
sql::term::SimpleTermInteger_strategy = st.builds(
    sql::term::SimpleTermInteger,
)
sql::term::SimpleTermChar_strategy = st.builds(
    sql::term::SimpleTermChar,
)
sql::term::SimpleTermString_strategy = st.builds(
    sql::term::SimpleTermString,
)
BooleanTerm_strategy = st.builds(
    BooleanTerm,
)
sql::term::BooleanTermFalse_strategy = st.builds(
    sql::term::BooleanTermFalse,
)
sql::term::BooleanTermTrue_strategy = st.builds(
    sql::term::BooleanTermTrue,
)
Term_strategy = st.builds(
    Term,
)
sql::term::CountStarTerm_strategy = st.builds(
    sql::term::CountStarTerm,
)
sql::term::ColumnTerm_strategy = st.builds(
    sql::term::ColumnTerm,
)
sql::term::SimpleTerm_strategy = st.builds(
    sql::term::SimpleTerm,
    value=
        safe_text
)
sql::term::StarTerm_strategy = st.builds(
    sql::term::StarTerm,
)
sql::term::NullTerm_strategy = st.builds(
    sql::term::NullTerm,
)
sql::term::BooleanTerm_strategy = st.builds(
    sql::term::BooleanTerm,
)
sql::term::Term_strategy = st.builds(
    sql::term::Term,
)
value::ValueFrontOperation_strategy = st.builds(
    value::ValueFrontOperation,
)
value::ValueOperation_strategy = st.builds(
    value::ValueOperation,
)
term::Term_strategy = st.builds(
    term::Term,
)
Value_strategy = st.builds(
    Value,
)
sql::value::ConditionValue_strategy = st.builds(
    sql::value::ConditionValue,
)
sql::value::FunctionValue_strategy = st.builds(
    sql::value::FunctionValue,
    functionName=
        safe_text
)
sql::value::SimpleValue_strategy = st.builds(
    sql::value::SimpleValue,
)
sql::value::ValueOperation_strategy = st.builds(
    sql::value::ValueOperation,
)
ValueFrontOperation_strategy = st.builds(
    ValueFrontOperation,
)
sql::value::ValueFrontOperationMinus_strategy = st.builds(
    sql::value::ValueFrontOperationMinus,
)
sql::value::ValueFrontOperationPlus_strategy = st.builds(
    sql::value::ValueFrontOperationPlus,
)
ValueOperation_strategy = st.builds(
    ValueOperation,
)
sql::value::ValueOperationDivide_strategy = st.builds(
    sql::value::ValueOperationDivide,
)
sql::value::ValueOperationParallel_strategy = st.builds(
    sql::value::ValueOperationParallel,
)
sql::value::ValueOperationMultiply_strategy = st.builds(
    sql::value::ValueOperationMultiply,
)
sql::value::ValueFrontOperation_strategy = st.builds(
    sql::value::ValueFrontOperation,
)
sql::value::Value_strategy = st.builds(
    sql::value::Value,
)
ConditionOperation_strategy = st.builds(
    ConditionOperation,
)
sql::condition::ConditionOperationUnEqual_strategy = st.builds(
    sql::condition::ConditionOperationUnEqual,
)
sql::condition::ConditionOperationGreater_strategy = st.builds(
    sql::condition::ConditionOperationGreater,
)
sql::condition::ConditionOperationGreatEqual_strategy = st.builds(
    sql::condition::ConditionOperationGreatEqual,
)
sql::condition::ConditionOperationUnEqual2_strategy = st.builds(
    sql::condition::ConditionOperationUnEqual2,
)
sql::condition::ConditionOperationEqual_strategy = st.builds(
    sql::condition::ConditionOperationEqual,
)
sql::condition::ConditionOperationLessEqual_strategy = st.builds(
    sql::condition::ConditionOperationLessEqual,
)
sql::condition::ConditionOperationLesser_strategy = st.builds(
    sql::condition::ConditionOperationLesser,
)
sql::condition::ConditionOperation_strategy = st.builds(
    sql::condition::ConditionOperation,
)
condition::ConditionOperation_strategy = st.builds(
    condition::ConditionOperation,
)
AndOrExpressionOperation_strategy = st.builds(
    AndOrExpressionOperation,
)
sql::expression::ExpressionOperationAnd_strategy = st.builds(
    sql::expression::ExpressionOperationAnd,
)
ExpressionOperation_strategy = st.builds(
    ExpressionOperation,
)
sql::expression::ExpressionOperationNot_strategy = st.builds(
    sql::expression::ExpressionOperationNot,
)
sql::expression::AndOrExpressionOperation_strategy = st.builds(
    sql::expression::AndOrExpressionOperation,
)
sql::expression::ExpressionOperation_strategy = st.builds(
    sql::expression::ExpressionOperation,
)
expression::ExpressionOperationNot_strategy = st.builds(
    expression::ExpressionOperationNot,
)
SimpleCondition_strategy = st.builds(
    SimpleCondition,
)
sql::condition::IsNullCondition_strategy = st.builds(
    sql::condition::IsNullCondition,
)
sql::condition::ExistsCondition_strategy = st.builds(
    sql::condition::ExistsCondition,
)
sql::condition::InCondition_strategy = st.builds(
    sql::condition::InCondition,
)
sql::condition::LikeCondition_strategy = st.builds(
    sql::condition::LikeCondition,
)
sql::condition::BetweenCondition_strategy = st.builds(
    sql::condition::BetweenCondition,
)
sql::condition::OperationCondition_strategy = st.builds(
    sql::condition::OperationCondition,
)
value::Value_strategy = st.builds(
    value::Value,
)
Condition_strategy = st.builds(
    Condition,
)
sql::condition::SimpleCondition_strategy = st.builds(
    sql::condition::SimpleCondition,
)
sql::condition::Condition_strategy = st.builds(
    sql::condition::Condition,
)
sql::expression::ExpressionOperationOr_strategy = st.builds(
    sql::expression::ExpressionOperationOr,
)
sql::limit::LimitExpression_strategy = st.builds(
    sql::limit::LimitExpression,
    limit=
        safe_text,
    offset=
        safe_text
)
condition::Condition_strategy = st.builds(
    condition::Condition,
)
expression::AndOrExpressionOperation_strategy = st.builds(
    expression::AndOrExpressionOperation,
)
Expression_strategy = st.builds(
    Expression,
)
sql::expression::SimpleExpression_strategy = st.builds(
    sql::expression::SimpleExpression,
)
sql::expression::Expression_strategy = st.builds(
    sql::expression::Expression,
)
set::SetOperation_strategy = st.builds(
    set::SetOperation,
)
sql::set::SetExpression_strategy = st.builds(
    sql::set::SetExpression,
)
sql::having::HavingExpression_strategy = st.builds(
    sql::having::HavingExpression,
)
sql::sqlDataTypes::DataType_strategy = st.builds(
    sql::sqlDataTypes::DataType,
)
DataType_strategy = st.builds(
    DataType,
)
sql::sqlDataTypes::Boolean_strategy = st.builds(
    sql::sqlDataTypes::Boolean,
)
sql::sqlDataTypes::Real_strategy = st.builds(
    sql::sqlDataTypes::Real,
)
sql::sqlDataTypes::Date_strategy = st.builds(
    sql::sqlDataTypes::Date,
)
sql::sqlDataTypes::String_strategy = st.builds(
    sql::sqlDataTypes::String,
)
parameter::SelectParameterDistinct_strategy = st.builds(
    parameter::SelectParameterDistinct,
)
SetOperation_strategy = st.builds(
    SetOperation,
)
sql::set::SetOperationExcept_strategy = st.builds(
    sql::set::SetOperationExcept,
)
sql::set::SetOperationMinus_strategy = st.builds(
    sql::set::SetOperationMinus,
)
sql::set::SetOperationIntersect_strategy = st.builds(
    sql::set::SetOperationIntersect,
)
sql::set::SetOperationUnion_strategy = st.builds(
    sql::set::SetOperationUnion,
)
sql::set::SetOperation_strategy = st.builds(
    sql::set::SetOperation,
)
sql::groupBy::GroupByExpression_strategy = st.builds(
    sql::groupBy::GroupByExpression,
)
sql::orderBy::OrderByParameter_strategy = st.builds(
    sql::orderBy::OrderByParameter,
)
OrderByParameter_strategy = st.builds(
    OrderByParameter,
)
sql::orderBy::OrderByParameterDesc_strategy = st.builds(
    sql::orderBy::OrderByParameterDesc,
)
sql::orderBy::OrderByParameterAsc_strategy = st.builds(
    sql::orderBy::OrderByParameterAsc,
)
column::Column_strategy = st.builds(
    column::Column,
)
OrderByExpression_strategy = st.builds(
    OrderByExpression,
)
sql::orderBy::OrderBySelectExpression_strategy = st.builds(
    sql::orderBy::OrderBySelectExpression,
)
sql::orderBy::OrderByColumnExpression_strategy = st.builds(
    sql::orderBy::OrderByColumnExpression,
)
orderBy::OrderByParameter_strategy = st.builds(
    orderBy::OrderByParameter,
)
sql::orderBy::OrderByExpression_strategy = st.builds(
    sql::orderBy::OrderByExpression,
)
sql::where::WhereExpression_strategy = st.builds(
    sql::where::WhereExpression,
)
sql::orderBy::OrderByAliasExpression_strategy = st.builds(
    sql::orderBy::OrderByAliasExpression,
    alias=
        safe_text
)
from::JoinOperation_strategy = st.builds(
    from::JoinOperation,
)
sql::from::JoinTableExpression_strategy = st.builds(
    sql::from::JoinTableExpression,
)
from::JoinTableExpression_strategy = st.builds(
    from::JoinTableExpression,
)
from::TableExpression_strategy = st.builds(
    from::TableExpression,
)
sql::from::TableListExpression_strategy = st.builds(
    sql::from::TableListExpression,
)
JoinOperation_strategy = st.builds(
    JoinOperation,
)
sql::from::JoinOperationLeft_strategy = st.builds(
    sql::from::JoinOperationLeft,
)
sql::from::JoinOperationOuter_strategy = st.builds(
    sql::from::JoinOperationOuter,
)
sql::from::JoinOperationRight_strategy = st.builds(
    sql::from::JoinOperationRight,
)
sql::from::JoinOperationInner_strategy = st.builds(
    sql::from::JoinOperationInner,
)
sql::from::JoinOperation_strategy = st.builds(
    sql::from::JoinOperation,
)
SelectExpression_strategy = st.builds(
    SelectExpression,
)
sql::from::TableExpression_strategy = st.builds(
    sql::from::TableExpression,
    label=
        safe_text
)
from::TableListExpression_strategy = st.builds(
    from::TableListExpression,
)
sql::from::FromExpression_strategy = st.builds(
    sql::from::FromExpression,
)
sql::column::Column_strategy = st.builds(
    sql::column::Column,
    name=
        safe_text
)
sql::from::Table_strategy = st.builds(
    sql::from::Table,
    name=
        safe_text
)
from::Table_strategy = st.builds(
    from::Table,
)
sql::column::ColumnOperation_strategy = st.builds(
    sql::column::ColumnOperation,
)
column::ColumnOperation_strategy = st.builds(
    column::ColumnOperation,
)
expression::Expression_strategy = st.builds(
    expression::Expression,
)
sql::column::SingleColumnExpression_strategy = st.builds(
    sql::column::SingleColumnExpression,
    alias=
        safe_text
)
column::SingleColumnExpression_strategy = st.builds(
    column::SingleColumnExpression,
)
sql::column::ColumnExpression_strategy = st.builds(
    sql::column::ColumnExpression,
)
ColumnOperation_strategy = st.builds(
    ColumnOperation,
)
sql::column::ColumnOperationAvg_strategy = st.builds(
    sql::column::ColumnOperationAvg,
)
sql::column::ColumnOperationSum_strategy = st.builds(
    sql::column::ColumnOperationSum,
)
sql::column::ColumnOperationEvery_strategy = st.builds(
    sql::column::ColumnOperationEvery,
)
sql::column::ColumnOperationSome_strategy = st.builds(
    sql::column::ColumnOperationSome,
)
sql::column::ColumnOperationMax_strategy = st.builds(
    sql::column::ColumnOperationMax,
)
sql::column::ColumnOperationMin_strategy = st.builds(
    sql::column::ColumnOperationMin,
)
sql::column::ColumnOperationCount_strategy = st.builds(
    sql::column::ColumnOperationCount,
)
sql::parameter::SelectParameter_strategy = st.builds(
    sql::parameter::SelectParameter,
)
limit::LimitExpression_strategy = st.builds(
    limit::LimitExpression,
)
orderBy::OrderByExpression_strategy = st.builds(
    orderBy::OrderByExpression,
)
set::SetExpression_strategy = st.builds(
    set::SetExpression,
)
having::HavingExpression_strategy = st.builds(
    having::HavingExpression,
)
SelectParameter_strategy = st.builds(
    SelectParameter,
)
sql::parameter::SelectParameterDistinct_strategy = st.builds(
    sql::parameter::SelectParameterDistinct,
)
sql::parameter::SelectParameterAll_strategy = st.builds(
    sql::parameter::SelectParameterAll,
)
from::FromExpression_strategy = st.builds(
    from::FromExpression,
)
column::ColumnExpression_strategy = st.builds(
    column::ColumnExpression,
)
parameter::SelectParameter_strategy = st.builds(
    parameter::SelectParameter,
)
sql::select::SelectExpression_strategy = st.builds(
    sql::select::SelectExpression,
)
sql::sqlDataTypes::Double_strategy = st.builds(
    sql::sqlDataTypes::Double,
)
sql::sqlDataTypes::Float_strategy = st.builds(
    sql::sqlDataTypes::Float,
)
groupBy::GroupByExpression_strategy = st.builds(
    groupBy::GroupByExpression,
)
where::WhereExpression_strategy = st.builds(
    where::WhereExpression,
)
Date_strategy = st.builds(
    Date,
)
sql::sqlDataTypes::TimeStamp_strategy = st.builds(
    sql::sqlDataTypes::TimeStamp,
)
sql::sqlDataTypes::Integer_strategy = st.builds(
    sql::sqlDataTypes::Integer,
)

@given(instance=SimpleTerm_strategy)
@settings(max_examples=50)
def test_simpleterm_instantiation(instance):
    assert isinstance(instance, SimpleTerm)

@given(instance=sql::term::SimpleTermFloat_strategy)
@settings(max_examples=50)
def test_sql::term::simpletermfloat_instantiation(instance):
    assert isinstance(instance, sql::term::SimpleTermFloat)

@given(instance=sql::term::SimpleTermInteger_strategy)
@settings(max_examples=50)
def test_sql::term::simpleterminteger_instantiation(instance):
    assert isinstance(instance, sql::term::SimpleTermInteger)

@given(instance=sql::term::SimpleTermChar_strategy)
@settings(max_examples=50)
def test_sql::term::simpletermchar_instantiation(instance):
    assert isinstance(instance, sql::term::SimpleTermChar)

@given(instance=sql::term::SimpleTermString_strategy)
@settings(max_examples=50)
def test_sql::term::simpletermstring_instantiation(instance):
    assert isinstance(instance, sql::term::SimpleTermString)

@given(instance=BooleanTerm_strategy)
@settings(max_examples=50)
def test_booleanterm_instantiation(instance):
    assert isinstance(instance, BooleanTerm)

@given(instance=sql::term::BooleanTermFalse_strategy)
@settings(max_examples=50)
def test_sql::term::booleantermfalse_instantiation(instance):
    assert isinstance(instance, sql::term::BooleanTermFalse)

@given(instance=sql::term::BooleanTermTrue_strategy)
@settings(max_examples=50)
def test_sql::term::booleantermtrue_instantiation(instance):
    assert isinstance(instance, sql::term::BooleanTermTrue)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=sql::term::CountStarTerm_strategy)
@settings(max_examples=50)
def test_sql::term::countstarterm_instantiation(instance):
    assert isinstance(instance, sql::term::CountStarTerm)

@given(instance=sql::term::ColumnTerm_strategy)
@settings(max_examples=50)
def test_sql::term::columnterm_instantiation(instance):
    assert isinstance(instance, sql::term::ColumnTerm)

@given(instance=sql::term::SimpleTerm_strategy)
@settings(max_examples=50)
def test_sql::term::simpleterm_instantiation(instance):
    assert isinstance(instance, sql::term::SimpleTerm)

@given(instance=sql::term::SimpleTerm_strategy)
def test_sql::term::simpleterm_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sql::term::SimpleTerm_strategy)
def test_sql::term::simpleterm_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sql::term::StarTerm_strategy)
@settings(max_examples=50)
def test_sql::term::starterm_instantiation(instance):
    assert isinstance(instance, sql::term::StarTerm)

@given(instance=sql::term::NullTerm_strategy)
@settings(max_examples=50)
def test_sql::term::nullterm_instantiation(instance):
    assert isinstance(instance, sql::term::NullTerm)

@given(instance=sql::term::BooleanTerm_strategy)
@settings(max_examples=50)
def test_sql::term::booleanterm_instantiation(instance):
    assert isinstance(instance, sql::term::BooleanTerm)

@given(instance=sql::term::Term_strategy)
@settings(max_examples=50)
def test_sql::term::term_instantiation(instance):
    assert isinstance(instance, sql::term::Term)

@given(instance=value::ValueFrontOperation_strategy)
@settings(max_examples=50)
def test_value::valuefrontoperation_instantiation(instance):
    assert isinstance(instance, value::ValueFrontOperation)

@given(instance=value::ValueOperation_strategy)
@settings(max_examples=50)
def test_value::valueoperation_instantiation(instance):
    assert isinstance(instance, value::ValueOperation)

@given(instance=term::Term_strategy)
@settings(max_examples=50)
def test_term::term_instantiation(instance):
    assert isinstance(instance, term::Term)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=sql::value::ConditionValue_strategy)
@settings(max_examples=50)
def test_sql::value::conditionvalue_instantiation(instance):
    assert isinstance(instance, sql::value::ConditionValue)

@given(instance=sql::value::FunctionValue_strategy)
@settings(max_examples=50)
def test_sql::value::functionvalue_instantiation(instance):
    assert isinstance(instance, sql::value::FunctionValue)

@given(instance=sql::value::FunctionValue_strategy)
def test_sql::value::functionvalue_functionName_type(instance):
    assert isinstance(instance.functionName, str)


@given(instance=sql::value::FunctionValue_strategy)
def test_sql::value::functionvalue_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original

@given(instance=sql::value::SimpleValue_strategy)
@settings(max_examples=50)
def test_sql::value::simplevalue_instantiation(instance):
    assert isinstance(instance, sql::value::SimpleValue)

@given(instance=sql::value::ValueOperation_strategy)
@settings(max_examples=50)
def test_sql::value::valueoperation_instantiation(instance):
    assert isinstance(instance, sql::value::ValueOperation)

@given(instance=ValueFrontOperation_strategy)
@settings(max_examples=50)
def test_valuefrontoperation_instantiation(instance):
    assert isinstance(instance, ValueFrontOperation)

@given(instance=sql::value::ValueFrontOperationMinus_strategy)
@settings(max_examples=50)
def test_sql::value::valuefrontoperationminus_instantiation(instance):
    assert isinstance(instance, sql::value::ValueFrontOperationMinus)

@given(instance=sql::value::ValueFrontOperationPlus_strategy)
@settings(max_examples=50)
def test_sql::value::valuefrontoperationplus_instantiation(instance):
    assert isinstance(instance, sql::value::ValueFrontOperationPlus)

@given(instance=ValueOperation_strategy)
@settings(max_examples=50)
def test_valueoperation_instantiation(instance):
    assert isinstance(instance, ValueOperation)

@given(instance=sql::value::ValueOperationDivide_strategy)
@settings(max_examples=50)
def test_sql::value::valueoperationdivide_instantiation(instance):
    assert isinstance(instance, sql::value::ValueOperationDivide)

@given(instance=sql::value::ValueOperationParallel_strategy)
@settings(max_examples=50)
def test_sql::value::valueoperationparallel_instantiation(instance):
    assert isinstance(instance, sql::value::ValueOperationParallel)

@given(instance=sql::value::ValueOperationMultiply_strategy)
@settings(max_examples=50)
def test_sql::value::valueoperationmultiply_instantiation(instance):
    assert isinstance(instance, sql::value::ValueOperationMultiply)

@given(instance=sql::value::ValueFrontOperation_strategy)
@settings(max_examples=50)
def test_sql::value::valuefrontoperation_instantiation(instance):
    assert isinstance(instance, sql::value::ValueFrontOperation)

@given(instance=sql::value::Value_strategy)
@settings(max_examples=50)
def test_sql::value::value_instantiation(instance):
    assert isinstance(instance, sql::value::Value)

@given(instance=ConditionOperation_strategy)
@settings(max_examples=50)
def test_conditionoperation_instantiation(instance):
    assert isinstance(instance, ConditionOperation)

@given(instance=sql::condition::ConditionOperationUnEqual_strategy)
@settings(max_examples=50)
def test_sql::condition::conditionoperationunequal_instantiation(instance):
    assert isinstance(instance, sql::condition::ConditionOperationUnEqual)

@given(instance=sql::condition::ConditionOperationGreater_strategy)
@settings(max_examples=50)
def test_sql::condition::conditionoperationgreater_instantiation(instance):
    assert isinstance(instance, sql::condition::ConditionOperationGreater)

@given(instance=sql::condition::ConditionOperationGreatEqual_strategy)
@settings(max_examples=50)
def test_sql::condition::conditionoperationgreatequal_instantiation(instance):
    assert isinstance(instance, sql::condition::ConditionOperationGreatEqual)

@given(instance=sql::condition::ConditionOperationUnEqual2_strategy)
@settings(max_examples=50)
def test_sql::condition::conditionoperationunequal2_instantiation(instance):
    assert isinstance(instance, sql::condition::ConditionOperationUnEqual2)

@given(instance=sql::condition::ConditionOperationEqual_strategy)
@settings(max_examples=50)
def test_sql::condition::conditionoperationequal_instantiation(instance):
    assert isinstance(instance, sql::condition::ConditionOperationEqual)

@given(instance=sql::condition::ConditionOperationLessEqual_strategy)
@settings(max_examples=50)
def test_sql::condition::conditionoperationlessequal_instantiation(instance):
    assert isinstance(instance, sql::condition::ConditionOperationLessEqual)

@given(instance=sql::condition::ConditionOperationLesser_strategy)
@settings(max_examples=50)
def test_sql::condition::conditionoperationlesser_instantiation(instance):
    assert isinstance(instance, sql::condition::ConditionOperationLesser)

@given(instance=sql::condition::ConditionOperation_strategy)
@settings(max_examples=50)
def test_sql::condition::conditionoperation_instantiation(instance):
    assert isinstance(instance, sql::condition::ConditionOperation)

@given(instance=condition::ConditionOperation_strategy)
@settings(max_examples=50)
def test_condition::conditionoperation_instantiation(instance):
    assert isinstance(instance, condition::ConditionOperation)

@given(instance=AndOrExpressionOperation_strategy)
@settings(max_examples=50)
def test_andorexpressionoperation_instantiation(instance):
    assert isinstance(instance, AndOrExpressionOperation)

@given(instance=sql::expression::ExpressionOperationAnd_strategy)
@settings(max_examples=50)
def test_sql::expression::expressionoperationand_instantiation(instance):
    assert isinstance(instance, sql::expression::ExpressionOperationAnd)

@given(instance=ExpressionOperation_strategy)
@settings(max_examples=50)
def test_expressionoperation_instantiation(instance):
    assert isinstance(instance, ExpressionOperation)

@given(instance=sql::expression::ExpressionOperationNot_strategy)
@settings(max_examples=50)
def test_sql::expression::expressionoperationnot_instantiation(instance):
    assert isinstance(instance, sql::expression::ExpressionOperationNot)

@given(instance=sql::expression::AndOrExpressionOperation_strategy)
@settings(max_examples=50)
def test_sql::expression::andorexpressionoperation_instantiation(instance):
    assert isinstance(instance, sql::expression::AndOrExpressionOperation)

@given(instance=sql::expression::ExpressionOperation_strategy)
@settings(max_examples=50)
def test_sql::expression::expressionoperation_instantiation(instance):
    assert isinstance(instance, sql::expression::ExpressionOperation)

@given(instance=expression::ExpressionOperationNot_strategy)
@settings(max_examples=50)
def test_expression::expressionoperationnot_instantiation(instance):
    assert isinstance(instance, expression::ExpressionOperationNot)

@given(instance=SimpleCondition_strategy)
@settings(max_examples=50)
def test_simplecondition_instantiation(instance):
    assert isinstance(instance, SimpleCondition)

@given(instance=sql::condition::IsNullCondition_strategy)
@settings(max_examples=50)
def test_sql::condition::isnullcondition_instantiation(instance):
    assert isinstance(instance, sql::condition::IsNullCondition)

@given(instance=sql::condition::ExistsCondition_strategy)
@settings(max_examples=50)
def test_sql::condition::existscondition_instantiation(instance):
    assert isinstance(instance, sql::condition::ExistsCondition)

@given(instance=sql::condition::InCondition_strategy)
@settings(max_examples=50)
def test_sql::condition::incondition_instantiation(instance):
    assert isinstance(instance, sql::condition::InCondition)

@given(instance=sql::condition::LikeCondition_strategy)
@settings(max_examples=50)
def test_sql::condition::likecondition_instantiation(instance):
    assert isinstance(instance, sql::condition::LikeCondition)

@given(instance=sql::condition::BetweenCondition_strategy)
@settings(max_examples=50)
def test_sql::condition::betweencondition_instantiation(instance):
    assert isinstance(instance, sql::condition::BetweenCondition)

@given(instance=sql::condition::OperationCondition_strategy)
@settings(max_examples=50)
def test_sql::condition::operationcondition_instantiation(instance):
    assert isinstance(instance, sql::condition::OperationCondition)

@given(instance=value::Value_strategy)
@settings(max_examples=50)
def test_value::value_instantiation(instance):
    assert isinstance(instance, value::Value)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=sql::condition::SimpleCondition_strategy)
@settings(max_examples=50)
def test_sql::condition::simplecondition_instantiation(instance):
    assert isinstance(instance, sql::condition::SimpleCondition)

@given(instance=sql::condition::Condition_strategy)
@settings(max_examples=50)
def test_sql::condition::condition_instantiation(instance):
    assert isinstance(instance, sql::condition::Condition)

@given(instance=sql::expression::ExpressionOperationOr_strategy)
@settings(max_examples=50)
def test_sql::expression::expressionoperationor_instantiation(instance):
    assert isinstance(instance, sql::expression::ExpressionOperationOr)

@given(instance=sql::limit::LimitExpression_strategy)
@settings(max_examples=50)
def test_sql::limit::limitexpression_instantiation(instance):
    assert isinstance(instance, sql::limit::LimitExpression)

@given(instance=sql::limit::LimitExpression_strategy)
def test_sql::limit::limitexpression_limit_type(instance):
    assert isinstance(instance.limit, str)


@given(instance=sql::limit::LimitExpression_strategy)
def test_sql::limit::limitexpression_limit_setter(instance):
    original = instance.limit
    instance.limit = original
    assert instance.limit == original

@given(instance=sql::limit::LimitExpression_strategy)
def test_sql::limit::limitexpression_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=sql::limit::LimitExpression_strategy)
def test_sql::limit::limitexpression_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=condition::Condition_strategy)
@settings(max_examples=50)
def test_condition::condition_instantiation(instance):
    assert isinstance(instance, condition::Condition)

@given(instance=expression::AndOrExpressionOperation_strategy)
@settings(max_examples=50)
def test_expression::andorexpressionoperation_instantiation(instance):
    assert isinstance(instance, expression::AndOrExpressionOperation)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sql::expression::SimpleExpression_strategy)
@settings(max_examples=50)
def test_sql::expression::simpleexpression_instantiation(instance):
    assert isinstance(instance, sql::expression::SimpleExpression)

@given(instance=sql::expression::Expression_strategy)
@settings(max_examples=50)
def test_sql::expression::expression_instantiation(instance):
    assert isinstance(instance, sql::expression::Expression)

@given(instance=set::SetOperation_strategy)
@settings(max_examples=50)
def test_set::setoperation_instantiation(instance):
    assert isinstance(instance, set::SetOperation)

@given(instance=sql::set::SetExpression_strategy)
@settings(max_examples=50)
def test_sql::set::setexpression_instantiation(instance):
    assert isinstance(instance, sql::set::SetExpression)

@given(instance=sql::having::HavingExpression_strategy)
@settings(max_examples=50)
def test_sql::having::havingexpression_instantiation(instance):
    assert isinstance(instance, sql::having::HavingExpression)

@given(instance=sql::sqlDataTypes::DataType_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::datatype_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::DataType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=sql::sqlDataTypes::Boolean_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::boolean_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::Boolean)

@given(instance=sql::sqlDataTypes::Real_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::real_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::Real)

@given(instance=sql::sqlDataTypes::Date_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::date_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::Date)

@given(instance=sql::sqlDataTypes::String_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::string_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::String)

@given(instance=parameter::SelectParameterDistinct_strategy)
@settings(max_examples=50)
def test_parameter::selectparameterdistinct_instantiation(instance):
    assert isinstance(instance, parameter::SelectParameterDistinct)

@given(instance=SetOperation_strategy)
@settings(max_examples=50)
def test_setoperation_instantiation(instance):
    assert isinstance(instance, SetOperation)

@given(instance=sql::set::SetOperationExcept_strategy)
@settings(max_examples=50)
def test_sql::set::setoperationexcept_instantiation(instance):
    assert isinstance(instance, sql::set::SetOperationExcept)

@given(instance=sql::set::SetOperationMinus_strategy)
@settings(max_examples=50)
def test_sql::set::setoperationminus_instantiation(instance):
    assert isinstance(instance, sql::set::SetOperationMinus)

@given(instance=sql::set::SetOperationIntersect_strategy)
@settings(max_examples=50)
def test_sql::set::setoperationintersect_instantiation(instance):
    assert isinstance(instance, sql::set::SetOperationIntersect)

@given(instance=sql::set::SetOperationUnion_strategy)
@settings(max_examples=50)
def test_sql::set::setoperationunion_instantiation(instance):
    assert isinstance(instance, sql::set::SetOperationUnion)

@given(instance=sql::set::SetOperation_strategy)
@settings(max_examples=50)
def test_sql::set::setoperation_instantiation(instance):
    assert isinstance(instance, sql::set::SetOperation)

@given(instance=sql::groupBy::GroupByExpression_strategy)
@settings(max_examples=50)
def test_sql::groupby::groupbyexpression_instantiation(instance):
    assert isinstance(instance, sql::groupBy::GroupByExpression)

@given(instance=sql::orderBy::OrderByParameter_strategy)
@settings(max_examples=50)
def test_sql::orderby::orderbyparameter_instantiation(instance):
    assert isinstance(instance, sql::orderBy::OrderByParameter)

@given(instance=OrderByParameter_strategy)
@settings(max_examples=50)
def test_orderbyparameter_instantiation(instance):
    assert isinstance(instance, OrderByParameter)

@given(instance=sql::orderBy::OrderByParameterDesc_strategy)
@settings(max_examples=50)
def test_sql::orderby::orderbyparameterdesc_instantiation(instance):
    assert isinstance(instance, sql::orderBy::OrderByParameterDesc)

@given(instance=sql::orderBy::OrderByParameterAsc_strategy)
@settings(max_examples=50)
def test_sql::orderby::orderbyparameterasc_instantiation(instance):
    assert isinstance(instance, sql::orderBy::OrderByParameterAsc)

@given(instance=column::Column_strategy)
@settings(max_examples=50)
def test_column::column_instantiation(instance):
    assert isinstance(instance, column::Column)

@given(instance=OrderByExpression_strategy)
@settings(max_examples=50)
def test_orderbyexpression_instantiation(instance):
    assert isinstance(instance, OrderByExpression)

@given(instance=sql::orderBy::OrderBySelectExpression_strategy)
@settings(max_examples=50)
def test_sql::orderby::orderbyselectexpression_instantiation(instance):
    assert isinstance(instance, sql::orderBy::OrderBySelectExpression)

@given(instance=sql::orderBy::OrderByColumnExpression_strategy)
@settings(max_examples=50)
def test_sql::orderby::orderbycolumnexpression_instantiation(instance):
    assert isinstance(instance, sql::orderBy::OrderByColumnExpression)

@given(instance=orderBy::OrderByParameter_strategy)
@settings(max_examples=50)
def test_orderby::orderbyparameter_instantiation(instance):
    assert isinstance(instance, orderBy::OrderByParameter)

@given(instance=sql::orderBy::OrderByExpression_strategy)
@settings(max_examples=50)
def test_sql::orderby::orderbyexpression_instantiation(instance):
    assert isinstance(instance, sql::orderBy::OrderByExpression)

@given(instance=sql::where::WhereExpression_strategy)
@settings(max_examples=50)
def test_sql::where::whereexpression_instantiation(instance):
    assert isinstance(instance, sql::where::WhereExpression)

@given(instance=sql::orderBy::OrderByAliasExpression_strategy)
@settings(max_examples=50)
def test_sql::orderby::orderbyaliasexpression_instantiation(instance):
    assert isinstance(instance, sql::orderBy::OrderByAliasExpression)

@given(instance=sql::orderBy::OrderByAliasExpression_strategy)
def test_sql::orderby::orderbyaliasexpression_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=sql::orderBy::OrderByAliasExpression_strategy)
def test_sql::orderby::orderbyaliasexpression_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=from::JoinOperation_strategy)
@settings(max_examples=50)
def test_from::joinoperation_instantiation(instance):
    assert isinstance(instance, from::JoinOperation)

@given(instance=sql::from::JoinTableExpression_strategy)
@settings(max_examples=50)
def test_sql::from::jointableexpression_instantiation(instance):
    assert isinstance(instance, sql::from::JoinTableExpression)

@given(instance=from::JoinTableExpression_strategy)
@settings(max_examples=50)
def test_from::jointableexpression_instantiation(instance):
    assert isinstance(instance, from::JoinTableExpression)

@given(instance=from::TableExpression_strategy)
@settings(max_examples=50)
def test_from::tableexpression_instantiation(instance):
    assert isinstance(instance, from::TableExpression)

@given(instance=sql::from::TableListExpression_strategy)
@settings(max_examples=50)
def test_sql::from::tablelistexpression_instantiation(instance):
    assert isinstance(instance, sql::from::TableListExpression)

@given(instance=JoinOperation_strategy)
@settings(max_examples=50)
def test_joinoperation_instantiation(instance):
    assert isinstance(instance, JoinOperation)

@given(instance=sql::from::JoinOperationLeft_strategy)
@settings(max_examples=50)
def test_sql::from::joinoperationleft_instantiation(instance):
    assert isinstance(instance, sql::from::JoinOperationLeft)

@given(instance=sql::from::JoinOperationOuter_strategy)
@settings(max_examples=50)
def test_sql::from::joinoperationouter_instantiation(instance):
    assert isinstance(instance, sql::from::JoinOperationOuter)

@given(instance=sql::from::JoinOperationRight_strategy)
@settings(max_examples=50)
def test_sql::from::joinoperationright_instantiation(instance):
    assert isinstance(instance, sql::from::JoinOperationRight)

@given(instance=sql::from::JoinOperationInner_strategy)
@settings(max_examples=50)
def test_sql::from::joinoperationinner_instantiation(instance):
    assert isinstance(instance, sql::from::JoinOperationInner)

@given(instance=sql::from::JoinOperation_strategy)
@settings(max_examples=50)
def test_sql::from::joinoperation_instantiation(instance):
    assert isinstance(instance, sql::from::JoinOperation)

@given(instance=SelectExpression_strategy)
@settings(max_examples=50)
def test_selectexpression_instantiation(instance):
    assert isinstance(instance, SelectExpression)

@given(instance=sql::from::TableExpression_strategy)
@settings(max_examples=50)
def test_sql::from::tableexpression_instantiation(instance):
    assert isinstance(instance, sql::from::TableExpression)

@given(instance=sql::from::TableExpression_strategy)
def test_sql::from::tableexpression_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=sql::from::TableExpression_strategy)
def test_sql::from::tableexpression_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=from::TableListExpression_strategy)
@settings(max_examples=50)
def test_from::tablelistexpression_instantiation(instance):
    assert isinstance(instance, from::TableListExpression)

@given(instance=sql::from::FromExpression_strategy)
@settings(max_examples=50)
def test_sql::from::fromexpression_instantiation(instance):
    assert isinstance(instance, sql::from::FromExpression)

@given(instance=sql::column::Column_strategy)
@settings(max_examples=50)
def test_sql::column::column_instantiation(instance):
    assert isinstance(instance, sql::column::Column)

@given(instance=sql::column::Column_strategy)
def test_sql::column::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::column::Column_strategy)
def test_sql::column::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sql::from::Table_strategy)
@settings(max_examples=50)
def test_sql::from::table_instantiation(instance):
    assert isinstance(instance, sql::from::Table)

@given(instance=sql::from::Table_strategy)
def test_sql::from::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sql::from::Table_strategy)
def test_sql::from::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=from::Table_strategy)
@settings(max_examples=50)
def test_from::table_instantiation(instance):
    assert isinstance(instance, from::Table)

@given(instance=sql::column::ColumnOperation_strategy)
@settings(max_examples=50)
def test_sql::column::columnoperation_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnOperation)

@given(instance=column::ColumnOperation_strategy)
@settings(max_examples=50)
def test_column::columnoperation_instantiation(instance):
    assert isinstance(instance, column::ColumnOperation)

@given(instance=expression::Expression_strategy)
@settings(max_examples=50)
def test_expression::expression_instantiation(instance):
    assert isinstance(instance, expression::Expression)

@given(instance=sql::column::SingleColumnExpression_strategy)
@settings(max_examples=50)
def test_sql::column::singlecolumnexpression_instantiation(instance):
    assert isinstance(instance, sql::column::SingleColumnExpression)

@given(instance=sql::column::SingleColumnExpression_strategy)
def test_sql::column::singlecolumnexpression_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=sql::column::SingleColumnExpression_strategy)
def test_sql::column::singlecolumnexpression_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=column::SingleColumnExpression_strategy)
@settings(max_examples=50)
def test_column::singlecolumnexpression_instantiation(instance):
    assert isinstance(instance, column::SingleColumnExpression)

@given(instance=sql::column::ColumnExpression_strategy)
@settings(max_examples=50)
def test_sql::column::columnexpression_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnExpression)

@given(instance=ColumnOperation_strategy)
@settings(max_examples=50)
def test_columnoperation_instantiation(instance):
    assert isinstance(instance, ColumnOperation)

@given(instance=sql::column::ColumnOperationAvg_strategy)
@settings(max_examples=50)
def test_sql::column::columnoperationavg_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnOperationAvg)

@given(instance=sql::column::ColumnOperationSum_strategy)
@settings(max_examples=50)
def test_sql::column::columnoperationsum_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnOperationSum)

@given(instance=sql::column::ColumnOperationEvery_strategy)
@settings(max_examples=50)
def test_sql::column::columnoperationevery_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnOperationEvery)

@given(instance=sql::column::ColumnOperationSome_strategy)
@settings(max_examples=50)
def test_sql::column::columnoperationsome_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnOperationSome)

@given(instance=sql::column::ColumnOperationMax_strategy)
@settings(max_examples=50)
def test_sql::column::columnoperationmax_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnOperationMax)

@given(instance=sql::column::ColumnOperationMin_strategy)
@settings(max_examples=50)
def test_sql::column::columnoperationmin_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnOperationMin)

@given(instance=sql::column::ColumnOperationCount_strategy)
@settings(max_examples=50)
def test_sql::column::columnoperationcount_instantiation(instance):
    assert isinstance(instance, sql::column::ColumnOperationCount)

@given(instance=sql::parameter::SelectParameter_strategy)
@settings(max_examples=50)
def test_sql::parameter::selectparameter_instantiation(instance):
    assert isinstance(instance, sql::parameter::SelectParameter)

@given(instance=limit::LimitExpression_strategy)
@settings(max_examples=50)
def test_limit::limitexpression_instantiation(instance):
    assert isinstance(instance, limit::LimitExpression)

@given(instance=orderBy::OrderByExpression_strategy)
@settings(max_examples=50)
def test_orderby::orderbyexpression_instantiation(instance):
    assert isinstance(instance, orderBy::OrderByExpression)

@given(instance=set::SetExpression_strategy)
@settings(max_examples=50)
def test_set::setexpression_instantiation(instance):
    assert isinstance(instance, set::SetExpression)

@given(instance=having::HavingExpression_strategy)
@settings(max_examples=50)
def test_having::havingexpression_instantiation(instance):
    assert isinstance(instance, having::HavingExpression)

@given(instance=SelectParameter_strategy)
@settings(max_examples=50)
def test_selectparameter_instantiation(instance):
    assert isinstance(instance, SelectParameter)

@given(instance=sql::parameter::SelectParameterDistinct_strategy)
@settings(max_examples=50)
def test_sql::parameter::selectparameterdistinct_instantiation(instance):
    assert isinstance(instance, sql::parameter::SelectParameterDistinct)

@given(instance=sql::parameter::SelectParameterAll_strategy)
@settings(max_examples=50)
def test_sql::parameter::selectparameterall_instantiation(instance):
    assert isinstance(instance, sql::parameter::SelectParameterAll)

@given(instance=from::FromExpression_strategy)
@settings(max_examples=50)
def test_from::fromexpression_instantiation(instance):
    assert isinstance(instance, from::FromExpression)

@given(instance=column::ColumnExpression_strategy)
@settings(max_examples=50)
def test_column::columnexpression_instantiation(instance):
    assert isinstance(instance, column::ColumnExpression)

@given(instance=parameter::SelectParameter_strategy)
@settings(max_examples=50)
def test_parameter::selectparameter_instantiation(instance):
    assert isinstance(instance, parameter::SelectParameter)

@given(instance=sql::select::SelectExpression_strategy)
@settings(max_examples=50)
def test_sql::select::selectexpression_instantiation(instance):
    assert isinstance(instance, sql::select::SelectExpression)

@given(instance=sql::sqlDataTypes::Double_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::double_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::Double)

@given(instance=sql::sqlDataTypes::Float_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::float_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::Float)

@given(instance=groupBy::GroupByExpression_strategy)
@settings(max_examples=50)
def test_groupby::groupbyexpression_instantiation(instance):
    assert isinstance(instance, groupBy::GroupByExpression)

@given(instance=where::WhereExpression_strategy)
@settings(max_examples=50)
def test_where::whereexpression_instantiation(instance):
    assert isinstance(instance, where::WhereExpression)

@given(instance=Date_strategy)
@settings(max_examples=50)
def test_date_instantiation(instance):
    assert isinstance(instance, Date)

@given(instance=sql::sqlDataTypes::TimeStamp_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::timestamp_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::TimeStamp)

@given(instance=sql::sqlDataTypes::Integer_strategy)
@settings(max_examples=50)
def test_sql::sqldatatypes::integer_instantiation(instance):
    assert isinstance(instance, sql::sqlDataTypes::Integer)
