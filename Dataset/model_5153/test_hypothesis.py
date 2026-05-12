import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    mytest_C,
    mytest_MyRoot,
    mytest_B,
    mytest_A,
    MyEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_mytest_c_is_not_abstract():
    assert not inspect.isabstract(mytest_C)


def test_mytest_c_constructor_exists():
    assert callable(mytest_C.__init__)


def test_mytest_c_constructor_args():
    sig = inspect.signature(mytest_C.__init__)
    params = list(sig.parameters.keys())



def test_mytest_myroot_is_not_abstract():
    assert not inspect.isabstract(mytest_MyRoot)


def test_mytest_myroot_constructor_exists():
    assert callable(mytest_MyRoot.__init__)


def test_mytest_myroot_constructor_args():
    sig = inspect.signature(mytest_MyRoot.__init__)
    params = list(sig.parameters.keys())



def test_mytest_b_is_not_abstract():
    assert not inspect.isabstract(mytest_B)


def test_mytest_b_constructor_exists():
    assert callable(mytest_B.__init__)


def test_mytest_b_constructor_args():
    sig = inspect.signature(mytest_B.__init__)
    params = list(sig.parameters.keys())
    assert "enumatt" in params, "Missing parameter 'enumatt'"

def test_mytest_b_has_enumatt():
    assert hasattr(mytest_B, "enumatt")
    descriptor = None
    for klass in mytest_B.__mro__:
        if "enumatt" in klass.__dict__:
            descriptor = klass.__dict__["enumatt"]
            break
    assert isinstance(descriptor, property)



def test_mytest_a_is_not_abstract():
    assert not inspect.isabstract(mytest_A)


def test_mytest_a_constructor_exists():
    assert callable(mytest_A.__init__)


def test_mytest_a_constructor_args():
    sig = inspect.signature(mytest_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mytest_a_has_name():
    assert hasattr(mytest_A, "name")
    descriptor = None
    for klass in mytest_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_myenum_exists():
    # Check that the Enumeration exists
    assert MyEnum is not None

def test_myenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MyEnum]
    expected_literals = [
        "ABC",
        "DEF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MyEnum"


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
B_strategy = st.builds(
    B,
)
mytest_C_strategy = st.builds(
    mytest_C,
)
mytest_MyRoot_strategy = st.builds(
    mytest_MyRoot,
)
mytest_B_strategy = st.builds(
    mytest_B,
    enumatt=
        safe_text
)
mytest_A_strategy = st.builds(
    mytest_A,
    name=
        safe_text
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=mytest_C_strategy)
@settings(max_examples=50)
def test_mytest_c_instantiation(instance):
    assert isinstance(instance, mytest_C)

@given(instance=mytest_MyRoot_strategy)
@settings(max_examples=50)
def test_mytest_myroot_instantiation(instance):
    assert isinstance(instance, mytest_MyRoot)

@given(instance=mytest_B_strategy)
@settings(max_examples=50)
def test_mytest_b_instantiation(instance):
    assert isinstance(instance, mytest_B)



@given(instance=mytest_B_strategy)
def test_mytest_b_enumatt_setter(instance):
    original = instance.enumatt
    instance.enumatt = original
    assert instance.enumatt == original

@given(instance=mytest_A_strategy)
@settings(max_examples=50)
def test_mytest_a_instantiation(instance):
    assert isinstance(instance, mytest_A)



@given(instance=mytest_A_strategy)
def test_mytest_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
