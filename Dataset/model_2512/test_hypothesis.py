import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_A,
    test_OptionTestClass,
    test_D,
    A,
    test_C,
    test_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_a_is_not_abstract():
    assert not inspect.isabstract(test_A)


def test_test_a_constructor_exists():
    assert callable(test_A.__init__)


def test_test_a_constructor_args():
    sig = inspect.signature(test_A.__init__)
    params = list(sig.parameters.keys())



def test_test_optiontestclass_is_not_abstract():
    assert not inspect.isabstract(test_OptionTestClass)


def test_test_optiontestclass_constructor_exists():
    assert callable(test_OptionTestClass.__init__)


def test_test_optiontestclass_constructor_args():
    sig = inspect.signature(test_OptionTestClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_test_optiontestclass_has_attribute2():
    assert hasattr(test_OptionTestClass, "attribute2")
    descriptor = None
    for klass in test_OptionTestClass.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_test_optiontestclass_has_attribute():
    assert hasattr(test_OptionTestClass, "attribute")
    descriptor = None
    for klass in test_OptionTestClass.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_test_d_is_not_abstract():
    assert not inspect.isabstract(test_D)


def test_test_d_constructor_exists():
    assert callable(test_D.__init__)


def test_test_d_constructor_args():
    sig = inspect.signature(test_D.__init__)
    params = list(sig.parameters.keys())
    assert "attr1" in params, "Missing parameter 'attr1'"

def test_test_d_has_attr1():
    assert hasattr(test_D, "attr1")
    descriptor = None
    for klass in test_D.__mro__:
        if "attr1" in klass.__dict__:
            descriptor = klass.__dict__["attr1"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_test_c_is_not_abstract():
    assert not inspect.isabstract(test_C)


def test_test_c_constructor_exists():
    assert callable(test_C.__init__)


def test_test_c_constructor_args():
    sig = inspect.signature(test_C.__init__)
    params = list(sig.parameters.keys())



def test_test_b_is_not_abstract():
    assert not inspect.isabstract(test_B)


def test_test_b_constructor_exists():
    assert callable(test_B.__init__)


def test_test_b_constructor_args():
    sig = inspect.signature(test_B.__init__)
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
test_A_strategy = st.builds(
    test_A,
)
test_OptionTestClass_strategy = st.builds(
    test_OptionTestClass,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
test_D_strategy = st.builds(
    test_D,
    attr1=
        safe_text
)
A_strategy = st.builds(
    A,
)
test_C_strategy = st.builds(
    test_C,
)
test_B_strategy = st.builds(
    test_B,
)

@given(instance=test_A_strategy)
@settings(max_examples=50)
def test_test_a_instantiation(instance):
    assert isinstance(instance, test_A)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test_A_strategy)
@settings(max_examples=30)
def test_test_a_op1_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.op1()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.op1).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'op1' in test_A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'op1' in test_A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'op1' in test_A is not implemented or raised an error")

@given(instance=test_OptionTestClass_strategy)
@settings(max_examples=50)
def test_test_optiontestclass_instantiation(instance):
    assert isinstance(instance, test_OptionTestClass)



@given(instance=test_OptionTestClass_strategy)
def test_test_optiontestclass_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=test_OptionTestClass_strategy)
def test_test_optiontestclass_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=test_D_strategy)
@settings(max_examples=50)
def test_test_d_instantiation(instance):
    assert isinstance(instance, test_D)



@given(instance=test_D_strategy)
def test_test_d_attr1_setter(instance):
    original = instance.attr1
    instance.attr1 = original
    assert instance.attr1 == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=test_C_strategy)
@settings(max_examples=50)
def test_test_c_instantiation(instance):
    assert isinstance(instance, test_C)

@given(instance=test_B_strategy)
@settings(max_examples=50)
def test_test_b_instantiation(instance):
    assert isinstance(instance, test_B)
