import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Literal,
    d3ql_StringLiteral,
    d3ql_BooleanLiteral,
    d3ql_IntegerLiteral,
    d3ql_Literal,
    d3ql_FunctionArgument,
    d3ql_FunctionCall,
    d3ql_PathElement,
    d3ql_PathExpression,
    d3ql_EObject,
    d3ql_SelectExpression,
    Named,
    d3ql_Alias,
    d3ql_Named,
    d3ql_AggregateRoot,
    d3ql_SelectStatement,
    d3ql_FromStatement,
    d3ql_Query,
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



def test_d3ql_stringliteral_is_not_abstract():
    assert not inspect.isabstract(d3ql_StringLiteral)


def test_d3ql_stringliteral_constructor_exists():
    assert callable(d3ql_StringLiteral.__init__)


def test_d3ql_stringliteral_constructor_args():
    sig = inspect.signature(d3ql_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_d3ql_stringliteral_has_value():
    assert hasattr(d3ql_StringLiteral, "value")
    descriptor = None
    for klass in d3ql_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_d3ql_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(d3ql_BooleanLiteral)


def test_d3ql_booleanliteral_constructor_exists():
    assert callable(d3ql_BooleanLiteral.__init__)


def test_d3ql_booleanliteral_constructor_args():
    sig = inspect.signature(d3ql_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_d3ql_booleanliteral_has_value():
    assert hasattr(d3ql_BooleanLiteral, "value")
    descriptor = None
    for klass in d3ql_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_d3ql_integerliteral_is_not_abstract():
    assert not inspect.isabstract(d3ql_IntegerLiteral)


def test_d3ql_integerliteral_constructor_exists():
    assert callable(d3ql_IntegerLiteral.__init__)


def test_d3ql_integerliteral_constructor_args():
    sig = inspect.signature(d3ql_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_d3ql_integerliteral_has_value():
    assert hasattr(d3ql_IntegerLiteral, "value")
    descriptor = None
    for klass in d3ql_IntegerLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_d3ql_literal_is_not_abstract():
    assert not inspect.isabstract(d3ql_Literal)


def test_d3ql_literal_constructor_exists():
    assert callable(d3ql_Literal.__init__)


def test_d3ql_literal_constructor_args():
    sig = inspect.signature(d3ql_Literal.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_functionargument_is_not_abstract():
    assert not inspect.isabstract(d3ql_FunctionArgument)


def test_d3ql_functionargument_constructor_exists():
    assert callable(d3ql_FunctionArgument.__init__)


def test_d3ql_functionargument_constructor_args():
    sig = inspect.signature(d3ql_FunctionArgument.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_functioncall_is_not_abstract():
    assert not inspect.isabstract(d3ql_FunctionCall)


def test_d3ql_functioncall_constructor_exists():
    assert callable(d3ql_FunctionCall.__init__)


def test_d3ql_functioncall_constructor_args():
    sig = inspect.signature(d3ql_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_d3ql_functioncall_has_function():
    assert hasattr(d3ql_FunctionCall, "function")
    descriptor = None
    for klass in d3ql_FunctionCall.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_d3ql_pathelement_is_not_abstract():
    assert not inspect.isabstract(d3ql_PathElement)


def test_d3ql_pathelement_constructor_exists():
    assert callable(d3ql_PathElement.__init__)


def test_d3ql_pathelement_constructor_args():
    sig = inspect.signature(d3ql_PathElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_d3ql_pathelement_has_name():
    assert hasattr(d3ql_PathElement, "name")
    descriptor = None
    for klass in d3ql_PathElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_d3ql_pathexpression_is_not_abstract():
    assert not inspect.isabstract(d3ql_PathExpression)


def test_d3ql_pathexpression_constructor_exists():
    assert callable(d3ql_PathExpression.__init__)


def test_d3ql_pathexpression_constructor_args():
    sig = inspect.signature(d3ql_PathExpression.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_eobject_is_not_abstract():
    assert not inspect.isabstract(d3ql_EObject)


def test_d3ql_eobject_constructor_exists():
    assert callable(d3ql_EObject.__init__)


def test_d3ql_eobject_constructor_args():
    sig = inspect.signature(d3ql_EObject.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_selectexpression_is_not_abstract():
    assert not inspect.isabstract(d3ql_SelectExpression)


def test_d3ql_selectexpression_constructor_exists():
    assert callable(d3ql_SelectExpression.__init__)


def test_d3ql_selectexpression_constructor_args():
    sig = inspect.signature(d3ql_SelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_alias_is_not_abstract():
    assert not inspect.isabstract(d3ql_Alias)


def test_d3ql_alias_constructor_exists():
    assert callable(d3ql_Alias.__init__)


def test_d3ql_alias_constructor_args():
    sig = inspect.signature(d3ql_Alias.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_named_is_not_abstract():
    assert not inspect.isabstract(d3ql_Named)


def test_d3ql_named_constructor_exists():
    assert callable(d3ql_Named.__init__)


def test_d3ql_named_constructor_args():
    sig = inspect.signature(d3ql_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_d3ql_named_has_name():
    assert hasattr(d3ql_Named, "name")
    descriptor = None
    for klass in d3ql_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_d3ql_aggregateroot_is_not_abstract():
    assert not inspect.isabstract(d3ql_AggregateRoot)


def test_d3ql_aggregateroot_constructor_exists():
    assert callable(d3ql_AggregateRoot.__init__)


def test_d3ql_aggregateroot_constructor_args():
    sig = inspect.signature(d3ql_AggregateRoot.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_selectstatement_is_not_abstract():
    assert not inspect.isabstract(d3ql_SelectStatement)


def test_d3ql_selectstatement_constructor_exists():
    assert callable(d3ql_SelectStatement.__init__)


def test_d3ql_selectstatement_constructor_args():
    sig = inspect.signature(d3ql_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_fromstatement_is_not_abstract():
    assert not inspect.isabstract(d3ql_FromStatement)


def test_d3ql_fromstatement_constructor_exists():
    assert callable(d3ql_FromStatement.__init__)


def test_d3ql_fromstatement_constructor_args():
    sig = inspect.signature(d3ql_FromStatement.__init__)
    params = list(sig.parameters.keys())



def test_d3ql_query_is_not_abstract():
    assert not inspect.isabstract(d3ql_Query)


def test_d3ql_query_constructor_exists():
    assert callable(d3ql_Query.__init__)


def test_d3ql_query_constructor_args():
    sig = inspect.signature(d3ql_Query.__init__)
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
d3ql_StringLiteral_strategy = st.builds(
    d3ql_StringLiteral,
    value=
        safe_text
)
d3ql_BooleanLiteral_strategy = st.builds(
    d3ql_BooleanLiteral,
    value=
        safe_text
)
d3ql_IntegerLiteral_strategy = st.builds(
    d3ql_IntegerLiteral,
    value=
        st.integers()
)
d3ql_Literal_strategy = st.builds(
    d3ql_Literal,
)
d3ql_FunctionArgument_strategy = st.builds(
    d3ql_FunctionArgument,
)
d3ql_FunctionCall_strategy = st.builds(
    d3ql_FunctionCall,
    function=
        safe_text
)
d3ql_PathElement_strategy = st.builds(
    d3ql_PathElement,
    name=
        safe_text
)
d3ql_PathExpression_strategy = st.builds(
    d3ql_PathExpression,
)
d3ql_EObject_strategy = st.builds(
    d3ql_EObject,
)
d3ql_SelectExpression_strategy = st.builds(
    d3ql_SelectExpression,
)
Named_strategy = st.builds(
    Named,
)
d3ql_Alias_strategy = st.builds(
    d3ql_Alias,
)
d3ql_Named_strategy = st.builds(
    d3ql_Named,
    name=
        safe_text
)
d3ql_AggregateRoot_strategy = st.builds(
    d3ql_AggregateRoot,
)
d3ql_SelectStatement_strategy = st.builds(
    d3ql_SelectStatement,
)
d3ql_FromStatement_strategy = st.builds(
    d3ql_FromStatement,
)
d3ql_Query_strategy = st.builds(
    d3ql_Query,
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=d3ql_StringLiteral_strategy)
@settings(max_examples=50)
def test_d3ql_stringliteral_instantiation(instance):
    assert isinstance(instance, d3ql_StringLiteral)



@given(instance=d3ql_StringLiteral_strategy)
def test_d3ql_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=d3ql_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_d3ql_booleanliteral_instantiation(instance):
    assert isinstance(instance, d3ql_BooleanLiteral)



@given(instance=d3ql_BooleanLiteral_strategy)
def test_d3ql_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=d3ql_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_d3ql_integerliteral_instantiation(instance):
    assert isinstance(instance, d3ql_IntegerLiteral)



@given(instance=d3ql_IntegerLiteral_strategy)
def test_d3ql_integerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=d3ql_Literal_strategy)
@settings(max_examples=50)
def test_d3ql_literal_instantiation(instance):
    assert isinstance(instance, d3ql_Literal)

@given(instance=d3ql_FunctionArgument_strategy)
@settings(max_examples=50)
def test_d3ql_functionargument_instantiation(instance):
    assert isinstance(instance, d3ql_FunctionArgument)

@given(instance=d3ql_FunctionCall_strategy)
@settings(max_examples=50)
def test_d3ql_functioncall_instantiation(instance):
    assert isinstance(instance, d3ql_FunctionCall)



@given(instance=d3ql_FunctionCall_strategy)
def test_d3ql_functioncall_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=d3ql_PathElement_strategy)
@settings(max_examples=50)
def test_d3ql_pathelement_instantiation(instance):
    assert isinstance(instance, d3ql_PathElement)



@given(instance=d3ql_PathElement_strategy)
def test_d3ql_pathelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=d3ql_PathExpression_strategy)
@settings(max_examples=50)
def test_d3ql_pathexpression_instantiation(instance):
    assert isinstance(instance, d3ql_PathExpression)

@given(instance=d3ql_EObject_strategy)
@settings(max_examples=50)
def test_d3ql_eobject_instantiation(instance):
    assert isinstance(instance, d3ql_EObject)

@given(instance=d3ql_SelectExpression_strategy)
@settings(max_examples=50)
def test_d3ql_selectexpression_instantiation(instance):
    assert isinstance(instance, d3ql_SelectExpression)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=d3ql_Alias_strategy)
@settings(max_examples=50)
def test_d3ql_alias_instantiation(instance):
    assert isinstance(instance, d3ql_Alias)

@given(instance=d3ql_Named_strategy)
@settings(max_examples=50)
def test_d3ql_named_instantiation(instance):
    assert isinstance(instance, d3ql_Named)



@given(instance=d3ql_Named_strategy)
def test_d3ql_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=d3ql_AggregateRoot_strategy)
@settings(max_examples=50)
def test_d3ql_aggregateroot_instantiation(instance):
    assert isinstance(instance, d3ql_AggregateRoot)

@given(instance=d3ql_SelectStatement_strategy)
@settings(max_examples=50)
def test_d3ql_selectstatement_instantiation(instance):
    assert isinstance(instance, d3ql_SelectStatement)

@given(instance=d3ql_FromStatement_strategy)
@settings(max_examples=50)
def test_d3ql_fromstatement_instantiation(instance):
    assert isinstance(instance, d3ql_FromStatement)

@given(instance=d3ql_Query_strategy)
@settings(max_examples=50)
def test_d3ql_query_instantiation(instance):
    assert isinstance(instance, d3ql_Query)
