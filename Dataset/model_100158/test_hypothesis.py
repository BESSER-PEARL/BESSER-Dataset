import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Value,
    mql_NullExpression,
    mql_BooleanExpression,
    mql_DateTimeExpression,
    mql_StringExpression,
    mql_IntegerExpression,
    mql_Function,
    Variable,
    mql_ParameterExpression,
    InExpression,
    mql_InQueryExpression,
    mql_InSeqExpression,
    Expression,
    mql_NullComparisonExpression,
    mql_AllExpression,
    mql_AnyExpression,
    mql_ExpressionTerm,
    mql_OrExpression,
    mql_EmptyComparisonExpression,
    mql_BetweenExpression,
    mql_ExistsExpression,
    mql_AndExpression,
    mql_SomeExpression,
    mql_InExpression,
    mql_CollectionExpression,
    mql_LikeExpression,
    mql_OperatorExpression,
    FromJoin,
    mql_LeftJoin,
    mql_InnerJoin,
    mql_Join,
    mql_SelectClause,
    mql_FromJoin,
    FromEntry,
    mql_FromCollection,
    mql_FromClass,
    mql_VariableDeclaration,
    SelectAggregateExpression,
    mql_MinAggregate,
    mql_SumAggregate,
    mql_MaxAggregate,
    mql_CountAggregate,
    mql_AvgAggregate,
    SelectExpression,
    mql_SelectConstructorExpression,
    mql_SelectAggregateExpression,
    mql_SelectExpression,
    mql_Expression,
    mql_OrderClause,
    mql_HavingClause,
    mql_FromClause,
    mql_DeleteClause,
    mql_Value,
    mql_AliasAttributeExpression,
    mql_UpdateItem,
    mql_SetClause,
    mql_UpdateClause,
    mql_FromEntry,
    mql_OrderItem,
    mql_SelectFromClause,
    ExpressionTerm,
    mql_Variable,
    MQuery,
    mql_DeleteStatement,
    mql_UpdateStatement,
    mql_SelectStatement,
    mql_WhereClause,
    mql_NamedQuery,
    mql_MQuery,
    mql_Import,
    mql_QueryModule,
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



def test_mql_nullexpression_is_not_abstract():
    assert not inspect.isabstract(mql_NullExpression)


def test_mql_nullexpression_constructor_exists():
    assert callable(mql_NullExpression.__init__)


def test_mql_nullexpression_constructor_args():
    sig = inspect.signature(mql_NullExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mql_nullexpression_has_value():
    assert hasattr(mql_NullExpression, "value")
    descriptor = None
    for klass in mql_NullExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mql_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(mql_BooleanExpression)


def test_mql_booleanexpression_constructor_exists():
    assert callable(mql_BooleanExpression.__init__)


def test_mql_booleanexpression_constructor_args():
    sig = inspect.signature(mql_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mql_booleanexpression_has_value():
    assert hasattr(mql_BooleanExpression, "value")
    descriptor = None
    for klass in mql_BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mql_datetimeexpression_is_not_abstract():
    assert not inspect.isabstract(mql_DateTimeExpression)


def test_mql_datetimeexpression_constructor_exists():
    assert callable(mql_DateTimeExpression.__init__)


def test_mql_datetimeexpression_constructor_args():
    sig = inspect.signature(mql_DateTimeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mql_datetimeexpression_has_value():
    assert hasattr(mql_DateTimeExpression, "value")
    descriptor = None
    for klass in mql_DateTimeExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mql_stringexpression_is_not_abstract():
    assert not inspect.isabstract(mql_StringExpression)


def test_mql_stringexpression_constructor_exists():
    assert callable(mql_StringExpression.__init__)


def test_mql_stringexpression_constructor_args():
    sig = inspect.signature(mql_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mql_stringexpression_has_value():
    assert hasattr(mql_StringExpression, "value")
    descriptor = None
    for klass in mql_StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mql_integerexpression_is_not_abstract():
    assert not inspect.isabstract(mql_IntegerExpression)


def test_mql_integerexpression_constructor_exists():
    assert callable(mql_IntegerExpression.__init__)


def test_mql_integerexpression_constructor_args():
    sig = inspect.signature(mql_IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mql_integerexpression_has_value():
    assert hasattr(mql_IntegerExpression, "value")
    descriptor = None
    for klass in mql_IntegerExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mql_function_is_not_abstract():
    assert not inspect.isabstract(mql_Function)


def test_mql_function_constructor_exists():
    assert callable(mql_Function.__init__)


def test_mql_function_constructor_args():
    sig = inspect.signature(mql_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mql_function_has_name():
    assert hasattr(mql_Function, "name")
    descriptor = None
    for klass in mql_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_mql_parameterexpression_is_not_abstract():
    assert not inspect.isabstract(mql_ParameterExpression)


def test_mql_parameterexpression_constructor_exists():
    assert callable(mql_ParameterExpression.__init__)


def test_mql_parameterexpression_constructor_args():
    sig = inspect.signature(mql_ParameterExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mql_parameterexpression_has_name():
    assert hasattr(mql_ParameterExpression, "name")
    descriptor = None
    for klass in mql_ParameterExpression.__mro__:
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



def test_mql_inqueryexpression_is_not_abstract():
    assert not inspect.isabstract(mql_InQueryExpression)


def test_mql_inqueryexpression_constructor_exists():
    assert callable(mql_InQueryExpression.__init__)


def test_mql_inqueryexpression_constructor_args():
    sig = inspect.signature(mql_InQueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_inseqexpression_is_not_abstract():
    assert not inspect.isabstract(mql_InSeqExpression)


def test_mql_inseqexpression_constructor_exists():
    assert callable(mql_InSeqExpression.__init__)


def test_mql_inseqexpression_constructor_args():
    sig = inspect.signature(mql_InSeqExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mql_nullcomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(mql_NullComparisonExpression)


def test_mql_nullcomparisonexpression_constructor_exists():
    assert callable(mql_NullComparisonExpression.__init__)


def test_mql_nullcomparisonexpression_constructor_args():
    sig = inspect.signature(mql_NullComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_mql_nullcomparisonexpression_has_isNot():
    assert hasattr(mql_NullComparisonExpression, "isNot")
    descriptor = None
    for klass in mql_NullComparisonExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_mql_allexpression_is_not_abstract():
    assert not inspect.isabstract(mql_AllExpression)


def test_mql_allexpression_constructor_exists():
    assert callable(mql_AllExpression.__init__)


def test_mql_allexpression_constructor_args():
    sig = inspect.signature(mql_AllExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_anyexpression_is_not_abstract():
    assert not inspect.isabstract(mql_AnyExpression)


def test_mql_anyexpression_constructor_exists():
    assert callable(mql_AnyExpression.__init__)


def test_mql_anyexpression_constructor_args():
    sig = inspect.signature(mql_AnyExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_expressionterm_is_not_abstract():
    assert not inspect.isabstract(mql_ExpressionTerm)


def test_mql_expressionterm_constructor_exists():
    assert callable(mql_ExpressionTerm.__init__)


def test_mql_expressionterm_constructor_args():
    sig = inspect.signature(mql_ExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_mql_orexpression_is_not_abstract():
    assert not inspect.isabstract(mql_OrExpression)


def test_mql_orexpression_constructor_exists():
    assert callable(mql_OrExpression.__init__)


def test_mql_orexpression_constructor_args():
    sig = inspect.signature(mql_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_emptycomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(mql_EmptyComparisonExpression)


def test_mql_emptycomparisonexpression_constructor_exists():
    assert callable(mql_EmptyComparisonExpression.__init__)


def test_mql_emptycomparisonexpression_constructor_args():
    sig = inspect.signature(mql_EmptyComparisonExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_mql_emptycomparisonexpression_has_isNot():
    assert hasattr(mql_EmptyComparisonExpression, "isNot")
    descriptor = None
    for klass in mql_EmptyComparisonExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_mql_betweenexpression_is_not_abstract():
    assert not inspect.isabstract(mql_BetweenExpression)


def test_mql_betweenexpression_constructor_exists():
    assert callable(mql_BetweenExpression.__init__)


def test_mql_betweenexpression_constructor_args():
    sig = inspect.signature(mql_BetweenExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_mql_betweenexpression_has_isNot():
    assert hasattr(mql_BetweenExpression, "isNot")
    descriptor = None
    for klass in mql_BetweenExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_mql_existsexpression_is_not_abstract():
    assert not inspect.isabstract(mql_ExistsExpression)


def test_mql_existsexpression_constructor_exists():
    assert callable(mql_ExistsExpression.__init__)


def test_mql_existsexpression_constructor_args():
    sig = inspect.signature(mql_ExistsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_mql_existsexpression_has_isNot():
    assert hasattr(mql_ExistsExpression, "isNot")
    descriptor = None
    for klass in mql_ExistsExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_mql_andexpression_is_not_abstract():
    assert not inspect.isabstract(mql_AndExpression)


def test_mql_andexpression_constructor_exists():
    assert callable(mql_AndExpression.__init__)


def test_mql_andexpression_constructor_args():
    sig = inspect.signature(mql_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_someexpression_is_not_abstract():
    assert not inspect.isabstract(mql_SomeExpression)


def test_mql_someexpression_constructor_exists():
    assert callable(mql_SomeExpression.__init__)


def test_mql_someexpression_constructor_args():
    sig = inspect.signature(mql_SomeExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_inexpression_is_not_abstract():
    assert not inspect.isabstract(mql_InExpression)


def test_mql_inexpression_constructor_exists():
    assert callable(mql_InExpression.__init__)


def test_mql_inexpression_constructor_args():
    sig = inspect.signature(mql_InExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_mql_inexpression_has_isNot():
    assert hasattr(mql_InExpression, "isNot")
    descriptor = None
    for klass in mql_InExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_mql_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(mql_CollectionExpression)


def test_mql_collectionexpression_constructor_exists():
    assert callable(mql_CollectionExpression.__init__)


def test_mql_collectionexpression_constructor_args():
    sig = inspect.signature(mql_CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_mql_collectionexpression_has_isNot():
    assert hasattr(mql_CollectionExpression, "isNot")
    descriptor = None
    for klass in mql_CollectionExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_mql_likeexpression_is_not_abstract():
    assert not inspect.isabstract(mql_LikeExpression)


def test_mql_likeexpression_constructor_exists():
    assert callable(mql_LikeExpression.__init__)


def test_mql_likeexpression_constructor_args():
    sig = inspect.signature(mql_LikeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "isNot" in params, "Missing parameter 'isNot'"

def test_mql_likeexpression_has_pattern():
    assert hasattr(mql_LikeExpression, "pattern")
    descriptor = None
    for klass in mql_LikeExpression.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_mql_likeexpression_has_isNot():
    assert hasattr(mql_LikeExpression, "isNot")
    descriptor = None
    for klass in mql_LikeExpression.__mro__:
        if "isNot" in klass.__dict__:
            descriptor = klass.__dict__["isNot"]
            break
    assert isinstance(descriptor, property)



def test_mql_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(mql_OperatorExpression)


def test_mql_operatorexpression_constructor_exists():
    assert callable(mql_OperatorExpression.__init__)


def test_mql_operatorexpression_constructor_args():
    sig = inspect.signature(mql_OperatorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mql_operatorexpression_has_operator():
    assert hasattr(mql_OperatorExpression, "operator")
    descriptor = None
    for klass in mql_OperatorExpression.__mro__:
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



def test_mql_leftjoin_is_not_abstract():
    assert not inspect.isabstract(mql_LeftJoin)


def test_mql_leftjoin_constructor_exists():
    assert callable(mql_LeftJoin.__init__)


def test_mql_leftjoin_constructor_args():
    sig = inspect.signature(mql_LeftJoin.__init__)
    params = list(sig.parameters.keys())
    assert "isOuter" in params, "Missing parameter 'isOuter'"

def test_mql_leftjoin_has_isOuter():
    assert hasattr(mql_LeftJoin, "isOuter")
    descriptor = None
    for klass in mql_LeftJoin.__mro__:
        if "isOuter" in klass.__dict__:
            descriptor = klass.__dict__["isOuter"]
            break
    assert isinstance(descriptor, property)



def test_mql_innerjoin_is_not_abstract():
    assert not inspect.isabstract(mql_InnerJoin)


def test_mql_innerjoin_constructor_exists():
    assert callable(mql_InnerJoin.__init__)


def test_mql_innerjoin_constructor_args():
    sig = inspect.signature(mql_InnerJoin.__init__)
    params = list(sig.parameters.keys())



def test_mql_join_is_not_abstract():
    assert not inspect.isabstract(mql_Join)


def test_mql_join_constructor_exists():
    assert callable(mql_Join.__init__)


def test_mql_join_constructor_args():
    sig = inspect.signature(mql_Join.__init__)
    params = list(sig.parameters.keys())



def test_mql_selectclause_is_not_abstract():
    assert not inspect.isabstract(mql_SelectClause)


def test_mql_selectclause_constructor_exists():
    assert callable(mql_SelectClause.__init__)


def test_mql_selectclause_constructor_args():
    sig = inspect.signature(mql_SelectClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_mql_selectclause_has_isDistinct():
    assert hasattr(mql_SelectClause, "isDistinct")
    descriptor = None
    for klass in mql_SelectClause.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_mql_fromjoin_is_not_abstract():
    assert not inspect.isabstract(mql_FromJoin)


def test_mql_fromjoin_constructor_exists():
    assert callable(mql_FromJoin.__init__)


def test_mql_fromjoin_constructor_args():
    sig = inspect.signature(mql_FromJoin.__init__)
    params = list(sig.parameters.keys())
    assert "isFetch" in params, "Missing parameter 'isFetch'"

def test_mql_fromjoin_has_isFetch():
    assert hasattr(mql_FromJoin, "isFetch")
    descriptor = None
    for klass in mql_FromJoin.__mro__:
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



def test_mql_fromcollection_is_not_abstract():
    assert not inspect.isabstract(mql_FromCollection)


def test_mql_fromcollection_constructor_exists():
    assert callable(mql_FromCollection.__init__)


def test_mql_fromcollection_constructor_args():
    sig = inspect.signature(mql_FromCollection.__init__)
    params = list(sig.parameters.keys())



def test_mql_fromclass_is_not_abstract():
    assert not inspect.isabstract(mql_FromClass)


def test_mql_fromclass_constructor_exists():
    assert callable(mql_FromClass.__init__)


def test_mql_fromclass_constructor_args():
    sig = inspect.signature(mql_FromClass.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mql_fromclass_has_type():
    assert hasattr(mql_FromClass, "type")
    descriptor = None
    for klass in mql_FromClass.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_mql_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(mql_VariableDeclaration)


def test_mql_variabledeclaration_constructor_exists():
    assert callable(mql_VariableDeclaration.__init__)


def test_mql_variabledeclaration_constructor_args():
    sig = inspect.signature(mql_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mql_variabledeclaration_has_name():
    assert hasattr(mql_VariableDeclaration, "name")
    descriptor = None
    for klass in mql_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_selectaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(SelectAggregateExpression)


def test_selectaggregateexpression_constructor_exists():
    assert callable(SelectAggregateExpression.__init__)


def test_selectaggregateexpression_constructor_args():
    sig = inspect.signature(SelectAggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_minaggregate_is_not_abstract():
    assert not inspect.isabstract(mql_MinAggregate)


def test_mql_minaggregate_constructor_exists():
    assert callable(mql_MinAggregate.__init__)


def test_mql_minaggregate_constructor_args():
    sig = inspect.signature(mql_MinAggregate.__init__)
    params = list(sig.parameters.keys())



def test_mql_sumaggregate_is_not_abstract():
    assert not inspect.isabstract(mql_SumAggregate)


def test_mql_sumaggregate_constructor_exists():
    assert callable(mql_SumAggregate.__init__)


def test_mql_sumaggregate_constructor_args():
    sig = inspect.signature(mql_SumAggregate.__init__)
    params = list(sig.parameters.keys())



def test_mql_maxaggregate_is_not_abstract():
    assert not inspect.isabstract(mql_MaxAggregate)


def test_mql_maxaggregate_constructor_exists():
    assert callable(mql_MaxAggregate.__init__)


def test_mql_maxaggregate_constructor_args():
    sig = inspect.signature(mql_MaxAggregate.__init__)
    params = list(sig.parameters.keys())



def test_mql_countaggregate_is_not_abstract():
    assert not inspect.isabstract(mql_CountAggregate)


def test_mql_countaggregate_constructor_exists():
    assert callable(mql_CountAggregate.__init__)


def test_mql_countaggregate_constructor_args():
    sig = inspect.signature(mql_CountAggregate.__init__)
    params = list(sig.parameters.keys())



def test_mql_avgaggregate_is_not_abstract():
    assert not inspect.isabstract(mql_AvgAggregate)


def test_mql_avgaggregate_constructor_exists():
    assert callable(mql_AvgAggregate.__init__)


def test_mql_avgaggregate_constructor_args():
    sig = inspect.signature(mql_AvgAggregate.__init__)
    params = list(sig.parameters.keys())



def test_selectexpression_is_not_abstract():
    assert not inspect.isabstract(SelectExpression)


def test_selectexpression_constructor_exists():
    assert callable(SelectExpression.__init__)


def test_selectexpression_constructor_args():
    sig = inspect.signature(SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_selectconstructorexpression_is_not_abstract():
    assert not inspect.isabstract(mql_SelectConstructorExpression)


def test_mql_selectconstructorexpression_constructor_exists():
    assert callable(mql_SelectConstructorExpression.__init__)


def test_mql_selectconstructorexpression_constructor_args():
    sig = inspect.signature(mql_SelectConstructorExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mql_selectconstructorexpression_has_name():
    assert hasattr(mql_SelectConstructorExpression, "name")
    descriptor = None
    for klass in mql_SelectConstructorExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mql_selectaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(mql_SelectAggregateExpression)


def test_mql_selectaggregateexpression_constructor_exists():
    assert callable(mql_SelectAggregateExpression.__init__)


def test_mql_selectaggregateexpression_constructor_args():
    sig = inspect.signature(mql_SelectAggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isDistinct" in params, "Missing parameter 'isDistinct'"

def test_mql_selectaggregateexpression_has_isDistinct():
    assert hasattr(mql_SelectAggregateExpression, "isDistinct")
    descriptor = None
    for klass in mql_SelectAggregateExpression.__mro__:
        if "isDistinct" in klass.__dict__:
            descriptor = klass.__dict__["isDistinct"]
            break
    assert isinstance(descriptor, property)



def test_mql_selectexpression_is_not_abstract():
    assert not inspect.isabstract(mql_SelectExpression)


def test_mql_selectexpression_constructor_exists():
    assert callable(mql_SelectExpression.__init__)


def test_mql_selectexpression_constructor_args():
    sig = inspect.signature(mql_SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_mql_expression_is_not_abstract():
    assert not inspect.isabstract(mql_Expression)


def test_mql_expression_constructor_exists():
    assert callable(mql_Expression.__init__)


def test_mql_expression_constructor_args():
    sig = inspect.signature(mql_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mql_orderclause_is_not_abstract():
    assert not inspect.isabstract(mql_OrderClause)


def test_mql_orderclause_constructor_exists():
    assert callable(mql_OrderClause.__init__)


def test_mql_orderclause_constructor_args():
    sig = inspect.signature(mql_OrderClause.__init__)
    params = list(sig.parameters.keys())
    assert "isDesc" in params, "Missing parameter 'isDesc'"
    assert "isAsc" in params, "Missing parameter 'isAsc'"

def test_mql_orderclause_has_isDesc():
    assert hasattr(mql_OrderClause, "isDesc")
    descriptor = None
    for klass in mql_OrderClause.__mro__:
        if "isDesc" in klass.__dict__:
            descriptor = klass.__dict__["isDesc"]
            break
    assert isinstance(descriptor, property)

def test_mql_orderclause_has_isAsc():
    assert hasattr(mql_OrderClause, "isAsc")
    descriptor = None
    for klass in mql_OrderClause.__mro__:
        if "isAsc" in klass.__dict__:
            descriptor = klass.__dict__["isAsc"]
            break
    assert isinstance(descriptor, property)



def test_mql_havingclause_is_not_abstract():
    assert not inspect.isabstract(mql_HavingClause)


def test_mql_havingclause_constructor_exists():
    assert callable(mql_HavingClause.__init__)


def test_mql_havingclause_constructor_args():
    sig = inspect.signature(mql_HavingClause.__init__)
    params = list(sig.parameters.keys())



def test_mql_fromclause_is_not_abstract():
    assert not inspect.isabstract(mql_FromClause)


def test_mql_fromclause_constructor_exists():
    assert callable(mql_FromClause.__init__)


def test_mql_fromclause_constructor_args():
    sig = inspect.signature(mql_FromClause.__init__)
    params = list(sig.parameters.keys())



def test_mql_deleteclause_is_not_abstract():
    assert not inspect.isabstract(mql_DeleteClause)


def test_mql_deleteclause_constructor_exists():
    assert callable(mql_DeleteClause.__init__)


def test_mql_deleteclause_constructor_args():
    sig = inspect.signature(mql_DeleteClause.__init__)
    params = list(sig.parameters.keys())



def test_mql_value_is_not_abstract():
    assert not inspect.isabstract(mql_Value)


def test_mql_value_constructor_exists():
    assert callable(mql_Value.__init__)


def test_mql_value_constructor_args():
    sig = inspect.signature(mql_Value.__init__)
    params = list(sig.parameters.keys())



def test_mql_aliasattributeexpression_is_not_abstract():
    assert not inspect.isabstract(mql_AliasAttributeExpression)


def test_mql_aliasattributeexpression_constructor_exists():
    assert callable(mql_AliasAttributeExpression.__init__)


def test_mql_aliasattributeexpression_constructor_args():
    sig = inspect.signature(mql_AliasAttributeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "attributes" in params, "Missing parameter 'attributes'"

def test_mql_aliasattributeexpression_has_attributes():
    assert hasattr(mql_AliasAttributeExpression, "attributes")
    descriptor = None
    for klass in mql_AliasAttributeExpression.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)



def test_mql_updateitem_is_not_abstract():
    assert not inspect.isabstract(mql_UpdateItem)


def test_mql_updateitem_constructor_exists():
    assert callable(mql_UpdateItem.__init__)


def test_mql_updateitem_constructor_args():
    sig = inspect.signature(mql_UpdateItem.__init__)
    params = list(sig.parameters.keys())



def test_mql_setclause_is_not_abstract():
    assert not inspect.isabstract(mql_SetClause)


def test_mql_setclause_constructor_exists():
    assert callable(mql_SetClause.__init__)


def test_mql_setclause_constructor_args():
    sig = inspect.signature(mql_SetClause.__init__)
    params = list(sig.parameters.keys())



def test_mql_updateclause_is_not_abstract():
    assert not inspect.isabstract(mql_UpdateClause)


def test_mql_updateclause_constructor_exists():
    assert callable(mql_UpdateClause.__init__)


def test_mql_updateclause_constructor_args():
    sig = inspect.signature(mql_UpdateClause.__init__)
    params = list(sig.parameters.keys())



def test_mql_fromentry_is_not_abstract():
    assert not inspect.isabstract(mql_FromEntry)


def test_mql_fromentry_constructor_exists():
    assert callable(mql_FromEntry.__init__)


def test_mql_fromentry_constructor_args():
    sig = inspect.signature(mql_FromEntry.__init__)
    params = list(sig.parameters.keys())



def test_mql_orderitem_is_not_abstract():
    assert not inspect.isabstract(mql_OrderItem)


def test_mql_orderitem_constructor_exists():
    assert callable(mql_OrderItem.__init__)


def test_mql_orderitem_constructor_args():
    sig = inspect.signature(mql_OrderItem.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_mql_orderitem_has_feature():
    assert hasattr(mql_OrderItem, "feature")
    descriptor = None
    for klass in mql_OrderItem.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_mql_selectfromclause_is_not_abstract():
    assert not inspect.isabstract(mql_SelectFromClause)


def test_mql_selectfromclause_constructor_exists():
    assert callable(mql_SelectFromClause.__init__)


def test_mql_selectfromclause_constructor_args():
    sig = inspect.signature(mql_SelectFromClause.__init__)
    params = list(sig.parameters.keys())



def test_expressionterm_is_not_abstract():
    assert not inspect.isabstract(ExpressionTerm)


def test_expressionterm_constructor_exists():
    assert callable(ExpressionTerm.__init__)


def test_expressionterm_constructor_args():
    sig = inspect.signature(ExpressionTerm.__init__)
    params = list(sig.parameters.keys())



def test_mql_variable_is_not_abstract():
    assert not inspect.isabstract(mql_Variable)


def test_mql_variable_constructor_exists():
    assert callable(mql_Variable.__init__)


def test_mql_variable_constructor_args():
    sig = inspect.signature(mql_Variable.__init__)
    params = list(sig.parameters.keys())



def test_mquery_is_not_abstract():
    assert not inspect.isabstract(MQuery)


def test_mquery_constructor_exists():
    assert callable(MQuery.__init__)


def test_mquery_constructor_args():
    sig = inspect.signature(MQuery.__init__)
    params = list(sig.parameters.keys())



def test_mql_deletestatement_is_not_abstract():
    assert not inspect.isabstract(mql_DeleteStatement)


def test_mql_deletestatement_constructor_exists():
    assert callable(mql_DeleteStatement.__init__)


def test_mql_deletestatement_constructor_args():
    sig = inspect.signature(mql_DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_mql_updatestatement_is_not_abstract():
    assert not inspect.isabstract(mql_UpdateStatement)


def test_mql_updatestatement_constructor_exists():
    assert callable(mql_UpdateStatement.__init__)


def test_mql_updatestatement_constructor_args():
    sig = inspect.signature(mql_UpdateStatement.__init__)
    params = list(sig.parameters.keys())



def test_mql_selectstatement_is_not_abstract():
    assert not inspect.isabstract(mql_SelectStatement)


def test_mql_selectstatement_constructor_exists():
    assert callable(mql_SelectStatement.__init__)


def test_mql_selectstatement_constructor_args():
    sig = inspect.signature(mql_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_mql_whereclause_is_not_abstract():
    assert not inspect.isabstract(mql_WhereClause)


def test_mql_whereclause_constructor_exists():
    assert callable(mql_WhereClause.__init__)


def test_mql_whereclause_constructor_args():
    sig = inspect.signature(mql_WhereClause.__init__)
    params = list(sig.parameters.keys())



def test_mql_namedquery_is_not_abstract():
    assert not inspect.isabstract(mql_NamedQuery)


def test_mql_namedquery_constructor_exists():
    assert callable(mql_NamedQuery.__init__)


def test_mql_namedquery_constructor_args():
    sig = inspect.signature(mql_NamedQuery.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mql_namedquery_has_name():
    assert hasattr(mql_NamedQuery, "name")
    descriptor = None
    for klass in mql_NamedQuery.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mql_mquery_is_not_abstract():
    assert not inspect.isabstract(mql_MQuery)


def test_mql_mquery_constructor_exists():
    assert callable(mql_MQuery.__init__)


def test_mql_mquery_constructor_args():
    sig = inspect.signature(mql_MQuery.__init__)
    params = list(sig.parameters.keys())



def test_mql_import_is_not_abstract():
    assert not inspect.isabstract(mql_Import)


def test_mql_import_constructor_exists():
    assert callable(mql_Import.__init__)


def test_mql_import_constructor_args():
    sig = inspect.signature(mql_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_mql_import_has_importURI():
    assert hasattr(mql_Import, "importURI")
    descriptor = None
    for klass in mql_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_mql_querymodule_is_not_abstract():
    assert not inspect.isabstract(mql_QueryModule)


def test_mql_querymodule_constructor_exists():
    assert callable(mql_QueryModule.__init__)


def test_mql_querymodule_constructor_args():
    sig = inspect.signature(mql_QueryModule.__init__)
    params = list(sig.parameters.keys())

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "greaterThen",
        "lessThen",
        "greaterEqual",
        "notEqual",
        "equal",
        "lessEqual",
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
mql_NullExpression_strategy = st.builds(
    mql_NullExpression,
    value=
        safe_text
)
mql_BooleanExpression_strategy = st.builds(
    mql_BooleanExpression,
    value=
        st.booleans()
)
mql_DateTimeExpression_strategy = st.builds(
    mql_DateTimeExpression,
    value=
        safe_text
)
mql_StringExpression_strategy = st.builds(
    mql_StringExpression,
    value=
        safe_text
)
mql_IntegerExpression_strategy = st.builds(
    mql_IntegerExpression,
    value=
        st.integers()
)
mql_Function_strategy = st.builds(
    mql_Function,
    name=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
mql_ParameterExpression_strategy = st.builds(
    mql_ParameterExpression,
    name=
        safe_text
)
InExpression_strategy = st.builds(
    InExpression,
)
mql_InQueryExpression_strategy = st.builds(
    mql_InQueryExpression,
)
mql_InSeqExpression_strategy = st.builds(
    mql_InSeqExpression,
)
Expression_strategy = st.builds(
    Expression,
)
mql_NullComparisonExpression_strategy = st.builds(
    mql_NullComparisonExpression,
    isNot=
        st.booleans()
)
mql_AllExpression_strategy = st.builds(
    mql_AllExpression,
)
mql_AnyExpression_strategy = st.builds(
    mql_AnyExpression,
)
mql_ExpressionTerm_strategy = st.builds(
    mql_ExpressionTerm,
)
mql_OrExpression_strategy = st.builds(
    mql_OrExpression,
)
mql_EmptyComparisonExpression_strategy = st.builds(
    mql_EmptyComparisonExpression,
    isNot=
        st.booleans()
)
mql_BetweenExpression_strategy = st.builds(
    mql_BetweenExpression,
    isNot=
        st.booleans()
)
mql_ExistsExpression_strategy = st.builds(
    mql_ExistsExpression,
    isNot=
        st.booleans()
)
mql_AndExpression_strategy = st.builds(
    mql_AndExpression,
)
mql_SomeExpression_strategy = st.builds(
    mql_SomeExpression,
)
mql_InExpression_strategy = st.builds(
    mql_InExpression,
    isNot=
        st.booleans()
)
mql_CollectionExpression_strategy = st.builds(
    mql_CollectionExpression,
    isNot=
        st.booleans()
)
mql_LikeExpression_strategy = st.builds(
    mql_LikeExpression,
    pattern=
        safe_text,
    isNot=
        st.booleans()
)
mql_OperatorExpression_strategy = st.builds(
    mql_OperatorExpression,
    operator=
        safe_text
)
FromJoin_strategy = st.builds(
    FromJoin,
)
mql_LeftJoin_strategy = st.builds(
    mql_LeftJoin,
    isOuter=
        st.booleans()
)
mql_InnerJoin_strategy = st.builds(
    mql_InnerJoin,
)
mql_Join_strategy = st.builds(
    mql_Join,
)
mql_SelectClause_strategy = st.builds(
    mql_SelectClause,
    isDistinct=
        st.booleans()
)
mql_FromJoin_strategy = st.builds(
    mql_FromJoin,
    isFetch=
        st.booleans()
)
FromEntry_strategy = st.builds(
    FromEntry,
)
mql_FromCollection_strategy = st.builds(
    mql_FromCollection,
)
mql_FromClass_strategy = st.builds(
    mql_FromClass,
    type=
        safe_text
)
mql_VariableDeclaration_strategy = st.builds(
    mql_VariableDeclaration,
    name=
        safe_text
)
SelectAggregateExpression_strategy = st.builds(
    SelectAggregateExpression,
)
mql_MinAggregate_strategy = st.builds(
    mql_MinAggregate,
)
mql_SumAggregate_strategy = st.builds(
    mql_SumAggregate,
)
mql_MaxAggregate_strategy = st.builds(
    mql_MaxAggregate,
)
mql_CountAggregate_strategy = st.builds(
    mql_CountAggregate,
)
mql_AvgAggregate_strategy = st.builds(
    mql_AvgAggregate,
)
SelectExpression_strategy = st.builds(
    SelectExpression,
)
mql_SelectConstructorExpression_strategy = st.builds(
    mql_SelectConstructorExpression,
    name=
        safe_text
)
mql_SelectAggregateExpression_strategy = st.builds(
    mql_SelectAggregateExpression,
    isDistinct=
        st.booleans()
)
mql_SelectExpression_strategy = st.builds(
    mql_SelectExpression,
)
mql_Expression_strategy = st.builds(
    mql_Expression,
)
mql_OrderClause_strategy = st.builds(
    mql_OrderClause,
    isDesc=
        st.booleans(),
    isAsc=
        st.booleans()
)
mql_HavingClause_strategy = st.builds(
    mql_HavingClause,
)
mql_FromClause_strategy = st.builds(
    mql_FromClause,
)
mql_DeleteClause_strategy = st.builds(
    mql_DeleteClause,
)
mql_Value_strategy = st.builds(
    mql_Value,
)
mql_AliasAttributeExpression_strategy = st.builds(
    mql_AliasAttributeExpression,
    attributes=
        safe_text
)
mql_UpdateItem_strategy = st.builds(
    mql_UpdateItem,
)
mql_SetClause_strategy = st.builds(
    mql_SetClause,
)
mql_UpdateClause_strategy = st.builds(
    mql_UpdateClause,
)
mql_FromEntry_strategy = st.builds(
    mql_FromEntry,
)
mql_OrderItem_strategy = st.builds(
    mql_OrderItem,
    feature=
        safe_text
)
mql_SelectFromClause_strategy = st.builds(
    mql_SelectFromClause,
)
ExpressionTerm_strategy = st.builds(
    ExpressionTerm,
)
mql_Variable_strategy = st.builds(
    mql_Variable,
)
MQuery_strategy = st.builds(
    MQuery,
)
mql_DeleteStatement_strategy = st.builds(
    mql_DeleteStatement,
)
mql_UpdateStatement_strategy = st.builds(
    mql_UpdateStatement,
)
mql_SelectStatement_strategy = st.builds(
    mql_SelectStatement,
)
mql_WhereClause_strategy = st.builds(
    mql_WhereClause,
)
mql_NamedQuery_strategy = st.builds(
    mql_NamedQuery,
    name=
        safe_text
)
mql_MQuery_strategy = st.builds(
    mql_MQuery,
)
mql_Import_strategy = st.builds(
    mql_Import,
    importURI=
        safe_text
)
mql_QueryModule_strategy = st.builds(
    mql_QueryModule,
)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=mql_NullExpression_strategy)
@settings(max_examples=50)
def test_mql_nullexpression_instantiation(instance):
    assert isinstance(instance, mql_NullExpression)



@given(instance=mql_NullExpression_strategy)
def test_mql_nullexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mql_BooleanExpression_strategy)
@settings(max_examples=50)
def test_mql_booleanexpression_instantiation(instance):
    assert isinstance(instance, mql_BooleanExpression)



@given(instance=mql_BooleanExpression_strategy)
def test_mql_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mql_DateTimeExpression_strategy)
@settings(max_examples=50)
def test_mql_datetimeexpression_instantiation(instance):
    assert isinstance(instance, mql_DateTimeExpression)



@given(instance=mql_DateTimeExpression_strategy)
def test_mql_datetimeexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mql_StringExpression_strategy)
@settings(max_examples=50)
def test_mql_stringexpression_instantiation(instance):
    assert isinstance(instance, mql_StringExpression)



@given(instance=mql_StringExpression_strategy)
def test_mql_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mql_IntegerExpression_strategy)
@settings(max_examples=50)
def test_mql_integerexpression_instantiation(instance):
    assert isinstance(instance, mql_IntegerExpression)



@given(instance=mql_IntegerExpression_strategy)
def test_mql_integerexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mql_Function_strategy)
@settings(max_examples=50)
def test_mql_function_instantiation(instance):
    assert isinstance(instance, mql_Function)



@given(instance=mql_Function_strategy)
def test_mql_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=mql_ParameterExpression_strategy)
@settings(max_examples=50)
def test_mql_parameterexpression_instantiation(instance):
    assert isinstance(instance, mql_ParameterExpression)



@given(instance=mql_ParameterExpression_strategy)
def test_mql_parameterexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InExpression_strategy)
@settings(max_examples=50)
def test_inexpression_instantiation(instance):
    assert isinstance(instance, InExpression)

@given(instance=mql_InQueryExpression_strategy)
@settings(max_examples=50)
def test_mql_inqueryexpression_instantiation(instance):
    assert isinstance(instance, mql_InQueryExpression)

@given(instance=mql_InSeqExpression_strategy)
@settings(max_examples=50)
def test_mql_inseqexpression_instantiation(instance):
    assert isinstance(instance, mql_InSeqExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=mql_NullComparisonExpression_strategy)
@settings(max_examples=50)
def test_mql_nullcomparisonexpression_instantiation(instance):
    assert isinstance(instance, mql_NullComparisonExpression)



@given(instance=mql_NullComparisonExpression_strategy)
def test_mql_nullcomparisonexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=mql_AllExpression_strategy)
@settings(max_examples=50)
def test_mql_allexpression_instantiation(instance):
    assert isinstance(instance, mql_AllExpression)

@given(instance=mql_AnyExpression_strategy)
@settings(max_examples=50)
def test_mql_anyexpression_instantiation(instance):
    assert isinstance(instance, mql_AnyExpression)

@given(instance=mql_ExpressionTerm_strategy)
@settings(max_examples=50)
def test_mql_expressionterm_instantiation(instance):
    assert isinstance(instance, mql_ExpressionTerm)

@given(instance=mql_OrExpression_strategy)
@settings(max_examples=50)
def test_mql_orexpression_instantiation(instance):
    assert isinstance(instance, mql_OrExpression)

@given(instance=mql_EmptyComparisonExpression_strategy)
@settings(max_examples=50)
def test_mql_emptycomparisonexpression_instantiation(instance):
    assert isinstance(instance, mql_EmptyComparisonExpression)



@given(instance=mql_EmptyComparisonExpression_strategy)
def test_mql_emptycomparisonexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=mql_BetweenExpression_strategy)
@settings(max_examples=50)
def test_mql_betweenexpression_instantiation(instance):
    assert isinstance(instance, mql_BetweenExpression)



@given(instance=mql_BetweenExpression_strategy)
def test_mql_betweenexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=mql_ExistsExpression_strategy)
@settings(max_examples=50)
def test_mql_existsexpression_instantiation(instance):
    assert isinstance(instance, mql_ExistsExpression)



@given(instance=mql_ExistsExpression_strategy)
def test_mql_existsexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=mql_AndExpression_strategy)
@settings(max_examples=50)
def test_mql_andexpression_instantiation(instance):
    assert isinstance(instance, mql_AndExpression)

@given(instance=mql_SomeExpression_strategy)
@settings(max_examples=50)
def test_mql_someexpression_instantiation(instance):
    assert isinstance(instance, mql_SomeExpression)

@given(instance=mql_InExpression_strategy)
@settings(max_examples=50)
def test_mql_inexpression_instantiation(instance):
    assert isinstance(instance, mql_InExpression)



@given(instance=mql_InExpression_strategy)
def test_mql_inexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=mql_CollectionExpression_strategy)
@settings(max_examples=50)
def test_mql_collectionexpression_instantiation(instance):
    assert isinstance(instance, mql_CollectionExpression)



@given(instance=mql_CollectionExpression_strategy)
def test_mql_collectionexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=mql_LikeExpression_strategy)
@settings(max_examples=50)
def test_mql_likeexpression_instantiation(instance):
    assert isinstance(instance, mql_LikeExpression)



@given(instance=mql_LikeExpression_strategy)
def test_mql_likeexpression_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=mql_LikeExpression_strategy)
def test_mql_likeexpression_isNot_setter(instance):
    original = instance.isNot
    instance.isNot = original
    assert instance.isNot == original

@given(instance=mql_OperatorExpression_strategy)
@settings(max_examples=50)
def test_mql_operatorexpression_instantiation(instance):
    assert isinstance(instance, mql_OperatorExpression)



@given(instance=mql_OperatorExpression_strategy)
def test_mql_operatorexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=FromJoin_strategy)
@settings(max_examples=50)
def test_fromjoin_instantiation(instance):
    assert isinstance(instance, FromJoin)

@given(instance=mql_LeftJoin_strategy)
@settings(max_examples=50)
def test_mql_leftjoin_instantiation(instance):
    assert isinstance(instance, mql_LeftJoin)



@given(instance=mql_LeftJoin_strategy)
def test_mql_leftjoin_isOuter_setter(instance):
    original = instance.isOuter
    instance.isOuter = original
    assert instance.isOuter == original

@given(instance=mql_InnerJoin_strategy)
@settings(max_examples=50)
def test_mql_innerjoin_instantiation(instance):
    assert isinstance(instance, mql_InnerJoin)

@given(instance=mql_Join_strategy)
@settings(max_examples=50)
def test_mql_join_instantiation(instance):
    assert isinstance(instance, mql_Join)

@given(instance=mql_SelectClause_strategy)
@settings(max_examples=50)
def test_mql_selectclause_instantiation(instance):
    assert isinstance(instance, mql_SelectClause)



@given(instance=mql_SelectClause_strategy)
def test_mql_selectclause_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=mql_FromJoin_strategy)
@settings(max_examples=50)
def test_mql_fromjoin_instantiation(instance):
    assert isinstance(instance, mql_FromJoin)



@given(instance=mql_FromJoin_strategy)
def test_mql_fromjoin_isFetch_setter(instance):
    original = instance.isFetch
    instance.isFetch = original
    assert instance.isFetch == original

@given(instance=FromEntry_strategy)
@settings(max_examples=50)
def test_fromentry_instantiation(instance):
    assert isinstance(instance, FromEntry)

@given(instance=mql_FromCollection_strategy)
@settings(max_examples=50)
def test_mql_fromcollection_instantiation(instance):
    assert isinstance(instance, mql_FromCollection)

@given(instance=mql_FromClass_strategy)
@settings(max_examples=50)
def test_mql_fromclass_instantiation(instance):
    assert isinstance(instance, mql_FromClass)



@given(instance=mql_FromClass_strategy)
def test_mql_fromclass_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=mql_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_mql_variabledeclaration_instantiation(instance):
    assert isinstance(instance, mql_VariableDeclaration)



@given(instance=mql_VariableDeclaration_strategy)
def test_mql_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SelectAggregateExpression_strategy)
@settings(max_examples=50)
def test_selectaggregateexpression_instantiation(instance):
    assert isinstance(instance, SelectAggregateExpression)

@given(instance=mql_MinAggregate_strategy)
@settings(max_examples=50)
def test_mql_minaggregate_instantiation(instance):
    assert isinstance(instance, mql_MinAggregate)

@given(instance=mql_SumAggregate_strategy)
@settings(max_examples=50)
def test_mql_sumaggregate_instantiation(instance):
    assert isinstance(instance, mql_SumAggregate)

@given(instance=mql_MaxAggregate_strategy)
@settings(max_examples=50)
def test_mql_maxaggregate_instantiation(instance):
    assert isinstance(instance, mql_MaxAggregate)

@given(instance=mql_CountAggregate_strategy)
@settings(max_examples=50)
def test_mql_countaggregate_instantiation(instance):
    assert isinstance(instance, mql_CountAggregate)

@given(instance=mql_AvgAggregate_strategy)
@settings(max_examples=50)
def test_mql_avgaggregate_instantiation(instance):
    assert isinstance(instance, mql_AvgAggregate)

@given(instance=SelectExpression_strategy)
@settings(max_examples=50)
def test_selectexpression_instantiation(instance):
    assert isinstance(instance, SelectExpression)

@given(instance=mql_SelectConstructorExpression_strategy)
@settings(max_examples=50)
def test_mql_selectconstructorexpression_instantiation(instance):
    assert isinstance(instance, mql_SelectConstructorExpression)



@given(instance=mql_SelectConstructorExpression_strategy)
def test_mql_selectconstructorexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mql_SelectAggregateExpression_strategy)
@settings(max_examples=50)
def test_mql_selectaggregateexpression_instantiation(instance):
    assert isinstance(instance, mql_SelectAggregateExpression)



@given(instance=mql_SelectAggregateExpression_strategy)
def test_mql_selectaggregateexpression_isDistinct_setter(instance):
    original = instance.isDistinct
    instance.isDistinct = original
    assert instance.isDistinct == original

@given(instance=mql_SelectExpression_strategy)
@settings(max_examples=50)
def test_mql_selectexpression_instantiation(instance):
    assert isinstance(instance, mql_SelectExpression)

@given(instance=mql_Expression_strategy)
@settings(max_examples=50)
def test_mql_expression_instantiation(instance):
    assert isinstance(instance, mql_Expression)

@given(instance=mql_OrderClause_strategy)
@settings(max_examples=50)
def test_mql_orderclause_instantiation(instance):
    assert isinstance(instance, mql_OrderClause)



@given(instance=mql_OrderClause_strategy)
def test_mql_orderclause_isDesc_setter(instance):
    original = instance.isDesc
    instance.isDesc = original
    assert instance.isDesc == original



@given(instance=mql_OrderClause_strategy)
def test_mql_orderclause_isAsc_setter(instance):
    original = instance.isAsc
    instance.isAsc = original
    assert instance.isAsc == original

@given(instance=mql_HavingClause_strategy)
@settings(max_examples=50)
def test_mql_havingclause_instantiation(instance):
    assert isinstance(instance, mql_HavingClause)

@given(instance=mql_FromClause_strategy)
@settings(max_examples=50)
def test_mql_fromclause_instantiation(instance):
    assert isinstance(instance, mql_FromClause)

@given(instance=mql_DeleteClause_strategy)
@settings(max_examples=50)
def test_mql_deleteclause_instantiation(instance):
    assert isinstance(instance, mql_DeleteClause)

@given(instance=mql_Value_strategy)
@settings(max_examples=50)
def test_mql_value_instantiation(instance):
    assert isinstance(instance, mql_Value)

@given(instance=mql_AliasAttributeExpression_strategy)
@settings(max_examples=50)
def test_mql_aliasattributeexpression_instantiation(instance):
    assert isinstance(instance, mql_AliasAttributeExpression)



@given(instance=mql_AliasAttributeExpression_strategy)
def test_mql_aliasattributeexpression_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=mql_UpdateItem_strategy)
@settings(max_examples=50)
def test_mql_updateitem_instantiation(instance):
    assert isinstance(instance, mql_UpdateItem)

@given(instance=mql_SetClause_strategy)
@settings(max_examples=50)
def test_mql_setclause_instantiation(instance):
    assert isinstance(instance, mql_SetClause)

@given(instance=mql_UpdateClause_strategy)
@settings(max_examples=50)
def test_mql_updateclause_instantiation(instance):
    assert isinstance(instance, mql_UpdateClause)

@given(instance=mql_FromEntry_strategy)
@settings(max_examples=50)
def test_mql_fromentry_instantiation(instance):
    assert isinstance(instance, mql_FromEntry)

@given(instance=mql_OrderItem_strategy)
@settings(max_examples=50)
def test_mql_orderitem_instantiation(instance):
    assert isinstance(instance, mql_OrderItem)



@given(instance=mql_OrderItem_strategy)
def test_mql_orderitem_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=mql_SelectFromClause_strategy)
@settings(max_examples=50)
def test_mql_selectfromclause_instantiation(instance):
    assert isinstance(instance, mql_SelectFromClause)

@given(instance=ExpressionTerm_strategy)
@settings(max_examples=50)
def test_expressionterm_instantiation(instance):
    assert isinstance(instance, ExpressionTerm)

@given(instance=mql_Variable_strategy)
@settings(max_examples=50)
def test_mql_variable_instantiation(instance):
    assert isinstance(instance, mql_Variable)

@given(instance=MQuery_strategy)
@settings(max_examples=50)
def test_mquery_instantiation(instance):
    assert isinstance(instance, MQuery)

@given(instance=mql_DeleteStatement_strategy)
@settings(max_examples=50)
def test_mql_deletestatement_instantiation(instance):
    assert isinstance(instance, mql_DeleteStatement)

@given(instance=mql_UpdateStatement_strategy)
@settings(max_examples=50)
def test_mql_updatestatement_instantiation(instance):
    assert isinstance(instance, mql_UpdateStatement)

@given(instance=mql_SelectStatement_strategy)
@settings(max_examples=50)
def test_mql_selectstatement_instantiation(instance):
    assert isinstance(instance, mql_SelectStatement)

@given(instance=mql_WhereClause_strategy)
@settings(max_examples=50)
def test_mql_whereclause_instantiation(instance):
    assert isinstance(instance, mql_WhereClause)

@given(instance=mql_NamedQuery_strategy)
@settings(max_examples=50)
def test_mql_namedquery_instantiation(instance):
    assert isinstance(instance, mql_NamedQuery)



@given(instance=mql_NamedQuery_strategy)
def test_mql_namedquery_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mql_MQuery_strategy)
@settings(max_examples=50)
def test_mql_mquery_instantiation(instance):
    assert isinstance(instance, mql_MQuery)

@given(instance=mql_Import_strategy)
@settings(max_examples=50)
def test_mql_import_instantiation(instance):
    assert isinstance(instance, mql_Import)



@given(instance=mql_Import_strategy)
def test_mql_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=mql_QueryModule_strategy)
@settings(max_examples=50)
def test_mql_querymodule_instantiation(instance):
    assert isinstance(instance, mql_QueryModule)
