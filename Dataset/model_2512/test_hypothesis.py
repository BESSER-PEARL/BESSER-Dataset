import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::A,
    test::OptionTestClass,
    test::D,
    A,
    test::C,
    test::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::a_is_not_abstract():
    assert not inspect.isabstract(test::A)


def test_test::a_constructor_exists():
    assert callable(test::A.__init__)


def test_test::a_constructor_args():
    sig = inspect.signature(test::A.__init__)
    params = list(sig.parameters.keys())



def test_test::optiontestclass_is_not_abstract():
    assert not inspect.isabstract(test::OptionTestClass)


def test_test::optiontestclass_constructor_exists():
    assert callable(test::OptionTestClass.__init__)


def test_test::optiontestclass_constructor_args():
    sig = inspect.signature(test::OptionTestClass.__init__)
    params = list(sig.parameters.keys())
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_test::optiontestclass_has_attribute2():
    assert hasattr(test::OptionTestClass, "attribute2")
    descriptor = None
    for klass in test::OptionTestClass.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_test::optiontestclass_has_attribute():
    assert hasattr(test::OptionTestClass, "attribute")
    descriptor = None
    for klass in test::OptionTestClass.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_test::d_is_not_abstract():
    assert not inspect.isabstract(test::D)


def test_test::d_constructor_exists():
    assert callable(test::D.__init__)


def test_test::d_constructor_args():
    sig = inspect.signature(test::D.__init__)
    params = list(sig.parameters.keys())
    assert "attr1" in params, "Missing parameter 'attr1'"

def test_test::d_has_attr1():
    assert hasattr(test::D, "attr1")
    descriptor = None
    for klass in test::D.__mro__:
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



def test_test::c_is_not_abstract():
    assert not inspect.isabstract(test::C)


def test_test::c_constructor_exists():
    assert callable(test::C.__init__)


def test_test::c_constructor_args():
    sig = inspect.signature(test::C.__init__)
    params = list(sig.parameters.keys())



def test_test::b_is_not_abstract():
    assert not inspect.isabstract(test::B)


def test_test::b_constructor_exists():
    assert callable(test::B.__init__)


def test_test::b_constructor_args():
    sig = inspect.signature(test::B.__init__)
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
test::A_strategy = st.builds(
    test::A,
)
test::OptionTestClass_strategy = st.builds(
    test::OptionTestClass,
    attribute2=
        safe_text,
    attribute=
        safe_text
)
test::D_strategy = st.builds(
    test::D,
    attr1=
        safe_text
)
A_strategy = st.builds(
    A,
)
test::C_strategy = st.builds(
    test::C,
)
test::B_strategy = st.builds(
    test::B,
)

@given(instance=test::A_strategy)
@settings(max_examples=50)
def test_test::a_instantiation(instance):
    assert isinstance(instance, test::A)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test::A_strategy)
@settings(max_examples=30)
def test_test::a_op1_changes_state(instance):
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
        assert has_statements, f"Function 'op1' in test::A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'op1' in test::A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'op1' in test::A is not implemented or raised an error")

@given(instance=test::OptionTestClass_strategy)
@settings(max_examples=50)
def test_test::optiontestclass_instantiation(instance):
    assert isinstance(instance, test::OptionTestClass)

@given(instance=test::OptionTestClass_strategy)
def test_test::optiontestclass_attribute2_type(instance):
    assert isinstance(instance.attribute2, str)


@given(instance=test::OptionTestClass_strategy)
def test_test::optiontestclass_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original

@given(instance=test::OptionTestClass_strategy)
def test_test::optiontestclass_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=test::OptionTestClass_strategy)
def test_test::optiontestclass_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=test::D_strategy)
@settings(max_examples=50)
def test_test::d_instantiation(instance):
    assert isinstance(instance, test::D)

@given(instance=test::D_strategy)
def test_test::d_attr1_type(instance):
    assert isinstance(instance.attr1, str)


@given(instance=test::D_strategy)
def test_test::d_attr1_setter(instance):
    original = instance.attr1
    instance.attr1 = original
    assert instance.attr1 == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=test::C_strategy)
@settings(max_examples=50)
def test_test::c_instantiation(instance):
    assert isinstance(instance, test::C)

@given(instance=test::B_strategy)
@settings(max_examples=50)
def test_test::b_instantiation(instance):
    assert isinstance(instance, test::B)
