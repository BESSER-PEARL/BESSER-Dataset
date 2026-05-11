import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeA::B,
    TypeA::A,
    TypeA::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea::b_is_not_abstract():
    assert not inspect.isabstract(TypeA::B)


def test_typea::b_constructor_exists():
    assert callable(TypeA::B.__init__)


def test_typea::b_constructor_args():
    sig = inspect.signature(TypeA::B.__init__)
    params = list(sig.parameters.keys())
    assert "description1" in params, "Missing parameter 'description1'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description2" in params, "Missing parameter 'description2'"
    assert "description3" in params, "Missing parameter 'description3'"

def test_typea::b_has_description1():
    assert hasattr(TypeA::B, "description1")
    descriptor = None
    for klass in TypeA::B.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)

def test_typea::b_has_name():
    assert hasattr(TypeA::B, "name")
    descriptor = None
    for klass in TypeA::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typea::b_has_description2():
    assert hasattr(TypeA::B, "description2")
    descriptor = None
    for klass in TypeA::B.__mro__:
        if "description2" in klass.__dict__:
            descriptor = klass.__dict__["description2"]
            break
    assert isinstance(descriptor, property)

def test_typea::b_has_description3():
    assert hasattr(TypeA::B, "description3")
    descriptor = None
    for klass in TypeA::B.__mro__:
        if "description3" in klass.__dict__:
            descriptor = klass.__dict__["description3"]
            break
    assert isinstance(descriptor, property)



def test_typea::a_is_not_abstract():
    assert not inspect.isabstract(TypeA::A)


def test_typea::a_constructor_exists():
    assert callable(TypeA::A.__init__)


def test_typea::a_constructor_args():
    sig = inspect.signature(TypeA::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typea::a_has_name():
    assert hasattr(TypeA::A, "name")
    descriptor = None
    for klass in TypeA::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typea::c_is_not_abstract():
    assert not inspect.isabstract(TypeA::C)


def test_typea::c_constructor_exists():
    assert callable(TypeA::C.__init__)


def test_typea::c_constructor_args():
    sig = inspect.signature(TypeA::C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description1" in params, "Missing parameter 'description1'"
    assert "description2" in params, "Missing parameter 'description2'"

def test_typea::c_has_name():
    assert hasattr(TypeA::C, "name")
    descriptor = None
    for klass in TypeA::C.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typea::c_has_description1():
    assert hasattr(TypeA::C, "description1")
    descriptor = None
    for klass in TypeA::C.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)

def test_typea::c_has_description2():
    assert hasattr(TypeA::C, "description2")
    descriptor = None
    for klass in TypeA::C.__mro__:
        if "description2" in klass.__dict__:
            descriptor = klass.__dict__["description2"]
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
TypeA::B_strategy = st.builds(
    TypeA::B,
    description1=
        safe_text,
    name=
        safe_text,
    description2=
        safe_text,
    description3=
        safe_text
)
TypeA::A_strategy = st.builds(
    TypeA::A,
    name=
        safe_text
)
TypeA::C_strategy = st.builds(
    TypeA::C,
    name=
        safe_text,
    description1=
        safe_text,
    description2=
        safe_text
)

@given(instance=TypeA::B_strategy)
@settings(max_examples=50)
def test_typea::b_instantiation(instance):
    assert isinstance(instance, TypeA::B)

@given(instance=TypeA::B_strategy)
def test_typea::b_description1_type(instance):
    assert isinstance(instance.description1, str)


@given(instance=TypeA::B_strategy)
def test_typea::b_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original

@given(instance=TypeA::B_strategy)
def test_typea::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeA::B_strategy)
def test_typea::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeA::B_strategy)
def test_typea::b_description2_type(instance):
    assert isinstance(instance.description2, str)


@given(instance=TypeA::B_strategy)
def test_typea::b_description2_setter(instance):
    original = instance.description2
    instance.description2 = original
    assert instance.description2 == original

@given(instance=TypeA::B_strategy)
def test_typea::b_description3_type(instance):
    assert isinstance(instance.description3, str)


@given(instance=TypeA::B_strategy)
def test_typea::b_description3_setter(instance):
    original = instance.description3
    instance.description3 = original
    assert instance.description3 == original

@given(instance=TypeA::A_strategy)
@settings(max_examples=50)
def test_typea::a_instantiation(instance):
    assert isinstance(instance, TypeA::A)

@given(instance=TypeA::A_strategy)
def test_typea::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeA::A_strategy)
def test_typea::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeA::C_strategy)
@settings(max_examples=50)
def test_typea::c_instantiation(instance):
    assert isinstance(instance, TypeA::C)

@given(instance=TypeA::C_strategy)
def test_typea::c_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeA::C_strategy)
def test_typea::c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeA::C_strategy)
def test_typea::c_description1_type(instance):
    assert isinstance(instance.description1, str)


@given(instance=TypeA::C_strategy)
def test_typea::c_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original

@given(instance=TypeA::C_strategy)
def test_typea::c_description2_type(instance):
    assert isinstance(instance.description2, str)


@given(instance=TypeA::C_strategy)
def test_typea::c_description2_setter(instance):
    original = instance.description2
    instance.description2 = original
    assert instance.description2 == original
