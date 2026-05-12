import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeD_BElementName,
    TypeD_AElementName,
    TypeD_C,
    TypeD_B,
    TypeD_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typed_belementname_is_not_abstract():
    assert not inspect.isabstract(TypeD_BElementName)


def test_typed_belementname_constructor_exists():
    assert callable(TypeD_BElementName.__init__)


def test_typed_belementname_constructor_args():
    sig = inspect.signature(TypeD_BElementName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed_belementname_has_name():
    assert hasattr(TypeD_BElementName, "name")
    descriptor = None
    for klass in TypeD_BElementName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typed_aelementname_is_not_abstract():
    assert not inspect.isabstract(TypeD_AElementName)


def test_typed_aelementname_constructor_exists():
    assert callable(TypeD_AElementName.__init__)


def test_typed_aelementname_constructor_args():
    sig = inspect.signature(TypeD_AElementName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed_aelementname_has_name():
    assert hasattr(TypeD_AElementName, "name")
    descriptor = None
    for klass in TypeD_AElementName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typed_c_is_not_abstract():
    assert not inspect.isabstract(TypeD_C)


def test_typed_c_constructor_exists():
    assert callable(TypeD_C.__init__)


def test_typed_c_constructor_args():
    sig = inspect.signature(TypeD_C.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed_c_has_name():
    assert hasattr(TypeD_C, "name")
    descriptor = None
    for klass in TypeD_C.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typed_b_is_not_abstract():
    assert not inspect.isabstract(TypeD_B)


def test_typed_b_constructor_exists():
    assert callable(TypeD_B.__init__)


def test_typed_b_constructor_args():
    sig = inspect.signature(TypeD_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed_b_has_name():
    assert hasattr(TypeD_B, "name")
    descriptor = None
    for klass in TypeD_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typed_a_is_not_abstract():
    assert not inspect.isabstract(TypeD_A)


def test_typed_a_constructor_exists():
    assert callable(TypeD_A.__init__)


def test_typed_a_constructor_args():
    sig = inspect.signature(TypeD_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typed_a_has_name():
    assert hasattr(TypeD_A, "name")
    descriptor = None
    for klass in TypeD_A.__mro__:
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
TypeD_BElementName_strategy = st.builds(
    TypeD_BElementName,
    name=
        safe_text
)
TypeD_AElementName_strategy = st.builds(
    TypeD_AElementName,
    name=
        safe_text
)
TypeD_C_strategy = st.builds(
    TypeD_C,
    name=
        safe_text
)
TypeD_B_strategy = st.builds(
    TypeD_B,
    name=
        safe_text
)
TypeD_A_strategy = st.builds(
    TypeD_A,
    name=
        safe_text
)

@given(instance=TypeD_BElementName_strategy)
@settings(max_examples=50)
def test_typed_belementname_instantiation(instance):
    assert isinstance(instance, TypeD_BElementName)



@given(instance=TypeD_BElementName_strategy)
def test_typed_belementname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeD_AElementName_strategy)
@settings(max_examples=50)
def test_typed_aelementname_instantiation(instance):
    assert isinstance(instance, TypeD_AElementName)



@given(instance=TypeD_AElementName_strategy)
def test_typed_aelementname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeD_C_strategy)
@settings(max_examples=50)
def test_typed_c_instantiation(instance):
    assert isinstance(instance, TypeD_C)



@given(instance=TypeD_C_strategy)
def test_typed_c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeD_B_strategy)
@settings(max_examples=50)
def test_typed_b_instantiation(instance):
    assert isinstance(instance, TypeD_B)



@given(instance=TypeD_B_strategy)
def test_typed_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeD_A_strategy)
@settings(max_examples=50)
def test_typed_a_instantiation(instance):
    assert isinstance(instance, TypeD_A)



@given(instance=TypeD_A_strategy)
def test_typed_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
