import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Value,
    jpql_NullExpression,
    jpql_StringExpression,
    jpql_BooleanExpression,
    jpql_IntegerExpression,
    jpql_Function,
    jpql_DateTimeExpression,
    Variable,
    jpql_ParameterExpression,
    InExpression,
    jpql_InQueryExpression,
    jpql_InSeqExpression,
    Expression,
    jpql_BetweenExpression,
    jpql_EmptyComparisonExpression,
    jpql_ExpressionTerm,
    jpql_InExpression,
    jpql_AndExpression,
    jpql_LikeExpression,
    jpql_OrExpression,
    jpql_OperatorExpression,
    FromJoin,
    jpql_LeftJoin,
    jpql_InnerJoin,
    jpql_Join,
    jpql_NullComparisonExpression,
    jpql_CollectionExpression,
    jpql_SomeExpression,
    jpql_AnyExpression,
    jpql_AllExpression,
    jpql_ExistsExpression,
    SelectAggregateExpression,
    jpql_MinAggregate,
    jpql_MaxAggregate,
    jpql_CountAggregate,
    jpql_SumAggregate,
    jpql_AvgAggregate,
    SelectExpression,
    jpql_SelectConstructorExpression,
    jpql_SelectAggregateExpression,
    jpql_SelectExpression,
    jpql_FromJoin,
    FromEntry,
    jpql_FromCollection,
    jpql_FromClass,
    jpql_VariableDeclaration,
    jpql_SetClause,
    jpql_UpdateClause,
    jpql_FromEntry,
    jpql_OrderItem,
    jpql_Expression,
    jpql_SelectClause,
    jpql_FromClause,
    jpql_DeleteClause,
    jpql_Value,
    jpql_AliasAttributeExpression,
    jpql_UpdateItem,
    jpql_Import,
    jpql_QueryModule,
    jpql_OrderClause,
    jpql_HavingClause,
    jpql_SelectFromClause,
    ExpressionTerm,
    jpql_Variable,
    JPQLQuery,
    jpql_UpdateStatement,
    jpql_DeleteStatement,
    jpql_SelectStatement,
    jpql_WhereClause,
    jpql_NamedQuery,
    jpql_JPQLQuery,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_jpql_nullexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_NullExpression)


def test_jpql_nullexpression_constructor_exists():
    assert callable(jpql_NullExpression.__init__)


def test_jpql_nullexpression_constructor_args():
    sig = inspect.signature(jpql_NullExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_nullexpression_has_value():
    assert hasattr(jpql_NullExpression, "value")
    descriptor = None
    for klass in jpql_NullExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jpql_stringexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_StringExpression)


def test_jpql_stringexpression_constructor_exists():
    assert callable(jpql_StringExpression.__init__)


def test_jpql_stringexpression_constructor_args():
    sig = inspect.signature(jpql_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_stringexpression_has_value():
    assert hasattr(jpql_StringExpression, "value")
    descriptor = None
    for klass in jpql_StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jpql_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_BooleanExpression)


def test_jpql_booleanexpression_constructor_exists():
    assert callable(jpql_BooleanExpression.__init__)


def test_jpql_booleanexpression_constructor_args():
    sig = inspect.signature(jpql_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_booleanexpression_has_value():
    assert hasattr(jpql_BooleanExpression, "value")
    descriptor = None
    for klass in jpql_BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jpql_integerexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_IntegerExpression)


def test_jpql_integerexpression_constructor_exists():
    assert callable(jpql_IntegerExpression.__init__)


def test_jpql_integerexpression_constructor_args():
    sig = inspect.signature(jpql_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_integerexpression_has_value():
    assert hasattr(jpql_IntegerExpression, "value")
    descriptor = None
    for klass in jpql_IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_jpql_function_is_not_abstract():
    assert not inspect.isabstract(jpql_Function)


def test_jpql_function_constructor_exists():
    assert callable(jpql_Function.__init__)


def test_jpql_function_constructor_args():
    sig = inspect.signature(jpql_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpql_function_has_name():
    assert hasattr(jpql_Function, "name")
    descriptor = None
    for klass in jpql_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpql_datetimeexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_DateTimeExpression)


def test_jpql_datetimeexpression_constructor_exists():
    assert callable(jpql_DateTimeExpression.__init__)


def test_jpql_datetimeexpression_constructor_args():
    sig = inspect.signature(jpql_DateTimeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_jpql_datetimeexpression_has_value():
    assert hasattr(jpql_DateTimeExpression, "value")
    descriptor = None
    for klass in jpql_DateTimeExpression.__mro__:
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
    assert not inspect.isabstract(jpql_ParameterExpression)


def test_jpql_parameterexpression_constructor_exists():
    assert callable(jpql_ParameterExpression.__init__)


def test_jpql_parameterexpression_constructor_args():
    sig = inspect.signature(jpql_ParameterExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpql_parameterexpression_has_name():
    assert hasattr(jpql_ParameterExpression, "name")
    descriptor = None
    for klass in jpql_ParameterExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_inexpression_is_not_abstract():
    assert not inspect.isabstract(InExpression)


def test_inexpression_constructor_exists():
    assert callable(InExpression.__init__)


def test_inexpression_constructor_args():
    sig = inspect.signature(InExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_inqueryexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_InQueryExpression)


def test_jpql_inqueryexpression_constructor_exists():
    assert callable(jpql_InQueryExpression.__init__)


def test_jpql_inqueryexpression_constructor_args():
    sig = inspect.signature(jpql_InQueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_inseqexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_InSeqExpression)


def test_jpql_inseqexpression_constructor_exists():
    assert callable(jpql_InSeqExpression.__init__)


def test_jpql_inseqexpression_constructor_args():
    sig = inspect.signature(jpql_InSeqExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_betweenexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_BetweenExpression)


def test_jpql_betweenexpression_constructor_exists():
    assert callable(jpql_BetweenExpression.__init__)


def test_jpql_betweenexpression_constructor_args():
    sig = inspect.signature(jpql_BetweenExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_jpql_betweenexpression_has_isNot():
    assert hasattr(jpql_BetweenExpression, "isNot")
    descriptor = None
    for klass in jpql_BetweenExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_jpql_emptycomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_EmptyComparisonExpression)


def test_jpql_emptycomparisonexpression_constructor_exists():
    assert callable(jpql_EmptyComparisonExpression.__init__)


def test_jpql_emptycomparisonexpression_constructor_args():
    sig = inspect.signature(jpql_EmptyComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_jpql_emptycomparisonexpression_has_isNot():
    assert hasattr(jpql_EmptyComparisonExpression, "isNot")
    descriptor = None
    for klass in jpql_EmptyComparisonExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_jpql_expressionterm_is_not_abstract():
    assert not inspect.isabstract(jpql_ExpressionTerm)


def test_jpql_expressionterm_constructor_exists():
    assert callable(jpql_ExpressionTerm.__init__)


def test_jpql_expressionterm_constructor_args():
    sig = inspect.signature(jpql_ExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_jpql_inexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_InExpression)


def test_jpql_inexpression_constructor_exists():
    assert callable(jpql_InExpression.__init__)


def test_jpql_inexpression_constructor_args():
    sig = inspect.signature(jpql_InExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_jpql_inexpression_has_isNot():
    assert hasattr(jpql_InExpression, "isNot")
    descriptor = None
    for klass in jpql_InExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_jpql_andexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_AndExpression)


def test_jpql_andexpression_constructor_exists():
    assert callable(jpql_AndExpression.__init__)


def test_jpql_andexpression_constructor_args():
    sig = inspect.signature(jpql_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_likeexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_LikeExpression)


def test_jpql_likeexpression_constructor_exists():
    assert callable(jpql_LikeExpression.__init__)


def test_jpql_likeexpression_constructor_args():
    sig = inspect.signature(jpql_LikeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_jpql_likeexpression_has_pattern():
    assert hasattr(jpql_LikeExpression, "pattern")
    descriptor = None
    for klass in jpql_LikeExpression.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_jpql_likeexpression_has_isNot():
    assert hasattr(jpql_LikeExpression, "isNot")
    descriptor = None
    for klass in jpql_LikeExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_jpql_orexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_OrExpression)


def test_jpql_orexpression_constructor_exists():
    assert callable(jpql_OrExpression.__init__)


def test_jpql_orexpression_constructor_args():
    sig = inspect.signature(jpql_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_OperatorExpression)


def test_jpql_operatorexpression_constructor_exists():
    assert callable(jpql_OperatorExpression.__init__)


def test_jpql_operatorexpression_constructor_args():
    sig = inspect.signature(jpql_OperatorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_jpql_operatorexpression_has_operator():
    assert hasattr(jpql_OperatorExpression, "operator")
    descriptor = None
    for klass in jpql_OperatorExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
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
    assert not inspect.isabstract(jpql_LeftJoin)


def test_jpql_leftjoin_constructor_exists():
    assert callable(jpql_LeftJoin.__init__)


def test_jpql_leftjoin_constructor_args():
    sig = inspect.signature(jpql_LeftJoin.__init__)
    params = list(sig.parameters.keys())
    assert "isOuter" in params, "Missing parameter 'isOuter'"

def test_jpql_leftjoin_has_isOuter():
    assert hasattr(jpql_LeftJoin, "isOuter")
    descriptor = None
    for klass in jpql_LeftJoin.__mro__:
        if "isOuter" in klass.__dict__:
            descriptor = klass.__dict__["isOuter"]
            break
    assert isinstance(descriptor, property)



def test_jpql_innerjoin_is_not_abstract():
    assert not inspect.isabstract(jpql_InnerJoin)


def test_jpql_innerjoin_constructor_exists():
    assert callable(jpql_InnerJoin.__init__)


def test_jpql_innerjoin_constructor_args():
    sig = inspect.signature(jpql_InnerJoin.__init__)
    params = list(sig.parameters.keys())



def test_jpql_join_is_not_abstract():
    assert not inspect.isabstract(jpql_Join)


def test_jpql_join_constructor_exists():
    assert callable(jpql_Join.__init__)


def test_jpql_join_constructor_args():
    sig = inspect.signature(jpql_Join.__init__)
    params = list(sig.parameters.keys())



def test_jpql_nullcomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_NullComparisonExpression)


def test_jpql_nullcomparisonexpression_constructor_exists():
    assert callable(jpql_NullComparisonExpression.__init__)


def test_jpql_nullcomparisonexpression_constructor_args():
    sig = inspect.signature(jpql_NullComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_jpql_nullcomparisonexpression_has_isNot():
    assert hasattr(jpql_NullComparisonExpression, "isNot")
    descriptor = None
    for klass in jpql_NullComparisonExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_jpql_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_CollectionExpression)


def test_jpql_collectionexpression_constructor_exists():
    assert callable(jpql_CollectionExpression.__init__)


def test_jpql_collectionexpression_constructor_args():
    sig = inspect.signature(jpql_CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_jpql_collectionexpression_has_isNot():
    assert hasattr(jpql_CollectionExpression, "isNot")
    descriptor = None
    for klass in jpql_CollectionExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_jpql_someexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_SomeExpression)


def test_jpql_someexpression_constructor_exists():
    assert callable(jpql_SomeExpression.__init__)


def test_jpql_someexpression_constructor_args():
    sig = inspect.signature(jpql_SomeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_anyexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_AnyExpression)


def test_jpql_anyexpression_constructor_exists():
    assert callable(jpql_AnyExpression.__init__)


def test_jpql_anyexpression_constructor_args():
    sig = inspect.signature(jpql_AnyExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_allexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_AllExpression)


def test_jpql_allexpression_constructor_exists():
    assert callable(jpql_AllExpression.__init__)


def test_jpql_allexpression_constructor_args():
    sig = inspect.signature(jpql_AllExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_existsexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_ExistsExpression)


def test_jpql_existsexpression_constructor_exists():
    assert callable(jpql_ExistsExpression.__init__)


def test_jpql_existsexpression_constructor_args():
    sig = inspect.signature(jpql_ExistsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_jpql_existsexpression_has_isNot():
    assert hasattr(jpql_ExistsExpression, "isNot")
    descriptor = None
    for klass in jpql_ExistsExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_selectaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(SelectAggregateExpression)


def test_selectaggregateexpression_constructor_exists():
    assert callable(SelectAggregateExpression.__init__)


def test_selectaggregateexpression_constructor_args():
    sig = inspect.signature(SelectAggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_minaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_MinAggregate)


def test_jpql_minaggregate_constructor_exists():
    assert callable(jpql_MinAggregate.__init__)


def test_jpql_minaggregate_constructor_args():
    sig = inspect.signature(jpql_MinAggregate.__init__)
    params = list(sig.parameters.keys())



def test_jpql_maxaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_MaxAggregate)


def test_jpql_maxaggregate_constructor_exists():
    assert callable(jpql_MaxAggregate.__init__)


def test_jpql_maxaggregate_constructor_args():
    sig = inspect.signature(jpql_MaxAggregate.__init__)
    params = list(sig.parameters.keys())



def test_jpql_countaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_CountAggregate)


def test_jpql_countaggregate_constructor_exists():
    assert callable(jpql_CountAggregate.__init__)


def test_jpql_countaggregate_constructor_args():
    sig = inspect.signature(jpql_CountAggregate.__init__)
    params = list(sig.parameters.keys())



def test_jpql_sumaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_SumAggregate)


def test_jpql_sumaggregate_constructor_exists():
    assert callable(jpql_SumAggregate.__init__)


def test_jpql_sumaggregate_constructor_args():
    sig = inspect.signature(jpql_SumAggregate.__init__)
    params = list(sig.parameters.keys())



def test_jpql_avgaggregate_is_not_abstract():
    assert not inspect.isabstract(jpql_AvgAggregate)


def test_jpql_avgaggregate_constructor_exists():
    assert callable(jpql_AvgAggregate.__init__)


def test_jpql_avgaggregate_constructor_args():
    sig = inspect.signature(jpql_AvgAggregate.__init__)
    params = list(sig.parameters.keys())



def test_selectexpression_is_not_abstract():
    assert not inspect.isabstract(SelectExpression)


def test_selectexpression_constructor_exists():
    assert callable(SelectExpression.__init__)


def test_selectexpression_constructor_args():
    sig = inspect.signature(SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_selectconstructorexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectConstructorExpression)


def test_jpql_selectconstructorexpression_constructor_exists():
    assert callable(jpql_SelectConstructorExpression.__init__)


def test_jpql_selectconstructorexpression_constructor_args():
    sig = inspect.signature(jpql_SelectConstructorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpql_selectconstructorexpression_has_name():
    assert hasattr(jpql_SelectConstructorExpression, "name")
    descriptor = None
    for klass in jpql_SelectConstructorExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpql_selectaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectAggregateExpression)


def test_jpql_selectaggregateexpression_constructor_exists():
    assert callable(jpql_SelectAggregateExpression.__init__)


def test_jpql_selectaggregateexpression_constructor_args():
    sig = inspect.signature(jpql_SelectAggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_jpql_selectaggregateexpression_has_isDistinct():
    assert hasattr(jpql_SelectAggregateExpression, "isDistinct")
    descriptor = None
    for klass in jpql_SelectAggregateExpression.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_jpql_selectexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectExpression)


def test_jpql_selectexpression_constructor_exists():
    assert callable(jpql_SelectExpression.__init__)


def test_jpql_selectexpression_constructor_args():
    sig = inspect.signature(jpql_SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromjoin_is_not_abstract():
    assert not inspect.isabstract(jpql_FromJoin)


def test_jpql_fromjoin_constructor_exists():
    assert callable(jpql_FromJoin.__init__)


def test_jpql_fromjoin_constructor_args():
    sig = inspect.signature(jpql_FromJoin.__init__)
    params = list(sig.parameters.keys())
    assert "isFetch" in params, "Missing parameter 'isFetch'"

def test_jpql_fromjoin_has_isFetch():
    assert hasattr(jpql_FromJoin, "isFetch")
    descriptor = None
    for klass in jpql_FromJoin.__mro__:
        if "isFetch" in klass.__dict__:
            descriptor = klass.__dict__["isFetch"]
            break
    assert isinstance(descriptor, property)



def test_fromentry_is_not_abstract():
    assert not inspect.isabstract(FromEntry)


def test_fromentry_constructor_exists():
    assert callable(FromEntry.__init__)


def test_fromentry_constructor_args():
    sig = inspect.signature(FromEntry.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromcollection_is_not_abstract():
    assert not inspect.isabstract(jpql_FromCollection)


def test_jpql_fromcollection_constructor_exists():
    assert callable(jpql_FromCollection.__init__)


def test_jpql_fromcollection_constructor_args():
    sig = inspect.signature(jpql_FromCollection.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromclass_is_not_abstract():
    assert not inspect.isabstract(jpql_FromClass)


def test_jpql_fromclass_constructor_exists():
    assert callable(jpql_FromClass.__init__)


def test_jpql_fromclass_constructor_args():
    sig = inspect.signature(jpql_FromClass.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jpql_fromclass_has_type():
    assert hasattr(jpql_FromClass, "type")
    descriptor = None
    for klass in jpql_FromClass.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jpql_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(jpql_VariableDeclaration)


def test_jpql_variabledeclaration_constructor_exists():
    assert callable(jpql_VariableDeclaration.__init__)


def test_jpql_variabledeclaration_constructor_args():
    sig = inspect.signature(jpql_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpql_variabledeclaration_has_name():
    assert hasattr(jpql_VariableDeclaration, "name")
    descriptor = None
    for klass in jpql_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpql_setclause_is_not_abstract():
    assert not inspect.isabstract(jpql_SetClause)


def test_jpql_setclause_constructor_exists():
    assert callable(jpql_SetClause.__init__)


def test_jpql_setclause_constructor_args():
    sig = inspect.signature(jpql_SetClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_updateclause_is_not_abstract():
    assert not inspect.isabstract(jpql_UpdateClause)


def test_jpql_updateclause_constructor_exists():
    assert callable(jpql_UpdateClause.__init__)


def test_jpql_updateclause_constructor_args():
    sig = inspect.signature(jpql_UpdateClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_fromentry_is_not_abstract():
    assert not inspect.isabstract(jpql_FromEntry)


def test_jpql_fromentry_constructor_exists():
    assert callable(jpql_FromEntry.__init__)


def test_jpql_fromentry_constructor_args():
    sig = inspect.signature(jpql_FromEntry.__init__)
    params = list(sig.parameters.keys())



def test_jpql_orderitem_is_not_abstract():
    assert not inspect.isabstract(jpql_OrderItem)


def test_jpql_orderitem_constructor_exists():
    assert callable(jpql_OrderItem.__init__)


def test_jpql_orderitem_constructor_args():
    sig = inspect.signature(jpql_OrderItem.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_jpql_orderitem_has_feature():
    assert hasattr(jpql_OrderItem, "feature")
    descriptor = None
    for klass in jpql_OrderItem.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_jpql_expression_is_not_abstract():
    assert not inspect.isabstract(jpql_Expression)


def test_jpql_expression_constructor_exists():
    assert callable(jpql_Expression.__init__)


def test_jpql_expression_constructor_args():
    sig = inspect.signature(jpql_Expression.__init__)
    params = list(sig.parameters.keys())



def test_jpql_selectclause_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectClause)


def test_jpql_selectclause_constructor_exists():
    assert callable(jpql_SelectClause.__init__)


def test_jpql_selectclause_constructor_args():
    sig = inspect.signature(jpql_SelectClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_jpql_selectclause_has_isDistinct():
    assert hasattr(jpql_SelectClause, "isDistinct")
    descriptor = None
    for klass in jpql_SelectClause.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_jpql_fromclause_is_not_abstract():
    assert not inspect.isabstract(jpql_FromClause)


def test_jpql_fromclause_constructor_exists():
    assert callable(jpql_FromClause.__init__)


def test_jpql_fromclause_constructor_args():
    sig = inspect.signature(jpql_FromClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_deleteclause_is_not_abstract():
    assert not inspect.isabstract(jpql_DeleteClause)


def test_jpql_deleteclause_constructor_exists():
    assert callable(jpql_DeleteClause.__init__)


def test_jpql_deleteclause_constructor_args():
    sig = inspect.signature(jpql_DeleteClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_value_is_not_abstract():
    assert not inspect.isabstract(jpql_Value)


def test_jpql_value_constructor_exists():
    assert callable(jpql_Value.__init__)


def test_jpql_value_constructor_args():
    sig = inspect.signature(jpql_Value.__init__)
    params = list(sig.parameters.keys())



def test_jpql_aliasattributeexpression_is_not_abstract():
    assert not inspect.isabstract(jpql_AliasAttributeExpression)


def test_jpql_aliasattributeexpression_constructor_exists():
    assert callable(jpql_AliasAttributeExpression.__init__)


def test_jpql_aliasattributeexpression_constructor_args():
    sig = inspect.signature(jpql_AliasAttributeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "attributes" in params, "Missing parameter 'attributes'"

def test_jpql_aliasattributeexpression_has_attributes():
    assert hasattr(jpql_AliasAttributeExpression, "attributes")
    descriptor = None
    for klass in jpql_AliasAttributeExpression.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)



def test_jpql_updateitem_is_not_abstract():
    assert not inspect.isabstract(jpql_UpdateItem)


def test_jpql_updateitem_constructor_exists():
    assert callable(jpql_UpdateItem.__init__)


def test_jpql_updateitem_constructor_args():
    sig = inspect.signature(jpql_UpdateItem.__init__)
    params = list(sig.parameters.keys())



def test_jpql_import_is_not_abstract():
    assert not inspect.isabstract(jpql_Import)


def test_jpql_import_constructor_exists():
    assert callable(jpql_Import.__init__)


def test_jpql_import_constructor_args():
    sig = inspect.signature(jpql_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_jpql_import_has_importURI():
    assert hasattr(jpql_Import, "importURI")
    descriptor = None
    for klass in jpql_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_jpql_querymodule_is_not_abstract():
    assert not inspect.isabstract(jpql_QueryModule)


def test_jpql_querymodule_constructor_exists():
    assert callable(jpql_QueryModule.__init__)


def test_jpql_querymodule_constructor_args():
    sig = inspect.signature(jpql_QueryModule.__init__)
    params = list(sig.parameters.keys())



def test_jpql_orderclause_is_not_abstract():
    assert not inspect.isabstract(jpql_OrderClause)


def test_jpql_orderclause_constructor_exists():
    assert callable(jpql_OrderClause.__init__)


def test_jpql_orderclause_constructor_args():
    sig = inspect.signature(jpql_OrderClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDesc" in params, "Missing parameter 'isDesc'"
    assert "isAsc" in params, "Missing parameter 'isAsc'"

def test_jpql_orderclause_has_isDesc():
    assert hasattr(jpql_OrderClause, "isDesc")
    descriptor = None
    for klass in jpql_OrderClause.__mro__:
        if "isDesc" in klass.__dict__:
            descriptor = klass.__dict__["isDesc"]
            break
    assert isinstance(descriptor, property)

def test_jpql_orderclause_has_isAsc():
    assert hasattr(jpql_OrderClause, "isAsc")
    descriptor = None
    for klass in jpql_OrderClause.__mro__:
        if "isAsc" in klass.__dict__:
            descriptor = klass.__dict__["isAsc"]
            break
    assert isinstance(descriptor, property)



def test_jpql_havingclause_is_not_abstract():
    assert not inspect.isabstract(jpql_HavingClause)


def test_jpql_havingclause_constructor_exists():
    assert callable(jpql_HavingClause.__init__)


def test_jpql_havingclause_constructor_args():
    sig = inspect.signature(jpql_HavingClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_selectfromclause_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectFromClause)


def test_jpql_selectfromclause_constructor_exists():
    assert callable(jpql_SelectFromClause.__init__)


def test_jpql_selectfromclause_constructor_args():
    sig = inspect.signature(jpql_SelectFromClause.__init__)
    params = list(sig.parameters.keys())



def test_expressionterm_is_not_abstract():
    assert not inspect.isabstract(ExpressionTerm)


def test_expressionterm_constructor_exists():
    assert callable(ExpressionTerm.__init__)


def test_expressionterm_constructor_args():
    sig = inspect.signature(ExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_jpql_variable_is_not_abstract():
    assert not inspect.isabstract(jpql_Variable)


def test_jpql_variable_constructor_exists():
    assert callable(jpql_Variable.__init__)


def test_jpql_variable_constructor_args():
    sig = inspect.signature(jpql_Variable.__init__)
    params = list(sig.parameters.keys())



def test_jpqlquery_is_not_abstract():
    assert not inspect.isabstract(JPQLQuery)


def test_jpqlquery_constructor_exists():
    assert callable(JPQLQuery.__init__)


def test_jpqlquery_constructor_args():
    sig = inspect.signature(JPQLQuery.__init__)
    params = list(sig.parameters.keys())



def test_jpql_updatestatement_is_not_abstract():
    assert not inspect.isabstract(jpql_UpdateStatement)


def test_jpql_updatestatement_constructor_exists():
    assert callable(jpql_UpdateStatement.__init__)


def test_jpql_updatestatement_constructor_args():
    sig = inspect.signature(jpql_UpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_jpql_deletestatement_is_not_abstract():
    assert not inspect.isabstract(jpql_DeleteStatement)


def test_jpql_deletestatement_constructor_exists():
    assert callable(jpql_DeleteStatement.__init__)


def test_jpql_deletestatement_constructor_args():
    sig = inspect.signature(jpql_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_jpql_selectstatement_is_not_abstract():
    assert not inspect.isabstract(jpql_SelectStatement)


def test_jpql_selectstatement_constructor_exists():
    assert callable(jpql_SelectStatement.__init__)


def test_jpql_selectstatement_constructor_args():
    sig = inspect.signature(jpql_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_jpql_whereclause_is_not_abstract():
    assert not inspect.isabstract(jpql_WhereClause)


def test_jpql_whereclause_constructor_exists():
    assert callable(jpql_WhereClause.__init__)


def test_jpql_whereclause_constructor_args():
    sig = inspect.signature(jpql_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_jpql_namedquery_is_not_abstract():
    assert not inspect.isabstract(jpql_NamedQuery)


def test_jpql_namedquery_constructor_exists():
    assert callable(jpql_NamedQuery.__init__)


def test_jpql_namedquery_constructor_args():
    sig = inspect.signature(jpql_NamedQuery.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jpql_namedquery_has_name():
    assert hasattr(jpql_NamedQuery, "name")
    descriptor = None
    for klass in jpql_NamedQuery.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jpql_jpqlquery_is_not_abstract():
    assert not inspect.isabstract(jpql_JPQLQuery)


def test_jpql_jpqlquery_constructor_exists():
    assert callable(jpql_JPQLQuery.__init__)


def test_jpql_jpqlquery_constructor_args():
    sig = inspect.signature(jpql_JPQLQuery.__init__)
    params = list(sig.parameters.keys())

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "notEqual",
        "equal",
        "lessEqual",
        "greaterEqual",
        "lessThen",
        "greaterThen",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
Value_strategy = st.builds(
    Value,
)
jpql_NullExpression_strategy = st.builds(
    jpql_NullExpression,
    value=
        safe_text
)
jpql_StringExpression_strategy = st.builds(
    jpql_StringExpression,
    value=
        safe_text
)
jpql_BooleanExpression_strategy = st.builds(
    jpql_BooleanExpression,
    value=
        st.booleans()
)
jpql_IntegerExpression_strategy = st.builds(
    jpql_IntegerExpression,
    value=
        st.integers()
)
jpql_Function_strategy = st.builds(
    jpql_Function,
    name=
        safe_text
)
jpql_DateTimeExpression_strategy = st.builds(
    jpql_DateTimeExpression,
    value=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
jpql_ParameterExpression_strategy = st.builds(
    jpql_ParameterExpression,
    name=
        safe_text
)
InExpression_strategy = st.builds(
    InExpression,
)
jpql_InQueryExpression_strategy = st.builds(
    jpql_InQueryExpression,
)
jpql_InSeqExpression_strategy = st.builds(
    jpql_InSeqExpression,
)
Expression_strategy = st.builds(
    Expression,
)
jpql_BetweenExpression_strategy = st.builds(
    jpql_BetweenExpression,
    isNot=
        st.booleans()
)
jpql_EmptyComparisonExpression_strategy = st.builds(
    jpql_EmptyComparisonExpression,
    isNot=
        st.booleans()
)
jpql_ExpressionTerm_strategy = st.builds(
    jpql_ExpressionTerm,
)
jpql_InExpression_strategy = st.builds(
    jpql_InExpression,
    isNot=
        st.booleans()
)
jpql_AndExpression_strategy = st.builds(
    jpql_AndExpression,
)
jpql_LikeExpression_strategy = st.builds(
    jpql_LikeExpression,
    pattern=
        safe_text,
    isNot=
        st.booleans()
)
jpql_OrExpression_strategy = st.builds(
    jpql_OrExpression,
)
jpql_OperatorExpression_strategy = st.builds(
    jpql_OperatorExpression,
    operator=
        safe_text
)
FromJoin_strategy = st.builds(
    FromJoin,
)
jpql_LeftJoin_strategy = st.builds(
    jpql_LeftJoin,
    isOuter=
        st.booleans()
)
jpql_InnerJoin_strategy = st.builds(
    jpql_InnerJoin,
)
jpql_Join_strategy = st.builds(
    jpql_Join,
)
jpql_NullComparisonExpression_strategy = st.builds(
    jpql_NullComparisonExpression,
    isNot=
        st.booleans()
)
jpql_CollectionExpression_strategy = st.builds(
    jpql_CollectionExpression,
    isNot=
        st.booleans()
)
jpql_SomeExpression_strategy = st.builds(
    jpql_SomeExpression,
)
jpql_AnyExpression_strategy = st.builds(
    jpql_AnyExpression,
)
jpql_AllExpression_strategy = st.builds(
    jpql_AllExpression,
)
jpql_ExistsExpression_strategy = st.builds(
    jpql_ExistsExpression,
    isNot=
        st.booleans()
)
SelectAggregateExpression_strategy = st.builds(
    SelectAggregateExpression,
)
jpql_MinAggregate_strategy = st.builds(
    jpql_MinAggregate,
)
jpql_MaxAggregate_strategy = st.builds(
    jpql_MaxAggregate,
)
jpql_CountAggregate_strategy = st.builds(
    jpql_CountAggregate,
)
jpql_SumAggregate_strategy = st.builds(
    jpql_SumAggregate,
)
jpql_AvgAggregate_strategy = st.builds(
    jpql_AvgAggregate,
)
SelectExpression_strategy = st.builds(
    SelectExpression,
)
jpql_SelectConstructorExpression_strategy = st.builds(
    jpql_SelectConstructorExpression,
    name=
        safe_text
)
jpql_SelectAggregateExpression_strategy = st.builds(
    jpql_SelectAggregateExpression,
    isDistinct=
        st.booleans()
)
jpql_SelectExpression_strategy = st.builds(
    jpql_SelectExpression,
)
jpql_FromJoin_strategy = st.builds(
    jpql_FromJoin,
    isFetch=
        st.booleans()
)
FromEntry_strategy = st.builds(
    FromEntry,
)
jpql_FromCollection_strategy = st.builds(
    jpql_FromCollection,
)
jpql_FromClass_strategy = st.builds(
    jpql_FromClass,
    type=
        safe_text
)
jpql_VariableDeclaration_strategy = st.builds(
    jpql_VariableDeclaration,
    name=
        safe_text
)
jpql_SetClause_strategy = st.builds(
    jpql_SetClause,
)
jpql_UpdateClause_strategy = st.builds(
    jpql_UpdateClause,
)
jpql_FromEntry_strategy = st.builds(
    jpql_FromEntry,
)
jpql_OrderItem_strategy = st.builds(
    jpql_OrderItem,
    feature=
        safe_text
)
jpql_Expression_strategy = st.builds(
    jpql_Expression,
)
jpql_SelectClause_strategy = st.builds(
    jpql_SelectClause,
    isDistinct=
        st.booleans()
)
jpql_FromClause_strategy = st.builds(
    jpql_FromClause,
)
jpql_DeleteClause_strategy = st.builds(
    jpql_DeleteClause,
)
jpql_Value_strategy = st.builds(
    jpql_Value,
)
jpql_AliasAttributeExpression_strategy = st.builds(
    jpql_AliasAttributeExpression,
    attributes=
        safe_text
)
jpql_UpdateItem_strategy = st.builds(
    jpql_UpdateItem,
)
jpql_Import_strategy = st.builds(
    jpql_Import,
    importURI=
        safe_text
)
jpql_QueryModule_strategy = st.builds(
    jpql_QueryModule,
)
jpql_OrderClause_strategy = st.builds(
    jpql_OrderClause,
    isDesc=
        st.booleans(),
    isAsc=
        st.booleans()
)
jpql_HavingClause_strategy = st.builds(
    jpql_HavingClause,
)
jpql_SelectFromClause_strategy = st.builds(
    jpql_SelectFromClause,
)
ExpressionTerm_strategy = st.builds(
    ExpressionTerm,
)
jpql_Variable_strategy = st.builds(
    jpql_Variable,
)
JPQLQuery_strategy = st.builds(
    JPQLQuery,
)
jpql_UpdateStatement_strategy = st.builds(
    jpql_UpdateStatement,
)
jpql_DeleteStatement_strategy = st.builds(
    jpql_DeleteStatement,
)
jpql_SelectStatement_strategy = st.builds(
    jpql_SelectStatement,
)
jpql_WhereClause_strategy = st.builds(
    jpql_WhereClause,
)
jpql_NamedQuery_strategy = st.builds(
    jpql_NamedQuery,
    name=
        safe_text
)
jpql_JPQLQuery_strategy = st.builds(
    jpql_JPQLQuery,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=jpql_NullExpression_strategy)
@settings(max_examples=50)
def test_jpql_nullexpression_instantiation(instance):
    assert isinstance(instance, jpql_NullExpression)



@given(instance=jpql_NullExpression_strategy)
def test_jpql_nullexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jpql_StringExpression_strategy)
@settings(max_examples=50)
def test_jpql_stringexpression_instantiation(instance):
    assert isinstance(instance, jpql_StringExpression)



@given(instance=jpql_StringExpression_strategy)
def test_jpql_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jpql_BooleanExpression_strategy)
@settings(max_examples=50)
def test_jpql_booleanexpression_instantiation(instance):
    assert isinstance(instance, jpql_BooleanExpression)



@given(instance=jpql_BooleanExpression_strategy)
def test_jpql_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jpql_IntegerExpression_strategy)
@settings(max_examples=50)
def test_jpql_integerexpression_instantiation(instance):
    assert isinstance(instance, jpql_IntegerExpression)



@given(instance=jpql_IntegerExpression_strategy)
def test_jpql_integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=jpql_Function_strategy)
@settings(max_examples=50)
def test_jpql_function_instantiation(instance):
    assert isinstance(instance, jpql_Function)



@given(instance=jpql_Function_strategy)
def test_jpql_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpql_DateTimeExpression_strategy)
@settings(max_examples=50)
def test_jpql_datetimeexpression_instantiation(instance):
    assert isinstance(instance, jpql_DateTimeExpression)



@given(instance=jpql_DateTimeExpression_strategy)
def test_jpql_datetimeexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=jpql_ParameterExpression_strategy)
@settings(max_examples=50)
def test_jpql_parameterexpression_instantiation(instance):
    assert isinstance(instance, jpql_ParameterExpression)



@given(instance=jpql_ParameterExpression_strategy)
def test_jpql_parameterexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InExpression_strategy)
@settings(max_examples=50)
def test_inexpression_instantiation(instance):
    assert isinstance(instance, InExpression)

@given(instance=jpql_InQueryExpression_strategy)
@settings(max_examples=50)
def test_jpql_inqueryexpression_instantiation(instance):
    assert isinstance(instance, jpql_InQueryExpression)

@given(instance=jpql_InSeqExpression_strategy)
@settings(max_examples=50)
def test_jpql_inseqexpression_instantiation(instance):
    assert isinstance(instance, jpql_InSeqExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=jpql_BetweenExpression_strategy)
@settings(max_examples=50)
def test_jpql_betweenexpression_instantiation(instance):
    assert isinstance(instance, jpql_BetweenExpression)



@given(instance=jpql_BetweenExpression_strategy)
def test_jpql_betweenexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=jpql_EmptyComparisonExpression_strategy)
@settings(max_examples=50)
def test_jpql_emptycomparisonexpression_instantiation(instance):
    assert isinstance(instance, jpql_EmptyComparisonExpression)



@given(instance=jpql_EmptyComparisonExpression_strategy)
def test_jpql_emptycomparisonexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=jpql_ExpressionTerm_strategy)
@settings(max_examples=50)
def test_jpql_expressionterm_instantiation(instance):
    assert isinstance(instance, jpql_ExpressionTerm)

@given(instance=jpql_InExpression_strategy)
@settings(max_examples=50)
def test_jpql_inexpression_instantiation(instance):
    assert isinstance(instance, jpql_InExpression)



@given(instance=jpql_InExpression_strategy)
def test_jpql_inexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=jpql_AndExpression_strategy)
@settings(max_examples=50)
def test_jpql_andexpression_instantiation(instance):
    assert isinstance(instance, jpql_AndExpression)

@given(instance=jpql_LikeExpression_strategy)
@settings(max_examples=50)
def test_jpql_likeexpression_instantiation(instance):
    assert isinstance(instance, jpql_LikeExpression)



@given(instance=jpql_LikeExpression_strategy)
def test_jpql_likeexpression_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=jpql_LikeExpression_strategy)
def test_jpql_likeexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=jpql_OrExpression_strategy)
@settings(max_examples=50)
def test_jpql_orexpression_instantiation(instance):
    assert isinstance(instance, jpql_OrExpression)

@given(instance=jpql_OperatorExpression_strategy)
@settings(max_examples=50)
def test_jpql_operatorexpression_instantiation(instance):
    assert isinstance(instance, jpql_OperatorExpression)



@given(instance=jpql_OperatorExpression_strategy)
def test_jpql_operatorexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=FromJoin_strategy)
@settings(max_examples=50)
def test_fromjoin_instantiation(instance):
    assert isinstance(instance, FromJoin)

@given(instance=jpql_LeftJoin_strategy)
@settings(max_examples=50)
def test_jpql_leftjoin_instantiation(instance):
    assert isinstance(instance, jpql_LeftJoin)



@given(instance=jpql_LeftJoin_strategy)
def test_jpql_leftjoin_isOuter_setter(instance):
    original = instance.isOuter
    instance.isOuter = original
    assert instance.isOuter == original

@given(instance=jpql_InnerJoin_strategy)
@settings(max_examples=50)
def test_jpql_innerjoin_instantiation(instance):
    assert isinstance(instance, jpql_InnerJoin)

@given(instance=jpql_Join_strategy)
@settings(max_examples=50)
def test_jpql_join_instantiation(instance):
    assert isinstance(instance, jpql_Join)

@given(instance=jpql_NullComparisonExpression_strategy)
@settings(max_examples=50)
def test_jpql_nullcomparisonexpression_instantiation(instance):
    assert isinstance(instance, jpql_NullComparisonExpression)



@given(instance=jpql_NullComparisonExpression_strategy)
def test_jpql_nullcomparisonexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=jpql_CollectionExpression_strategy)
@settings(max_examples=50)
def test_jpql_collectionexpression_instantiation(instance):
    assert isinstance(instance, jpql_CollectionExpression)



@given(instance=jpql_CollectionExpression_strategy)
def test_jpql_collectionexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=jpql_SomeExpression_strategy)
@settings(max_examples=50)
def test_jpql_someexpression_instantiation(instance):
    assert isinstance(instance, jpql_SomeExpression)

@given(instance=jpql_AnyExpression_strategy)
@settings(max_examples=50)
def test_jpql_anyexpression_instantiation(instance):
    assert isinstance(instance, jpql_AnyExpression)

@given(instance=jpql_AllExpression_strategy)
@settings(max_examples=50)
def test_jpql_allexpression_instantiation(instance):
    assert isinstance(instance, jpql_AllExpression)

@given(instance=jpql_ExistsExpression_strategy)
@settings(max_examples=50)
def test_jpql_existsexpression_instantiation(instance):
    assert isinstance(instance, jpql_ExistsExpression)



@given(instance=jpql_ExistsExpression_strategy)
def test_jpql_existsexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=SelectAggregateExpression_strategy)
@settings(max_examples=50)
def test_selectaggregateexpression_instantiation(instance):
    assert isinstance(instance, SelectAggregateExpression)

@given(instance=jpql_MinAggregate_strategy)
@settings(max_examples=50)
def test_jpql_minaggregate_instantiation(instance):
    assert isinstance(instance, jpql_MinAggregate)

@given(instance=jpql_MaxAggregate_strategy)
@settings(max_examples=50)
def test_jpql_maxaggregate_instantiation(instance):
    assert isinstance(instance, jpql_MaxAggregate)

@given(instance=jpql_CountAggregate_strategy)
@settings(max_examples=50)
def test_jpql_countaggregate_instantiation(instance):
    assert isinstance(instance, jpql_CountAggregate)

@given(instance=jpql_SumAggregate_strategy)
@settings(max_examples=50)
def test_jpql_sumaggregate_instantiation(instance):
    assert isinstance(instance, jpql_SumAggregate)

@given(instance=jpql_AvgAggregate_strategy)
@settings(max_examples=50)
def test_jpql_avgaggregate_instantiation(instance):
    assert isinstance(instance, jpql_AvgAggregate)

@given(instance=SelectExpression_strategy)
@settings(max_examples=50)
def test_selectexpression_instantiation(instance):
    assert isinstance(instance, SelectExpression)

@given(instance=jpql_SelectConstructorExpression_strategy)
@settings(max_examples=50)
def test_jpql_selectconstructorexpression_instantiation(instance):
    assert isinstance(instance, jpql_SelectConstructorExpression)



@given(instance=jpql_SelectConstructorExpression_strategy)
def test_jpql_selectconstructorexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpql_SelectAggregateExpression_strategy)
@settings(max_examples=50)
def test_jpql_selectaggregateexpression_instantiation(instance):
    assert isinstance(instance, jpql_SelectAggregateExpression)



@given(instance=jpql_SelectAggregateExpression_strategy)
def test_jpql_selectaggregateexpression_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=jpql_SelectExpression_strategy)
@settings(max_examples=50)
def test_jpql_selectexpression_instantiation(instance):
    assert isinstance(instance, jpql_SelectExpression)

@given(instance=jpql_FromJoin_strategy)
@settings(max_examples=50)
def test_jpql_fromjoin_instantiation(instance):
    assert isinstance(instance, jpql_FromJoin)



@given(instance=jpql_FromJoin_strategy)
def test_jpql_fromjoin_isFetch_setter(instance):
    original = instance.isFetch
    instance.isFetch = original
    assert instance.isFetch == original

@given(instance=FromEntry_strategy)
@settings(max_examples=50)
def test_fromentry_instantiation(instance):
    assert isinstance(instance, FromEntry)

@given(instance=jpql_FromCollection_strategy)
@settings(max_examples=50)
def test_jpql_fromcollection_instantiation(instance):
    assert isinstance(instance, jpql_FromCollection)

@given(instance=jpql_FromClass_strategy)
@settings(max_examples=50)
def test_jpql_fromclass_instantiation(instance):
    assert isinstance(instance, jpql_FromClass)



@given(instance=jpql_FromClass_strategy)
def test_jpql_fromclass_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=jpql_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_jpql_variabledeclaration_instantiation(instance):
    assert isinstance(instance, jpql_VariableDeclaration)



@given(instance=jpql_VariableDeclaration_strategy)
def test_jpql_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpql_SetClause_strategy)
@settings(max_examples=50)
def test_jpql_setclause_instantiation(instance):
    assert isinstance(instance, jpql_SetClause)

@given(instance=jpql_UpdateClause_strategy)
@settings(max_examples=50)
def test_jpql_updateclause_instantiation(instance):
    assert isinstance(instance, jpql_UpdateClause)

@given(instance=jpql_FromEntry_strategy)
@settings(max_examples=50)
def test_jpql_fromentry_instantiation(instance):
    assert isinstance(instance, jpql_FromEntry)

@given(instance=jpql_OrderItem_strategy)
@settings(max_examples=50)
def test_jpql_orderitem_instantiation(instance):
    assert isinstance(instance, jpql_OrderItem)



@given(instance=jpql_OrderItem_strategy)
def test_jpql_orderitem_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=jpql_Expression_strategy)
@settings(max_examples=50)
def test_jpql_expression_instantiation(instance):
    assert isinstance(instance, jpql_Expression)

@given(instance=jpql_SelectClause_strategy)
@settings(max_examples=50)
def test_jpql_selectclause_instantiation(instance):
    assert isinstance(instance, jpql_SelectClause)



@given(instance=jpql_SelectClause_strategy)
def test_jpql_selectclause_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=jpql_FromClause_strategy)
@settings(max_examples=50)
def test_jpql_fromclause_instantiation(instance):
    assert isinstance(instance, jpql_FromClause)

@given(instance=jpql_DeleteClause_strategy)
@settings(max_examples=50)
def test_jpql_deleteclause_instantiation(instance):
    assert isinstance(instance, jpql_DeleteClause)

@given(instance=jpql_Value_strategy)
@settings(max_examples=50)
def test_jpql_value_instantiation(instance):
    assert isinstance(instance, jpql_Value)

@given(instance=jpql_AliasAttributeExpression_strategy)
@settings(max_examples=50)
def test_jpql_aliasattributeexpression_instantiation(instance):
    assert isinstance(instance, jpql_AliasAttributeExpression)



@given(instance=jpql_AliasAttributeExpression_strategy)
def test_jpql_aliasattributeexpression_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=jpql_UpdateItem_strategy)
@settings(max_examples=50)
def test_jpql_updateitem_instantiation(instance):
    assert isinstance(instance, jpql_UpdateItem)

@given(instance=jpql_Import_strategy)
@settings(max_examples=50)
def test_jpql_import_instantiation(instance):
    assert isinstance(instance, jpql_Import)



@given(instance=jpql_Import_strategy)
def test_jpql_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=jpql_QueryModule_strategy)
@settings(max_examples=50)
def test_jpql_querymodule_instantiation(instance):
    assert isinstance(instance, jpql_QueryModule)

@given(instance=jpql_OrderClause_strategy)
@settings(max_examples=50)
def test_jpql_orderclause_instantiation(instance):
    assert isinstance(instance, jpql_OrderClause)



@given(instance=jpql_OrderClause_strategy)
def test_jpql_orderclause_isDesc_setter(instance):
    original = instance.isDesc
    instance.isDesc = original
    assert instance.isDesc == original



@given(instance=jpql_OrderClause_strategy)
def test_jpql_orderclause_isAsc_setter(instance):
    original = instance.isAsc
    instance.isAsc = original
    assert instance.isAsc == original

@given(instance=jpql_HavingClause_strategy)
@settings(max_examples=50)
def test_jpql_havingclause_instantiation(instance):
    assert isinstance(instance, jpql_HavingClause)

@given(instance=jpql_SelectFromClause_strategy)
@settings(max_examples=50)
def test_jpql_selectfromclause_instantiation(instance):
    assert isinstance(instance, jpql_SelectFromClause)

@given(instance=ExpressionTerm_strategy)
@settings(max_examples=50)
def test_expressionterm_instantiation(instance):
    assert isinstance(instance, ExpressionTerm)

@given(instance=jpql_Variable_strategy)
@settings(max_examples=50)
def test_jpql_variable_instantiation(instance):
    assert isinstance(instance, jpql_Variable)

@given(instance=JPQLQuery_strategy)
@settings(max_examples=50)
def test_jpqlquery_instantiation(instance):
    assert isinstance(instance, JPQLQuery)

@given(instance=jpql_UpdateStatement_strategy)
@settings(max_examples=50)
def test_jpql_updatestatement_instantiation(instance):
    assert isinstance(instance, jpql_UpdateStatement)

@given(instance=jpql_DeleteStatement_strategy)
@settings(max_examples=50)
def test_jpql_deletestatement_instantiation(instance):
    assert isinstance(instance, jpql_DeleteStatement)

@given(instance=jpql_SelectStatement_strategy)
@settings(max_examples=50)
def test_jpql_selectstatement_instantiation(instance):
    assert isinstance(instance, jpql_SelectStatement)

@given(instance=jpql_WhereClause_strategy)
@settings(max_examples=50)
def test_jpql_whereclause_instantiation(instance):
    assert isinstance(instance, jpql_WhereClause)

@given(instance=jpql_NamedQuery_strategy)
@settings(max_examples=50)
def test_jpql_namedquery_instantiation(instance):
    assert isinstance(instance, jpql_NamedQuery)



@given(instance=jpql_NamedQuery_strategy)
def test_jpql_namedquery_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=jpql_JPQLQuery_strategy)
@settings(max_examples=50)
def test_jpql_jpqlquery_instantiation(instance):
    assert isinstance(instance, jpql_JPQLQuery)
