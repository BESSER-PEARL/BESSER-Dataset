import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    B::If,
    B::Begin,
    B::Skip,
    B::VariableList,
    B::Expression,
    B::Action,
    B::Variable,
    B::Predicate,
    B::Operation,
    B::SET,
    B::Any,
    B::Machine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_b::if_is_not_abstract():
    assert not inspect.isabstract(B::If)


def test_b::if_constructor_exists():
    assert callable(B::If.__init__)


def test_b::if_constructor_args():
    sig = inspect.signature(B::If.__init__)
    params = list(sig.parameters.keys())



def test_b::begin_is_not_abstract():
    assert not inspect.isabstract(B::Begin)


def test_b::begin_constructor_exists():
    assert callable(B::Begin.__init__)


def test_b::begin_constructor_args():
    sig = inspect.signature(B::Begin.__init__)
    params = list(sig.parameters.keys())



def test_b::skip_is_not_abstract():
    assert not inspect.isabstract(B::Skip)


def test_b::skip_constructor_exists():
    assert callable(B::Skip.__init__)


def test_b::skip_constructor_args():
    sig = inspect.signature(B::Skip.__init__)
    params = list(sig.parameters.keys())



def test_b::variablelist_is_not_abstract():
    assert not inspect.isabstract(B::VariableList)


def test_b::variablelist_constructor_exists():
    assert callable(B::VariableList.__init__)


def test_b::variablelist_constructor_args():
    sig = inspect.signature(B::VariableList.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_b::variablelist_has_size():
    assert hasattr(B::VariableList, "size")
    descriptor = None
    for klass in B::VariableList.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_b::expression_is_not_abstract():
    assert not inspect.isabstract(B::Expression)


def test_b::expression_constructor_exists():
    assert callable(B::Expression.__init__)


def test_b::expression_constructor_args():
    sig = inspect.signature(B::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_b::expression_has_expression():
    assert hasattr(B::Expression, "expression")
    descriptor = None
    for klass in B::Expression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_b::action_is_not_abstract():
    assert not inspect.isabstract(B::Action)


def test_b::action_constructor_exists():
    assert callable(B::Action.__init__)


def test_b::action_constructor_args():
    sig = inspect.signature(B::Action.__init__)
    params = list(sig.parameters.keys())



def test_b::variable_is_not_abstract():
    assert not inspect.isabstract(B::Variable)


def test_b::variable_constructor_exists():
    assert callable(B::Variable.__init__)


def test_b::variable_constructor_args():
    sig = inspect.signature(B::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::variable_has_name():
    assert hasattr(B::Variable, "name")
    descriptor = None
    for klass in B::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b::predicate_is_not_abstract():
    assert not inspect.isabstract(B::Predicate)


def test_b::predicate_constructor_exists():
    assert callable(B::Predicate.__init__)


def test_b::predicate_constructor_args():
    sig = inspect.signature(B::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_b::operation_is_not_abstract():
    assert not inspect.isabstract(B::Operation)


def test_b::operation_constructor_exists():
    assert callable(B::Operation.__init__)


def test_b::operation_constructor_args():
    sig = inspect.signature(B::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::operation_has_name():
    assert hasattr(B::Operation, "name")
    descriptor = None
    for klass in B::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b::set_is_not_abstract():
    assert not inspect.isabstract(B::SET)


def test_b::set_constructor_exists():
    assert callable(B::SET.__init__)


def test_b::set_constructor_args():
    sig = inspect.signature(B::SET.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::set_has_name():
    assert hasattr(B::SET, "name")
    descriptor = None
    for klass in B::SET.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b::any_is_not_abstract():
    assert not inspect.isabstract(B::Any)


def test_b::any_constructor_exists():
    assert callable(B::Any.__init__)


def test_b::any_constructor_args():
    sig = inspect.signature(B::Any.__init__)
    params = list(sig.parameters.keys())



def test_b::machine_is_not_abstract():
    assert not inspect.isabstract(B::Machine)


def test_b::machine_constructor_exists():
    assert callable(B::Machine.__init__)


def test_b::machine_constructor_args():
    sig = inspect.signature(B::Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b::machine_has_name():
    assert hasattr(B::Machine, "name")
    descriptor = None
    for klass in B::Machine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
Expression_strategy = st.builds(
    Expression,
)
B::If_strategy = st.builds(
    B::If,
)
B::Begin_strategy = st.builds(
    B::Begin,
)
B::Skip_strategy = st.builds(
    B::Skip,
)
B::VariableList_strategy = st.builds(
    B::VariableList,
    size=
        safe_text
)
B::Expression_strategy = st.builds(
    B::Expression,
    expression=
        safe_text
)
B::Action_strategy = st.builds(
    B::Action,
)
B::Variable_strategy = st.builds(
    B::Variable,
    name=
        safe_text
)
B::Predicate_strategy = st.builds(
    B::Predicate,
)
B::Operation_strategy = st.builds(
    B::Operation,
    name=
        safe_text
)
B::SET_strategy = st.builds(
    B::SET,
    name=
        safe_text
)
B::Any_strategy = st.builds(
    B::Any,
)
B::Machine_strategy = st.builds(
    B::Machine,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=B::If_strategy)
@settings(max_examples=50)
def test_b::if_instantiation(instance):
    assert isinstance(instance, B::If)

@given(instance=B::Begin_strategy)
@settings(max_examples=50)
def test_b::begin_instantiation(instance):
    assert isinstance(instance, B::Begin)

@given(instance=B::Skip_strategy)
@settings(max_examples=50)
def test_b::skip_instantiation(instance):
    assert isinstance(instance, B::Skip)

@given(instance=B::VariableList_strategy)
@settings(max_examples=50)
def test_b::variablelist_instantiation(instance):
    assert isinstance(instance, B::VariableList)

@given(instance=B::VariableList_strategy)
def test_b::variablelist_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=B::VariableList_strategy)
def test_b::variablelist_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=B::Expression_strategy)
@settings(max_examples=50)
def test_b::expression_instantiation(instance):
    assert isinstance(instance, B::Expression)

@given(instance=B::Expression_strategy)
def test_b::expression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=B::Expression_strategy)
def test_b::expression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=B::Action_strategy)
@settings(max_examples=50)
def test_b::action_instantiation(instance):
    assert isinstance(instance, B::Action)

@given(instance=B::Variable_strategy)
@settings(max_examples=50)
def test_b::variable_instantiation(instance):
    assert isinstance(instance, B::Variable)

@given(instance=B::Variable_strategy)
def test_b::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=B::Variable_strategy)
def test_b::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B::Predicate_strategy)
@settings(max_examples=50)
def test_b::predicate_instantiation(instance):
    assert isinstance(instance, B::Predicate)

@given(instance=B::Operation_strategy)
@settings(max_examples=50)
def test_b::operation_instantiation(instance):
    assert isinstance(instance, B::Operation)

@given(instance=B::Operation_strategy)
def test_b::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=B::Operation_strategy)
def test_b::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B::SET_strategy)
@settings(max_examples=50)
def test_b::set_instantiation(instance):
    assert isinstance(instance, B::SET)

@given(instance=B::SET_strategy)
def test_b::set_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=B::SET_strategy)
def test_b::set_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B::Any_strategy)
@settings(max_examples=50)
def test_b::any_instantiation(instance):
    assert isinstance(instance, B::Any)

@given(instance=B::Machine_strategy)
@settings(max_examples=50)
def test_b::machine_instantiation(instance):
    assert isinstance(instance, B::Machine)

@given(instance=B::Machine_strategy)
def test_b::machine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=B::Machine_strategy)
def test_b::machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
