import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    B_Begin,
    B_If,
    B_Skip,
    B_VariableList,
    B_Expression,
    B_Action,
    B_Variable,
    B_Predicate,
    B_Operation,
    B_SET,
    B_Any,
    B_Machine,
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



def test_b_begin_is_not_abstract():
    assert not inspect.isabstract(B_Begin)


def test_b_begin_constructor_exists():
    assert callable(B_Begin.__init__)


def test_b_begin_constructor_args():
    sig = inspect.signature(B_Begin.__init__)
    params = list(sig.parameters.keys())



def test_b_if_is_not_abstract():
    assert not inspect.isabstract(B_If)


def test_b_if_constructor_exists():
    assert callable(B_If.__init__)


def test_b_if_constructor_args():
    sig = inspect.signature(B_If.__init__)
    params = list(sig.parameters.keys())



def test_b_skip_is_not_abstract():
    assert not inspect.isabstract(B_Skip)


def test_b_skip_constructor_exists():
    assert callable(B_Skip.__init__)


def test_b_skip_constructor_args():
    sig = inspect.signature(B_Skip.__init__)
    params = list(sig.parameters.keys())



def test_b_variablelist_is_not_abstract():
    assert not inspect.isabstract(B_VariableList)


def test_b_variablelist_constructor_exists():
    assert callable(B_VariableList.__init__)


def test_b_variablelist_constructor_args():
    sig = inspect.signature(B_VariableList.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_b_variablelist_has_size():
    assert hasattr(B_VariableList, "size")
    descriptor = None
    for klass in B_VariableList.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_b_expression_is_not_abstract():
    assert not inspect.isabstract(B_Expression)


def test_b_expression_constructor_exists():
    assert callable(B_Expression.__init__)


def test_b_expression_constructor_args():
    sig = inspect.signature(B_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_b_expression_has_expression():
    assert hasattr(B_Expression, "expression")
    descriptor = None
    for klass in B_Expression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_b_action_is_not_abstract():
    assert not inspect.isabstract(B_Action)


def test_b_action_constructor_exists():
    assert callable(B_Action.__init__)


def test_b_action_constructor_args():
    sig = inspect.signature(B_Action.__init__)
    params = list(sig.parameters.keys())



def test_b_variable_is_not_abstract():
    assert not inspect.isabstract(B_Variable)


def test_b_variable_constructor_exists():
    assert callable(B_Variable.__init__)


def test_b_variable_constructor_args():
    sig = inspect.signature(B_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_variable_has_name():
    assert hasattr(B_Variable, "name")
    descriptor = None
    for klass in B_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b_predicate_is_not_abstract():
    assert not inspect.isabstract(B_Predicate)


def test_b_predicate_constructor_exists():
    assert callable(B_Predicate.__init__)


def test_b_predicate_constructor_args():
    sig = inspect.signature(B_Predicate.__init__)
    params = list(sig.parameters.keys())



def test_b_operation_is_not_abstract():
    assert not inspect.isabstract(B_Operation)


def test_b_operation_constructor_exists():
    assert callable(B_Operation.__init__)


def test_b_operation_constructor_args():
    sig = inspect.signature(B_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_operation_has_name():
    assert hasattr(B_Operation, "name")
    descriptor = None
    for klass in B_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b_set_is_not_abstract():
    assert not inspect.isabstract(B_SET)


def test_b_set_constructor_exists():
    assert callable(B_SET.__init__)


def test_b_set_constructor_args():
    sig = inspect.signature(B_SET.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_set_has_name():
    assert hasattr(B_SET, "name")
    descriptor = None
    for klass in B_SET.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_b_any_is_not_abstract():
    assert not inspect.isabstract(B_Any)


def test_b_any_constructor_exists():
    assert callable(B_Any.__init__)


def test_b_any_constructor_args():
    sig = inspect.signature(B_Any.__init__)
    params = list(sig.parameters.keys())



def test_b_machine_is_not_abstract():
    assert not inspect.isabstract(B_Machine)


def test_b_machine_constructor_exists():
    assert callable(B_Machine.__init__)


def test_b_machine_constructor_args():
    sig = inspect.signature(B_Machine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_b_machine_has_name():
    assert hasattr(B_Machine, "name")
    descriptor = None
    for klass in B_Machine.__mro__:
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
B_Begin_strategy = st.builds(
    B_Begin,
)
B_If_strategy = st.builds(
    B_If,
)
B_Skip_strategy = st.builds(
    B_Skip,
)
B_VariableList_strategy = st.builds(
    B_VariableList,
    size=
        safe_text
)
B_Expression_strategy = st.builds(
    B_Expression,
    expression=
        safe_text
)
B_Action_strategy = st.builds(
    B_Action,
)
B_Variable_strategy = st.builds(
    B_Variable,
    name=
        safe_text
)
B_Predicate_strategy = st.builds(
    B_Predicate,
)
B_Operation_strategy = st.builds(
    B_Operation,
    name=
        safe_text
)
B_SET_strategy = st.builds(
    B_SET,
    name=
        safe_text
)
B_Any_strategy = st.builds(
    B_Any,
)
B_Machine_strategy = st.builds(
    B_Machine,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=B_Begin_strategy)
@settings(max_examples=50)
def test_b_begin_instantiation(instance):
    assert isinstance(instance, B_Begin)

@given(instance=B_If_strategy)
@settings(max_examples=50)
def test_b_if_instantiation(instance):
    assert isinstance(instance, B_If)

@given(instance=B_Skip_strategy)
@settings(max_examples=50)
def test_b_skip_instantiation(instance):
    assert isinstance(instance, B_Skip)

@given(instance=B_VariableList_strategy)
@settings(max_examples=50)
def test_b_variablelist_instantiation(instance):
    assert isinstance(instance, B_VariableList)



@given(instance=B_VariableList_strategy)
def test_b_variablelist_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=B_Expression_strategy)
@settings(max_examples=50)
def test_b_expression_instantiation(instance):
    assert isinstance(instance, B_Expression)



@given(instance=B_Expression_strategy)
def test_b_expression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=B_Action_strategy)
@settings(max_examples=50)
def test_b_action_instantiation(instance):
    assert isinstance(instance, B_Action)

@given(instance=B_Variable_strategy)
@settings(max_examples=50)
def test_b_variable_instantiation(instance):
    assert isinstance(instance, B_Variable)



@given(instance=B_Variable_strategy)
def test_b_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B_Predicate_strategy)
@settings(max_examples=50)
def test_b_predicate_instantiation(instance):
    assert isinstance(instance, B_Predicate)

@given(instance=B_Operation_strategy)
@settings(max_examples=50)
def test_b_operation_instantiation(instance):
    assert isinstance(instance, B_Operation)



@given(instance=B_Operation_strategy)
def test_b_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B_SET_strategy)
@settings(max_examples=50)
def test_b_set_instantiation(instance):
    assert isinstance(instance, B_SET)



@given(instance=B_SET_strategy)
def test_b_set_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=B_Any_strategy)
@settings(max_examples=50)
def test_b_any_instantiation(instance):
    assert isinstance(instance, B_Any)

@given(instance=B_Machine_strategy)
@settings(max_examples=50)
def test_b_machine_instantiation(instance):
    assert isinstance(instance, B_Machine)



@given(instance=B_Machine_strategy)
def test_b_machine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
