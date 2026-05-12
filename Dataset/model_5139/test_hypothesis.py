import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mytest_A,
    mytest_MyRoot,
    mytest_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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
mytest_A_strategy = st.builds(
    mytest_A,
    name=
        safe_text
)
mytest_MyRoot_strategy = st.builds(
    mytest_MyRoot,
)
mytest_B_strategy = st.builds(
    mytest_B,
)

@given(instance=mytest_A_strategy)
@settings(max_examples=50)
def test_mytest_a_instantiation(instance):
    assert isinstance(instance, mytest_A)



@given(instance=mytest_A_strategy)
def test_mytest_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mytest_MyRoot_strategy)
@settings(max_examples=50)
def test_mytest_myroot_instantiation(instance):
    assert isinstance(instance, mytest_MyRoot)

@given(instance=mytest_B_strategy)
@settings(max_examples=50)
def test_mytest_b_instantiation(instance):
    assert isinstance(instance, mytest_B)
