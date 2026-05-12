import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Literal,
    d3ql::BooleanLiteral,
    d3ql::StringLiteral,
    d3ql::IntegerLiteral,
    d3ql::Literal,
    d3ql::FunctionArgument,
    d3ql::FunctionCall,
    d3ql::PathElement,
    d3ql::PathExpression,
    d3ql::EObject,
    d3ql::SelectExpression,
    Named,
    d3ql::Alias,
    d3ql::Named,
    d3ql::AggregateRoot,
    d3ql::SelectStatement,
    d3ql::FromStatement,
    d3ql::Query,
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



def test_d3ql::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(d3ql::BooleanLiteral)


def test_d3ql::booleanliteral_constructor_exists():
    assert callable(d3ql::BooleanLiteral.__init__)


def test_d3ql::booleanliteral_constructor_args():
    sig = inspect.signature(d3ql::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_d3ql::booleanliteral_has_value():
    assert hasattr(d3ql::BooleanLiteral, "value")
    descriptor = None
    for klass in d3ql::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_d3ql::stringliteral_is_not_abstract():
    assert not inspect.isabstract(d3ql::StringLiteral)


def test_d3ql::stringliteral_constructor_exists():
    assert callable(d3ql::StringLiteral.__init__)


def test_d3ql::stringliteral_constructor_args():
    sig = inspect.signature(d3ql::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_d3ql::stringliteral_has_value():
    assert hasattr(d3ql::StringLiteral, "value")
    descriptor = None
    for klass in d3ql::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_d3ql::integerliteral_is_not_abstract():
    assert not inspect.isabstract(d3ql::IntegerLiteral)


def test_d3ql::integerliteral_constructor_exists():
    assert callable(d3ql::IntegerLiteral.__init__)


def test_d3ql::integerliteral_constructor_args():
    sig = inspect.signature(d3ql::IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_d3ql::integerliteral_has_value():
    assert hasattr(d3ql::IntegerLiteral, "value")
    descriptor = None
    for klass in d3ql::IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_d3ql::literal_is_not_abstract():
    assert not inspect.isabstract(d3ql::Literal)


def test_d3ql::literal_constructor_exists():
    assert callable(d3ql::Literal.__init__)


def test_d3ql::literal_constructor_args():
    sig = inspect.signature(d3ql::Literal.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::functionargument_is_not_abstract():
    assert not inspect.isabstract(d3ql::FunctionArgument)


def test_d3ql::functionargument_constructor_exists():
    assert callable(d3ql::FunctionArgument.__init__)


def test_d3ql::functionargument_constructor_args():
    sig = inspect.signature(d3ql::FunctionArgument.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::functioncall_is_not_abstract():
    assert not inspect.isabstract(d3ql::FunctionCall)


def test_d3ql::functioncall_constructor_exists():
    assert callable(d3ql::FunctionCall.__init__)


def test_d3ql::functioncall_constructor_args():
    sig = inspect.signature(d3ql::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_d3ql::functioncall_has_function():
    assert hasattr(d3ql::FunctionCall, "function")
    descriptor = None
    for klass in d3ql::FunctionCall.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_d3ql::pathelement_is_not_abstract():
    assert not inspect.isabstract(d3ql::PathElement)


def test_d3ql::pathelement_constructor_exists():
    assert callable(d3ql::PathElement.__init__)


def test_d3ql::pathelement_constructor_args():
    sig = inspect.signature(d3ql::PathElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_d3ql::pathelement_has_name():
    assert hasattr(d3ql::PathElement, "name")
    descriptor = None
    for klass in d3ql::PathElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_d3ql::pathexpression_is_not_abstract():
    assert not inspect.isabstract(d3ql::PathExpression)


def test_d3ql::pathexpression_constructor_exists():
    assert callable(d3ql::PathExpression.__init__)


def test_d3ql::pathexpression_constructor_args():
    sig = inspect.signature(d3ql::PathExpression.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::eobject_is_not_abstract():
    assert not inspect.isabstract(d3ql::EObject)


def test_d3ql::eobject_constructor_exists():
    assert callable(d3ql::EObject.__init__)


def test_d3ql::eobject_constructor_args():
    sig = inspect.signature(d3ql::EObject.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::selectexpression_is_not_abstract():
    assert not inspect.isabstract(d3ql::SelectExpression)


def test_d3ql::selectexpression_constructor_exists():
    assert callable(d3ql::SelectExpression.__init__)


def test_d3ql::selectexpression_constructor_args():
    sig = inspect.signature(d3ql::SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::alias_is_not_abstract():
    assert not inspect.isabstract(d3ql::Alias)


def test_d3ql::alias_constructor_exists():
    assert callable(d3ql::Alias.__init__)


def test_d3ql::alias_constructor_args():
    sig = inspect.signature(d3ql::Alias.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::named_is_not_abstract():
    assert not inspect.isabstract(d3ql::Named)


def test_d3ql::named_constructor_exists():
    assert callable(d3ql::Named.__init__)


def test_d3ql::named_constructor_args():
    sig = inspect.signature(d3ql::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_d3ql::named_has_name():
    assert hasattr(d3ql::Named, "name")
    descriptor = None
    for klass in d3ql::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_d3ql::aggregateroot_is_not_abstract():
    assert not inspect.isabstract(d3ql::AggregateRoot)


def test_d3ql::aggregateroot_constructor_exists():
    assert callable(d3ql::AggregateRoot.__init__)


def test_d3ql::aggregateroot_constructor_args():
    sig = inspect.signature(d3ql::AggregateRoot.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::selectstatement_is_not_abstract():
    assert not inspect.isabstract(d3ql::SelectStatement)


def test_d3ql::selectstatement_constructor_exists():
    assert callable(d3ql::SelectStatement.__init__)


def test_d3ql::selectstatement_constructor_args():
    sig = inspect.signature(d3ql::SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::fromstatement_is_not_abstract():
    assert not inspect.isabstract(d3ql::FromStatement)


def test_d3ql::fromstatement_constructor_exists():
    assert callable(d3ql::FromStatement.__init__)


def test_d3ql::fromstatement_constructor_args():
    sig = inspect.signature(d3ql::FromStatement.__init__)
    params = list(sig.parameters.keys())



def test_d3ql::query_is_not_abstract():
    assert not inspect.isabstract(d3ql::Query)


def test_d3ql::query_constructor_exists():
    assert callable(d3ql::Query.__init__)


def test_d3ql::query_constructor_args():
    sig = inspect.signature(d3ql::Query.__init__)
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
Literal_strategy = st.builds(
    Literal,
)
d3ql::BooleanLiteral_strategy = st.builds(
    d3ql::BooleanLiteral,
    value=
        safe_text
)
d3ql::StringLiteral_strategy = st.builds(
    d3ql::StringLiteral,
    value=
        safe_text
)
d3ql::IntegerLiteral_strategy = st.builds(
    d3ql::IntegerLiteral,
    value=
        st.integers()
)
d3ql::Literal_strategy = st.builds(
    d3ql::Literal,
)
d3ql::FunctionArgument_strategy = st.builds(
    d3ql::FunctionArgument,
)
d3ql::FunctionCall_strategy = st.builds(
    d3ql::FunctionCall,
    function=
        safe_text
)
d3ql::PathElement_strategy = st.builds(
    d3ql::PathElement,
    name=
        safe_text
)
d3ql::PathExpression_strategy = st.builds(
    d3ql::PathExpression,
)
d3ql::EObject_strategy = st.builds(
    d3ql::EObject,
)
d3ql::SelectExpression_strategy = st.builds(
    d3ql::SelectExpression,
)
Named_strategy = st.builds(
    Named,
)
d3ql::Alias_strategy = st.builds(
    d3ql::Alias,
)
d3ql::Named_strategy = st.builds(
    d3ql::Named,
    name=
        safe_text
)
d3ql::AggregateRoot_strategy = st.builds(
    d3ql::AggregateRoot,
)
d3ql::SelectStatement_strategy = st.builds(
    d3ql::SelectStatement,
)
d3ql::FromStatement_strategy = st.builds(
    d3ql::FromStatement,
)
d3ql::Query_strategy = st.builds(
    d3ql::Query,
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=d3ql::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_d3ql::booleanliteral_instantiation(instance):
    assert isinstance(instance, d3ql::BooleanLiteral)

@given(instance=d3ql::BooleanLiteral_strategy)
def test_d3ql::booleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=d3ql::BooleanLiteral_strategy)
def test_d3ql::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=d3ql::StringLiteral_strategy)
@settings(max_examples=50)
def test_d3ql::stringliteral_instantiation(instance):
    assert isinstance(instance, d3ql::StringLiteral)

@given(instance=d3ql::StringLiteral_strategy)
def test_d3ql::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=d3ql::StringLiteral_strategy)
def test_d3ql::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=d3ql::IntegerLiteral_strategy)
@settings(max_examples=50)
def test_d3ql::integerliteral_instantiation(instance):
    assert isinstance(instance, d3ql::IntegerLiteral)

@given(instance=d3ql::IntegerLiteral_strategy)
def test_d3ql::integerliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=d3ql::IntegerLiteral_strategy)
def test_d3ql::integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=d3ql::Literal_strategy)
@settings(max_examples=50)
def test_d3ql::literal_instantiation(instance):
    assert isinstance(instance, d3ql::Literal)

@given(instance=d3ql::FunctionArgument_strategy)
@settings(max_examples=50)
def test_d3ql::functionargument_instantiation(instance):
    assert isinstance(instance, d3ql::FunctionArgument)

@given(instance=d3ql::FunctionCall_strategy)
@settings(max_examples=50)
def test_d3ql::functioncall_instantiation(instance):
    assert isinstance(instance, d3ql::FunctionCall)

@given(instance=d3ql::FunctionCall_strategy)
def test_d3ql::functioncall_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=d3ql::FunctionCall_strategy)
def test_d3ql::functioncall_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=d3ql::PathElement_strategy)
@settings(max_examples=50)
def test_d3ql::pathelement_instantiation(instance):
    assert isinstance(instance, d3ql::PathElement)

@given(instance=d3ql::PathElement_strategy)
def test_d3ql::pathelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=d3ql::PathElement_strategy)
def test_d3ql::pathelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=d3ql::PathExpression_strategy)
@settings(max_examples=50)
def test_d3ql::pathexpression_instantiation(instance):
    assert isinstance(instance, d3ql::PathExpression)

@given(instance=d3ql::EObject_strategy)
@settings(max_examples=50)
def test_d3ql::eobject_instantiation(instance):
    assert isinstance(instance, d3ql::EObject)

@given(instance=d3ql::SelectExpression_strategy)
@settings(max_examples=50)
def test_d3ql::selectexpression_instantiation(instance):
    assert isinstance(instance, d3ql::SelectExpression)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=d3ql::Alias_strategy)
@settings(max_examples=50)
def test_d3ql::alias_instantiation(instance):
    assert isinstance(instance, d3ql::Alias)

@given(instance=d3ql::Named_strategy)
@settings(max_examples=50)
def test_d3ql::named_instantiation(instance):
    assert isinstance(instance, d3ql::Named)

@given(instance=d3ql::Named_strategy)
def test_d3ql::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=d3ql::Named_strategy)
def test_d3ql::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=d3ql::AggregateRoot_strategy)
@settings(max_examples=50)
def test_d3ql::aggregateroot_instantiation(instance):
    assert isinstance(instance, d3ql::AggregateRoot)

@given(instance=d3ql::SelectStatement_strategy)
@settings(max_examples=50)
def test_d3ql::selectstatement_instantiation(instance):
    assert isinstance(instance, d3ql::SelectStatement)

@given(instance=d3ql::FromStatement_strategy)
@settings(max_examples=50)
def test_d3ql::fromstatement_instantiation(instance):
    assert isinstance(instance, d3ql::FromStatement)

@given(instance=d3ql::Query_strategy)
@settings(max_examples=50)
def test_d3ql::query_instantiation(instance):
    assert isinstance(instance, d3ql::Query)
