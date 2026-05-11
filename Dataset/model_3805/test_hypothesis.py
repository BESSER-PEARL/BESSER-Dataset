import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A::A3,
    A::A2,
    A::A1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::a3_is_not_abstract():
    assert not inspect.isabstract(A::A3)


def test_a::a3_constructor_exists():
    assert callable(A::A3.__init__)


def test_a::a3_constructor_args():
    sig = inspect.signature(A::A3.__init__)
    params = list(sig.parameters.keys())



def test_a::a2_is_not_abstract():
    assert not inspect.isabstract(A::A2)


def test_a::a2_constructor_exists():
    assert callable(A::A2.__init__)


def test_a::a2_constructor_args():
    sig = inspect.signature(A::A2.__init__)
    params = list(sig.parameters.keys())
    assert "f" in params, "Missing parameter 'f'"

def test_a::a2_has_f():
    assert hasattr(A::A2, "f")
    descriptor = None
    for klass in A::A2.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)



def test_a::a1_is_not_abstract():
    assert not inspect.isabstract(A::A1)


def test_a::a1_constructor_exists():
    assert callable(A::A1.__init__)


def test_a::a1_constructor_args():
    sig = inspect.signature(A::A1.__init__)
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
A::A3_strategy = st.builds(
    A::A3,
)
A::A2_strategy = st.builds(
    A::A2,
    f=
        safe_text
)
A::A1_strategy = st.builds(
    A::A1,
)

@given(instance=A::A3_strategy)
@settings(max_examples=50)
def test_a::a3_instantiation(instance):
    assert isinstance(instance, A::A3)

@given(instance=A::A2_strategy)
@settings(max_examples=50)
def test_a::a2_instantiation(instance):
    assert isinstance(instance, A::A2)

@given(instance=A::A2_strategy)
def test_a::a2_f_type(instance):
    assert isinstance(instance.f, str)


@given(instance=A::A2_strategy)
def test_a::a2_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original

@given(instance=A::A1_strategy)
@settings(max_examples=50)
def test_a::a1_instantiation(instance):
    assert isinstance(instance, A::A1)
