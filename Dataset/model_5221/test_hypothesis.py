import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    anytype::EObject,
    anytype::TestAny,
    anytype::C,
    anytype::B,
    anytype::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_anytype::eobject_is_not_abstract():
    assert not inspect.isabstract(anytype::EObject)


def test_anytype::eobject_constructor_exists():
    assert callable(anytype::EObject.__init__)


def test_anytype::eobject_constructor_args():
    sig = inspect.signature(anytype::EObject.__init__)
    params = list(sig.parameters.keys())



def test_anytype::testany_is_not_abstract():
    assert not inspect.isabstract(anytype::TestAny)


def test_anytype::testany_constructor_exists():
    assert callable(anytype::TestAny.__init__)


def test_anytype::testany_constructor_args():
    sig = inspect.signature(anytype::TestAny.__init__)
    params = list(sig.parameters.keys())
    assert "myAny" in params, "Missing parameter 'myAny'"
    assert "a" in params, "Missing parameter 'a'"
    assert "name" in params, "Missing parameter 'name'"
    assert "any" in params, "Missing parameter 'any'"

def test_anytype::testany_has_myAny():
    assert hasattr(anytype::TestAny, "myAny")
    descriptor = None
    for klass in anytype::TestAny.__mro__:
        if "myAny" in klass.__dict__:
            descriptor = klass.__dict__["myAny"]
            break
    assert isinstance(descriptor, property)

def test_anytype::testany_has_a():
    assert hasattr(anytype::TestAny, "a")
    descriptor = None
    for klass in anytype::TestAny.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_anytype::testany_has_name():
    assert hasattr(anytype::TestAny, "name")
    descriptor = None
    for klass in anytype::TestAny.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_anytype::testany_has_any():
    assert hasattr(anytype::TestAny, "any")
    descriptor = None
    for klass in anytype::TestAny.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_anytype::c_is_not_abstract():
    assert not inspect.isabstract(anytype::C)


def test_anytype::c_constructor_exists():
    assert callable(anytype::C.__init__)


def test_anytype::c_constructor_args():
    sig = inspect.signature(anytype::C.__init__)
    params = list(sig.parameters.keys())



def test_anytype::b_is_not_abstract():
    assert not inspect.isabstract(anytype::B)


def test_anytype::b_constructor_exists():
    assert callable(anytype::B.__init__)


def test_anytype::b_constructor_args():
    sig = inspect.signature(anytype::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_anytype::b_has_name():
    assert hasattr(anytype::B, "name")
    descriptor = None
    for klass in anytype::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_anytype::a_is_not_abstract():
    assert not inspect.isabstract(anytype::A)


def test_anytype::a_constructor_exists():
    assert callable(anytype::A.__init__)


def test_anytype::a_constructor_args():
    sig = inspect.signature(anytype::A.__init__)
    params = list(sig.parameters.keys())
    assert "doub" in params, "Missing parameter 'doub'"
    assert "lon" in params, "Missing parameter 'lon'"
    assert "name" in params, "Missing parameter 'name'"

def test_anytype::a_has_doub():
    assert hasattr(anytype::A, "doub")
    descriptor = None
    for klass in anytype::A.__mro__:
        if "doub" in klass.__dict__:
            descriptor = klass.__dict__["doub"]
            break
    assert isinstance(descriptor, property)

def test_anytype::a_has_lon():
    assert hasattr(anytype::A, "lon")
    descriptor = None
    for klass in anytype::A.__mro__:
        if "lon" in klass.__dict__:
            descriptor = klass.__dict__["lon"]
            break
    assert isinstance(descriptor, property)

def test_anytype::a_has_name():
    assert hasattr(anytype::A, "name")
    descriptor = None
    for klass in anytype::A.__mro__:
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
anytype::EObject_strategy = st.builds(
    anytype::EObject,
)
anytype::TestAny_strategy = st.builds(
    anytype::TestAny,
    myAny=
        safe_text,
    a=
        safe_text,
    name=
        safe_text,
    any=
        safe_text
)
anytype::C_strategy = st.builds(
    anytype::C,
)
anytype::B_strategy = st.builds(
    anytype::B,
    name=
        safe_text
)
anytype::A_strategy = st.builds(
    anytype::A,
    doub=
        safe_text,
    lon=
        safe_text,
    name=
        safe_text
)

@given(instance=anytype::EObject_strategy)
@settings(max_examples=50)
def test_anytype::eobject_instantiation(instance):
    assert isinstance(instance, anytype::EObject)

@given(instance=anytype::TestAny_strategy)
@settings(max_examples=50)
def test_anytype::testany_instantiation(instance):
    assert isinstance(instance, anytype::TestAny)

@given(instance=anytype::TestAny_strategy)
def test_anytype::testany_myAny_type(instance):
    assert isinstance(instance.myAny, str)


@given(instance=anytype::TestAny_strategy)
def test_anytype::testany_myAny_setter(instance):
    original = instance.myAny
    instance.myAny = original
    assert instance.myAny == original

@given(instance=anytype::TestAny_strategy)
def test_anytype::testany_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=anytype::TestAny_strategy)
def test_anytype::testany_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=anytype::TestAny_strategy)
def test_anytype::testany_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=anytype::TestAny_strategy)
def test_anytype::testany_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=anytype::TestAny_strategy)
def test_anytype::testany_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=anytype::TestAny_strategy)
def test_anytype::testany_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=anytype::C_strategy)
@settings(max_examples=50)
def test_anytype::c_instantiation(instance):
    assert isinstance(instance, anytype::C)

@given(instance=anytype::B_strategy)
@settings(max_examples=50)
def test_anytype::b_instantiation(instance):
    assert isinstance(instance, anytype::B)

@given(instance=anytype::B_strategy)
def test_anytype::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=anytype::B_strategy)
def test_anytype::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=anytype::A_strategy)
@settings(max_examples=50)
def test_anytype::a_instantiation(instance):
    assert isinstance(instance, anytype::A)

@given(instance=anytype::A_strategy)
def test_anytype::a_doub_type(instance):
    assert isinstance(instance.doub, str)


@given(instance=anytype::A_strategy)
def test_anytype::a_doub_setter(instance):
    original = instance.doub
    instance.doub = original
    assert instance.doub == original

@given(instance=anytype::A_strategy)
def test_anytype::a_lon_type(instance):
    assert isinstance(instance.lon, str)


@given(instance=anytype::A_strategy)
def test_anytype::a_lon_setter(instance):
    original = instance.lon
    instance.lon = original
    assert instance.lon == original

@given(instance=anytype::A_strategy)
def test_anytype::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=anytype::A_strategy)
def test_anytype::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
