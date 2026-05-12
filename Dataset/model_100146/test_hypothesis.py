import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Literal,
    jPQL_FloatLiteral,
    jPQL_BooleanLiteral,
    jPQL_NullLiteral,
    jPQL_IntegerLiteral,
    Variable,
    jPQL_ParameterExpression,
    OrderBySpec,
    jPQL_StringLiteral,
    jPQL_Float,
    FromJoin,
    jPQL_LeftJoin,
    jPQL_InnerJoin,
    jPQL_Join,
    jPQL_FromJoin,
    Expression,
    jPQL_OrExpression,
    jPQL_AndExpression,
    jPQL_AdditionExpression,
    jPQL_FunctionExpression,
    jPQL_MultiplicationExpression,
    jPQL_ExpressionTerm,
    jPQL_ComparisonOperatorExpression,
    SelectAggregateExpression,
    jPQL_CountAggregate,
    jPQL_MinAggregate,
    jPQL_SumAggregate,
    jPQL_MaxAggregate,
    jPQL_AvgAggregate,
    SelectExpression,
    jPQL_SelectConstructorExpression,
    jPQL_SelectAggregateExpression,
    jPQL_SelectExpression,
    jPQL_DeleteClause,
    jPQL_Literal,
    FromEntry,
    jPQL_FromCollection,
    jPQL_FromClass,
    jPQL_VariableDeclaration,
    jPQL_UpdateClause,
    jPQL_OrderBySpec,
    jPQL_Expression,
    jPQL_HavingClause,
    jPQL_AliasAttributeExpression,
    jPQL_OrderByClause,
    jPQL_GroupByClause,
    jPQL_FromClause,
    jPQL_SelectClause,
    ExpressionTerm,
    jPQL_Variable,
    JPQLQuery,
    jPQL_UpdateStatement,
    jPQL_DeleteStatement,
    jPQL_SelectStatement,
    jPQL_WhereClause,
    jPQL_UpdateItem,
    jPQL_FromEntry,
    jPQL_SetClause,
    jPQL_JPQLQuery,
    MultiplicationOperator,
    ComparisonOperator,
    UnaryOperator,
    TrimSpec,
    AdditionOperator,
    OrderByDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_jpql_floatliteral_is_not_abstract():
    assert not inspect.isabstract(jPQL_FloatLiteral)


def test_jpql_floatliteral_constructor_exists():
    assert callable(jPQL_FloatLiteral.__init__)


def test_jpql_floatliteral_constructor_args():
    sig = inspect.signature(jPQL_FloatLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jpql_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(jPQL_BooleanLiteral)


def test_jpql_booleanliteral_constructor_exists():
    assert callable(jPQL_BooleanLiteral.__init__)


def test_jpql_booleanliteral_constructor_args():
    sig = inspect.signature(jPQL_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_booleanliteral_has_value():
    assert hasattr(jPQL_BooleanLiteral, "value")
    descriptor = None
    for klass in jPQL_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jpql_nullliteral_is_not_abstract():
    assert not inspect.isabstract(jPQL_NullLiteral)


def test_jpql_nullliteral_constructor_exists():
    assert callable(jPQL_NullLiteral.__init__)


def test_jpql_nullliteral_constructor_args():
    sig = inspect.signature(jPQL_NullLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_nullliteral_has_value():
    assert hasattr(jPQL_NullLiteral, "value")
    descriptor = None
    for klass in jPQL_NullLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jpql_integerliteral_is_not_abstract():
    assert not inspect.isabstract(jPQL_IntegerLiteral)


def test_jpql_integerliteral_constructor_exists():
    assert callable(jPQL_IntegerLiteral.__init__)


def test_jpql_integerliteral_constructor_args():
    sig = inspect.signature(jPQL_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_integerliteral_has_value():
    assert hasattr(jPQL_IntegerLiteral, "value")
    descriptor = None
    for klass in jPQL_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_jpql_parameterexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_ParameterExpression)


def test_jpql_parameterexpression_constructor_exists():
    assert callable(jPQL_ParameterExpression.__init__)


def test_jpql_parameterexpression_constructor_args():
    sig = inspect.signature(jPQL_ParameterExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"

def test_jpql_parameterexpression_has_name():
    assert hasattr(jPQL_ParameterExpression, "name")
    descriptor = None
    for klass in jPQL_ParameterExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpql_parameterexpression_has_index():
    assert hasattr(jPQL_ParameterExpression, "index")
    descriptor = None
    for klass in jPQL_ParameterExpression.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_orderbyspec_is_not_abstract():
    assert not inspect.isabstract(OrderBySpec)


def test_orderbyspec_constructor_exists():
    assert callable(OrderBySpec.__init__)


def test_orderbyspec_constructor_args():
    sig = inspect.signature(OrderBySpec.__init__)
    params = list(sig.parameters.keys())



def test_jpql_stringliteral_is_not_abstract():
    assert not inspect.isabstract(jPQL_StringLiteral)


def test_jpql_stringliteral_constructor_exists():
    assert callable(jPQL_StringLiteral.__init__)


def test_jpql_stringliteral_constructor_args():
    sig = inspect.signature(jPQL_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_stringliteral_has_value():
    assert hasattr(jPQL_StringLiteral, "value")
    descriptor = None
    for klass in jPQL_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jpql_float_is_not_abstract():
    assert not inspect.isabstract(jPQL_Float)


def test_jpql_float_constructor_exists():
    assert callable(jPQL_Float.__init__)


def test_jpql_float_constructor_args():
    sig = inspect.signature(jPQL_Float.__init__)
    params = list(sig.parameters.keys())
    assert "fractionValue" in params, "Missing parameter 'fractionValue'"
    assert "integerValue" in params, "Missing parameter 'integerValue'"

def test_jpql_float_has_fractionValue():
    assert hasattr(jPQL_Float, "fractionValue")
    descriptor = None
    for klass in jPQL_Float.__mro__:
        if "fractionValue" in klass.__dict__:
            descriptor = klass.__dict__["fractionValue"]
            break
    assert isinstance(descriptor, property)

def test_jpql_float_has_integerValue():
    assert hasattr(jPQL_Float, "integerValue")
    descriptor = None
    for klass in jPQL_Float.__mro__:
        if "integerValue" in klass.__dict__:
            descriptor = klass.__dict__["integerValue"]
            break
    assert isinstance(descriptor, property)



def test_fromjoin_is_not_abstract():
    assert not inspect.isabstract(FromJoin)


def test_fromjoin_constructor_exists():
    assert callable(FromJoin.__init__)


def test_fromjoin_constructor_args():
    sig = inspect.signature(FromJoin.__init__)
    params = list(sig.parameters.keys())



def test_jpql_leftjoin_is_not_abstract():
    assert not inspect.isabstract(jPQL_LeftJoin)


def test_jpql_leftjoin_constructor_exists():
    assert callable(jPQL_LeftJoin.__init__)


def test_jpql_leftjoin_constructor_args():
    sig = inspect.signature(jPQL_LeftJoin.__init__)
    params = list(sig.parameters.keys())
    assert "isOuter" in params, "Missing parameter 'isOuter'"

def test_jpql_leftjoin_has_isOuter():
    assert hasattr(jPQL_LeftJoin, "isOuter")
    descriptor = None
    for klass in jPQL_LeftJoin.__mro__:
        if "isOuter" in klass.__dict__:
            descriptor = klass.__dict__["isOuter"]
            break
    assert isinstance(descriptor, property)



def test_jpql_innerjoin_is_not_abstract():
    assert not inspect.isabstract(jPQL_InnerJoin)


def test_jpql_innerjoin_constructor_exists():
    assert callable(jPQL_InnerJoin.__init__)


def test_jpql_innerjoin_constructor_args():
    sig = inspect.signature(jPQL_InnerJoin.__init__)
    params = list(sig.parameters.keys())



def test_jpql_join_is_not_abstract():
    assert not inspect.isabstract(jPQL_Join)


def test_jpql_join_constructor_exists():
    assert callable(jPQL_Join.__init__)


def test_jpql_join_constructor_args():
    sig = inspect.signature(jPQL_Join.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromjoin_is_not_abstract():
    assert not inspect.isabstract(jPQL_FromJoin)


def test_jpql_fromjoin_constructor_exists():
    assert callable(jPQL_FromJoin.__init__)


def test_jpql_fromjoin_constructor_args():
    sig = inspect.signature(jPQL_FromJoin.__init__)
    params = list(sig.parameters.keys())
    assert "isFetch" in params, "Missing parameter 'isFetch'"

def test_jpql_fromjoin_has_isFetch():
    assert hasattr(jPQL_FromJoin, "isFetch")
    descriptor = None
    for klass in jPQL_FromJoin.__mro__:
        if "isFetch" in klass.__dict__:
            descriptor = klass.__dict__["isFetch"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_orexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_OrExpression)


def test_jpql_orexpression_constructor_exists():
    assert callable(jPQL_OrExpression.__init__)


def test_jpql_orexpression_constructor_args():
    sig = inspect.signature(jPQL_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_andexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_AndExpression)


def test_jpql_andexpression_constructor_exists():
    assert callable(jPQL_AndExpression.__init__)


def test_jpql_andexpression_constructor_args():
    sig = inspect.signature(jPQL_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_additionexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_AdditionExpression)


def test_jpql_additionexpression_constructor_exists():
    assert callable(jPQL_AdditionExpression.__init__)


def test_jpql_additionexpression_constructor_args():
    sig = inspect.signature(jPQL_AdditionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jpql_additionexpression_has_operator():
    assert hasattr(jPQL_AdditionExpression, "operator")
    descriptor = None
    for klass in jPQL_AdditionExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jpql_functionexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_FunctionExpression)


def test_jpql_functionexpression_constructor_exists():
    assert callable(jPQL_FunctionExpression.__init__)


def test_jpql_functionexpression_constructor_args():
    sig = inspect.signature(jPQL_FunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "trimSpec" in params, "Missing parameter 'trimSpec'"

def test_jpql_functionexpression_has_name():
    assert hasattr(jPQL_FunctionExpression, "name")
    descriptor = None
    for klass in jPQL_FunctionExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jpql_functionexpression_has_trimSpec():
    assert hasattr(jPQL_FunctionExpression, "trimSpec")
    descriptor = None
    for klass in jPQL_FunctionExpression.__mro__:
        if "trimSpec" in klass.__dict__:
            descriptor = klass.__dict__["trimSpec"]
            break
    assert isinstance(descriptor, property)



def test_jpql_multiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_MultiplicationExpression)


def test_jpql_multiplicationexpression_constructor_exists():
    assert callable(jPQL_MultiplicationExpression.__init__)


def test_jpql_multiplicationexpression_constructor_args():
    sig = inspect.signature(jPQL_MultiplicationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jpql_multiplicationexpression_has_operator():
    assert hasattr(jPQL_MultiplicationExpression, "operator")
    descriptor = None
    for klass in jPQL_MultiplicationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_jpql_expressionterm_is_not_abstract():
    assert not inspect.isabstract(jPQL_ExpressionTerm)


def test_jpql_expressionterm_constructor_exists():
    assert callable(jPQL_ExpressionTerm.__init__)


def test_jpql_expressionterm_constructor_args():
    sig = inspect.signature(jPQL_ExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_jpql_comparisonoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_ComparisonOperatorExpression)


def test_jpql_comparisonoperatorexpression_constructor_exists():
    assert callable(jPQL_ComparisonOperatorExpression.__init__)


def test_jpql_comparisonoperatorexpression_constructor_args():
    sig = inspect.signature(jPQL_ComparisonOperatorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jpql_comparisonoperatorexpression_has_operator():
    assert hasattr(jPQL_ComparisonOperatorExpression, "operator")
    descriptor = None
    for klass in jPQL_ComparisonOperatorExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_selectaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(SelectAggregateExpression)


def test_selectaggregateexpression_constructor_exists():
    assert callable(SelectAggregateExpression.__init__)


def test_selectaggregateexpression_constructor_args():
    sig = inspect.signature(SelectAggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_countaggregate_is_not_abstract():
    assert not inspect.isabstract(jPQL_CountAggregate)


def test_jpql_countaggregate_constructor_exists():
    assert callable(jPQL_CountAggregate.__init__)


def test_jpql_countaggregate_constructor_args():
    sig = inspect.signature(jPQL_CountAggregate.__init__)
    params = list(sig.parameters.keys())



def test_jpql_minaggregate_is_not_abstract():
    assert not inspect.isabstract(jPQL_MinAggregate)


def test_jpql_minaggregate_constructor_exists():
    assert callable(jPQL_MinAggregate.__init__)


def test_jpql_minaggregate_constructor_args():
    sig = inspect.signature(jPQL_MinAggregate.__init__)
    params = list(sig.parameters.keys())



def test_jpql_sumaggregate_is_not_abstract():
    assert not inspect.isabstract(jPQL_SumAggregate)


def test_jpql_sumaggregate_constructor_exists():
    assert callable(jPQL_SumAggregate.__init__)


def test_jpql_sumaggregate_constructor_args():
    sig = inspect.signature(jPQL_SumAggregate.__init__)
    params = list(sig.parameters.keys())



def test_jpql_maxaggregate_is_not_abstract():
    assert not inspect.isabstract(jPQL_MaxAggregate)


def test_jpql_maxaggregate_constructor_exists():
    assert callable(jPQL_MaxAggregate.__init__)


def test_jpql_maxaggregate_constructor_args():
    sig = inspect.signature(jPQL_MaxAggregate.__init__)
    params = list(sig.parameters.keys())



def test_jpql_avgaggregate_is_not_abstract():
    assert not inspect.isabstract(jPQL_AvgAggregate)


def test_jpql_avgaggregate_constructor_exists():
    assert callable(jPQL_AvgAggregate.__init__)


def test_jpql_avgaggregate_constructor_args():
    sig = inspect.signature(jPQL_AvgAggregate.__init__)
    params = list(sig.parameters.keys())



def test_selectexpression_is_not_abstract():
    assert not inspect.isabstract(SelectExpression)


def test_selectexpression_constructor_exists():
    assert callable(SelectExpression.__init__)


def test_selectexpression_constructor_args():
    sig = inspect.signature(SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_selectconstructorexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_SelectConstructorExpression)


def test_jpql_selectconstructorexpression_constructor_exists():
    assert callable(jPQL_SelectConstructorExpression.__init__)


def test_jpql_selectconstructorexpression_constructor_args():
    sig = inspect.signature(jPQL_SelectConstructorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpql_selectconstructorexpression_has_name():
    assert hasattr(jPQL_SelectConstructorExpression, "name")
    descriptor = None
    for klass in jPQL_SelectConstructorExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpql_selectaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_SelectAggregateExpression)


def test_jpql_selectaggregateexpression_constructor_exists():
    assert callable(jPQL_SelectAggregateExpression.__init__)


def test_jpql_selectaggregateexpression_constructor_args():
    sig = inspect.signature(jPQL_SelectAggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_jpql_selectaggregateexpression_has_isDistinct():
    assert hasattr(jPQL_SelectAggregateExpression, "isDistinct")
    descriptor = None
    for klass in jPQL_SelectAggregateExpression.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_jpql_selectexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_SelectExpression)


def test_jpql_selectexpression_constructor_exists():
    assert callable(jPQL_SelectExpression.__init__)


def test_jpql_selectexpression_constructor_args():
    sig = inspect.signature(jPQL_SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_deleteclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_DeleteClause)


def test_jpql_deleteclause_constructor_exists():
    assert callable(jPQL_DeleteClause.__init__)


def test_jpql_deleteclause_constructor_args():
    sig = inspect.signature(jPQL_DeleteClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_literal_is_not_abstract():
    assert not inspect.isabstract(jPQL_Literal)


def test_jpql_literal_constructor_exists():
    assert callable(jPQL_Literal.__init__)


def test_jpql_literal_constructor_args():
    sig = inspect.signature(jPQL_Literal.__init__)
    params = list(sig.parameters.keys())



def test_fromentry_is_not_abstract():
    assert not inspect.isabstract(FromEntry)


def test_fromentry_constructor_exists():
    assert callable(FromEntry.__init__)


def test_fromentry_constructor_args():
    sig = inspect.signature(FromEntry.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromcollection_is_not_abstract():
    assert not inspect.isabstract(jPQL_FromCollection)


def test_jpql_fromcollection_constructor_exists():
    assert callable(jPQL_FromCollection.__init__)


def test_jpql_fromcollection_constructor_args():
    sig = inspect.signature(jPQL_FromCollection.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromclass_is_not_abstract():
    assert not inspect.isabstract(jPQL_FromClass)


def test_jpql_fromclass_constructor_exists():
    assert callable(jPQL_FromClass.__init__)


def test_jpql_fromclass_constructor_args():
    sig = inspect.signature(jPQL_FromClass.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jpql_fromclass_has_type():
    assert hasattr(jPQL_FromClass, "type")
    descriptor = None
    for klass in jPQL_FromClass.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jpql_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(jPQL_VariableDeclaration)


def test_jpql_variabledeclaration_constructor_exists():
    assert callable(jPQL_VariableDeclaration.__init__)


def test_jpql_variabledeclaration_constructor_args():
    sig = inspect.signature(jPQL_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpql_variabledeclaration_has_name():
    assert hasattr(jPQL_VariableDeclaration, "name")
    descriptor = None
    for klass in jPQL_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpql_updateclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_UpdateClause)


def test_jpql_updateclause_constructor_exists():
    assert callable(jPQL_UpdateClause.__init__)


def test_jpql_updateclause_constructor_args():
    sig = inspect.signature(jPQL_UpdateClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_orderbyspec_is_not_abstract():
    assert not inspect.isabstract(jPQL_OrderBySpec)


def test_jpql_orderbyspec_constructor_exists():
    assert callable(jPQL_OrderBySpec.__init__)


def test_jpql_orderbyspec_constructor_args():
    sig = inspect.signature(jPQL_OrderBySpec.__init__)
    params = list(sig.parameters.keys())



def test_jpql_expression_is_not_abstract():
    assert not inspect.isabstract(jPQL_Expression)


def test_jpql_expression_constructor_exists():
    assert callable(jPQL_Expression.__init__)


def test_jpql_expression_constructor_args():
    sig = inspect.signature(jPQL_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_jpql_expression_has_unaryOperator():
    assert hasattr(jPQL_Expression, "unaryOperator")
    descriptor = None
    for klass in jPQL_Expression.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)

def test_jpql_expression_has_isNot():
    assert hasattr(jPQL_Expression, "isNot")
    descriptor = None
    for klass in jPQL_Expression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_jpql_havingclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_HavingClause)


def test_jpql_havingclause_constructor_exists():
    assert callable(jPQL_HavingClause.__init__)


def test_jpql_havingclause_constructor_args():
    sig = inspect.signature(jPQL_HavingClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_aliasattributeexpression_is_not_abstract():
    assert not inspect.isabstract(jPQL_AliasAttributeExpression)


def test_jpql_aliasattributeexpression_constructor_exists():
    assert callable(jPQL_AliasAttributeExpression.__init__)


def test_jpql_aliasattributeexpression_constructor_args():
    sig = inspect.signature(jPQL_AliasAttributeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "attributes" in params, "Missing parameter 'attributes'"

def test_jpql_aliasattributeexpression_has_direction():
    assert hasattr(jPQL_AliasAttributeExpression, "direction")
    descriptor = None
    for klass in jPQL_AliasAttributeExpression.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_jpql_aliasattributeexpression_has_attributes():
    assert hasattr(jPQL_AliasAttributeExpression, "attributes")
    descriptor = None
    for klass in jPQL_AliasAttributeExpression.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)



def test_jpql_orderbyclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_OrderByClause)


def test_jpql_orderbyclause_constructor_exists():
    assert callable(jPQL_OrderByClause.__init__)


def test_jpql_orderbyclause_constructor_args():
    sig = inspect.signature(jPQL_OrderByClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_groupbyclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_GroupByClause)


def test_jpql_groupbyclause_constructor_exists():
    assert callable(jPQL_GroupByClause.__init__)


def test_jpql_groupbyclause_constructor_args():
    sig = inspect.signature(jPQL_GroupByClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_FromClause)


def test_jpql_fromclause_constructor_exists():
    assert callable(jPQL_FromClause.__init__)


def test_jpql_fromclause_constructor_args():
    sig = inspect.signature(jPQL_FromClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_selectclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_SelectClause)


def test_jpql_selectclause_constructor_exists():
    assert callable(jPQL_SelectClause.__init__)


def test_jpql_selectclause_constructor_args():
    sig = inspect.signature(jPQL_SelectClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_jpql_selectclause_has_isDistinct():
    assert hasattr(jPQL_SelectClause, "isDistinct")
    descriptor = None
    for klass in jPQL_SelectClause.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_expressionterm_is_not_abstract():
    assert not inspect.isabstract(ExpressionTerm)


def test_expressionterm_constructor_exists():
    assert callable(ExpressionTerm.__init__)


def test_expressionterm_constructor_args():
    sig = inspect.signature(ExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_jpql_variable_is_not_abstract():
    assert not inspect.isabstract(jPQL_Variable)


def test_jpql_variable_constructor_exists():
    assert callable(jPQL_Variable.__init__)


def test_jpql_variable_constructor_args():
    sig = inspect.signature(jPQL_Variable.__init__)
    params = list(sig.parameters.keys())



def test_jpqlquery_is_not_abstract():
    assert not inspect.isabstract(JPQLQuery)


def test_jpqlquery_constructor_exists():
    assert callable(JPQLQuery.__init__)


def test_jpqlquery_constructor_args():
    sig = inspect.signature(JPQLQuery.__init__)
    params = list(sig.parameters.keys())



def test_jpql_updatestatement_is_not_abstract():
    assert not inspect.isabstract(jPQL_UpdateStatement)


def test_jpql_updatestatement_constructor_exists():
    assert callable(jPQL_UpdateStatement.__init__)


def test_jpql_updatestatement_constructor_args():
    sig = inspect.signature(jPQL_UpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_jpql_deletestatement_is_not_abstract():
    assert not inspect.isabstract(jPQL_DeleteStatement)


def test_jpql_deletestatement_constructor_exists():
    assert callable(jPQL_DeleteStatement.__init__)


def test_jpql_deletestatement_constructor_args():
    sig = inspect.signature(jPQL_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_jpql_selectstatement_is_not_abstract():
    assert not inspect.isabstract(jPQL_SelectStatement)


def test_jpql_selectstatement_constructor_exists():
    assert callable(jPQL_SelectStatement.__init__)


def test_jpql_selectstatement_constructor_args():
    sig = inspect.signature(jPQL_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_jpql_whereclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_WhereClause)


def test_jpql_whereclause_constructor_exists():
    assert callable(jPQL_WhereClause.__init__)


def test_jpql_whereclause_constructor_args():
    sig = inspect.signature(jPQL_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_updateitem_is_not_abstract():
    assert not inspect.isabstract(jPQL_UpdateItem)


def test_jpql_updateitem_constructor_exists():
    assert callable(jPQL_UpdateItem.__init__)


def test_jpql_updateitem_constructor_args():
    sig = inspect.signature(jPQL_UpdateItem.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromentry_is_not_abstract():
    assert not inspect.isabstract(jPQL_FromEntry)


def test_jpql_fromentry_constructor_exists():
    assert callable(jPQL_FromEntry.__init__)


def test_jpql_fromentry_constructor_args():
    sig = inspect.signature(jPQL_FromEntry.__init__)
    params = list(sig.parameters.keys())



def test_jpql_setclause_is_not_abstract():
    assert not inspect.isabstract(jPQL_SetClause)


def test_jpql_setclause_constructor_exists():
    assert callable(jPQL_SetClause.__init__)


def test_jpql_setclause_constructor_args():
    sig = inspect.signature(jPQL_SetClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_jpqlquery_is_not_abstract():
    assert not inspect.isabstract(jPQL_JPQLQuery)


def test_jpql_jpqlquery_constructor_exists():
    assert callable(jPQL_JPQLQuery.__init__)


def test_jpql_jpqlquery_constructor_args():
    sig = inspect.signature(jPQL_JPQLQuery.__init__)
    params = list(sig.parameters.keys())

def test_multiplicationoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicationOperator is not None

def test_multiplicationoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicationOperator]
    expected_literals = [
        "multiply",
        "divide",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicationOperator"

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "lessThen",
        "equal",
        "greaterThen",
        "notEqual",
        "greaterEqual",
        "lessEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "logicalNot",
        "positive",
        "negative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_trimspec_exists():
    # Check that the Enumeration exists
    assert TrimSpec is not None

def test_trimspec_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TrimSpec]
    expected_literals = [
        "leading",
        "both",
        "trailing",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TrimSpec"

def test_additionoperator_exists():
    # Check that the Enumeration exists
    assert AdditionOperator is not None

def test_additionoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditionOperator]
    expected_literals = [
        "add",
        "subtract",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditionOperator"

def test_orderbydirection_exists():
    # Check that the Enumeration exists
    assert OrderByDirection is not None

def test_orderbydirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrderByDirection]
    expected_literals = [
        "desc",
        "asc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrderByDirection"


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
Literal_strategy = st.builds(
    Literal,
)
jPQL_FloatLiteral_strategy = st.builds(
    jPQL_FloatLiteral,
)
jPQL_BooleanLiteral_strategy = st.builds(
    jPQL_BooleanLiteral,
    value=
        safe_text
)
jPQL_NullLiteral_strategy = st.builds(
    jPQL_NullLiteral,
    value=
        safe_text
)
jPQL_IntegerLiteral_strategy = st.builds(
    jPQL_IntegerLiteral,
    value=
        st.integers()
)
Variable_strategy = st.builds(
    Variable,
)
jPQL_ParameterExpression_strategy = st.builds(
    jPQL_ParameterExpression,
    name=
        safe_text,
    index=
        st.integers()
)
OrderBySpec_strategy = st.builds(
    OrderBySpec,
)
jPQL_StringLiteral_strategy = st.builds(
    jPQL_StringLiteral,
    value=
        safe_text
)
jPQL_Float_strategy = st.builds(
    jPQL_Float,
    fractionValue=
        st.integers(),
    integerValue=
        st.integers()
)
FromJoin_strategy = st.builds(
    FromJoin,
)
jPQL_LeftJoin_strategy = st.builds(
    jPQL_LeftJoin,
    isOuter=
        st.booleans()
)
jPQL_InnerJoin_strategy = st.builds(
    jPQL_InnerJoin,
)
jPQL_Join_strategy = st.builds(
    jPQL_Join,
)
jPQL_FromJoin_strategy = st.builds(
    jPQL_FromJoin,
    isFetch=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
jPQL_OrExpression_strategy = st.builds(
    jPQL_OrExpression,
)
jPQL_AndExpression_strategy = st.builds(
    jPQL_AndExpression,
)
jPQL_AdditionExpression_strategy = st.builds(
    jPQL_AdditionExpression,
    operator=
        safe_text
)
jPQL_FunctionExpression_strategy = st.builds(
    jPQL_FunctionExpression,
    name=
        safe_text,
    trimSpec=
        safe_text
)
jPQL_MultiplicationExpression_strategy = st.builds(
    jPQL_MultiplicationExpression,
    operator=
        safe_text
)
jPQL_ExpressionTerm_strategy = st.builds(
    jPQL_ExpressionTerm,
)
jPQL_ComparisonOperatorExpression_strategy = st.builds(
    jPQL_ComparisonOperatorExpression,
    operator=
        safe_text
)
SelectAggregateExpression_strategy = st.builds(
    SelectAggregateExpression,
)
jPQL_CountAggregate_strategy = st.builds(
    jPQL_CountAggregate,
)
jPQL_MinAggregate_strategy = st.builds(
    jPQL_MinAggregate,
)
jPQL_SumAggregate_strategy = st.builds(
    jPQL_SumAggregate,
)
jPQL_MaxAggregate_strategy = st.builds(
    jPQL_MaxAggregate,
)
jPQL_AvgAggregate_strategy = st.builds(
    jPQL_AvgAggregate,
)
SelectExpression_strategy = st.builds(
    SelectExpression,
)
jPQL_SelectConstructorExpression_strategy = st.builds(
    jPQL_SelectConstructorExpression,
    name=
        safe_text
)
jPQL_SelectAggregateExpression_strategy = st.builds(
    jPQL_SelectAggregateExpression,
    isDistinct=
        st.booleans()
)
jPQL_SelectExpression_strategy = st.builds(
    jPQL_SelectExpression,
)
jPQL_DeleteClause_strategy = st.builds(
    jPQL_DeleteClause,
)
jPQL_Literal_strategy = st.builds(
    jPQL_Literal,
)
FromEntry_strategy = st.builds(
    FromEntry,
)
jPQL_FromCollection_strategy = st.builds(
    jPQL_FromCollection,
)
jPQL_FromClass_strategy = st.builds(
    jPQL_FromClass,
    type=
        safe_text
)
jPQL_VariableDeclaration_strategy = st.builds(
    jPQL_VariableDeclaration,
    name=
        safe_text
)
jPQL_UpdateClause_strategy = st.builds(
    jPQL_UpdateClause,
)
jPQL_OrderBySpec_strategy = st.builds(
    jPQL_OrderBySpec,
)
jPQL_Expression_strategy = st.builds(
    jPQL_Expression,
    unaryOperator=
        safe_text,
    isNot=
        st.booleans()
)
jPQL_HavingClause_strategy = st.builds(
    jPQL_HavingClause,
)
jPQL_AliasAttributeExpression_strategy = st.builds(
    jPQL_AliasAttributeExpression,
    direction=
        safe_text,
    attributes=
        safe_text
)
jPQL_OrderByClause_strategy = st.builds(
    jPQL_OrderByClause,
)
jPQL_GroupByClause_strategy = st.builds(
    jPQL_GroupByClause,
)
jPQL_FromClause_strategy = st.builds(
    jPQL_FromClause,
)
jPQL_SelectClause_strategy = st.builds(
    jPQL_SelectClause,
    isDistinct=
        st.booleans()
)
ExpressionTerm_strategy = st.builds(
    ExpressionTerm,
)
jPQL_Variable_strategy = st.builds(
    jPQL_Variable,
)
JPQLQuery_strategy = st.builds(
    JPQLQuery,
)
jPQL_UpdateStatement_strategy = st.builds(
    jPQL_UpdateStatement,
)
jPQL_DeleteStatement_strategy = st.builds(
    jPQL_DeleteStatement,
)
jPQL_SelectStatement_strategy = st.builds(
    jPQL_SelectStatement,
)
jPQL_WhereClause_strategy = st.builds(
    jPQL_WhereClause,
)
jPQL_UpdateItem_strategy = st.builds(
    jPQL_UpdateItem,
)
jPQL_FromEntry_strategy = st.builds(
    jPQL_FromEntry,
)
jPQL_SetClause_strategy = st.builds(
    jPQL_SetClause,
)
jPQL_JPQLQuery_strategy = st.builds(
    jPQL_JPQLQuery,
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=jPQL_FloatLiteral_strategy)
@settings(max_examples=50)
def test_jpql_floatliteral_instantiation(instance):
    assert isinstance(instance, jPQL_FloatLiteral)

@given(instance=jPQL_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_jpql_booleanliteral_instantiation(instance):
    assert isinstance(instance, jPQL_BooleanLiteral)



@given(instance=jPQL_BooleanLiteral_strategy)
def test_jpql_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jPQL_NullLiteral_strategy)
@settings(max_examples=50)
def test_jpql_nullliteral_instantiation(instance):
    assert isinstance(instance, jPQL_NullLiteral)



@given(instance=jPQL_NullLiteral_strategy)
def test_jpql_nullliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jPQL_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_jpql_integerliteral_instantiation(instance):
    assert isinstance(instance, jPQL_IntegerLiteral)



@given(instance=jPQL_IntegerLiteral_strategy)
def test_jpql_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=jPQL_ParameterExpression_strategy)
@settings(max_examples=50)
def test_jpql_parameterexpression_instantiation(instance):
    assert isinstance(instance, jPQL_ParameterExpression)



@given(instance=jPQL_ParameterExpression_strategy)
def test_jpql_parameterexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jPQL_ParameterExpression_strategy)
def test_jpql_parameterexpression_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=OrderBySpec_strategy)
@settings(max_examples=50)
def test_orderbyspec_instantiation(instance):
    assert isinstance(instance, OrderBySpec)

@given(instance=jPQL_StringLiteral_strategy)
@settings(max_examples=50)
def test_jpql_stringliteral_instantiation(instance):
    assert isinstance(instance, jPQL_StringLiteral)



@given(instance=jPQL_StringLiteral_strategy)
def test_jpql_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jPQL_Float_strategy)
@settings(max_examples=50)
def test_jpql_float_instantiation(instance):
    assert isinstance(instance, jPQL_Float)



@given(instance=jPQL_Float_strategy)
def test_jpql_float_fractionValue_setter(instance):
    original = instance.fractionValue
    instance.fractionValue = original
    assert instance.fractionValue == original



@given(instance=jPQL_Float_strategy)
def test_jpql_float_integerValue_setter(instance):
    original = instance.integerValue
    instance.integerValue = original
    assert instance.integerValue == original

@given(instance=FromJoin_strategy)
@settings(max_examples=50)
def test_fromjoin_instantiation(instance):
    assert isinstance(instance, FromJoin)

@given(instance=jPQL_LeftJoin_strategy)
@settings(max_examples=50)
def test_jpql_leftjoin_instantiation(instance):
    assert isinstance(instance, jPQL_LeftJoin)



@given(instance=jPQL_LeftJoin_strategy)
def test_jpql_leftjoin_isOuter_setter(instance):
    original = instance.isOuter
    instance.isOuter = original
    assert instance.isOuter == original

@given(instance=jPQL_InnerJoin_strategy)
@settings(max_examples=50)
def test_jpql_innerjoin_instantiation(instance):
    assert isinstance(instance, jPQL_InnerJoin)

@given(instance=jPQL_Join_strategy)
@settings(max_examples=50)
def test_jpql_join_instantiation(instance):
    assert isinstance(instance, jPQL_Join)

@given(instance=jPQL_FromJoin_strategy)
@settings(max_examples=50)
def test_jpql_fromjoin_instantiation(instance):
    assert isinstance(instance, jPQL_FromJoin)



@given(instance=jPQL_FromJoin_strategy)
def test_jpql_fromjoin_isFetch_setter(instance):
    original = instance.isFetch
    instance.isFetch = original
    assert instance.isFetch == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=jPQL_OrExpression_strategy)
@settings(max_examples=50)
def test_jpql_orexpression_instantiation(instance):
    assert isinstance(instance, jPQL_OrExpression)

@given(instance=jPQL_AndExpression_strategy)
@settings(max_examples=50)
def test_jpql_andexpression_instantiation(instance):
    assert isinstance(instance, jPQL_AndExpression)

@given(instance=jPQL_AdditionExpression_strategy)
@settings(max_examples=50)
def test_jpql_additionexpression_instantiation(instance):
    assert isinstance(instance, jPQL_AdditionExpression)



@given(instance=jPQL_AdditionExpression_strategy)
def test_jpql_additionexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=jPQL_FunctionExpression_strategy)
@settings(max_examples=50)
def test_jpql_functionexpression_instantiation(instance):
    assert isinstance(instance, jPQL_FunctionExpression)



@given(instance=jPQL_FunctionExpression_strategy)
def test_jpql_functionexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=jPQL_FunctionExpression_strategy)
def test_jpql_functionexpression_trimSpec_setter(instance):
    original = instance.trimSpec
    instance.trimSpec = original
    assert instance.trimSpec == original

@given(instance=jPQL_MultiplicationExpression_strategy)
@settings(max_examples=50)
def test_jpql_multiplicationexpression_instantiation(instance):
    assert isinstance(instance, jPQL_MultiplicationExpression)



@given(instance=jPQL_MultiplicationExpression_strategy)
def test_jpql_multiplicationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=jPQL_ExpressionTerm_strategy)
@settings(max_examples=50)
def test_jpql_expressionterm_instantiation(instance):
    assert isinstance(instance, jPQL_ExpressionTerm)

@given(instance=jPQL_ComparisonOperatorExpression_strategy)
@settings(max_examples=50)
def test_jpql_comparisonoperatorexpression_instantiation(instance):
    assert isinstance(instance, jPQL_ComparisonOperatorExpression)



@given(instance=jPQL_ComparisonOperatorExpression_strategy)
def test_jpql_comparisonoperatorexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=SelectAggregateExpression_strategy)
@settings(max_examples=50)
def test_selectaggregateexpression_instantiation(instance):
    assert isinstance(instance, SelectAggregateExpression)

@given(instance=jPQL_CountAggregate_strategy)
@settings(max_examples=50)
def test_jpql_countaggregate_instantiation(instance):
    assert isinstance(instance, jPQL_CountAggregate)

@given(instance=jPQL_MinAggregate_strategy)
@settings(max_examples=50)
def test_jpql_minaggregate_instantiation(instance):
    assert isinstance(instance, jPQL_MinAggregate)

@given(instance=jPQL_SumAggregate_strategy)
@settings(max_examples=50)
def test_jpql_sumaggregate_instantiation(instance):
    assert isinstance(instance, jPQL_SumAggregate)

@given(instance=jPQL_MaxAggregate_strategy)
@settings(max_examples=50)
def test_jpql_maxaggregate_instantiation(instance):
    assert isinstance(instance, jPQL_MaxAggregate)

@given(instance=jPQL_AvgAggregate_strategy)
@settings(max_examples=50)
def test_jpql_avgaggregate_instantiation(instance):
    assert isinstance(instance, jPQL_AvgAggregate)

@given(instance=SelectExpression_strategy)
@settings(max_examples=50)
def test_selectexpression_instantiation(instance):
    assert isinstance(instance, SelectExpression)

@given(instance=jPQL_SelectConstructorExpression_strategy)
@settings(max_examples=50)
def test_jpql_selectconstructorexpression_instantiation(instance):
    assert isinstance(instance, jPQL_SelectConstructorExpression)



@given(instance=jPQL_SelectConstructorExpression_strategy)
def test_jpql_selectconstructorexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jPQL_SelectAggregateExpression_strategy)
@settings(max_examples=50)
def test_jpql_selectaggregateexpression_instantiation(instance):
    assert isinstance(instance, jPQL_SelectAggregateExpression)



@given(instance=jPQL_SelectAggregateExpression_strategy)
def test_jpql_selectaggregateexpression_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=jPQL_SelectExpression_strategy)
@settings(max_examples=50)
def test_jpql_selectexpression_instantiation(instance):
    assert isinstance(instance, jPQL_SelectExpression)

@given(instance=jPQL_DeleteClause_strategy)
@settings(max_examples=50)
def test_jpql_deleteclause_instantiation(instance):
    assert isinstance(instance, jPQL_DeleteClause)

@given(instance=jPQL_Literal_strategy)
@settings(max_examples=50)
def test_jpql_literal_instantiation(instance):
    assert isinstance(instance, jPQL_Literal)

@given(instance=FromEntry_strategy)
@settings(max_examples=50)
def test_fromentry_instantiation(instance):
    assert isinstance(instance, FromEntry)

@given(instance=jPQL_FromCollection_strategy)
@settings(max_examples=50)
def test_jpql_fromcollection_instantiation(instance):
    assert isinstance(instance, jPQL_FromCollection)

@given(instance=jPQL_FromClass_strategy)
@settings(max_examples=50)
def test_jpql_fromclass_instantiation(instance):
    assert isinstance(instance, jPQL_FromClass)



@given(instance=jPQL_FromClass_strategy)
def test_jpql_fromclass_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jPQL_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_jpql_variabledeclaration_instantiation(instance):
    assert isinstance(instance, jPQL_VariableDeclaration)



@given(instance=jPQL_VariableDeclaration_strategy)
def test_jpql_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jPQL_UpdateClause_strategy)
@settings(max_examples=50)
def test_jpql_updateclause_instantiation(instance):
    assert isinstance(instance, jPQL_UpdateClause)

@given(instance=jPQL_OrderBySpec_strategy)
@settings(max_examples=50)
def test_jpql_orderbyspec_instantiation(instance):
    assert isinstance(instance, jPQL_OrderBySpec)

@given(instance=jPQL_Expression_strategy)
@settings(max_examples=50)
def test_jpql_expression_instantiation(instance):
    assert isinstance(instance, jPQL_Expression)



@given(instance=jPQL_Expression_strategy)
def test_jpql_expression_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original



@given(instance=jPQL_Expression_strategy)
def test_jpql_expression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=jPQL_HavingClause_strategy)
@settings(max_examples=50)
def test_jpql_havingclause_instantiation(instance):
    assert isinstance(instance, jPQL_HavingClause)

@given(instance=jPQL_AliasAttributeExpression_strategy)
@settings(max_examples=50)
def test_jpql_aliasattributeexpression_instantiation(instance):
    assert isinstance(instance, jPQL_AliasAttributeExpression)



@given(instance=jPQL_AliasAttributeExpression_strategy)
def test_jpql_aliasattributeexpression_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=jPQL_AliasAttributeExpression_strategy)
def test_jpql_aliasattributeexpression_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=jPQL_OrderByClause_strategy)
@settings(max_examples=50)
def test_jpql_orderbyclause_instantiation(instance):
    assert isinstance(instance, jPQL_OrderByClause)

@given(instance=jPQL_GroupByClause_strategy)
@settings(max_examples=50)
def test_jpql_groupbyclause_instantiation(instance):
    assert isinstance(instance, jPQL_GroupByClause)

@given(instance=jPQL_FromClause_strategy)
@settings(max_examples=50)
def test_jpql_fromclause_instantiation(instance):
    assert isinstance(instance, jPQL_FromClause)

@given(instance=jPQL_SelectClause_strategy)
@settings(max_examples=50)
def test_jpql_selectclause_instantiation(instance):
    assert isinstance(instance, jPQL_SelectClause)



@given(instance=jPQL_SelectClause_strategy)
def test_jpql_selectclause_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=ExpressionTerm_strategy)
@settings(max_examples=50)
def test_expressionterm_instantiation(instance):
    assert isinstance(instance, ExpressionTerm)

@given(instance=jPQL_Variable_strategy)
@settings(max_examples=50)
def test_jpql_variable_instantiation(instance):
    assert isinstance(instance, jPQL_Variable)

@given(instance=JPQLQuery_strategy)
@settings(max_examples=50)
def test_jpqlquery_instantiation(instance):
    assert isinstance(instance, JPQLQuery)

@given(instance=jPQL_UpdateStatement_strategy)
@settings(max_examples=50)
def test_jpql_updatestatement_instantiation(instance):
    assert isinstance(instance, jPQL_UpdateStatement)

@given(instance=jPQL_DeleteStatement_strategy)
@settings(max_examples=50)
def test_jpql_deletestatement_instantiation(instance):
    assert isinstance(instance, jPQL_DeleteStatement)

@given(instance=jPQL_SelectStatement_strategy)
@settings(max_examples=50)
def test_jpql_selectstatement_instantiation(instance):
    assert isinstance(instance, jPQL_SelectStatement)

@given(instance=jPQL_WhereClause_strategy)
@settings(max_examples=50)
def test_jpql_whereclause_instantiation(instance):
    assert isinstance(instance, jPQL_WhereClause)

@given(instance=jPQL_UpdateItem_strategy)
@settings(max_examples=50)
def test_jpql_updateitem_instantiation(instance):
    assert isinstance(instance, jPQL_UpdateItem)

@given(instance=jPQL_FromEntry_strategy)
@settings(max_examples=50)
def test_jpql_fromentry_instantiation(instance):
    assert isinstance(instance, jPQL_FromEntry)

@given(instance=jPQL_SetClause_strategy)
@settings(max_examples=50)
def test_jpql_setclause_instantiation(instance):
    assert isinstance(instance, jPQL_SetClause)

@given(instance=jPQL_JPQLQuery_strategy)
@settings(max_examples=50)
def test_jpql_jpqlquery_instantiation(instance):
    assert isinstance(instance, jPQL_JPQLQuery)
