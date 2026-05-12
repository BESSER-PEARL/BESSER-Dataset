import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ArrayExpression,
    query::BooleanArrayExpression,
    query::NullArrayExpression,
    query::StringArrayExpression,
    query::LongArrayExpression,
    query::DateArrayExpression,
    query::DoubleArrayExpression,
    query::ArrayExpression,
    Expression,
    query::LongExpression,
    query::DoubleExpression,
    query::StringExpression,
    query::NullExpression,
    query::BooleanExpression,
    query::DateExpression,
    query::ReplacableValue,
    query::Expression,
    ExpressionWhereEntry,
    query::MultiExpressionWhereEntry,
    query::SingleExpressionWhereEntry,
    WhereEntry,
    query::OrWhereEntry,
    query::AndWhereEntry,
    query::ExpressionWhereEntry,
    query::WhereEntry,
    query::Database,
    query::Model,
    Operator,
    ArrayOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arrayexpression_is_not_abstract():
    assert not inspect.isabstract(ArrayExpression)


def test_arrayexpression_constructor_exists():
    assert callable(ArrayExpression.__init__)


def test_arrayexpression_constructor_args():
    sig = inspect.signature(ArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_query::booleanarrayexpression_is_not_abstract():
    assert not inspect.isabstract(query::BooleanArrayExpression)


def test_query::booleanarrayexpression_constructor_exists():
    assert callable(query::BooleanArrayExpression.__init__)


def test_query::booleanarrayexpression_constructor_args():
    sig = inspect.signature(query::BooleanArrayExpression.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_query::booleanarrayexpression_has_values():
    assert hasattr(query::BooleanArrayExpression, "values")
    descriptor = None
    for klass in query::BooleanArrayExpression.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_query::nullarrayexpression_is_not_abstract():
    assert not inspect.isabstract(query::NullArrayExpression)


def test_query::nullarrayexpression_constructor_exists():
    assert callable(query::NullArrayExpression.__init__)


def test_query::nullarrayexpression_constructor_args():
    sig = inspect.signature(query::NullArrayExpression.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_query::nullarrayexpression_has_values():
    assert hasattr(query::NullArrayExpression, "values")
    descriptor = None
    for klass in query::NullArrayExpression.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_query::stringarrayexpression_is_not_abstract():
    assert not inspect.isabstract(query::StringArrayExpression)


def test_query::stringarrayexpression_constructor_exists():
    assert callable(query::StringArrayExpression.__init__)


def test_query::stringarrayexpression_constructor_args():
    sig = inspect.signature(query::StringArrayExpression.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_query::stringarrayexpression_has_values():
    assert hasattr(query::StringArrayExpression, "values")
    descriptor = None
    for klass in query::StringArrayExpression.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_query::longarrayexpression_is_not_abstract():
    assert not inspect.isabstract(query::LongArrayExpression)


def test_query::longarrayexpression_constructor_exists():
    assert callable(query::LongArrayExpression.__init__)


def test_query::longarrayexpression_constructor_args():
    sig = inspect.signature(query::LongArrayExpression.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_query::longarrayexpression_has_values():
    assert hasattr(query::LongArrayExpression, "values")
    descriptor = None
    for klass in query::LongArrayExpression.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_query::datearrayexpression_is_not_abstract():
    assert not inspect.isabstract(query::DateArrayExpression)


def test_query::datearrayexpression_constructor_exists():
    assert callable(query::DateArrayExpression.__init__)


def test_query::datearrayexpression_constructor_args():
    sig = inspect.signature(query::DateArrayExpression.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_query::datearrayexpression_has_values():
    assert hasattr(query::DateArrayExpression, "values")
    descriptor = None
    for klass in query::DateArrayExpression.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_query::doublearrayexpression_is_not_abstract():
    assert not inspect.isabstract(query::DoubleArrayExpression)


def test_query::doublearrayexpression_constructor_exists():
    assert callable(query::DoubleArrayExpression.__init__)


def test_query::doublearrayexpression_constructor_args():
    sig = inspect.signature(query::DoubleArrayExpression.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_query::doublearrayexpression_has_values():
    assert hasattr(query::DoubleArrayExpression, "values")
    descriptor = None
    for klass in query::DoubleArrayExpression.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_query::arrayexpression_is_not_abstract():
    assert not inspect.isabstract(query::ArrayExpression)


def test_query::arrayexpression_constructor_exists():
    assert callable(query::ArrayExpression.__init__)


def test_query::arrayexpression_constructor_args():
    sig = inspect.signature(query::ArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_query::longexpression_is_not_abstract():
    assert not inspect.isabstract(query::LongExpression)


def test_query::longexpression_constructor_exists():
    assert callable(query::LongExpression.__init__)


def test_query::longexpression_constructor_args():
    sig = inspect.signature(query::LongExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_query::longexpression_has_value():
    assert hasattr(query::LongExpression, "value")
    descriptor = None
    for klass in query::LongExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_query::doubleexpression_is_not_abstract():
    assert not inspect.isabstract(query::DoubleExpression)


def test_query::doubleexpression_constructor_exists():
    assert callable(query::DoubleExpression.__init__)


def test_query::doubleexpression_constructor_args():
    sig = inspect.signature(query::DoubleExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_query::doubleexpression_has_value():
    assert hasattr(query::DoubleExpression, "value")
    descriptor = None
    for klass in query::DoubleExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_query::stringexpression_is_not_abstract():
    assert not inspect.isabstract(query::StringExpression)


def test_query::stringexpression_constructor_exists():
    assert callable(query::StringExpression.__init__)


def test_query::stringexpression_constructor_args():
    sig = inspect.signature(query::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_query::stringexpression_has_value():
    assert hasattr(query::StringExpression, "value")
    descriptor = None
    for klass in query::StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_query::nullexpression_is_not_abstract():
    assert not inspect.isabstract(query::NullExpression)


def test_query::nullexpression_constructor_exists():
    assert callable(query::NullExpression.__init__)


def test_query::nullexpression_constructor_args():
    sig = inspect.signature(query::NullExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_query::nullexpression_has_value():
    assert hasattr(query::NullExpression, "value")
    descriptor = None
    for klass in query::NullExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_query::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(query::BooleanExpression)


def test_query::booleanexpression_constructor_exists():
    assert callable(query::BooleanExpression.__init__)


def test_query::booleanexpression_constructor_args():
    sig = inspect.signature(query::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "true" in params, "Missing parameter 'true'"

def test_query::booleanexpression_has_true():
    assert hasattr(query::BooleanExpression, "true")
    descriptor = None
    for klass in query::BooleanExpression.__mro__:
        if "true" in klass.__dict__:
            descriptor = klass.__dict__["true"]
            break
    assert isinstance(descriptor, property)



def test_query::dateexpression_is_not_abstract():
    assert not inspect.isabstract(query::DateExpression)


def test_query::dateexpression_constructor_exists():
    assert callable(query::DateExpression.__init__)


def test_query::dateexpression_constructor_args():
    sig = inspect.signature(query::DateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_query::dateexpression_has_value():
    assert hasattr(query::DateExpression, "value")
    descriptor = None
    for klass in query::DateExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_query::replacablevalue_is_not_abstract():
    assert not inspect.isabstract(query::ReplacableValue)


def test_query::replacablevalue_constructor_exists():
    assert callable(query::ReplacableValue.__init__)


def test_query::replacablevalue_constructor_args():
    sig = inspect.signature(query::ReplacableValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_query::replacablevalue_has_value():
    assert hasattr(query::ReplacableValue, "value")
    descriptor = None
    for klass in query::ReplacableValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_query::expression_is_not_abstract():
    assert not inspect.isabstract(query::Expression)


def test_query::expression_constructor_exists():
    assert callable(query::Expression.__init__)


def test_query::expression_constructor_args():
    sig = inspect.signature(query::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressionwhereentry_is_not_abstract():
    assert not inspect.isabstract(ExpressionWhereEntry)


def test_expressionwhereentry_constructor_exists():
    assert callable(ExpressionWhereEntry.__init__)


def test_expressionwhereentry_constructor_args():
    sig = inspect.signature(ExpressionWhereEntry.__init__)
    params = list(sig.parameters.keys())



def test_query::multiexpressionwhereentry_is_not_abstract():
    assert not inspect.isabstract(query::MultiExpressionWhereEntry)


def test_query::multiexpressionwhereentry_constructor_exists():
    assert callable(query::MultiExpressionWhereEntry.__init__)


def test_query::multiexpressionwhereentry_constructor_args():
    sig = inspect.signature(query::MultiExpressionWhereEntry.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_query::multiexpressionwhereentry_has_operator():
    assert hasattr(query::MultiExpressionWhereEntry, "operator")
    descriptor = None
    for klass in query::MultiExpressionWhereEntry.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_query::singleexpressionwhereentry_is_not_abstract():
    assert not inspect.isabstract(query::SingleExpressionWhereEntry)


def test_query::singleexpressionwhereentry_constructor_exists():
    assert callable(query::SingleExpressionWhereEntry.__init__)


def test_query::singleexpressionwhereentry_constructor_args():
    sig = inspect.signature(query::SingleExpressionWhereEntry.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_query::singleexpressionwhereentry_has_operator():
    assert hasattr(query::SingleExpressionWhereEntry, "operator")
    descriptor = None
    for klass in query::SingleExpressionWhereEntry.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_whereentry_is_not_abstract():
    assert not inspect.isabstract(WhereEntry)


def test_whereentry_constructor_exists():
    assert callable(WhereEntry.__init__)


def test_whereentry_constructor_args():
    sig = inspect.signature(WhereEntry.__init__)
    params = list(sig.parameters.keys())



def test_query::orwhereentry_is_not_abstract():
    assert not inspect.isabstract(query::OrWhereEntry)


def test_query::orwhereentry_constructor_exists():
    assert callable(query::OrWhereEntry.__init__)


def test_query::orwhereentry_constructor_args():
    sig = inspect.signature(query::OrWhereEntry.__init__)
    params = list(sig.parameters.keys())



def test_query::andwhereentry_is_not_abstract():
    assert not inspect.isabstract(query::AndWhereEntry)


def test_query::andwhereentry_constructor_exists():
    assert callable(query::AndWhereEntry.__init__)


def test_query::andwhereentry_constructor_args():
    sig = inspect.signature(query::AndWhereEntry.__init__)
    params = list(sig.parameters.keys())



def test_query::expressionwhereentry_is_not_abstract():
    assert not inspect.isabstract(query::ExpressionWhereEntry)


def test_query::expressionwhereentry_constructor_exists():
    assert callable(query::ExpressionWhereEntry.__init__)


def test_query::expressionwhereentry_constructor_args():
    sig = inspect.signature(query::ExpressionWhereEntry.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_query::expressionwhereentry_has_name():
    assert hasattr(query::ExpressionWhereEntry, "name")
    descriptor = None
    for klass in query::ExpressionWhereEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_query::whereentry_is_not_abstract():
    assert not inspect.isabstract(query::WhereEntry)


def test_query::whereentry_constructor_exists():
    assert callable(query::WhereEntry.__init__)


def test_query::whereentry_constructor_args():
    sig = inspect.signature(query::WhereEntry.__init__)
    params = list(sig.parameters.keys())



def test_query::database_is_not_abstract():
    assert not inspect.isabstract(query::Database)


def test_query::database_constructor_exists():
    assert callable(query::Database.__init__)


def test_query::database_constructor_args():
    sig = inspect.signature(query::Database.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dbName" in params, "Missing parameter 'dbName'"
    assert "port" in params, "Missing parameter 'port'"
    assert "url" in params, "Missing parameter 'url'"

def test_query::database_has_name():
    assert hasattr(query::Database, "name")
    descriptor = None
    for klass in query::Database.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_query::database_has_dbName():
    assert hasattr(query::Database, "dbName")
    descriptor = None
    for klass in query::Database.__mro__:
        if "dbName" in klass.__dict__:
            descriptor = klass.__dict__["dbName"]
            break
    assert isinstance(descriptor, property)

def test_query::database_has_port():
    assert hasattr(query::Database, "port")
    descriptor = None
    for klass in query::Database.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_query::database_has_url():
    assert hasattr(query::Database, "url")
    descriptor = None
    for klass in query::Database.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_query::model_is_not_abstract():
    assert not inspect.isabstract(query::Model)


def test_query::model_constructor_exists():
    assert callable(query::Model.__init__)


def test_query::model_constructor_args():
    sig = inspect.signature(query::Model.__init__)
    params = list(sig.parameters.keys())
    assert "attrs" in params, "Missing parameter 'attrs'"

def test_query::model_has_attrs():
    assert hasattr(query::Model, "attrs")
    descriptor = None
    for klass in query::Model.__mro__:
        if "attrs" in klass.__dict__:
            descriptor = klass.__dict__["attrs"]
            break
    assert isinstance(descriptor, property)

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "like",
        "greaterEqual",
        "greaterThen",
        "notEqual",
        "notIn",
        "lessThen",
        "in_",
        "lessEqual",
        "equal",
        "notLike",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_arrayoperator_exists():
    # Check that the Enumeration exists
    assert ArrayOperator is not None

def test_arrayoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrayOperator]
    expected_literals = [
        "sql_notIn",
        "mongo_all",
        "mongo_in",
        "sql_in",
        "mongo_nin",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrayOperator"


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
ArrayExpression_strategy = st.builds(
    ArrayExpression,
)
query::BooleanArrayExpression_strategy = st.builds(
    query::BooleanArrayExpression,
    values=
        safe_text
)
query::NullArrayExpression_strategy = st.builds(
    query::NullArrayExpression,
    values=
        safe_text
)
query::StringArrayExpression_strategy = st.builds(
    query::StringArrayExpression,
    values=
        safe_text
)
query::LongArrayExpression_strategy = st.builds(
    query::LongArrayExpression,
    values=
        safe_text
)
query::DateArrayExpression_strategy = st.builds(
    query::DateArrayExpression,
    values=
        st.dates()
)
query::DoubleArrayExpression_strategy = st.builds(
    query::DoubleArrayExpression,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
query::ArrayExpression_strategy = st.builds(
    query::ArrayExpression,
)
Expression_strategy = st.builds(
    Expression,
)
query::LongExpression_strategy = st.builds(
    query::LongExpression,
    value=
        safe_text
)
query::DoubleExpression_strategy = st.builds(
    query::DoubleExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
query::StringExpression_strategy = st.builds(
    query::StringExpression,
    value=
        safe_text
)
query::NullExpression_strategy = st.builds(
    query::NullExpression,
    value=
        safe_text
)
query::BooleanExpression_strategy = st.builds(
    query::BooleanExpression,
    true=
        safe_text
)
query::DateExpression_strategy = st.builds(
    query::DateExpression,
    value=
        st.dates()
)
query::ReplacableValue_strategy = st.builds(
    query::ReplacableValue,
    value=
        safe_text
)
query::Expression_strategy = st.builds(
    query::Expression,
)
ExpressionWhereEntry_strategy = st.builds(
    ExpressionWhereEntry,
)
query::MultiExpressionWhereEntry_strategy = st.builds(
    query::MultiExpressionWhereEntry,
    operator=
        safe_text
)
query::SingleExpressionWhereEntry_strategy = st.builds(
    query::SingleExpressionWhereEntry,
    operator=
        safe_text
)
WhereEntry_strategy = st.builds(
    WhereEntry,
)
query::OrWhereEntry_strategy = st.builds(
    query::OrWhereEntry,
)
query::AndWhereEntry_strategy = st.builds(
    query::AndWhereEntry,
)
query::ExpressionWhereEntry_strategy = st.builds(
    query::ExpressionWhereEntry,
    name=
        safe_text
)
query::WhereEntry_strategy = st.builds(
    query::WhereEntry,
)
query::Database_strategy = st.builds(
    query::Database,
    name=
        safe_text,
    dbName=
        safe_text,
    port=
        safe_text,
    url=
        safe_text
)
query::Model_strategy = st.builds(
    query::Model,
    attrs=
        safe_text
)

@given(instance=ArrayExpression_strategy)
@settings(max_examples=50)
def test_arrayexpression_instantiation(instance):
    assert isinstance(instance, ArrayExpression)

@given(instance=query::BooleanArrayExpression_strategy)
@settings(max_examples=50)
def test_query::booleanarrayexpression_instantiation(instance):
    assert isinstance(instance, query::BooleanArrayExpression)

@given(instance=query::BooleanArrayExpression_strategy)
def test_query::booleanarrayexpression_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=query::BooleanArrayExpression_strategy)
def test_query::booleanarrayexpression_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=query::NullArrayExpression_strategy)
@settings(max_examples=50)
def test_query::nullarrayexpression_instantiation(instance):
    assert isinstance(instance, query::NullArrayExpression)

@given(instance=query::NullArrayExpression_strategy)
def test_query::nullarrayexpression_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=query::NullArrayExpression_strategy)
def test_query::nullarrayexpression_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=query::StringArrayExpression_strategy)
@settings(max_examples=50)
def test_query::stringarrayexpression_instantiation(instance):
    assert isinstance(instance, query::StringArrayExpression)

@given(instance=query::StringArrayExpression_strategy)
def test_query::stringarrayexpression_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=query::StringArrayExpression_strategy)
def test_query::stringarrayexpression_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=query::LongArrayExpression_strategy)
@settings(max_examples=50)
def test_query::longarrayexpression_instantiation(instance):
    assert isinstance(instance, query::LongArrayExpression)

@given(instance=query::LongArrayExpression_strategy)
def test_query::longarrayexpression_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=query::LongArrayExpression_strategy)
def test_query::longarrayexpression_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=query::DateArrayExpression_strategy)
@settings(max_examples=50)
def test_query::datearrayexpression_instantiation(instance):
    assert isinstance(instance, query::DateArrayExpression)

@given(instance=query::DateArrayExpression_strategy)
def test_query::datearrayexpression_values_type(instance):
    assert isinstance(instance.values, date)


@given(instance=query::DateArrayExpression_strategy)
def test_query::datearrayexpression_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=query::DoubleArrayExpression_strategy)
@settings(max_examples=50)
def test_query::doublearrayexpression_instantiation(instance):
    assert isinstance(instance, query::DoubleArrayExpression)

@given(instance=query::DoubleArrayExpression_strategy)
def test_query::doublearrayexpression_values_type(instance):
    assert isinstance(instance.values, float)


@given(instance=query::DoubleArrayExpression_strategy)
def test_query::doublearrayexpression_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=query::ArrayExpression_strategy)
@settings(max_examples=50)
def test_query::arrayexpression_instantiation(instance):
    assert isinstance(instance, query::ArrayExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=query::LongExpression_strategy)
@settings(max_examples=50)
def test_query::longexpression_instantiation(instance):
    assert isinstance(instance, query::LongExpression)

@given(instance=query::LongExpression_strategy)
def test_query::longexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=query::LongExpression_strategy)
def test_query::longexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=query::DoubleExpression_strategy)
@settings(max_examples=50)
def test_query::doubleexpression_instantiation(instance):
    assert isinstance(instance, query::DoubleExpression)

@given(instance=query::DoubleExpression_strategy)
def test_query::doubleexpression_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=query::DoubleExpression_strategy)
def test_query::doubleexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=query::StringExpression_strategy)
@settings(max_examples=50)
def test_query::stringexpression_instantiation(instance):
    assert isinstance(instance, query::StringExpression)

@given(instance=query::StringExpression_strategy)
def test_query::stringexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=query::StringExpression_strategy)
def test_query::stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=query::NullExpression_strategy)
@settings(max_examples=50)
def test_query::nullexpression_instantiation(instance):
    assert isinstance(instance, query::NullExpression)

@given(instance=query::NullExpression_strategy)
def test_query::nullexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=query::NullExpression_strategy)
def test_query::nullexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=query::BooleanExpression_strategy)
@settings(max_examples=50)
def test_query::booleanexpression_instantiation(instance):
    assert isinstance(instance, query::BooleanExpression)

@given(instance=query::BooleanExpression_strategy)
def test_query::booleanexpression_true_type(instance):
    assert isinstance(instance.true, str)


@given(instance=query::BooleanExpression_strategy)
def test_query::booleanexpression_true_setter(instance):
    original = instance.true
    instance.true = original
    assert instance.true == original

@given(instance=query::DateExpression_strategy)
@settings(max_examples=50)
def test_query::dateexpression_instantiation(instance):
    assert isinstance(instance, query::DateExpression)

@given(instance=query::DateExpression_strategy)
def test_query::dateexpression_value_type(instance):
    assert isinstance(instance.value, date)


@given(instance=query::DateExpression_strategy)
def test_query::dateexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=query::ReplacableValue_strategy)
@settings(max_examples=50)
def test_query::replacablevalue_instantiation(instance):
    assert isinstance(instance, query::ReplacableValue)

@given(instance=query::ReplacableValue_strategy)
def test_query::replacablevalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=query::ReplacableValue_strategy)
def test_query::replacablevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=query::Expression_strategy)
@settings(max_examples=50)
def test_query::expression_instantiation(instance):
    assert isinstance(instance, query::Expression)

@given(instance=ExpressionWhereEntry_strategy)
@settings(max_examples=50)
def test_expressionwhereentry_instantiation(instance):
    assert isinstance(instance, ExpressionWhereEntry)

@given(instance=query::MultiExpressionWhereEntry_strategy)
@settings(max_examples=50)
def test_query::multiexpressionwhereentry_instantiation(instance):
    assert isinstance(instance, query::MultiExpressionWhereEntry)

@given(instance=query::MultiExpressionWhereEntry_strategy)
def test_query::multiexpressionwhereentry_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=query::MultiExpressionWhereEntry_strategy)
def test_query::multiexpressionwhereentry_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=query::SingleExpressionWhereEntry_strategy)
@settings(max_examples=50)
def test_query::singleexpressionwhereentry_instantiation(instance):
    assert isinstance(instance, query::SingleExpressionWhereEntry)

@given(instance=query::SingleExpressionWhereEntry_strategy)
def test_query::singleexpressionwhereentry_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=query::SingleExpressionWhereEntry_strategy)
def test_query::singleexpressionwhereentry_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=WhereEntry_strategy)
@settings(max_examples=50)
def test_whereentry_instantiation(instance):
    assert isinstance(instance, WhereEntry)

@given(instance=query::OrWhereEntry_strategy)
@settings(max_examples=50)
def test_query::orwhereentry_instantiation(instance):
    assert isinstance(instance, query::OrWhereEntry)

@given(instance=query::AndWhereEntry_strategy)
@settings(max_examples=50)
def test_query::andwhereentry_instantiation(instance):
    assert isinstance(instance, query::AndWhereEntry)

@given(instance=query::ExpressionWhereEntry_strategy)
@settings(max_examples=50)
def test_query::expressionwhereentry_instantiation(instance):
    assert isinstance(instance, query::ExpressionWhereEntry)

@given(instance=query::ExpressionWhereEntry_strategy)
def test_query::expressionwhereentry_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=query::ExpressionWhereEntry_strategy)
def test_query::expressionwhereentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=query::WhereEntry_strategy)
@settings(max_examples=50)
def test_query::whereentry_instantiation(instance):
    assert isinstance(instance, query::WhereEntry)

@given(instance=query::Database_strategy)
@settings(max_examples=50)
def test_query::database_instantiation(instance):
    assert isinstance(instance, query::Database)

@given(instance=query::Database_strategy)
def test_query::database_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=query::Database_strategy)
def test_query::database_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=query::Database_strategy)
def test_query::database_dbName_type(instance):
    assert isinstance(instance.dbName, str)


@given(instance=query::Database_strategy)
def test_query::database_dbName_setter(instance):
    original = instance.dbName
    instance.dbName = original
    assert instance.dbName == original

@given(instance=query::Database_strategy)
def test_query::database_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=query::Database_strategy)
def test_query::database_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=query::Database_strategy)
def test_query::database_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=query::Database_strategy)
def test_query::database_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=query::Model_strategy)
@settings(max_examples=50)
def test_query::model_instantiation(instance):
    assert isinstance(instance, query::Model)

@given(instance=query::Model_strategy)
def test_query::model_attrs_type(instance):
    assert isinstance(instance.attrs, str)


@given(instance=query::Model_strategy)
def test_query::model_attrs_setter(instance):
    original = instance.attrs
    instance.attrs = original
    assert instance.attrs == original
