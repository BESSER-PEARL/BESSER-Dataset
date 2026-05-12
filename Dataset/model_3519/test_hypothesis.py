import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    modelA_B,
    modelA_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modela_b_is_not_abstract():
    assert not inspect.isabstract(modelA_B)


def test_modela_b_constructor_exists():
    assert callable(modelA_B.__init__)


def test_modela_b_constructor_args():
    sig = inspect.signature(modelA_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_modela_b_has_b():
    assert hasattr(modelA_B, "b")
    descriptor = None
    for klass in modelA_B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_modela_a_is_not_abstract():
    assert not inspect.isabstract(modelA_A)


def test_modela_a_constructor_exists():
    assert callable(modelA_A.__init__)


def test_modela_a_constructor_args():
    sig = inspect.signature(modelA_A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_modela_a_has_a():
    assert hasattr(modelA_A, "a")
    descriptor = None
    for klass in modelA_A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
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
modelA_B_strategy = st.builds(
    modelA_B,
    b=
        st.booleans()
)
modelA_A_strategy = st.builds(
    modelA_A,
    a=
        st.integers()
)

@given(instance=modelA_B_strategy)
@settings(max_examples=50)
def test_modela_b_instantiation(instance):
    assert isinstance(instance, modelA_B)



@given(instance=modelA_B_strategy)
def test_modela_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=modelA_A_strategy)
@settings(max_examples=50)
def test_modela_a_instantiation(instance):
    assert isinstance(instance, modelA_A)



@given(instance=modelA_A_strategy)
def test_modela_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
