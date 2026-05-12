import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    anytype_EObject,
    anytype_TestAny,
    anytype_C,
    anytype_B,
    anytype_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_anytype_eobject_is_not_abstract():
    assert not inspect.isabstract(anytype_EObject)


def test_anytype_eobject_constructor_exists():
    assert callable(anytype_EObject.__init__)


def test_anytype_eobject_constructor_args():
    sig = inspect.signature(anytype_EObject.__init__)
    params = list(sig.parameters.keys())



def test_anytype_testany_is_not_abstract():
    assert not inspect.isabstract(anytype_TestAny)


def test_anytype_testany_constructor_exists():
    assert callable(anytype_TestAny.__init__)


def test_anytype_testany_constructor_args():
    sig = inspect.signature(anytype_TestAny.__init__)
    params = list(sig.parameters.keys())
    assert "any" in params, "Missing parameter 'any'"
    assert "name" in params, "Missing parameter 'name'"
    assert "myAny" in params, "Missing parameter 'myAny'"
    assert "a" in params, "Missing parameter 'a'"

def test_anytype_testany_has_any():
    assert hasattr(anytype_TestAny, "any")
    descriptor = None
    for klass in anytype_TestAny.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_anytype_testany_has_name():
    assert hasattr(anytype_TestAny, "name")
    descriptor = None
    for klass in anytype_TestAny.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_anytype_testany_has_myAny():
    assert hasattr(anytype_TestAny, "myAny")
    descriptor = None
    for klass in anytype_TestAny.__mro__:
        if "myAny" in klass.__dict__:
            descriptor = klass.__dict__["myAny"]
            break
    assert isinstance(descriptor, property)

def test_anytype_testany_has_a():
    assert hasattr(anytype_TestAny, "a")
    descriptor = None
    for klass in anytype_TestAny.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_anytype_c_is_not_abstract():
    assert not inspect.isabstract(anytype_C)


def test_anytype_c_constructor_exists():
    assert callable(anytype_C.__init__)


def test_anytype_c_constructor_args():
    sig = inspect.signature(anytype_C.__init__)
    params = list(sig.parameters.keys())



def test_anytype_b_is_not_abstract():
    assert not inspect.isabstract(anytype_B)


def test_anytype_b_constructor_exists():
    assert callable(anytype_B.__init__)


def test_anytype_b_constructor_args():
    sig = inspect.signature(anytype_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_anytype_b_has_name():
    assert hasattr(anytype_B, "name")
    descriptor = None
    for klass in anytype_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_anytype_a_is_not_abstract():
    assert not inspect.isabstract(anytype_A)


def test_anytype_a_constructor_exists():
    assert callable(anytype_A.__init__)


def test_anytype_a_constructor_args():
    sig = inspect.signature(anytype_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "doub" in params, "Missing parameter 'doub'"
    assert "lon" in params, "Missing parameter 'lon'"

def test_anytype_a_has_name():
    assert hasattr(anytype_A, "name")
    descriptor = None
    for klass in anytype_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_anytype_a_has_doub():
    assert hasattr(anytype_A, "doub")
    descriptor = None
    for klass in anytype_A.__mro__:
        if "doub" in klass.__dict__:
            descriptor = klass.__dict__["doub"]
            break
    assert isinstance(descriptor, property)

def test_anytype_a_has_lon():
    assert hasattr(anytype_A, "lon")
    descriptor = None
    for klass in anytype_A.__mro__:
        if "lon" in klass.__dict__:
            descriptor = klass.__dict__["lon"]
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
anytype_EObject_strategy = st.builds(
    anytype_EObject,
)
anytype_TestAny_strategy = st.builds(
    anytype_TestAny,
    any=
        safe_text,
    name=
        safe_text,
    myAny=
        safe_text,
    a=
        safe_text
)
anytype_C_strategy = st.builds(
    anytype_C,
)
anytype_B_strategy = st.builds(
    anytype_B,
    name=
        safe_text
)
anytype_A_strategy = st.builds(
    anytype_A,
    name=
        safe_text,
    doub=
        safe_text,
    lon=
        safe_text
)

@given(instance=anytype_EObject_strategy)
@settings(max_examples=50)
def test_anytype_eobject_instantiation(instance):
    assert isinstance(instance, anytype_EObject)

@given(instance=anytype_TestAny_strategy)
@settings(max_examples=50)
def test_anytype_testany_instantiation(instance):
    assert isinstance(instance, anytype_TestAny)



@given(instance=anytype_TestAny_strategy)
def test_anytype_testany_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=anytype_TestAny_strategy)
def test_anytype_testany_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=anytype_TestAny_strategy)
def test_anytype_testany_myAny_setter(instance):
    original = instance.myAny
    instance.myAny = original
    assert instance.myAny == original



@given(instance=anytype_TestAny_strategy)
def test_anytype_testany_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=anytype_C_strategy)
@settings(max_examples=50)
def test_anytype_c_instantiation(instance):
    assert isinstance(instance, anytype_C)

@given(instance=anytype_B_strategy)
@settings(max_examples=50)
def test_anytype_b_instantiation(instance):
    assert isinstance(instance, anytype_B)



@given(instance=anytype_B_strategy)
def test_anytype_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=anytype_A_strategy)
@settings(max_examples=50)
def test_anytype_a_instantiation(instance):
    assert isinstance(instance, anytype_A)



@given(instance=anytype_A_strategy)
def test_anytype_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=anytype_A_strategy)
def test_anytype_a_doub_setter(instance):
    original = instance.doub
    instance.doub = original
    assert instance.doub == original



@given(instance=anytype_A_strategy)
def test_anytype_a_lon_setter(instance):
    original = instance.lon
    instance.lon = original
    assert instance.lon == original
