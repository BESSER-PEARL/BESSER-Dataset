import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    p_C,
    p_B,
    p_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_p_c_is_not_abstract():
    assert not inspect.isabstract(p_C)


def test_p_c_constructor_exists():
    assert callable(p_C.__init__)


def test_p_c_constructor_args():
    sig = inspect.signature(p_C.__init__)
    params = list(sig.parameters.keys())



def test_p_b_is_not_abstract():
    assert not inspect.isabstract(p_B)


def test_p_b_constructor_exists():
    assert callable(p_B.__init__)


def test_p_b_constructor_args():
    sig = inspect.signature(p_B.__init__)
    params = list(sig.parameters.keys())



def test_p_a_is_not_abstract():
    assert not inspect.isabstract(p_A)


def test_p_a_constructor_exists():
    assert callable(p_A.__init__)


def test_p_a_constructor_args():
    sig = inspect.signature(p_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_p_a_has_name():
    assert hasattr(p_A, "name")
    descriptor = None
    for klass in p_A.__mro__:
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
p_C_strategy = st.builds(
    p_C,
)
p_B_strategy = st.builds(
    p_B,
)
p_A_strategy = st.builds(
    p_A,
    name=
        safe_text
)

@given(instance=p_C_strategy)
@settings(max_examples=50)
def test_p_c_instantiation(instance):
    assert isinstance(instance, p_C)

@given(instance=p_B_strategy)
@settings(max_examples=50)
def test_p_b_instantiation(instance):
    assert isinstance(instance, p_B)

@given(instance=p_A_strategy)
@settings(max_examples=50)
def test_p_a_instantiation(instance):
    assert isinstance(instance, p_A)



@given(instance=p_A_strategy)
def test_p_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
