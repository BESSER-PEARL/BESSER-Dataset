import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeB::A,
    TypeB::C,
    TypeB::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typeb::a_is_not_abstract():
    assert not inspect.isabstract(TypeB::A)


def test_typeb::a_constructor_exists():
    assert callable(TypeB::A.__init__)


def test_typeb::a_constructor_args():
    sig = inspect.signature(TypeB::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb::a_has_name():
    assert hasattr(TypeB::A, "name")
    descriptor = None
    for klass in TypeB::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb::c_is_not_abstract():
    assert not inspect.isabstract(TypeB::C)


def test_typeb::c_constructor_exists():
    assert callable(TypeB::C.__init__)


def test_typeb::c_constructor_args():
    sig = inspect.signature(TypeB::C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb::c_has_name():
    assert hasattr(TypeB::C, "name")
    descriptor = None
    for klass in TypeB::C.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typeb::b_is_not_abstract():
    assert not inspect.isabstract(TypeB::B)


def test_typeb::b_constructor_exists():
    assert callable(TypeB::B.__init__)


def test_typeb::b_constructor_args():
    sig = inspect.signature(TypeB::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typeb::b_has_name():
    assert hasattr(TypeB::B, "name")
    descriptor = None
    for klass in TypeB::B.__mro__:
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
TypeB::A_strategy = st.builds(
    TypeB::A,
    name=
        safe_text
)
TypeB::C_strategy = st.builds(
    TypeB::C,
    name=
        safe_text
)
TypeB::B_strategy = st.builds(
    TypeB::B,
    name=
        safe_text
)

@given(instance=TypeB::A_strategy)
@settings(max_examples=50)
def test_typeb::a_instantiation(instance):
    assert isinstance(instance, TypeB::A)

@given(instance=TypeB::A_strategy)
def test_typeb::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeB::A_strategy)
def test_typeb::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeB::C_strategy)
@settings(max_examples=50)
def test_typeb::c_instantiation(instance):
    assert isinstance(instance, TypeB::C)

@given(instance=TypeB::C_strategy)
def test_typeb::c_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeB::C_strategy)
def test_typeb::c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeB::B_strategy)
@settings(max_examples=50)
def test_typeb::b_instantiation(instance):
    assert isinstance(instance, TypeB::B)

@given(instance=TypeB::B_strategy)
def test_typeb::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeB::B_strategy)
def test_typeb::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
