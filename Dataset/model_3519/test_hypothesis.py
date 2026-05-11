import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    modelA::B,
    modelA::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modela::b_is_not_abstract():
    assert not inspect.isabstract(modelA::B)


def test_modela::b_constructor_exists():
    assert callable(modelA::B.__init__)


def test_modela::b_constructor_args():
    sig = inspect.signature(modelA::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_modela::b_has_b():
    assert hasattr(modelA::B, "b")
    descriptor = None
    for klass in modelA::B.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_modela::a_is_not_abstract():
    assert not inspect.isabstract(modelA::A)


def test_modela::a_constructor_exists():
    assert callable(modelA::A.__init__)


def test_modela::a_constructor_args():
    sig = inspect.signature(modelA::A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_modela::a_has_a():
    assert hasattr(modelA::A, "a")
    descriptor = None
    for klass in modelA::A.__mro__:
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
modelA::B_strategy = st.builds(
    modelA::B,
    b=
        st.booleans()
)
modelA::A_strategy = st.builds(
    modelA::A,
    a=
        st.integers()
)

@given(instance=modelA::B_strategy)
@settings(max_examples=50)
def test_modela::b_instantiation(instance):
    assert isinstance(instance, modelA::B)

@given(instance=modelA::B_strategy)
def test_modela::b_b_type(instance):
    assert isinstance(instance.b, bool)


@given(instance=modelA::B_strategy)
def test_modela::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=modelA::A_strategy)
@settings(max_examples=50)
def test_modela::a_instantiation(instance):
    assert isinstance(instance, modelA::A)

@given(instance=modelA::A_strategy)
def test_modela::a_a_type(instance):
    assert isinstance(instance.a, int)


@given(instance=modelA::A_strategy)
def test_modela::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
