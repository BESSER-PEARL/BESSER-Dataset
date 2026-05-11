import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B,
    minher::E,
    Named,
    minher::G,
    minher::C,
    minher::B,
    minher::A,
    minher::Named,
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



def test_minher::e_is_not_abstract():
    assert not inspect.isabstract(minher::E)


def test_minher::e_constructor_exists():
    assert callable(minher::E.__init__)


def test_minher::e_constructor_args():
    sig = inspect.signature(minher::E.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_minher::g_is_not_abstract():
    assert not inspect.isabstract(minher::G)


def test_minher::g_constructor_exists():
    assert callable(minher::G.__init__)


def test_minher::g_constructor_args():
    sig = inspect.signature(minher::G.__init__)
    params = list(sig.parameters.keys())



def test_minher::c_is_not_abstract():
    assert not inspect.isabstract(minher::C)


def test_minher::c_constructor_exists():
    assert callable(minher::C.__init__)


def test_minher::c_constructor_args():
    sig = inspect.signature(minher::C.__init__)
    params = list(sig.parameters.keys())



def test_minher::b_is_not_abstract():
    assert not inspect.isabstract(minher::B)


def test_minher::b_constructor_exists():
    assert callable(minher::B.__init__)


def test_minher::b_constructor_args():
    sig = inspect.signature(minher::B.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minher::b_has_value():
    assert hasattr(minher::B, "value")
    descriptor = None
    for klass in minher::B.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minher::a_is_not_abstract():
    assert not inspect.isabstract(minher::A)


def test_minher::a_constructor_exists():
    assert callable(minher::A.__init__)


def test_minher::a_constructor_args():
    sig = inspect.signature(minher::A.__init__)
    params = list(sig.parameters.keys())



def test_minher::named_is_not_abstract():
    assert not inspect.isabstract(minher::Named)


def test_minher::named_constructor_exists():
    assert callable(minher::Named.__init__)


def test_minher::named_constructor_args():
    sig = inspect.signature(minher::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minher::named_has_name():
    assert hasattr(minher::Named, "name")
    descriptor = None
    for klass in minher::Named.__mro__:
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
minher::E_strategy = st.builds(
    minher::E,
)
Named_strategy = st.builds(
    Named,
)
minher::G_strategy = st.builds(
    minher::G,
)
minher::C_strategy = st.builds(
    minher::C,
)
minher::B_strategy = st.builds(
    minher::B,
    value=
        safe_text
)
minher::A_strategy = st.builds(
    minher::A,
)
minher::Named_strategy = st.builds(
    minher::Named,
    name=
        safe_text
)

@given(instance=B_strategy)
@settings(max_examples=50)
def test_b_instantiation(instance):
    assert isinstance(instance, B)

@given(instance=minher::E_strategy)
@settings(max_examples=50)
def test_minher::e_instantiation(instance):
    assert isinstance(instance, minher::E)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=minher::G_strategy)
@settings(max_examples=50)
def test_minher::g_instantiation(instance):
    assert isinstance(instance, minher::G)

@given(instance=minher::C_strategy)
@settings(max_examples=50)
def test_minher::c_instantiation(instance):
    assert isinstance(instance, minher::C)

@given(instance=minher::B_strategy)
@settings(max_examples=50)
def test_minher::b_instantiation(instance):
    assert isinstance(instance, minher::B)

@given(instance=minher::B_strategy)
def test_minher::b_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=minher::B_strategy)
def test_minher::b_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=minher::A_strategy)
@settings(max_examples=50)
def test_minher::a_instantiation(instance):
    assert isinstance(instance, minher::A)

@given(instance=minher::Named_strategy)
@settings(max_examples=50)
def test_minher::named_instantiation(instance):
    assert isinstance(instance, minher::Named)

@given(instance=minher::Named_strategy)
def test_minher::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minher::Named_strategy)
def test_minher::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
