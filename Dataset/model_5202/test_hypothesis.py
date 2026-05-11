import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TypeD::BElementName,
    TypeD::AElementName,
    TypeD::C,
    TypeD::B,
    TypeD::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typed::belementname_is_not_abstract():
    assert not inspect.isabstract(TypeD::BElementName)


def test_typed::belementname_constructor_exists():
    assert callable(TypeD::BElementName.__init__)


def test_typed::belementname_constructor_args():
    sig = inspect.signature(TypeD::BElementName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed::belementname_has_name():
    assert hasattr(TypeD::BElementName, "name")
    descriptor = None
    for klass in TypeD::BElementName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typed::aelementname_is_not_abstract():
    assert not inspect.isabstract(TypeD::AElementName)


def test_typed::aelementname_constructor_exists():
    assert callable(TypeD::AElementName.__init__)


def test_typed::aelementname_constructor_args():
    sig = inspect.signature(TypeD::AElementName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed::aelementname_has_name():
    assert hasattr(TypeD::AElementName, "name")
    descriptor = None
    for klass in TypeD::AElementName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typed::c_is_not_abstract():
    assert not inspect.isabstract(TypeD::C)


def test_typed::c_constructor_exists():
    assert callable(TypeD::C.__init__)


def test_typed::c_constructor_args():
    sig = inspect.signature(TypeD::C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed::c_has_name():
    assert hasattr(TypeD::C, "name")
    descriptor = None
    for klass in TypeD::C.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typed::b_is_not_abstract():
    assert not inspect.isabstract(TypeD::B)


def test_typed::b_constructor_exists():
    assert callable(TypeD::B.__init__)


def test_typed::b_constructor_args():
    sig = inspect.signature(TypeD::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed::b_has_name():
    assert hasattr(TypeD::B, "name")
    descriptor = None
    for klass in TypeD::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typed::a_is_not_abstract():
    assert not inspect.isabstract(TypeD::A)


def test_typed::a_constructor_exists():
    assert callable(TypeD::A.__init__)


def test_typed::a_constructor_args():
    sig = inspect.signature(TypeD::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed::a_has_name():
    assert hasattr(TypeD::A, "name")
    descriptor = None
    for klass in TypeD::A.__mro__:
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
TypeD::BElementName_strategy = st.builds(
    TypeD::BElementName,
    name=
        safe_text
)
TypeD::AElementName_strategy = st.builds(
    TypeD::AElementName,
    name=
        safe_text
)
TypeD::C_strategy = st.builds(
    TypeD::C,
    name=
        safe_text
)
TypeD::B_strategy = st.builds(
    TypeD::B,
    name=
        safe_text
)
TypeD::A_strategy = st.builds(
    TypeD::A,
    name=
        safe_text
)

@given(instance=TypeD::BElementName_strategy)
@settings(max_examples=50)
def test_typed::belementname_instantiation(instance):
    assert isinstance(instance, TypeD::BElementName)

@given(instance=TypeD::BElementName_strategy)
def test_typed::belementname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeD::BElementName_strategy)
def test_typed::belementname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeD::AElementName_strategy)
@settings(max_examples=50)
def test_typed::aelementname_instantiation(instance):
    assert isinstance(instance, TypeD::AElementName)

@given(instance=TypeD::AElementName_strategy)
def test_typed::aelementname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeD::AElementName_strategy)
def test_typed::aelementname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeD::C_strategy)
@settings(max_examples=50)
def test_typed::c_instantiation(instance):
    assert isinstance(instance, TypeD::C)

@given(instance=TypeD::C_strategy)
def test_typed::c_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeD::C_strategy)
def test_typed::c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeD::B_strategy)
@settings(max_examples=50)
def test_typed::b_instantiation(instance):
    assert isinstance(instance, TypeD::B)

@given(instance=TypeD::B_strategy)
def test_typed::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeD::B_strategy)
def test_typed::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeD::A_strategy)
@settings(max_examples=50)
def test_typed::a_instantiation(instance):
    assert isinstance(instance, TypeD::A)

@given(instance=TypeD::A_strategy)
def test_typed::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=TypeD::A_strategy)
def test_typed::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
