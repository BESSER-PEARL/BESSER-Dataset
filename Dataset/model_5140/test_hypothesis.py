import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mytest::MyRoot,
    mytest::B,
    mytest::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mytest::myroot_is_not_abstract():
    assert not inspect.isabstract(mytest::MyRoot)


def test_mytest::myroot_constructor_exists():
    assert callable(mytest::MyRoot.__init__)


def test_mytest::myroot_constructor_args():
    sig = inspect.signature(mytest::MyRoot.__init__)
    params = list(sig.parameters.keys())



def test_mytest::b_is_not_abstract():
    assert not inspect.isabstract(mytest::B)


def test_mytest::b_constructor_exists():
    assert callable(mytest::B.__init__)


def test_mytest::b_constructor_args():
    sig = inspect.signature(mytest::B.__init__)
    params = list(sig.parameters.keys())



def test_mytest::a_is_not_abstract():
    assert not inspect.isabstract(mytest::A)


def test_mytest::a_constructor_exists():
    assert callable(mytest::A.__init__)


def test_mytest::a_constructor_args():
    sig = inspect.signature(mytest::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mytest::a_has_name():
    assert hasattr(mytest::A, "name")
    descriptor = None
    for klass in mytest::A.__mro__:
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
mytest::MyRoot_strategy = st.builds(
    mytest::MyRoot,
)
mytest::B_strategy = st.builds(
    mytest::B,
)
mytest::A_strategy = st.builds(
    mytest::A,
    name=
        safe_text
)

@given(instance=mytest::MyRoot_strategy)
@settings(max_examples=50)
def test_mytest::myroot_instantiation(instance):
    assert isinstance(instance, mytest::MyRoot)

@given(instance=mytest::B_strategy)
@settings(max_examples=50)
def test_mytest::b_instantiation(instance):
    assert isinstance(instance, mytest::B)

@given(instance=mytest::A_strategy)
@settings(max_examples=50)
def test_mytest::a_instantiation(instance):
    assert isinstance(instance, mytest::A)

@given(instance=mytest::A_strategy)
def test_mytest::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mytest::A_strategy)
def test_mytest::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
