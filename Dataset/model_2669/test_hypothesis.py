import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B,
    minher_E,
    Named,
    minher_G,
    minher_C,
    minher_B,
    minher_A,
    minher_Named,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_is_not_abstract():
    assert not inspect.isabstract(B)


def test_b_constructor_exists():
    assert callable(B.__init__)


def test_b_constructor_args():
    sig = inspect.signature(B.__init__)
    params = list(sig.parameters.keys())



def test_minher_e_is_not_abstract():
    assert not inspect.isabstract(minher_E)


def test_minher_e_constructor_exists():
    assert callable(minher_E.__init__)


def test_minher_e_constructor_args():
    sig = inspect.signature(minher_E.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_minher_g_is_not_abstract():
    assert not inspect.isabstract(minher_G)


def test_minher_g_constructor_exists():
    assert callable(minher_G.__init__)


def test_minher_g_constructor_args():
    sig = inspect.signature(minher_G.__init__)
    params = list(sig.parameters.keys())



def test_minher_c_is_not_abstract():
    assert not inspect.isabstract(minher_C)


def test_minher_c_constructor_exists():
    assert callable(minher_C.__init__)


def test_minher_c_constructor_args():
    sig = inspect.signature(minher_C.__init__)
    params = list(sig.parameters.keys())



def test_minher_b_is_not_abstract():
    assert not inspect.isabstract(minher_B)


def test_minher_b_constructor_exists():
    assert callable(minher_B.__init__)


def test_minher_b_constructor_args():
    sig = inspect.signature(minher_B.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minher_b_has_value():
    assert hasattr(minher_B, "value")
    descriptor = None
    for klass in minher_B.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minher_a_is_not_abstract():
    assert not inspect.isabstract(minher_A)


def test_minher_a_constructor_exists():
    assert callable(minher_A.__init__)


def test_minher_a_constructor_args():
    sig = inspect.signature(minher_A.__init__)
    params = list(sig.parameters.keys())



def test_minher_named_is_not_abstract():
    assert not inspect.isabstract(minher_Named)


def test_minher_named_constructor_exists():
    assert callable(minher_Named.__init__)


def test_minher_named_constructor_args():
    sig = inspect.signature(minher_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minher_named_has_name():
    assert hasattr(minher_Named, "name")
    descriptor = None
    for klass in minher_Named.__mro__:
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
B_strategy = st.builds(
    B,
)
minher_E_strategy = st.builds(
    minher_E,
)
Named_strategy = st.builds(
    Named,
)
minher_G_strategy = st.builds(
    minher_G,
)
minher_C_strategy = st.builds(
    minher_C,
)
minher_B_strategy = st.builds(
    minher_B,
    value=
        safe_text
)
minher_A_strategy = st.builds(
    minher_A,
)
minher_Named_strategy = st.builds(
    minher_Named,
    name=
        safe_text
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=minher_E_strategy)
@settings(max_examples=50)
def test_minher_e_instantiation(instance):
    assert isinstance(instance, minher_E)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=minher_G_strategy)
@settings(max_examples=50)
def test_minher_g_instantiation(instance):
    assert isinstance(instance, minher_G)

@given(instance=minher_C_strategy)
@settings(max_examples=50)
def test_minher_c_instantiation(instance):
    assert isinstance(instance, minher_C)

@given(instance=minher_B_strategy)
@settings(max_examples=50)
def test_minher_b_instantiation(instance):
    assert isinstance(instance, minher_B)



@given(instance=minher_B_strategy)
def test_minher_b_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=minher_A_strategy)
@settings(max_examples=50)
def test_minher_a_instantiation(instance):
    assert isinstance(instance, minher_A)

@given(instance=minher_Named_strategy)
@settings(max_examples=50)
def test_minher_named_instantiation(instance):
    assert isinstance(instance, minher_Named)



@given(instance=minher_Named_strategy)
def test_minher_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
