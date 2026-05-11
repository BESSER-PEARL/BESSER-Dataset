import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    p::C,
    p::B,
    p::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p::c_is_not_abstract():
    assert not inspect.isabstract(p::C)


def test_p::c_constructor_exists():
    assert callable(p::C.__init__)


def test_p::c_constructor_args():
    sig = inspect.signature(p::C.__init__)
    params = list(sig.parameters.keys())



def test_p::b_is_not_abstract():
    assert not inspect.isabstract(p::B)


def test_p::b_constructor_exists():
    assert callable(p::B.__init__)


def test_p::b_constructor_args():
    sig = inspect.signature(p::B.__init__)
    params = list(sig.parameters.keys())



def test_p::a_is_not_abstract():
    assert not inspect.isabstract(p::A)


def test_p::a_constructor_exists():
    assert callable(p::A.__init__)


def test_p::a_constructor_args():
    sig = inspect.signature(p::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_p::a_has_name():
    assert hasattr(p::A, "name")
    descriptor = None
    for klass in p::A.__mro__:
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
p::C_strategy = st.builds(
    p::C,
)
p::B_strategy = st.builds(
    p::B,
)
p::A_strategy = st.builds(
    p::A,
    name=
        safe_text
)

@given(instance=p::C_strategy)
@settings(max_examples=50)
def test_p::c_instantiation(instance):
    assert isinstance(instance, p::C)

@given(instance=p::B_strategy)
@settings(max_examples=50)
def test_p::b_instantiation(instance):
    assert isinstance(instance, p::B)

@given(instance=p::A_strategy)
@settings(max_examples=50)
def test_p::a_instantiation(instance):
    assert isinstance(instance, p::A)

@given(instance=p::A_strategy)
def test_p::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=p::A_strategy)
def test_p::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
