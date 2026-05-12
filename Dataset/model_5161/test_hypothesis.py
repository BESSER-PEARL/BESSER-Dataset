import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RootIn,
    in_B,
    in_A,
    in_RootIn,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rootin_is_not_abstract():
    assert not inspect.isabstract(RootIn)


def test_rootin_constructor_exists():
    assert callable(RootIn.__init__)


def test_rootin_constructor_args():
    sig = inspect.signature(RootIn.__init__)
    params = list(sig.parameters.keys())



def test_in_b_is_not_abstract():
    assert not inspect.isabstract(in_B)


def test_in_b_constructor_exists():
    assert callable(in_B.__init__)


def test_in_b_constructor_args():
    sig = inspect.signature(in_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_in_b_has_name():
    assert hasattr(in_B, "name")
    descriptor = None
    for klass in in_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_in_a_is_not_abstract():
    assert not inspect.isabstract(in_A)


def test_in_a_constructor_exists():
    assert callable(in_A.__init__)


def test_in_a_constructor_args():
    sig = inspect.signature(in_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_in_a_has_name():
    assert hasattr(in_A, "name")
    descriptor = None
    for klass in in_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_in_rootin_is_not_abstract():
    assert not inspect.isabstract(in_RootIn)


def test_in_rootin_constructor_exists():
    assert callable(in_RootIn.__init__)


def test_in_rootin_constructor_args():
    sig = inspect.signature(in_RootIn.__init__)
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
RootIn_strategy = st.builds(
    RootIn,
)
in_B_strategy = st.builds(
    in_B,
    name=
        safe_text
)
in_A_strategy = st.builds(
    in_A,
    name=
        safe_text
)
in_RootIn_strategy = st.builds(
    in_RootIn,
)

@given(instance=RootIn_strategy)
@settings(max_examples=50)
def test_rootin_instantiation(instance):
    assert isinstance(instance, RootIn)

@given(instance=in_B_strategy)
@settings(max_examples=50)
def test_in_b_instantiation(instance):
    assert isinstance(instance, in_B)



@given(instance=in_B_strategy)
def test_in_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=in_A_strategy)
@settings(max_examples=50)
def test_in_a_instantiation(instance):
    assert isinstance(instance, in_A)



@given(instance=in_A_strategy)
def test_in_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=in_RootIn_strategy)
@settings(max_examples=50)
def test_in_rootin_instantiation(instance):
    assert isinstance(instance, in_RootIn)
