import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AB::A,
    AB::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ab::a_is_not_abstract():
    assert not inspect.isabstract(AB::A)


def test_ab::a_constructor_exists():
    assert callable(AB::A.__init__)


def test_ab::a_constructor_args():
    sig = inspect.signature(AB::A.__init__)
    params = list(sig.parameters.keys())
    assert "i" in params, "Missing parameter 'i'"

def test_ab::a_has_i():
    assert hasattr(AB::A, "i")
    descriptor = None
    for klass in AB::A.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)



def test_ab::b_is_not_abstract():
    assert not inspect.isabstract(AB::B)


def test_ab::b_constructor_exists():
    assert callable(AB::B.__init__)


def test_ab::b_constructor_args():
    sig = inspect.signature(AB::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ab::b_has_name():
    assert hasattr(AB::B, "name")
    descriptor = None
    for klass in AB::B.__mro__:
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
AB::A_strategy = st.builds(
    AB::A,
    i=
        st.integers()
)
AB::B_strategy = st.builds(
    AB::B,
    name=
        safe_text
)

@given(instance=AB::A_strategy)
@settings(max_examples=50)
def test_ab::a_instantiation(instance):
    assert isinstance(instance, AB::A)

@given(instance=AB::A_strategy)
def test_ab::a_i_type(instance):
    assert isinstance(instance.i, int)


@given(instance=AB::A_strategy)
def test_ab::a_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=AB::B_strategy)
@settings(max_examples=50)
def test_ab::b_instantiation(instance):
    assert isinstance(instance, AB::B)

@given(instance=AB::B_strategy)
def test_ab::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=AB::B_strategy)
def test_ab::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
