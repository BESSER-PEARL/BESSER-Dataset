import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LHS::D,
    LHS::C,
    LHS::B,
    LHS::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lhs::d_is_not_abstract():
    assert not inspect.isabstract(LHS::D)


def test_lhs::d_constructor_exists():
    assert callable(LHS::D.__init__)


def test_lhs::d_constructor_args():
    sig = inspect.signature(LHS::D.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lhs::d_has_name():
    assert hasattr(LHS::D, "name")
    descriptor = None
    for klass in LHS::D.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lhs::c_is_not_abstract():
    assert not inspect.isabstract(LHS::C)


def test_lhs::c_constructor_exists():
    assert callable(LHS::C.__init__)


def test_lhs::c_constructor_args():
    sig = inspect.signature(LHS::C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lhs::c_has_name():
    assert hasattr(LHS::C, "name")
    descriptor = None
    for klass in LHS::C.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lhs::b_is_not_abstract():
    assert not inspect.isabstract(LHS::B)


def test_lhs::b_constructor_exists():
    assert callable(LHS::B.__init__)


def test_lhs::b_constructor_args():
    sig = inspect.signature(LHS::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lhs::b_has_name():
    assert hasattr(LHS::B, "name")
    descriptor = None
    for klass in LHS::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_lhs::a_is_not_abstract():
    assert not inspect.isabstract(LHS::A)


def test_lhs::a_constructor_exists():
    assert callable(LHS::A.__init__)


def test_lhs::a_constructor_args():
    sig = inspect.signature(LHS::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lhs::a_has_name():
    assert hasattr(LHS::A, "name")
    descriptor = None
    for klass in LHS::A.__mro__:
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
LHS::D_strategy = st.builds(
    LHS::D,
    name=
        safe_text
)
LHS::C_strategy = st.builds(
    LHS::C,
    name=
        safe_text
)
LHS::B_strategy = st.builds(
    LHS::B,
    name=
        safe_text
)
LHS::A_strategy = st.builds(
    LHS::A,
    name=
        safe_text
)

@given(instance=LHS::D_strategy)
@settings(max_examples=50)
def test_lhs::d_instantiation(instance):
    assert isinstance(instance, LHS::D)

@given(instance=LHS::D_strategy)
def test_lhs::d_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=LHS::D_strategy)
def test_lhs::d_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LHS::C_strategy)
@settings(max_examples=50)
def test_lhs::c_instantiation(instance):
    assert isinstance(instance, LHS::C)

@given(instance=LHS::C_strategy)
def test_lhs::c_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=LHS::C_strategy)
def test_lhs::c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LHS::B_strategy)
@settings(max_examples=50)
def test_lhs::b_instantiation(instance):
    assert isinstance(instance, LHS::B)

@given(instance=LHS::B_strategy)
def test_lhs::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=LHS::B_strategy)
def test_lhs::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LHS::A_strategy)
@settings(max_examples=50)
def test_lhs::a_instantiation(instance):
    assert isinstance(instance, LHS::A)

@given(instance=LHS::A_strategy)
def test_lhs::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=LHS::A_strategy)
def test_lhs::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
