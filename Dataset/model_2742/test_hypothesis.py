import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypeA_B,
    TypeA_A,
    TypeA_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typea_b_is_not_abstract():
    assert not inspect.isabstract(TypeA_B)


def test_typea_b_constructor_exists():
    assert callable(TypeA_B.__init__)


def test_typea_b_constructor_args():
    sig = inspect.signature(TypeA_B.__init__)
    params = list(sig.parameters.keys())
    assert "description3" in params, "Missing parameter 'description3'"
    assert "description2" in params, "Missing parameter 'description2'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description1" in params, "Missing parameter 'description1'"

def test_typea_b_has_description3():
    assert hasattr(TypeA_B, "description3")
    descriptor = None
    for klass in TypeA_B.__mro__:
        if "description3" in klass.__dict__:
            descriptor = klass.__dict__["description3"]
            break
    assert isinstance(descriptor, property)

def test_typea_b_has_description2():
    assert hasattr(TypeA_B, "description2")
    descriptor = None
    for klass in TypeA_B.__mro__:
        if "description2" in klass.__dict__:
            descriptor = klass.__dict__["description2"]
            break
    assert isinstance(descriptor, property)

def test_typea_b_has_name():
    assert hasattr(TypeA_B, "name")
    descriptor = None
    for klass in TypeA_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typea_b_has_description1():
    assert hasattr(TypeA_B, "description1")
    descriptor = None
    for klass in TypeA_B.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)



def test_typea_a_is_not_abstract():
    assert not inspect.isabstract(TypeA_A)


def test_typea_a_constructor_exists():
    assert callable(TypeA_A.__init__)


def test_typea_a_constructor_args():
    sig = inspect.signature(TypeA_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typea_a_has_name():
    assert hasattr(TypeA_A, "name")
    descriptor = None
    for klass in TypeA_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typea_c_is_not_abstract():
    assert not inspect.isabstract(TypeA_C)


def test_typea_c_constructor_exists():
    assert callable(TypeA_C.__init__)


def test_typea_c_constructor_args():
    sig = inspect.signature(TypeA_C.__init__)
    params = list(sig.parameters.keys())
    assert "description2" in params, "Missing parameter 'description2'"
    assert "description1" in params, "Missing parameter 'description1'"
    assert "name" in params, "Missing parameter 'name'"

def test_typea_c_has_description2():
    assert hasattr(TypeA_C, "description2")
    descriptor = None
    for klass in TypeA_C.__mro__:
        if "description2" in klass.__dict__:
            descriptor = klass.__dict__["description2"]
            break
    assert isinstance(descriptor, property)

def test_typea_c_has_description1():
    assert hasattr(TypeA_C, "description1")
    descriptor = None
    for klass in TypeA_C.__mro__:
        if "description1" in klass.__dict__:
            descriptor = klass.__dict__["description1"]
            break
    assert isinstance(descriptor, property)

def test_typea_c_has_name():
    assert hasattr(TypeA_C, "name")
    descriptor = None
    for klass in TypeA_C.__mro__:
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
TypeA_B_strategy = st.builds(
    TypeA_B,
    description3=
        safe_text,
    description2=
        safe_text,
    name=
        safe_text,
    description1=
        safe_text
)
TypeA_A_strategy = st.builds(
    TypeA_A,
    name=
        safe_text
)
TypeA_C_strategy = st.builds(
    TypeA_C,
    description2=
        safe_text,
    description1=
        safe_text,
    name=
        safe_text
)

@given(instance=TypeA_B_strategy)
@settings(max_examples=50)
def test_typea_b_instantiation(instance):
    assert isinstance(instance, TypeA_B)



@given(instance=TypeA_B_strategy)
def test_typea_b_description3_setter(instance):
    original = instance.description3
    instance.description3 = original
    assert instance.description3 == original



@given(instance=TypeA_B_strategy)
def test_typea_b_description2_setter(instance):
    original = instance.description2
    instance.description2 = original
    assert instance.description2 == original



@given(instance=TypeA_B_strategy)
def test_typea_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=TypeA_B_strategy)
def test_typea_b_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original

@given(instance=TypeA_A_strategy)
@settings(max_examples=50)
def test_typea_a_instantiation(instance):
    assert isinstance(instance, TypeA_A)



@given(instance=TypeA_A_strategy)
def test_typea_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeA_C_strategy)
@settings(max_examples=50)
def test_typea_c_instantiation(instance):
    assert isinstance(instance, TypeA_C)



@given(instance=TypeA_C_strategy)
def test_typea_c_description2_setter(instance):
    original = instance.description2
    instance.description2 = original
    assert instance.description2 == original



@given(instance=TypeA_C_strategy)
def test_typea_c_description1_setter(instance):
    original = instance.description1
    instance.description1 = original
    assert instance.description1 == original



@given(instance=TypeA_C_strategy)
def test_typea_c_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
