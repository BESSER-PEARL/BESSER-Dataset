import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A_A3,
    A_A2,
    A_A1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_a3_is_not_abstract():
    assert not inspect.isabstract(A_A3)


def test_a_a3_constructor_exists():
    assert callable(A_A3.__init__)


def test_a_a3_constructor_args():
    sig = inspect.signature(A_A3.__init__)
    params = list(sig.parameters.keys())



def test_a_a2_is_not_abstract():
    assert not inspect.isabstract(A_A2)


def test_a_a2_constructor_exists():
    assert callable(A_A2.__init__)


def test_a_a2_constructor_args():
    sig = inspect.signature(A_A2.__init__)
    params = list(sig.parameters.keys())
    assert "f" in params, "Missing parameter 'f'"

def test_a_a2_has_f():
    assert hasattr(A_A2, "f")
    descriptor = None
    for klass in A_A2.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)



def test_a_a1_is_not_abstract():
    assert not inspect.isabstract(A_A1)


def test_a_a1_constructor_exists():
    assert callable(A_A1.__init__)


def test_a_a1_constructor_args():
    sig = inspect.signature(A_A1.__init__)
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
A_A3_strategy = st.builds(
    A_A3,
)
A_A2_strategy = st.builds(
    A_A2,
    f=
        safe_text
)
A_A1_strategy = st.builds(
    A_A1,
)

@given(instance=A_A3_strategy)
@settings(max_examples=50)
def test_a_a3_instantiation(instance):
    assert isinstance(instance, A_A3)

@given(instance=A_A2_strategy)
@settings(max_examples=50)
def test_a_a2_instantiation(instance):
    assert isinstance(instance, A_A2)



@given(instance=A_A2_strategy)
def test_a_a2_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original

@given(instance=A_A1_strategy)
@settings(max_examples=50)
def test_a_a1_instantiation(instance):
    assert isinstance(instance, A_A1)
