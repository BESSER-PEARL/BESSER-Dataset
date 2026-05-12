import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    foo_J,
    J,
    foo_B,
    B,
    foo_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_foo_j_is_not_abstract():
    assert not inspect.isabstract(foo_J)


def test_foo_j_constructor_exists():
    assert callable(foo_J.__init__)


def test_foo_j_constructor_args():
    sig = inspect.signature(foo_J.__init__)
    params = list(sig.parameters.keys())



def test_j_is_not_abstract():
    assert not inspect.isabstract(J)


def test_j_constructor_exists():
    assert callable(J.__init__)


def test_j_constructor_args():
    sig = inspect.signature(J.__init__)
    params = list(sig.parameters.keys())



def test_foo_b_is_not_abstract():
    assert not inspect.isabstract(foo_B)


def test_foo_b_constructor_exists():
    assert callable(foo_B.__init__)


def test_foo_b_constructor_args():
    sig = inspect.signature(foo_B.__init__)
    params = list(sig.parameters.keys())



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_foo_a_is_not_abstract():
    assert not inspect.isabstract(foo_A)


def test_foo_a_constructor_exists():
    assert callable(foo_A.__init__)


def test_foo_a_constructor_args():
    sig = inspect.signature(foo_A.__init__)
    params = list(sig.parameters.keys())
    assert "fooA" in params, "Missing parameter 'fooA'"

def test_foo_a_has_fooA():
    assert hasattr(foo_A, "fooA")
    descriptor = None
    for klass in foo_A.__mro__:
        if "fooA" in klass.__dict__:
            descriptor = klass.__dict__["fooA"]
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
foo_J_strategy = st.builds(
    foo_J,
)
J_strategy = st.builds(
    J,
)
foo_B_strategy = st.builds(
    foo_B,
)
B_strategy = st.builds(
    B,
)
foo_A_strategy = st.builds(
    foo_A,
    fooA=
        safe_text
)

@given(instance=foo_J_strategy)
@settings(max_examples=50)
def test_foo_j_instantiation(instance):
    assert isinstance(instance, foo_J)

@given(instance=J_strategy)
@settings(max_examples=50)
def test_j_instantiation(instance):
    assert isinstance(instance, J)

@given(instance=foo_B_strategy)
@settings(max_examples=50)
def test_foo_b_instantiation(instance):
    assert isinstance(instance, foo_B)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=foo_A_strategy)
@settings(max_examples=50)
def test_foo_a_instantiation(instance):
    assert isinstance(instance, foo_A)



@given(instance=foo_A_strategy)
def test_foo_a_fooA_setter(instance):
    original = instance.fooA
    instance.fooA = original
    assert instance.fooA == original
